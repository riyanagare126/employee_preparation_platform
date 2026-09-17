"""
AI Employee Preparation Platform
Root Application Entry Point for Render, Gunicorn, and Local Development
"""
import os
import sys

from backend.app import create_app
from backend.database import init_db

# Initialize database schema (PostgreSQL if DATABASE_URL is set, else SQLite)
init_db()

# Create production Flask application instance
app = create_app()

if __name__ == "__main__":
    # Render provides PORT environment variable. Default to 5000 locally.
    port = int(os.getenv("PORT", 5000))
    # Bind to 0.0.0.0 for containerized/cloud deployments, or HOST env var.
    host = os.getenv("HOST", "0.0.0.0")
    print(f"✔ AI Employee Preparation Platform running on http://{host}:{port}")
    app.run(host=host, port=port)
