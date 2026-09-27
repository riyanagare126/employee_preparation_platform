"""
FastAPI application for AI Employee Preparation Platform.
Fully compatible with SQLAlchemy models in backend.models_sa,
while seamlessly mounting and delegating to existing endpoints.
Can be executed with: py -m uvicorn backend.fastapi_app:app --reload
"""
import os
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, JSONResponse
from starlette.middleware.wsgi import WSGIMiddleware

from backend.database import init_db
from backend.models import (
    DashboardSummaryModel, SmartRoadmapModel, ResumeVersionModel,
    TrendingTemplateModel, AIFluencyModel, StructuredAnswerModel,
    TrendInsightModel, NoticePlanModel, AchievementModel, GamificationModel,
    ConvertedAnswerModel, QuestionModel, UserQuestionHistoryModel, EmployeeModel,
    TestSecurityModel
)
from backend.services.ai_service import (
    generate_notice_period_plan, generate_simple_notice_plan, convert_achievement_to_star,
    convert_honest_to_professional, generate_company_questions
)
from backend.app import create_app


# Initialize DB
init_db()

app = FastAPI(
    title="AI Employee Preparation Platform API (FastAPI + SQLAlchemy)",
    version="2026.1",
    description="Interactive employee readiness platform with company-specific roadmaps, ATS resume builder, 2026 AI fluency rounds, and recruiter 60-second pitch framework."
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FRONTEND_DIR = os.path.join(BASE_DIR, "frontend")


# =========================================================================
# 1. MAIN DASHBOARD API
# =========================================================================
@app.get("/api/dashboard/summary")
def get_dashboard_summary(employee_id: int):
    summary = DashboardSummaryModel.get_summary(employee_id)
    return {"success": True, "data": summary}


@app.get("/api/trends/active")
def get_active_trends(role: str = "", company: str = ""):
    trends = TrendInsightModel.get_active(role=role, company=company)
    return {"success": True, "trends": trends}


# =========================================================================
# 2. SMART PREP ROADMAP API
# =========================================================================
@app.get("/api/roadmap/smart")
def get_smart_roadmap(employee_id: int, company: str = ""):
    roadmap = SmartRoadmapModel.get_current(employee_id, company)
    return {"success": True, "data": roadmap}


@app.post("/api/roadmap/smart/generate")
async def generate_smart_roadmap(request: Request):
    data = await request.json()
    roadmap = SmartRoadmapModel.generate(
        employee_id=int(data.get("employee_id")),
        company_name=data.get("company_name", "Target Enterprise"),
        company_slug=data.get("company_slug", "tcs"),
        target_role=data.get("target_role", "Software Engineer"),
        duration_days=int(data.get("duration_days", 14))
    )
    return {"success": True, "data": roadmap}


@app.post("/api/roadmap/smart/task/toggle")
async def toggle_smart_roadmap_task(request: Request):
    data = await request.json()
    result = SmartRoadmapModel.toggle_task(int(data.get("employee_id")), int(data.get("task_id")))
    return result


@app.post("/api/roadmap/smart/adjust")
async def adjust_smart_roadmap(request: Request):
    data = await request.json()
    result = SmartRoadmapModel.auto_adjust(int(data.get("employee_id")), int(data.get("roadmap_id")))
    return result


# =========================================================================
# 3. RESUME BUILDER WITH TRENDING TEMPLATES API
# =========================================================================
@app.get("/api/resume/templates")
def get_resume_templates():
    templates = TrendingTemplateModel.get_active()
    return {"success": True, "templates": templates}


@app.post("/api/resume/versions/save")
async def save_resume_version(request: Request):
    data = await request.json()
    saved = ResumeVersionModel.save_version(
        employee_id=int(data.get("employee_id")),
        version_name=data.get("version_name", "Default Resume"),
        template_name=data.get("template_name", "modern-single"),
        target_role=data.get("target_role", "Software Engineer"),
        target_company=data.get("target_company", "Enterprise"),
        resume_data=data.get("resume_data", {}),
        score=int(data.get("score", 85))
    )
    return {"success": True, "data": saved}


@app.get("/api/resume/versions")
def get_resume_versions(employee_id: int):
    versions = ResumeVersionModel.get_versions(employee_id)
    return {"success": True, "versions": versions}


@app.post("/api/resume/rewrite-bullet")
async def rewrite_bullet(request: Request):
    data = await request.json()
    result = ResumeVersionModel.rewrite_bullet(data.get("bullet_text", ""), data.get("target_role", "Software Engineer"))
    return result


@app.post("/api/resume/score-ats")
async def score_ats(request: Request):
    data = await request.json()
    result = ResumeVersionModel.score_ats(data.get("resume_data", {}), data.get("target_role", "Software Engineer"), data.get("job_description", ""))
    return result


# =========================================================================
# 4. AI FLUENCY ROUND API
# =========================================================================
@app.get("/api/ai-fluency/questions")
def get_ai_fluency_questions(category: str = ""):
    questions = AIFluencyModel.get_questions(category)
    return {"success": True, "questions": questions}


@app.post("/api/ai-fluency/evaluate")
async def evaluate_ai_fluency(request: Request):
    data = await request.json()
    result = AIFluencyModel.evaluate_answer(int(data.get("employee_id")), data.get("question_id"), data.get("candidate_answer", ""))
    return result


@app.get("/api/ai-fluency/history")
def get_ai_fluency_history(employee_id: int):
    history = AIFluencyModel.get_history(employee_id)
    return {"success": True, "data": history}


# =========================================================================
# 5. PRESENT-PAST-FUTURE ANSWER BUILDER API
# =========================================================================
@app.post("/api/answer-builder/analyze")
async def analyze_structured_answer(request: Request):
    data = await request.json()
    analysis = StructuredAnswerModel.analyze(
        employee_id=int(data.get("employee_id", 1)),
        question_title=data.get("question_title", "Tell me about yourself"),
        present_text=data.get("present_text", ""),
        past_text=data.get("past_text", ""),
        future_text=data.get("future_text", ""),
        target_role=data.get("target_role", "Software Engineer"),
        target_company=data.get("target_company", "Enterprise")
    )
    return analysis


@app.post("/api/answer-builder/save")
async def save_structured_answer(request: Request):
    data = await request.json()
    result = StructuredAnswerModel.save(int(data.get("employee_id")), data)
    return result


@app.get("/api/answer-builder/saved")
def get_saved_structured_answers(employee_id: int):
    answers = StructuredAnswerModel.get_saved(employee_id)
    return {"success": True, "data": answers}


# =========================================================================
# 6. NOTICE PERIOD COUNTDOWN PLANNER API
# =========================================================================
@app.get("/api/notice-plan/latest")
def get_latest_notice_plan_api(employee_id: int):
    plan = NoticePlanModel.get_latest_simple_plan(employee_id)
    return {"success": True, "data": plan}


@app.get("/api/notice-plan/active")
def get_active_notice_plan_api(employee_id: int):
    plan = NoticePlanModel.get_active_plan(employee_id)
    return {"success": True, "data": plan}


@app.post("/api/notice-plan/generate")
async def generate_notice_plan_api(request: Request):
    data = await request.json()
    employee_id = int(data.get("employee_id"))
    target_role = (data.get("target_role") or "Software Engineer").strip()
    experience = str(data.get("experience") or data.get("experience_years") or "1-3").strip()
    notice_days = int(data.get("notice_days") or data.get("notice_period_days") or 30)
    weak_areas = data.get("weak_areas") or []

    # Generate simple plan text
    plan_text = generate_simple_notice_plan(target_role, experience, notice_days, weak_areas)
    saved_simple = NoticePlanModel.save_simple_plan(
        employee_id, target_role, experience, notice_days, weak_areas, plan_text
    )

    # Maintain legacy daily task generation if requested
    try:
        plan_dict = generate_notice_period_plan(data)
        NoticePlanModel.save_plan(employee_id, data, plan_dict)
    except Exception:
        pass

    return {"success": True, "data": saved_simple}


@app.post("/api/notice-plan/task/toggle")
async def toggle_notice_plan_task_api(request: Request):
    data = await request.json()
    result = NoticePlanModel.toggle_task(int(data.get("employee_id")), int(data.get("task_id")), data.get("is_completed"))
    return result


@app.get("/api/notice-plan/full")
def get_full_notice_plan_api(employee_id: int):
    plan = NoticePlanModel.get_active_plan(employee_id)
    return {"success": True, "data": plan}


# =========================================================================
# 7. ACHIEVEMENT VAULT API
# =========================================================================
@app.get("/api/achievements")
def get_achievements_api(employee_id: int):
    achievements = AchievementModel.get_all(employee_id)
    return {"success": True, "count": len(achievements), "data": achievements}


@app.get("/api/achievements/{achievement_id}")
def get_achievement_by_id_api(achievement_id: int, employee_id: int):
    item = AchievementModel.get_by_id(achievement_id, employee_id)
    if not item:
        return JSONResponse(status_code=404, content={"success": False, "message": "Achievement not found."})
    return {"success": True, "data": item}


@app.post("/api/achievements/save")
async def save_achievement_api(request: Request):
    data = await request.json()
    employee_id = int(data.get("employee_id"))

    # If STAR fields absent, convert
    if not (data.get("star_situation") and data.get("star_action")):
        transformed = convert_achievement_to_star(data)
        data.update(transformed)

    res = AchievementModel.save(employee_id, data)
    try:
        GamificationModel.add_points(employee_id, 20, "Added STAR Achievement to Vault")
    except Exception:
        pass
    return {"success": True, "message": "Achievement saved to vault!", "data": res.get("achievement")}


@app.delete("/api/achievements/{achievement_id}")
def delete_achievement_api(achievement_id: int, employee_id: int):
    success = AchievementModel.delete(achievement_id, employee_id)
    if not success:
        return JSONResponse(status_code=404, content={"success": False, "message": "Achievement not found."})
    return {"success": True, "message": "Achievement deleted from vault."}


# =========================================================================
# 8. HONEST-TO-PROFESSIONAL ANSWER CONVERTER API
# =========================================================================
@app.get("/api/converted-answers")
def get_converted_answers_api(employee_id: int):
    answers = ConvertedAnswerModel.get_all(employee_id)
    return {"success": True, "count": len(answers), "data": answers}


@app.get("/api/converted-answers/{answer_id}")
def get_converted_answer_by_id_api(answer_id: int, employee_id: int):
    item = ConvertedAnswerModel.get_by_id(answer_id, employee_id)
    if not item:
        return JSONResponse(status_code=404, content={"success": False, "message": "Record not found."})
    return {"success": True, "data": item}


@app.post("/api/converted-answers/convert")
async def convert_answer_api(request: Request):
    data = await request.json()
    res = convert_honest_to_professional(data)
    employee_id = data.get("employee_id")
    payload = {
        "question_type": data.get("question_type") or "Why are you leaving your current job?",
        "raw_answer": data.get("raw_answer") or "",
        "professional_answer": res.get("professional_answer", ""),
        "short_answer": res.get("short_answer", ""),
        "red_flags": res.get("red_flags", []),
        "follow_up_questions": res.get("follow_up_questions", [])
    }
    saved_record = None
    if employee_id:
        try:
            save_res = ConvertedAnswerModel.save(int(employee_id), payload)
            if save_res.get("success"):
                saved_record = save_res.get("converted_answer")
                payload["id"] = save_res.get("id")
        except Exception:
            pass
    return {"success": True, "data": payload, "saved": saved_record, **payload}


@app.post("/api/converted-answers/save")
async def save_converted_answer_api(request: Request):
    data = await request.json()
    employee_id = int(data.get("employee_id"))
    if not data.get("professional_answer"):
        converted = convert_honest_to_professional(data)
        data.update(converted)

    res = ConvertedAnswerModel.save(employee_id, data)
    try:
        GamificationModel.add_points(employee_id, 20, "Reframed Honest Interview Answer")
    except Exception:
        pass
    return {"success": True, "message": "Answer saved to library!", "data": res.get("converted_answer")}


@app.delete("/api/converted-answers/{answer_id}")
def delete_converted_answer_api(answer_id: int, employee_id: int):
    success = ConvertedAnswerModel.delete(answer_id, employee_id)
    if not success:
        return JSONResponse(status_code=404, content={"success": False, "message": "Answer not found."})
    return {"success": True, "message": "Answer deleted."}


# =========================================================================
# 7. COMPANY INTERVIEW PREPARATION ENDPOINTS
# =========================================================================
@app.get("/api/preparation/{company}/questions")
def get_company_questions_fastapi(
    company: str,
    request: Request,
    count: int = 10,
    category: str = "all",
    role: str = "",
    experience_level: str = "",
    question_type: str = "",
    employee_id: int = 0
):
    # Try header if query param employee_id == 0
    if not employee_id:
        h_id = request.headers.get("X-Employee-Id") or request.headers.get("employee-id")
        if h_id:
            try:
                employee_id = int(h_id)
            except ValueError:
                employee_id = 0

    count = min(count, 25)
    normalized_company = QuestionModel.normalize_company(company)

    if experience_level:
        level = QuestionModel.normalize_level(experience_level)
    elif employee_id > 0:
        emp = EmployeeModel.get_by_id(employee_id)
        if emp and emp.get("experience"):
            level = EmployeeModel.map_experience_to_level(emp.get("experience"))
        else:
            level = "fresher (0-1 year)"
    else:
        level = "fresher (0-1 year)"

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
    if len(unseen_questions) < count:
        needed = count - len(unseen_questions)
        existing_texts = QuestionModel.get_all_existing_texts(normalized_company, level)
        ai_questions = generate_company_questions(
            company=normalized_company,
            experience_level=level,
            role=role or "Software Engineer",
            question_type=question_type,
            count=max(needed, 5),
            existing_questions=existing_texts
        )
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
            unseen_questions = QuestionModel.get_unseen_questions(
                employee_id=employee_id,
                company=normalized_company,
                experience_level=level,
                category=category,
                role=role,
                question_type=question_type,
                limit=count
            )

        if len(unseen_questions) == 0 and employee_id > 0:
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

    if employee_id > 0 and unseen_questions:
        UserQuestionHistoryModel.mark_as_seen(employee_id, [q["id"] for q in unseen_questions])


    stats = QuestionModel.get_company_stats(employee_id, normalized_company, level)

    headers = {
        "Cache-Control": "no-store, no-cache, must-revalidate, max-age=0",
        "Pragma": "no-cache",
        "Expires": "0"
    }
    return JSONResponse(
        status_code=200,
        content={
            "success": True,
            "company": normalized_company,
            "experience_level": level,
            "count": len(unseen_questions),
            "questions": unseen_questions,
            "stats": stats,
            "pool_recycled": pool_recycled
        },
        headers=headers
    )


@app.post("/api/preparation/{company}/reset")
async def reset_preparation_history_fastapi(company: str, request: Request):
    data = await request.json() if request.headers.get("content-type", "").startswith("application/json") else {}
    emp_id = data.get("employee_id") or request.headers.get("X-Employee-Id") or request.query_params.get("employee_id")
    try:
        employee_id = int(emp_id)
    except (TypeError, ValueError):
        return JSONResponse(status_code=400, content={"success": False, "message": "Valid employee_id required."})

    normalized_company = QuestionModel.normalize_company(company)
    UserQuestionHistoryModel.reset_history(employee_id, normalized_company)
    stats = QuestionModel.get_company_stats(employee_id, normalized_company)

    return {
        "success": True,
        "message": f"Successfully reset practice history for {normalized_company}.",
        "company": normalized_company,
        "stats": stats
    }


@app.post("/api/employee/experience")
async def update_employee_experience_fastapi(request: Request):
    data = await request.json()
    employee_id = data.get("employee_id")
    experience = (data.get("experience") or "").strip()
    if not employee_id or not experience:
        return JSONResponse(status_code=400, content={"success": False, "message": "employee_id and experience required."})

    updated = EmployeeModel.update_experience(int(employee_id), experience)
    if not updated:
        return JSONResponse(status_code=404, content={"success": False, "message": "Employee not found."})

    mapped_level = EmployeeModel.map_experience_to_level(experience)
    return {
        "success": True,
        "message": "Experience updated successfully.",
        "experience": experience,
        "mapped_level": mapped_level
    }


# =========================================================================
# TEST SECURITY / ANTI-CHEATING API
# =========================================================================
@app.post("/api/test/{attempt_id}/violation")
async def record_test_violation_fastapi(attempt_id: str, request: Request):
    """
    Records an anti-cheating violation during an active test:
    tab_switch, window_blur, fullscreen_exit, copy_paste_attempt, right_click.
    Increments server-authoritative count and returns auto_submit: true if count >= 3.
    """
    data = await request.json() if request.headers.get("content-type", "").startswith("application/json") else {}
    emp_id = data.get("employee_id") or request.headers.get("X-Employee-Id") or request.query_params.get("employee_id")
    try:
        employee_id = int(emp_id)
    except (TypeError, ValueError):
        return JSONResponse(status_code=400, content={"success": False, "message": "Valid employee_id required."})

    event_type = data.get("event_type", "tab_switch")
    duration_away = data.get("duration_away_seconds")

    result = TestSecurityModel.record_violation(
        employee_id=employee_id,
        test_attempt_id=str(attempt_id),
        event_type=event_type,
        duration_away_seconds=duration_away
    )
    return result


@app.get("/api/test/{attempt_id}/security-report")
def get_test_security_report_fastapi(attempt_id: str, request: Request):
    """
    Returns proctoring audit log and violation summary for a test attempt.
    """
    emp_id = request.headers.get("X-Employee-Id") or request.query_params.get("employee_id")
    employee_id = None
    if emp_id:
        try:
            employee_id = int(emp_id)
        except (TypeError, ValueError):
            pass

    report = TestSecurityModel.get_security_report(
        test_attempt_id=str(attempt_id),
        employee_id=employee_id
    )
    return report


# Mount the full Flask application as WSGIMiddleware for complete backward compatibility
flask_app = create_app()
app.mount("/flask", WSGIMiddleware(flask_app))

# Serve frontend static files
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")

