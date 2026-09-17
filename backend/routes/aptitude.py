import random
import uuid
import time
from typing import List, Dict, Any, Tuple
from flask import Blueprint, request, jsonify

from backend.data.aptitude_bank import MASTER_APTITUDE_BANK
from backend.data.company_questions_bank import get_company_aptitude_questions
from backend.models import (
    AptitudeModel, AptitudeSessionModel, EmployeeModel,
    SecureTestSessionModel
)

aptitude_bp = Blueprint("aptitude", __name__)

# Fast lookup map of all questions by ID
QUESTION_LOOKUP: Dict[int, Dict[str, Any]] = {q["id"]: q for q in MASTER_APTITUDE_BANK}


def generate_personalized_test(
    employee_id: int,
    job_role: str = "Software Engineer",
    qualification: str = "",
    skills: str = "",
    count: int = 15,
    company: str = "",
    difficulty: str = ""
) -> Tuple[List[Dict[str, Any]], List[Dict[str, Any]], List[int]]:
    """
    Generates a randomized, personalized aptitude test for the given employee:
    - Supports difficulty levels: 'Easy' (Low), 'Medium', 'Hard' (High), or balanced mix
    - Prioritizes company-specific questions if company is specified
    - 4 Quantitative Aptitude questions
    - 4 Logical Reasoning questions
    - 3 Verbal Ability questions
    - 2 Data Interpretation questions
    - 2 Basic Technical Aptitude questions
    - Shuffles options for every question, preserving secure backend key
    """
    recent_ids = set(AptitudeSessionModel.get_recent_question_ids(employee_id, limit=50))
    role_lower = (job_role or "").lower()
    skills_lower = (skills or "").lower()

    # Split question bank by category
    quant_pool = [q for q in MASTER_APTITUDE_BANK if q["category"] == "Quantitative Aptitude"]
    logical_pool = [q for q in MASTER_APTITUDE_BANK if q["category"] == "Logical Reasoning"]
    verbal_pool = [q for q in MASTER_APTITUDE_BANK if q["category"] == "Verbal Ability"]
    di_pool = [q for q in MASTER_APTITUDE_BANK if q["category"] == "Data Interpretation"]
    tech_pool = [q for q in MASTER_APTITUDE_BANK if q["category"] == "Basic Technical Aptitude"]

    # Filter technical questions by relevance to job role & skills
    role_tech_pool = []
    for q in tech_pool:
        roles = [r.lower() for r in q.get("roles", [])]
        if "all" in roles:
            role_tech_pool.append(q)
        elif any(r in role_lower or r in skills_lower for r in roles):
            role_tech_pool.append(q)

    if len(role_tech_pool) < 2:
        role_tech_pool = tech_pool

    def select_from_pool(pool: List[Dict[str, Any]], required_count: int) -> List[Dict[str, Any]]:
        target_pool = pool
        if difficulty:
            diff_match = [q for q in pool if q.get("difficulty", "Medium").lower() == difficulty.lower()]
            if len(diff_match) >= required_count:
                target_pool = diff_match
            elif diff_match:
                target_pool = diff_match + [q for q in pool if q not in diff_match]

        unseen = [q for q in target_pool if q["id"] not in recent_ids]
        if len(unseen) >= required_count:
            return random.sample(unseen, required_count)
        
        needed = required_count - len(unseen)
        seen = [q for q in target_pool if q["id"] in recent_ids]
        fallback = random.sample(seen, min(needed, len(seen))) if seen else []
        return unseen + fallback

    comp_qs = []
    if company:
        comp_raw = get_company_aptitude_questions(company, shuffle=True)
        # Convert string ID to numeric or keep as is
        for c_idx, cq in enumerate(comp_raw):
            cq_copy = dict(cq)
            if isinstance(cq_copy.get("id"), str):
                cq_copy["id"] = 90000 + (hash(cq_copy["id"]) % 10000)
            comp_qs.append(cq_copy)

    selected_quant = select_from_pool(quant_pool, 4)
    selected_logical = select_from_pool(logical_pool, 4)
    selected_verbal = select_from_pool(verbal_pool, 3)
    selected_di = select_from_pool(di_pool, 2)
    selected_tech = select_from_pool(role_tech_pool, 2)

    general_pool = selected_quant + selected_logical + selected_verbal + selected_di + selected_tech
    if comp_qs:
        combined = comp_qs[:min(len(comp_qs), 6)] + [q for q in general_pool if q["id"] not in {x["id"] for x in comp_qs}]
        combined = combined[:count]
    else:
        combined = general_pool[:count]

    random.shuffle(combined)

    client_questions = []
    options_map = []

    for idx, q in enumerate(combined):
        orig_options = q["options"]
        orig_correct = q["correctIndex"]

        perm = list(range(len(orig_options)))
        random.shuffle(perm)

        shuffled_options = [orig_options[i] for i in perm]
        shuffled_correct_index = perm.index(orig_correct)

        options_map.append({
            "question_id": q["id"],
            "correct_index": shuffled_correct_index,
            "orig_correct_index": orig_correct,
            "shuffled_options": shuffled_options
        })

        client_questions.append({
            "id": q["id"],
            "index": idx,
            "category": q["category"],
            "difficulty": q.get("difficulty", "Medium"),
            "question": q["question"],
            "options": shuffled_options
        })

    return client_questions, options_map, [q["id"] for q in combined]


