"""
Comprehensive End-to-End Test Suite for 2026 Trending Features
AI Employee Preparation Platform
"""
import json
import sys
from backend.app import create_app

if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

def run_tests():
    app = create_app()
    app.config["TESTING"] = True
    client = app.test_client()

    print("==================================================")
    print("RUNNING 2026 FEATURE SUITE VERIFICATION")
    print("==================================================")

    student_id = 19  # Rahul Sharma seeded test profile

    # 1. Main Dashboard Summary
    print("\n[1/7] Testing Main Dashboard Summary...")
    res = client.get(f"/api/dashboard/summary?employee_id={student_id}")
    assert res.status_code == 200, f"Dashboard summary failed: {res.status_code}"
    data = res.get_json()
    assert data["success"] is True
    summary = data["data"]
    assert "stats" in summary
    assert "trend_insights" in summary
    assert "session_trend" in summary
    print(f"  [OK] Dashboard Stats: Interviews={summary['stats']['interviews_taken']}, Avg Score={summary['stats']['avg_score']}%, Resume={summary['stats']['resume_score']}%, AI Fluency={summary['stats']['ai_fluency_score']}%")
    print(f"  [OK] Active Trends: {len(summary['trend_insights'])} curated insights returned")
    print(f"  [OK] Session History: {len(summary['session_trend'])} historical sessions returned")

    # 2. Smart Prep Roadmap
    print("\n[2/7] Testing Smart Prep Roadmap...")
    res = client.get(f"/api/roadmap/smart?employee_id={student_id}")
    assert res.status_code == 200
    r_data = res.get_json()
    assert r_data["success"] is True
    roadmap = r_data["data"]
    print(f"  [OK] Current Roadmap: {roadmap['company_name']} - {roadmap['target_role']} ({roadmap['duration_days']} Days)")
    print(f"  [OK] Tasks loaded: {len(roadmap.get('tasks', []))} days/tasks")

    # Generate custom roadmap for 14 days
    res = client.post("/api/roadmap/smart/generate", json={
        "employee_id": student_id,
        "company_name": "Microsoft",
        "company_slug": "microsoft",
        "target_role": "Backend Engineer",
        "duration_days": 14
    })
    assert res.status_code == 200
    gen_data = res.get_json()
    assert gen_data["success"] is True
    gen_roadmap = gen_data["data"]
    print(f"  [OK] AI Generated Roadmap: ID #{gen_roadmap['id']}, Tasks={len(gen_roadmap['tasks'])}")

    # Toggle task completion
    first_task = gen_roadmap['tasks'][0]
    res = client.post("/api/roadmap/smart/task/toggle", json={
        "task_id": first_task["id"],
        "employee_id": student_id
    })
    assert res.status_code == 200
    toggle_data = res.get_json()
    assert toggle_data["success"] is True
    print(f"  [OK] Task #{first_task['id']} toggled: New progress = {toggle_data.get('progress_percent', 0)}%")

    # 3. Trending Resume Templates & ATS
    print("\n[3/7] Testing Trending Resume Templates & ATS...")
    res = client.get("/api/resume/templates")
    assert res.status_code == 200
    t_data = res.get_json()
    assert t_data["success"] is True
    assert len(t_data["templates"]) >= 3
    print(f"  [OK] Loaded {len(t_data['templates'])} trending templates:")
    for t in t_data["templates"]:
        print(f"    - [{t['template_id']}] {t['name']} ({t['badge_text']})")

    # Bullet rewriter
    res = client.post("/api/resume/rewrite-bullet", json={
        "bullet_text": "Worked on database speed and fixed bugs",
        "target_role": "Backend Engineer"
    })
    assert res.status_code == 200
    rw_data = res.get_json()
    assert rw_data["success"] is True
    print(f"  [OK] Bullet Rewritten: \"{rw_data['rewritten_bullet']}\"")

    # ATS Scoring
    res = client.post("/api/resume/score-ats", json={
        "resume_data": {"name": "Rahul Sharma", "summary": "Experienced Python Backend Engineer. Architected REST APIs, optimized SQL queries by 40%, deployed microservices using Docker."},
        "target_role": "Backend Engineer",
        "job_description": "We are seeking a Backend Engineer with Python, Docker, SQL, and REST APIs."
    })
    assert res.status_code == 200
    ats_data = res.get_json()
    assert ats_data["success"] is True
    print(f"  [OK] ATS Match Score: {ats_data['overall_score']}% (Matched {len(ats_data.get('detected_keywords', []))} keywords)")

    # Save version
    res = client.post("/api/resume/versions/save", json={
        "employee_id": student_id,
        "version_name": "Microsoft Backend Lead v1",
        "template_name": "modern-single",
        "target_role": "Backend Engineer",
        "target_company": "Microsoft",
        "resume_data": {"name": "Rahul Sharma", "headline": "Backend Engineer"},
        "score": ats_data["overall_score"]
    })
    assert res.status_code == 200
    v_data = res.get_json()
    assert v_data["success"] is True
    print(f"  [OK] Saved resume version #{v_data['data']['id']}")

    # 4. AI Fluency Round
    print("\n[4/7] Testing 2026 AI Fluency Round...")
    res = client.get("/api/ai-fluency/questions")
    assert res.status_code == 200
    q_data = res.get_json()
    assert q_data["success"] is True
    assert len(q_data["questions"]) >= 3
    print(f"  [OK] AI Fluency Questions: {len(q_data['questions'])} loaded")

    # Evaluate answer
    sample_q = q_data["questions"][0]
    res = client.post("/api/ai-fluency/evaluate", json={
        "employee_id": student_id,
        "question_id": sample_q["id"],
        "question_text": sample_q["question_text"],
        "category": sample_q["category"],
        "candidate_answer": "When facing this race condition bug, I used GitHub Copilot to scaffold asynchronous test harness scenarios. However, I never trust AI output blindly, so I added invariant assertions and verified edge cases with property-based fuzz testing. This reduced turnaround time by 50% while guaranteeing zero hallucinated logic in production."
    })
    assert res.status_code == 200
    ev = res.get_json()
    assert ev["success"] is True
    print(f"  [OK] AI Fluency Evaluation Overall: {ev['overall_score']}%")
    print(f"    - Tool Integration: {ev['ai_tool_score']}%")
    print(f"    - Verification Mindset: {ev['verification_score']}%")
    print(f"    - Velocity: {ev['velocity_score']}%")
    print(f"    - Authenticity: {ev['communication_score']}%")
    print(f"    - Natural AI Rewrite: \"{ev['rewrite_sample'][:80]}...\"")

    # 5. Present-Past-Future 60s Answer Builder
    print("\n[5/7] Testing Present-Past-Future 60s Pitch Builder...")
    res = client.get("/api/answer-builder/questions")
    assert res.status_code == 200
    ab_q = res.get_json()
    assert ab_q["success"] is True
    print(f"  [OK] Preset Questions: {len(ab_q['questions'])} available")

    # Analyze 3-box pitch
    res = client.post("/api/answer-builder/analyze", json={
        "employee_id": student_id,
        "question_title": "Tell me about yourself",
        "present_text": "Currently, I am a final-year Computer Science student specializing in scalable web systems with Python FastAPI and PostgreSQL. Right now, I'm developing microservice APIs for real-time employee workflows.",
        "past_text": "Previously, during my engineering internship, I re-architected an asynchronous pipeline that cut query latencies by 42% and handled 100k daily requests with zero downtime. I also led our 4-person hackathon team to 1st place.",
        "future_text": "Looking forward, I want to join Google's Cloud Platform team because of your commitment to robust distributed systems. In my first 90 days, I plan to leverage my API performance experience to contribute directly to your cloud deployment features.",
        "target_role": "Full Stack Software Engineer",
        "target_company": "Google"
    })
    assert res.status_code == 200
    ab_eval = res.get_json()
    assert ab_eval["success"] is True
    print(f"  [OK] Word Count: {ab_eval['word_count']} words (~{ab_eval['speaking_time_seconds']}s) -> Status: {ab_eval['length_status']}")
    print(f"  [OK] Structure Score: {ab_eval['structure_score']}/100")
    print(f"  [OK] AI Optimized Pitch: \"{ab_eval['ai_optimized_pitch'][:80]}...\"")

    # Save to library
    res = client.post("/api/answer-builder/save", json={
        "employee_id": student_id,
        "question_key": "tell-me-about-yourself",
        "question_title": "Tell me about yourself",
        "target_role": "Full Stack Software Engineer",
        "target_company": "Google",
        "present_text": "Currently...",
        "past_text": "Previously...",
        "future_text": "Looking forward...",
        "combined_text": "Full text...",
        "speaking_time_seconds": ab_eval['speaking_time_seconds'],
        "structure_score": ab_eval['structure_score'],
        "ai_optimized_pitch": ab_eval['ai_optimized_pitch']
    })
    assert res.status_code == 200
    save_pitch = res.get_json()
    assert save_pitch["success"] is True
    print(f"  [OK] Saved to pitch library ID #{save_pitch['id']}")

    # 6. Admin CMS Endpoints
    print("\n[6/7] Testing Admin CMS Endpoints (Trends, Templates, Fluency)...")
    # Trends CMS
    res = client.get("/api/admin/trends")
    assert res.status_code == 200
    tr_list = res.get_json()
    assert tr_list["success"] is True
    print(f"  [OK] Admin Trends: {len(tr_list['trends'])} items")

    # Add trend
    res = client.post("/api/admin/trends", json={
        "title": "Agentic Coding Literacy",
        "category": "AI Fluency",
        "role_tag": "All",
        "company_tag": "All",
        "content": "Interviewers expect awareness of agentic loops and tool calling in IDEs.",
        "actionable_tip": "Explain how you review agentic edits with unit tests and git diff scrutiny.",
        "priority": 1
    })
    assert res.status_code == 201
    new_tr = res.get_json()
    print(f"  [OK] Added trend insight ID #{new_tr['id']}")

    # Templates CMS
    res = client.get("/api/admin/templates")
    assert res.status_code == 200
    tmpl_list = res.get_json()
    assert tmpl_list["success"] is True
    print(f"  [OK] Admin Templates: {len(tmpl_list['templates'])} items")

    # Fluency CMS
    res = client.get("/api/admin/ai-fluency-questions")
    assert res.status_code == 200
    fl_list = res.get_json()
    assert fl_list["success"] is True
    print(f"  [OK] Admin Fluency Questions: {len(fl_list['questions'])} items")

    # 7. Preserved Existing Core Modules Check
    print("\n[7/7] Verifying Preserved Existing Features...")
    # Check companies
    res = client.get("/api/companies")
    assert res.status_code == 200
    comps = res.get_json()
    print(f"  [OK] Companies API preserved: {len(comps.get('companies', []))} companies")

    # Check aptitude
    res = client.post("/api/aptitude/start", json={"employee_id": student_id, "refresh": True})
    assert res.status_code in (200, 201)
    apt_data = res.get_json()
    assert apt_data["success"] is True
    print(f"  [OK] Aptitude engine preserved: {len(apt_data.get('questions', []))} questions generated")

    # Check analyzer
    res = client.post("/api/resume/extract-skills", json={
        "employee_id": student_id,
        "resume_text": "Python, SQL, Docker, React, REST API development"
    })
    assert res.status_code == 200
    ex_data = res.get_json()
    assert ex_data["success"] is True
    print(f"  [OK] Resume Analyzer / Extractor preserved: {len(ex_data.get('detected', []))} skills detected")

    print("\n==================================================")
    print("ALL 7 CORE MODULES & CMS PASS 100% SUITE VERIFICATION!")
    print("==================================================")

if __name__ == "__main__":
    run_tests()
