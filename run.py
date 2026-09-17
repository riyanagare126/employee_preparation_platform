#!/usr/bin/env python3
"""
AI Employee Preparation Platform
Main Entry Point to initialize database and launch Flask server.
"""
import os
import sys

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

from backend.app import create_app
from backend.database import init_db

if __name__ == "__main__":
    print("=" * 60)
    print("[INIT] Initializing AI Employee Preparation Platform...")
    print("=" * 60)
    
    # Initialize SQLite database schema
    init_db()
    print("✔ SQLite Database verified and initialized.")
    
    # Start Flask Web Server
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    host = os.getenv("HOST", "0.0.0.0" if os.getenv("PORT") else "127.0.0.1")
    
    print(f"✔ Backend server starting on http://{host}:{port}")
    print(f"✔ Serving frontend from: http://{host}:{port}/")
    print("=" * 60)
    
    app.run(host=host, port=port, debug=True)
