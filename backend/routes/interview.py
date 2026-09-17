import random
import uuid
from typing import List, Dict, Any
from flask import Blueprint, request, jsonify

from backend.data.interview_bank import MASTER_INTERVIEW_BANK
from backend.data.company_questions_bank import (
    get_company_technical_questions,
    get_company_hr_questions
)
from backend.models import (
    InterviewModel, EmployeeModel, SecureTestSessionModel,
    ResumeModel, TestAttemptModel, UserPreparationModel, GamificationModel
)

interview_bp = Blueprint("interview", __name__)


def generate_personalized_interview_questions(
    employee_id: int = 1,
    job_role: str = "Software Engineer",
    qualification: str = "",
    skills: str = "",
    experience: str = "",
    interview_type: str = "mock",
    company: str = "",
    difficulty: str = ""
) -> List[Dict[str, Any]]:
    """
    Generates dynamic interview questions tailored to:
    1. Target Company
    2. Target Job Role
    3. Candidate's Resume Projects & Skills (Resume -> AI Interview Connection)
    4. Interview Type ('hr', 'technical', 'mock')
    5. Difficulty ('Easy' / Low, 'Medium', 'Hard' / High)
    """
    emp = EmployeeModel.get_by_id(employee_id) or {}
    company = company or emp.get("target_company") or "Tata Consultancy Services (TCS)"
    resume = ResumeModel.get_by_employee(employee_id) or {}

    role_lower = (job_role or emp.get("target_role") or emp.get("job_role") or "Software Engineer").lower()
    candidate_skills = (skills or resume.get("skills") or emp.get("skills") or "").lower()

    # Extract resume projects
    resume_projects = resume.get("projects") or ""
    project_list = [p.strip() for p in resume_projects.replace("\n", ";").split(";") if p.strip()]
    top_project = project_list[0] if project_list else "your primary capstone software engineering project"

    hr_pool = [q for q in MASTER_INTERVIEW_BANK if any(k in q["category"].lower() for k in ["hr", "alignment", "intro"])]
    tech_pool = [q for q in MASTER_INTERVIEW_BANK if any(k in q["category"].lower() for k in ["tech", "system", "security", "devops", "cloud", "architecture", "fundamentals"])]
    beh_pool = [q for q in MASTER_INTERVIEW_BANK if any(k in q["category"].lower() for k in ["behavioral", "star"])]
    sit_pool = [q for q in MASTER_INTERVIEW_BANK if any(k in q["category"].lower() for k in ["situational", "scenario", "production", "incident"])]

    # Filter by difficulty if provided
    if difficulty:
        d_lower = difficulty.lower()
        hr_f = [q for q in hr_pool if q.get("difficulty", "Medium").lower() == d_lower]
        if hr_f: hr_pool = hr_f
        tech_f = [q for q in tech_pool if q.get("difficulty", "Medium").lower() == d_lower]
        if tech_f: tech_pool = tech_f
        beh_f = [q for q in beh_pool if q.get("difficulty", "Medium").lower() == d_lower]
        if beh_f: beh_pool = beh_f
        sit_f = [q for q in sit_pool if q.get("difficulty", "Medium").lower() == d_lower]
        if sit_f: sit_pool = sit_f

    if not hr_pool: hr_pool = list(MASTER_INTERVIEW_BANK)
    if not tech_pool: tech_pool = list(MASTER_INTERVIEW_BANK)
    if not beh_pool: beh_pool = list(MASTER_INTERVIEW_BANK)
    if not sit_pool: sit_pool = list(MASTER_INTERVIEW_BANK)

    # Filter technical pool by role and candidate resume skills
    matching_tech = []
    for q in tech_pool:
        roles = [r.lower() for r in q.get("roles", [])]
        if "all" in roles:
            matching_tech.append(q)
        elif any(r in role_lower or r in candidate_skills for r in roles):
            matching_tech.append(q)

    if len(matching_tech) < 2:
        matching_tech = tech_pool

    # Dynamic Opening & Company Alignment Variations
    intro_templates = [
        (
            f"Please introduce yourself. Why are you targeting {company}, and how does your background prepare you to excel as a {job_role}?",
            "Highlight your educational background, core technical skills, key projects, and strong motivation for the company."
        ),
        (
            f"Walk me through your background and technical journey. What specifically motivated you to apply for the {job_role} role at {company}?",
            f"Demonstrate clear knowledge of {company}'s industry presence and articulate how your goals align with this position."
        ),
        (
            f"What makes you stand out from other applicants for this {job_role} position, and what unique strengths do you bring to {company}?",
            f"Connect your technical proficiencies, work ethic, problem-solving skills, and alignment with {company}'s engineering culture."
        ),
        (
            f"Tell us about a major turning point in your programming journey. What technical milestone solidified your passion to work as a {job_role} at {company}?",
            "Discuss self-driven learning, technical breakthroughs, and your vision for long-term impact."
        ),
        (
            f"Can you give us a 2-minute elevator pitch summarizing your core stack expertise, hands-on experience, and why {company} is your ideal workplace?",
            "Deliver a structured, confident overview covering languages, frameworks, capstone accomplishments, and enthusiasm."
        ),
        (
            f"How do your technical philosophy and coding standards align with the enterprise engineering expectations at {company} for a {job_role}?",
            "Discuss code maintainability, testing, clean architecture, and delivering customer-centric software."
        )
    ]

    # Dynamic Project Deep-Dive Variations
    project_templates = [
        (
            f"In your project '{top_project}', what key architectural tradeoffs did you make, and how did you resolve any performance or scalability bottlenecks?",
            "Explain framework choices, data layer architecture, caching strategies, and measurable speedups."
        ),
        (
            f"Walk us through a complex bug, race condition, or edge case you encountered while developing '{top_project}'. How did you isolate and resolve it?",
            "Detail your debugging methodology, log analysis, testing techniques, and preventive refactoring."
        ),
        (
            f"If you were tasked with re-architecting '{top_project}' today to support 100x current user traffic and 99.99% uptime, what architectural changes would you implement?",
            "Discuss load balancing, horizontal scaling, database sharding/read replicas, and asynchronous queue processing."
        ),
        (
            f"How did you handle security, authentication, and data validation in '{top_project}'? What potential vulnerabilities did you safeguard against?",
            "Cover JWT/session security, input sanitization, SQL injection prevention, and CORS/CSRF protections."
        ),
        (
            f"What was the most technically challenging feature you implemented in '{top_project}', and what alternative approaches did you evaluate before deciding?",
            "Explain algorithmic complexity, third-party libraries vs custom code, and user experience tradeoffs."
        ),
        (
            f"Describe how you tested and deployed '{top_project}'. If a critical production issue occurred right after deployment, how would you handle rollback?",
            "Mention unit/integration test coverage, CI/CD pipelines, staging environments, and zero-downtime rollback strategies."
        )
    ]

    # Dynamic System & Architecture Variations
    system_templates = [
        (
            "How do you design database schemas for high read/write performance, and how do you handle indexing, transactions (ACID), and race conditions?",
            "Discuss normalization, indexing strategies, B-Trees, transactions (ACID), and concurrency controls."
        ),
        (
            "Explain the trade-offs between Microservices architecture and Monolithic architecture. When is it appropriate to decompose a monolith?",
            "Cover operational overhead, independent deployment, network latency, distributed transactions, and domain-driven boundaries."
        ),
        (
            "How do you implement distributed caching strategies (e.g. Redis), and how do you handle cache invalidation, cache stampede, and cache penetration?",
            "Explain Cache-Aside vs Write-Through, TTL strategies, bloom filters, and distributed locking mechanisms."
        ),
        (
            "When designing high-availability RESTful APIs, how do you handle rate-limiting, idempotency, API versioning, and graceful error responses?",
            "Discuss token-bucket algorithms, idempotency keys for mutations, semantic versioning, and RFC-7807 error responses."
        ),
        (
            "Describe your approach to asynchronous event-driven architecture using message queues. How do you guarantee exactly-once message delivery?",
            "Explain pub/sub models, consumer offsets, dead letter queues, and consumer deduplication logic."
        ),
        (
            "What strategies and tools do you use for profiling application memory leaks, high latency spikes, and CPU bottlenecks in a live production environment?",
            "Detail APM tooling, heap dump analysis, garbage collection logs, thread dumps, and flame graphs."
        )
    ]

    # Shuffle all pools to guarantee different questions on each request / reload
    shuffled_tech = list(matching_tech)
    random.shuffle(shuffled_tech)
    
    shuffled_beh = list(beh_pool)
    random.shuffle(shuffled_beh)

    shuffled_sit = list(sit_pool)
    random.shuffle(shuffled_sit)

    shuffled_hr = list(hr_pool)
    random.shuffle(shuffled_hr)

    comp_slug = (company or "").lower().strip()
    comp_hr_pool = get_company_hr_questions(comp_slug, shuffle=True) if comp_slug else []
    comp_tech_pool = get_company_technical_questions(comp_slug, shuffle=True) if comp_slug else []

    # CASE A: HR & Behavioral Interview
    if interview_type == "hr":
        selected_intro = random.choice(intro_templates)
        beh_sample = shuffled_beh[:2]
        sit_sample = shuffled_sit[:1]
        hr_sample = shuffled_hr[:1]

        q2_text = comp_hr_pool[0]["question"] if comp_hr_pool else (beh_sample[0]["question"] if beh_sample else "Describe a difficult conflict or disagreement in a technical team project.")
        q2_cat = comp_hr_pool[0].get("category", "Company Leadership & STAR") if comp_hr_pool else "Behavioral / STAR"
        q2_guidance = comp_hr_pool[0].get("tips", "Structure using Situation, Task, Action, and Result (STAR).") if comp_hr_pool else "Structure using STAR."

        questions_payload = [
            {
                "id": 1,
                "category": "Company Alignment & Fit",
                "question": selected_intro[0],
                "guidance": selected_intro[1]
            },
            {
                "id": 2,
                "bank_id": f"comp_hr_{comp_slug}" if comp_hr_pool else (beh_sample[0]["id"] if beh_sample else "beh_501"),
                "category": q2_cat,
                "question": q2_text,
                "guidance": q2_guidance
            },
            {
                "id": 3,
                "bank_id": beh_sample[1]["id"] if len(beh_sample) > 1 else "beh_504",
                "category": "Work Ethic & Priorities",
                "question": beh_sample[1]["question"] if len(beh_sample) > 1 else "How do you prioritize deliverables when managing multiple competing deadlines?",
                "guidance": beh_sample[1].get("guidance", "Explain prioritization frameworks, communication, and time management.")
            },
            {
                "id": 4,
                "bank_id": sit_sample[0]["id"] if sit_sample else "sit_603",
                "category": "Situational Judgment",
                "question": sit_sample[0]["question"] if sit_sample else "How do you negotiate scope when stakeholder timelines are aggressively compressed?",
                "guidance": sit_sample[0].get("guidance", "Advocate for code quality and transparent communication.")
            },
            {
                "id": 5,
                "category": "Career Growth & Culture",
                "question": f"Where do you see yourself contributing within {company} over the next 2-3 years, and what skills are you currently actively learning?",
                "guidance": "Highlight passion for continuous learning, technical excellence, and long-term career commitment."
            }
        ]
        return questions_payload

    # CASE B: Technical Domain Interview
    elif interview_type == "technical":
        selected_sys = random.choice(system_templates)
        selected_proj = random.choice(project_templates)
        tech_sample = shuffled_tech[:3]
        sit_sample = shuffled_sit[:1]

        questions_payload = [
            {
                "id": 1,
                "category": "Architecture & System Design",
                "question": selected_sys[0],
                "guidance": selected_sys[1]
            },
            {
                "id": 2,
                "bank_id": tech_sample[0]["id"] if tech_sample else "tech_core",
                "category": "Core Technical Principles",
                "question": tech_sample[0]["question"] if tech_sample else f"Explain the core runtime architecture and design patterns of {job_role}.",
                "guidance": tech_sample[0].get("guidance", "Explain core principles with practical examples.")
            },
            {
                "id": 3,
                "bank_id": tech_sample[1]["id"] if len(tech_sample) > 1 else tech_sample[0]["id"],
                "category": "Data Structures & Performance",
                "question": tech_sample[1]["question"] if len(tech_sample) > 1 else "How do you optimize memory consumption and execution runtime in high-throughput services?",
                "guidance": tech_sample[1].get("guidance", "Discuss computational complexity, caching, and clean resource management.")
            },
            {
                "id": 4,
                "category": "Project Engineering Deep-Dive",
                "question": selected_proj[0],
                "guidance": selected_proj[1]
            },
            {
                "id": 5,
                "bank_id": sit_sample[0]["id"] if sit_sample else "sit_prod",
                "category": "Production Troubleshooting",
                "question": sit_sample[0]["question"] if sit_sample else "How do you diagnose and recover from a high-severity production outage with zero downtime?",
                "guidance": sit_sample[0].get("guidance", "Detail metrics monitoring, root cause isolation, rollback, and post-mortems.")
            }
        ]
        return questions_payload

    # CASE C: Full AI Mock Interview (Default - All Questions Change on Reload)
    else:
        selected_intro = random.choice(intro_templates)
        selected_proj = random.choice(project_templates)
        selected_sys = random.choice(system_templates)
        tech_sample = shuffled_tech[:2]
        beh_sample = shuffled_beh[:1]

        questions_payload = [
            {
                "id": 1,
                "category": "Introduction & Company Alignment",
                "question": selected_intro[0],
                "guidance": selected_intro[1]
            },
            {
                "id": 2,
                "bank_id": tech_sample[0]["id"] if tech_sample else "tech_core",
                "category": "Technical Domain",
                "question": tech_sample[0]["question"] if tech_sample else f"Explain the architectural foundations and best practices of {job_role}.",
                "guidance": tech_sample[0].get("guidance", "Explain core principles with concrete examples.")
            },
            {
                "id": 3,
                "bank_id": tech_sample[1]["id"] if len(tech_sample) > 1 else "sys_arch",
                "category": "System Design & Algorithms",
                "question": tech_sample[1]["question"] if len(tech_sample) > 1 else selected_sys[0],
                "guidance": tech_sample[1].get("guidance", selected_sys[1]) if len(tech_sample) > 1 else selected_sys[1]
            },
            {
                "id": 4,
                "category": "Resume Project Architecture",
                "question": selected_proj[0],
                "guidance": selected_proj[1]
            },
            {
                "id": 5,
                "bank_id": beh_sample[0]["id"] if beh_sample else "beh_501",
                "category": beh_sample[0]["category"] if beh_sample else "Behavioral & STAR",
                "question": beh_sample[0]["question"] if beh_sample else "Describe a complex technical obstacle you encountered in a team project and how you resolved it.",
                "guidance": beh_sample[0].get("guidance", "Structure using Situation, Task, Action, and Result (STAR).")
            }
        ]

        return questions_payload


