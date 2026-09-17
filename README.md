# AI Employee Preparation & Placement Readiness Platform 🚀

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue.svg)](https://www.python.org/)
[![Database: Supabase PostgreSQL](https://img.shields.io/badge/Database-Supabase%20PostgreSQL-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com/)
[![Deploy: Render](https://img.shields.io/badge/Deploy-Render-46E3B7?logo=render&logoColor=white)](https://render.com/)
[![Tests: 100% Passed](https://img.shields.io/badge/Tests-100%25%20Passed-success.svg)](verify_all_endpoints.py)
[![License: MIT](https://img.shields.io/badge/License-MIT-purple.svg)](LICENSE)

A next-generation, full-stack placement readiness platform designed to prepare engineering students and job candidates for 2026 Tier-1 enterprise recruitment rounds (TCS, Infosys, Google, Amazon, Microsoft).

---

## 🌟 Key Features

* **⚡ 5-Pillar Employee Readiness Score:** Algorithmic composite scoring across Aptitude (25%), Coding (25%), Technical Domain (20%), AI Mock Interviews (15%), and ATS Resume (15%).
* **🏢 Enterprise-Calibrated Smart Roadmaps:** Customized day-wise schedules (7, 14, 30, or 60 days) tailored to specific corporate hiring patterns.
* **📄 2026 ATS Resume Builder:** Single-column layouts with AI STAR-bullet rewriting and JD keyword matching.
* **🧠 2026 AI Fluency Round:** Evaluates candidate tool fluency (Copilot/Cursor), zero-trust test verification discipline, and sprint velocity.
* **⏱️ Present-Past-Future 60s Pitch Builder:** Recruiter-approved 3-box framework with a live 140 WPM speech pacing meter.
* **🗄️ Multi-Database Support:** Seamlessly runs on **Supabase PostgreSQL** in production and **SQLite** in local development.
* **⚙️ Content & Trend Admin CMS:** Real-time publishing of hiring trends, template schemas, and interview questions.

---

## 🏗️ System Architecture

```
[ Client Browser (HTML5 / CSS3 Tokens / Modular JS) ]
                        │
                        ▼ (HTTP REST API)
       [ Flask WSGI / FastAPI ASGI Web Engine ]
                        │
    ┌───────────────────┴───────────────────┐
    ▼                                       ▼
[ Local Development ]              [ Production Cloud ]
  SQLite Database                  Supabase PostgreSQL
(employees.db)                  (Pooled Connection String)
```

---

## 🚀 Quick Start (Local Development)

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/YOUR_USERNAME/employee_preparation_platform.git
cd employee_preparation_platform
pip install -r requirements.txt
```

### 2. Configure Environment (Optional)
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```
*(By default, the platform uses local SQLite. To connect to Supabase, paste your `DATABASE_URL` into `.env`)*.

### 3. Run Platform
```bash
python run.py
```
Open **[http://localhost:5000](http://localhost:5000)** in your browser!

---

## 🗄️ Supabase PostgreSQL Setup

1. Sign up / Log in to [Supabase](https://supabase.com) with your GitHub account.
2. Create a **New Project** and set a database password.
3. Open **SQL Editor** in Supabase, paste the contents of [`supabase_schema.sql`](supabase_schema.sql), and click **Run**.
4. Go to **Project Settings -> Database -> Connection String (URI)**, copy the URL, and set it as `DATABASE_URL`:
   ```env
   DATABASE_URL=postgresql://postgres:[YOUR-PASSWORD]@db.[YOUR-PROJECT-REF].supabase.co:5432/postgres
   ```

---

## ☁️ 1-Click Deployment on Render

[![Deploy to Render](https://render.com/images/deploy-to-render-button.svg)](https://render.com)

1. Log in to [Render](https://render.com) using your GitHub account.
2. Click **New +** -> **Web Service**.
3. Connect your forked / pushed repository.
4. Set the following:
   * **Runtime:** `Python 3`
   * **Build Command:** `pip install -r requirements.txt`
   * **Start Command:** `gunicorn wsgi:app --bind 0.0.0.0:$PORT --workers 2 --threads 4`
5. Under **Environment Variables**, add:
   * `DATABASE_URL`: *(Your Supabase connection string)*
   * `SECRET_KEY`: *(Any secure random string)*
   * `PYTHON_VERSION`: `3.11.9`
6. Click **Deploy Web Service**! Render automatically deploys and provides a free HTTPS domain.

---

## 🧪 Automated Verification Suite

Run all 7 end-to-end integration test suites:
```bash
python verify_all_endpoints.py
```

---

## 📄 Final Project Documentation & Reports

* **Full Academic Report (Markdown):** [`FINAL_PROJECT_REPORT.md`](FINAL_PROJECT_REPORT.md)
* **Printable Web Report:** Open `http://localhost:5000/report.html` and click **Print / Save as PDF**
* **College Viva Voce & Demo Guide:** [`COLLEGE_DEMO_GUIDE.md`](COLLEGE_DEMO_GUIDE.md)

---

## 📜 License
MIT License. Created for Academic and Professional Skill Readiness.
