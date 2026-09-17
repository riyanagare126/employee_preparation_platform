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
    TrendInsightModel
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


# Mount the full Flask application as WSGIMiddleware for complete backward compatibility
flask_app = create_app()
app.mount("/flask", WSGIMiddleware(flask_app))

# Serve frontend static files
app.mount("/", StaticFiles(directory=FRONTEND_DIR, html=True), name="frontend")
