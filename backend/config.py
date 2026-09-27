"""
Configuration module for AI Employee Preparation Platform.
Standardizes environment variables across Flask and FastAPI instances.
"""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB_DIR = os.path.join(BASE_DIR, "backend", "database")
DEFAULT_SQLITE_PATH = os.path.join(DB_DIR, "employees.db")

DATABASE_URL = os.getenv("DATABASE_URL")
if not DATABASE_URL:
    DATABASE_URL = f"sqlite:///{DEFAULT_SQLITE_PATH}"
elif DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

SECRET_KEY = os.getenv("SECRET_KEY", "ai-employee-prep-secret-key-2026")
PORT = int(os.getenv("PORT", 5000))
HOST = os.getenv("HOST", "0.0.0.0" if os.getenv("PORT") else "127.0.0.1")

# AI API Keys
AI_API_KEY = (
    os.getenv("AI_API_KEY") or
    os.getenv("OPENAI_API_KEY") or
    os.getenv("GEMINI_API_KEY") or
    os.getenv("GROQ_API_KEY") or
    ""
)
