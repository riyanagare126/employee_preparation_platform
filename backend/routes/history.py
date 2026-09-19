from flask import Blueprint, request, jsonify
from backend.models import (
    AptitudeModel, CodingModel, InterviewModel,
    TestAttemptModel, UserPreparationModel, ResumeAnalyzerModel
)

history_bp = Blueprint("history", __name__)


@history_bp.route("/api/history/timeline", methods=["GET"])
def get_preparation_timeline():
    """
    Combines test attempts, coding solutions, mock interviews, and resume analyses
    into a comprehensive chronological activity log with company-wise progress.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        timeline = []

        # 1. Official Test Attempts (from test_attempts table)
        attempts = TestAttemptModel.get_attempts_for_user(employee_id, limit=50)
        for a in attempts:
            comp_name = (a.get("company_slug") or "General").upper()
            role_name = a.get("role_name") or "Software Engineer"
            t_type = a.get("test_type", "test").lower()

            type_labels = {
                "aptitude": ("fa-solid fa-calculator", "Aptitude Assessment"),
                "coding": ("fa-solid fa-laptop-code", "Coding Assessment"),
                "technical": ("fa-solid fa-gears", "Technical Assessment"),
                "interview": ("fa-solid fa-microphone", "AI Mock Interview"),
                "hr": ("fa-solid fa-handshake", "HR Interview")
            }
            icon, label = type_labels.get(t_type, ("fa-solid fa-pen-to-square", f"{t_type.capitalize()} Test"))

            timeline.append({
                "type": t_type,
                "icon": icon,
                "company": comp_name,
                "role": role_name,
                "title": f"{comp_name} • {label} ({role_name})",
                "score": f"{a.get('percentage', 0)}% ({a.get('score', 0)}/{a.get('total', 100)})",
                "rating": "Passed" if float(a.get("percentage", 0)) >= 60 else "Review Needed",
                "date": a.get("created_at")
            })

        # 2. Coding Progress Solutions
        coding_items = CodingModel.get_all_by_employee(employee_id)
        for c in coding_items:
            timeline.append({
                "type": "coding",
                "icon": "fa-solid fa-laptop-code",
                "company": "PRACTICE",
                "role": c.get("language", "Code"),
                "title": f"Solved: {c.get('problem_title')} ({c.get('language')})",
                "score": f"Status: {c.get('status', 'Solved')}",
                "rating": c.get("difficulty", "Easy"),
                "date": c.get("completed_at")
            })

        # 3. Interviews (from interview_results)
        interviews = InterviewModel.get_all_by_employee(employee_id)
        for i in interviews:
            timeline.append({
                "type": "interview",
                "icon": "fa-solid fa-microphone",
                "company": "SIMULATION",
                "role": i.get("job_role", "Software Engineer"),
                "title": f"AI Mock Interview ({i.get('job_role')})",
                "score": f"Overall: {i.get('overall_score', 0)}/100 (Tech: {i.get('technical_score', 0)}/100)",
                "rating": "Evaluated",
                "date": i.get("created_at")
            })

        # 4. Resume Analyses
        resume_rep = ResumeAnalyzerModel.get_latest_by_employee(employee_id)
        if resume_rep:
            timeline.append({
                "type": "resume",
                "icon": "fa-solid fa-file-lines",
                "company": "RESUME",
                "role": resume_rep.get("target_role", "Software Engineer"),
                "title": f"Resume ATS Audit ({resume_rep.get('target_role', 'General')})",
                "score": f"ATS Score: {resume_rep.get('ats_score', 0)}/100",
                "rating": "Optimized" if int(resume_rep.get("ats_score", 0)) >= 75 else "Needs Work",
                "date": resume_rep.get("created_at")
            })

        # Deduplicate and sort combined timeline descending by date
        timeline.sort(key=lambda x: str(x.get("date") or ""), reverse=True)

        # 5. Company-Wise Preparation Records
        company_progress = UserPreparationModel.get_all_for_user(employee_id)

        return jsonify({
            "success": True,
            "total_activities": len(timeline),
            "timeline": timeline,
            "company_progress": company_progress
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": f"Error fetching history timeline: {str(e)}"}), 500
