# Supabase PostgreSQL Configuration, GitHub Repository & Render/Vercel Deployment Plan

This plan outlines the end-to-end technical steps to connect the AI Employee Preparation Platform to a **Supabase PostgreSQL** cloud database, initialize and push the project to **GitHub**, and deploy the full-stack application to **Render** (recommended for Python Flask/FastAPI) and/or **Vercel**.

---

## 1. Architectural & Technology Evaluation: Render vs. Vercel

Based on the project's codebase (Python Flask with 17 blueprints, FastAPI ASGI option, Gunicorn/Uvicorn, REST API endpoints, and static HTML5/CSS/JS frontend):

| Feature | Render (Recommended 🏆) | Vercel |
| :--- | :--- | :--- |
| **Runtime Model** | Native Long-Running Web Service (Gunicorn / Uvicorn) | Serverless Functions (`api/index.py`) |
| **Python Support** | First-class native Python 3.10+ environment | Serverless Python with cold-starts & 10s timeout |
| **Database Connection** | Persistent connection pooling to Supabase PostgreSQL | New connection per serverless invocation (requires Supabase connection pooler) |
| **Static File Serving** | Automatically serves all frontend HTML/CSS/JS without routing hacks | Requires URL rewriting rules in `vercel.json` |
| **Deploy Simplicity** | 1-Click deploy with `render.yaml` or `Procfile` | Requires `api/index.py` wrapper + `vercel.json` |

> [!NOTE]
> **Recommendation:** We will deploy to **Render** as the primary, seamless full-stack deployment service, while also supplying `vercel.json` and a serverless entrypoint for full multi-cloud flexibility.

---

## 2. Proposed Implementation Steps

### Phase 1: Supabase PostgreSQL Database Integration
1. **Driver & Dependencies:**
   - Add `psycopg2-binary` (or `pg8000`), `SQLAlchemy`, and `gunicorn` to [`requirements.txt`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/requirements.txt).
2. **Multi-Database Connection Adapter ([`backend/database.py`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/backend/database.py)):**
   - Enhance `get_db_connection()` to detect if `DATABASE_URL` is set to PostgreSQL (`postgresql://...` or `postgres://...`).
   - If PostgreSQL: connect via `psycopg2` with `RealDictCursor` and provide an automatic SQL placeholder translator (`?` to `%s`) so all existing queries in [`backend/models.py`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/backend/models.py) execute transparently without breaking changes.
   - If SQLite (local default): preserve existing local `employees.db` workflow.
3. **Supabase Migration Script (`supabase_schema.sql`):**
   - Create a clean, production-ready SQL script for Supabase's SQL Editor that defines all tables (`employees`, `smart_roadmaps`, `roadmap_tasks`, `resume_versions`, `ai_fluency_attempts`, `structured_answers`, `trend_insights`, `trending_templates`, `gamification`, etc.) with proper PostgreSQL data types, foreign keys, and default seeds.
4. **Environment Variables Configuration ([`.env.example`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/.env.example)):**
   - Add Supabase connection string format:
     ```env
     DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
     SECRET_KEY=ai-employee-prep-secret-key-2026
     PORT=5000
     ```

---

### Phase 2: Production Deployment Configuration (Render & Vercel)
1. **Render Configuration:**
   - Create [`render.yaml`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/render.yaml) defining the Web Service with build command (`pip install -r requirements.txt`) and start command (`gunicorn run:flask_app --bind 0.0.0.0:$PORT`).
   - Create [`Procfile`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/Procfile) for standard Heroku/Render/Railway buildpack compatibility.
   - Create [`runtime.txt`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/runtime.txt) pinning `python-3.11.9`.
2. **Vercel Configuration (Optional Multi-Cloud):**
   - Create `vercel.json` with builds and routes configuration pointing to WSGI handler.
   - Create `api/index.py` exporting the Flask app instance for Vercel Serverless.

---

### Phase 3: Git Installation, Repository Setup & GitHub Push
1. **Git Setup:**
   - Verify/install Git on Windows via `winget install --id Git.Git -e --source winget`.
   - Configure user name and email.
2. **Project Cleanliness & [`.gitignore`](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/.gitignore):**
   - Exclude `.env`, `__pycache__`, `*.pyc`, `backend/database/employees.db`, and temp files.
   - Include reports, documentation, assets, scripts, and source code.
3. **Repository Initialization:**
   - Run `git init -b main`.
   - Add all files: `git add .`.
   - Initial commit: `git commit -m "feat: AI Employee Preparation Platform v2.0 - 2026 Enterprise Placement Edition"`.
4. **GitHub Creation & Push:**
   - Guide/automate creating the repository on GitHub via GitHub CLI (`gh`) or standard remote URL (`git remote add origin ... && git push -u origin main`).

---

### Phase 4: Step-by-Step GitHub Login & Cloud Linkage Guide
1. **Supabase Setup:**
   - Login to [Supabase](https://supabase.com) using your GitHub account.
   - Click "New Project" -> Name it `employee-prep-platform` -> Set a Database Password -> Select region.
   - Copy the **Connection String (URI)** from Project Settings -> Database.
   - Run `supabase_schema.sql` in the Supabase SQL Editor.
2. **Render Setup:**
   - Login to [Render](https://render.com) using your GitHub account.
   - Click "New +" -> "Web Service".
   - Connect the newly created GitHub repository (`employee_preparation_platform`).
   - In Environment Variables, paste `DATABASE_URL` from Supabase and `SECRET_KEY`.
   - Click "Deploy Web Service"! Render builds and gives you a live `https://...onrender.com` URL with free SSL!

---

## 3. User Review Required

> [!IMPORTANT]
> **Git Installation:** `git` is currently not in your system's PATH. We will install it cleanly using Windows Package Manager (`winget`).
> 
> **GitHub Authentication:** To push the repository to your GitHub profile, you will either log in using GitHub CLI (`gh auth login`) or create an empty repository on GitHub and provide the remote URL.
>
> **Supabase Password:** You will need to set a strong database password when creating your free Supabase project, which will be placed into the `DATABASE_URL`.

---

## 4. Verification Plan

### Automated Checks
* Test PostgreSQL adapter in `backend/database.py` with both SQLite fallback and PostgreSQL URL parsing.
* Validate that `requirements.txt` installs cleanly and `py verify_all_endpoints.py` passes 100%.
* Verify `git status` confirms clean commit with correct `.gitignore`.

### Deployment Verification
* Validate `render.yaml`, `Procfile`, and `vercel.json` syntax.
* Verify Supabase SQL schema executes cleanly in PostgreSQL syntax.
