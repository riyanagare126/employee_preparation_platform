import os
from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
from dotenv import load_dotenv

from backend.database import init_db
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

# Load environment variables
load_dotenv()


def create_app():
    # Resolve frontend directory path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    frontend_dir = os.path.join(base_dir, "frontend")

    app = Flask(__name__, static_folder=frontend_dir, static_url_path="")
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "ai-employee-prep-secret-key-2026")

    # Configure CORS to permit all origins and credentials for development and API consumers
    CORS(app, resources={r"/api/*": {"origins": "*"}}, supports_credentials=True)

    # Initialize SQLite Database tables
    with app.app_context():
        init_db()

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(aptitude_bp)
    app.register_blueprint(coding_bp)
    app.register_blueprint(interview_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(ai_bp)
    app.register_blueprint(skills_bp)
    app.register_blueprint(roadmap_bp)
    app.register_blueprint(analyzer_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(gamification_bp)
    app.register_blueprint(history_bp)
    app.register_blueprint(admin_bp)
    app.register_blueprint(smart_roadmap_bp)
    app.register_blueprint(ai_fluency_bp)
    app.register_blueprint(answer_builder_bp)
    app.register_blueprint(dashboard_bp)

    # Route: Serve Frontend Landing Page
    @app.route("/")
    def index():
        return send_from_directory(frontend_dir, "index.html")

    # Route: Serve any Frontend HTML or Asset files
    @app.route("/<path:filename>")
    def serve_frontend(filename):
        file_path = os.path.join(frontend_dir, filename)
        if os.path.exists(file_path):
            return send_from_directory(frontend_dir, filename)
        # Default fallback to index.html for unknown routes if not an API call
        if not filename.startswith("api/"):
            return send_from_directory(frontend_dir, "index.html")
        return jsonify({"success": False, "message": "Endpoint not found"}), 404

    # API 404 and 500 error handlers
    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"success": False, "message": "Resource not found."}), 404

    @app.errorhandler(500)
    def server_error(e):
        return jsonify({"success": False, "message": "An internal server error occurred."}), 500

    return app


if __name__ == "__main__":
    app = create_app()
    port = int(os.getenv("PORT", 5000))
    print(f"AI Employee Preparation Platform Backend running at http://127.0.0.1:{port}")
    app.run(host="127.0.0.1", port=port, debug=False)
