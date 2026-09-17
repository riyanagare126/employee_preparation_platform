import os
import sqlite3
import json
import time
from werkzeug.security import generate_password_hash

# Path to the SQLite database
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "employees.db")


class PostgresRowWrapper:
    """Provides SQLite Row-like dictionary and index access to PostgreSQL rows."""
    def __init__(self, data_dict, description=None):
        self._dict = dict(data_dict) if isinstance(data_dict, dict) else {}
        self._list = list(data_dict.values()) if isinstance(data_dict, dict) else list(data_dict)
        if description and not self._dict:
            for idx, col in enumerate(description):
                self._dict[col.name] = self._list[idx]

    def __getitem__(self, key):
        if isinstance(key, int):
            return self._list[key]
        return self._dict.get(key)

    def get(self, key, default=None):
        return self._dict.get(key, default)

    def keys(self):
        return self._dict.keys()

    def values(self):
        return self._dict.values()

    def items(self):
        return self._dict.items()

    def __contains__(self, key):
        return key in self._dict

    def __iter__(self):
        return iter(self._list)

    def __repr__(self):
        return f"<PostgresRow {self._dict}>"


class PostgresCursorWrapper:
    """Wraps psycopg2 cursor to provide SQLite-compatible ? placeholder translation."""
    def __init__(self, real_cursor):
        self._cur = real_cursor
        self.lastrowid = None

    def execute(self, query, params=None):
        pg_query = query.replace("?", "%s")
        if pg_query.strip().upper().startswith("PRAGMA"):
            return self

        is_insert = pg_query.strip().upper().startswith("INSERT INTO")
        if params is not None:
            if isinstance(params, (list, tuple)):
                self._cur.execute(pg_query, tuple(params))
            else:
                self._cur.execute(pg_query, params)
        else:
            self._cur.execute(pg_query)

        if is_insert:
            try:
                self._cur.execute("SELECT LASTVAL();")
                row = self._cur.fetchone()
                if row:
                    self.lastrowid = list(row.values())[0] if isinstance(row, dict) else row[0]
            except Exception:
                pass
        return self

    def executemany(self, query, seq_of_params):
        pg_query = query.replace("?", "%s")
        return self._cur.executemany(pg_query, seq_of_params)

    def fetchone(self):
        row = self._cur.fetchone()
        if row is None:
            return None
        return PostgresRowWrapper(row, self._cur.description)

    def fetchall(self):
        rows = self._cur.fetchall()
        if not rows:
            return []
        desc = self._cur.description
        return [PostgresRowWrapper(r, desc) for r in rows]

    def fetchmany(self, size=None):
        rows = self._cur.fetchmany(size) if size else self._cur.fetchmany()
        desc = self._cur.description
        return [PostgresRowWrapper(r, desc) for r in rows]

    @property
    def rowcount(self):
        return self._cur.rowcount

    @property
    def description(self):
        return self._cur.description

    def close(self):
        try:
            self._cur.close()
        except Exception:
            pass


class PostgresConnectionWrapper:
    """Wraps psycopg2 connection to mirror SQLite interface."""
    def __init__(self, pg_conn):
        self._conn = pg_conn
        self.row_factory = None

    def cursor(self):
        import psycopg2.extras
        cur = self._conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        return PostgresCursorWrapper(cur)

    def commit(self):
        self._conn.commit()

    def rollback(self):
        self._conn.rollback()

    def close(self):
        self._conn.close()

    def execute(self, query, params=None):
        cur = self.cursor()
        cur.execute(query, params)
        return cur


def get_db_connection():
    """
    Establish a connection to the database.
    If DATABASE_URL is defined (e.g. Supabase PostgreSQL), connects via psycopg2.
    Otherwise, falls back to local SQLite database with Row factory.
    """
    raw_url = os.getenv("DATABASE_URL")
    if raw_url and (raw_url.startswith("postgresql://") or raw_url.startswith("postgres://")):
        import psycopg2
        pg_url = raw_url.replace("postgres://", "postgresql://", 1)
        conn = psycopg2.connect(pg_url)
        return PostgresConnectionWrapper(conn)

    # Local SQLite Fallback
    if not os.path.exists(DB_DIR):
        os.makedirs(DB_DIR, exist_ok=True)
        
    conn = sqlite3.connect(DB_PATH, timeout=30.0)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn


