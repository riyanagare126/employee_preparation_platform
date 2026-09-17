from flask import Blueprint, request, jsonify
from backend.models import ResumeModel, ResumeVersionModel, TrendingTemplateModel

resume_bp = Blueprint("resume", __name__)


@resume_bp.route("/api/resume", methods=["POST", "GET"])
def handle_resume():
    if request.method == "POST":
        try:
            data = request.get_json() or {}
            employee_id = data.get("employee_id")

            if not employee_id:
                return jsonify({
                    "success": False,
                    "message": "employee_id is required to save resume."
                }), 400

            saved = ResumeModel.save_or_update(int(employee_id), data)

            return jsonify({
                "success": True,
                "message": "Resume data saved successfully!",
                "data": saved
            }), 200

        except Exception as e:
            return jsonify({
                "success": False,
                "message": f"Error saving resume: {str(e)}"
            }), 500

    else:  # GET
        try:
            employee_id = request.args.get("employee_id", type=int)
            if not employee_id:
                return jsonify({
                    "success": False,
                    "message": "employee_id query parameter is required."
                }), 400

            resume = ResumeModel.get_by_employee(employee_id)
            return jsonify({
                "success": True,
                "data": resume
            }), 200

        except Exception as e:
            return jsonify({
                "success": False,
                "message": f"Error fetching resume: {str(e)}"
            }), 500


@resume_bp.route("/api/resume/templates", methods=["GET"])
def get_resume_templates():
    """
    Returns active trending resume templates from DB.
    """
    try:
        templates = TrendingTemplateModel.get_active()
        return jsonify({"success": True, "templates": templates}), 200
    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching templates: {str(e)}"}), 500


@resume_bp.route("/api/resume/versions/save", methods=["POST"])
def save_resume_version():
    """
    Saves a named version of the resume for the candidate.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        version_name = data.get("version_name", "Default Resume")
        template_name = data.get("template_name", "modern-single")
        target_role = data.get("target_role", "Software Engineer")
        target_company = data.get("target_company", "Enterprise")
        resume_data = data.get("resume_data", {})
        score = int(data.get("score", 85))

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        saved = ResumeVersionModel.save_version(
            employee_id=int(employee_id),
            version_name=version_name,
            template_name=template_name,
            target_role=target_role,
            target_company=target_company,
            resume_data=resume_data,
            score=score
        )

        return jsonify({
            "success": True,
            "message": f"Resume version '{version_name}' saved successfully!",
            "data": saved
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error saving version: {str(e)}"}), 500


@resume_bp.route("/api/resume/versions", methods=["GET"])
def get_resume_versions():
    """
    Returns all saved versions for the candidate.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id query parameter is required."}), 400

        versions = ResumeVersionModel.get_versions(employee_id)
        return jsonify({"success": True, "versions": versions}), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching versions: {str(e)}"}), 500


@resume_bp.route("/api/resume/versions/<int:version_id>", methods=["GET", "DELETE"])
def handle_single_version(version_id):
    """
    Loads or deletes a specific saved version.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            data = request.get_json() or {}
            employee_id = data.get("employee_id")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        if request.method == "GET":
            version = ResumeVersionModel.get_version(version_id, int(employee_id))
            if not version:
                return jsonify({"success": False, "message": "Version not found"}), 404
            return jsonify({"success": True, "data": version}), 200

        else:  # DELETE
            deleted = ResumeVersionModel.delete_version(version_id, int(employee_id))
            return jsonify({"success": deleted}), (200 if deleted else 404)

    except Exception as e:
        return jsonify({"success": False, "message": f"Error handling version: {str(e)}"}), 500


@resume_bp.route("/api/resume/rewrite-bullet", methods=["POST"])
def rewrite_bullet():
    """
    AI bullet point rewriter that transforms raw bullet statements into high-impact metric-driven STAR statements.
    """
    try:
        data = request.get_json() or {}
        bullet_text = data.get("bullet_text", "")
        target_role = data.get("target_role", "Software Engineer")

        result = ResumeVersionModel.rewrite_bullet(bullet_text, target_role)
        return jsonify(result), (200 if result.get("success") else 400)

    except Exception as e:
        return jsonify({"success": False, "message": f"Error enhancing bullet: {str(e)}"}), 500


@resume_bp.route("/api/resume/score-ats", methods=["POST"])
def score_ats():
    """
    AI Resume score assessing ATS friendliness and JD keyword matching.
    """
    try:
        data = request.get_json() or {}
        resume_data = data.get("resume_data", {})
        target_role = data.get("target_role", "Software Engineer")
        job_description = data.get("job_description", "")

        result = ResumeVersionModel.score_ats(resume_data, target_role, job_description)
        return jsonify(result), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error calculating ATS score: {str(e)}"}), 500
