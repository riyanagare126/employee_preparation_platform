from flask import Blueprint, request, jsonify
from backend.models import SmartRoadmapModel, EmployeeModel

smart_roadmap_bp = Blueprint("smart_roadmap", __name__)


@smart_roadmap_bp.route("/api/roadmap/smart", methods=["GET"])
def get_smart_roadmap():
    """
    Returns active company-specific smart prep roadmap for candidate.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        company = request.args.get("company", type=str, default="")
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        roadmap = SmartRoadmapModel.get_current(employee_id, company)
        if not roadmap:
            # Auto-generate baseline roadmap if none exists
            emp = EmployeeModel.get_by_id(employee_id) or {}
            comp_name = emp.get("target_company") or "Tata Consultancy Services (TCS)"
            comp_slug = "tcs" if "tcs" in comp_name.lower() else "google"
            role = emp.get("target_role") or "Software Engineer"
            roadmap = SmartRoadmapModel.generate(employee_id, comp_name, comp_slug, role, 14)

        return jsonify({"success": True, "data": roadmap}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading roadmap: {str(e)}"}), 500


@smart_roadmap_bp.route("/api/roadmap/smart/generate", methods=["POST"])
def generate_smart_roadmap():
    """
    Generates tailored day-wise prep roadmap for specific enterprise and duration.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        company_name = data.get("company_name", "Tata Consultancy Services (TCS)")
        company_slug = data.get("company_slug", "tcs")
        target_role = data.get("target_role", "Software Engineer")
        duration_days = int(data.get("duration_days", 14))

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        roadmap = SmartRoadmapModel.generate(
            employee_id=int(employee_id),
            company_name=company_name,
            company_slug=company_slug,
            target_role=target_role,
            duration_days=duration_days
        )

        return jsonify({
            "success": True,
            "message": f"Smart Roadmap successfully generated for {company_name} ({duration_days} Days)!",
            "data": roadmap
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error generating roadmap: {str(e)}"}), 500


@smart_roadmap_bp.route("/api/roadmap/smart/task/toggle", methods=["POST"])
def toggle_roadmap_task():
    """
    Toggles completion state of a daily roadmap task.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        task_id = data.get("task_id")

        if not employee_id or not task_id:
            return jsonify({"success": False, "message": "Missing employee_id or task_id."}), 400

        result = SmartRoadmapModel.toggle_task(int(employee_id), int(task_id))
        return jsonify(result), (200 if result.get("success") else 400)

    except Exception as e:
        return jsonify({"success": False, "message": f"Error updating task: {str(e)}"}), 500


@smart_roadmap_bp.route("/api/roadmap/smart/adjust", methods=["POST"])
def adjust_roadmap():
    """
    Auto-adjusts roadmap based on employee test and mock scores.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        roadmap_id = data.get("roadmap_id")

        if not employee_id or not roadmap_id:
            return jsonify({"success": False, "message": "Missing employee_id or roadmap_id."}), 400

        result = SmartRoadmapModel.auto_adjust(int(employee_id), int(roadmap_id))
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error auto-adjusting roadmap: {str(e)}"}), 500
