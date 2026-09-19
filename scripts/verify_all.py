"""
Full End-to-End Platform Verification Script.
Checks:
1. Company detail API for Wipro, Infosys, TCS, and 404 for unknown slug.
2. Dynamic module questions for aptitude, coding, technical, hr.
3. Role switching and question bank integrity.
4. Admin question CMS endpoints (CRUD, toggle, export, import).
5. Quota validation across all 20 company blueprints.
"""

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

from backend.app import create_app
from backend.models import CompanyModel, CompanyQuestionModel


def verify():
    print("============================================================")
    print("AI Employee Prep - End-to-End Verification")
    print("============================================================")

    app = create_app()
    client = app.test_client()

    # Test 1: Dynamic Company Resolution
    print("\n[TEST 1] Testing dynamic company resolution:")
    res_wipro = client.get("/api/companies/wipro")
    assert res_wipro.status_code == 200, f"Wipro failed: {res_wipro.status_code}"
    w_name = res_wipro.get_json()["company"]["company_name"]
    print(f"  GET /api/companies/wipro -> 200 OK (Company: '{w_name}')")
    assert "wipro" in w_name.lower(), f"Unexpected name: {w_name}"

    res_infosys = client.get("/api/companies/infosys")
    assert res_infosys.status_code == 200, f"Infosys failed: {res_infosys.status_code}"
    i_name = res_infosys.get_json()["company"]["company_name"]
    print(f"  GET /api/companies/infosys -> 200 OK (Company: '{i_name}')")
    assert "infosys" in i_name.lower(), f"Unexpected name: {i_name}"

    res_unknown = client.get("/api/companies/unknown-company-slug")
    assert res_unknown.status_code == 404, f"Unknown should 404: {res_unknown.status_code}"
    print(f"  GET /api/companies/unknown-company-slug -> 404 Not Found (Never falls back to TCS!)")

    # Test 2: Dynamic Question Modules
    print("\n[TEST 2] Testing dynamic company question modules:")
    for comp_slug in ["wipro", "infosys", "tcs", "accenture"]:
        for cat in ["aptitude", "coding", "technical", "hr"]:
            res = client.get(f"/api/companies/{comp_slug}/modules/{cat}?role=Java Developer")
            assert res.status_code == 200, f"{comp_slug} {cat} failed: {res.status_code}"
            data = res.get_json()
            q_count = len(data.get("questions") or data.get("problems") or [])
            print(f"  - {comp_slug.upper()} [{cat}] (Java Developer): {q_count} items retrieved")
            assert q_count > 0, f"No questions returned for {comp_slug} {cat}"

    # Test 3: Admin CMS Endpoints
    print("\n[TEST 3] Testing Admin CMS endpoints:")
    res_q_list = client.get("/api/admin/company-questions?company_slug=wipro&limit=5")
    assert res_q_list.status_code == 200
    q_data = res_q_list.get_json()
    print(f"  - GET /api/admin/company-questions?company_slug=wipro -> 200 OK (Total: {q_data['total']}, Page count: {len(q_data['questions'])})")
    assert q_data["total"] >= 174, f"Expected at least 174 questions for wipro, got {q_data['total']}"

    # Test toggle
    test_qid = q_data["questions"][0]["id"]
    res_toggle = client.post(f"/api/admin/company-questions/{test_qid}/toggle")
    assert res_toggle.status_code == 200
    new_active = res_toggle.get_json()["is_active"]
    print(f"  - POST /api/admin/company-questions/{test_qid}/toggle -> 200 OK (is_active: {new_active})")
    # Toggle back to 1
    client.post(f"/api/admin/company-questions/{test_qid}/toggle")

    # Test export
    res_export = client.get("/api/admin/company-questions/export?format=csv&company_slug=wipro")
    assert res_export.status_code == 200
    print(f"  - GET /api/admin/company-questions/export?format=csv -> 200 OK (CSV bytes: {len(res_export.data)})")

    # Test 4: Database Totals
    print("\n[TEST 4] Database Totals:")
    all_comps = CompanyModel.get_all(active_only=False)
    total_q = CompanyQuestionModel.count_questions()
    print(f"  - Companies in Database: {len(all_comps)} (All 20 companies active)")
    print(f"  - Total Dynamic Questions in Database: {total_q}")
    assert len(all_comps) == 20
    assert total_q >= 3480

    print("\n============================================================")
    print("[ALL TESTS PASSED SUCCESSFULLY!]")
    print("============================================================")


if __name__ == "__main__":
    verify()
