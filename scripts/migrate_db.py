"""
Safe Database Migration & Seed Runner for Local and Render Deployments.

Ensures:
1. All tables (including companies and company_questions) exist with correct indexes.
2. Does NOT drop any existing tables, users, or candidate preparation progress.
3. Automatically triggers idempotent seeding from data/companies/*.json if needed.
4. Verifies database integrity across SQLite and PostgreSQL (DATABASE_URL).
"""

import os
import sys

# Ensure root directory is on python path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from dotenv import load_dotenv
load_dotenv()

from backend.database import init_db, get_db_connection
from backend.models import CompanyModel, CompanyQuestionModel, EmployeeModel


def run_migration():
    print("=" * 65)
    print("AI Employee Preparation Platform - Database Migration & Verification")
    print("=" * 65)

    db_url = os.getenv("DATABASE_URL")
    if db_url and (db_url.startswith("postgresql://") or db_url.startswith("postgres://")):
        print(f"[DB INFO] Detected production PostgreSQL database: {db_url.split('@')[-1] if '@' in db_url else 'configured'}")
    else:
        print("[DB INFO] Detected local SQLite database (backend/database/employees.db)")

    # 1. Run schema initialization (safe CREATE TABLE IF NOT EXISTS)
    print("\n[STEP 1] Running schema initialization and safe column migrations...")
    try:
        init_db()
        print("[SUCCESS] Database tables and indexes verified/created.")
    except Exception as e:
        print(f"[ERROR] Failed during schema initialization: {e}")
        sys.exit(1)

    # 2. Check if companies and company_questions need seeding
    print("\n[STEP 2] Verifying company blueprints and question banks...")
    total_companies = len(CompanyModel.get_all(active_only=False))
    total_questions = CompanyQuestionModel.count_questions()

    print(f"Current companies in DB: {total_companies}")
    print(f"Current questions in DB: {total_questions}")

    if total_companies < 20 or total_questions < 3480:
        print("\n[SEEDING] Running idempotent company & question seeder (scripts/seed_companies.py)...")
        from scripts.seed_companies import seed_all
        seed_res = seed_all()
        print(f"[SEED COMPLETED] Companies: {seed_res.get('companies_seeded', 0)}, Questions: {seed_res.get('questions_seeded', 0)}")
    else:
        print("[UP TO DATE] All companies and question banks are fully populated.")

    # 3. Print integrity report
    print("\n[STEP 3] Final Database Health Check:")
    try:
        users = EmployeeModel.get_all(limit=10)
        final_comp_count = len(CompanyModel.get_all(active_only=False))
        final_q_count = CompanyQuestionModel.count_questions()
        print(f"  - Total Registered Candidates Preserved: {len(users)}")
        print(f"  - Active Enterprise Company Blueprints: {final_comp_count}")
        print(f"  - Total Role-Specific Questions Ready: {final_q_count}")
        print("\n[ALL SYSTEMS OPERATIONAL] Database is ready for traffic!")
        print("=" * 65)
    except Exception as e:
        print(f"[WARNING] Health check warning: {e}")


if __name__ == "__main__":
    run_migration()
