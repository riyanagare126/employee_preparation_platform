# -*- coding: utf-8 -*-
"""
Preparation Module Routes (Flask Blueprint).

Provides endpoints for company-specific, level-wise, non-repeating interview preparation:
- GET /api/preparation/<company>/questions
- POST /api/preparation/<company>/reset
- POST /api/employee/experience

Viva Core Logic:
1. Candidate Isolation: Questions are fetched based on employee_id, company, and experience level.
2. Repetition Prevention: Excludes all questions present in `user_question_history`.
3. Auto-AI Refill: When questions for a level are exhausted, calls Gemini AI to generate new ones.
4. Graceful Fallback: If AI is unavailable, resets user history for that company/level so the candidate
   never sees a blank screen.
5. Cache Invalidation: Emits Cache-Control: no-store to force browser to fetch fresh questions on reloads.
"""

import logging
from flask import Blueprint, request, jsonify, make_response
from backend.models import EmployeeModel, QuestionModel, UserQuestionHistoryModel
from backend.services.ai_service import generate_company_questions

logger = logging.getLogger("preparation_route")
preparation_bp = Blueprint("preparation", __name__)


def _extract_employee_id():
    """Extracts employee_id from query params, headers, or request body."""
    # 1. Query parameter
    emp_id = request.args.get("employee_id")
    if emp_id:
        try:
            return int(emp_id)
        except ValueError:
            pass

    # 2. Custom header
    header_id = request.headers.get("X-Employee-Id") or request.headers.get("employee-id")
    if header_id:
        try:
            return int(header_id)
        except ValueError:
            pass

    # 3. JSON body (for POST requests)
    if request.is_json:
        body = request.get_json(silent=True) or {}
        body_id = body.get("employee_id")
        if body_id:
            try:
                return int(body_id)
            except ValueError:
                pass

    return 0  # 0 indicates guest / preview user


@preparation_bp.route("/api/preparation/<company>/questions", methods=["GET"])
def get_company_questions(company: str):
    """
    Fetch non-repeating company-specific questions tailored to candidate's experience level.
    Query Parameters:
      - count: Number of questions to return (default: 10, max: 25)
      - category: Filter by category (e.g., 'Technical', 'Behavioral', 'System Design', 'all')
      - role: Candidate role (e.g., 'Software Engineer')
      - experience_level: Explicit level override from dropdown (e.g. 'senior (5-8 years)')
      - question_type: Filter by type (e.g., 'technical_basics', 'behavioral_star', etc.)
      - employee_id: Candidate ID
    """
    try:
        employee_id = _extract_employee_id()
        count = min(int(request.args.get("count", 10)), 25)
        category = request.args.get("category", "all").strip()
        role = request.args.get("role", "").strip()
        question_type = request.args.get("question_type", "").strip()
        req_level = request.args.get("experience_level", "").strip()

        # Normalize company name (e.g., "tcs" -> "TCS", "deloitte" -> "Deloitte")
        normalized_company = QuestionModel.normalize_company(company)

        # Determine Experience Level:
        # Priority 1: User explicitly selected from dropdown in UI
        # Priority 2: User profile experience mapped to canonical level
        # Priority 3: Default to 'fresher (0-1 year)'
        if req_level:
            level = QuestionModel.normalize_level(req_level)
        elif employee_id > 0:
            emp = EmployeeModel.get_by_id(employee_id)
            if emp and emp.get("experience"):
                level = EmployeeModel.map_experience_to_level(emp.get("experience"))
            else:
                level = "fresher (0-1 year)"
        else:
            level = "fresher (0-1 year)"

        logger.info(
            f"Fetching questions: company={normalized_company}, level={level}, "
            f"emp_id={employee_id}, count={count}, category={category}"
        )

        # Fetch unseen questions from database
        unseen_questions = QuestionModel.get_unseen_questions(
            employee_id=employee_id,
            company=normalized_company,
            experience_level=level,
            category=category,
            role=role,
            question_type=question_type,
            limit=count
        )

        pool_recycled = False

        # If unseen questions are fewer than requested, generate new ones with AI
        if len(unseen_questions) < count:
            needed = count - len(unseen_questions)
            logger.info(f"Unseen questions ({len(unseen_questions)}) < requested ({count}). Refilling {needed} via AI...")

            existing_texts = QuestionModel.get_all_existing_texts(normalized_company, level)
            ai_questions = generate_company_questions(
                company=normalized_company,
                experience_level=level,
                role=role or "Software Engineer",
                question_type=question_type,
                count=max(needed, 5),
                existing_questions=existing_texts
            )

            # Insert newly generated questions into DB
            if ai_questions:
                for q_data in ai_questions:
                    QuestionModel.insert(
                        company=normalized_company,
                        experience_level=level,
                        role=q_data.get("role") or role or "Software Engineer",
                        question_type=q_data.get("question_type") or question_type or "technical_depth",
                        category=q_data.get("category") or "Technical",
                        question_text=q_data.get("question_text", ""),
                        sample_answer=q_data.get("sample_answer", ""),
                        difficulty=q_data.get("difficulty", "medium"),
                        source="ai_generated"
                    )

                # Re-fetch unseen questions with the new AI additions
                unseen_questions = QuestionModel.get_unseen_questions(
                    employee_id=employee_id,
                    company=normalized_company,
                    experience_level=level,
                    category=category,
                    role=role,
                    question_type=question_type,
                    limit=count
                )

            # If AI generation failed or returned nothing AND we have zero unseen questions:
            # Gracefully recycle/reset history for this employee for this company/level
            # so the candidate is NEVER presented with a blank page!
            if len(unseen_questions) == 0 and employee_id > 0:
                logger.warning(f"All questions exhausted and AI unavailable for {normalized_company} [{level}]. Recycling history.")
                UserQuestionHistoryModel.reset_history(employee_id, normalized_company)
                pool_recycled = True
                unseen_questions = QuestionModel.get_unseen_questions(
                    employee_id=employee_id,
                    company=normalized_company,
                    experience_level=level,
                    category=category,
                    role=role,
                    question_type=question_type,
                    limit=count
                )

        # Mark all served questions as seen for this employee
        if employee_id > 0 and unseen_questions:
            UserQuestionHistoryModel.mark_as_seen(employee_id, [q["id"] for q in unseen_questions])


        # Fetch progress stats
        stats = QuestionModel.get_company_stats(employee_id, normalized_company, level)

        payload = {
            "success": True,
            "company": normalized_company,
            "experience_level": level,
            "count": len(unseen_questions),
            "questions": unseen_questions,
            "stats": stats,
            "pool_recycled": pool_recycled
        }

        # Create response with strict anti-caching headers (Cache-Control: no-store)
        response = make_response(jsonify(payload))
        response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        response.headers["Pragma"] = "no-cache"
        response.headers["Expires"] = "0"
        return response

    except Exception as e:
        logger.error(f"Error in get_company_questions: {e}", exc_info=True)
        return jsonify({"success": False, "message": str(e)}), 500


