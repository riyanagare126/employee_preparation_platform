from flask import Blueprint, request, jsonify
from backend.models import NoticePlanModel
from backend.services.ai_service import generate_notice_period_plan, generate_simple_notice_plan

notice_plan_bp = Blueprint("notice_plan", __name__)


@notice_plan_bp.route("/api/notice-plan/latest", methods=["GET"])
def get_latest_notice_plan():
    """
    Retrieves the latest Notice Period Preparation Plan for the logged-in employee,
    including calculated days_left based on notice_days and created_at.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        plan = NoticePlanModel.get_latest_simple_plan(employee_id)
        return jsonify({
            "success": True,
            "data": plan
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading latest notice plan: {str(e)}"}), 500


@notice_plan_bp.route("/api/notice-plan/active", methods=["GET"])
def get_active_notice_plan():
    """
    Retrieves the active Notice Period Countdown Plan for the logged-in employee.
    Includes remaining days, upcoming interview alerts, today's tasks, and progress.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        plan = NoticePlanModel.get_active_plan(employee_id)
        return jsonify({
            "success": True,
            "data": plan
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading notice plan: {str(e)}"}), 500


@notice_plan_bp.route("/api/notice-plan/generate", methods=["POST"])
def generate_notice_plan():
    """
    Generates and persists a new Notice Period Plan using AI (with expert fallback).
    Saves the structured record in table 'notice_plan' and returns the plan.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        target_role = (data.get("target_role") or "Software Engineer").strip()
        experience = str(data.get("experience") or data.get("experience_years") or "1-3").strip()
        notice_days = int(data.get("notice_days") or data.get("notice_period_days") or 30)
        weak_areas = data.get("weak_areas") or []

        if not target_role:
            return jsonify({"success": False, "message": "Target role is required."}), 400
        if notice_days <= 0:
            return jsonify({"success": False, "message": "Notice period must be at least 1 day."}), 400

        # Generate simple plan text via AI service (with expert fallback)
        plan_text = generate_simple_notice_plan(target_role, experience, notice_days, weak_areas)

        # Save to 'notice_plan' table
        saved_simple = NoticePlanModel.save_simple_plan(
            int(employee_id), target_role, experience, notice_days, weak_areas, plan_text
        )

        # Also populate legacy notice_plans & tasks if requested or for full timeline support
        saved_legacy = {}
        try:
            generated_legacy = generate_notice_period_plan(data)
            saved_legacy = NoticePlanModel.save_plan(int(employee_id), data, generated_legacy) or {}
        except Exception as ex:
            print(f"[Notice Plan Route] Legacy plan sync warning: {ex}")

        # Combine both datasets so both simple and legacy consumers receive required fields
        response_data = {**saved_legacy, **saved_simple}
        if "total_tasks" in saved_legacy and "total_tasks" not in response_data:
            response_data["total_tasks"] = saved_legacy["total_tasks"]

        return jsonify({
            "success": True,
            "message": "Notice period preparation plan generated successfully!",
            "data": response_data
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error generating notice plan: {str(e)}"}), 500


@notice_plan_bp.route("/api/notice-plan/task/toggle", methods=["POST"])
def toggle_notice_task():
    """
    Toggles completion status for a notice plan task, updates overall progress,
    and awards gamification XP.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        task_id = data.get("task_id")
        is_completed = data.get("is_completed")

        if not employee_id or task_id is None:
            return jsonify({"success": False, "message": "employee_id and task_id are required."}), 400

        result = NoticePlanModel.toggle_task(int(employee_id), int(task_id), is_completed)
        return jsonify(result), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error updating task status: {str(e)}"}), 500


@notice_plan_bp.route("/api/notice-plan/full", methods=["GET"])
def get_full_notice_plan():
    """
    Retrieves the complete day-by-day breakdown with all tasks, dates,
    and interview alerts for the full plan modal.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        plan = NoticePlanModel.get_active_plan(employee_id)
        if not plan:
            return jsonify({"success": False, "message": "No active notice plan found."}), 404

        return jsonify({
            "success": True,
            "data": plan
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching full plan: {str(e)}"}), 500
