from flask import Blueprint, request, jsonify
from backend.models import DashboardSummaryModel

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/api/dashboard/summary", methods=["GET"])
def get_dashboard_summary():
    """
    Returns complete live aggregated dashboard data per employee_id:
    - Stat cards: interviews taken, avg score, resume ATS score, AI fluency score
    - Improvement trend progress chart data over sessions
    - Smart Roadmap progress and active enterprise
    - Curated 2026 Trend Insight tips
    - Gamification points and daily streak
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        summary = DashboardSummaryModel.get_summary(employee_id)
        return jsonify({"success": True, "data": summary}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading dashboard summary: {str(e)}"}), 500
