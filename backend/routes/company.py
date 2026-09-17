import json
import random
from flask import Blueprint, request, jsonify
from backend.models import (
    CompanyPrepModel, JobRoleModel, UserPreparationModel,
    EmployeeModel, TestAttemptModel, QuestionModel, AdminModel
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

company_bp = Blueprint("company", __name__)


@company_bp.route("/api/companies", methods=["GET"])
def get_companies():
    """
    Returns list of all enterprise recruitment companies with search & category filters.
    """
    try:
        search = request.args.get("search", "")
        category = request.args.get("category", "")
        difficulty = request.args.get("difficulty", "")

        companies = CompanyPrepModel.get_all(search=search, category=category, difficulty=difficulty)
        return jsonify({
            "success": True,
            "total": len(companies),
            "companies": companies
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching companies: {str(e)}"}), 500


@company_bp.route("/api/companies/<slug>", methods=["GET"])
def get_company_detail(slug: str):
    """
    Returns full company hiring syllabus, rounds, and available job roles.
    """
    try:
        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        roles = JobRoleModel.get_roles_for_company(slug)
        comp["job_roles"] = roles

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

        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        emp = EmployeeModel.get_by_id(employee_id) if employee_id else None
        prep = UserPreparationModel.get_user_company_progress(employee_id, slug) if employee_id else None

        role_lower = job_role.lower()

        # 1. Aptitude Module Data (Company-Specific + Randomized)
        if module_name == "aptitude":
            comp_qs = get_company_aptitude_questions(slug, shuffle=True)
            general_matching = [
                q for q in MASTER_APTITUDE_BANK
                if "all" in [r.lower() for r in q.get("roles", [])] or any(r in role_lower for r in [x.lower() for x in q.get("roles", [])])
            ]
            random.shuffle(general_matching)
            all_qs = comp_qs + [q for q in general_matching if q["id"] not in {x["id"] for x in comp_qs}]
            selected_qs = all_qs[:15]
            random.shuffle(selected_qs)

            return jsonify({
                "success": True,
                "module": "aptitude",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "pattern": comp["aptitude_pattern"],
                "duration_minutes": 15,
                "total_questions": len(selected_qs),
                "questions": selected_qs,
                "current_progress": prep.get("aptitude_progress", 0.0) if prep else 0.0
            }), 200

        # 2. Coding Module Data (Company-Specific + Randomized)
        elif module_name == "coding":
            comp_problems = get_company_coding_problems(slug, shuffle=True)
            gen_matching = [
                p for p in MASTER_CODING_BANK
                if any(slug in c.lower() for c in p.get("companies", [])) or comp["company_name"].lower() in [c.lower() for c in p.get("companies", [])]
            ]
            if not gen_matching:
                gen_matching = list(MASTER_CODING_BANK)
            random.shuffle(gen_matching)
            all_problems = comp_problems + [p for p in gen_matching if p["id"] not in {x["id"] for x in comp_problems}]
            selected_problems = all_problems[:10]
            random.shuffle(selected_problems)

            return jsonify({
                "success": True,
                "module": "coding",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "coding_pattern": comp["coding_pattern"],
                "problems": selected_problems,
                "current_progress": prep.get("coding_progress", 0.0) if prep else 0.0
            }), 200

        # 3. Technical Questions Module Data (Company-Specific + Randomized)
        elif module_name == "technical":
            comp_tech = get_company_technical_questions(slug, shuffle=True)
            db_tech = QuestionModel.get_questions("technical", company_slug=slug, role_name=job_role, limit=30) or []
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
            all_tech = comp_tech + db_tech + bank_tech
            random.shuffle(all_tech)
            selected_tech = all_tech[:15]

            return jsonify({
                "success": True,
                "module": "technical",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "technical_focus": comp["technical_focus"],
                "questions": selected_tech,
                "current_progress": prep.get("technical_progress", 0.0) if prep else 0.0
            }), 200

        # 4. HR Interview Module Data (Company-Specific + Randomized)
        elif module_name == "hr":
            comp_hr = get_company_hr_questions(slug, shuffle=True)
            beh_bank = [q for q in MASTER_INTERVIEW_BANK if "beh" in q.get("category", "").lower() or "hr" in q.get("category", "").lower()]
            random.shuffle(beh_bank)

            hr_questions = list(comp_hr)
            if len(hr_questions) < 4:
                hr_questions.append({
                    "id": 101,
                    "category": "Company Alignment",
                    "question": f"Why do you want to join {comp['company_name']} as a {job_role}?",
                    "tips": f"Review {comp['company_name']}'s core values and culture: {comp['hr_tips']}"
                })
                if beh_bank:
                    hr_questions.append({
                        "id": 102,
                        "category": "STAR Behavioral",
                        "question": beh_bank[0]["question"],
                        "tips": beh_bank[0].get("guidance", "Structure using Situation, Task, Action, and Result (STAR).")
                    })
            random.shuffle(hr_questions)

            return jsonify({
                "success": True,
                "module": "hr",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "hr_tips": comp["hr_tips"],
                "questions": hr_questions,
                "current_progress": prep.get("hr_progress", 0.0) if prep else 0.0
            }), 200

        # 5. AI Mock Interview Module Data
        elif module_name == "interview":
            return jsonify({
                "success": True,
                "module": "interview",
                "company_name": comp["company_name"],
                "target_role": job_role,
                "hiring_rounds": comp["hiring_rounds"],
                "current_progress": prep.get("interview_progress", 0.0) if prep else 0.0
            }), 200

        # 6. Resume Module Data
        elif module_name == "resume":
            rec_skills = [s.strip() for s in (comp["recommended_skills"] or "").split(",") if s.strip()]
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
            rec_skills = [s.strip() for s in (comp["recommended_skills"] or "").split(",") if s.strip()]
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
    Returns full categorized question sets specifically curated for this company:
    - Aptitude MCQs (pattern-specific)
    - Technical Domain questions
    - Coding challenges (PYQs)
    - HR & Behavioral culture questions
    Shuffled dynamically so every call produces fresh, changeable questions.
    """
    try:
        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        return jsonify({
            "success": True,
            "company_name": comp["company_name"],
            "slug": slug,
            "aptitude": get_company_aptitude_questions(slug, shuffle=True),
            "technical": get_company_technical_questions(slug, shuffle=True),
            "coding": get_company_coding_problems(slug, shuffle=True),
            "hr": get_company_hr_questions(slug, shuffle=True)
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@company_bp.route("/api/companies/<slug>/random-question", methods=["GET"])
def get_company_random_question(slug: str):
    """
    Returns a single fresh randomized question for this company in the specified module.
    """
    try:
        comp = CompanyPrepModel.get_by_slug(slug)
        if not comp:
            return jsonify({"success": False, "message": "Company not found."}), 404

        q_type = request.args.get("type", "aptitude").strip().lower()
        exclude_id = request.args.get("exclude_id", "").strip()

        if q_type == "aptitude":
            pool = get_company_aptitude_questions(slug, shuffle=False)
        elif q_type == "coding":
            pool = get_company_coding_problems(slug, shuffle=False)
        elif q_type == "technical":
            pool = get_company_technical_questions(slug, shuffle=False)
        else:
            pool = get_company_hr_questions(slug, shuffle=False)

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
