from flask import Blueprint, request, jsonify
from backend.models import ResumeAnalyzerModel, EmployeeModel

analyzer_bp = Blueprint("analyzer", __name__)


@analyzer_bp.route("/api/resume/analyze", methods=["POST"])
def analyze_resume():
    """
    Parses candidate resume text and generates an ATS compatibility report with score, strengths, and keywords.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        resume_text = data.get("resume_text", "")
        target_role = data.get("target_role", "Software Engineer")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        if not resume_text.strip():
            return jsonify({"success": False, "message": "Please provide your resume content to analyze."}), 400

        emp = EmployeeModel.get_by_id(int(employee_id))
        if emp and not target_role:
            target_role = emp.get("job_role", "Software Engineer")

        report = ResumeAnalyzerModel.analyze_resume(
            employee_id=int(employee_id),
            resume_text=resume_text,
            target_role=target_role
        )

        # Automatically extract structured skills & sync to employee profile
        from backend.models import ResumeExtractorModel
        extracted_skills = ResumeExtractorModel.extract_skills_from_text(resume_text, int(employee_id))
        report["extracted_skills"] = extracted_skills

        return jsonify({
            "success": True,
            "message": "Resume analyzed successfully!",
            "report": report
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error analyzing resume: {str(e)}"}), 500


@analyzer_bp.route("/api/resume/extract-skills", methods=["POST"])
def extract_skills():
    """
    Extracts structured technical and soft skills (Detected vs Not identified) from resume text.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        resume_text = data.get("resume_text", "")

        from backend.models import ResumeExtractorModel
        extracted = ResumeExtractorModel.extract_skills_from_text(resume_text, int(employee_id) if employee_id else None)

        return jsonify({
            "success": True,
            "data": extracted
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error extracting skills: {str(e)}"}), 500


@analyzer_bp.route("/api/resume/analysis-history", methods=["GET"])
def get_analysis_history():
    """
    Returns latest resume analysis record.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        latest = ResumeAnalyzerModel.get_latest_by_employee(employee_id)
        return jsonify({
            "success": True,
            "data": latest
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error retrieving analysis history: {str(e)}"}), 500
