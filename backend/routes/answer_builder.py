from flask import Blueprint, request, jsonify
from backend.models import StructuredAnswerModel

answer_builder_bp = Blueprint("answer_builder", __name__)

PRESET_QUESTIONS = [
    {
        "key": "tell-me-about-yourself",
        "title": "Tell me about yourself / Walk me through your resume",
        "hint": "Start with your current role and active technical focus (Present), transition to high-impact projects or internship outcomes (Past), and conclude with why this enterprise is your natural next step (Future)."
    },
    {
        "key": "why-should-we-hire-you",
        "title": "Why should we hire you for this role?",
        "hint": "Highlight your current engineering core strengths (Present), demonstrate proven problem-solving and reliability from previous builds (Past), and commit to solving immediate business/technical challenges (Future)."
    },
    {
        "key": "why-this-company",
        "title": "Why do you want to join our company specifically?",
        "hint": "Address how your current career aspirations align (Present), reference how your past technical work prepared you for enterprise scale (Past), and state the exact impact you aim to deliver in 90 days (Future)."
    },
    {
        "key": "first-90-days",
        "title": "Where do you see yourself contributing most in your first 90 days?",
        "hint": "Express current velocity and willingness to absorb the codebase (Present), cite a past example of ramping up fast (Past), and outline how you will ship dependable features autonomously (Future)."
    }
]


@answer_builder_bp.route("/api/answer-builder/questions", methods=["GET"])
def get_preset_questions():
    """
    Returns list of recruiter-approved questions.
    """
    return jsonify({"success": True, "questions": PRESET_QUESTIONS}), 200


@answer_builder_bp.route("/api/answer-builder/analyze", methods=["POST"])
def analyze_structured_answer():
    """
    Analyzes Present-Past-Future boxes for speaking rate (~60s), section balance, and cohesive flow.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id", 1)
        question_title = data.get("question_title", "Tell me about yourself")
        present_text = data.get("present_text", "")
        past_text = data.get("past_text", "")
        future_text = data.get("future_text", "")
        target_role = data.get("target_role", "Software Engineer")
        target_company = data.get("target_company", "Target Enterprise")

        analysis = StructuredAnswerModel.analyze(
            employee_id=int(employee_id),
            question_title=question_title,
            present_text=present_text,
            past_text=past_text,
            future_text=future_text,
            target_role=target_role,
            target_company=target_company
        )
        return jsonify(analysis), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error analyzing pitch: {str(e)}"}), 500


@answer_builder_bp.route("/api/answer-builder/save", methods=["POST"])
def save_structured_answer():
    """
    Saves candidate's customized pitch to their library.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        result = StructuredAnswerModel.save(int(employee_id), data)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving pitch: {str(e)}"}), 500


@answer_builder_bp.route("/api/answer-builder/saved", methods=["GET"])
def get_saved_structured_answers():
    """
    Returns candidate's library of saved 60-second pitches.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        answers = StructuredAnswerModel.get_saved(employee_id)
        return jsonify({"success": True, "data": answers}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading saved pitches: {str(e)}"}), 500


@answer_builder_bp.route("/api/answer-builder/saved/<int:answer_id>", methods=["DELETE"])
def delete_structured_answer(answer_id):
    """
    Deletes saved pitch from candidate library.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            data = request.get_json() or {}
            employee_id = data.get("employee_id")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        deleted = StructuredAnswerModel.delete(answer_id, int(employee_id))
        return jsonify({"success": deleted}), (200 if deleted else 404)

    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting pitch: {str(e)}"}), 500
