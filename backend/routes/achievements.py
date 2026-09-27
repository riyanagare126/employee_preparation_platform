from flask import Blueprint, request, jsonify, session
from backend.models import AchievementModel, GamificationModel
from backend.services.ai_service import convert_achievement_to_star

achievements_bp = Blueprint("achievements", __name__)


@achievements_bp.route("/api/achievements", methods=["GET"])
def get_achievements():
    """
    Returns all saved career achievements for the logged-in employee,
    including STAR breakdowns and mapped behavioral questions.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        achievements = AchievementModel.get_all(employee_id)
        return jsonify({
            "success": True,
            "count": len(achievements),
            "data": achievements
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading achievements: {str(e)}"}), 500


@achievements_bp.route("/api/achievements/<int:achievement_id>", methods=["GET"])
def get_achievement(achievement_id: int):
    """
    Returns a single achievement by ID for the authorized employee.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        item = AchievementModel.get_by_id(achievement_id, employee_id)
        if not item:
            return jsonify({"success": False, "message": "Achievement not found."}), 404

        return jsonify({
            "success": True,
            "data": item
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error retrieving achievement: {str(e)}"}), 500


@achievements_bp.route("/api/achievements/save", methods=["POST"])
def save_achievement():
    """
    Saves or updates a career achievement.
    If STAR fields are absent, automatically transforms the raw achievement
    into a structured STAR narrative with mapped behavioral questions.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        title = (data.get("title") or "").strip()
        raw_desc = (data.get("raw_description") or "").strip()
        metrics = (data.get("metrics_result") or "").strip()
        skills = (data.get("skills_used") or "").strip()

        if not title:
            return jsonify({"success": False, "message": "Achievement title is required."}), 400
        if not raw_desc:
            return jsonify({"success": False, "message": "Description of what you did is required."}), 400

        # If STAR fields are missing or empty, generate them via AI service with expert fallback
        star_situation = (data.get("star_situation") or "").strip()
        star_task = (data.get("star_task") or "").strip()
        star_action = (data.get("star_action") or "").strip()
        star_result = (data.get("star_result") or "").strip()
        mapped_questions = data.get("mapped_questions")

        if not (star_situation and star_task and star_action and star_result):
            transformed = convert_achievement_to_star(data)
            data["star_situation"] = transformed.get("star_situation", "")
            data["star_task"] = transformed.get("star_task", "")
            data["star_action"] = transformed.get("star_action", "")
            data["star_result"] = transformed.get("star_result", "")
            if not mapped_questions:
                data["mapped_questions"] = transformed.get("mapped_questions", [])

        # Persist to database
        res = AchievementModel.save(int(employee_id), data)
        if not res.get("success"):
            return jsonify(res), 400

        # Award Gamification XP for building their vault
        try:
            GamificationModel.add_points(int(employee_id), 20, "Added STAR Achievement to Vault")
        except Exception:
            pass

        return jsonify({
            "success": True,
            "message": "Achievement successfully saved and transformed into STAR format!",
            "data": res.get("achievement")
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving achievement: {str(e)}"}), 500


@achievements_bp.route("/api/achievements/<int:achievement_id>", methods=["DELETE"])
def delete_achievement(achievement_id: int):
    """
    Deletes an achievement from the employee's vault.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            data = request.get_json(silent=True) or {}
            employee_id = data.get("employee_id")
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        success = AchievementModel.delete(achievement_id, int(employee_id))
        if not success:
            return jsonify({"success": False, "message": "Achievement not found or already deleted."}), 404

        return jsonify({
            "success": True,
            "message": "Achievement deleted successfully from vault."
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting achievement: {str(e)}"}), 500
