import json
import random
from flask import Blueprint, request, jsonify
from backend.models import (
    CompanyPrepModel, JobRoleModel, UserPreparationModel,
    EmployeeModel, TestAttemptModel, QuestionModel, AdminModel,
    CompanyModel, CompanyQuestionModel
)
from backend.data.aptitude_bank import MASTER_APTITUDE_BANK
from backend.data.coding_bank import MASTER_CODING_BANK
from backend.data.interview_bank import MASTER_INTERVIEW_BANK
from backend.data.company_questions_bank import (
    COMPANY_QUESTIONS_BANK,
    get_company_bank,
    get_company_aptitude_questions,
    get_company_technical_questions,
    get_company_coding_problems,
    get_company_hr_questions
)

from backend.data.company_intel import get_company_intel

company_bp = Blueprint("company", __name__)


def _resolve_company(slug: str):
    """Fetches company from dynamic companies table or fallback to company_prep."""
    if not slug:
        return None
    comp = CompanyModel.get_by_slug(slug)
    if not comp:
        comp = CompanyPrepModel.get_by_slug(slug)
    if not comp or comp.get("is_active") == 0:
        return None

    # Normalize fields
    if "name" in comp and "company_name" not in comp:
        comp["company_name"] = comp["name"]
    if "company_name" in comp and "name" not in comp:
        comp["name"] = comp["company_name"]
    if "industry" in comp and "category" not in comp:
        comp["category"] = comp["industry"]
    return comp


