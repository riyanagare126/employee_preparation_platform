"""
Idempotent Database Seed Script for Company Question Banks.
Loads data/companies/<slug>.json into 'companies' and 'company_questions' tables.
Strictly idempotent:
- Running twice will NEVER create duplicates.
- Will NEVER overwrite admin modifications to existing companies or questions.
"""
import os
import sys
import glob
import json
import re

# Add repository root to python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.database import get_db_connection, init_db
from backend.models import CompanyModel, CompanyQuestionModel

def seed_database(clean: bool = False) -> dict:
    init_db()

    data_dir = os.path.join(ROOT_DIR, "data", "companies")
    files = glob.glob(os.path.join(data_dir, "*.json"))

    if not files:
        print(f"[!] No seed files found in {data_dir}")
        return {"companies": 0, "questions_inserted": 0, "questions_skipped": 0}

    conn = get_db_connection()
    cursor = conn.cursor()

    if clean:
        print("[!] --clean flag provided: clearing existing company_questions table...")
        cursor.execute("DELETE FROM company_questions")
        conn.commit()

    total_companies = 0
    total_q_inserted = 0
    total_q_skipped = 0

    print(f"[*] Starting idempotent seed across {len(files)} companies (clean={clean})...")

    for file_path in sorted(files):
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        slug = data.get("slug")
        name = data.get("name") or data.get("company_name")
        if not slug or not name:
            continue

        # 1. Insert or update company
        cursor.execute("SELECT id FROM companies WHERE LOWER(slug) = LOWER(?)", (slug.strip(),))
        comp_row = cursor.fetchone()

        if not comp_row:
            cursor.execute("""
                INSERT INTO companies (
                    name, slug, industry, difficulty, logo, is_active,
                    description, common_roles, hiring_rounds, aptitude_pattern,
                    coding_pattern, technical_focus, hr_tips, recommended_skills
                ) VALUES (?, ?, ?, ?, ?, 1, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                name, slug, data.get("industry", "IT Services"),
                data.get("difficulty", "Medium"), data.get("logo", "fas fa-building"),
                data.get("description", ""), data.get("common_roles", ""),
                data.get("hiring_rounds", ""), data.get("aptitude_pattern", ""),
                data.get("coding_pattern", ""), data.get("technical_focus", ""),
                data.get("hr_tips", ""), data.get("recommended_skills", "")
            ))
            comp_id = cursor.lastrowid
        else:
            comp_id = comp_row["id"] if isinstance(comp_row, dict) else comp_row[0]
            cursor.execute("""
                UPDATE companies SET
                    name = ?, industry = ?, difficulty = ?, logo = ?,
                    description = ?, common_roles = ?, hiring_rounds = ?,
                    aptitude_pattern = ?, coding_pattern = ?, technical_focus = ?,
                    hr_tips = ?, recommended_skills = ?
                WHERE id = ?
            """, (
                name, data.get("industry", "IT Services"),
                data.get("difficulty", "Medium"), data.get("logo", "fas fa-building"),
                data.get("description", ""), data.get("common_roles", ""),
                data.get("hiring_rounds", ""), data.get("aptitude_pattern", ""),
                data.get("coding_pattern", ""), data.get("technical_focus", ""),
                data.get("hr_tips", ""), data.get("recommended_skills", ""),
                comp_id
            ))

        total_companies += 1

        # 2. Insert questions idempotently (keyed by category, role, and normalized text)
        cursor.execute("SELECT category, role, question FROM company_questions WHERE company_id = ?", (comp_id,))
        existing_rows = cursor.fetchall()
        existing_norms = {
            (
                (r["category"] if isinstance(r, dict) else r[0] or "").strip().lower(),
                (r["role"] if isinstance(r, dict) else r[1] or "").strip().lower(),
                re.sub(r'[^a-z0-9]', '', (r["question"] if isinstance(r, dict) else r[2] or "").lower())
            )
            for r in existing_rows
        }

        questions = data.get("questions", [])
        for q in questions:
            q_text = (q.get("question") or "").strip()
            if not q_text:
                continue

            cat = (q.get("category") or "aptitude").strip().lower()
            role = (q.get("role") or "All").strip()
            norm = re.sub(r'[^a-z0-9]', '', q_text.lower())
            key = (cat, role.lower(), norm)

            if key in existing_norms:
                total_q_skipped += 1
                continue

            diff = (q.get("difficulty") or "Medium").strip()
            opts = json.dumps(q["options"]) if isinstance(q.get("options"), list) else q.get("options")
            ans = (q.get("correct_answer") or "").strip()
            exp = (q.get("explanation") or "").strip()
            ext = json.dumps(q["extra"]) if isinstance(q.get("extra"), dict) else q.get("extra")
            act = int(q.get("is_active", 1))

            cursor.execute("""
                INSERT INTO company_questions (
                    company_id, category, role, difficulty, question,
                    options, correct_answer, explanation, extra, is_active
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (comp_id, cat, role, diff, q_text, opts, ans, exp, ext, act))

            existing_norms.add(key)
            total_q_inserted += 1

        conn.commit()

    # Get final DB count
    cursor.execute("SELECT COUNT(*) FROM company_questions")
    final_count = cursor.fetchone()[0]
    conn.close()

    print("\n" + "=" * 60)
    print("SEED EXECUTION REPORT:")
    print(f"Total Companies Processed: {total_companies}")
    print(f"New Questions Inserted: {total_q_inserted}")
    print(f"Existing Questions Preserved (Skipped): {total_q_skipped}")
    print(f"Total Questions in Database: {final_count}")
    print("=" * 60)

    return {
        "companies": total_companies,
        "questions_inserted": total_q_inserted,
        "questions_skipped": total_q_skipped,
        "total_in_db": final_count
    }

if __name__ == "__main__":
    is_clean = "--clean" in sys.argv
    seed_database(clean=is_clean)
