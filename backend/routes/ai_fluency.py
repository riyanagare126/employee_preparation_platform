from flask import Blueprint, request, jsonify
from backend.models import AIFluencyModel

ai_fluency_bp = Blueprint("ai_fluency", __name__)


@ai_fluency_bp.route("/api/ai-fluency/questions", methods=["GET"])
def get_ai_fluency_questions():
    """
    Returns list of 2026 indirect AI fluency questions.
    """
    try:
        category = request.args.get("category", default="")
        questions = AIFluencyModel.get_questions(category)
        return jsonify({"success": True, "questions": questions}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching questions: {str(e)}"}), 500


@ai_fluency_bp.route("/api/ai-fluency/evaluate", methods=["POST"])
def evaluate_ai_fluency():
    """
    Evaluates candidate's typed response across 4 core dimensions:
    - Tool Integration
    - Critical Verification & Security
    - Velocity & Impact
    - Authenticity & Communication
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        question_id = data.get("question_id")
        candidate_answer = data.get("candidate_answer", "")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        result = AIFluencyModel.evaluate_answer(int(employee_id), question_id, candidate_answer)
        return jsonify(result), (200 if result.get("success") else 400)

    except Exception as e:
        return jsonify({"success": False, "message": f"Error evaluating response: {str(e)}"}), 500


@ai_fluency_bp.route("/api/ai-fluency/history", methods=["GET"])
def get_ai_fluency_history():
    """
    Returns past attempts and score progression trend for candidate.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        history = AIFluencyModel.get_history(employee_id)
        return jsonify({"success": True, "data": history}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading fluency history: {str(e)}"}), 500
