"""
Test Suite for Achievement Vault Feature.
Tests:
- AI STAR transformation (with heuristic fallback)
- Model operations (save, retrieve, update, delete)
- API endpoints for Flask & FastAPI
"""
import sys
import os
import json

# Ensure project root is in sys.path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from backend.database import init_db, get_db_connection
from backend.models import AchievementModel, GamificationModel
from backend.services.ai_service import convert_achievement_to_star, generate_fallback_star_achievement
from backend.app import create_app


def run_tests():
    print("==================================================")
    print("STARTING ACHIEVEMENT VAULT TEST SUITE")
    print("==================================================")

    init_db()

    # 1. Test AI Heuristic STAR Transformation
    print("\n[TEST 1] AI STAR Transformation Heuristic...")
    sample_input = {
        "title": "Migrated Monolithic Billing to Event-Driven Microservices",
        "raw_description": "Our legacy billing system suffered severe concurrency deadlocks during month-end invoice processing. I decomposed the monolith into Kafka-driven microservices with Redis idempotency caches, resolved deadlock issues, and coordinated with DevOps to automate zero-downtime deployment pipelines.",
        "metrics_result": "Cut processing latency by 68%, eliminated concurrency deadlocks, and scaled throughput to 25,000 invoices/minute",
        "skills_used": "Python, FastAPI, Apache Kafka, Redis, Docker, AWS"
    }

    star_output = convert_achievement_to_star(sample_input)
    assert star_output is not None, "STAR conversion returned None"
    assert len(star_output.get("star_situation", "")) > 20, "Situation is too short"
    assert len(star_output.get("star_task", "")) > 20, "Task is too short"
    assert len(star_output.get("star_action", "")) > 20, "Action is too short"
    assert len(star_output.get("star_result", "")) > 20, "Result is too short"
    assert isinstance(star_output.get("mapped_questions"), list), "Mapped questions must be a list"
    assert len(star_output["mapped_questions"]) >= 3, "Expected at least 3 mapped questions"
    print(" [PASS] STAR conversion generated valid Situation, Task, Action, Result, and Mapped Questions.")
    for idx, q in enumerate(star_output["mapped_questions"]):
        tag = q.get("tag", "General") if isinstance(q, dict) else "Q"
        text = q.get("question") if isinstance(q, dict) else q
        print(f"        Q{idx+1} [{tag}]: {text}")

    # 2. Test AchievementModel Database CRUD
    print("\n[TEST 2] AchievementModel CRUD Operations...")
    test_emp_id = 1
    
    # Save new achievement
    save_data = dict(sample_input)
    save_data.update(star_output)
    save_res = AchievementModel.save(test_emp_id, save_data)
    assert save_res.get("success"), f"Save failed: {save_res}"
    achievement_id = save_res["achievement"]["id"]
    print(f" [PASS] Achievement saved successfully with ID={achievement_id}")

    # Get all achievements
    all_achievements = AchievementModel.get_all(test_emp_id)
    assert len(all_achievements) >= 1, "Expected at least 1 achievement in list"
    found = any(a["id"] == achievement_id for a in all_achievements)
    assert found, "Saved achievement not found in get_all"
    print(f" [PASS] get_all returned {len(all_achievements)} achievements including ID={achievement_id}")

    # Get by ID
    single = AchievementModel.get_by_id(achievement_id, test_emp_id)
    assert single is not None, "get_by_id returned None"
    assert single["title"] == sample_input["title"], "Title mismatch"
    assert len(single["mapped_questions"]) >= 3, "Questions deserialization failed"
    print(" [PASS] get_by_id successfully retrieved record and parsed JSON mapped questions.")

    # Update achievement
    update_data = dict(single)
    update_data["metrics_result"] = "Updated: 75% latency reduction and zero incidents in 12 months"
    update_res = AchievementModel.save(test_emp_id, update_data)
    assert update_res.get("success"), "Update failed"
    updated_single = AchievementModel.get_by_id(achievement_id, test_emp_id)
    assert "75% latency" in updated_single["metrics_result"], "Updated field not persisted"
    print(" [PASS] Updated existing achievement successfully.")

    # 3. Test Flask HTTP Endpoints
    print("\n[TEST 3] Testing Flask API Routes...")
    app = create_app()
    client = app.test_client()

    # GET /api/achievements
    res_get = client.get(f"/api/achievements?employee_id={test_emp_id}")
    assert res_get.status_code == 200, f"GET returned {res_get.status_code}"
    get_json = res_get.get_json()
    assert get_json.get("success"), "GET failed"
    print(f" [PASS] GET /api/achievements returned {len(get_json['data'])} records.")

    # POST /api/achievements/save (Auto STAR transformation on backend)
    raw_payload = {
        "employee_id": test_emp_id,
        "title": "Automated Multi-Region Disaster Recovery in AWS",
        "raw_description": "Our database backups were manual and untested for disaster recovery. I designed an automated Terraform pipeline with cross-region S3 replication and automated failover simulations.",
        "metrics_result": "Reduced RTO from 6 hours to 12 minutes, achieving SOC2 compliance",
        "skills_used": "Terraform, AWS Route53, PostgreSQL, Python, Bash"
    }
    res_post = client.post("/api/achievements/save", json=raw_payload)
    assert res_post.status_code == 200, f"POST returned {res_post.status_code}: {res_post.data}"
    post_json = res_post.get_json()
    assert post_json.get("success"), "POST save failed"
    saved_auto = post_json["data"]
    assert len(saved_auto.get("star_situation", "")) > 10, "Auto STAR situation missing"
    assert len(saved_auto.get("star_action", "")) > 10, "Auto STAR action missing"
    assert len(saved_auto.get("mapped_questions", [])) >= 3, "Auto STAR questions missing"
    print(f" [PASS] POST /api/achievements/save auto-generated STAR content with ID={saved_auto['id']}")

    # DELETE /api/achievements/<id>
    del_id = saved_auto["id"]
    res_del = client.delete(f"/api/achievements/{del_id}?employee_id={test_emp_id}")
    assert res_del.status_code == 200, f"DELETE returned {res_del.status_code}"
    assert res_del.get_json().get("success"), "DELETE success flag false"
    # Verify deletion
    after_del = AchievementModel.get_by_id(del_id, test_emp_id)
    assert after_del is None, "Record was not deleted"
    print(f" [PASS] DELETE /api/achievements/{del_id} successfully deleted record.")

    print("\n==================================================")
    print("ALL ACHIEVEMENT VAULT TESTS PASSED SUCCESSFULLY!")
    print("==================================================")


if __name__ == "__main__":
    run_tests()
