from flask import Blueprint, request, jsonify
from backend.models import LearningRoadmapModel, EmployeeModel

roadmap_bp = Blueprint("roadmap", __name__)


@roadmap_bp.route("/api/roadmap", methods=["GET"])
def get_roadmap():
    """
    Returns personalized career learning roadmap for the candidate's job role.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        role = request.args.get("role", type=str)

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        if not role:
            emp = EmployeeModel.get_by_id(employee_id)
            role = emp.get("job_role", "Java Developer") if emp else "Java Developer"

        roadmap_data = LearningRoadmapModel.get_or_generate(employee_id, role)
        return jsonify({
            "success": True,
            "data": roadmap_data
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching roadmap: {str(e)}"}), 500


@roadmap_bp.route("/api/roadmap/update-step", methods=["POST"])
def update_step():
    """
    Updates status of a learning milestone (completed, in_progress, upcoming).
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        step_num = data.get("step_num")
        new_status = data.get("status", "completed")

        if not employee_id or step_num is None:
            return jsonify({"success": False, "message": "Missing employee_id or step_num."}), 400

        LearningRoadmapModel.update_step_status(int(employee_id), int(step_num), new_status)
        return jsonify({
            "success": True,
            "message": "Roadmap milestone updated successfully!"
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error updating roadmap step: {str(e)}"}), 500
