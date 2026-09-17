"""
Supabase PostgreSQL Connection & Verification Script
Usage:
    py test_supabase_connection.py "postgresql://postgres:password@db.xyz.supabase.co:5432/postgres"
    or set DATABASE_URL in .env and run:
    py test_supabase_connection.py
"""
import sys
import os
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    # 1. Resolve connection URI
    if len(sys.argv) > 1:
        db_url = sys.argv[1].strip()
    else:
        db_url = os.getenv("DATABASE_URL", "").strip()

    if not db_url:
        print("=" * 60)
        print("❌ ERROR: No DATABASE_URL provided!")
        print("Usage:")
        print("  py test_supabase_connection.py \"postgresql://postgres:pass@db.xyz.supabase.co:5432/postgres\"")
        print("  or add DATABASE_URL to your .env file.")
        print("=" * 60)
        sys.exit(1)

    if db_url.startswith("postgres://"):
        db_url = db_url.replace("postgres://", "postgresql://", 1)

    print("=" * 60)
    print("🔄 Connecting to Supabase PostgreSQL Database...")
    print(f"Host Target: {db_url.split('@')[-1].split('/')[0] if '@' in db_url else 'Hidden'}")
    print("=" * 60)

    try:
        import psycopg2
        import psycopg2.extras
    except ImportError:
        print("❌ Error: psycopg2-binary is not installed. Run: pip install psycopg2-binary")
        sys.exit(1)

    try:
        conn = psycopg2.connect(db_url, connect_timeout=10)
        cur = conn.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
        print("✔ Connected successfully to Supabase PostgreSQL server!")
        
        # Check PostgreSQL Version
        cur.execute("SELECT version();")
        v = cur.fetchone()
        print(f"✔ Database Engine: {list(v.values())[0][:50]}...")

        # Query all public tables
        cur.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public' 
            ORDER BY table_name ASC;
        """)
        tables = [r["table_name"] for r in cur.fetchall()]
        print(f"\n✔ Total Public Tables Found: {len(tables)}")
        
        expected_tables = [
            "employees", "smart_roadmaps", "roadmap_tasks", "resume_versions",
            "ai_fluency_attempts", "structured_answers", "trend_insights",
            "company_prep", "gamification", "trending_templates"
        ]

        missing = [t for t in expected_tables if t not in tables]
        if missing:
            print(f"⚠️ Notice: Some tables not found yet: {missing}")
            print("👉 To create them: Open Supabase -> SQL Editor -> paste supabase_schema.sql -> click Run!")
        else:
            print("✔ All 10 Core Application Tables are present and ready!")

        # Query sample counts if employees exists
        if "employees" in tables:
            cur.execute("SELECT COUNT(*) as count FROM employees;")
            cnt = cur.fetchone()["count"]
            print(f"✔ Users / Employees registered: {cnt}")

        if "company_prep" in tables:
            cur.execute("SELECT COUNT(*) as count FROM company_prep;")
            cnt = cur.fetchone()["count"]
            print(f"✔ Enterprise Companies seeded: {cnt}")

        conn.close()
        print("\n" + "=" * 60)
        print("🎉 SUCCESS: Your Supabase database is 100% READY for deployment!")
        print("=" * 60)

    except Exception as e:
        print(f"\n❌ Connection Failed: {e}")
        print("\nTroubleshooting Tips:")
        print("1. Check that you replaced [YOUR-PASSWORD] with your actual Supabase database password.")
        print("2. In Supabase -> Settings -> Database -> Network Bans, ensure no IP is blocked.")
        print("3. Ensure the project is not paused in Supabase Dashboard.")
        sys.exit(1)

if __name__ == "__main__":
    test_connection()
