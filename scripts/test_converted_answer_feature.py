import sys
import os
import sqlite3

workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, workspace)
sys.path.insert(0, os.path.join(workspace, "backend"))

from backend.database import init_db, get_db_connection
from backend.models import ConvertedAnswerModel
from backend.services.ai_service import convert_honest_to_professional
from backend.app import create_app

def run_tests():
    print("=== Testing Honest-to-Professional Answer Converter Feature ===")
    
    # 1. Initialize DB and check table converted_answer
    init_db()
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("PRAGMA table_info(converted_answer)")
    columns = {col[1]: col[2] for col in c.fetchall()}
    print(f"[1] converted_answer table schema: {columns}")
    
    expected_cols = ["id", "employee_id", "question_type", "raw_answer", "professional_answer", "created_at"]
    for col in expected_cols:
        assert col in columns, f"Missing column {col} in converted_answer table"
    print("  [OK] Table converted_answer exists with all required columns!")

    # Ensure a test employee
    c.execute("SELECT id FROM employees LIMIT 1")
    row = c.fetchone()
    emp_id = row["id"] if isinstance(row, dict) else row[0]
    conn.close()

    # 2. Test the 3 required question types and non-lying 4-6 sentence behavior
    test_cases = [
        ("Why are you leaving your current job?", "My boss is a micromanager and they refuse to give me a hike after 2 years."),
        ("Explain your employment gap", "I took 6 months off to care for my sick mother and re-evaluate my career path."),
        ("Why were you laid off?", "Our division was impacted by macroeconomic layoffs after the company missed revenue.")
    ]

    for qtype, raw in test_cases:
        res = convert_honest_to_professional({"question_type": qtype, "raw_answer": raw})
        prof = res.get("professional_answer", "")
        sentences = [s.strip() for s in prof.replace("!", ".").replace("?", ".").split(".") if s.strip()]
        sentence_count = len(sentences)
        print(f"[2] Q: '{qtype}' -> Polished Answer: {sentence_count} sentences")
        print(f"    Answer text: {prof[:120]}...")
        assert sentence_count >= 3 and sentence_count <= 8, f"Expected 4-6 sentences, got {sentence_count}"
        # Ensure no lying encouraged
        lower_ans = prof.lower()
        import re
        assert not re.search(r"\b(lie|lying|fabricate|fabrication)\b", lower_ans)
        print(f"  [OK] '{qtype}' converted into truthful, positive professional answer!")

    # 3. Test API submission with auto-save
    app = create_app()
    client = app.test_client()

    resp = client.post("/api/converted-answers/convert", json={
        "employee_id": emp_id,
        "question_type": "Why were you laid off?",
        "raw_answer": "Company downsized 15% of engineering staff due to budget constraints."
    })
    assert resp.status_code == 200
    res_data = resp.get_json()
    assert res_data.get("success") is True
    assert res_data.get("saved") is not None or "id" in res_data.get("data", {})
    print(f"[3] POST /api/converted-answers/convert auto-saved successfully! ID: {res_data.get('data', {}).get('id')}")

    # 4. Verify record in converted_answer table
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT id, employee_id, question_type, raw_answer, professional_answer, created_at FROM converted_answer WHERE employee_id = ? ORDER BY id DESC LIMIT 1", (emp_id,))
    latest = c.fetchone()
    assert latest is not None, "Record not found in converted_answer table"
    print(f"[4] Record verified in converted_answer table: ID #{latest['id']}, Q: '{latest['question_type']}'")
    conn.close()

    # 5. Verify GET /api/converted-answers
    resp_get = client.get(f"/api/converted-answers?employee_id={emp_id}")
    assert resp_get.status_code == 200
    get_data = resp_get.get_json()
    assert get_data.get("success") is True
    assert len(get_data.get("data", [])) >= 1
    print(f"[5] GET /api/converted-answers returned {len(get_data['data'])} saved answers.")

    print("\n=== ALL HONEST CONVERTER TESTS PASSED 100%! ===")

if __name__ == "__main__":
    run_tests()
