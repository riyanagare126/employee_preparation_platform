"""
Automated Integration Test for Notice Period Planner Feature.
Verifies:
1. Automatic creation of 'notice_plan' table on startup with exact schema.
2. Saving and fetching simple notice plans per employee.
3. Accurate 'days_left' calculation based on notice_days.
4. Proper fallback generation in ai_service.py without crashing.
5. Endpoints:
   - POST /api/notice-plan/generate
   - GET /api/notice-plan/latest
6. Form validation error handling.
"""
import os
import sys
import json
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from backend.database import init_db, get_db_connection
from backend.models import NoticePlanModel
from backend.services.ai_service import generate_simple_notice_plan
from backend.app import create_app

def run_tests():
    print("=" * 60)
    print("RUNNING NOTICE PERIOD PLANNER FEATURE TESTS")
    print("=" * 60)

    # 1. Test Database Schema
    print("\n[Test 1] Verifying 'notice_plan' table schema...")
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("PRAGMA table_info(notice_plan);")
    columns = {col[1]: col[2] for col in cursor.fetchall()}
    conn.close()

    expected_cols = ["id", "employee_id", "target_role", "experience", "notice_days", "weak_areas", "plan_text", "created_at"]
    for col in expected_cols:
        assert col in columns, f"Column '{col}' missing from table 'notice_plan'!"
    print(f"✔ Table 'notice_plan' verified with all required columns: {list(columns.keys())}")

    # 2. Test AI Service Generator (Fallback & Structure)
    print("\n[Test 2] Testing generate_simple_notice_plan AI service fallback...")
    plan_text_short = generate_simple_notice_plan(
        target_role="Full Stack Engineer",
        experience="2",
        notice_days=14,
        weak_areas=["DSA", "SQL"]
    )
    assert "Full Stack Engineer" in plan_text_short
    assert "DSA" in plan_text_short or "Algorithms" in plan_text_short
    assert "SQL" in plan_text_short
    assert "Day" in plan_text_short
    print("✔ 14-day Day-wise preparation plan generated cleanly without errors.")

    plan_text_long = generate_simple_notice_plan(
        target_role="System Architect",
        experience="5",
        notice_days=45,
        weak_areas=["System Design", "HR/Behavioral", "Aptitude"]
    )
    assert "System Architect" in plan_text_long
    assert "Week" in plan_text_long
    print("✔ 45-day Week-wise preparation plan generated cleanly without errors.")

    # 3. Test Flask Endpoints
    print("\n[Test 3] Testing Flask API Endpoints...")
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()

    test_employee_id = 1

    # Generate Plan API
    payload = {
        "employee_id": test_employee_id,
        "target_role": "Lead Cloud Engineer",
        "experience": "5-8",
        "notice_days": 30,
        "weak_areas": ["DSA", "System Design"]
    }
    resp = client.post("/api/notice-plan/generate", json=payload)
    assert resp.status_code == 200, f"Generate failed with {resp.status_code}: {resp.data}"
    data = resp.get_json()
    assert data["success"] is True
    plan_data = data["data"]
    assert plan_data["target_role"] == "Lead Cloud Engineer"
    assert plan_data["days_left"] == 30
    assert "plan_text" in plan_data
    assert len(plan_data["plan_text"]) > 100
    print(f"✔ POST /api/notice-plan/generate succeeded (ID: {plan_data.get('id')}, Days Left: {plan_data['days_left']}).")

    # Fetch Latest Plan API
    resp_get = client.get(f"/api/notice-plan/latest?employee_id={test_employee_id}")
    assert resp_get.status_code == 200
    get_data = resp_get.get_json()
    assert get_data["success"] is True
    assert get_data["data"] is not None
    assert get_data["data"]["target_role"] == "Lead Cloud Engineer"
    assert get_data["data"]["days_left"] == 30
    print("✔ GET /api/notice-plan/latest returned latest saved plan successfully.")

    # 4. Test Validation Handling
    print("\n[Test 4] Testing Validation & Error Handling...")
    # Missing employee_id
    bad_resp = client.post("/api/notice-plan/generate", json={"target_role": "Dev"})
    assert bad_resp.status_code == 400
    # Invalid notice days
    bad_days = client.post("/api/notice-plan/generate", json={"employee_id": test_employee_id, "target_role": "Dev", "notice_days": -5})
    assert bad_days.status_code == 400
    print("✔ Form validation and error responses verified.")

    # Clean up test row
    conn = get_db_connection()
    conn.execute("DELETE FROM notice_plan WHERE employee_id = ?", (test_employee_id,))
    conn.commit()
    conn.close()
    print("✔ Test database record cleaned up.")

    print("\n" + "=" * 60)
    print("ALL NOTICE PERIOD PLANNER TESTS PASSED 100%!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
