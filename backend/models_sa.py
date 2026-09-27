"""
SQLAlchemy ORM Models for AI Employee Preparation Platform.
Provides declarative models bound to backend/database/employees.db.
Supports both SQLAlchemy direct usage and FastAPI dependency injection.
"""
import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, Boolean, DateTime, ForeignKey, UniqueConstraint
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_DIR = os.path.join(BASE_DIR, "database")
DB_PATH = os.path.join(DB_DIR, "employees.db")

RAW_DB_URL = os.getenv("DATABASE_URL")
if RAW_DB_URL and (RAW_DB_URL.startswith("postgresql://") or RAW_DB_URL.startswith("postgres://")):
    DATABASE_URL = RAW_DB_URL.replace("postgres://", "postgresql://", 1)
    engine = create_engine(DATABASE_URL, pool_pre_ping=True)
else:
    DATABASE_URL = f"sqlite:///{DB_PATH}"
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_sa_db():
    """Dependency helper to get a SQLAlchemy database session."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class User(Base):
    __tablename__ = "employees"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    password = Column(String(255), nullable=False)
    qualification = Column(String(150), nullable=False)
    skills = Column(Text, nullable=False)
    experience = Column(String(100), nullable=False)
    job_role = Column(String(100), nullable=False)
    target_company = Column(String(150), default="Tata Consultancy Services (TCS)")
    target_role = Column(String(150), default="Software Engineer")
    extracted_skills_json = Column(Text, nullable=True)
    is_admin = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    roadmaps = relationship("SmartRoadmap", back_populates="employee", cascade="all, delete-orphan")
    resume_versions = relationship("ResumeVersion", back_populates="employee", cascade="all, delete-orphan")
    ai_fluency_attempts = relationship("AIFluencyAttempt", back_populates="employee", cascade="all, delete-orphan")
    structured_answers = relationship("StructuredAnswer", back_populates="employee", cascade="all, delete-orphan")
    notice_plans = relationship("NoticePlan", back_populates="employee", cascade="all, delete-orphan")
    achievements = relationship("Achievement", back_populates="employee", cascade="all, delete-orphan")
    converted_answers = relationship("ConvertedAnswer", back_populates="employee", cascade="all, delete-orphan")


class TrendInsight(Base):
    __tablename__ = "trend_insights"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String(200), nullable=False)
    category = Column(String(100), nullable=False)
    role_tag = Column(String(100), default="All")
    company_tag = Column(String(100), default="All")
    content = Column(Text, nullable=False)
    actionable_tip = Column(Text, nullable=False)
    priority = Column(Integer, default=1)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)


class TrendingTemplate(Base):
    __tablename__ = "trending_templates"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    template_id = Column(String(80), unique=True, nullable=False)
    name = Column(String(120), nullable=False)
    badge_text = Column(String(80), default="Trending 2026")
    description = Column(Text, nullable=False)
    css_class = Column(String(100), nullable=False)
    is_trending = Column(Integer, default=1)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)


class SmartRoadmap(Base):
    __tablename__ = "smart_roadmaps"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    company_name = Column(String(150), nullable=False)
    company_slug = Column(String(100), nullable=False, index=True)
    target_role = Column(String(150), nullable=False)
    duration_days = Column(Integer, nullable=False)
    total_tasks = Column(Integer, default=0)
    completed_tasks = Column(Integer, default=0)
    progress_percent = Column(Float, default=0.0)
    streak_days = Column(Integer, default=1)
    ai_notes = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("User", back_populates="roadmaps")
    tasks = relationship("RoadmapTask", back_populates="roadmap", cascade="all, delete-orphan")


class RoadmapTask(Base):
    __tablename__ = "roadmap_tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    roadmap_id = Column(Integer, ForeignKey("smart_roadmaps.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    day_number = Column(Integer, nullable=False, index=True)
    phase_name = Column(String(150), nullable=False)
    title = Column(String(200), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(80), nullable=False)
    estimated_minutes = Column(Integer, default=45)
    is_completed = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)

    roadmap = relationship("SmartRoadmap", back_populates="tasks")


class ResumeVersion(Base):
    __tablename__ = "resume_versions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    version_name = Column(String(150), nullable=False)
    template_name = Column(String(100), default="modern-single")
    target_role = Column(String(150), nullable=True)
    target_company = Column(String(150), nullable=True)
    resume_data_json = Column(Text, nullable=False)
    score = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("User", back_populates="resume_versions")


class AIFluencyQuestion(Base):
    __tablename__ = "ai_fluency_questions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    question_text = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    difficulty = Column(String(50), default="Medium")
    context_hint = Column(Text, nullable=True)
    ideal_talking_points_json = Column(Text, nullable=True)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)


class AIFluencyAttempt(Base):
    __tablename__ = "ai_fluency_attempts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(Integer, nullable=True)
    question_text = Column(Text, nullable=False)
    candidate_answer = Column(Text, nullable=False)
    overall_score = Column(Integer, nullable=False)
    ai_tool_score = Column(Integer, nullable=False)
    verification_score = Column(Integer, nullable=False)
    velocity_score = Column(Integer, nullable=False)
    communication_score = Column(Integer, nullable=False)
    feedback = Column(Text, nullable=False)
    suggestions_json = Column(Text, nullable=True)
    rewrite_sample = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("User", back_populates="ai_fluency_attempts")


class StructuredAnswer(Base):
    __tablename__ = "structured_answers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    question_key = Column(String(100), nullable=False)
    question_title = Column(String(255), nullable=False)
    target_role = Column(String(150), nullable=True)
    target_company = Column(String(150), nullable=True)
    present_text = Column(Text, nullable=False)
    past_text = Column(Text, nullable=False)
    future_text = Column(Text, nullable=False)
    combined_text = Column(Text, nullable=False)
    speaking_time_seconds = Column(Integer, default=60)
    word_count = Column(Integer, default=0)
    structure_score = Column(Integer, default=0)
    ai_critique = Column(Text, nullable=True)
    ai_optimized_pitch = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow)

    employee = relationship("User", back_populates="structured_answers")


class Company(Base):
    __tablename__ = "companies"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(150), nullable=False)
    slug = Column(String(100), unique=True, nullable=False, index=True)
    industry = Column(String(100), default="IT Services")
    difficulty = Column(String(50), default="Medium")
    logo = Column(String(255), default="fas fa-building")
    is_active = Column(Integer, default=1)
    description = Column(Text, nullable=True)
    common_roles = Column(Text, nullable=True)
    hiring_rounds = Column(Text, nullable=True)
    aptitude_pattern = Column(Text, nullable=True)
    coding_pattern = Column(Text, nullable=True)
    technical_focus = Column(Text, nullable=True)
    hr_tips = Column(Text, nullable=True)
    recommended_skills = Column(Text, nullable=True)
    roadmap_json = Column(Text, nullable=True)
    intel_json = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    questions = relationship("CompanyQuestion", back_populates="company", cascade="all, delete-orphan")


class CompanyQuestion(Base):
    __tablename__ = "company_questions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company_id = Column(Integer, ForeignKey("companies.id", ondelete="CASCADE"), nullable=False, index=True)
    category = Column(String(50), nullable=False, index=True)
    role = Column(String(100), default="All", index=True)
    difficulty = Column(String(50), default="Medium")
    question = Column(Text, nullable=False)
    options = Column(Text, nullable=True)
    correct_answer = Column(Text, nullable=True)
    explanation = Column(Text, nullable=True)
    extra = Column(Text, nullable=True)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    company = relationship("Company", back_populates="questions")


class NoticePlan(Base):
    __tablename__ = "notice_plans"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    target_role = Column(String(150), nullable=False)
    experience_years = Column(String(50), nullable=False)
    notice_period_days = Column(Integer, nullable=False)
    last_working_date = Column(String(50), nullable=False)
    interview_dates_json = Column(Text, default="[]")
    weak_areas_json = Column(Text, default="[]")
    daily_study_time = Column(String(50), default="1 hr")
    inputs_json = Column(Text, nullable=True)
    generated_plan_json = Column(Text, nullable=False)
    is_active = Column(Integer, default=1)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    employee = relationship("User", back_populates="notice_plans")
    tasks = relationship("NoticePlanTask", back_populates="notice_plan", cascade="all, delete-orphan")


class NoticePlanTask(Base):
    __tablename__ = "notice_plan_tasks"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    notice_plan_id = Column(Integer, ForeignKey("notice_plans.id", ondelete="CASCADE"), nullable=False, index=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    day_number = Column(Integer, nullable=False, index=True)
    task_key = Column(String(100), nullable=False)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    category = Column(String(80), nullable=False)
    estimated_minutes = Column(Integer, default=30)
    link_url = Column(String(255), nullable=True)
    is_completed = Column(Integer, default=0)
    completed_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    notice_plan = relationship("NoticePlan", back_populates="tasks")


class NoticePlanRecord(Base):
    __tablename__ = "notice_plan"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    target_role = Column(String(150), nullable=False)
    experience = Column(String(50), nullable=False)
    notice_days = Column(Integer, nullable=False)
    weak_areas = Column(Text, nullable=True)
    plan_text = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)


class Achievement(Base):
    __tablename__ = "achievements"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    title = Column(String(255), nullable=False)
    raw_description = Column(Text, nullable=False)
    metrics_result = Column(Text, nullable=False)
    skills_used = Column(Text, nullable=False)
    star_situation = Column(Text, nullable=False)
    star_task = Column(Text, nullable=False)
    star_action = Column(Text, nullable=False)
    star_result = Column(Text, nullable=False)
    mapped_questions_json = Column(Text, default="[]")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    employee = relationship("User", back_populates="achievements")


class ConvertedAnswer(Base):
    __tablename__ = "converted_answer"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    question_type = Column(String(150), nullable=False)
    raw_answer = Column(Text, nullable=False)
    professional_answer = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    employee = relationship("User", back_populates="converted_answers")


class ConvertedAnswerLegacy(Base):
    __tablename__ = "converted_answers"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    question_type = Column(String(150), nullable=False)
    raw_answer = Column(Text, nullable=False)
    professional_answer = Column(Text, nullable=False)
    short_answer = Column(Text, nullable=False, default="")
    red_flags_json = Column(Text, default="[]")
    follow_up_questions_json = Column(Text, default="[]")
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)



class Question(Base):
    """
    Company-specific, level-wise interview preparation question repository.
    Tracks questions across difficulty, category, and strict experience levels.
    """
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    company = Column(String(100), nullable=False, index=True)
    category = Column(String(100), nullable=False)
    role = Column(String(100), nullable=True, default="")
    difficulty = Column(String(50), nullable=False, default="medium")
    experience_level = Column(String(80), nullable=False, index=True)
    question_type = Column(String(80), nullable=False, index=True)
    question_text = Column(Text, nullable=False)
    sample_answer = Column(Text, nullable=True)
    question_hash = Column(String(64), nullable=False)
    source = Column(String(50), nullable=False, default="seed")
    created_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("company", "question_hash", name="uq_company_question_hash"),
    )

    history_records = relationship("UserQuestionHistory", back_populates="question", cascade="all, delete-orphan")


class UserQuestionHistory(Base):
    """
    Tracks which questions each employee has already seen to guarantee zero repetition.
    """
    __tablename__ = "user_question_history"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    question_id = Column(Integer, ForeignKey("questions.id", ondelete="CASCADE"), nullable=False, index=True)
    seen_at = Column(DateTime, default=datetime.utcnow)

    __table_args__ = (
        UniqueConstraint("employee_id", "question_id", name="uq_user_question"),
    )

    employee = relationship("User", backref="seen_questions")
    question = relationship("Question", back_populates="history_records")


class SecureTestSession(Base):
    __tablename__ = "secure_test_sessions"

    session_id = Column(String(100), primary_key=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    test_type = Column(String(50), nullable=False)
    job_role = Column(String(150), nullable=True)
    questions_json = Column(Text, nullable=False)
    options_map_json = Column(Text, nullable=True)
    duration_seconds = Column(Integer, nullable=False)
    start_epoch = Column(Float, nullable=False)
    tab_token = Column(String(100), nullable=False)
    status = Column(String(50), default="active")
    answers_json = Column(Text, nullable=True)
    score = Column(Integer, nullable=True)
    percentage = Column(Float, nullable=True)
    performance_message = Column(String(255), nullable=True)
    result_json = Column(Text, nullable=True)
    violation_count = Column(Integer, default=0)
    auto_submitted = Column(Integer, default=0)
    mode = Column(String(20), default="mock")
    started_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    submitted_at = Column(DateTime, nullable=True)

    employee = relationship("User", backref="secure_sessions")


class TestAttempt(Base):
    __tablename__ = "test_attempts"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    company_id = Column(Integer, nullable=True)
    company_slug = Column(String(100), nullable=False, index=True)
    role_name = Column(String(150), nullable=True)
    test_type = Column(String(50), nullable=False)
    score = Column(Float, nullable=False)
    total = Column(Float, nullable=False)
    percentage = Column(Float, nullable=False)
    status = Column(String(50), default="completed")
    details_json = Column(Text, nullable=True)
    violation_count = Column(Integer, default=0)
    auto_submitted = Column(Integer, default=0)
    mode = Column(String(20), default="mock")
    started_at = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", backref="test_attempts_list")


class TestSecurityLog(Base):
    """
    Records security and proctoring events during online tests:
    - tab_switch: User left test tab / browser minimized
    - window_blur: Focus moved away to external window or app
    - fullscreen_exit: Candidate escaped or exited mandatory fullscreen mode
    - copy_paste_attempt: Keyboard copy/cut/paste attempt
    - right_click: Context menu attempt
    """
    __tablename__ = "test_security_logs"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    employee_id = Column(Integer, ForeignKey("employees.id", ondelete="CASCADE"), nullable=False, index=True)
    test_attempt_id = Column(String(100), nullable=False, index=True)
    event_type = Column(String(50), nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    duration_away_seconds = Column(Float, nullable=True)

    employee = relationship("User", backref="security_logs")


# Ensure all tables exist when SQLAlchemy models are loaded
try:
    Base.metadata.create_all(bind=engine)
except Exception as _e_sa:
    pass