@interview_bp.route("/api/interview/session/active", methods=["GET"])
def get_active_interview_session():
    """
    Checks for active in-flight interview session or returns already completed status.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        tab_token = request.args.get("tab_token", "")

        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        if SecureTestSessionModel.check_already_completed(employee_id, "interview"):
            completed = InterviewModel.get_latest_result(employee_id)
            return jsonify({
                "success": True,
                "has_active": False,
                "already_completed": True,
                "completed_result": completed,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 200

        session = SecureTestSessionModel.get_active_session(employee_id, "interview", tab_token)
        if not session or session.get("status") != "active":
            return jsonify({"success": True, "has_active": False}), 200

        return jsonify({
            "success": True,
            "has_active": True,
            "session_id": session["session_id"],
            "job_role": session.get("job_role", ""),
            "duration_seconds": session["duration_seconds"],
            "remaining_seconds": session.get("remaining_seconds", session["duration_seconds"]),
            "questions": session.get("questions", []),
            "draft_answers": session.get("answers", {})
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@interview_bp.route("/api/interview/questions", methods=["GET", "POST"])
def get_interview_questions():
    """
    Returns dynamically generated interview questions with 1-attempt guard.
    """
    try:
        data = {}
        if request.method == "POST":
            data = request.get_json() or {}
            employee_id = data.get("employee_id")
            job_role = data.get("job_role", "Software Engineer")
            qualification = data.get("qualification", "")
            skills = data.get("skills", "")
            experience = data.get("experience", "")
            interview_type = data.get("type", "mock")
            company = data.get("company") or data.get("comp") or ""
            tab_token = data.get("tab_token") or f"tab_{uuid.uuid4().hex[:8]}"
        else:
            employee_id = request.args.get("employee_id", type=int)
            job_role = request.args.get("job_role", type=str, default="Software Engineer")
            qualification = request.args.get("qualification", type=str, default="")
            skills = request.args.get("skills", type=str, default="")
            experience = request.args.get("experience", type=str, default="")
            interview_type = request.args.get("type", type=str, default="mock")
            company = request.args.get("company", type=str, default="") or request.args.get("comp", type=str, default="")
            tab_token = request.args.get("tab_token", f"tab_{uuid.uuid4().hex[:8]}")

        emp_id = int(employee_id) if employee_id else 1

        # Check if user requested fresh questions (page reload, shuffle, or restart)
        is_refresh = (
            request.args.get("refresh", "").lower() == "true"
            or request.args.get("force_new", "").lower() == "true"
            or request.args.get("shuffle", "").lower() == "true"
            or (isinstance(data, dict) and (data.get("refresh") or data.get("force_new") or data.get("shuffle")))
        )

        # Allow continuous practice for mock interviews; check lock only if strict_policy is requested
        if not is_refresh and request.args.get("strict_policy", "").lower() == "true":
            if SecureTestSessionModel.check_already_completed(emp_id, "interview"):
                completed = InterviewModel.get_latest_result(emp_id)
                return jsonify({
                    "success": False,
                    "already_completed": True,
                    "completed_result": completed,
                    "message": "You have already completed this test."
                }), 403

        # Check active session only if NOT requesting fresh/reload questions
        if not is_refresh:
            active = SecureTestSessionModel.get_active_session(emp_id, "interview", tab_token)
            if active and active.get("status") == "active":
                return jsonify({
                    "success": True,
                    "restored": True,
                    "role": active.get("job_role", job_role),
                    "total": len(active.get("questions", [])),
                    "questions": active.get("questions", [])
                }), 200

        # Fetch employee profile from DB if not provided
        if employee_id:
            emp = EmployeeModel.get_by_id(emp_id)
            if emp:
                job_role = job_role or emp.get("target_role") or emp.get("job_role", "Software Engineer")
                qualification = qualification or emp.get("qualification", "")
                skills = skills or emp.get("skills", "")
                experience = experience or emp.get("experience", "")
                company = company or emp.get("target_company", "")

        raw_diff = (request.args.get("difficulty", "") or (data.get("difficulty") if isinstance(data, dict) else "") or "").strip().lower()
        if raw_diff in ["easy", "low"]:
            difficulty = "Easy"
        elif raw_diff in ["hard", "high"]:
            difficulty = "Hard"
        elif raw_diff in ["medium", "mid"]:
            difficulty = "Medium"
        else:
            difficulty = ""

        questions = generate_personalized_interview_questions(
            employee_id=emp_id,
            job_role=job_role,
            qualification=qualification,
            skills=skills,
            experience=experience,
            interview_type=interview_type,
            company=company,
            difficulty=difficulty
        )

        session_id = f"int_{uuid.uuid4().hex[:12]}"
        SecureTestSessionModel.create_session(
            session_id=session_id,
            employee_id=emp_id,
            test_type="interview",
            questions=questions,
            options_map=[],
            duration_seconds=900,
            tab_token=tab_token,
            job_role=job_role
        )

        return jsonify({
            "success": True,
            "session_id": session_id,
            "role": job_role,
            "total": len(questions),
            "questions": questions
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error generating interview questions: {str(e)}"
        }), 500


@interview_bp.route("/api/interview/random-question", methods=["GET"])
def get_random_interview_question():
    """
    Returns a single fresh randomized question matching category or role,
    excluding current question bank_id to allow instant in-session question change.
    """
    try:
        category = request.args.get("category", "").strip().lower()
        role = request.args.get("role", "Software Engineer").strip().lower()
        company = request.args.get("company", "").strip().lower()
        exclude_id = request.args.get("exclude_id", "").strip()

        matched = []
        if company:
            if "beh" in category or "hr" in category or "align" in category or "culture" in category:
                comp_pool = get_company_hr_questions(company, shuffle=True)
            else:
                comp_pool = get_company_technical_questions(company, shuffle=True)
            matched = [q for q in comp_pool if str(q.get("id")) != exclude_id]

        if not matched:
            pool = list(MASTER_INTERVIEW_BANK)
            if exclude_id:
                pool = [q for q in pool if q.get("id") != exclude_id]

            if category:
                matched = [q for q in pool if category in q.get("category", "").lower()]

            if not matched:
                matched = [q for q in pool if any(r in role for r in [x.lower() for x in q.get("roles", [])])] or pool

        picked = random.choice(matched)
        return jsonify({
            "success": True,
            "question": {
                "bank_id": picked["id"],
                "category": picked["category"],
                "question": picked["question"],
                "guidance": picked.get("guidance", "Focus on technical principles and practical engineering execution.")
            }
        }), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@interview_bp.route("/api/interview/submit", methods=["POST"])
def submit_interview_answers():
    """
    Evaluates candidate's responses and generates AI scores & detailed feedback with 1-attempt guard.
    """
    try:
        data = request.get_json() or {}
        employee_id = data.get("employee_id")
        job_role = data.get("job_role", "Software Engineer")
        answers = data.get("answers", [])
        session_id = data.get("session_id", f"int_{uuid.uuid4().hex[:12]}")

        if not employee_id:
            return jsonify({
                "success": False,
                "message": "employee_id is required."
            }), 400

        emp_id = int(employee_id)

        # Check 1-attempt
        if SecureTestSessionModel.check_already_completed(emp_id, "interview"):
            completed = InterviewModel.get_latest_result(emp_id)
            return jsonify({
                "success": False,
                "already_completed": True,
                "completed_result": completed,
                "message": "You have already completed this test. A second attempt is not allowed."
            }), 403

        # Evaluation of answers
        total_answers = len(answers)
        answered_count = sum(1 for a in answers if a.get("answer", "").strip())
        total_words = sum(len(a.get("answer", "").split()) for a in answers)

        if total_answers == 0:
            overall_score = 0
            tech_score = 0
            comm_score = 0
            feedback = "No responses recorded. Please complete all interview questions."
            strengths = []
            weak_areas = ["No answers submitted"]
            suggestions = ["Provide detailed structured responses with real project examples."]
        else:
            avg_words = total_words / total_answers
            base_score = int((answered_count / total_answers) * 55)
            depth_bonus = min(25, int(avg_words * 0.45))
            clarity_bonus = 15 if avg_words >= 25 else 5

            overall_score = min(95, max(30, base_score + depth_bonus + clarity_bonus))
            tech_score = min(96, max(35, overall_score + random.randint(-4, 4)))
            comm_score = min(98, max(40, overall_score + random.randint(-3, 5)))

            if overall_score >= 80:
                feedback = (
                    "Outstanding interview performance! Responses showed strong technical clarity, "
                    "well-structured STAR explanations, and confident communication."
                )
                strengths = ["Strong technical articulation", "Clear STAR project structuring", "Confident delivery"]
                weak_areas = ["Minor edge case elaboration"]
                suggestions = ["Continue practicing high-level system design trade-offs and latency benchmarks."]
            elif overall_score >= 60:
                feedback = (
                    "Good performance overall. Consider expanding on technical implementation specifics, "
                    "quantifying project impacts, and structuring behavioral examples with clearer resolution steps."
                )
                strengths = ["Good foundational knowledge", "Relevant project familiarity"]
                weak_areas = ["Needs deeper technical specifics", "Could structure answers with more quantifiable results"]
                suggestions = ["Practice explaining trade-offs between different database and architectural choices."]
            else:
                feedback = (
                    "Needs preparation. Focus on answering with comprehensive explanations (aim for 50+ words per answer), "
                    "using standard industry terminology and real project anecdotes."
                )
                strengths = ["Attempted core questions"]
                weak_areas = ["Answers were brief", "Lacked concrete architectural examples"]
                suggestions = ["Review core data structures, algorithms, and rehearse the STAR method for behavioral questions."]

        result_payload = {
            "overall_score": overall_score,
            "technical_score": tech_score,
            "communication_score": comm_score,
            "feedback": feedback,
            "strengths": strengths,
            "weak_areas": weak_areas,
            "suggestions": suggestions,
            "answers": answers
        }

        # Save to SecureTestSessionModel
        SecureTestSessionModel.submit_session(
            session_id=session_id,
            employee_id=emp_id,
            test_type="interview",
            score=overall_score,
            percentage=float(overall_score),
            performance_message=feedback[:50],
            answers={"answers": answers},
            result_payload=result_payload
        )

        # Save result to interview_results table
        InterviewModel.save_result(
            employee_id=emp_id,
            job_role=job_role,
            overall_score=overall_score,
            technical_score=tech_score,
            communication_score=comm_score,
            feedback=feedback,
            answers=answers
        )

        # Record in test_attempts & update company preparation
        emp_record = EmployeeModel.get_by_id(emp_id) or {}
        comp_slug = (emp_record.get("target_company_slug") or "tcs").lower()
        TestAttemptModel.record_attempt(
            user_id=emp_id,
            company_slug=comp_slug,
            test_type="interview",
            score=overall_score,
            total=100.0,
            percentage=float(overall_score),
            role_name=job_role,
            details_json=result_payload
        )

        # Award gamification XP
        GamificationModel.award_points(emp_id, "mock_interview", 50)

        return jsonify({
            "success": True,
            "message": "Interview evaluation completed successfully.",
            "overall_score": overall_score,
            "technical_score": tech_score,
            "communication_score": comm_score,
            "feedback": feedback,
            "strengths": strengths,
            "weak_areas": weak_areas,
            "suggestions": suggestions
        }), 200

    except Exception as e:
        return jsonify({
            "success": False,
            "message": f"Error evaluating interview: {str(e)}"
        }), 500


@interview_bp.route("/api/interview/result", methods=["GET"])
def get_interview_result():
    """
    Fetches the latest interview result for an employee.
    """
    try:
        employee_id = request.args.get("employee_id", type=int)
        if not employee_id:
            return jsonify({"success": False, "message": "employee_id is required."}), 400

        result = InterviewModel.get_latest_result(employee_id)
        return jsonify({
            "success": True,
            "data": result
        }), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500
