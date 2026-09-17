from flask import Blueprint, request, jsonify
from backend.models import SkillAssessmentModel, DailyPlanModel, ReadinessModel, EmployeeModel, ResumeExtractorModel

skills_bp = Blueprint("skills", __name__)


@skills_bp.route("/api/skills/assessment", methods=["GET"])
def get_skill_assessment():
    """
    Evaluates candidate's performance across modules and synthesizes a 3-tier Skill Matrix,
    transparent weighted Employee Readiness Score, and actionable gap analysis.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        assessment = SkillAssessmentModel.get_assessment(employee_id)
        return jsonify({
            "success": True,
            "data": assessment
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error evaluating skills: {str(e)}"}), 500


@skills_bp.route("/api/skills/daily-plan", methods=["GET"])
def get_daily_plan():
    """
    Returns today's personalized 5-step preparation agenda based on candidate's weak skills and target role.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        plan = DailyPlanModel.get_or_create_daily_plan(employee_id)
        return jsonify({
            "success": True,
            "data": plan
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching daily plan: {str(e)}"}), 500


@skills_bp.route("/api/skills/daily-plan/toggle", methods=["POST"])
def toggle_daily_task():
    """
    Toggles completion status for a daily preparation task.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        task_id = data.get("task_id")

        if not employee_id or task_id is None:
            return jsonify({"success": False, "message": "employee_id and task_id are required."}), 400

        res = DailyPlanModel.toggle_task(int(employee_id), int(task_id))
        return jsonify(res), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error toggling daily task: {str(e)}"}), 500


@skills_bp.route("/api/skills/readiness-trend", methods=["GET"])
def get_readiness_trend():
    """
    Returns the historical progression trend of the candidate's Employee Readiness Score.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        trend = ReadinessModel.get_progression_trend(employee_id)
        return jsonify({
            "success": True,
            "trend": trend
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching trend: {str(e)}"}), 500
