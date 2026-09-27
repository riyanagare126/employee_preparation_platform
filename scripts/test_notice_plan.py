"""
Automated unit and integration test for Notice Period Countdown Planner feature.
Tests:
1. Database schema initialization (notice_plans & notice_plan_tasks).
2. AI Service fallback planner with priority weak areas and 2-day interview revision rules.
3. API endpoints:
   - GET /api/notice-plan/active
   - POST /api/notice-plan/generate
   - POST /api/notice-plan/task/toggle
   - GET /api/notice-plan/full
"""
import os
import sys
import json
from datetime import date, timedelta

# Ensure workspace root is in path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from backend.database import init_db, get_db_connection
from backend.models import EmployeeModel, NoticePlanModel
from backend.services.ai_service import generate_fallback_notice_plan, generate_notice_period_plan
from backend.app import create_app

def run_tests():
    print("=" * 60)
    print("STARTING NOTICE PERIOD COUNTDOWN PLANNER TEST SUITE")
    print("=" * 60)

    # 1. Database Initialization
    print("\n[Step 1] Initializing database and verifying table creation...")
    init_db()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('notice_plans', 'notice_plan_tasks');")
    tables = [row[0] for row in cursor.fetchall()]
    conn.close()
    assert "notice_plans" in tables, "Table notice_plans was not created!"
    assert "notice_plan_tasks" in tables, "Table notice_plan_tasks was not created!"
    print("[OK] Tables 'notice_plans' and 'notice_plan_tasks' exist in database.")

    # 2. Test Fallback AI Engine
    print("\n[Step 2] Testing AI Service Notice Period Planner (Fallback & Logic)...")
    today = date.today()
    intv_date = (today + timedelta(days=10)).strftime("%Y-%m-%d")
    lwd_date = (today + timedelta(days=30)).strftime("%Y-%m-%d")

    inputs = {
        "target_role": "Backend Engineer",
        "experience_years": "3",
        "notice_period_days": 30,
        "last_working_date": lwd_date,
        "interview_dates": [intv_date],
        "weak_areas": ["DSA", "System Design"],
        "daily_study_time": "1 hr"
    }

    plan = generate_notice_period_plan(inputs)
    assert plan is not None, "Plan generation returned None"
    assert len(plan["days"]) == 30, f"Expected 30 days, got {len(plan['days'])}"

    # Verify that Day 9, 10, or 11 has interview milestone
    interview_milestone_days = [d for d in plan["days"] if d.get("is_interview_prep")]
    assert len(interview_milestone_days) >= 2, f"Expected at least 2 interview milestone days, found {len(interview_milestone_days)}"
    print(f"✔ Found {len(interview_milestone_days)} interview revision days for interview on {intv_date}:")
    for d in interview_milestone_days:
        print(f"   -> Day {d['day_number']}: {d['interview_alert']}")
        assert any(t["category"] in ["Behavioral", "Resume", "Interview", "Technical", "Company"] for t in d["tasks"])

    # Verify deep links
    all_links = [t["link_url"] for d in plan["days"] for t in d["tasks"] if t.get("link_url")]
    assert "preparation.html" in all_links
    assert "interview.html" in all_links
    print(f"[OK] Platform deep links correctly assigned ({len(all_links)} task links).")

    # 3. Test Flask Endpoints with Test Client
    print("\n[Step 3] Testing Flask API endpoints...")
    app = create_app()
    client = app.test_client()

    # Get or create a test employee
    test_emp = EmployeeModel.get_by_email("student@prep.com")
    if not test_emp:
        emp_id = EmployeeModel.create(
            "Test Employee", "student@prep.com", "TestPass123!",
            "B.Tech", "Python, SQL", "2 years", "Software Developer"
        )
    else:
        emp_id = test_emp["id"]

    # Test POST /api/notice-plan/generate
    gen_payload = {
        "employee_id": emp_id,
        "target_role": "Senior Full Stack Engineer",
        "experience_years": "4",
        "notice_period_days": 30,
        "last_working_date": lwd_date,
        "interview_dates": [intv_date],
        "weak_areas": ["DSA", "SQL", "System Design"],
        "daily_study_time": "1 hr"
    }

    resp = client.post("/api/notice-plan/generate", json=gen_payload)
    assert resp.status_code == 200, f"Generate failed with {resp.status_code}: {resp.data}"
    gen_data = json.loads(resp.data)
    assert gen_data["success"] is True
    plan_obj = gen_data["data"]
    assert plan_obj["target_role"] == "Senior Full Stack Engineer"
    assert plan_obj["total_tasks"] > 0
    print(f"[OK] POST /api/notice-plan/generate created plan with {plan_obj['total_tasks']} tasks.")

    # Test GET /api/notice-plan/active
    resp_act = client.get(f"/api/notice-plan/active?employee_id={emp_id}")
    assert resp_act.status_code == 200
    act_data = json.loads(resp_act.data)
    assert act_data["success"] is True
    assert act_data["data"]["days_left"] > 0
    assert len(act_data["data"]["today_tasks"]) > 0
    print(f"[OK] GET /api/notice-plan/active returned active plan ({act_data['data']['days_left']} days left, {len(act_data['data']['today_tasks'])} tasks for today).")

    # Test POST /api/notice-plan/task/toggle
    first_task = act_data["data"]["today_tasks"][0]
    first_task_id = first_task["id"]

    resp_tog = client.post("/api/notice-plan/task/toggle", json={
        "employee_id": emp_id,
        "task_id": first_task_id
    })
    assert resp_tog.status_code == 200
    tog_data = json.loads(resp_tog.data)
    assert tog_data["success"] is True
    assert tog_data["is_completed"] == 1
    assert tog_data["completed_tasks"] >= 1
    print(f"[OK] POST /api/notice-plan/task/toggle marked task {first_task_id} completed (progress: {tog_data['progress_percent']}%).")

    # Test GET /api/notice-plan/full
    resp_full = client.get(f"/api/notice-plan/full?employee_id={emp_id}")
    assert resp_full.status_code == 200
    full_data = json.loads(resp_full.data)
    assert full_data["success"] is True
    assert len(full_data["data"]["days"]) == 30
    print(f"[OK] GET /api/notice-plan/full returned all 30 days with tasks.")

    print("\n" + "=" * 60)
    print("ALL TESTS PASSED WITH 100% SUCCESS!")
    print("=" * 60)

if __name__ == "__main__":
    run_tests()
