"""
Main entry point for AI Employee Preparation Platform.
Supports both direct Flask execution (py run.py / py main.py)
and ASGI servers (py -m uvicorn main:app --reload).
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from backend.app import create_app
from backend.database import init_db

# Initialize database
init_db()

# Create Flask application instance
flask_app = create_app()

# Expose FastAPI application instance for uvicorn (py -m uvicorn main:app --reload)
try:
    from backend.fastapi_app import app
except Exception:
    try:
        from starlette.middleware.wsgi import WSGIMiddleware
        app = WSGIMiddleware(flask_app)
    except Exception:
        app = flask_app

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0" if os.getenv("PORT") else "127.0.0.1")
    print("=" * 60)
    print("✔ AI Employee Preparation Platform Starting...")
    print(f"✔ Local URL: http://{host}:{port}")
    print("=" * 60)
    flask_app.run(host=host, port=port, debug=True)