@aptitude_bp.route("/api/aptitude/session/active", methods=["GET"])
def get_active_session():
    """
    Checks for an in-flight active test session. Restores exact questions,
    draft answers, and calculates server-authoritative remaining time on page refresh.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        tab_token = request.args.get("tab_token", "")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        # Check if already completed (enforced only if strict_lock is requested)
        if request.args.get("strict_lock", "").lower() == "true" and SecureTestSessionModel.check_already_completed(employee_id, "aptitude"):
            completed_result = SecureTestSessionModel.get_completed_result(employee_id, "aptitude")
            return jsonify({
                "success": True,
                "has_active": False,
                "already_completed": True,
                "completed_result": completed_result,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 200

        session = SecureTestSessionModel.get_active_session(employee_id, "aptitude", tab_token)
        if not session or session.get("status") != "active":
            return jsonify({"success": True, "has_active": False}), 200

        # Check multi-tab collision
        if tab_token and session.get("tab_token") and session.get("tab_token") != tab_token:
            return jsonify({
                "success": False,
                "has_active": True,
                "tab_collision": True,
                "message": "This test is already active in another browser tab/session."
            }), 409

        return jsonify({
            "success": True,
            "has_active": True,
            "session_id": session["session_id"],
            "total": len(session.get("questions", [])),
            "duration_seconds": session["duration_seconds"],
            "remaining_seconds": session.get("remaining_seconds", session["duration_seconds"]),
            "job_role": session.get("job_role", ""),
            "tab_token": session.get("tab_token", ""),
            "questions": session.get("questions", []),
            "draft_answers": session.get("answers", {})
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error checking active session: {str(e)}"}), 500


@aptitude_bp.route("/api/aptitude/start", methods=["POST"])
def start_aptitude_test():
    """
    Initializes a new dynamic aptitude test session with strict 1-attempt policy:
    - Rejects if candidate has already completed an attempt
    - Returns existing active session if one is currently in progress
    - Freezes server-generated question set and starts authoritative server timer
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        tab_token = data.get("tab_token") or f"tab_{uuid.uuid4().hex[:8]}"
        job_role = data.get("job_role", "Software Engineer")
        qualification = data.get("qualification", "")
        skills = data.get("skills", "")

        if not employee_id:
            return jsonify({
                "success": False,
                "message": "employee_id is required to start an assessment session."
            }), 400

        emp_id = int(employee_id)

        is_refresh = (
            request.args.get("refresh", "").lower() == "true"
            or request.args.get("force_new", "").lower() == "true"
            or (isinstance(data, dict) and (data.get("refresh") or data.get("force_new") or data.get("retake")))
        )

        # Allow continuous practice and dynamic retakes; check lock only if strict_lock is requested
        if not is_refresh and request.args.get("strict_lock", "").lower() == "true":
            if SecureTestSessionModel.check_already_completed(emp_id, "aptitude"):
                completed_result = SecureTestSessionModel.get_completed_result(emp_id, "aptitude")
                return jsonify({
                    "success": False,
                    "already_completed": True,
                    "completed_result": completed_result,
                    "message": "You have already completed this test. A second attempt is not allowed."
                }), 403

        # Restore active session only if not requesting fresh/new questions
        if not is_refresh:
            existing_session = SecureTestSessionModel.get_active_session(emp_id, "aptitude", tab_token)
            if existing_session and existing_session.get("status") == "active":
                return jsonify({
                    "success": True,
                    "restored": True,
                    "session_id": existing_session["session_id"],
                    "total": len(existing_session.get("questions", [])),
                    "duration_seconds": existing_session["duration_seconds"],
                    "remaining_seconds": existing_session.get("remaining_seconds", existing_session["duration_seconds"]),
                    "job_role": existing_session.get("job_role", job_role),
                    "tab_token": existing_session.get("tab_token", tab_token),
                    "questions": existing_session.get("questions", []),
                    "draft_answers": existing_session.get("answers", {})
                }), 200

        # 3. Create fresh secure session
        emp_profile = EmployeeModel.get_by_id(emp_id)
        if emp_profile:
            job_role = job_role or emp_profile.get("job_role", "Software Engineer")
            qualification = qualification or emp_profile.get("qualification", "")
            skills = skills or emp_profile.get("skills", "")

        company = request.args.get("company", "") or (data.get("company") if isinstance(data, dict) else "") or ""
        
        # Difficulty filter: Easy (Low), Medium, Hard (High), or balanced
        raw_diff = (request.args.get("difficulty", "") or (data.get("difficulty") if isinstance(data, dict) else "") or "").strip().lower()
        if raw_diff in ["easy", "low"]:
            difficulty = "Easy"
        elif raw_diff in ["hard", "high"]:
            difficulty = "Hard"
        elif raw_diff in ["medium", "mid"]:
            difficulty = "Medium"
        else:
            difficulty = ""

        total_questions = 15
        duration_seconds = 900  # 15 minutes

        client_questions, options_map, question_ids = generate_personalized_test(
            employee_id=emp_id,
            job_role=job_role,
            qualification=qualification,
            skills=skills,
            count=total_questions,
            company=company,
            difficulty=difficulty
        )

        session_id = f"apt_{uuid.uuid4().hex[:12]}"

        # Save in secure_test_sessions
        SecureTestSessionModel.create_session(
            session_id=session_id,
            employee_id=emp_id,
            test_type="aptitude",
            questions=client_questions,
            options_map=options_map,
            duration_seconds=duration_seconds,
            tab_token=tab_token,
            job_role=job_role
        )

        # Also store in legacy AptitudeSessionModel for backwards compatibility
        AptitudeSessionModel.create_session(
            session_id=session_id,
            employee_id=emp_id,
            job_role=job_role,
            question_ids=question_ids,
            options_map=options_map,
            total_questions=len(client_questions),
            duration_seconds=duration_seconds
        )
        AptitudeSessionModel.record_recent_questions(emp_id, question_ids)

        return jsonify({
            "success": True,
            "session_id": session_id,
            "total": len(client_questions),
            "duration_seconds": duration_seconds,
            "remaining_seconds": duration_seconds,
            "tab_token": tab_token,
            "job_role": job_role,
            "questions": client_questions
        }), 201

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error starting aptitude test session: {str(e)}"
        }), 500