@preparation_bp.route("/api/preparation/<company>/reset", methods=["POST"])
def reset_preparation_history(company: str):
    """
    Resets the candidate's question history for the given company,
    allowing them to practice all questions again from scratch.
    """
    try:
        employee_id = _extract_employee_id()
        if employee_id <= 0:
            return jsonify({"success": False, "message": "Valid employee_id is required to reset progress."}), 400

        normalized_company = QuestionModel.normalize_company(company)
        UserQuestionHistoryModel.reset_history(employee_id, normalized_company)

        # Return updated stats after reset
        stats = QuestionModel.get_company_stats(employee_id, normalized_company)

        return jsonify({
            "success": True,
            "message": f"Successfully reset your practice history for {normalized_company}. You can now practice all questions again!",
            "company": normalized_company,
            "stats": stats
        })

    except Exception as e:
        logger.error(f"Error in reset_preparation_history: {e}", exc_info=True)
        return jsonify({"success": False, "message": str(e)}), 500


@preparation_bp.route("/api/employee/experience", methods=["POST"])
def update_employee_experience():
    """
    Updates the candidate's experience level in their profile.
    Accepts JSON: { "employee_id": 1, "experience": "3-5 years" }
    """
    try:
        data = request.get_json(silent=True) or {}
        employee_id = data.get("employee_id") or _extract_employee_id()
        experience = (data.get("experience") or "").strip()

        if not employee_id or not experience:
            return jsonify({"success": False, "message": "employee_id and experience are required."}), 400

        updated = EmployeeModel.update_experience(int(employee_id), experience)
        if not updated:
            return jsonify({"success": False, "message": "Failed to update employee experience. Employee not found."}), 404

        mapped_level = EmployeeModel.map_experience_to_level(experience)

        return jsonify({
            "success": True,
            "message": "Experience level updated successfully.",
            "experience": experience,
            "mapped_level": mapped_level
        })

    except Exception as e:
        logger.error(f"Error in update_employee_experience: {e}", exc_info=True)
        return jsonify({"success": False, "message": str(e)}), 500
