from flask import Blueprint, request, jsonify
from backend.models import GamificationModel

gamification_bp = Blueprint("gamification", __name__)


@gamification_bp.route("/api/gamification/stats", methods=["GET"])
@gamification_bp.route("/api/gamification/status", methods=["GET"])
def get_gamification_stats():
    """
    Returns candidate's XP points, level, streak, and unlocked badges list.
    Supports both /api/gamification/stats and /api/gamification/status.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        stats = GamificationModel.get_or_create(employee_id)
        
        # Enrich unlocked badges with catalog metadata
        unlocked_keys = stats.get("badges_json", [])
        badges_list = []
        for b_id, meta in GamificationModel.BADGES_CATALOG.items():
            badges_list.append({
                "id": b_id,
                "name": meta["name"],
                "emoji": meta["emoji"],
                "desc": meta["desc"],
                "unlocked": (b_id in unlocked_keys)
            })

        points = stats.get("points", 50)
        streak = stats.get("streak_days", 1)
        level = stats.get("level", 1)

        payload = {
            "points": points,
            "level": level,
            "streak_days": streak,
            "current_streak": streak,
            "last_activity_date": stats.get("last_activity_date")
        }

        return jsonify({
            "success": True,
            "stats": payload,
            "data": payload,
            "badges": badges_list
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error retrieving gamification stats: {str(e)}"}), 500


@gamification_bp.route("/api/gamification/award-points", methods=["POST"])
def award_points():
    """
    Awards points for completing activities.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        activity = data.get("activity", "general")
        points = data.get("points", 10)

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        updated = GamificationModel.award_points(int(employee_id), activity, int(points))
        return jsonify({
            "success": True,
            "message": f"Awarded {points} XP!",
            "data": updated
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error awarding points: {str(e)}"}), 500
