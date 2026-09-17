"""
WSGI entrypoint for production deployment (Render, Gunicorn, Railway, etc.)
"""
import os
from backend.app import create_app
from backend.database import init_db

# Initialize database schema (PostgreSQL if DATABASE_URL is set, else SQLite)
init_db()

# Create production Flask application
app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