def init_db():
    """
    Initialize all database tables with parameterized schemas and default seeds.
    Supports both Supabase PostgreSQL (via supabase_schema.sql) and SQLite.
    """
    raw_url = os.getenv("DATABASE_URL")
    if raw_url and (raw_url.startswith("postgresql://") or raw_url.startswith("postgres://")):
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'employees');")
            res = cursor.fetchone()
            exists = res[0] if res else False
            if not exists:
                schema_path = os.path.join(os.path.dirname(BASE_DIR), "supabase_schema.sql")
                if os.path.exists(schema_path):
                    with open(schema_path, "r", encoding="utf-8") as f:
                        sql = f.read()
                    raw_cur = conn._conn.cursor()
                    raw_cur.execute(sql)
                    conn.commit()
                    raw_cur.close()
        except Exception as e:
            print(f"Warning initializing PostgreSQL database: {e}")
        finally:
            conn.close()
        return

    conn = get_db_connection()
    cursor = conn.cursor()

    # 1. Employees / Users Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            qualification TEXT NOT NULL,
            skills TEXT NOT NULL,
            experience TEXT NOT NULL,
            job_role TEXT NOT NULL,
            target_company TEXT DEFAULT 'Tata Consultancy Services (TCS)',
            target_role TEXT DEFAULT 'Software Engineer',
            extracted_skills_json TEXT,
            is_admin INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Safe column migrations for employees
    emp_cols = [
        ("target_company", "TEXT DEFAULT 'Tata Consultancy Services (TCS)'"),
        ("target_role", "TEXT DEFAULT 'Software Engineer'"),
        ("extracted_skills_json", "TEXT"),
        ("is_admin", "INTEGER DEFAULT 0")
    ]
    for col_name, col_type in emp_cols:
        try:
            cursor.execute(f"ALTER TABLE employees ADD COLUMN {col_name} {col_type};")
        except sqlite3.OperationalError:
            pass

    # 2. Aptitude Results Table (Legacy compatibility)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aptitude_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            score INTEGER NOT NULL,
            total INTEGER NOT NULL,
            percentage REAL NOT NULL,
            performance_message TEXT NOT NULL,
            category_breakdown TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 3. Coding Progress Table (Legacy compatibility)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS coding_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            problem_title TEXT NOT NULL,
            language TEXT NOT NULL,
            difficulty TEXT NOT NULL,
            status TEXT NOT NULL,
            code TEXT,
            completed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 4. Interview Results Table (Legacy compatibility)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS interview_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            job_role TEXT NOT NULL,
            overall_score INTEGER NOT NULL,
            technical_score INTEGER NOT NULL,
            communication_score INTEGER NOT NULL,
            feedback TEXT NOT NULL,
            answers_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 5. Resume Data Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER UNIQUE NOT NULL,
            full_name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            role TEXT,
            objective TEXT,
            qualification TEXT,
            skills TEXT,
            soft_skills TEXT,
            projects TEXT,
            internships TEXT,
            experience TEXT,
            certifications TEXT,
            achievements TEXT,
            languages TEXT,
            hobbies TEXT,
            strengths TEXT,
            extracurricular TEXT,
            github TEXT,
            linkedin TEXT,
            portfolio TEXT,
            template TEXT DEFAULT 'modern',
            sections_json TEXT,
            custom_json TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 6. Legacy Aptitude Test Sessions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aptitude_sessions (
            session_id TEXT PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            job_role TEXT,
            question_ids TEXT NOT NULL,
            options_map TEXT NOT NULL,
            total_questions INTEGER NOT NULL,
            duration_seconds INTEGER NOT NULL,
            score INTEGER,
            percentage REAL,
            performance_message TEXT,
            answers_json TEXT,
            review_json TEXT,
            status TEXT DEFAULT 'active',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            submitted_at TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 7. Secure Test Sessions Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS secure_test_sessions (
            session_id TEXT PRIMARY KEY,
            employee_id INTEGER NOT NULL,
            test_type TEXT NOT NULL,
            job_role TEXT,
            questions_json TEXT NOT NULL,
            options_map_json TEXT,
            duration_seconds INTEGER NOT NULL,
            start_epoch REAL NOT NULL,
            tab_token TEXT NOT NULL,
            status TEXT DEFAULT 'active',
            answers_json TEXT,
            score INTEGER,
            percentage REAL,
            performance_message TEXT,
            result_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            submitted_at TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 8. Aptitude Recently Served Questions
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS aptitude_recent_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            question_id INTEGER NOT NULL,
            seen_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 9. Resume Analyses Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_analyses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            overall_score INTEGER NOT NULL,
            readability_score INTEGER NOT NULL,
            relevance_score INTEGER NOT NULL,
            target_role TEXT,
            strengths_json TEXT,
            missing_json TEXT,
            keywords_json TEXT,
            suggestions_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 10. Gamification Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS gamification (
            employee_id INTEGER PRIMARY KEY,
            points INTEGER DEFAULT 0,
            level INTEGER DEFAULT 1,
            streak_days INTEGER DEFAULT 1,
            last_activity_date TEXT,
            badges_json TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 11. Learning Roadmaps Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS learning_roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            job_role TEXT NOT NULL,
            roadmap_json TEXT NOT NULL,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 12. Companies Table (company_prep)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS company_prep (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_name TEXT UNIQUE NOT NULL,
            slug TEXT UNIQUE NOT NULL,
            logo_emoji TEXT NOT NULL,
            category TEXT DEFAULT 'IT Services',
            difficulty TEXT NOT NULL,
            description TEXT,
            common_roles TEXT,
            hiring_rounds TEXT NOT NULL,
            aptitude_pattern TEXT NOT NULL,
            coding_pattern TEXT NOT NULL,
            technical_focus TEXT NOT NULL,
            hr_tips TEXT NOT NULL,
            recommended_skills TEXT,
            roadmap_json TEXT,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # Safe column migrations for company_prep
    company_cols = [
        ("category", "TEXT DEFAULT 'IT Services'"),
        ("description", "TEXT"),
        ("common_roles", "TEXT"),
        ("roadmap_json", "TEXT")
    ]
    for col_name, col_type in company_cols:
        try:
            cursor.execute(f"ALTER TABLE company_prep ADD COLUMN {col_name} {col_type};")
        except sqlite3.OperationalError:
            pass

    # 13. Job Roles Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS job_roles (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            company_id INTEGER,
            company_slug TEXT DEFAULT 'all',
            role_name TEXT NOT NULL,
            description TEXT,
            skills_required TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (company_id) REFERENCES company_prep(id) ON DELETE CASCADE
        );
    """)

    # 14. User Company Preparation Table (Tracks per-company progress independently)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS user_preparation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            company_id INTEGER,
            company_slug TEXT NOT NULL,
            company_name TEXT NOT NULL,
            role_id INTEGER,
            role_name TEXT NOT NULL,
            status TEXT DEFAULT 'in_progress',
            progress REAL DEFAULT 0.0,
            aptitude_progress REAL DEFAULT 0.0,
            coding_progress REAL DEFAULT 0.0,
            technical_progress REAL DEFAULT 0.0,
            interview_progress REAL DEFAULT 0.0,
            hr_progress REAL DEFAULT 0.0,
            resume_progress REAL DEFAULT 0.0,
            skills_progress REAL DEFAULT 0.0,
            roadmap_progress REAL DEFAULT 0.0,
            last_accessed TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES employees(id) ON DELETE CASCADE,
            UNIQUE(user_id, company_slug)
        );
    """)

    # 15. Test Attempts Table (Company-wise test results)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS test_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            company_id INTEGER,
            company_slug TEXT NOT NULL,
            role_name TEXT,
            test_type TEXT NOT NULL,
            score REAL NOT NULL,
            total REAL NOT NULL,
            percentage REAL NOT NULL,
            status TEXT DEFAULT 'completed',
            details_json TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 16. Preparation Questions Table (Admin-managed & Company-assigned questions)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS preparation_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_type TEXT NOT NULL,
            company_id INTEGER,
            company_slug TEXT DEFAULT 'all',
            role_name TEXT DEFAULT 'all',
            category TEXT NOT NULL,
            difficulty TEXT DEFAULT 'Medium',
            question TEXT NOT NULL,
            options_json TEXT,
            correct_answer TEXT,
            explanation TEXT,
            starter_code TEXT,
            expected_output TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 17. Admin Activity Log Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS admin_logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            admin_email TEXT NOT NULL,
            action TEXT NOT NULL,
            details TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 18. AI Daily Preparation Plans Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS daily_plans (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            plan_date TEXT NOT NULL,
            tasks_json TEXT NOT NULL,
            completed_tasks_json TEXT DEFAULT '[]',
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 19. Readiness History Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS readiness_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            readiness_score INTEGER NOT NULL,
            aptitude_score INTEGER NOT NULL,
            coding_score INTEGER NOT NULL,
            interview_score INTEGER NOT NULL,
            resume_score INTEGER NOT NULL,
            status_tier TEXT NOT NULL,
            recorded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 20. Trend Insights Table (2026 hiring trends curated tips)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trend_insights (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            category TEXT NOT NULL,
            role_tag TEXT DEFAULT 'All',
            company_tag TEXT DEFAULT 'All',
            content TEXT NOT NULL,
            actionable_tip TEXT NOT NULL,
            priority INTEGER DEFAULT 1,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 21. Trending Resume Templates Table (CMS-managed)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS trending_templates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            template_id TEXT UNIQUE NOT NULL,
            name TEXT NOT NULL,
            badge_text TEXT DEFAULT '🔥 Trending 2026',
            description TEXT NOT NULL,
            css_class TEXT NOT NULL,
            is_trending INTEGER DEFAULT 1,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 22. Smart Roadmaps Table (Company-specific prep roadmap)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS smart_roadmaps (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            company_name TEXT NOT NULL,
            company_slug TEXT NOT NULL,
            target_role TEXT NOT NULL,
            duration_days INTEGER NOT NULL,
            total_tasks INTEGER DEFAULT 0,
            completed_tasks INTEGER DEFAULT 0,
            progress_percent REAL DEFAULT 0.0,
            streak_days INTEGER DEFAULT 1,
            ai_notes TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 23. Roadmap Tasks Table (Day-wise checklist)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS roadmap_tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            roadmap_id INTEGER NOT NULL,
            employee_id INTEGER NOT NULL,
            day_number INTEGER NOT NULL,
            phase_name TEXT NOT NULL,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            category TEXT NOT NULL,
            estimated_minutes INTEGER DEFAULT 45,
            is_completed INTEGER DEFAULT 0,
            completed_at TIMESTAMP,
            FOREIGN KEY (roadmap_id) REFERENCES smart_roadmaps(id) ON DELETE CASCADE,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 24. Resume Versions Table (Multiple saved versions per employee_id)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS resume_versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            version_name TEXT NOT NULL,
            template_name TEXT DEFAULT 'modern-single',
            target_role TEXT,
            target_company TEXT,
            resume_data_json TEXT NOT NULL,
            score INTEGER DEFAULT 0,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 25. AI Fluency Questions Table (2026 indirect practice questions)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_fluency_questions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question_text TEXT NOT NULL,
            category TEXT NOT NULL,
            difficulty TEXT DEFAULT 'Medium',
            context_hint TEXT,
            ideal_talking_points_json TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)

    # 26. AI Fluency Attempts Table (Scored across 4 pillars with natural rewrite)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS ai_fluency_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            question_id INTEGER,
            question_text TEXT NOT NULL,
            candidate_answer TEXT NOT NULL,
            overall_score INTEGER NOT NULL,
            ai_tool_score INTEGER NOT NULL,
            verification_score INTEGER NOT NULL,
            velocity_score INTEGER NOT NULL,
            communication_score INTEGER NOT NULL,
            feedback TEXT NOT NULL,
            suggestions_json TEXT,
            rewrite_sample TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # 27. Structured Answers Table (Present-Past-Future 60s pitch answers)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS structured_answers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            employee_id INTEGER NOT NULL,
            question_key TEXT NOT NULL,
            question_title TEXT NOT NULL,
            target_role TEXT,
            target_company TEXT,
            present_text TEXT NOT NULL,
            past_text TEXT NOT NULL,
            future_text TEXT NOT NULL,
            combined_text TEXT NOT NULL,
            speaking_time_seconds INTEGER DEFAULT 60,
            word_count INTEGER DEFAULT 0,
            structure_score INTEGER DEFAULT 0,
            ai_critique TEXT,
            ai_optimized_pitch TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (employee_id) REFERENCES employees(id) ON DELETE CASCADE
        );
    """)

    # Unique Indexes
    cursor.execute("CREATE UNIQUE INDEX IF NOT EXISTS idx_user_prep_user_comp ON user_preparation(user_id, company_slug);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_test_attempts_user ON test_attempts(user_id, company_slug);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_prep_questions_type ON preparation_questions(question_type, company_slug, role_name);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_roadmap_user ON smart_roadmaps(employee_id, company_slug);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_roadmap_tasks ON roadmap_tasks(roadmap_id, day_number);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_resume_ver_user ON resume_versions(employee_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_ai_fluency_user ON ai_fluency_attempts(employee_id);")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_struct_ans_user ON structured_answers(employee_id);")

    # Seed Default Admin User if not exists
    cursor.execute("SELECT id FROM employees WHERE email = 'admin@prep.com'")
    if not cursor.fetchone():
        hashed_admin_pw = generate_password_hash("admin123")
        cursor.execute("""
            INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, 1)
        """, (
            "Platform Administrator",
            "admin@prep.com",
            hashed_admin_pw,
            "Master of Technology",
            "Full Stack, System Architecture, Management",
            "5+ Years",
            "Platform Admin",
            "Tata Consultancy Services (TCS)",
            "Software Engineer"
        ))

    # Seed 20 Top Companies Catalog
    top_20_companies = [
        (
            "Tata Consultancy Services (TCS)", "tcs", "🏢", "IT Services", "Medium",
            "Global leader in IT services, consulting, and business solutions.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (NQT) | Round 2: Technical Interview | Round 3: MR & HR",
            "Numerical Ability (20 Qs), Verbal Ability (25 Qs), Reasoning Ability (20 Qs) [Total: 75 mins]",
            "2 Coding Challenges (Arrays, Matrix, String Manipulation, Math). Languages: Java, Python, C++, C.",
            "Core Java/OOPs, SQL Joins & Aggregate Functions, Basic Data Structures (Linked List, Stack), DBMS ACID properties, Capstone Project.",
            "Familiarize yourself with TCS BaNCS and digital cloud initiatives. Highlight flexibility, teamwork, and strong work ethics.",
            "Java, Python, SQL, C++, Data Structures, DBMS, Cloud Basics",
            json.dumps(["Aptitude (NQT)", "Reasoning Ability", "Verbal Ability", "Coding Round", "Technical Interview", "Managerial & HR", "AI Mock Simulation"])
        ),
        (
            "Infosys", "infosys", "🔷", "IT Services & Consulting", "Medium-Hard",
            "Multinational information technology company specializing in digital services and consulting.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (Reasoning, Math, Verbal, Pseudocode) | Round 2: Technical + HR Interview",
            "Quantitative Aptitude (10 Qs), Logical Reasoning (15 Qs), Verbal Ability (20 Qs), Pseudocode & Puzzles (5 Qs)",
            "1 Problem on Arrays/Hashing, 1 Problem on Dynamic Programming or Greedy Algorithms.",
            "Java Collections Framework, Multithreading, REST APIs, Microservices basics, Operating Systems (Process vs Thread).",
            "Show high trainability, adaptability to Mysore DC training, and passion for continuous technology learning.",
            "Java, Python, Algorithms, DSA, SQL, Spring Boot, REST APIs",
            json.dumps(["Mathematical Thinking", "Logical Analysis", "Pseudocode Mastery", "Coding Challenges", "Technical Deep-Dive", "Behavioral Interview", "Mock Interview"])
        ),
        (
            "Wipro", "wipro", "🌐", "IT & Consulting", "Medium",
            "Leading technology services and consulting company focused on building innovative solutions.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Elite NTH (Quantitative, Logical, Verbal, Essay Writing, Coding) | Round 2: Technical Interview | Round 3: HR Interview",
            "Quantitative (16 Qs), Logical Reasoning (14 Qs), Verbal (22 Qs), Written Communication Essay (20 mins)",
            "2 Coding Questions (Mathematical algorithms, String reversal, Array frequency counting).",
            "C++/Java programming, Database management systems, Computer Networks, Software Engineering lifecycle (SDLC).",
            "Practice structured professional essay writing. Emphasize long-term commitment and client delivery excellence.",
            "C++, Java, Python, SQL, Computer Networks, SDLC",
            json.dumps(["Aptitude Assessment", "Essay Writing", "Coding Round", "Core Technical Review", "HR & Culture", "Mock Interview"])
        ),
        (
            "Capgemini", "capgemini", "💠", "Consulting & Technology", "Medium",
            "Global leader in partnering with companies to transform and manage their business through technology.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Technical Test (Pseudocode, English, Game-Based Aptitude) | Round 2: Behavioral / Spoken English | Round 3: Technical + HR",
            "Pseudocode (30 Qs), English (30 Qs), Game-Based Aptitude (Grid Challenge, Motion Challenge, Deductive Logic)",
            "Optional Differenciator Coding round: String parsing, Matrix traversal, Tree algorithms.",
            "Core Java (Polymorphism, Abstract classes, Streams), SQL subqueries, Web Services, Version control (Git).",
            "Highlight active listening, clear verbal articulation, and collaborative hybrid teamwork mindset.",
            "Java, SQL, Git, Web Services, Algorithms, Problem Solving",
            json.dumps(["Pseudocode Round", "Game-Based Aptitude", "Spoken English", "Domain Coding", "Technical Interview", "HR Fitment", "Mock Review"])
        ),
        (
            "Deloitte", "deloitte", "🟢", "Consulting & Advisory", "Medium-Hard",
            "One of the Big Four accounting and technology consulting networks.",
            "Data Analyst, Software Developer, Java Developer, Python Developer, Web Developer, Software Engineer, QA Tester",
            "Round 1: Online Aptitude & Technical MCQs | Round 2: Group Discussion / Case Study | Round 3: Technical & Partner Interview",
            "Quantitative Aptitude, Logical Reasoning, Business English, Computer Fundamentals (60 Qs / 60 mins)",
            "1-2 Algorithmic Coding Questions or SQL Query challenges.",
            "Database Architecture, Cloud Security, Cyber Security fundamentals, Object-Oriented Analysis, Analytics.",
            "Exhibit strong business acumen, problem-solving structuring (Case Interviews), and executive communication.",
            "SQL, Python, Cloud Fundamentals, Data Analysis, Cybersecurity, Business Strategy",
            json.dumps(["Cognitive Ability", "Technical MCQs", "Case Study / GD", "System Architecture", "Partner Interview", "Executive Mock"])
        ),
        (
            "Red Hat", "redhat", "🎩", "Open Source & Enterprise OS", "Hard",
            "World's leading provider of enterprise open source solutions including Linux and Kubernetes.",
            "Software Engineer, Python Developer, Software Developer, Java Developer, Web Developer, QA Tester, Data Analyst",
            "Round 1: Online Technical Assessment (Linux, OS, Data Structures, Coding) | Round 2: System Architecture & Coding | Round 3: Culture & Fit",
            "OS Fundamentals (Memory, Kernel, Processes), Shell Scripting, Networking (TCP/IP, Sockets) (30 Qs)",
            "2 System-Level Coding Problems (C / Python / Go) focusing on Concurrency, Memory management, and Data Structures.",
            "Linux Internals, Kernel Architecture, Docker/Podman, Kubernetes, Git, Open Source contribution history.",
            "Show genuine passion for open source software, Linux command line fluency, and collaborative code review practices.",
            "Linux, C, Python, Go, Docker, Kubernetes, Git, Operating Systems, Networking",
            json.dumps(["Linux & OS Foundations", "Shell Scripting", "System-Level Coding", "Architecture Design", "Open Source Fit", "Mock Interview"])
        ),
        (
            "Accenture", "accenture", "🔺", "Technology & Consulting", "Easy-Medium",
            "Global professional services company with leading capabilities in digital, cloud and security.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Cognitive & Technical Assessment | Round 2: Coding Assessment | Round 3: Technical + HR Interview",
            "Critical Thinking & Problem Solving (18 Qs), English (17 Qs), Abstract Reasoning (15 Qs), Common Tech Applications (12 Qs)",
            "2 Coding Challenges (String manipulation, Array frequency, Simple sorting/searching).",
            "Cloud Fundamentals (AWS/Azure), Object-Oriented Design, Agile Methodology, Web Development basics (HTML/CSS/JS/React).",
            "Demonstrate high emotional intelligence (EQ), adaptability to client needs, and familiarity with AI-driven enterprise transformation.",
            "Python, Java, JavaScript, Cloud Basics, Agile, SQL, Networking",
            json.dumps(["Cognitive Test", "Technical Aptitude", "Coding Round", "Communication Assessment", "Interview Round", "AI Mock Simulator"])
        ),
        (
            "Cognizant", "cognizant", "⚡", "Digital Services", "Medium",
            "Leading professional services company, transforming clients' business, operating, and technology models for the digital era.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: GenC / Elevate Assessment (Quantitative, Analytical, Verbal, Domain Coding) | Round 2: Technical + HR Interview",
            "Quantitative Reasoning (16 Qs), Analytical Reasoning (14 Qs), Verbal Ability (20 Qs)",
            "2 Coding Challenges (Array transformations, Bitwise operations, Graph/Tree fundamentals for Elevate).",
            "Relational Databases (PostgreSQL/MySQL), Java Spring Boot or Python Django, JavaScript ES6+, Cloud deployment basics.",
            "Display strong curiosity for emerging digital technology stacks and discuss tangible outcomes from your capstone projects.",
            "Java, Python, React, PostgreSQL, Docker, Data Structures",
            json.dumps(["Analytical Reasoning", "Verbal Assessment", "Algorithmic Coding", "Framework Specialization", "Technical Interview", "HR Assessment"])
        ),
        (
            "HCLTech", "hcltech", "🔵", "IT Services & R&D", "Easy-Medium",
            "Global technology company, home to 220,000+ people across 60 countries, delivering industry-leading capabilities.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Aptitude & Technical Test | Round 2: Technical Interview | Round 3: HR Interview",
            "Quantitative Aptitude (15 Qs), Logical Reasoning (15 Qs), Verbal (15 Qs), Core Technical (15 Qs)",
            "1-2 Basic to Medium Coding Questions in C/C++/Java/Python.",
            "C Programming, OOPs with C++/Java, Database Management Systems, Computer Networks.",
            "Be well-prepared on your core engineering subjects and demonstrate willingness to work across diverse client domains.",
            "C, C++, Java, SQL, Computer Networks, DBMS",
            json.dumps(["Aptitude Test", "Technical MCQs", "Coding Round", "Technical Round", "HR Round", "Mock Interview"])
        ),
        (
            "Tech Mahindra", "techmahindra", "🔴", "IT & Telecom Solutions", "Easy-Medium",
            "Leading provider of digital transformation, consulting and business re-engineering services.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Aptitude + Essay Writing | Round 2: Technical Test | Round 3: Technical & HR Interview",
            "Numerical Ability (15 Qs), Logical Reasoning (15 Qs), Verbal Ability (15 Qs), Essay (10 mins)",
            "2 Coding Questions (Strings, Array Searching, Basic Math).",
            "Telecom Fundamentals, 5G Basics, Core Java, SQL, Web Basics.",
            "Demonstrate clarity in spoken English, good typing speed for the essay round, and customer-first mindset.",
            "Java, Python, C++, SQL, Telecom Basics, Web Technologies",
            json.dumps(["Aptitude Test", "English Essay", "Technical Assessment", "Technical Interview", "HR Interview", "Mock Interview"])
        ),
        (
            "IBM", "ibm", "🟦", "Enterprise Cloud & AI", "Medium-Hard",
            "Global leader in hybrid cloud, AI, and enterprise consulting services with Watson and Red Hat.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Cognitive Ability Games | Round 2: Learning Agility Assessment | Round 3: English Test | Round 4: Technical & HR",
            "Cognitive Assessment Games (Grid challenge, Resemblance, Shortcut logic, Digit challenge)",
            "2 Coding Questions (HackerRank test - Strings, Arrays, Recursion, Trees).",
            "Cloud Computing (IaaS, PaaS, SaaS), Python/Java, Microservices, Data Structures, AI/Watson basics.",
            "Emphasize agility in learning new technologies, structured design thinking, and collaborative team problem solving.",
            "Java, Python, Cloud Architectures, Data Structures, Docker, REST APIs, Design Thinking",
            json.dumps(["Cognitive Games", "English Assessment", "Coding Challenge", "System Architecture", "Technical Interview", "Executive HR"])
        ),
        (
            "LTIMindtree", "ltimindtree", "🔶", "Digital Solutions", "Medium",
            "Global technology consulting and digital solutions company helping enterprises reimagine business models.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (Aptitude, Verbal, Coding) | Round 2: Technical Interview | Round 3: HR Interview",
            "Quantitative Aptitude (15 Qs), Logical Reasoning (15 Qs), Verbal (15 Qs), Technical MCQs (15 Qs)",
            "2 Coding Challenges (Arrays, String hashing, Sorting algorithms).",
            "Core Java, Spring Boot, React / Angular, SQL Joins, REST APIs, Cloud basics.",
            "Demonstrate practical knowledge of full stack application integration and strong problem-solving fundamentals.",
            "Java, Spring Boot, React, SQL, Cloud Basics, Data Structures",
            json.dumps(["Aptitude & Logic", "Technical MCQs", "Coding Round", "Full Stack Interview", "HR Fitment", "Mock Review"])
        ),
        (
            "Persistent Systems", "persistent", "🟠", "Digital Engineering & Product Development", "Medium-Hard",
            "Specializes in software product development and digital engineering for global innovators.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (Aptitude, Computer Fundamentals, Coding) | Round 2: Advanced Coding | Round 3: Technical & HR",
            "Quantitative Aptitude, Computer Science fundamentals (OS, DBMS, CN, Data Structures)",
            "2-3 Algorithmic Coding Problems (Binary Search, Two Pointers, Dynamic Programming, Trees).",
            "Data Structures & Algorithms, Object-Oriented Design, Operating Systems, Database Optimization, Spring/Django.",
            "Deep understanding of algorithmic complexity (Time/Space O(n)), clean coding standards, and system design basics.",
            "Java, Python, C++, DSA, DBMS, System Design, Algorithms",
            json.dumps(["CS Fundamentals", "Algorithmic Coding", "Advanced Problem Solving", "System Architecture", "HR Interview", "Mock Interview"])
        ),
        (
            "Oracle", "oracle", "🔴", "Cloud Infrastructure & Enterprise Software", "Hard",
            "Cloud technology company providing organizations around the world with computing infrastructure and software.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (CS Fundamentals, Aptitude, Coding) | Round 2: Data Structures Round | Round 3: System Design | Round 4: Hiring Manager",
            "CS Fundamentals (OS, DBMS, SQL, Computer Networks, Compilers) & Quantitative Reasoning",
            "2 Coding Questions (Tree traversal, Graph BFS/DFS, Linked List, Dynamic Programming).",
            "Database Internals (B-Trees, WAL, Transactions, Isolation Levels), Concurrency, Memory Management, Distributed Systems.",
            "Explain thought processes aloud, optimize algorithms from brute-force to optimal O(n log n) / O(n), and write clean modular code.",
            "Java, C++, SQL, Database Internals, DSA, Concurrency, Distributed Systems",
            json.dumps(["CS Core Foundations", "Data Structures Round", "Algorithms & DP", "Database Internals", "System Design", "Managerial Round"])
        ),
        (
            "Microsoft", "microsoft", "🪟", "Product & Cloud Platforms", "Hard",
            "Global technology innovator powering cloud computing with Azure, productivity tools, and AI copilot solutions.",
            "Software Engineer, Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, QA Tester",
            "Round 1: Online Coding Assessment (Codility) | Round 2: Data Structures & Algorithms (2-3 Rounds) | Round 3: System Design | Round 4: AA / Fitment",
            "No pure MCQs — Online test consists of 3 algorithmic coding challenges evaluated on edge cases and scalability.",
            "3 Difficult Coding Challenges (Graphs, Dynamic Programming, Tree serializations, Heap algorithms).",
            "Advanced Data Structures (Segment Trees, Trie, Graph Shortest Paths), Object-Oriented Design, Scalability, Azure basics.",
            "Focus on collaborative problem-solving, test-driven development thinking, and embodying Microsoft's Growth Mindset culture.",
            "C++, Java, C#, Python, DSA, System Design, Cloud Architecture, Scalability",
            json.dumps(["Online Assessment", "Data Structures & Trees", "Graph Algorithms", "Low-Level Design", "High-Level Architecture", "As-Appropriate (AA) Round"])
        ),
        (
            "Google", "google", "🌈", "Search, AI & Distributed Systems", "Hard",
            "Technology company specializing in search engine, online advertising, cloud computing, quantum computing, and AI.",
            "Software Engineer, Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, QA Tester",
            "Round 1: Online Challenge (Google Online Assessment) | Round 2: 4-5 Rounds of Data Structures & Algorithms | Round 3: Googliness & Leadership",
            "Algorithmic challenges testing deep mathematical, graph, and combinatorial problem solving.",
            "Complex Algorithmic Problems: Graph Flows, 2D Dynamic Programming, Segment Trees, Bit Manipulation, String Algorithms.",
            "Algorithm Complexity Proofs, Distributed Caching, Memory Allocations, Concurrency, API Design.",
            "Demonstrate 'Googliness' (humility, thriving in ambiguity, collaboration), clear whiteboarding communication, and proactive edge-case testing.",
            "C++, Java, Python, Go, Advanced DSA, Algorithms, Distributed Systems, Scalability",
            json.dumps(["Google Online Challenge", "Algorithmic Round 1", "Algorithmic Round 2", "System Scalability", "Googliness & Leadership", "Hiring Committee Review"])
        ),
        (
            "Amazon", "amazon", "📦", "E-Commerce & Cloud Infrastructure (AWS)", "Hard",
            "Multinational technology company focusing on e-commerce, cloud computing (AWS), online streaming, and artificial intelligence.",
            "Software Engineer, Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, QA Tester",
            "Round 1: Online Assessment (OA1 Debugging, OA2 Coding, OA3 Work Simulation) | Round 2: 3-4 Rounds of DSA + Leadership Principles (LPs)",
            "Work Simulation Assessment (measuring Amazon Leadership Principles) + 2 Algorithmic Coding Challenges.",
            "2 Challenging Coding Problems (Topological Sort, LRU Cache, Sliding Window, Tree Traversals, Two Pointers).",
            "Object-Oriented Design (LLD), Scalable Microservices, AWS Services (S3, DynamoDB, Lambda, EC2), Data Structures.",
            "Crucial: Structure every behavioral answer using STAR format mapping directly to Amazon's 16 Leadership Principles (Customer Obsession, Ownership, Bias for Action).",
            "Java, C++, Python, DSA, System Design, AWS Cloud, Object-Oriented Design, Amazon LPs",
            json.dumps(["Amazon Online Assessment", "Coding Round 1 + LPs", "Coding Round 2 + LPs", "Object-Oriented Design (LLD)", "Bar Raiser Round", "Mock Interview"])
        ),
        (
            "SAP", "sap", "💼", "Enterprise ERP & Cloud Applications", "Medium-Hard",
            "Market leader in enterprise application software, helping companies of all sizes and in all industries run at their best.",
            "Software Developer, Java Developer, Python Developer, Web Developer, Data Analyst, Software Engineer, QA Tester",
            "Round 1: Online Assessment (Aptitude, CS Fundamentals, Coding) | Round 2: Technical Interview | Round 3: Managerial & HR",
            "Aptitude (20 Qs), CS Fundamentals (DBMS, OS, OOP, Data Structures) (25 Qs)",
            "2 Coding Questions (Arrays, Strings, Hash Maps, Simple Trees).",
            "Enterprise Architecture, Core Java, Spring Boot, Database Indexing & ACID, RESTful microservices, Cloud Foundry/K8s.",
            "Show understanding of business workflows, enterprise data integrity, and passion for building robust scalable software.",
            "Java, Python, C++, SQL, Spring Boot, Database Design, Cloud Fundamentals",
            json.dumps(["Aptitude & CS MCQs", "Coding Round", "Core Technical Review", "System & ERP Architecture", "Managerial Fitment", "Mock Review"])
        ),
        (
            "EY", "ey", "🟨", "Consulting & Technology Advisory", "Medium",
            "Global leader in assurance, consulting, strategy and transactions, and technology services.",
            "Data Analyst, Software Developer, Java Developer, Python Developer, Web Developer, Software Engineer, QA Tester",
            "Round 1: Cognitive Aptitude + Technical Assessment | Round 2: Technical Case Interview | Round 3: Partner / HR Round",
            "Numerical Reasoning (15 Qs), Logical Deduction (15 Qs), Verbal Comprehension (15 Qs), Technical Basics (15 Qs)",
            "1-2 Basic to Medium Coding Challenges (SQL Querying & Data Transformation / Python).",
            "Data Analytics (SQL, PowerBI/Tableau), Cloud Architecture (Azure/AWS), Cybersecurity Governance, Business Process Modeling.",
            "Clear articulate communication, business problem decomposition, and commercial awareness.",
            "SQL, Python, PowerBI, Azure, Cybersecurity, Data Analytics, Communication",
            json.dumps(["Cognitive Aptitude", "Technical Assessment", "Data & SQL Case Study", "Consulting Interview", "Partner Interview", "Executive Mock"])
        ),
        (
            "PwC", "pwc", "🟧", "Advisory & Digital Solutions", "Medium",
            "Leading professional services firm delivering quality in assurance, advisory, tax and digital technology consulting services.",
            "Data Analyst, Software Developer, Java Developer, Python Developer, Web Developer, Software Engineer, QA Tester",
            "Round 1: Online Aptitude & Technical MCQs | Round 2: Group Discussion / Case Analysis | Round 3: Technical & Leadership Interview",
            "Quantitative Reasoning, Logical Ability, Verbal Fluency, IT & Cyber Fundamentals (50 Qs / 60 mins)",
            "1 Coding / Data Manipulation Problem (Python / SQL / Java).",
            "Cloud Security, Enterprise Databases, Agile Software Delivery, Business Intelligence, Python/SQL for Analytics.",
            "Demonstrate high professional integrity, active listening skills, and structured problem framing.",
            "SQL, Python, Java, Cloud Computing, Cybersecurity, Agile, Business Analytics",
            json.dumps(["Aptitude & Logic", "Technical Foundations", "Case Discussion", "Technical Interview", "Director / Partner Round", "Mock Interview"])
        )
    ]

    for comp in top_20_companies:
        cursor.execute("SELECT id FROM company_prep WHERE slug = ?", (comp[1],))
        existing_c = cursor.fetchone()
        if existing_c:
            cursor.execute("""
                UPDATE company_prep
                SET company_name = ?, logo_emoji = ?, category = ?, difficulty = ?, description = ?,
                    common_roles = ?, hiring_rounds = ?, aptitude_pattern = ?, coding_pattern = ?,
                    technical_focus = ?, hr_tips = ?, recommended_skills = ?, roadmap_json = ?,
                    updated_at = CURRENT_TIMESTAMP
                WHERE slug = ?
            """, (
                comp[0], comp[2], comp[3], comp[4], comp[5],
                comp[6], comp[7], comp[8], comp[9],
                comp[10], comp[11], comp[12], comp[13],
                comp[1],
            ))
            comp_id = existing_c["id"]
        else:
            cursor.execute("""
                INSERT INTO company_prep (
                    company_name, slug, logo_emoji, category, difficulty, description,
                    common_roles, hiring_rounds, aptitude_pattern, coding_pattern,
                    technical_focus, hr_tips, recommended_skills, roadmap_json
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, comp)
            comp_id = cursor.lastrowid

        # Seed standard job roles for each company if not present
        roles_list = [r.strip() for r in comp[6].split(",") if r.strip()]
        for role_name in roles_list:
            cursor.execute("SELECT id FROM job_roles WHERE company_slug = ? AND role_name = ?", (comp[1], role_name))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO job_roles (company_id, company_slug, role_name, description, skills_required)
                    VALUES (?, ?, ?, ?, ?)
                """, (comp_id, comp[1], role_name, f"{role_name} hiring position at {comp[0]}", comp[12]))

    # Seed default global job roles
    default_global_roles = [
        "Software Developer", "Java Developer", "Python Developer",
        "Web Developer", "Data Analyst", "Software Engineer", "QA Tester"
    ]
    for r_name in default_global_roles:
        cursor.execute("SELECT id FROM job_roles WHERE company_slug = 'all' AND role_name = ?", (r_name,))
        if not cursor.fetchone():
            cursor.execute("""
                INSERT INTO job_roles (company_id, company_slug, role_name, description, skills_required)
                VALUES (NULL, 'all', ?, ?, ?)
            """, (r_name, f"Global industry benchmark role: {r_name}", "Programming, DSA, SQL, Problem Solving"))

    # Seed Admin User (admin@prep.com / AdminPassword123!)
    cursor.execute("SELECT id FROM employees WHERE LOWER(email) = 'admin@prep.com'")
    if not cursor.fetchone():
        admin_pass_hash = generate_password_hash("AdminPassword123!")
        cursor.execute("""
            INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
            VALUES ('Platform Administrator', 'admin@prep.com', ?, 'MCA / M.Tech', 'Full Stack, Cloud Architecture, Python, Security', '5+ Years', 'System Administrator', 'Tata Consultancy Services (TCS)', 'Software Engineer', 1)
        """, (admin_pass_hash,))

    # Seed Demo Student Candidate (student@prep.com / Student123!) for College Demo
    cursor.execute("SELECT id FROM employees WHERE LOWER(email) = 'student@prep.com'")
    demo_emp = cursor.fetchone()
    if not demo_emp:
        student_pass_hash = generate_password_hash("Student123!")
        cursor.execute("""
            INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
            VALUES ('Rahul Sharma', 'student@prep.com', ?, 'B.Tech Computer Science', 'Java, Spring Boot, SQL, Python, React, DSA', 'Fresher', 'Software Engineer', 'Tata Consultancy Services (TCS)', 'Java Developer', 0)
        """, (student_pass_hash,))
        student_id = cursor.lastrowid
    else:
        student_id = demo_emp["id"]

    # Seed demo aptitude result if not present
    cursor.execute("SELECT id FROM aptitude_results WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        cat_breakdown = json.dumps({
            "Quantitative Aptitude": {"score": 4, "total": 4, "percentage": 100},
            "Logical Reasoning": {"score": 3, "total": 4, "percentage": 75},
            "Verbal Ability": {"score": 3, "total": 3, "percentage": 100},
            "Basic Technical Aptitude": {"score": 2, "total": 2, "percentage": 100},
            "Data Interpretation": {"score": 0, "total": 2, "percentage": 0}
        })
        cursor.execute("""
            INSERT INTO aptitude_results (employee_id, score, total, percentage, performance_message, category_breakdown)
            VALUES (?, 12, 15, 80.0, 'Excellent performance across Quantitative and Technical sections. Well-prepared for technical assessments.', ?)
        """, (student_id, cat_breakdown))

    # Seed demo coding progress if not present
    cursor.execute("SELECT id FROM coding_progress WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        demo_problems = [
            ("Two Sum (Hash Map Lookup)", "python", "Easy", "Solved", "def two_sum(nums, target):\n    seen = {}\n    for i, n in enumerate(nums):\n        if target - n in seen: return [seen[target - n], i]\n        seen[n] = i"),
            ("Valid Parentheses", "python", "Easy", "Solved", "def is_valid(s):\n    stack = []\n    m = {')':'(', '}':'{', ']':'['}\n    for c in s:\n        if c in m.values(): stack.append(c)\n        elif not stack or stack.pop() != m.get(c): return False\n    return len(stack) == 0"),
            ("Maximum Subarray (Kadane's Algorithm)", "python", "Medium", "Solved", "def max_sub_array(nums):\n    max_so_far = curr = nums[0]\n    for x in nums[1:]:\n        curr = max(x, curr + x)\n        max_so_far = max(max_so_far, curr)\n    return max_so_far"),
            ("Trapping Rain Water", "python", "Hard", "Solved", "def trap(height):\n    l, r = 0, len(height) - 1\n    l_max = r_max = water = 0\n    while l < r:\n        if height[l] < height[r]:\n            if height[l] >= l_max: l_max = height[l]\n            else: water += l_max - height[l]\n            l += 1\n        else:\n            if height[r] >= r_max: r_max = height[r]\n            else: water += r_max - height[r]\n            r -= 1\n    return water")
        ]
        for p_title, lang, diff, status, code in demo_problems:
            cursor.execute("""
                INSERT INTO coding_progress (employee_id, problem_title, language, difficulty, status, code)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (student_id, p_title, lang, diff, status, code))
    else:
        cursor.execute("UPDATE coding_progress SET status = 'Solved' WHERE employee_id = ?", (student_id,))

    # Seed demo interview result if not present
    cursor.execute("SELECT id FROM interview_results WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO interview_results (employee_id, job_role, overall_score, technical_score, communication_score, feedback, answers_json)
            VALUES (?, 'Java Developer', 84, 86, 82, 'Strong command over Java OOP principles, JVM memory model, and RESTful service design. Clear articulation with structured STAR responses.', '[]')
        """, (student_id,))

    # Seed demo resume data if not present
    cursor.execute("SELECT id FROM resume_data WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO resume_data (employee_id, full_name, email, phone, role, objective, qualification, skills, projects, experience, certifications, achievements)
            VALUES (?, 'Rahul Sharma', 'student@prep.com', '+91 9876543210', 'Java Developer', 'Aspiring software engineer eager to build high-scale distributed backend systems.', 'B.Tech Computer Science (CGPA: 8.7)', 'Java, Spring Boot, SQL, Python, Microservices, React, Git, Docker', 'Placement Preparation Platform (AI Copilot); Distributed File Sharing Service; E-Commerce Microservices Engine', 'Software Engineering Intern (Summer 2025) - Built REST APIs using Spring Boot and PostgreSQL.', 'AWS Certified Cloud Practitioner; Oracle Certified Java SE Programmer', 'Winner of University Hackathon 2025 (1st of 60 teams); Dean Academic Excellence Award')
        """, (student_id,))

    # Seed demo resume analyses (ATS Score)
    cursor.execute("SELECT id FROM resume_analyses WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        cursor.execute("""
            INSERT INTO resume_analyses (employee_id, overall_score, readability_score, relevance_score, target_role, strengths_json, missing_json, keywords_json, suggestions_json)
            VALUES (?, 84, 88, 85, 'Java Developer', '["Strong project descriptions with measurable outcomes", "Clean formatting with high ATS parseability", "Comprehensive Java and SQL skill coverage"]', '["Kubernetes", "Kafka", "CI/CD Pipeline tools"]', '["Java", "Spring Boot", "SQL", "Microservices", "REST API", "Docker"]', '["Add GitHub links to projects", "Include CI/CD deployment tools like Jenkins or GitHub Actions"]')
        """, (student_id,))

    # Seed demo gamification stats
    cursor.execute("SELECT employee_id FROM gamification WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        badges = json.dumps(["first_step", "aptitude_ace", "code_warrior", "streak_3"])
        cursor.execute("""
            INSERT INTO gamification (employee_id, points, level, streak_days, last_activity_date, badges_json)
            VALUES (?, 350, 3, 5, DATE('now'), ?)
        """, (student_id, badges))

    # Seed demo readiness history progression (trend line on dashboard)
    cursor.execute("SELECT id FROM readiness_history WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        trends = [(54, 50, 45, 60, 65, "Developing"), (62, 65, 60, 65, 70, "Developing"), (71, 75, 70, 75, 80, "Ready"), (82, 80, 80, 84, 84, "Job Ready")]
        for t in trends:
            cursor.execute("""
                INSERT INTO readiness_history (employee_id, readiness_score, aptitude_score, coding_score, interview_score, resume_score, status_tier)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (student_id, t[0], t[1], t[2], t[3], t[4], t[5]))

    # Seed 2026 Trend Insights
    cursor.execute("SELECT COUNT(*) as count FROM trend_insights")
    if cursor.fetchone()["count"] == 0:
        trends_data = [
            ("Indirect AI Fluency Testing", "AI Fluency", "All", "All", "Top tech enterprises in 2026 do not ask 'Do you know AI?'. Instead, they evaluate how seamlessly candidates use GitHub Copilot, Cursor, or LLM-based fuzzing during real-time architecture and debugging without losing conceptual mastery.", "When asked how you solve tricky bugs, mention using AI to generate edge-case unit tests while verifying algorithmic correctness yourself.", 1),
            ("60-Second Present-Past-Future Pitch", "Recruiter Framework", "All", "All", "Recruiters favor the concise 60-second Present-Past-Future formula (Present role/strengths -> Past high-impact achievements -> Future company fit) over rambling multi-minute self-introductions.", "Keep your opening pitch strictly between 120-160 words (~60 seconds) so the interviewer stays engaged.", 1),
            ("Single-Column ATS Dominance", "Resume/ATS", "All", "All", "Over 82% of Fortune 500 ATS scanners (Workday, Taleo, Greenhouse) parse single-column markdown/text resumes with 40% higher accuracy than dual-column or graphic-heavy PDFs.", "Use clean single-column layouts with standard headings (Experience, Projects, Education) and bullet metrics.", 1),
            ("Microservice AI Guardrails & Latency", "System Design", "Backend", "Google, Amazon, Microsoft", "System design interviews now evaluate how you safeguard external AI API latency with Redis semantic caching, fallback circuits, and token-cost rate limiters.", "Always mention caching LLM responses and setting timeout fallbacks when designing AI-integrated APIs.", 2),
            ("TCS Prime & Digital Algorithmic Tier", "Company Specific", "Software Engineer", "Tata Consultancy Services (TCS)", "TCS 2026 NQT / Digital rounds heavily weight dynamic programming, graph traversal, and clean modular code with zero global state.", "Prioritize solving LeetCode Medium array, string, and DP challenges with strict time complexity analysis.", 1),
            ("Full-Stack Agentic Workflows", "Dev Productivity", "Full Stack", "All", "Full-stack interviews assess candidate speed in scaffolding boilerplate with AI agents while spending 90% of effort on domain logic and integration security.", "Highlight your ability to rapidly prototype UI/API components while maintaining strict test coverage.", 2),
            ("Amazon Leadership Principles + AI Ethics", "Behavioral", "All", "Amazon", "Amazon bar-raisers test 'Ownership' and 'Bias for Action' regarding how candidates handle AI hallucinations or unverified open-source snippets in production.", "Emphasize your verification checklist before merging AI-assisted code into production branches.", 1)
        ]
        cursor.executemany("""
            INSERT INTO trend_insights (title, category, role_tag, company_tag, content, actionable_tip, priority)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, trends_data)

    # Seed 2026 Trending Resume Templates
    cursor.execute("SELECT COUNT(*) as count FROM trending_templates")
    if cursor.fetchone()["count"] == 0:
        templates_data = [
            ("modern-single", "Modern Single-Column", "🔥 Trending 2026", "Ultra-clean ATS-optimized layout with modern typography, crisp section dividers, and maximum scanability for enterprise ATS systems.", "template-modern-single", 1, 1),
            ("minimalist-accent", "Minimalist Accent", "✨ Top Pick 2026", "Refined contemporary design featuring subtle indigo/teal left borders, modern badges, and structured technical skill chips.", "template-minimalist-accent", 1, 1),
            ("classic-chrono", "Classic Reverse-Chronological", "💼 Corporate Standard", "Time-tested corporate format favored by Tier-1 consulting firms, investment banks, and enterprise leaders. Right-aligned dates and elegant serif headings.", "template-classic-chrono", 1, 1)
        ]
        cursor.executemany("""
            INSERT INTO trending_templates (template_id, name, badge_text, description, css_class, is_trending, is_active)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, templates_data)

    # Seed 2026 AI Fluency Round Questions
    cursor.execute("SELECT COUNT(*) as count FROM ai_fluency_questions")
    if cursor.fetchone()["count"] == 0:
        ai_fluency_questions_data = [
            (
                "How did you improve your developer workflow, sprint velocity, or personal coding productivity recently?",
                "Workflow Velocity",
                "Medium",
                "Interviewers are listening for natural integration of modern developer tools (Copilot, Cursor, CLI bots) paired with disciplined engineering habits.",
                json.dumps([
                    "Mention specific AI-assisted practices (e.g. generating unit test scaffolds, regex writing, boilerplate setup)",
                    "Highlight how you maintain quality control and code reviews",
                    "Cite a concrete metric (e.g., cut PR turnaround by 30%, saved 2 hours per sprint)"
                ])
            ),
            (
                "Describe a time when you encountered a subtle bug or edge case in legacy code. How did you diagnose and resolve it?",
                "Debugging & Incident",
                "Hard",
                "Interviewers check whether you rely blindly on AI or use it as a pair programmer for hypothesis testing and log analysis while understanding root causes.",
                json.dumps([
                    "Explain your systematic debugging steps: reproduction, log analysis, breakpoint tracing",
                    "Weave in how you leveraged AI to explore edge-case inputs or syntax nuances",
                    "Demonstrate verification via regression tests and guard assertions"
                ])
            ),
            (
                "How do you approach learning a new complex framework, language, or system architecture under a tight deadline?",
                "System Learning",
                "Medium",
                "Tests whether you can rapidly synthesize documentation using interactive AI queries without skipping core concepts.",
                json.dumps([
                    "Describe your learning roadmap: official docs + AI architectural summaries",
                    "Explain building a minimum working prototype to test assumptions",
                    "Show how you validate design patterns against production standards"
                ])
            ),
            (
                "Walk me through how you design and validate unit and integration tests for a newly created microservice.",
                "Testing & Quality",
                "Medium",
                "Tests whether you use generative tools to achieve high branch/boundary coverage while writing key integration tests manually.",
                json.dumps([
                    "Mention using AI to generate property-based tests or boundary mock datasets",
                    "Explain writing core business invariant assertions manually",
                    "Discuss CI/CD automated pipeline execution and code coverage metrics"
                ])
            ),
            (
                "How do you verify the correctness and security of code when using generative assistance or external open-source libraries?",
                "Security & Verification",
                "Hard",
                "Tests security awareness: preventing hallucinations, credential leaks, license compliance, and CVE vulnerabilities.",
                json.dumps([
                    "Emphasize zero-trust code review for AI snippets and external packages",
                    "Mention static security analysis (SAST), linter checks, and dependency auditing",
                    "Explain rigorous test-driven validation before deployment"
                ])
            ),
            (
                "Tell me about a project where you had to balance code quality with fast delivery. What trade-offs did you make?",
                "Workflow Velocity",
                "Medium",
                "Evaluates pragmatic engineering: using modern tooling to handle low-risk boilerplate while focusing human energy on high-risk business logic.",
                json.dumps([
                    "Discuss deliberate architectural prioritization",
                    "Show how AI pair programming accelerated routine implementations",
                    "Highlight post-release refactoring and technical debt management"
                ])
            )
        ]
        cursor.executemany("""
            INSERT INTO ai_fluency_questions (question_text, category, difficulty, context_hint, ideal_talking_points_json)
            VALUES (?, ?, ?, ?, ?)
        """, ai_fluency_questions_data)

    # Seed demo student Smart Roadmap
    cursor.execute("SELECT id FROM smart_roadmaps WHERE employee_id = ?", (student_id,))
    existing_roadmap = cursor.fetchone()
    if not existing_roadmap:
        cursor.execute("""
            INSERT INTO smart_roadmaps (employee_id, company_name, company_slug, target_role, duration_days, total_tasks, completed_tasks, progress_percent, streak_days, ai_notes)
            VALUES (?, 'Tata Consultancy Services (TCS)', 'tcs', 'Java Developer', 14, 14, 5, 35.7, 5, 'Tailored to TCS NQT Digital syllabus: Foundation Aptitude, Advanced Java/OOP, Database Query Tuning, and STAR Behavioral Round.')
        """, (student_id,))
        roadmap_id = cursor.lastrowid

        demo_tasks = [
            (roadmap_id, student_id, 1, "Day 1: Company Pattern & Aptitude Mastery", "Quantitative Foundations", "Practice Numerical Reasoning (Percentages & Speed Math) with 10 timed questions.", "Aptitude", 45, 1, "2026-03-01 10:00:00"),
            (roadmap_id, student_id, 2, "Day 2: Java Fundamentals & OOP Drill", "OOP Core Architecture", "Review OOP Encapsulation, Polymorphism, Abstract classes & Collections framework.", "Coding", 60, 1, "2026-03-02 11:30:00"),
            (roadmap_id, student_id, 3, "Day 3: Data Structures (Arrays & Two Pointers)", "Linear DSA Practice", "Solve Two Sum, 3Sum, and Maximum Subarray with O(n) target time complexity.", "Coding", 60, 1, "2026-03-03 14:00:00"),
            (roadmap_id, student_id, 4, "Day 4: Logical Reasoning & Syllogisms", "Analytical Deductions", "Complete 10 Logical Reasoning & Syllogism questions under exam clock constraints.", "Aptitude", 40, 1, "2026-03-04 16:15:00"),
            (roadmap_id, student_id, 5, "Day 5: 60-Second Pitch & STAR Simulator", "Executive Self-Intro", "Draft and practice your Present-Past-Future self-introduction pitch under 60 seconds.", "Behavioral", 45, 1, "2026-03-05 09:30:00"),
            (roadmap_id, student_id, 6, "Day 6: Database SQL Joins & Indexing", "RDBMS Performance", "Write complex queries with INNER/LEFT JOIN, GROUP BY, and explain B-Tree index scans.", "Technical", 50, 0, None),
            (roadmap_id, student_id, 7, "Day 7: String Manipulation & HashMaps", "Hash Table Optimization", "Solve Longest Substring Without Repeating Characters and Group Anagrams.", "Coding", 60, 0, None),
            (roadmap_id, student_id, 8, "Day 8: Spring Boot Microservices Architecture", "Backend Engineering", "Explain REST controllers, Spring IoC, Dependency Injection, and JPA repository queries.", "Technical", 55, 0, None),
            (roadmap_id, student_id, 9, "Day 9: AI Fluency & Modern Workflow Round", "2026 AI Workflow", "Complete AI Fluency round demonstrating natural integration of Copilot for mock tests.", "AI Fluency", 45, 0, None),
            (roadmap_id, student_id, 10, "Day 10: Dynamic Programming Fundamentals", "Optimal Substructure", "Solve 1D Dynamic Programming problems: Fibonacci, Climbing Stairs, and Coin Change.", "Coding", 75, 0, None),
            (roadmap_id, student_id, 11, "Day 11: Verbal & Business Communication", "Professional English", "Practice Reading Comprehension, Sentence Correction, and active listening summaries.", "Aptitude", 40, 0, None),
            (roadmap_id, student_id, 12, "Day 12: Resume ATS Alignment & Project Polish", "ATS Optimization", "Score resume with AI ATS tool, optimize impact bullet points, and select template.", "Technical", 50, 0, None),
            (roadmap_id, student_id, 13, "Day 13: Full Technical Mock Interview", "Simulated Technical Round", "Complete 30-min simulated TCS technical interview with coding & architecture questions.", "Mock Interview", 60, 0, None),
            (roadmap_id, student_id, 14, "Day 14: Managerial & Final Culture Fit Round", "Enterprise Behavioral", "Review TCS core values, adaptability under change, and leadership conflict stories.", "Behavioral", 45, 0, None)
        ]
        cursor.executemany("""
            INSERT INTO roadmap_tasks (roadmap_id, employee_id, day_number, phase_name, title, description, category, estimated_minutes, is_completed, completed_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, demo_tasks)

    # Seed demo student Saved Resume Version
    cursor.execute("SELECT id FROM resume_versions WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        resume_demo_data = {
            "full_name": "Rahul Sharma",
            "email": "student@prep.com",
            "phone": "+91 9876543210",
            "location": "Bengaluru, India",
            "role": "Java Developer",
            "summary": "Results-oriented Software Engineer specializing in Java, Spring Boot, and cloud-native microservices. Passionate about building high-throughput APIs with 99.9% uptime and leveraging modern AI-assisted workflows for rapid test coverage and robust system reliability.",
            "skills": "Java 17, Spring Boot, SQL, PostgreSQL, Python, Docker, Git, RESTful APIs, Redis, JUnit, Kafka, Microservices",
            "experience": [
                {
                    "title": "Software Engineering Intern",
                    "company": "Apex Cloud Systems",
                    "location": "Bengaluru, India",
                    "duration": "June 2025 - August 2025",
                    "bullets": [
                        "Architected and deployed 4 RESTful microservices using Spring Boot and PostgreSQL, reducing batch latency by 32%.",
                        "Integrated Redis caching layer for frequent user profile reads, cutting database query pressure by 45%.",
                        "Wrote comprehensive unit and integration test suites with JUnit and Mockito, increasing branch coverage from 68% to 91%."
                    ]
                }
            ],
            "projects": [
                {
                    "name": "AI Employee Preparation Platform",
                    "technologies": "Python, FastAPI, Flask, SQLite, Vanilla CSS/JS",
                    "description": "Architected an interactive employee assessment engine featuring company-specific roadmaps, live code evaluation, and ATS resume scoring for 1,000+ candidates."
                },
                {
                    "name": "Distributed Task Queue Service",
                    "technologies": "Java, Spring Boot, Redis, Docker",
                    "description": "Engineered an asynchronous task worker processing 10k+ concurrent jobs with exponential backoff retries and Dead Letter Queue fault tolerance."
                }
            ],
            "education": [
                {
                    "degree": "B.Tech in Computer Science and Engineering",
                    "institution": "National Institute of Technology",
                    "year": "2022 - 2026",
                    "gpa": "8.7 / 10.0"
                }
            ],
            "certifications": [
                "Oracle Certified Associate: Java SE Programmer",
                "AWS Certified Cloud Practitioner"
            ]
        }
        cursor.execute("""
            INSERT INTO resume_versions (employee_id, version_name, template_name, target_role, target_company, resume_data_json, score)
            VALUES (?, 'TCS - Java Developer v1', 'modern-single', 'Java Developer', 'Tata Consultancy Services (TCS)', ?, 88)
        """, (student_id, json.dumps(resume_demo_data)))

    # Seed demo student AI Fluency Attempt
    cursor.execute("SELECT id FROM ai_fluency_attempts WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        answer_text = "Recently I improved my team sprint velocity by using GitHub Copilot to scaffold boilerplate test fixtures and parameterized unit test suites. Instead of spending hours writing manual JSON mock payloads, I prompt the AI with edge-case requirements like null boundaries and concurrency races. Then I carefully review and verify every assertion myself, run the CI suite locally, and profile execution time. This helped our team ship our payment service sprint 2 days ahead of schedule while maintaining 92% test coverage."
        rewrite_sample = "In our recent microservices milestone, I accelerated our delivery velocity by integrating AI pair-programming into our testing workflow. Specifically, I utilized GitHub Copilot to scaffold complex test mock datasets and boundary edge cases. Crucially, rather than accepting suggestions blindly, I applied a verification-first mindset—conducting rigorous manual code inspections and executing local regression runs. This cut our test authoring time by ~35% while ensuring zero regressions reached staging."
        cursor.execute("""
            INSERT INTO ai_fluency_attempts (employee_id, question_id, question_text, candidate_answer, overall_score, ai_tool_score, verification_score, velocity_score, communication_score, feedback, suggestions_json, rewrite_sample)
            VALUES (?, 1, 'How did you improve your developer workflow, sprint velocity, or personal coding productivity recently?', ?, 88, 92, 90, 86, 84, 'Excellent response! You demonstrated genuine AI tool fluency by citing GitHub Copilot for mock scaffolding while emphasizing critical manual verification and local regression runs.', '["Highlight quantitative time saved upfront", "Mention continuous integration pipeline verification", "Frame tool usage as assistive pair programming"]', ?)
        """, (student_id, answer_text, rewrite_sample))

    # Seed demo student Structured Answer (Present-Past-Future 60s Pitch)
    cursor.execute("SELECT id FROM structured_answers WHERE employee_id = ?", (student_id,))
    if not cursor.fetchone():
        present = "I am a final-year Computer Science engineer and backend developer specializing in Java, Spring Boot, and scalable API architecture. My primary technical focus is designing high-performance REST microservices and database query optimization."
        past = "Over the past year, I built an enterprise placement preparation engine supporting 1,000+ candidate simulations and completed a software engineering internship where I reduced API batch processing latency by 32% using Spring Boot and Redis caching."
        future = "I want to join TCS as a Java Developer because of your pioneering digital transformation work in banking and cloud solutions. I am excited to apply my core backend skills and deliver production-ready, highly reliable services from day one."
        combined = f"{present} {past} {future}"
        critique = "Outstanding 60-second delivery! The transition from your active technical focus to your concrete internship achievements and clear TCS alignment is crisp, persuasive, and perfectly timed."
        optimized = f"{present} {past} {future}"
        cursor.execute("""
            INSERT INTO structured_answers (employee_id, question_key, question_title, target_role, target_company, present_text, past_text, future_text, combined_text, speaking_time_seconds, word_count, structure_score, ai_critique, ai_optimized_pitch)
            VALUES (?, 'tell-me-about-yourself', 'Tell me about yourself / Walk me through your resume', 'Java Developer', 'Tata Consultancy Services (TCS)', ?, ?, ?, ?, 58, 142, 92, ?, ?)
        """, (student_id, present, past, future, combined, critique, optimized))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    init_db()
    print("Database successfully initialized with full relational schema at:", DB_PATH)
