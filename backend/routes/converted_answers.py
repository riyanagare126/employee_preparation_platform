from flask import Blueprint, request, jsonify, session
from backend.models import ConvertedAnswerModel, GamificationModel
from backend.services.ai_service import convert_honest_to_professional

converted_answers_bp = Blueprint("converted_answers", __name__)


@converted_answers_bp.route("/api/converted-answers", methods=["GET"])
def get_converted_answers():
    """
    Retrieves all saved honest-to-professional answers for the logged-in employee.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        records = ConvertedAnswerModel.get_all(employee_id)
        return jsonify({
            "success": True,
            "count": len(records),
            "data": records
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading converted answers: {str(e)}"}), 500


@converted_answers_bp.route("/api/converted-answers/<int:answer_id>", methods=["GET"])
def get_converted_answer(answer_id: int):
    """
    Retrieves a single converted answer record.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        item = ConvertedAnswerModel.get_by_id(answer_id, employee_id)
        if not item:
            return jsonify({"success": False, "message": "Record not found."}), 404

        return jsonify({
            "success": True,
            "data": item
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error loading answer: {str(e)}"}), 500


@converted_answers_bp.route("/api/converted-answers/convert", methods=["POST"])
def convert_answer():
    """
    Transforms raw honest reason into a professional answer, 30s version,
    red-flag analysis, and 2 likely follow-up questions.
    """
    try:
        data = request.get_json() or {}
        raw_answer = (data.get("raw_answer") or "").strip()
        question_type = (data.get("question_type") or "Why are you leaving your current job?").strip()

        if not raw_answer:
            return jsonify({"success": False, "message": "Please share your raw, honest answer to convert."}), 400

        # Execute AI conversion with deterministic fallback
        converted = convert_honest_to_professional(data)

        payload = {
            "question_type": question_type,
            "raw_answer": raw_answer,
            "professional_answer": converted.get("professional_answer", ""),
            "short_answer": converted.get("short_answer", ""),
            "red_flags": converted.get("red_flags", []),
            "follow_up_questions": converted.get("follow_up_questions", [])
        }

        # Automatically save in DB if employee_id is available
        employee_id = data.get("employee_id")
        if not employee_id:
            user = session.get("user") or session.get("employee")
            if isinstance(user, dict) and user.get("id"):
                employee_id = int(user["id"])

        saved_record = None
        if employee_id:
            try:
                save_data = {
                    "question_type": question_type,
                    "raw_answer": raw_answer,
                    "professional_answer": payload["professional_answer"],
                    "short_answer": payload["short_answer"],
                    "red_flags": payload["red_flags"],
                    "follow_up_questions": payload["follow_up_questions"],
                    "target_role": data.get("target_role", ""),
                    "target_company": data.get("target_company", "")
                }
                res = ConvertedAnswerModel.save(int(employee_id), save_data)
                if res.get("success"):
                    saved_record = res.get("converted_answer")
                    payload["id"] = res.get("id")
                    try:
                        GamificationModel.add_points(int(employee_id), 20, "Reframed Honest Interview Answer")
                    except Exception:
                        pass
            except Exception as e_save:
                print(f"Auto-save converted answer notice: {e_save}")

        return jsonify({
            "success": True,
            "data": payload,
            "saved": saved_record,
            **payload
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error converting answer: {str(e)}"}), 500


@converted_answers_bp.route("/api/converted-answers/save", methods=["POST"])
def save_converted_answer():
    """
    Persists a converted answer record to the database and awards gamification XP.
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

        raw_answer = (data.get("raw_answer") or "").strip()
        if not raw_answer:
            return jsonify({"success": False, "message": "Raw answer is required."}), 400

        # If professional_answer is missing, convert it first
        if not data.get("professional_answer"):
            converted = convert_honest_to_professional(data)
            data["professional_answer"] = converted.get("professional_answer", "")
            data["short_answer"] = converted.get("short_answer", "")
            data["red_flags"] = converted.get("red_flags", [])
            data["follow_up_questions"] = converted.get("follow_up_questions", [])

        res = ConvertedAnswerModel.save(int(employee_id), data)
        if not res.get("success"):
            return jsonify(res), 400

        # Award Gamification XP
        try:
            GamificationModel.add_points(int(employee_id), 20, "Reframed Honest Interview Answer")
        except Exception:
            pass

        return jsonify({
            "success": True,
            "message": "Answer successfully saved to your library!",
            "data": res.get("converted_answer")
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving answer: {str(e)}"}), 500


@converted_answers_bp.route("/api/converted-answers/<int:answer_id>", methods=["DELETE"])
def delete_converted_answer(answer_id: int):
    """
    Deletes a converted answer from the employee's library.
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

        success = ConvertedAnswerModel.delete(answer_id, int(employee_id))
        if not success:
            return jsonify({"success": False, "message": "Answer not found or already removed."}), 404

        return jsonify({
            "success": True,
            "message": "Saved answer deleted successfully."
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error deleting answer: {str(e)}"}), 500
