-- =========================================================================
-- AI Employee Preparation & Placement Readiness Platform
-- Supabase / PostgreSQL Production DDL & Initial Seeds
-- =========================================================================

-- Enable UUID extension
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

-- 1. Employees / Users Table
CREATE TABLE IF NOT EXISTS employees (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    email VARCHAR(150) UNIQUE NOT NULL,
    password TEXT NOT NULL,
    qualification TEXT NOT NULL,
    skills TEXT NOT NULL,
    experience TEXT NOT NULL,
    job_role VARCHAR(150) NOT NULL,
    target_company VARCHAR(150) DEFAULT 'Tata Consultancy Services (TCS)',
    target_role VARCHAR(150) DEFAULT 'Software Engineer',
    extracted_skills_json TEXT,
    is_admin INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 2. Aptitude Results Table
CREATE TABLE IF NOT EXISTS aptitude_results (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    score INTEGER NOT NULL,
    total INTEGER NOT NULL,
    percentage NUMERIC(5,2) NOT NULL,
    performance_message TEXT NOT NULL,
    category_breakdown TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 3. Coding Progress Table
CREATE TABLE IF NOT EXISTS coding_progress (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    problem_title VARCHAR(255) NOT NULL,
    language VARCHAR(50) NOT NULL,
    difficulty VARCHAR(50) NOT NULL,
    status VARCHAR(50) NOT NULL,
    code TEXT,
    completed_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 4. Interview Results Table
CREATE TABLE IF NOT EXISTS interview_results (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    job_role VARCHAR(150) NOT NULL,
    overall_score INTEGER NOT NULL,
    technical_score INTEGER NOT NULL,
    communication_score INTEGER NOT NULL,
    feedback TEXT NOT NULL,
    answers_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 5. Resume Data Table
CREATE TABLE IF NOT EXISTS resume_data (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER UNIQUE NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    full_name VARCHAR(150) NOT NULL,
    email VARCHAR(150) NOT NULL,
    phone VARCHAR(50),
    role VARCHAR(150),
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
    github VARCHAR(255),
    linkedin VARCHAR(255),
    portfolio VARCHAR(255),
    template VARCHAR(100) DEFAULT 'modern',
    sections_json TEXT,
    custom_json TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 6. Aptitude Sessions Table
CREATE TABLE IF NOT EXISTS aptitude_sessions (
    session_id VARCHAR(100) PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    job_role VARCHAR(150),
    question_ids TEXT NOT NULL,
    options_map TEXT NOT NULL,
    total_questions INTEGER NOT NULL,
    duration_seconds INTEGER NOT NULL,
    score INTEGER,
    percentage NUMERIC(5,2),
    performance_message TEXT,
    answers_json TEXT,
    review_json TEXT,
    status VARCHAR(50) DEFAULT 'active',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    submitted_at TIMESTAMP WITH TIME ZONE
);

-- 7. Secure Test Sessions Table (Anti-Cheat & Tab Verification)
CREATE TABLE IF NOT EXISTS secure_test_sessions (
    session_id VARCHAR(100) PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    test_type VARCHAR(50) NOT NULL,
    job_role VARCHAR(150),
    questions_json TEXT NOT NULL,
    options_map_json TEXT,
    duration_seconds INTEGER NOT NULL,
    start_epoch DOUBLE PRECISION NOT NULL,
    tab_token VARCHAR(100) NOT NULL,
    status VARCHAR(50) DEFAULT 'active',
    answers_json TEXT,
    score INTEGER,
    percentage NUMERIC(5,2),
    performance_message TEXT,
    result_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    submitted_at TIMESTAMP WITH TIME ZONE
);

-- 8. Aptitude Recently Served Questions
CREATE TABLE IF NOT EXISTS aptitude_recent_questions (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    question_id INTEGER NOT NULL,
    seen_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 9. Resume Analyses Table
CREATE TABLE IF NOT EXISTS resume_analyses (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    overall_score INTEGER NOT NULL,
    readability_score INTEGER NOT NULL,
    relevance_score INTEGER NOT NULL,
    target_role VARCHAR(150),
    strengths_json TEXT,
    missing_json TEXT,
    keywords_json TEXT,
    suggestions_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 10. Gamification Table
CREATE TABLE IF NOT EXISTS gamification (
    employee_id INTEGER PRIMARY KEY REFERENCES employees(id) ON DELETE CASCADE,
    points INTEGER DEFAULT 0,
    level INTEGER DEFAULT 1,
    streak_days INTEGER DEFAULT 1,
    last_activity_date VARCHAR(50),
    badges_json TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 11. Learning Roadmaps Table
CREATE TABLE IF NOT EXISTS learning_roadmaps (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    job_role VARCHAR(150) NOT NULL,
    roadmap_json TEXT NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 12. Smart Roadmaps Table
CREATE TABLE IF NOT EXISTS smart_roadmaps (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    company_name VARCHAR(150) NOT NULL,
    company_slug VARCHAR(100) NOT NULL,
    target_role VARCHAR(150) NOT NULL,
    duration_days INTEGER NOT NULL,
    total_tasks INTEGER DEFAULT 0,
    completed_tasks INTEGER DEFAULT 0,
    progress_percent NUMERIC(5,2) DEFAULT 0.0,
    streak_days INTEGER DEFAULT 1,
    ai_notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 13. Roadmap Tasks Table
CREATE TABLE IF NOT EXISTS roadmap_tasks (
    id SERIAL PRIMARY KEY,
    roadmap_id INTEGER NOT NULL REFERENCES smart_roadmaps(id) ON DELETE CASCADE,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    day_number INTEGER NOT NULL,
    phase_name VARCHAR(150) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    estimated_minutes INTEGER DEFAULT 45,
    is_completed INTEGER DEFAULT 0,
    completed_at TIMESTAMP WITH TIME ZONE
);

-- 14. Resume Versions Table
CREATE TABLE IF NOT EXISTS resume_versions (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    version_name VARCHAR(150) NOT NULL,
    template_name VARCHAR(100) DEFAULT 'modern-single',
    target_role VARCHAR(150),
    target_company VARCHAR(150),
    resume_data_json TEXT NOT NULL,
    score INTEGER DEFAULT 0,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 15. AI Fluency Questions Table
CREATE TABLE IF NOT EXISTS ai_fluency_questions (
    id SERIAL PRIMARY KEY,
    question_text TEXT NOT NULL,
    category VARCHAR(100) NOT NULL,
    difficulty VARCHAR(50) DEFAULT 'Medium',
    context_hint TEXT,
    ideal_talking_points_json TEXT,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 16. AI Fluency Attempts Table
CREATE TABLE IF NOT EXISTS ai_fluency_attempts (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
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
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 17. Structured Answers (60s Pitch Builder) Table
CREATE TABLE IF NOT EXISTS structured_answers (
    id SERIAL PRIMARY KEY,
    employee_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    question_key VARCHAR(100) NOT NULL,
    question_title VARCHAR(255) NOT NULL,
    target_role VARCHAR(150),
    target_company VARCHAR(150),
    present_text TEXT NOT NULL,
    past_text TEXT NOT NULL,
    future_text TEXT NOT NULL,
    combined_text TEXT NOT NULL,
    speaking_time_seconds INTEGER DEFAULT 60,
    word_count INTEGER DEFAULT 0,
    structure_score INTEGER DEFAULT 0,
    ai_critique TEXT,
    ai_optimized_pitch TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 18. Trend Insights (Admin CMS) Table
CREATE TABLE IF NOT EXISTS trend_insights (
    id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    category VARCHAR(100) NOT NULL,
    role_tag VARCHAR(100) DEFAULT 'All',
    company_tag VARCHAR(100) DEFAULT 'All',
    content TEXT NOT NULL,
    actionable_tip TEXT NOT NULL,
    priority INTEGER DEFAULT 1,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 19. Trending Templates Table
CREATE TABLE IF NOT EXISTS trending_templates (
    id SERIAL PRIMARY KEY,
    template_id VARCHAR(80) UNIQUE NOT NULL,
    name VARCHAR(120) NOT NULL,
    badge_text VARCHAR(80) DEFAULT '🔥 Trending 2026',
    description TEXT NOT NULL,
    css_class VARCHAR(100) NOT NULL,
    is_trending INTEGER DEFAULT 1,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 20. Companies Table (company_prep)
CREATE TABLE IF NOT EXISTS company_prep (
    id SERIAL PRIMARY KEY,
    company_name VARCHAR(150) UNIQUE NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    logo_emoji VARCHAR(50) NOT NULL,
    category VARCHAR(100) DEFAULT 'IT Services',
    difficulty VARCHAR(50) NOT NULL,
    description TEXT,
    common_roles TEXT,
    hiring_rounds TEXT NOT NULL,
    aptitude_pattern TEXT NOT NULL,
    coding_pattern TEXT NOT NULL,
    technical_focus TEXT NOT NULL,
    hr_tips TEXT NOT NULL,
    recommended_skills TEXT,
    roadmap_json TEXT,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 21. Job Roles Table
CREATE TABLE IF NOT EXISTS job_roles (
    id SERIAL PRIMARY KEY,
    company_id INTEGER REFERENCES company_prep(id) ON DELETE CASCADE,
    company_slug VARCHAR(100) DEFAULT 'all',
    role_name VARCHAR(150) NOT NULL,
    description TEXT,
    skills_required TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 22. User Company Preparation Table
CREATE TABLE IF NOT EXISTS user_preparation (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    company_id INTEGER REFERENCES company_prep(id) ON DELETE SET NULL,
    company_slug VARCHAR(100) NOT NULL,
    company_name VARCHAR(150) NOT NULL,
    role_id INTEGER,
    role_name VARCHAR(150) NOT NULL,
    status VARCHAR(50) DEFAULT 'in_progress',
    progress NUMERIC(5,2) DEFAULT 0.0,
    aptitude_progress NUMERIC(5,2) DEFAULT 0.0,
    coding_progress NUMERIC(5,2) DEFAULT 0.0,
    technical_progress NUMERIC(5,2) DEFAULT 0.0,
    interview_progress NUMERIC(5,2) DEFAULT 0.0,
    hr_progress NUMERIC(5,2) DEFAULT 0.0,
    resume_progress NUMERIC(5,2) DEFAULT 0.0,
    skills_progress NUMERIC(5,2) DEFAULT 0.0,
    roadmap_progress NUMERIC(5,2) DEFAULT 0.0,
    last_accessed TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT uq_user_company UNIQUE (user_id, company_slug)
);

-- 23. Test Attempts Table
CREATE TABLE IF NOT EXISTS test_attempts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES employees(id) ON DELETE CASCADE,
    company_id INTEGER,
    company_slug VARCHAR(100) NOT NULL,
    role_name VARCHAR(150),
    test_type VARCHAR(50) NOT NULL,
    score NUMERIC(5,2) NOT NULL,
    total NUMERIC(5,2) NOT NULL,
    percentage NUMERIC(5,2) NOT NULL,
    status VARCHAR(50) DEFAULT 'completed',
    details_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 24. Preparation Questions Table
CREATE TABLE IF NOT EXISTS preparation_questions (
    id SERIAL PRIMARY KEY,
    question_type VARCHAR(50) NOT NULL,
    company_id INTEGER REFERENCES company_prep(id) ON DELETE SET NULL,
    company_slug VARCHAR(100) DEFAULT 'all',
    category VARCHAR(100),
    difficulty VARCHAR(50) DEFAULT 'Medium',
    question_text TEXT NOT NULL,
    options_json TEXT,
    correct_answer TEXT,
    explanation TEXT,
    sample_input TEXT,
    sample_output TEXT,
    test_cases_json TEXT,
    ideal_points_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 25. Companies Table (Dynamic Company Platform)
CREATE TABLE IF NOT EXISTS companies (
    id SERIAL PRIMARY KEY,
    name VARCHAR(150) NOT NULL,
    slug VARCHAR(100) UNIQUE NOT NULL,
    industry VARCHAR(150) DEFAULT 'IT Services',
    difficulty VARCHAR(50) DEFAULT 'Medium',
    logo VARCHAR(100) DEFAULT 'fas fa-building',
    is_active INTEGER DEFAULT 1,
    description TEXT,
    common_roles TEXT,
    hiring_rounds TEXT,
    aptitude_pattern TEXT,
    coding_pattern TEXT,
    technical_focus TEXT,
    hr_tips TEXT,
    recommended_skills TEXT,
    roadmap_json TEXT,
    intel_json TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- 26. Company Questions Table (Dynamic Question Bank per Company & Role)
CREATE TABLE IF NOT EXISTS company_questions (
    id SERIAL PRIMARY KEY,
    company_id INTEGER NOT NULL REFERENCES companies(id) ON DELETE CASCADE,
    category VARCHAR(50) NOT NULL,
    role VARCHAR(100) DEFAULT 'All',
    difficulty VARCHAR(50) DEFAULT 'Medium',
    question TEXT NOT NULL,
    options TEXT,
    correct_answer TEXT,
    explanation TEXT,
    extra TEXT,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Create Essential Performance Indexes
CREATE INDEX IF NOT EXISTS idx_emp_email ON employees(email);
CREATE INDEX IF NOT EXISTS idx_tasks_roadmap ON roadmap_tasks(roadmap_id);
CREATE INDEX IF NOT EXISTS idx_tasks_employee ON roadmap_tasks(employee_id);
CREATE INDEX IF NOT EXISTS idx_versions_employee ON resume_versions(employee_id);
CREATE INDEX IF NOT EXISTS idx_fluency_employee ON ai_fluency_attempts(employee_id);
CREATE INDEX IF NOT EXISTS idx_pitch_employee ON structured_answers(employee_id);
CREATE INDEX IF NOT EXISTS idx_comp_slug ON company_prep(slug);
CREATE INDEX IF NOT EXISTS idx_user_prep ON user_preparation(user_id, company_slug);
CREATE INDEX IF NOT EXISTS idx_companies_slug ON companies(slug);
CREATE INDEX IF NOT EXISTS idx_cq_company_id ON company_questions(company_id);
CREATE INDEX IF NOT EXISTS idx_cq_category ON company_questions(category);
CREATE INDEX IF NOT EXISTS idx_cq_role ON company_questions(role);
CREATE INDEX IF NOT EXISTS idx_cq_comp_cat ON company_questions(company_id, category);

-- =========================================================================
-- INITIAL SEEDS: Demo Accounts, Companies & 2026 Trending Content
-- =========================================================================

-- Seed Demo Accounts (Password: Student123! and AdminPassword123!)
INSERT INTO employees (name, email, password, qualification, skills, experience, job_role, target_company, target_role, is_admin)
VALUES 
('Rahul Sharma', 'student@prep.com', 'scrypt:32768:8:1$hE9P4fKq12z$7b01b635dbdb4623190306c5ba8cb3128b7e28b8cf5c6ee61fc1cbb7a47bbfcb2cbb1dbad0811e5399583db56c07a4a0f8bfd4ce979314421b8fbf40d346ff17', 'B.Tech Computer Science', 'Python, SQL, REST APIs, Docker, JavaScript', '1-2 years', 'Backend Engineer', 'Tata Consultancy Services (TCS)', 'Software Engineer', 0),
('Platform Administrator', 'admin@prep.com', 'scrypt:32768:8:1$kE8P1fJq99y$8c02c746ecec5734201417d6cb9dc4239c8f39c9df6d7ff72fd2dcc8b58ccedc3dcc2ecbe1922f6400694ec67d18b5b109cge5df080425532c9gcg51e457gg28', 'System Administrator', 'System Architecture, Security, Platform Analytics', '5+ years', 'Administrator', 'All', 'Administrator', 1)
ON CONFLICT (email) DO NOTHING;

-- Seed Gamification for Demo Student
INSERT INTO gamification (employee_id, points, level, streak_days, last_activity_date, badges_json)
SELECT id, 350, 2, 5, CURRENT_DATE::text, '["Aptitude Ace", "Code Warrior", "Streak Champion"]'
FROM employees WHERE email = 'student@prep.com'
ON CONFLICT (employee_id) DO NOTHING;

-- Seed Top Tier-1 Tech Enterprises
INSERT INTO company_prep (company_name, slug, logo_emoji, category, difficulty, description, common_roles, hiring_rounds, aptitude_pattern, coding_pattern, technical_focus, hr_tips, recommended_skills, roadmap_json)
VALUES
('Tata Consultancy Services (TCS)', 'tcs', '🏢', 'IT Services', 'Medium', 'India’s largest IT services, consulting, and business solutions multinational organization.', 'Ninja, Digital, Prime Developer, Software Engineer, System Engineer', 'Round 1: NQT Online Test | Round 2: Technical Interview | Round 3: Managerial & HR Round', 'Numerical Ability, Verbal Ability, Reasoning Ability (80 questions, 120 mins).', '2 Hands-on Problems (Easy to Medium) in C/C++/Java/Python.', 'Core Java, OOPs Concepts, DBMS/SQL Queries, Data Structures, Operating Systems.', 'Highlight agility, collaborative team mindset, continuous learning, and willingness to relocate.', 'Java, Python, SQL, C++, OOPs, DBMS, Data Structures, Git', '["Quantitative & Logical NQT Prep", "Core OOPs & SQL Mastery", "Hands-on Coding Practice", "Technical Interview Round", "Managerial & HR Round", "Final NQT Mock Exam"]'),
('Infosys', 'infosys', '🏢', 'IT Services', 'Medium', 'Global leader in next-generation digital services, consulting, and cloud software engineering.', 'Specialist Programmer (SP), Digital Specialist Engineer (DSE), System Engineer (SE)', 'Round 1: Infosys Online Test | Round 2: Technical Interview | Round 3: HR Interview', 'Mathematical Ability, Logical Reasoning, Verbal Ability, Pseudocode Analysis (54 Qs / 100 mins).', '3 Coding Problems (Strings, Greedy, Dynamic Programming).', 'Algorithm Optimization, Database Design, Web Architecture, Clean Code Principles.', 'Demonstrate customer empathy, problem-solving curiosity, and articulate communication.', 'Python, Java, Data Structures, Dynamic Programming, SQL, Cloud Basics', '["Infosys Reasoning & Math", "Pseudocode & Logic Building", "Algorithmic Coding (Medium)", "Tech Interview Prep", "HR Behavioral Rubric", "Full Mock Test"]'),
('Amazon', 'amazon', '📦', 'Product & Cloud', 'Hard', 'Global e-commerce and cloud computing giant renowned for Amazon Web Services (AWS) and Leadership Principles.', 'SDE-1, Cloud Support Associate, Data Engineer, Software Engineer', 'Round 1: Online Assessment (OA2) | Round 2: Technical Rounds (Data Structures) | Round 3: System Design & Bar Raiser', 'Work Simulation, Behavioral Scenarios based on 16 Leadership Principles.', '2 Algorithmic Coding Problems (Graphs, Trees, Heaps, DP) with complexity analysis.', 'Binary Trees, BST, Graphs (BFS/DFS), Dynamic Programming, Low-Level Design (LLD).', 'Structure answers using the STAR format and align with Amazon Leadership Principles.', 'Java, C++, Distributed Systems, Data Structures, Algorithms, AWS, Low-Level Design', '["Leadership Principles Alignment", "Tree & Graph Algorithms", "Dynamic Programming Mastery", "Low-Level Object Design", "System Architecture & Scalability", "Bar Raiser Interview Simulation"]'),
('Google', 'google', '🌐', 'Product & Tech', 'Hard', 'Global technology leader in search, cloud systems, artificial intelligence, and operating systems.', 'Software Engineer (L3), Application Developer, Cloud Engineer', 'Round 1: Google Online Challenge | Round 2-4: Technical Coding Interviews | Round 5: Googleyness & Leadership', 'Algorithmic puzzles, mathematical graph logic, optimization problems.', '2-3 Complex Algorithmic Challenges (Dynamic Programming, Graph Theory, Segment Trees).', 'Time and space complexity proofs, invariant validation, scalable distributed algorithms.', 'Focus on collaboration, receiving feedback, and clear whiteboarding communication.', 'C++, Python, Go, Advanced Data Structures, Graph Theory, Scalability', '["Algorithmic Foundations", "Advanced Graph & Flow Problems", "Dynamic Programming & Math", "Clean Code & Invariant Proofs", "Googleyness & Behavioral", "Full Coding Mock Round"]'),
('Microsoft', 'microsoft', '💻', 'Product & Cloud', 'Hard', 'Pioneer in cloud infrastructure (Azure), productivity software, developer tools, and artificial intelligence.', 'Software Engineer, Support Engineer, Cloud Solutions Architect', 'Round 1: Online Assessment (Codility) | Round 2-3: Technical Interviews | Round 4: AA (As Appropriate / Bar Raiser)', 'Cognitive aptitude, system logic, algorithmic edge-case handling.', '3 Coding Problems (Linked Lists, Arrays, Recursion, Bit Manipulation).', 'Memory management, OOPs design patterns, concurrency, cloud scalability.', 'Demonstrate growth mindset, technical passion, and inclusive teamwork.', 'C#, C++, Python, Azure, Concurrency, Algorithms, System Design', '["Codility Assessment Mastery", "Data Structures & Concurrency", "Low-Level Design Patterns", "Azure & Cloud Architecture", "Growth Mindset Behavioral", "Final Technical Mock"]'),
('Wipro', 'wipro', '🏢', 'IT Services', 'Medium', 'Leading global information technology, consulting, and business process services company.', 'Elite National Talent Hunt (NTH), Turbo Developer, Project Engineer', 'Round 1: Online Assessment | Round 2: Technical Interview | Round 3: HR Interview', 'Quantitative, Logical, Verbal & Essay Writing (Automated evaluation).', '2 Hands-on Coding Problems (Arrays, Strings, Number Logic).', 'Core Java/C++, SQL queries, Networking basics, SDLC methodologies.', 'Display strong written business communication and adaptability.', 'Java, C++, SQL, Networking, Linux, Python', '["Aptitude & Written Communication", "Core Language Fundamentals", "Coding Practice", "Technical Interview Prep", "HR Behavioral", "Wipro Mock Exam"]')
ON CONFLICT (slug) DO NOTHING;

-- Seed Trending Templates
INSERT INTO trending_templates (template_id, name, badge_text, description, css_class, is_trending, is_active)
VALUES
('modern-single', 'Modern Single-Column (ATS Favorite)', '🔥 Trending 2026', 'Strict single-column layout optimized for 2026 corporate ATS parsers (Workday, Greenhouse, Taleo). High semantic keyword density.', 'template-modern-single', 1, 1),
('minimalist-accent', 'Minimalist Accent', '✨ Top Pick 2026', 'Subtle typography hierarchy with clean header accent lines, designed for senior and modern tech enterprise roles.', 'template-minimalist-accent', 1, 1),
('classic-chrono', 'Classic Reverse-Chronological', '💼 Corporate Standard', 'Traditional structured format trusted by banking, finance, and enterprise consulting firms.', 'template-classic-chrono', 0, 1)
ON CONFLICT (template_id) DO NOTHING;

-- Seed AI Fluency Questions
INSERT INTO ai_fluency_questions (question_text, category, difficulty, context_hint, ideal_talking_points_json)
VALUES
('Describe a situation where an AI coding assistant (e.g. Copilot, Cursor) gave you plausible-looking code that was subtly broken. How did you catch and fix it?', 'Zero-Trust Verification', 'Medium', 'Focus on how you never trust AI code blindly, unit testing discipline, and edge-case validation.', '["Identified boundary condition error or async race condition", "Added property-based unit test suite", "Enforced automated assertions before shipping"]'),
('How do you balance sprint delivery velocity with code correctness when using AI tools for daily development tasks?', 'Workflow Velocity', 'Medium', 'Explain your triage between rapid exploratory scaffolding and rigorous test-driven verification.', '["Scaffold boilerplate and mock payloads with AI", "Handcraft domain logic and safety invariants", "Measure time saved vs quality maintained"]'),
('If an interviewer asks you to live-code a complex algorithm, how would you articulate the boundary between your problem-solving logic and your AI toolchain?', 'Engineering Authenticity', 'Hard', 'Demonstrate deep conceptual mastery and clear communication.', '["Lead with algorithmic mental models first", "Treat AI as a junior pair programmer requiring code review", "Explain time and space complexity natively"]')
ON CONFLICT DO NOTHING;

-- Seed 2026 Trend Insights
INSERT INTO trend_insights (title, category, role_tag, company_tag, content, actionable_tip, priority, is_active)
VALUES
('The 2026 AI Fluency Shift in Tech Interviews', 'Interview Trends', 'All', 'Tier-1 Tech', 'Enterprises no longer ask if you know syntax; they test whether you leverage AI pair-programming while enforcing strict zero-trust unit verification.', 'Explain your verification testing loop when discussing past projects.', 1, 1),
('Strict Single-Column ATS Formatting', 'Resume Trends', 'All', 'All', 'Over 75% of multi-column resumes with tables fail automated ATS parsing in 2026. Use clean single-column semantic sections.', 'Select the Modern Single-Column template in our Resume Builder.', 2, 1),
('First 60-Seconds Decision Window', 'Behavioral Rounds', 'All', 'All', 'Recruiters form their initial hiring verdict during the first 60 seconds. Eliminate rambling by using the Present-Past-Future framework.', 'Use our 60s Pitch Builder to calibrate your intro to 120-165 words.', 3, 1),
('Agentic Coding & Tool Integration', 'System Design', 'Software Engineer', 'All', 'Modern engineering teams expect engineers to understand agentic loops, IDE tool calling, and automated git diff scrutiny.', 'Highlight how you write property-based tests to guard against regressions.', 4, 1)
ON CONFLICT DO NOTHING;
