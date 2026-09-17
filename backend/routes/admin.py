from flask import Blueprint, request, jsonify
from backend.models import (
    AdminModel, EmployeeModel, CompanyPrepModel,
    JobRoleModel, QuestionModel, TrendInsightModel,
    TrendingTemplateModel, AIFluencyModel
)
from backend.database import get_db_connection
from backend.data.aptitude_bank import MASTER_APTITUDE_BANK
from backend.data.coding_bank import MASTER_CODING_BANK
from backend.data.interview_bank import MASTER_INTERVIEW_BANK

admin_bp = Blueprint("admin", __name__)


def check_admin_auth(request_obj) -> bool:
    """
    Validates admin access header or parameter.
    """
    admin_email = request_obj.headers.get("X-Admin-Email") or request_obj.args.get("admin_email")
    if not admin_email:
        return False
    user = EmployeeModel.get_by_email(admin_email)
    return bool(user and user.get("is_admin"))


@admin_bp.route("/api/admin/stats", methods=["GET"])
def get_admin_stats():
    """
    Returns platform-wide metrics for the Admin Dashboard.
    """
    try:
        stats = AdminModel.get_stats()
        stats["total_aptitude_questions"] = len(MASTER_APTITUDE_BANK)
        stats["total_coding_questions"] = len(MASTER_CODING_BANK)
        stats["total_interview_questions"] = len(MASTER_INTERVIEW_BANK)

        return jsonify({
            "success": True,
            "stats": stats
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching admin stats: {str(e)}"}), 500


@admin_bp.route("/api/admin/users", methods=["GET"])
def get_admin_users():
    """
    Returns full list of registered candidates and their metrics.
    """
    try:
        users = EmployeeModel.get_all(limit=200)
        return jsonify({
            "success": True,
            "total": len(users),
            "users": users
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching users: {str(e)}"}), 500


@admin_bp.route("/api/admin/user/<int:user_id>", methods=["DELETE"])
def delete_user(user_id: int):
    """
    Deletes user by ID.
    """
    try:
        deleted = EmployeeModel.delete_user(user_id)
        if deleted:
            AdminModel.log_action("admin@prep.com", "DELETE_USER", f"Deleted user id #{user_id}")
            return jsonify({"success": True, "message": f"User #{user_id} deleted successfully."}), 200
        return jsonify({"success": False, "message": "User not found."}), 404

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting user: {str(e)}"}), 500


# ==========================================
# COMPANY MANAGEMENT ENDPOINTS
# ==========================================

@admin_bp.route("/api/admin/companies", methods=["GET", "POST"])
def admin_companies():
    """
    GET: list all companies.
    POST: add or update company blueprint.
    """
    try:
        if request.method == "GET":
            companies = CompanyPrepModel.get_all()
            return jsonify({"success": True, "total": len(companies), "companies": companies}), 200

        data = request.get_json() or {}
        company_name = data.get("company_name", "").strip()
        slug = data.get("slug", "").strip().lower() or company_name.lower().replace(" ", "-")

        if not company_name:
            return jsonify({"success": False, "message": "company_name is required."}), 400

        data["slug"] = slug
        CompanyPrepModel.save_or_update(data)
        AdminModel.log_action("admin@prep.com", "SAVE_COMPANY", f"Saved company {company_name} ({slug})")

        return jsonify({
            "success": True,
            "message": f"Company '{company_name}' saved successfully.",
            "slug": slug
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error in admin companies: {str(e)}"}), 500


@admin_bp.route("/api/admin/company/<slug>", methods=["DELETE", "GET"])
def admin_company_detail(slug: str):
    """
    GET: retrieve single company for editing.
    DELETE: delete company by slug.
    """
    try:
        if request.method == "GET":
            comp = CompanyPrepModel.get_by_slug(slug)
            if not comp:
                return jsonify({"success": False, "message": "Company not found."}), 404
            return jsonify({"success": True, "company": comp}), 200

        deleted = CompanyPrepModel.delete_by_slug(slug)
        if deleted:
            AdminModel.log_action("admin@prep.com", "DELETE_COMPANY", f"Deleted company slug: {slug}")
            return jsonify({"success": True, "message": f"Company '{slug}' deleted successfully."}), 200
        return jsonify({"success": False, "message": "Company not found."}), 404

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting company: {str(e)}"}), 500


# ==========================================
# JOB ROLES MANAGEMENT ENDPOINTS
# ==========================================

@admin_bp.route("/api/admin/roles", methods=["GET", "POST"])
def admin_roles():
    """
    GET: get roles (optional filter by company_slug).
    POST: add new job role.
    """
    try:
        if request.method == "GET":
            company_slug = request.args.get("company_slug", "all")
            roles = JobRoleModel.get_roles_for_company(company_slug)
            return jsonify({"success": True, "roles": roles}), 200

        data = request.get_json() or {}
        role_name = data.get("role_name", "").strip()
        company_slug = (data.get("company_slug") or "all").strip().lower()
        description = data.get("description", "").strip()
        skills = data.get("skills_required", "").strip()

        if not role_name:
            return jsonify({"success": False, "message": "role_name is required."}), 400

        role_id = JobRoleModel.add_role(role_name, company_slug=company_slug, description=description, skills_required=skills)
        AdminModel.log_action("admin@prep.com", "ADD_ROLE", f"Added role {role_name} to {company_slug}")

        return jsonify({
            "success": True,
            "message": f"Role '{role_name}' created successfully.",
            "role_id": role_id
        }), 201

    except Exception as e:
        return jsonify({"success": False, "message": f"Error managing roles: {str(e)}"}), 500


@admin_bp.route("/api/admin/role/<int:role_id>", methods=["DELETE"])
def admin_delete_role(role_id: int):
    """
    Deletes job role by ID.
    """
    try:
        deleted = JobRoleModel.delete_role(role_id)
        if deleted:
            AdminModel.log_action("admin@prep.com", "DELETE_ROLE", f"Deleted role #{role_id}")
            return jsonify({"success": True, "message": "Job role deleted."}), 200
        return jsonify({"success": False, "message": "Job role not found."}), 404

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting role: {str(e)}"}), 500


# ==========================================
# QUESTION BANK MANAGEMENT ENDPOINTS
# ==========================================

@admin_bp.route("/api/admin/questions", methods=["GET", "POST"])
def admin_questions():
    """
    GET: list all questions with optional filters (question_type, company_slug, role_name).
    POST: add custom question assigned to company and job role.
    """
    try:
        if request.method == "GET":
            q_type = request.args.get("type")
            questions = QuestionModel.get_all_admin(question_type=q_type, limit=300)
            return jsonify({"success": True, "total": len(questions), "questions": questions}), 200

        data = request.get_json() or {}
        question_type = (data.get("question_type") or "technical").strip().lower()
        category = data.get("category", "General").strip()
        question = data.get("question", "").strip()
        company_slug = (data.get("company_slug") or "all").strip().lower()
        role_name = (data.get("role_name") or "all").strip()
        difficulty = data.get("difficulty", "Medium").strip()
        options = data.get("options", [])
        correct_answer = data.get("correct_answer", "").strip()
        explanation = data.get("explanation", "").strip()
        starter_code = data.get("starter_code", "")
        expected_output = data.get("expected_output", "")

        if not question:
            return jsonify({"success": False, "message": "question text is required."}), 400

        q_id = QuestionModel.create_question(
            question_type=question_type,
            category=category,
            question=question,
            company_slug=company_slug,
            role_name=role_name,
            difficulty=difficulty,
            options=options,
            correct_answer=correct_answer,
            explanation=explanation,
            starter_code=starter_code,
            expected_output=expected_output
        )

        AdminModel.log_action("admin@prep.com", "CREATE_QUESTION", f"Created {question_type} question #{q_id} for {company_slug}")

        return jsonify({
            "success": True,
            "message": "Question added successfully.",
            "question_id": q_id
        }), 201

    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving question: {str(e)}"}), 500


@admin_bp.route("/api/admin/question/<int:q_id>", methods=["DELETE"])
def admin_delete_question(q_id: int):
    """
    Deletes question by ID.
    """
    try:
        deleted = QuestionModel.delete_question(q_id)
        if deleted:
            AdminModel.log_action("admin@prep.com", "DELETE_QUESTION", f"Deleted question #{q_id}")
            return jsonify({"success": True, "message": f"Question #{q_id} deleted."}), 200
        return jsonify({"success": False, "message": "Question not found."}), 404

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting question: {str(e)}"}), 500


@admin_bp.route("/api/admin/questions/aptitude", methods=["GET"])
def get_admin_aptitude_questions():
    """
    Returns full question bank for aptitude inspection.
    """
    return jsonify({
        "success": True,
        "total": len(MASTER_APTITUDE_BANK),
        "questions": MASTER_APTITUDE_BANK
    }), 200


@admin_bp.route("/api/admin/questions/coding", methods=["GET"])
def get_admin_coding_questions():
    """
    Returns full coding question bank.
    """
    return jsonify({
        "success": True,
        "total": len(MASTER_CODING_BANK),
        "problems": MASTER_CODING_BANK
    }), 200


@admin_bp.route("/api/admin/questions/interview", methods=["GET"])
def get_admin_interview_questions():
    """
    Returns full interview question bank.
    """
    return jsonify({
        "success": True,
        "total": len(MASTER_INTERVIEW_BANK),
        "questions": MASTER_INTERVIEW_BANK
    }), 200


# =========================================================================
# 2026 CMS: TREND INSIGHTS
# =========================================================================

@admin_bp.route("/api/trends/active", methods=["GET"])
def get_active_trends():
    """
    Public endpoint for Main Dashboard Trend Insight Widget.
    """
    role = request.args.get("role", "")
    company = request.args.get("company", "")
    trends = TrendInsightModel.get_active(role=role, company=company)
    return jsonify({"success": True, "trends": trends}), 200


@admin_bp.route("/api/admin/trends", methods=["GET", "POST"])
def handle_admin_trends():
    if request.method == "GET":
        trends = TrendInsightModel.get_all()
        return jsonify({"success": True, "trends": trends}), 200
    else:
        data = request.get_json() or {}
        new_id = TrendInsightModel.create(
            title=data.get("title", ""),
            category=data.get("category", "AI Fluency"),
            role_tag=data.get("role_tag", "All"),
            company_tag=data.get("company_tag", "All"),
            content=data.get("content", ""),
            actionable_tip=data.get("actionable_tip", ""),
            priority=data.get("priority", 1)
        )
        return jsonify({"success": True, "id": new_id, "message": "Trend insight created!"}), 201


@admin_bp.route("/api/admin/trends/<int:item_id>", methods=["PUT", "DELETE"])
def handle_single_admin_trend(item_id):
    if request.method == "DELETE":
        deleted = TrendInsightModel.delete(item_id)
        return jsonify({"success": deleted}), (200 if deleted else 404)
    else:
        data = request.get_json() or {}
        updated = TrendInsightModel.update(
            item_id=item_id,
            title=data.get("title", ""),
            category=data.get("category", "AI Fluency"),
            role_tag=data.get("role_tag", "All"),
            company_tag=data.get("company_tag", "All"),
            content=data.get("content", ""),
            actionable_tip=data.get("actionable_tip", ""),
            priority=data.get("priority", 1),
            is_active=data.get("is_active", 1)
        )
        return jsonify({"success": updated}), (200 if updated else 404)


# =========================================================================
# 2026 CMS: TRENDING RESUME TEMPLATES
# =========================================================================

@admin_bp.route("/api/admin/templates", methods=["GET", "POST"])
def handle_admin_templates():
    if request.method == "GET":
        templates = TrendingTemplateModel.get_all()
        return jsonify({"success": True, "templates": templates}), 200
    else:
        data = request.get_json() or {}
        new_id = TrendingTemplateModel.create(
            template_id=data.get("template_id", "custom-template"),
            name=data.get("name", "Custom Template"),
            badge_text=data.get("badge_text", "🔥 Trending 2026"),
            description=data.get("description", ""),
            css_class=data.get("css_class", "template-modern-single"),
            is_trending=data.get("is_trending", 1)
        )
        return jsonify({"success": True, "id": new_id, "message": "Template created!"}), 201


@admin_bp.route("/api/admin/templates/<int:item_id>", methods=["PUT", "DELETE"])
def handle_single_admin_template(item_id):
    if request.method == "DELETE":
        deleted = TrendingTemplateModel.delete(item_id)
        return jsonify({"success": deleted}), (200 if deleted else 404)
    else:
        data = request.get_json() or {}
        updated = TrendingTemplateModel.update(
            item_id=item_id,
            name=data.get("name", ""),
            badge_text=data.get("badge_text", ""),
            description=data.get("description", ""),
            css_class=data.get("css_class", ""),
            is_trending=data.get("is_trending", 1),
            is_active=data.get("is_active", 1)
        )
        return jsonify({"success": updated}), (200 if updated else 404)


# =========================================================================
# 2026 CMS: AI FLUENCY QUESTIONS
# =========================================================================

@admin_bp.route("/api/admin/ai-fluency-questions", methods=["GET", "POST"])
def handle_admin_fluency_questions():
    if request.method == "GET":
        questions = AIFluencyModel.get_questions()
        return jsonify({"success": True, "questions": questions}), 200
    else:
        data = request.get_json() or {}
        import json
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ai_fluency_questions (question_text, category, difficulty, context_hint, ideal_talking_points_json, is_active)
            VALUES (?, ?, ?, ?, ?, 1)
        """, (
            data.get("question_text", ""),
            data.get("category", "Workflow Velocity"),
            data.get("difficulty", "Medium"),
            data.get("context_hint", ""),
            json.dumps(data.get("ideal_talking_points", []))
        ))
        new_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return jsonify({"success": True, "id": new_id, "message": "Question added!"}), 201


@admin_bp.route("/api/admin/ai-fluency-questions/<int:item_id>", methods=["PUT", "DELETE"])
def handle_single_admin_fluency_question(item_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == "DELETE":
        cursor.execute("DELETE FROM ai_fluency_questions WHERE id = ?", (item_id,))
        affected = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return jsonify({"success": affected}), (200 if affected else 404)
    else:
        data = request.get_json() or {}
        import json
        cursor.execute("""
            UPDATE ai_fluency_questions
            SET question_text = ?, category = ?, difficulty = ?, context_hint = ?, ideal_talking_points_json = ?, is_active = ?
            WHERE id = ?
        """, (
            data.get("question_text", ""),
            data.get("category", "Workflow Velocity"),
            data.get("difficulty", "Medium"),
            data.get("context_hint", ""),
            json.dumps(data.get("ideal_talking_points", [])),
            data.get("is_active", 1),
            item_id
        ))
        affected = cursor.rowcount > 0
        conn.commit()
        conn.close()
        return jsonify({"success": affected}), (200 if affected else 404)

