"""
Pydantic schemas for AI Employee Preparation Platform.
Supports validation for Companies, Company Questions, and Bulk Import/Export.
"""
from typing import Optional, List, Any, Dict, Union
from datetime import datetime
from pydantic import BaseModel, Field, ConfigDict


# ==========================================
# COMPANY SCHEMAS
# ==========================================

class CompanyBase(BaseModel):
    name: str = Field(..., description="Display name of the company")
    slug: str = Field(..., description="Unique URL-friendly slug")
    industry: str = Field(default="IT Services", description="Industry classification")
    difficulty: str = Field(default="Medium", description="Placement difficulty rating")
    logo: str = Field(default="fas fa-building", description="FontAwesome icon or logo URL")
    is_active: int = Field(default=1, description="Active status (1=active, 0=inactive)")
    description: Optional[str] = None
    common_roles: Optional[str] = None
    hiring_rounds: Optional[str] = None
    aptitude_pattern: Optional[str] = None
    coding_pattern: Optional[str] = None
    technical_focus: Optional[str] = None
    hr_tips: Optional[str] = None
    recommended_skills: Optional[str] = None


class CompanyCreate(CompanyBase):
    pass


class CompanyUpdate(BaseModel):
    name: Optional[str] = None
    industry: Optional[str] = None
    difficulty: Optional[str] = None
    logo: Optional[str] = None
    is_active: Optional[int] = None
    description: Optional[str] = None
    common_roles: Optional[str] = None
    hiring_rounds: Optional[str] = None
    aptitude_pattern: Optional[str] = None
    coding_pattern: Optional[str] = None
    technical_focus: Optional[str] = None
    hr_tips: Optional[str] = None
    recommended_skills: Optional[str] = None


class CompanyResponse(CompanyBase):
    id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# ==========================================
# COMPANY QUESTION SCHEMAS
# ==========================================

class CompanyQuestionBase(BaseModel):
    category: str = Field(..., description="aptitude | coding | technical | ai_interview | hr")
    role: str = Field(default="All", description="Target job role (Java Developer, Python Developer, etc.)")
    difficulty: str = Field(default="Medium", description="Easy, Medium, Hard")
    question: str = Field(..., description="Question statement or coding problem title/description")
    options: Optional[Union[List[str], str]] = Field(default=None, description="List of MCQ options or JSON string")
    correct_answer: Optional[str] = Field(default=None, description="Correct option text/key or expected answer")
    explanation: Optional[str] = Field(default=None, description="Detailed explanation or guidance")
    extra: Optional[Union[Dict[str, Any], str]] = Field(default=None, description="Coding starter code, testcases, input/output")
    is_active: int = Field(default=1, description="1=active, 0=inactive")


class CompanyQuestionCreate(CompanyQuestionBase):
    company_id: Optional[int] = None
    company_slug: Optional[str] = None


class CompanyQuestionUpdate(BaseModel):
    category: Optional[str] = None
    role: Optional[str] = None
    difficulty: Optional[str] = None
    question: Optional[str] = None
    options: Optional[Union[List[str], str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    extra: Optional[Union[Dict[str, Any], str]] = None
    is_active: Optional[int] = None


class CompanyQuestionResponse(CompanyQuestionBase):
    id: int
    company_id: int
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)


# ==========================================
# BULK IMPORT / EXPORT SCHEMAS
# ==========================================

class QuestionImportItem(BaseModel):
    category: str
    role: Optional[str] = "All"
    difficulty: Optional[str] = "Medium"
    question: str
    options: Optional[Union[List[str], str]] = None
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    extra: Optional[Union[Dict[str, Any], str]] = None
    is_active: Optional[int] = 1


class BulkImportRequest(BaseModel):
    company_slug: str
    questions: List[QuestionImportItem]


class BulkImportResponse(BaseModel):
    success: bool
    imported: int
    skipped: int
    total: int
    message: str


class BulkExportResponse(BaseModel):
    success: bool
    company_slug: str
    company_name: str
    total_questions: int
    questions: List[Dict[str, Any]]
