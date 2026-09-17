# AI Employee Preparation Platform — College Viva & Demo Guide 🎓

## 🚀 How to Open & Run the Project (1-Click)

### Method 1: Double-Click (Easiest)
Simply double-click the **`start_project.bat`** file in the project folder.
1. It automatically checks Python.
2. It initializes and verifies the SQLite database.
3. It launches the server on `http://localhost:5000`.
4. It **automatically opens Google Chrome** to `http://localhost:5000` within 2 seconds!

---

### Method 2: From Terminal / Command Prompt
Open your terminal in the project folder (`c:\Users\JOHN\Desktop\employee_preparation_platform`) and run:
```powershell
py run.py
```
Then open Google Chrome and visit:
👉 **[http://localhost:5000](http://localhost:5000)** (or **[http://127.0.0.1:5000](http://127.0.0.1:5000)**)

*(Note: The server also supports ASGI uvicorn on port 8000 via `py -m uvicorn main:app --reload` and frontend will seamlessly adapt).*

---

## 📄 Formal Final Project Report (Ready for Submission & PDF Print)

A complete, university-grade academic and technical project report has been prepared for submission and viva evaluation:
* **Markdown Document:** [FINAL_PROJECT_REPORT.md](file:///c:/Users/JOHN/Desktop/employee_preparation_platform/FINAL_PROJECT_REPORT.md)
* **Interactive & Printable Browser Version:** 👉 **[http://localhost:5000/report.html](http://localhost:5000/report.html)**
  *(Click the **"🖨️ Print / Save as PDF"** button in Chrome to instantly generate a submission-ready PDF file!)*
* **Key Sections Covered:** Executive Summary, Industry Problem Statement, System Architecture, Relational Database Schema & ER Model, 5-Pillar Readiness Score Algorithm, 2026 AI Fluency & 60s Pitch Engines, REST API Reference, 100% QA Verification Results, and Viva Voce Defense Q&A.

---

## 🔑 Demo Login Credentials

On the **Login Page** (`login.html`), you don't even need to type! There are **1-Click Demo Login buttons**:

| Account Type | Email | Password | What it Shows |
| :--- | :--- | :--- | :--- |
| **Demo Student** *(1-Click Button)* | `student@prep.com` | `Student123!` | **Rahul Sharma** — Pre-loaded with 77% Readiness, 350 XP, 5-Day Streak, Solved Coding Challenges, Aptitude Report, and Unlocked Badges! |
| **Platform Admin** *(1-Click Button)* | `admin@prep.com` | `AdminPassword123!` | System Administrator portal with platform analytics and user logs. |
| **Fresh Registration** | Any email | Any password | Evaluators can also register a brand new account live! |

---

## 🎯 5-Minute College Viva Presentation Flow

### Step 1: Landing Page (`index.html`)
* **Explain to Evaluator:** "This is an AI-powered placement and employee skill readiness platform designed for students and job seekers targeting Tier-1 tech enterprises (TCS, Infosys, Amazon, Google, etc.)."
* **Highlight:** Clean responsive design, modern UI, and direct access to all preparation modules.

### Step 2: 1-Click Demo Login (`login.html`)
* Click **"⚡ Demo Student Login (Rahul Sharma)"**.
* **Explain:** "We have built secure SHA-256 session token authentication with role-based access control (Student vs Admin)."

### Step 3: Interactive Employee Dashboard (`dashboard.html`)
* **Employee Readiness Score Gauge (77/100 - Job Ready 🚀):**
  * Show the 5-pillar transparent calculation:
    - **Aptitude (25% weight)**: 80% score
    - **Coding (25% weight)**: 60% score (3 challenges solved)
    - **Technical Domain (20% weight)**: 86% score
    - **AI Mock Interview (15% weight)**: 84% score
    - **Resume ATS Score (15% weight)**: 84% score
* **Historical Readiness Trend:** Show the historical progression graph: `54 → 62 → 71 → 82`.
* **Interactive Daily Preparation Agenda:**
  * **Interactive Action:** Click the checkbox on any daily task (e.g. *Practice 5 Aptitude Qs*).
  * Notice the instant green checkmark and toast notification!
* **3-Tier Skill Status Matrix:**
  * Displays 🟢 Strong Competencies, 🟡 Developing Skills, and 🔴 Critical Improvement areas.
* **Goal Switcher Modal:**
  * Click **"Switch Company 🔄"** to switch target enterprise (e.g. from TCS to Amazon or Google) with dynamic progress calculation.

### Step 4: 2026 Trending Placement Modules (Showcase These!)

#### A. Smart Prep Roadmap (`roadmap.html`)
* **Explain to Evaluator:** *"Enterprise hiring rounds have diverged significantly. A candidate preparing for TCS needs different focus than Amazon or Microsoft. Our Smart Roadmap generates day-wise preparation schedules tailored to specific companies across 7, 14, 30, or 60 days."*
* **Demonstrate:**
  - Select **"Microsoft"** or **"Google"** from the searchable company dropdown.
  - Select **"14 Days"** duration. Click **"Generate Smart Roadmap ✨"**.
  - Review the categorized daily phases (Fundamentals → System Design → AI Fluency → Mock Interviews).
  - Click any task checkbox: notice instant database toggle and progress calculation!

#### B. 2026 Resume Builder & Trending Templates (`resume.html`)
* **Explain to Evaluator:** *"In 2026, recruiters use strict single-column ATS parsers. We offer 3 modern trending layouts with real-time reactive preview and AI enhancements."*
* **Demonstrate:**
  - Switch between **"Modern Single-Column (ATS Favorite)"**, **"Minimalist Accent"**, and **"Classic Reverse-Chronological"**.
  - Show the **AI Bullet Point Enhancer**: transforms raw statements into quantifiable STAR bullets with metrics and action verbs.
  - Click **"Score Resume with AI 📊"** to show instant keyword matching against target enterprise JDs.
  - Click **"Export Clean PDF 🖨️"** to show the clean print stylesheet.

#### C. 2026 AI Fluency Round (`ai-fluency.html`)
* **Explain to Evaluator:** *"Top tech enterprises in 2026 do not ask 'Do you know AI?'. They test indirect AI tool fluency—whether you naturally leverage tools like Copilot and Cursor while enforcing zero-trust code verification and testing discipline."*
* **Demonstrate:**
  - Select a question (e.g. *Workflow Velocity: Resolving a tricky production bug*).
  - Review the **"What Interviewers Are Listening For"** criteria.
  - Enter an answer and click **"Evaluate Fluency & Security ✨"**.
  - Show the **4-Pillar Score Breakdown**: Tool Integration, Verification Mindset, Workflow Velocity, and Authenticity.
  - Show the **AI Rewritten Version** demonstrating natural conversational delivery.

#### D. Present-Past-Future 60-Second Pitch Builder (`answer-builder.html`)
* **Explain to Evaluator:** *"Recruiters form their initial evaluation within the first 60 seconds. Our 3-Box builder structures introductions into Present (current stack), Past (quantifiable metrics), and Future (company alignment) while live-calibrating spoken pacing (120-165 words)."*
* **Demonstrate:**
  - Click **"💡 Load High-Impact Sample"**.
  - Watch the **Real-Time Speaking Length Gauge** calculate word count and speak duration (`~60s Sweet Spot 🎯`).
  - Click **"Analyze & Polish with AI ✨"** to show structure score and synthesized spoken-word elevator pitch.
  - Click **"💾 Save to My Library"** to demonstrate persistence in candidate profile.

#### E. Trend & Content Admin CMS (`admin.html`)
* **Explain to Evaluator:** *"Placement criteria evolve constantly. Our lightweight CMS enables administrators to publish 2026 hiring trends, manage resume templates, and update AI fluency questions with instant propagation to student dashboards."*
* **Demonstrate:**
  - Switch to **"💡 Trend Insights CMS"**, **"🎨 Resume Templates CMS"**, and **"🧠 AI Fluency Questions CMS"** tabs.
  - Add or toggle an item and see it live without restarting the server.

### Step 5: Gamification & Milestone Badges (`achievements.html`)
* Show the active streak tracking, experience points (XP), and unlocked milestone badges (`Aptitude Ace`, `Code Warrior`, `Streak Champion`).

---

## 💡 Top Viva Questions & Answers

**Q1: What is the architecture of this project?**  
> *"It follows a clean modular client-server architecture. The backend is built with Python (supporting FastAPI ASGI and Flask WSGI), with SQLAlchemy ORM and SQLite as the relational persistence store. The frontend uses semantic HTML5, Vanilla CSS design tokens, and modular JavaScript controllers communicating over REST APIs."*

**Q2: What is the 2026 AI Fluency Round and why is it unique?**  
> *"Unlike basic coding tests, top 2026 tech companies test how developers use AI as a force multiplier without losing critical thinking. Our AI Fluency engine grades candidate responses across 4 distinct dimensions: Tool Integration (leveraging AI pair-programming), Verification Mindset (sanitizing and verifying AI logic with tests), Workflow Velocity (time saved in sprints), and Authenticity (sounding like an engineer, not a bot)."*

**Q3: How does the Present-Past-Future 60-Second Pitch Builder work?**  
> *"It enforces the recruiter-approved framework: Box 1 (Present: active technical identity), Box 2 (Past: measurable metrics and milestones), Box 3 (Future: strategic company alignment). A real-time speaking gauge monitors word count against the standard professional cadence of ~140 words per minute to hit the 50-70 second sweet spot."*

**Q4: How does the Smart Prep Roadmap calibrate to different enterprises?**  
> *"Enterprise requirements vary dramatically—for example, TCS emphasizes core aptitude, OOPs, and DBMS, whereas Google and Microsoft prioritize distributed algorithms, scalability, and system design. Our roadmap engine adjusts day-wise quotas and generates prioritized phase checklists for durations ranging from 7 to 60 days."*

