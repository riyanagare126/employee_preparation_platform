"""
API Route Blueprints for AI Employee Preparation Platform
"""
from backend.routes.auth import auth_bp
from backend.routes.aptitude import aptitude_bp
from backend.routes.coding import coding_bp
from backend.routes.interview import interview_bp
from backend.routes.resume import resume_bp
from backend.routes.ai import ai_bp
from backend.routes.skills import skills_bp
from backend.routes.roadmap import roadmap_bp
from backend.routes.analyzer import analyzer_bp
from backend.routes.company import company_bp
from backend.routes.gamification import gamification_bp
from backend.routes.history import history_bp
from backend.routes.admin import admin_bp
from backend.routes.smart_roadmap import smart_roadmap_bp
from backend.routes.ai_fluency import ai_fluency_bp
from backend.routes.answer_builder import answer_builder_bp
from backend.routes.dashboard import dashboard_bp

__all__ = [
    "auth_bp", "aptitude_bp", "coding_bp", "interview_bp", "resume_bp",
    "ai_bp", "skills_bp", "roadmap_bp", "analyzer_bp", "company_bp",
    "gamification_bp", "history_bp", "admin_bp", "smart_roadmap_bp",
    "ai_fluency_bp", "answer_builder_bp", "dashboard_bp"
]