@aptitude_bp.route("/api/aptitude/session/save-draft", methods=["POST"])
def save_draft():
    """
    Autosaves user draft answers during active test without finalizing the session.
    """
    try:
        data = request.get_json() or {}
        session_id = data.get("session_id")
        employee_id = data.get("employee_id")
        answers = data.get("answers", {})

        if not session_id or not employee_id:
            return jsonify({"success": False, "message": "Missing session_id or employee_id"}), 400

        saved = SecureTestSessionModel.save_draft_answers(session_id, int(employee_id), answers)
        return jsonify({"success": saved}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@aptitude_bp.route("/api/aptitude/session/change-question", methods=["POST"])
def change_aptitude_question():
    """
    Swaps out a specific question in an active session with an alternative unseen question,
    shuffles its options, updates the secure session in DB, and returns the new question.
    """
    try:
        data = request.get_json() or {}
        session_id = data.get("session_id")
        employee_id = data.get("employee_id")
        question_index = data.get("question_index")
        category = data.get("category", "")
        current_id = data.get("current_id")

        if not session_id or employee_id is None or question_index is None:
            return jsonify({"success": False, "message": "Missing required parameters."}), 400

        session = SecureTestSessionModel.get_active_session(int(employee_id), "aptitude")
        if not session or session.get("session_id") != session_id:
            return jsonify({"success": False, "message": "Active session not found."}), 404

        questions = session.get("questions", [])
        options_map = session.get("options_map", [])

        if question_index < 0 or question_index >= len(questions):
            return jsonify({"success": False, "message": "Invalid question index."}), 400

        existing_ids = {q["id"] for q in questions}
        company = data.get("company", "").strip().lower()

        category_pool = []
        if company:
            comp_candidates = get_company_aptitude_questions(company, shuffle=True)
            for cq in comp_candidates:
                cq_copy = dict(cq)
                if isinstance(cq_copy.get("id"), str):
                    cq_copy["id"] = 90000 + (hash(cq_copy["id"]) % 10000)
                if cq_copy["id"] not in existing_ids and cq_copy["id"] != current_id:
                    category_pool.append(cq_copy)

        if not category_pool:
            category_pool = [q for q in MASTER_APTITUDE_BANK if q.get("category") == category and q["id"] not in existing_ids]
        if not category_pool:
            category_pool = [q for q in MASTER_APTITUDE_BANK if q["id"] not in existing_ids]
        if not category_pool:
            category_pool = [q for q in MASTER_APTITUDE_BANK if q["id"] != current_id]

        new_q = random.choice(category_pool)

        # Shuffle options
        orig_options = new_q["options"]
        orig_correct = new_q["correctIndex"]
        perm = list(range(len(orig_options)))
        random.shuffle(perm)
        shuffled_options = [orig_options[i] for i in perm]
        shuffled_correct = perm.index(orig_correct)

        new_client_q = {
            "id": new_q["id"],
            "index": question_index,
            "category": new_q["category"],
            "difficulty": new_q.get("difficulty", "Medium"),
            "question": new_q["question"],
            "options": shuffled_options
        }

        new_opt_map = {
            "question_id": new_q["id"],
            "correct_index": shuffled_correct,
            "orig_correct_index": orig_correct,
            "shuffled_options": shuffled_options
        }

        questions[question_index] = new_client_q
        if question_index < len(options_map):
            options_map[question_index] = new_opt_map
        else:
            options_map.append(new_opt_map)

        SecureTestSessionModel.update_session_questions(session_id, int(employee_id), questions, options_map)

        return jsonify({
            "success": True,
            "question": new_client_q
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@aptitude_bp.route("/api/aptitude/session/terminate", methods=["POST"])
def terminate_session():
    """
    Marks the active session as abandoned/terminated if user navigates away.
    """
    try:
        data = request.get_json() or {}
        session_id = data.get("session_id")
        employee_id = data.get("employee_id")
        reason = data.get("reason", "abandoned")

        if session_id and employee_id:
            SecureTestSessionModel.terminate_session(session_id, int(employee_id), reason)

        return jsonify({
            "success": True,
            "message": "This test session has ended. You cannot restart this attempt."
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@aptitude_bp.route("/api/aptitude/submit", methods=["POST"])
def submit_aptitude_test():
    """
    Server-side authoritative test grading:
    - Verifies session is valid and active
    - Computes final score and percentage strictly on backend
    - Stores result, sets status to completed, and prevents multiple final submissions
    """
    try:
        data = request.get_json() or {}
        session_id = data.get("session_id")
        employee_id = data.get("employee_id")
        user_answers = data.get("user_answers", [])

        if not session_id or employee_id is None:
            return jsonify({
                "success": False,
                "message": "Missing session_id or employee_id."
            }), 400

        emp_id = int(employee_id)

        # Check if already completed
        if SecureTestSessionModel.check_already_completed(emp_id, "aptitude"):
            completed_result = SecureTestSessionModel.get_completed_result(emp_id, "aptitude")
            return jsonify({
                "success": False,
                "already_completed": True,
                "completed_result": completed_result,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 403

        # Retrieve session
        session = SecureTestSessionModel.get_active_session(emp_id, "aptitude")
        if not session or session["session_id"] != session_id:
            # Fallback check on legacy session model
            session = AptitudeSessionModel.get_session(session_id)
            if not session:
                return jsonify({
                    "success": False,
                    "message": "This test session has ended. You cannot restart this attempt."
                }), 404

        options_map = session.get("options_map", [])
        total = len(options_map)
        score = 0
        review = []
        category_stats = {}

        for idx, item in enumerate(options_map):
            q_id = item["question_id"]
            correct_idx = item["correct_index"]
            shuffled_options = item.get("shuffled_options", [])
            q_obj = QUESTION_LOOKUP.get(q_id, {})

            user_choice = user_answers[idx] if idx < len(user_answers) else None
            is_correct = (user_choice is not None and user_choice == correct_idx)

            if is_correct:
                score += 1

            cat = q_obj.get("category", "General")
            if cat not in category_stats:
                category_stats[cat] = {"total": 0, "correct": 0}
            category_stats[cat]["total"] += 1
            if is_correct:
                category_stats[cat]["correct"] += 1

            review.append({
                "question_id": q_id,
                "question": q_obj.get("question", ""),
                "category": cat,
                "difficulty": q_obj.get("difficulty", "Medium"),
                "options": shuffled_options or q_obj.get("options", []),
                "user_answer_index": user_choice,
                "correct_answer_index": correct_idx,
                "is_correct": is_correct,
                "explanation": q_obj.get("explanation", "Standard problem solving formula applied.")
            })

        percentage = round((score / total) * 100, 2) if total > 0 else 0.0

        if percentage >= 80:
            performance_message = "Excellent"
        elif percentage >= 50:
            performance_message = "Good"
        else:
            performance_message = "Needs Improvement"

        result_payload = {
            "score": score,
            "total": total,
            "percentage": percentage,
            "performance_message": performance_message,
            "category_breakdown": category_stats,
            "review": review
        }

        # Mark secure session completed
        SecureTestSessionModel.submit_session(
            session_id=session_id,
            employee_id=emp_id,
            test_type="aptitude",
            score=score,
            percentage=percentage,
            performance_message=performance_message,
            answers=user_answers,
            result_payload=result_payload
        )

        # Complete legacy session record
        AptitudeSessionModel.complete_session(
            session_id=session_id,
            score=score,
            percentage=percentage,
            performance_message=performance_message,
            answers_json=user_answers,
            review_json=review
        )

        # Upsert latest result for instant Dashboard metrics
        AptitudeModel.save_result(
            employee_id=emp_id,
            score=score,
            total=total,
            percentage=percentage,
            performance_message=performance_message,
            category_breakdown=category_stats
        )

        return jsonify({
            "success": True,
            "session_id": session_id,
            "score": score,
            "total": total,
            "percentage": percentage,
            "performance_message": performance_message,
            "category_breakdown": category_stats,
            "review": review
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error submitting test: {str(e)}"
        }), 500


@aptitude_bp.route("/api/aptitude/result", methods=["GET"])
def get_aptitude_result():
    """
    Returns the completed result for an employee.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        result = AptitudeModel.get_latest_result(employee_id)
        if not result:
            return jsonify({"success": True, "latest": None, "message": "No test completed yet."}), 200

        return jsonify({"success": True, "latest": result}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@aptitude_bp.route("/api/aptitude/result", methods=["POST"])
def save_aptitude_result_compat():
    """
    Backward-compatible save result endpoint.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        score = data.get("score")
        total = data.get("total", 10)
        percentage = data.get("percentage")
        performance_message = data.get("performance_message", "Completed")
        category_breakdown = data.get("category_breakdown", {})

        if employee_id is None or score is None:
            return jsonify({"success": False, "message": "Missing employee_id or score."}), 400

        if percentage is None and total > 0:
            percentage = round((score / total) * 100, 2)

        AptitudeModel.save_result(
            employee_id=int(employee_id),
            score=score,
            total=total,
            percentage=percentage,
            performance_message=performance_message,
            category_breakdown=category_breakdown
        )

        return jsonify({"success": True, "message": "Result saved successfully."}), 201

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
