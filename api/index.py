"""
Vercel Serverless Function entry point
"""
import sys
import os

# Add root directory to python path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from backend.app import create_app
from backend.database import init_db

# Initialize database
init_db()

# Expose app for Vercel WSGI
app = create_app()
