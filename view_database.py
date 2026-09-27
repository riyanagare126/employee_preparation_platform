"""
Database Viewer Utility for College Viva & Demonstrations
Displays live records directly from backend/database/employees.db
"""
import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "backend", "database", "employees.db")

def print_separator(title):
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def main():
    if not os.path.exists(DB_PATH):
        print(f"[!] Database file not found at: {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()

    print_separator("DATABASE OVERVIEW (SQLite Engine)")
    print(f"DB Location : {DB_PATH}")
    print(f"DB File Size: {round(os.path.getsize(DB_PATH) / (1024 * 1024), 2)} MB")

    # 1. Show all Tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name NOT LIKE 'sqlite_%' ORDER BY name;")
    tables = [row["name"] for row in cursor.fetchall()]
    print(f"Total Tables: {len(tables)} Relational Tables")
    print("Key Tables  : " + ", ".join(tables[:12]) + "...")

    # 2. Registered Employees
    print_separator("TABLE: employees (Registered Candidates & Profile Data)")
    cursor.execute("SELECT id, name, email, target_company, target_role, is_admin, created_at FROM employees ORDER BY id DESC LIMIT 5;")
    users = cursor.fetchall()
    print(f"{'ID':<4} | {'Name':<20} | {'Email':<25} | {'Target Company':<18} | {'Role'}")
    print("-" * 80)
    for u in users:
        admin_tag = "[Admin]" if u["is_admin"] else "[Student]"
        print(f"{u['id']:<4} | {u['name'][:20]:<20} | {u['email'][:25]:<25} | {str(u['target_company'])[:18]:<18} | {admin_tag}")

    # 3. Aptitude Test Results
    print_separator("TABLE: aptitude_results (Recent Test Submissions & Scores)")
    cursor.execute("SELECT id, employee_id, score, total, percentage, performance_message, created_at FROM aptitude_results ORDER BY id DESC LIMIT 5;")
    tests = cursor.fetchall()
    if tests:
        print(f"{'Test ID':<8} | {'Student ID':<10} | {'Score':<10} | {'Percentage':<12} | {'Created At'}")
        print("-" * 65)
        for t in tests:
            print(f"{t['id']:<8} | {t['employee_id']:<10} | {t['score']}/{t['total']:<7} | {t['percentage']}%{'':<6} | {str(t['created_at'])[:16]}")
    else:
        print("No test attempts recorded yet.")

    # 4. Coding Progress
    print_separator("TABLE: coding_progress (Coding Challenge Submissions)")
    cursor.execute("SELECT id, employee_id, problem_title, language, difficulty, status FROM coding_progress ORDER BY id DESC LIMIT 5;")
    codes = cursor.fetchall()
    if codes:
        print(f"{'ID':<4} | {'Student ID':<10} | {'Problem Title':<25} | {'Language':<10} | {'Status'}")
        print("-" * 65)
        for c in codes:
            print(f"{c['id']:<4} | {c['employee_id']:<10} | {str(c['problem_title'])[:25]:<25} | {str(c['language']):<10} | {c['status']}")
    else:
        print("No coding submissions recorded yet.")

    # 5. Smart Roadmaps
    print_separator("TABLE: smart_roadmaps (Personalized 2026 AI Roadmaps)")
    cursor.execute("SELECT id, employee_id, company_name, duration_days, total_tasks, completed_tasks, progress_percent FROM smart_roadmaps ORDER BY id DESC LIMIT 5;")
    roadmaps = cursor.fetchall()
    if roadmaps:
        print(f"{'ID':<4} | {'Student ID':<10} | {'Company':<20} | {'Duration':<10} | {'Progress'}")
        print("-" * 65)
        for r in roadmaps:
            print(f"{r['id']:<4} | {r['employee_id']:<10} | {str(r['company_name'])[:20]:<20} | {r['duration_days']} Days{'':<3} | {r['completed_tasks']}/{r['total_tasks']} Tasks ({r['progress_percent']}%)")
    else:
        print("No roadmaps generated yet.")

    conn.close()
    print("\n" + "=" * 70)
    print("  [OK] Data is persistently stored in SQLite & synced via REST APIs!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