@company_bp.route("/api/companies", methods=["GET"])
def get_companies():
    """
    Returns catalog of all supported active companies with filtering.
    """
    try:
        search = request.args.get("search", "").lower().strip()
        category = request.args.get("category", "")
        difficulty = request.args.get("difficulty", "")

        companies = CompanyModel.get_all(active_only=True)
        if not companies:
            companies = CompanyPrepModel.get_all(search=search, category=category, difficulty=difficulty)
        else:
            # Normalize and filter
            filtered = []
            for c in companies:
                if "company_name" not in c and "name" in c:
                    c["company_name"] = c["name"]
                if "category" not in c and "industry" in c:
                    c["category"] = c["industry"]

                match_search = not search or search in c.get("company_name", "").lower() or search in c.get("description", "").lower() or search in c.get("common_roles", "").lower()
                match_cat = not category or category == "All" or category in c.get("category", "")
                match_diff = not difficulty or difficulty == "All" or difficulty in c.get("difficulty", "")

                if match_search and match_cat and match_diff:
                    filtered.append(c)
            companies = filtered

        return jsonify({
            "success": True,
            "count": len(companies),
            "companies": companies
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching companies: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>", methods=["GET"])
def get_company_detail(slug: str):
    """
    Returns full company hiring syllabus, rounds, intel, and available job roles.
    """
    try:
        comp = _resolve_company(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        roles = JobRoleModel.get_roles_for_company(slug)
        comp["job_roles"] = roles
        comp["intel"] = get_company_intel(slug)

        return jsonify({
            "success": True,
            "company": comp
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching company details: {str(e)}"}), 500



@company_bp.route("/api/companies/<slug>/roles", methods=["GET"])
def get_company_roles(slug: str):
    """
    Returns all job roles specific to the target company.
    """
    try:
        roles = JobRoleModel.get_roles_for_company(slug)
        return jsonify({
            "success": True,
            "roles": roles
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching company roles: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>/select", methods=["POST"])
def select_target_company(slug: str):
    """
    Selects target company for the candidate:
    - Stores company + role in database.
    - Preserves independent per-company progress.
    - Returns active company preparation state.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id") or request.args.get("employee_id", type=int)
        role = (data.get("role") or data.get("target_role") or "Software Engineer").strip()

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        # Update candidate's active career goal in employees table
        EmployeeModel.set_career_goal(int(employee_id), comp["company_name"], role)

        # Get or create specific user_preparation row
        prep = UserPreparationModel.get_or_create(int(employee_id), slug, comp["company_name"], role)

        return jsonify({
            "success": True,
            "message": f"Target company updated to {comp['company_name']} — {role}!",
            "company": comp,
            "selected_role": role,
            "preparation": prep
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error selecting company: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>/progress", methods=["GET"])
def get_company_progress(slug: str):
    """
    Returns the candidate's isolated progress for the specified company.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        prep = UserPreparationModel.get_user_company_progress(employee_id, slug)
        attempts = TestAttemptModel.get_attempts_for_user(employee_id, company_slug=slug, limit=10)

        return jsonify({
            "success": True,
            "company": comp,
            "preparation": prep,
            "recent_attempts": attempts
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching company progress: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>/modules/<module_name>", methods=["GET"])
def get_company_module_data(slug: str, module_name: str):
    """
    Returns company + job role tailored preparation data for the 8 core modules:
    1. aptitude
    2. coding
    3. technical
    4. hr
    5. interview
    6. resume
    7. skills
    8. roadmap
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        job_role = request.args.get("role", "").strip() or "Software Engineer"

        comp = _resolve_company(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        emp = EmployeeModel.get_by_id(employee_id) if employee_id else None
        prep = UserPreparationModel.get_user_company_progress(employee_id, slug) if employee_id else None

        role_lower = job_role.lower()

        # 1. Aptitude Module Data (Dynamic Database Questions)
        if module_name == "aptitude":
            db_qs = CompanyQuestionModel.get_questions(company_slug=slug, category="aptitude", role=job_role, active_only=True)
            if db_qs:
                selected_qs = [
                    {
                        "id": q["id"],
                        "category": (q.get("extra") or {}).get("section", "Quantitative Ability"),
                        "question": q["question"],
                        "options": q.get("options", []),
                        "correct_answer": q.get("correct_answer"),
                        "explanation": q.get("explanation")
                    } for q in db_qs
                ]
            else:
                comp_qs = get_company_aptitude_questions(slug, shuffle=True)
                general_matching = [
                    q for q in MASTER_APTITUDE_BANK
                    if "all" in [r.lower() for r in q.get("roles", [])] or any(r in role_lower for r in [x.lower() for x in q.get("roles", [])])
                ]
                random.shuffle(general_matching)
                rem_needed = max(0, 15 - len(comp_qs))
                filler = [q for q in general_matching if q["id"] not in {x["id"] for x in comp_qs}][:rem_needed]
                selected_qs = comp_qs + filler

            return jsonify({
                "success": True,
                "module": "aptitude",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "pattern": comp.get("aptitude_pattern", "Quantitative and Logical reasoning"),
                "duration_minutes": 15,
                "total_questions": len(selected_qs),
                "questions": selected_qs,
                "current_progress": prep.get("aptitude_progress", 0.0) if prep else 0.0
            }), 200

        # 2. Coding Module Data (Dynamic Database Problems)
        elif module_name == "coding":
            db_problems = CompanyQuestionModel.get_questions(company_slug=slug, category="coding", role=job_role, active_only=True)
            if db_problems:
                selected_problems = [
                    {
                        "id": p["id"],
                        "title": p["question"].split("] ")[-1].split(":")[0] if "]" in p["question"] else p["question"][:50],
                        "difficulty": p.get("difficulty", "Medium"),
                        "description": p["question"],
                        "sample_input": (p.get("extra") or {}).get("sample_input", ""),
                        "sample_output": (p.get("extra") or {}).get("sample_output", ""),
                        "starter_code": (p.get("extra") or {}).get("starter_code", ""),
                        "explanation": p.get("explanation", "")
                    } for p in db_problems
                ]
            else:
                comp_problems = get_company_coding_problems(slug, shuffle=True)
                gen_matching = [
                    p for p in MASTER_CODING_BANK
                    if any(slug in c.lower() for c in p.get("companies", [])) or comp["company_name"].lower() in [c.lower() for c in p.get("companies", [])]
                ]
                if not gen_matching:
                    gen_matching = list(MASTER_CODING_BANK)
                random.shuffle(gen_matching)
                rem_needed = max(0, 10 - len(comp_problems))
                filler = [p for p in gen_matching if p["id"] not in {x["id"] for x in comp_problems}][:rem_needed]
                selected_problems = comp_problems + filler

            return jsonify({
                "success": True,
                "module": "coding",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "coding_pattern": comp.get("coding_pattern", "Algorithmic Challenges"),
                "problems": selected_problems,
                "current_progress": prep.get("coding_progress", 0.0) if prep else 0.0
            }), 200

        # 3. Technical Questions Module Data
        elif module_name == "technical":
            db_tech = CompanyQuestionModel.get_questions(company_slug=slug, category="technical", role=job_role, active_only=True)
            if db_tech:
                selected_tech = [
                    {
                        "id": q["id"],
                        "category": (q.get("extra") or {}).get("topic", "Technical Domain"),
                        "difficulty": q.get("difficulty", "Medium"),
                        "question": q["question"],
                        "explanation": q.get("explanation", "")
                    } for q in db_tech
                ]
            else:
                comp_tech = get_company_technical_questions(slug, shuffle=True)
                db_tech_legacy = QuestionModel.get_questions("technical", company_slug=slug, role_name=job_role, limit=30) or []
                bank_tech = [
                    {
                        "id": q["id"],
                        "category": q.get("category", "Technical"),
                        "difficulty": "Medium",
                        "question": q["question"],
                        "explanation": q.get("guidance", "Focus on practical software engineering design.")
                    }
                    for q in MASTER_INTERVIEW_BANK
                    if "tech" in q.get("category", "").lower() or "sys" in q.get("category", "").lower() or "sec" in q.get("category", "").lower()
                ]
                extra_pool = db_tech_legacy + bank_tech
                random.shuffle(extra_pool)
                rem_needed = max(0, 15 - len(comp_tech))
                filler = [q for q in extra_pool if q["id"] not in {x["id"] for x in comp_tech}][:rem_needed]
                selected_tech = comp_tech + filler

            return jsonify({
                "success": True,
                "module": "technical",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "technical_focus": comp.get("technical_focus", "Core Computer Science & Architecture"),
                "questions": selected_tech,
                "current_progress": prep.get("technical_progress", 0.0) if prep else 0.0
            }), 200

        # 4. HR Interview Module Data
        elif module_name == "hr":
            db_hr = CompanyQuestionModel.get_questions(company_slug=slug, category="hr", role=job_role, active_only=True)
            if db_hr:
                hr_questions = [
                    {
                        "id": q["id"],
                        "category": "HR & Behavioral",
                        "question": q["question"],
                        "tips": q.get("explanation", comp.get("hr_tips", "Frame using STAR method."))
                    } for q in db_hr
                ]
            else:
                comp_hr = get_company_hr_questions(slug, shuffle=True)
                hr_questions = list(comp_hr)

            return jsonify({
                "success": True,
                "module": "hr",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "hr_tips": comp.get("hr_tips", "Adhere to core values and clear communication."),
                "questions": hr_questions,
                "current_progress": prep.get("hr_progress", 0.0) if prep else 0.0
            }), 200

        # 5. AI Mock Interview Module Data
        elif module_name == "interview":
            db_ai = CompanyQuestionModel.get_questions(company_slug=slug, category="ai_interview", role=job_role, active_only=True)
            return jsonify({
                "success": True,
                "module": "interview",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "hiring_rounds": comp.get("hiring_rounds", "Round 1: OA | Round 2: Technical | Round 3: HR"),
                "questions": db_ai,
                "current_progress": prep.get("interview_progress", 0.0) if prep else 0.0
            }), 200

        # 6. Resume Module Data
        elif module_name == "resume":
            rec_skills = [s.strip() for s in (comp.get("recommended_skills") or "").split(",") if s.strip()]
            return jsonify({
                "success": True,
                "module": "resume",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "recommended_skills": rec_skills,
                "ats_keywords": rec_skills + [job_role, comp["company_name"], "System Design", "Agile", "Unit Testing"],
                "current_progress": prep.get("resume_progress", 0.0) if prep else 0.0
            }), 200

        # 7. Skill Assessment Module Data
        elif module_name == "skills":
            rec_skills = [s.strip() for s in (comp.get("recommended_skills") or "").split(",") if s.strip()]
            candidate_skills = [s.strip().lower() for s in (emp.get("skills", "") if emp else "").split(",") if s.strip()]

            matched = [s for s in rec_skills if any(cs in s.lower() or s.lower() in cs for cs in candidate_skills)]
            missing = [s for s in rec_skills if not any(cs in s.lower() or s.lower() in cs for cs in candidate_skills)]

            return jsonify({
                "success": True,
                "module": "skills",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "benchmark_skills": rec_skills,
                "strong_skills": matched if matched else ["Core Programming"],
                "focus_skills": missing if missing else ["Advanced System Architecture"],
                "current_progress": prep.get("skills_progress", 0.0) if prep else 0.0
            }), 200

        # 8. Learning Roadmap Module Data
        elif module_name == "roadmap":
            return jsonify({
                "success": True,
                "module": "roadmap",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "roadmap": comp.get("roadmap", []),
                "current_progress": prep.get("roadmap_progress", 0.0) if prep else 0.0
            }), 200

        else:
            return jsonify({"success": False, "message": f"Unknown module: {module_name}"}), 404

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching module data: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>/questions", methods=["GET"])
def get_company_all_questions(slug: str):
    """
    Returns full categorized question sets specifically curated for this company from the database.
    """
    try:
        comp = _resolve_company(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        role = request.args.get("role")
        apt = CompanyQuestionModel.get_questions(company_slug=slug, category="aptitude", role=role, active_only=True)
        tech = CompanyQuestionModel.get_questions(company_slug=slug, category="technical", role=role, active_only=True)
        code = CompanyQuestionModel.get_questions(company_slug=slug, category="coding", role=role, active_only=True)
        hr = CompanyQuestionModel.get_questions(company_slug=slug, category="hr", role=role, active_only=True)
        ai_intv = CompanyQuestionModel.get_questions(company_slug=slug, category="ai_interview", role=role, active_only=True)

        return jsonify({
            "success": True,
            "company_name": comp["company_name"],
            "slug": slug,
            "aptitude": apt if apt else get_company_aptitude_questions(slug, shuffle=True),
            "technical": tech if tech else get_company_technical_questions(slug, shuffle=True),
            "coding": code if code else get_company_coding_problems(slug, shuffle=True),
            "hr": hr if hr else get_company_hr_questions(slug, shuffle=True),
            "ai_interview": ai_intv
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@company_bp.route("/api/companies/<slug>/random-question", methods=["GET"])
def get_company_random_question(slug: str):
    """
    Returns a single fresh randomized question for this company in the specified module.
    """
    try:
        comp = _resolve_company(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        q_type = request.args.get("type", "aptitude").strip().lower()
        exclude_id = request.args.get("exclude_id", "").strip()

        pool = CompanyQuestionModel.get_questions(company_slug=slug, category=q_type, active_only=True)
        if not pool:
            if q_type == "aptitude": pool = get_company_aptitude_questions(slug, shuffle=False)
            elif q_type == "coding": pool = get_company_coding_problems(slug, shuffle=False)
            elif q_type == "technical": pool = get_company_technical_questions(slug, shuffle=False)
            else: pool = get_company_hr_questions(slug, shuffle=False)

        if exclude_id:
            filtered = [q for q in pool if str(q.get("id")) != str(exclude_id)]
            if filtered:
                pool = filtered

        if not pool:
            return jsonify({"success": False, "message": "No questions available."}), 404

        picked = random.choice(pool)
        return jsonify({
            "success": True,
            "company": comp["company_name"],
            "type": q_type,
            "question": picked
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@company_bp.route("/api/companies/compare", methods=["POST"])
def compare_companies():
    """
    Compares 2 selected companies across hiring rounds, difficulty, skills, and patterns.
    """
    try:
        data = request.get_json() or {}
        slug1 = data.get("slug1", "").strip().lower()
        slug2 = data.get("slug2", "").strip().lower()

        if not slug1 or not slug2:
            return jsonify({"success": False, "message": "Both slug1 and slug2 are required."}), 400

        result = CompanyPrepModel.compare_companies(slug1, slug2)
        if not result.get("success"):
            return jsonify(result), 404

        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error comparing companies: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>/recommendations", methods=["GET"])
def get_company_recommendations(slug: str):
    """
    Analyzes candidate profile against company benchmarks and returns targeted AI recommendations.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        job_role = request.args.get("role", "")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        result = CompanyPrepModel.get_role_recommendations(employee_id, slug, job_role)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error generating recommendations: {str(e)}"}), 500


@company_bp.route("/api/companies/admin/save", methods=["POST"])
def admin_save_company():
    """
    Admin endpoint to create or update a company preparation blueprint.
    """
    try:
        data = request.get_json() or {}
        slug = data.get("slug", "").strip().lower()
        company_name = data.get("company_name", "").strip()

        if not slug or not company_name:
            return jsonify({"success": False, "message": "slug and company_name are required."}), 400

        CompanyPrepModel.save_or_update(data)
        AdminModel.log_action("admin@prep.com", "SAVE_COMPANY", f"Saved company blueprint: {company_name} ({slug})")

        return jsonify({
            "success": True,
            "message": f"Company '{company_name}' saved successfully."
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving company: {str(e)}"}), 500


@company_bp.route("/api/companies/admin/<slug>", methods=["DELETE"])
def admin_delete_company(slug: str):
    """
    Admin endpoint to delete a company preparation blueprint.
    """
    try:
        deleted = CompanyPrepModel.delete_by_slug(slug)
        if not deleted:
            return jsonify({"success": False, "message": "Company not found or already deleted."}), 404

        AdminModel.log_action("admin@prep.com", "DELETE_COMPANY", f"Deleted company slug: {slug}")
        return jsonify({
            "success": True,
            "message": f"Company '{slug}' deleted successfully."
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting company: {str(e)}"}), 500
