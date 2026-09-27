import sys
import os
import json

# Set paths
workspace = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, workspace)
sys.path.insert(0, os.path.join(workspace, "backend"))

print("[TEST] 1. Testing AI Service: Honest-to-Professional Answer Converter...")
from backend.services.ai_service import convert_honest_to_professional, generate_fallback_converted_answer

scenarios = [
    ("Why are you leaving your current job?", "My boss is completely toxic and micromanages everything. The salary is terrible, no raise for 2 years, and I'm totally bored and burnt out."),
    ("Explain your employment gap", "I was exhausted and quit with no job lined up. Spent 9 months doing nothing, resting, and dealing with family stuff."),
    ("Why did you get laid off?", "The company fired 20% of our team out of nowhere after missing quarterly targets. It was super abrupt and unfair."),
    ("Why so many job changes?", "My first job paid pennies so I left after 7 months. Second job changed my tech stack without asking so I quit after 9 months. Third job had terrible management.")
]

for qtype, raw in scenarios:
    res = generate_fallback_converted_answer(qtype, raw, "Senior Engineer", "Acme Corp")
    assert res is not None, f"Failed fallback generation for {qtype}"
    assert "professional_answer" in res and len(res["professional_answer"]) > 50, f"Missing professional answer for {qtype}"
    assert "short_answer" in res and len(res["short_answer"]) > 20, f"Missing short answer for {qtype}"
    assert "red_flags" in res and len(res["red_flags"]) >= 1, f"Expected red flags detected for {qtype}"
    assert "follow_up_questions" in res and len(res["follow_up_questions"]) == 2, f"Expected 2 follow-ups for {qtype}"
    print(f"  [OK] Heuristic test passed for '{qtype[:30]}...' -> {len(res['red_flags'])} red flags, 2 followups")

# Test live convert function
live_res = convert_honest_to_professional("Why are you leaving your current job?", "Bad manager, low salary", "Tech Lead", "Google")
assert live_res is not None and "professional_answer" in live_res
print("  [OK] convert_honest_to_professional() returned successfully")

print("\n[TEST] 2. Testing ConvertedAnswerModel & Database Init...")
from backend.database import init_db, get_db_connection
init_db()

from backend.models import ConvertedAnswerModel

# Ensure a test employee exists
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT id FROM employees LIMIT 1")
row = cursor.fetchone()
if not row:
    cursor.execute("INSERT INTO employees (name, email, password_hash) VALUES ('Test User', 'testconv@example.com', 'hash123')")
    conn.commit()
    cursor.execute("SELECT id FROM employees WHERE email='testconv@example.com'")
    row = cursor.fetchone()
employee_id = row["id"] if isinstance(row, dict) else row[0]
conn.close()

# Save converted answer
saved = ConvertedAnswerModel.save(
    employee_id=employee_id,
    question_type="Why are you leaving your current job?",
    raw_answer="Manager was terrible and micromanaged every commit.",
    professional_answer="Over the past two years, I delivered high-impact microservices. I am now seeking an environment with greater technical autonomy and ownership.",
    short_answer="I am seeking a high-trust engineering culture focused on scalable distributed systems.",
    red_flags=[{"flagged_phrase": "Manager was terrible", "risk": "Criticizing management", "safer_alternative": "Seeking greater technical autonomy"}],
    follow_up_questions=[{"question": "What leadership style allows you to thrive?", "recruiter_intent": "Assessing cultural fit"}],
    target_role="Backend Engineer",
    target_company="Stripe"
)
assert saved is not None and "id" in saved, "Failed to save converted answer"
answer_id = saved["id"]
print(f"  [OK] ConvertedAnswerModel.save() created record ID #{answer_id}")

# Fetch all
all_answers = ConvertedAnswerModel.get_all(employee_id=employee_id)
assert len(all_answers) >= 1, "Failed to retrieve saved answers"
print(f"  [OK] ConvertedAnswerModel.get_all() returned {len(all_answers)} records")

# Fetch single
single = ConvertedAnswerModel.get_by_id(answer_id, employee_id=employee_id)
assert single is not None and single["id"] == answer_id, "Failed to retrieve single converted answer"
print(f"  [OK] ConvertedAnswerModel.get_by_id() retrieved record successfully")

# Delete
deleted = ConvertedAnswerModel.delete(answer_id, employee_id=employee_id)
assert deleted is True, "Failed to delete converted answer"
after_delete = ConvertedAnswerModel.get_by_id(answer_id, employee_id=employee_id)
assert after_delete is None, "Record still exists after delete"
print(f"  [OK] ConvertedAnswerModel.delete() removed record #{answer_id}")

print("\n[TEST] 3. Testing Flask Blueprint Endpoints...")
from backend.app import create_app
app = create_app()
client = app.test_client()

# 3a. POST /api/converted-answers/convert
resp_convert = client.post("/api/converted-answers/convert", json={
    "question_type": "Explain your employment gap",
    "raw_answer": "I took a break after burnout to rest, spend time with family, and learn Next.js and cloud tools.",
    "target_role": "Full Stack Dev",
    "target_company": "Amazon"
})
assert resp_convert.status_code == 200, f"Convert API returned {resp_convert.status_code}: {resp_convert.data}"
data_convert = resp_convert.get_json()
assert data_convert.get("success") is True, "Convert API success was not True"
assert "professional_answer" in data_convert["data"], "Missing professional answer in API response"
assert "short_answer" in data_convert["data"], "Missing short answer in API response"
assert "red_flags" in data_convert["data"], "Missing red flags in API response"
assert "follow_up_questions" in data_convert["data"], "Missing follow up questions in API response"
print("  [OK] POST /api/converted-answers/convert passed")

# 3b. POST /api/converted-answers/save
resp_save = client.post("/api/converted-answers/save", json={
    "employee_id": employee_id,
    "question_type": "Explain your employment gap",
    "raw_answer": "I took a break after burnout to rest and learn new skills.",
    "professional_answer": "I intentionally took a planned sabbatical to invest in advanced cloud certifications and deepen my full-stack expertise.",
    "short_answer": "I took an intentional sabbatical dedicated to upskilling in distributed systems.",
    "red_flags": [{"flagged_phrase": "burnout", "risk": "High stress concern", "safer_alternative": "Intentional career sabbatical"}],
    "follow_up_questions": [{"question": "How did you structure your learning during this sabbatical?", "recruiter_intent": "Checking self-discipline"}],
    "target_role": "Full Stack Dev",
    "target_company": "Amazon"
})
assert resp_save.status_code == 200, f"Save API returned {resp_save.status_code}: {resp_save.data}"
data_save = resp_save.get_json()
assert data_save.get("success") is True, "Save API success was not True"
api_saved_id = data_save["data"]["id"]
print(f"  [OK] POST /api/converted-answers/save passed, record ID #{api_saved_id}")

# 3c. GET /api/converted-answers?employee_id=...
resp_get = client.get(f"/api/converted-answers?employee_id={employee_id}")
assert resp_get.status_code == 200, f"Get API returned {resp_get.status_code}"
data_get = resp_get.get_json()
assert data_get.get("success") is True and len(data_get.get("data", [])) >= 1, "Get API did not return saved answer"
print(f"  [OK] GET /api/converted-answers returned {len(data_get['data'])} records")

# 3d. DELETE /api/converted-answers/<id>?employee_id=...
resp_del = client.delete(f"/api/converted-answers/{api_saved_id}?employee_id={employee_id}")
assert resp_del.status_code == 200, f"Delete API returned {resp_del.status_code}"
data_del = resp_del.get_json()
assert data_del.get("success") is True, "Delete API success was not True"
print(f"  [OK] DELETE /api/converted-answers/{api_saved_id} passed")

print("\n[ALL TESTS PASSED SUCCESSFULLY!]")
