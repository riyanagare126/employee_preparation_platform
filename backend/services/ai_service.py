"""
AI Service Module for AI Employee Preparation Platform.
Provides LLM integration with OpenAI / Gemini / Groq with an expert, 
production-grade algorithmic fallback engine ensuring 100% reliability.
"""
import os
import json
import re
from datetime import datetime, date, timedelta
from typing import Dict, Any, List, Optional


def generate_notice_period_plan(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates a day-by-day notice period preparation plan tailored to:
    - Target role
    - Experience in years
    - Notice period days
    - Last working date
    - Upcoming interview dates (optional, multiple)
    - Weak skill areas (DSA, SQL, System Design, HR/Behavioral, Aptitude)
    - Available daily study time (30 min / 1 hr / 2 hr)

    Attempts to call configured external LLM (OpenAI/Gemini/Groq),
    and falls back seamlessly to the expert deterministic planner if unconfigured or on error.
    """
    ai_api_key = (
        os.getenv("AI_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY") or
        os.getenv("GROQ_API_KEY")
    )

    if ai_api_key:
        try:
            llm_plan = _call_external_llm_for_notice_plan(inputs, ai_api_key)
            if llm_plan and "days" in llm_plan and len(llm_plan["days"]) > 0:
                return llm_plan
        except Exception as e:
            print(f"[AI Service] External LLM call failed, switching to expert fallback: {e}")

    # Seamless fallback engine
    return generate_fallback_notice_plan(inputs)


def _call_external_llm_for_notice_plan(inputs: Dict[str, Any], api_key: str) -> Optional[Dict[str, Any]]:
    """
    Optional external LLM API caller using standard urllib/requests to avoid heavy dependencies.
    """
    import urllib.request
    import urllib.error

    target_role = inputs.get("target_role", "Software Engineer")
    experience_years = inputs.get("experience_years", "2")
    notice_days = int(inputs.get("notice_period_days", 30))
    weak_areas = inputs.get("weak_areas", [])
    daily_time = inputs.get("daily_study_time", "1 hr")
    interview_dates = inputs.get("interview_dates", [])

    prompt = f"""
You are an expert technical career coach. Generate a day-by-day interview preparation plan for a candidate in their notice period.
Candidate Profile:
- Target Role: {target_role}
- Experience: {experience_years} years
- Notice Period: {notice_days} days
- Weak Areas to Prioritize: {', '.join(weak_areas) if weak_areas else 'General Tech'}
- Daily Study Time Available: {daily_time}
- Upcoming Interview Dates: {', '.join(interview_dates) if interview_dates else 'None yet'}

CRITICAL RULES:
1. Days immediately preceding any scheduled interview must be STRICTLY "Revision + Mock Only".
2. Prioritize weak areas across the core preparation days.
3. Every task must specify: day_number, title, description, category (Coding/System Design/Aptitude/Interview/Resume/Behavioral), estimated_minutes, link_url (e.g. preparation.html, aptitude.html, interview.html, resume.html, answer-builder.html, company-prep.html).
4. Return ONLY valid JSON with no markdown wrapping, schema:
{{
  "plan_summary": "string",
  "target_role": "{target_role}",
  "notice_period_days": {notice_days},
  "daily_study_time": "{daily_time}",
  "weak_areas": {json.dumps(weak_areas)},
  "days": [
    {{
      "day_number": 1,
      "date_label": "Day 1",
      "theme": "string",
      "is_interview_prep": false,
      "interview_alert": null,
      "tasks": [
        {{
          "task_key": "day1_task1",
          "title": "string",
          "description": "string",
          "category": "Coding",
          "estimated_minutes": 30,
          "link_url": "preparation.html",
          "link_text": "Open Coding"
        }}
      ]
    }}
  ]
}}
"""
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a specialized career prep planner that outputs strictly JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.5,
        "max_tokens": 2500
    }

    req = urllib.request.Request(openai_url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=12) as response:
        result = json.loads(response.read().decode("utf-8"))
        content = result["choices"][0]["message"]["content"].strip()
        # Clean markdown if enclosed in ```json ... ```
        if content.startswith("```"):
            content = re.sub(r"^```[a-zA-Z]*\n?", "", content)
            content = re.sub(r"\n?```$", "", content)
        return json.loads(content)


def generate_fallback_notice_plan(inputs: Dict[str, Any]) -> Dict[str, Any]:
    """
    Deterministic, high-quality preparation plan generator based on
    expert engineering interview standards.
    Features:
    - Accurate day-by-day progression spanning 1 to notice_period_days (up to 90)
    - Prioritizes candidate weak areas (DSA, SQL, System Design, HR/Behavioral, Aptitude)
    - Automatically schedules 'Revision + Mock Only' for the 2 days before any scheduled interview
    - Adjusts daily task count and estimated minutes according to daily study time (30 min / 1 hr / 2 hr)
    - Seamlessly links to existing platform pages
    """
    target_role = inputs.get("target_role") or "Software Engineer"
    experience_years = str(inputs.get("experience_years") or "2")
    notice_days = max(3, min(int(inputs.get("notice_period_days") or 30), 90))
    daily_time = inputs.get("daily_study_time") or "1 hr"
    last_working_date_str = inputs.get("last_working_date") or ""

    weak_areas = inputs.get("weak_areas") or []
    if isinstance(weak_areas, str):
        try:
            weak_areas = json.loads(weak_areas)
        except Exception:
            weak_areas = [w.strip() for w in weak_areas.split(",") if w.strip()]

    interview_dates_raw = inputs.get("interview_dates") or []
    if isinstance(interview_dates_raw, str):
        try:
            interview_dates_raw = json.loads(interview_dates_raw)
        except Exception:
            interview_dates_raw = [d.strip() for d in interview_dates_raw.split(",") if d.strip()]

    today = date.today()

    # Parse interview dates into date objects
    parsed_interview_dates = []
    for d_str in interview_dates_raw:
        if not d_str:
            continue
        try:
            # Handle YYYY-MM-DD
            clean_d = d_str.split()[0].strip()
            parsed_d = datetime.strptime(clean_d, "%Y-%m-%d").date()
            parsed_interview_dates.append(parsed_d)
        except Exception:
            pass

    # Determine daily workload scale
    if "30" in daily_time:
        tasks_per_day = 1
        default_mins = 25
    elif "2" in daily_time:
        tasks_per_day = 3
        default_mins = 40
    else:  # 1 hr default
        tasks_per_day = 2
        default_mins = 30

    # Knowledge catalogs for topics based on weak areas & general requirements
    curriculum = _build_curriculum_bank(target_role, weak_areas)

    days_plan = []
    weak_curriculum_cycle = 0
    general_curriculum_cycle = 0

    for day_num in range(1, notice_days + 1):
        day_date = today + timedelta(days=day_num - 1)
        day_date_str = day_date.strftime("%Y-%m-%d")

        # Check if this day is within 2 days before an interview OR on interview day
        is_interview_prep = False
        interview_alert_msg = None

        for intv_d in parsed_interview_dates:
            diff = (intv_d - day_date).days
            if diff == 0:
                is_interview_prep = True
                interview_alert_msg = f"🎯 INTERVIEW TODAY ({intv_d.strftime('%b %d')})! Pre-Interview Mindset & STAR Pitch"
                break
            elif diff == 1:
                is_interview_prep = True
                interview_alert_msg = f"⚠️ INTERVIEW TOMORROW ({intv_d.strftime('%b %d')})! Rapid Revision & Full AI Mock Simulator"
                break
            elif diff == 2:
                is_interview_prep = True
                interview_alert_msg = f"⚠️ 2 Days to Interview ({intv_d.strftime('%b %d')}): Core Concept Review & Behavioral STAR Polishing"
                break

        # Generate day's tasks
        day_tasks = []
        if is_interview_prep:
            theme = "Interview Milestone: Revision + Mock Only"
            # Specialized revision tasks
            if interview_alert_msg and "TODAY" in interview_alert_msg:
                day_tasks.append({
                    "task_key": f"day{day_num}_task1",
                    "title": "60-Second Elevator Pitch & STAR Opening",
                    "description": "Rehearse your Present-Past-Future introduction and core project impact statements.",
                    "category": "Behavioral",
                    "estimated_minutes": default_mins,
                    "link_url": "answer-builder.html",
                    "link_text": "Open 60s Pitch Builder"
                })
                if tasks_per_day >= 2:
                    day_tasks.append({
                        "task_key": f"day{day_num}_task2",
                        "title": "ATS Resume High-Yield Project Walkthrough",
                        "description": "Review the specific bullet points and metrics on your resume that recruiters will probe.",
                        "category": "Resume",
                        "estimated_minutes": default_mins,
                        "link_url": "resume.html",
                        "link_text": "Open Resume"
                    })
            elif interview_alert_msg and "TOMORROW" in interview_alert_msg:
                day_tasks.append({
                    "task_key": f"day{day_num}_task1",
                    "title": "Full-Length AI Mock Interview Simulation",
                    "description": f"Complete a simulated technical and situational interview tailored to {target_role}.",
                    "category": "Interview",
                    "estimated_minutes": default_mins + 15,
                    "link_url": "interview.html",
                    "link_text": "Start Mock Interview"
                })
                if tasks_per_day >= 2:
                    day_tasks.append({
                        "task_key": f"day{day_num}_task2",
                        "title": "Formula & Time Complexity Quick Revision",
                        "description": "Rapidly scan time/space bounds, SQL joins, and design trade-offs without coding from scratch.",
                        "category": "Technical",
                        "estimated_minutes": default_mins,
                        "link_url": "preparation.html",
                        "link_text": "Review Cheat Sheets"
                    })
            else:  # 2 days out
                day_tasks.append({
                    "task_key": f"day{day_num}_task1",
                    "title": "Target Company Pattern & Recruiter Focus Areas",
                    "description": "Examine the hiring round breakdown and frequent interview questions for your target enterprise.",
                    "category": "Company",
                    "estimated_minutes": default_mins,
                    "link_url": "company-prep.html",
                    "link_text": "Open Company Hub"
                })
                if tasks_per_day >= 2:
                    day_tasks.append({
                        "task_key": f"day{day_num}_task2",
                        "title": "AI Mock Interview Practice Session",
                        "description": "Practice verbal STAR responses under simulated timer constraints.",
                        "category": "Interview",
                        "estimated_minutes": default_mins,
                        "link_url": "interview.html",
                        "link_text": "Open AI Interview"
                    })
        else:
            # Regular day: Balance between weak areas and core fundamentals
            # Determine if this day prioritizes a weak area (60% weight if weak areas specified)
            focus_on_weak = bool(weak_areas) and (day_num % 3 != 0)

            if focus_on_weak and curriculum["weak_items"]:
                item = curriculum["weak_items"][weak_curriculum_cycle % len(curriculum["weak_items"])]
                weak_curriculum_cycle += 1
                theme = f"Weak Area Priority: {item['category']} — {item['topic']}"
                day_tasks.append({
                    "task_key": f"day{day_num}_task1",
                    "title": item["title"],
                    "description": item["description"],
                    "category": item["category"],
                    "estimated_minutes": default_mins,
                    "link_url": item["link_url"],
                    "link_text": item["link_text"]
                })
                # Secondary task
                if tasks_per_day >= 2:
                    sec_item = curriculum["weak_items"][weak_curriculum_cycle % len(curriculum["weak_items"])]
                    weak_curriculum_cycle += 1
                    day_tasks.append({
                        "task_key": f"day{day_num}_task2",
                        "title": sec_item["title"],
                        "description": sec_item["description"],
                        "category": sec_item["category"],
                        "estimated_minutes": default_mins,
                        "link_url": sec_item["link_url"],
                        "link_text": sec_item["link_text"]
                    })
                if tasks_per_day >= 3:
                    gen_item = curriculum["general_items"][general_curriculum_cycle % len(curriculum["general_items"])]
                    general_curriculum_cycle += 1
                    day_tasks.append({
                        "task_key": f"day{day_num}_task3",
                        "title": gen_item["title"],
                        "description": gen_item["description"],
                        "category": gen_item["category"],
                        "estimated_minutes": default_mins,
                        "link_url": gen_item["link_url"],
                        "link_text": gen_item["link_text"]
                    })
            else:
                gen_item = curriculum["general_items"][general_curriculum_cycle % len(curriculum["general_items"])]
                general_curriculum_cycle += 1
                theme = f"Core Mastery: {gen_item['category']} — {gen_item['topic']}"
                day_tasks.append({
                    "task_key": f"day{day_num}_task1",
                    "title": gen_item["title"],
                    "description": gen_item["description"],
                    "category": gen_item["category"],
                    "estimated_minutes": default_mins,
                    "link_url": gen_item["link_url"],
                    "link_text": gen_item["link_text"]
                })
                if tasks_per_day >= 2:
                    gen_item2 = curriculum["general_items"][general_curriculum_cycle % len(curriculum["general_items"])]
                    general_curriculum_cycle += 1
                    day_tasks.append({
                        "task_key": f"day{day_num}_task2",
                        "title": gen_item2["title"],
                        "description": gen_item2["description"],
                        "category": gen_item2["category"],
                        "estimated_minutes": default_mins,
                        "link_url": gen_item2["link_url"],
                        "link_text": gen_item2["link_text"]
                    })
                if tasks_per_day >= 3:
                    gen_item3 = curriculum["general_items"][general_curriculum_cycle % len(curriculum["general_items"])]
                    general_curriculum_cycle += 1
                    day_tasks.append({
                        "task_key": f"day{day_num}_task3",
                        "title": gen_item3["title"],
                        "description": gen_item3["description"],
                        "category": gen_item3["category"],
                        "estimated_minutes": default_mins,
                        "link_url": gen_item3["link_url"],
                        "link_text": gen_item3["link_text"]
                    })

        days_plan.append({
            "day_number": day_num,
            "date_str": day_date_str,
            "date_label": f"Day {day_num} ({day_date.strftime('%b %d')})",
            "theme": theme,
            "is_interview_prep": is_interview_prep,
            "interview_alert": interview_alert_msg,
            "tasks": day_tasks
        })

    summary_text = (
        f"Customized {notice_days}-Day Notice Period Countdown Plan for {target_role} ({experience_years} yrs exp). "
        f"Allocating daily {daily_time} with high-intensity focus on {', '.join(weak_areas) if weak_areas else 'Core Tech'} "
        f"and structured Revision + Mock intervals before upcoming interview rounds."
    )

    return {
        "plan_summary": summary_text,
        "target_role": target_role,
        "experience_years": experience_years,
        "notice_period_days": notice_days,
        "last_working_date": last_working_date_str,
        "daily_study_time": daily_time,
        "weak_areas": weak_areas,
        "interview_dates": [d.strftime("%Y-%m-%d") for d in parsed_interview_dates],
        "days": days_plan
    }


def _build_curriculum_bank(target_role: str, weak_areas: List[str]) -> Dict[str, List[Dict[str, Any]]]:
    """
    Builds pools of specialized preparation tasks for weak areas and general curriculum.
    """
    weak_items = []
    general_items = []

    # Map weak areas
    weak_set = {w.lower().strip() for w in weak_areas}

    # 1. DSA Tasks
    dsa_tasks = [
        {
            "category": "DSA / Coding",
            "topic": "Arrays & Sliding Window",
            "title": "Sliding Window & Substring Problems",
            "description": "Solve 2 Medium problems on Maximum Sum Subarray and Longest Substring Without Repeating Characters.",
            "link_url": "preparation.html",
            "link_text": "Practice in Code Editor"
        },
        {
            "category": "DSA / Coding",
            "topic": "Two Pointers & Binary Search",
            "title": "Two Pointers & Rotated Sorted Arrays",
            "description": "Implement binary search in a rotated sorted array and two-sum two-pointer variants.",
            "link_url": "preparation.html",
            "link_text": "Solve DSA Challenge"
        },
        {
            "category": "DSA / Coding",
            "topic": "Stack & Monotonic Deque",
            "title": "Valid Parentheses & Min Stack Architecture",
            "description": "Build a MinStack in O(1) time and evaluate balanced bracket expressions.",
            "link_url": "preparation.html",
            "link_text": "Solve Stack Challenge"
        },
        {
            "category": "DSA / Coding",
            "topic": "HashMaps & Frequency Counting",
            "title": "LRU Cache & HashMap Collision Handling",
            "description": "Explain internal HashMap bucket operations and implement an LRU cache with doubly linked list.",
            "link_url": "preparation.html",
            "link_text": "Implement LRU Cache"
        },
        {
            "category": "DSA / Coding",
            "topic": "Trees & Graph Traversals",
            "title": "Binary Tree Level-Order & DFS Depth",
            "description": "Traverse binary trees using BFS queue and recursive DFS. Calculate diameter and maximum path sum.",
            "link_url": "preparation.html",
            "link_text": "Practice Tree Traversal"
        }
    ]

    # 2. SQL Tasks
    sql_tasks = [
        {
            "category": "SQL / Database",
            "topic": "Complex Joins & Aggregations",
            "title": "Multi-Table INNER / LEFT JOIN & GROUP BY",
            "description": "Write queries calculating second-highest salary and department-wise active employee aggregates.",
            "link_url": "preparation.html",
            "link_text": "Practice SQL Queries"
        },
        {
            "category": "SQL / Database",
            "topic": "Window Functions",
            "title": "ROW_NUMBER(), RANK(), DENSE_RANK()",
            "description": "Solve top-N records per category using window functions and partition clauses.",
            "link_url": "preparation.html",
            "link_text": "Execute SQL Challenges"
        },
        {
            "category": "SQL / Database",
            "topic": "Indexing & Query Optimization",
            "title": "B-Tree Indexing & EXPLAIN Execution Plans",
            "description": "Analyze query performance, index selectivity, composite indexes, and table scans.",
            "link_url": "company-prep.html",
            "link_text": "Read Technical DB Guide"
        }
    ]

    # 3. System Design Tasks
    sys_tasks = [
        {
            "category": "System Design",
            "topic": "API Rate Limiting & Redis Caching",
            "title": "High-Throughput API Rate Limiter Design",
            "description": "Design token-bucket and sliding-window rate limiters with distributed Redis state.",
            "link_url": "company-prep.html",
            "link_text": "Open System Design Prep"
        },
        {
            "category": "System Design",
            "topic": "Microservices & Database Sharding",
            "title": "URL Shortener & Consistent Hashing",
            "description": "Architect a distributed URL shortening service with hash collisions, database sharding, and 301 vs 302 redirects.",
            "link_url": "company-prep.html",
            "link_text": "Explore Architecture Patterns"
        },
        {
            "category": "System Design",
            "topic": "Event-Driven Messaging & Kafka",
            "title": "Asynchronous Queue & Pub/Sub Architectures",
            "description": "Design decoupled processing for order notifications with at-least-once message delivery.",
            "link_url": "company-prep.html",
            "link_text": "Study Enterprise System Design"
        }
    ]

    # 4. HR / Behavioral Tasks
    hr_tasks = [
        {
            "category": "Behavioral / HR",
            "topic": "STAR Story Crafting",
            "title": "Conflict Resolution & Leadership Under Pressure",
            "description": "Draft a structured STAR story regarding a time you had a technical disagreement with a teammate or tight deadline.",
            "link_url": "answer-builder.html",
            "link_text": "Build STAR Story"
        },
        {
            "category": "Behavioral / HR",
            "topic": "Notice Period Justification",
            "title": "Why Are You Leaving & Career Switch Narrative",
            "description": "Frame your job switch positively, emphasizing growth, ownership, and target enterprise alignment.",
            "link_url": "answer-builder.html",
            "link_text": "Refine 60s Pitch"
        },
        {
            "category": "Behavioral / HR",
            "topic": "Questions for the Interviewer",
            "title": "High-Impact Questions to Ask the Hiring Team",
            "description": "Prepare 3 strategic questions about team engineering culture, deployment frequency, and AI tooling.",
            "link_url": "interview.html",
            "link_text": "Practice with AI Mock Coach"
        }
    ]

    # 5. Aptitude Tasks
    apt_tasks = [
        {
            "category": "Aptitude",
            "topic": "Quantitative Arithmetic",
            "title": "Speed Math, Profit & Loss, Percentages",
            "description": "Solve 15 quantitative aptitude questions under timer constraints to sharpen mental math.",
            "link_url": "aptitude.html",
            "link_text": "Take Aptitude Test"
        },
        {
            "category": "Aptitude",
            "topic": "Logical & Analytical Reasoning",
            "title": "Blood Relations, Coding-Decoding & Puzzles",
            "description": "Practice rapid deduction and syllogisms commonly found in initial screening rounds.",
            "link_url": "aptitude.html",
            "link_text": "Practice Reasoning Questions"
        }
    ]

    # Assign weak items based on candidate selections
    if any(k in weak_set for k in ["dsa", "coding", "algorithm"]):
        weak_items.extend(dsa_tasks)
    if any(k in weak_set for k in ["sql", "database", "rdbms"]):
        weak_items.extend(sql_tasks)
    if any(k in weak_set for k in ["system design", "system", "architecture", "design"]):
        weak_items.extend(sys_tasks)
    if any(k in weak_set for k in ["hr", "behavioral", "communication"]):
        weak_items.extend(hr_tasks)
    if any(k in weak_set for k in ["aptitude", "quant", "logical"]):
        weak_items.extend(apt_tasks)

    # General pool covers all dimensions
    general_items = dsa_tasks + sql_tasks + sys_tasks + [
        {
            "category": "Resume / ATS",
            "topic": "ATS Keyword Calibration",
            "title": "Resume Keyword Audit for Target Role",
            "description": f"Scan your resume against {target_role} expectations and optimize bullet points with measurable impact metrics.",
            "link_url": "resume.html",
            "link_text": "Optimize ATS Resume"
        },
        {
            "category": "AI Fluency",
            "topic": "2026 AI-Assisted Engineering",
            "title": "AI Pair Programming & Code Verification",
            "description": "Practice articulating how you leverage AI assistance while maintaining zero-trust test boundaries.",
            "link_url": "ai-fluency.html",
            "link_text": "Take AI Fluency Round"
        }
    ] + hr_tasks + apt_tasks

    # If no weak areas selected, use all items in weak_items too so cycling works seamlessly
    if not weak_items:
        weak_items = list(general_items)

    return {
        "weak_items": weak_items,
        "general_items": general_items
    }


def convert_achievement_to_star(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Converts a candidate's career achievement into a structured STAR
    (Situation, Task, Action, Result) narrative and maps 3-5 high-probability
    behavioral interview questions.

    Uses external LLM (OpenAI/Gemini/Groq) if configured, or falls back to
    deterministic domain heuristics.
    """
    ai_api_key = (
        os.getenv("AI_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY") or
        os.getenv("GROQ_API_KEY")
    )

    if ai_api_key:
        try:
            llm_result = _call_external_llm_for_star(data, ai_api_key)
            if (
                llm_result and
                llm_result.get("star_situation") and
                llm_result.get("star_action") and
                llm_result.get("star_result")
            ):
                return llm_result
        except Exception as e:
            print(f"[AI Service] External LLM call for STAR achievement failed: {e}")

    return generate_fallback_star_achievement(data)


def _call_external_llm_for_star(data: Dict[str, Any], api_key: str) -> Optional[Dict[str, Any]]:
    """
    Optional external LLM API caller using standard urllib.request.
    """
    import urllib.request
    import urllib.error

    title = data.get("title", "")
    raw_desc = data.get("raw_description", "")
    metrics = data.get("metrics_result", "")
    skills = data.get("skills_used", "")

    prompt = f"""
You are an executive interview coach specializing in behavioral interviews for top tech companies (FAANG, tier-1 enterprises).
Transform the following career achievement into an impactful STAR (Situation, Task, Action, Result) response suitable for behavioral interviews.
Then provide 3 to 5 common behavioral interview questions (e.g., conflict, leadership, failure, deadline pressure, technical ownership) that this story can answer.

Candidate's Input:
- Title: {title}
- What I Did (Raw Details): {raw_desc}
- Quantifiable Results / Impact: {metrics}
- Skills & Tools Used: {skills}

CRITICAL RULES:
1. Write in confident, polished first-person past tense ("I architected...", "I identified...").
2. Ensure the Situation clearly describes the technical or business context and stakes.
3. Ensure the Task specifies candidate's explicit responsibility and objectives.
4. Ensure the Action highlights decision-making, engineering steps, tools used ({skills}), and cross-functional collaboration.
5. Ensure the Result integrates the candidate's metrics ({metrics}) and highlights overall organizational value.
6. Provide 3-5 mapped behavioral interview questions with category and tag.
7. Return ONLY valid JSON with no markdown wrapping, schema:
{{
  "star_situation": "string",
  "star_task": "string",
  "star_action": "string",
  "star_result": "string",
  "mapped_questions": [
    {{
      "question": "string",
      "category": "Leadership / Execution / Conflict / Resilience / Optimization",
      "tag": "Leadership"
    }}
  ]
}}
"""
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an expert interview coach. Always respond in valid JSON format."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    req = urllib.request.Request(openai_url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            resp_data = json.loads(response.read().decode("utf-8"))
            content = resp_data["choices"][0]["message"]["content"].strip()
            if content.startswith("```"):
                content = re.sub(r"^```json\s*", "", content)
                content = re.sub(r"^```\s*", "", content)
                content = re.sub(r"```$", "", content).strip()
            parsed = json.loads(content)
            if "star_situation" in parsed and "star_action" in parsed:
                return parsed
    except Exception as err:
        print(f"[AI Service] OpenAI STAR API error: {err}")

    return None


def generate_fallback_star_achievement(data: Dict[str, Any]) -> Dict[str, Any]:
    """
    Expert heuristic fallback engine that parses user inputs and crafts a
    high-impact, executive STAR response with contextual behavioral questions.
    """
    title = (data.get("title") or "Technical Milestone").strip()
    raw_desc = (data.get("raw_description") or "").strip()
    metrics = (data.get("metrics_result") or "Achieved significant business improvements and high team acclaim").strip()
    skills = (data.get("skills_used") or "Modern Engineering Practices").strip()

    # Normalize description sentences
    sentences = [s.strip() for s in re.split(r"[.\n]+", raw_desc) if len(s.strip()) > 5]
    primary_sentence = sentences[0] if sentences else raw_desc
    secondary_sentence = ". ".join(sentences[1:]) if len(sentences) > 1 else ""

    # Situation
    situation = (
        f"In my previous role, our team faced a high-stakes challenge regarding {title.lower()}. "
        f"Specifically, {primary_sentence}. The existing technical setup and workflow created performance bottlenecks, "
        f"which threatened delivery timelines, system scalability, and key user experience SLAs."
    )

    # Task
    task = (
        f"My core objective was to take ownership of {title.lower()} and deliver an enterprise-grade solution utilizing {skills}. "
        f"I was accountable for architecting the strategy, breaking down technical requirements, mitigating deployment risks, "
        f"and establishing rigorous automated validation to ensure zero downtime."
    )

    # Action
    action_body = secondary_sentence if secondary_sentence else f"I conducted a systematic gap analysis, engineered modular components, and leveraged {skills} to eliminate inefficiencies"
    action = (
        f"To resolve this, I spearheaded a structured execution approach: First, {action_body}. "
        f"Second, I instituted best engineering practices, automated unit and regression checks, and conducted thorough code reviews. "
        f"Throughout the process, I maintained transparent alignment with cross-functional stakeholders, engineering leads, "
        f"and product managers to resolve impediments promptly and ensure flawless integration."
    )

    # Result
    result = (
        f"The initiative delivered outstanding measurable impact: {metrics}. "
        f"Beyond the quantifiable metrics, the project significantly reduced maintenance overhead, elevated operational reliability, "
        f"and established a standardized reference architecture adopted across subsequent engineering sprints."
    )

    # Contextual behavioral question matching
    combined_text = f"{title} {raw_desc} {metrics} {skills}".lower()
    candidate_questions: List[Dict[str, str]] = []

    # 1. Deadline & Pressure
    if any(k in combined_text for k in ["deadline", "pressure", "urgent", "timeline", "delay", "crunch", "fast", "sprint"]):
        candidate_questions.append({
            "question": "Tell me about a time you had to deliver a critical project under tight deadlines or high pressure.",
            "category": "Time & Deadline Management",
            "tag": "Deadline Pressure"
        })

    # 2. Conflict & Collaboration
    if any(k in combined_text for k in ["conflict", "disagree", "stakeholder", "team", "review", "negotiat", "alignment"]):
        candidate_questions.append({
            "question": "Describe a situation where you had a technical disagreement with teammates or stakeholders. How did you build consensus?",
            "category": "Conflict & Consensus",
            "tag": "Conflict Resolution"
        })

    # 3. Failure, Roadblocks & Resilience
    if any(k in combined_text for k in ["fail", "roadblock", "bug", "outage", "bottleneck", "issue", "break", "recovery", "incident"]):
        candidate_questions.append({
            "question": "Give an example of a time when a project encountered unexpected roadblocks or failures. How did you adapt and recover?",
            "category": "Resilience & Problem Solving",
            "tag": "Overcoming Failure"
        })

    # 4. Leadership & Ownership
    if any(k in combined_text for k in ["lead", "own", "mentor", "initiative", "spearhead", "drove", "architect", "propose"]):
        candidate_questions.append({
            "question": "Tell me about a time you took initiative or demonstrated technical leadership beyond your defined job scope.",
            "category": "Leadership & Ownership",
            "tag": "Leadership"
        })

    # 5. Performance & Optimization
    if any(k in combined_text for k in ["latency", "optimize", "speed", "scale", "cost", "performance", "memory", "throughput", "cache"]):
        candidate_questions.append({
            "question": "Describe a scenario where you identified a performance bottleneck or architectural inefficiency and successfully optimized it.",
            "category": "Optimization & Architecture",
            "tag": "Optimization"
        })

    # Standard fallback questions if pool has fewer than 4 questions
    standard_questions = [
        {
            "question": "Describe a complex technical problem you solved that delivered significant business impact.",
            "category": "Problem Solving & Execution",
            "tag": "Problem Solving"
        },
        {
            "question": "Tell me about a project where you had to learn and apply new technologies or tools under tight constraints.",
            "category": "Adaptability & Learning",
            "tag": "Continuous Learning"
        },
        {
            "question": "How do you ensure code quality, testability, and resilience when shipping critical features?",
            "category": "Engineering Discipline",
            "tag": "Execution Quality"
        },
        {
            "question": "Describe a situation where you had to explain complex technical concepts to non-technical stakeholders.",
            "category": "Communication & Collaboration",
            "tag": "Communication"
        }
    ]

    for sq in standard_questions:
        if len(candidate_questions) >= 4:
            break
        if not any(q["question"] == sq["question"] for q in candidate_questions):
            candidate_questions.append(sq)

    return {
        "star_situation": situation,
        "star_task": task,
        "star_action": action,
        "star_result": result,
        "mapped_questions": candidate_questions[:5]
    }


def convert_honest_to_professional(*args, **kwargs) -> Dict[str, Any]:
    """
    Transforms a candidate's honest, high-risk reason for leaving a job or
    having an employment gap (low pay, bad manager, burnout, layoffs, career break)
    into a polished, interview-safe, truthful, and forward-looking professional answer.
    Supports either a dictionary or positional arguments (question_type, raw_answer, target_role, target_company).

    Outputs:
    - professional_answer: 4-6 sentences, confident and truthful
    - short_answer: 30-second version (~40-65 words)
    - red_flags: list of risky words/phrases found with safer alternatives
    - follow_up_questions: 2 likely interviewer follow-up questions
    """
    if len(args) == 1 and isinstance(args[0], dict):
        data = dict(args[0])
    elif len(args) >= 1 and isinstance(args[0], str):
        data = {
            "question_type": args[0],
            "raw_answer": args[1] if len(args) > 1 else kwargs.get("raw_answer", ""),
            "target_role": args[2] if len(args) > 2 else kwargs.get("target_role", ""),
            "target_company": args[3] if len(args) > 3 else kwargs.get("target_company", "")
        }
    else:
        data = dict(kwargs)
    data.update(kwargs)

    ai_api_key = (
        os.getenv("AI_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY") or
        os.getenv("GROQ_API_KEY")
    )

    if ai_api_key:
        try:
            llm_result = _call_external_llm_for_honest_conversion(data, ai_api_key)
            if (
                llm_result and
                llm_result.get("professional_answer") and
                llm_result.get("short_answer") and
                isinstance(llm_result.get("red_flags"), list) and
                isinstance(llm_result.get("follow_up_questions"), list)
            ):
                return llm_result
        except Exception as e:
            print(f"[AI Service] External LLM call for honest conversion failed: {e}")

    return generate_fallback_converted_answer(data)


def _call_external_llm_for_honest_conversion(data: Dict[str, Any], api_key: str) -> Optional[Dict[str, Any]]:
    """
    Calls LLM for Honest-to-Professional answer conversion with strict truthfulness constraint.
    """
    import urllib.request
    import urllib.error

    q_type = str(data.get("question_type") or "Why are you leaving your current job?")
    raw_answer = str(data.get("raw_answer") or "")

    prompt = (
        "You are an executive career transition coach. An employee is preparing to answer a difficult interview question.\n"
        "They have provided their completely raw, honest reason (which may include risky reasons like low pay, toxic manager, burnout, company layoffs, or career gaps).\n\n"
        "Candidate Input:\n"
        "- Question Scenario: " + q_type + "\n"
        "- Raw Honest Reason: " + raw_answer + "\n\n"
        "CRITICAL RULES:\n"
        "1. DO NOT ENCOURAGE LYING. The rewritten answers MUST stay completely truthful to the core reality while remaining positive, diplomatic, and forward-looking.\n"
        "2. Produce:\n"
        "   (a) professional_answer: A polished, confident 4-6 sentence answer suitable for senior recruiter interviews.\n"
        "   (b) short_answer: A punchy 30-second version (approx. 40-65 words).\n"
        "   (c) red_flags: An array of objects highlighting specific risky words/phrases found in the raw text with why they sound risky and a safer alternative phrasing.\n"
        "   (d) follow_up_questions: An array of 2 realistic follow-up questions the interviewer may probe with.\n"
        "3. Return ONLY valid JSON with no markdown wrapping, schema:\n"
        '{\n'
        '  "professional_answer": "string (4-6 sentences)",\n'
        '  "short_answer": "string (~30s)",\n'
        '  "red_flags": [\n'
        '    {\n'
        '      "flag": "string (the risky word/phrase)",\n'
        '      "risk": "string (why it sounds risky to recruiters)",\n'
        '      "alternative": "string (constructive professional alternative)"\n'
        '    }\n'
        '  ],\n'
        '  "follow_up_questions": [\n'
        '    "string (Follow-up question 1)",\n'
        '    "string (Follow-up question 2)"\n'
        '  ]\n'
        '}'
    )
    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are an executive career coach. Return ONLY valid JSON."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    req = urllib.request.Request(openai_url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    try:
        with urllib.request.urlopen(req, timeout=12) as response:
            resp_data = json.loads(response.read().decode("utf-8"))
            content = resp_data["choices"][0]["message"]["content"].strip()
            if content.startswith("```"):
                content = re.sub(r"^```json\s*", "", content)
                content = re.sub(r"^```\s*", "", content)
                content = re.sub(r"```$", "", content).strip()
            parsed = json.loads(content)
            if "professional_answer" in parsed and "short_answer" in parsed:
                return parsed
    except Exception as err:
        print(f"[AI Service] OpenAI honest conversion error: {err}")

    return None


def generate_fallback_converted_answer(*args, **kwargs) -> Dict[str, Any]:
    """
    Expert heuristic fallback engine that parses risky raw honesty and converts it
    into a truthful, positive, forward-looking 4-6 sentence answer, a 30s version,
    red-flag phrase detections with alternatives, and 2 interviewer follow-up questions.
    Supports dictionary or positional arguments (question_type, raw_answer, target_role, target_company).
    """
    if len(args) == 1 and isinstance(args[0], dict):
        data = dict(args[0])
    elif len(args) >= 1 and isinstance(args[0], str):
        data = {
            "question_type": args[0],
            "raw_answer": args[1] if len(args) > 1 else kwargs.get("raw_answer", ""),
            "target_role": args[2] if len(args) > 2 else kwargs.get("target_role", ""),
            "target_company": args[3] if len(args) > 3 else kwargs.get("target_company", "")
        }
    else:
        data = dict(kwargs)
    data.update(kwargs)

    q_type = (data.get("question_type") or "Why are you leaving your current job?").strip()
    raw_answer = (data.get("raw_answer") or "").strip()
    raw_lower = raw_answer.lower()

    # Red-Flag Analysis Engine
    detected_red_flags: List[Dict[str, str]] = []

    red_flag_patterns = [
        {
            "terms": ["low salary", "underpaid", "money", "compensation", "hike", "raise", "cheap", "peanuts", "pay"],
            "flag": "Direct mention of low salary / lack of raise",
            "risk": "Can make you appear purely transactional or unmotivated by the technical craft.",
            "alternative": "Seeking fair market-aligned compensation that matches my expanded technical responsibilities and proven delivery impact."
        },
        {
            "terms": ["toxic", "bad manager", "boss", "micromanag", "horrible", "awful", "terrible", "abuse", "hate", "fight", "jerk"],
            "flag": "Criticizing former manager, leadership, or team culture",
            "risk": "Recruiters worry about interpersonal conflict, difficulty taking feedback, or high drama.",
            "alternative": "Looking for an engineering culture founded on autonomy, trust, transparent leadership, and collaborative code reviews."
        },
        {
            "terms": ["burnout", "overwork", "exhausted", "too much work", "60 hours", "weekend", "tired", "stressed"],
            "flag": "Complaining of burnout or long hours",
            "risk": "Interviewers might misinterpret this as low stamina, inability to handle enterprise deadlines, or poor work boundaries.",
            "alternative": "Targeting an environment with sustainable engineering velocity, realistic capacity planning, and deliberate sprint cadences."
        },
        {
            "terms": ["bored", "stagnant", "no growth", "repetitive", "monotonous", "doing nothing", "bench", "waste of time"],
            "flag": "Stating you are bored or doing nothing",
            "risk": "Can sound passive, implying you wait to be handed tasks rather than creating value autonomously.",
            "alternative": "Proactively seeking steeper technical learning curves, larger system ownership, and complex production architectures."
        },
        {
            "terms": ["fired", "terminated", "kicked out", "let go"],
            "flag": "Blunt language around termination",
            "risk": "Triggers immediate defensiveness or suspicion regarding conduct or performance.",
            "alternative": "Mutually agreed to part ways after determining an organizational direction and skillset mismatch."
        },
        {
            "terms": ["layoff", "laid off", "downsized", "downsizing", "cost cutting", "restructur"],
            "flag": "Ambiguous layoff explanation",
            "risk": "If not explained clearly as an organizational macro-decision, panels may wonder if it was performance-based.",
            "alternative": "Part of an organizational macroeconomic restructuring that strategically phased out our entire business vertical."
        },
        {
            "terms": ["gap", "break", "family", "health", "personal", "care", "sick", "leave"],
            "flag": "Unclear employment gap or personal time",
            "risk": "Unstructured explanations leave room for speculation about commitment, retention, or rusty skills.",
            "alternative": "Took an intentional sabbatical to fulfill personal commitments while actively maintaining modern software engineering fluency."
        },
        {
            "terms": ["jump", "switch", "hopping", "short stint", "quit"],
            "flag": "Frequent transitions or short tenures",
            "risk": "Raises flight risk concerns about whether you will leave after 6 to 12 months.",
            "alternative": "Prioritizing long-term organizational roots to compound my technical impact over multiple years in an established team."
        }
    ]

    for p in red_flag_patterns:
        if any(t in raw_lower for t in p["terms"]):
            detected_red_flags.append({
                "flag": p["flag"],
                "risk": p["risk"],
                "alternative": p["alternative"]
            })

    # Default fallback red-flag if candidate wrote a very short or safe text
    if not detected_red_flags:
        detected_red_flags.append({
            "flag": "Informal / unstructured phrasing",
            "risk": "Casual delivery without clear framing can weaken your executive presence.",
            "alternative": "Structure your explanation around the Present-Past-Future framework to keep it confident and succinct."
        })

    # Scenario-Based Transformation
    q_norm = q_type.lower()

    if "gap" in q_norm or "break" in q_norm:
        professional_answer = (
            "Following my previous role, I took an intentional, planned career sabbatical to fulfill important personal and family commitments. "
            "Throughout this period, I made it a daily priority to maintain and elevate my technical engineering fluency through hands-on project development, "
            "deep algorithmic practice, and mastering modern cloud frameworks. "
            "This dedicated interval provided me with valuable perspective and allowed me to recalibrate my long-term career trajectory with complete clarity. "
            "Today, those commitments are fully resolved, and I am completely energized, technically sharp, and eager to commit my full energy to high-impact production engineering."
        )
        short_answer = (
            "I took an intentional sabbatical to resolve personal priorities while actively keeping my technical skills sharp through hands-on cloud projects and system design practice. "
            "I am now fully refreshed, technically ready, and enthusiastic to bring my undivided focus to your engineering team."
        )
        follow_ups = [
            "What specific technical projects or modern engineering concepts did you explore most deeply during your sabbatical?",
            "How will you approach your first 30 days to ensure a smooth, high-velocity ramp-up back into daily production sprints?"
        ]

    elif "laid off" in q_norm or "layoff" in q_norm:
        professional_answer = (
            "Earlier this year, my previous organization conducted a company-wide macroeconomic restructuring, which impacted several business divisions including my engineering unit. "
            "This was strictly a top-level strategic reorganization driven by shifting market conditions rather than individual performance or technical delivery. "
            "Throughout my tenure there, I consistently met our sprint commitments, maintained high code quality benchmarks, and collaborated closely with cross-functional partners. "
            "While departing from talented teammates was difficult, the experience highlighted my adaptability, resilience, and composure under sudden organizational changes. "
            "I am using this transition as a deliberate opportunity to join an established enterprise with strong product-market fit where my technical contributions can drive durable value."
        )
        short_answer = (
            "My role was impacted by a broad strategic restructuring across our department due to shifting corporate priorities. "
            "I maintained strong delivery records and positive relationships throughout, and I’m now focused on applying my engineering skills to your core product mission."
        )
        follow_ups = [
            "What engineering achievement or system from that previous position are you most proud of carrying forward?",
            "If we speak with your previous engineering manager or colleagues, what would they highlight as your greatest technical strength?"
        ]

    elif "changes" in q_norm or "hopping" in q_norm:
        professional_answer = (
            "In the earlier phase of my career journey, each transition was driven by a deliberate ambition to gain accelerated hands-on exposure across diverse technical stacks, system scales, and engineering cultures. "
            "These experiences rapidly strengthened my agility—enabling me to jump into unfamiliar codebases, debug complex production issues, and deliver reliable features with fast turnaround times. "
            "Having built this versatile foundation, my unequivocal priority for my next chapter is long-term stability and deep organizational roots. "
            "I am specifically looking for an established engineering culture where I can stay for multiple years, take end-to-end ownership of core systems, and mentor newer teammates as the product evolves. "
            "This role represents the exact environment where I want to anchor my career and build lasting technical and business impact."
        )
        short_answer = (
            "My earlier transitions gave me rapid cross-stack versatility and strong adaptability across diverse codebases. "
            "Having proven my delivery agility, my clear priority now is long-term stability—joining an engineering team where I can anchor my career and compound value over multiple years."
        )
        follow_ups = [
            "What specific factors in a company culture and team structure are most essential for you to ensure you stay for 3+ years?",
            "How do you build deep domain expertise and earn the trust of senior engineering peers quickly when entering a new team?"
        ]

    else:
        # Default: "Why are you leaving your current job?"
        # Tailor based on detected sentiments
        has_pay = any("salary" in r["flag"].lower() for r in detected_red_flags)
        has_manager = any("manager" in r["flag"].lower() for r in detected_red_flags)

        if has_manager:
            theme_focus = "collaborative leadership, higher engineering autonomy, and transparent technical decision-making"
        elif has_pay:
            theme_focus = "greater architectural scope, steeper technical challenges, and compensation calibrated to senior delivery impact"
        else:
            theme_focus = "deeper architectural ownership, larger production scale, and modern engineering practices"

        professional_answer = (
            "In my current role, I have had the privilege of developing a solid technical foundation, collaborating with great peers, and delivering dependable production features. "
            "However, over the past year, my professional capabilities have matured, and I have reached a ceiling in terms of technical scope and architectural ownership within the existing team structure. "
            f"I am actively seeking an environment with {theme_focus} where I can tackle complex distributed problems and see the direct business impact of my engineering decisions. "
            "Your organization’s emphasis on high-availability systems and forward-thinking technical culture represents the exact standard of excellence I want to align myself with. "
            "I am eager to channel my dedication and delivery discipline into helping your team achieve its next engineering milestones."
        )
        short_answer = (
            "I’ve built a strong technical foundation in my current role, but my scope has plateaued. "
            "I’m looking for an engineering culture with greater architectural scale and higher technical ownership where I can contribute to mission-critical systems and build a long-term career."
        )
        follow_ups = [
            "What specific technical challenges or architectural scope are you not getting in your current role that you expect here?",
            "How did you approach discussing career progression or scope expansion with your current leadership before deciding to explore external opportunities?"
        ]

    return {
        "professional_answer": professional_answer,
        "short_answer": short_answer,
        "red_flags": detected_red_flags[:4],
        "follow_up_questions": follow_ups[:2]
    }


def generate_simple_notice_plan(
    target_role: str,
    experience: str,
    notice_days: int,
    weak_areas: Any
) -> str:
    """
    Generates a simple, comprehensive day-wise or week-wise preparation plan
    specifically fitting the notice period and heavily focusing on weak areas.
    Uses external LLM (Gemini / OpenAI / Groq) if available, with an expert fallback
    ensuring 100% reliability and zero crash risk.
    """
    if isinstance(weak_areas, str):
        if weak_areas.startswith("[") and weak_areas.endswith("]"):
            try:
                weak_list = json.loads(weak_areas)
            except Exception:
                weak_list = [w.strip() for w in weak_areas.replace("[", "").replace("]", "").replace("'", "").replace('"', '').split(",") if w.strip()]
        else:
            weak_list = [w.strip() for w in weak_areas.split(",") if w.strip()]
    elif isinstance(weak_areas, list):
        weak_list = [str(w).strip() for w in weak_areas if str(w).strip()]
    else:
        weak_list = []

    weak_str = ", ".join(weak_list) if weak_list else "General Technical & Core Concepts"

    ai_api_key = (
        os.getenv("AI_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY") or
        os.getenv("GROQ_API_KEY")
    )

    if ai_api_key:
        try:
            llm_text = _call_llm_for_simple_plan(target_role, experience, notice_days, weak_str, ai_api_key)
            if llm_text and len(llm_text.strip()) > 50:
                return llm_text.strip()
        except Exception as e:
            print(f"[AI Service] External LLM call for notice plan failed, using fallback: {e}")

    # Seamless fallback planner
    return _generate_fallback_simple_notice_plan(target_role, experience, notice_days, weak_list)


def _call_llm_for_simple_plan(target_role: str, experience: str, notice_days: int, weak_str: str, api_key: str) -> Optional[str]:
    """Calls OpenAI/compatible API to generate a notice period plan."""
    import urllib.request
    import urllib.error

    structure_hint = "day-wise breakdown (e.g. Day 1, Day 2...)" if notice_days <= 14 else "week-wise breakdown (e.g. Week 1, Week 2...)"

    prompt = f"""You are an elite career coach and tech interview expert.
Generate a structured, motivating, and highly actionable {structure_hint} interview preparation plan for an employee currently serving their notice period.

Candidate Profile:
- Target Role: {target_role}
- Experience: {experience} years
- Notice Period: {notice_days} days
- Critical Weak Areas to Prioritize: {weak_str}

Guidelines:
1. Provide a clear {structure_hint} structure that directly fits {notice_days} days.
2. Heavily focus extra time and practice on their weak areas: {weak_str}.
3. Include specific daily/weekly milestones, practice topics, and mock interview checkpoints.
4. Keep the output beautifully formatted with Markdown headers (### Week 1 or ### Day 1), bullet points, and practical daily actionable tips.
5. Add a short section on managing handover/KT at the current job while studying efficiently.
"""

    openai_url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "system", "content": "You are a professional tech career strategist. Format your responses in clean GitHub markdown."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.6,
        "max_tokens": 1800
    }

    req = urllib.request.Request(openai_url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
    with urllib.request.urlopen(req, timeout=12) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result["choices"][0]["message"]["content"].strip()


def _generate_fallback_simple_notice_plan(target_role: str, experience: str, notice_days: int, weak_list: List[str]) -> str:
    """Deterministic, high-value fallback plan tailored to candidate weak areas and notice period."""
    weak_str = ", ".join(weak_list) if weak_list else "Core Fundamentals"
    is_dsa = any("dsa" in w.lower() or "algo" in w.lower() for w in weak_list)
    is_sql = any("sql" in w.lower() or "data" in w.lower() for w in weak_list)
    is_sys = any("system" in w.lower() or "design" in w.lower() or "arch" in w.lower() for w in weak_list)
    is_hr = any("hr" in w.lower() or "behav" in w.lower() for w in weak_list)
    is_apt = any("apt" in w.lower() or "math" in w.lower() for w in weak_list)

    lines = []
    lines.append(f"## 🎯 {notice_days}-Day Notice Period Preparation Plan for {target_role}")
    lines.append(f"**Experience Level:** {experience} • **Notice Period:** {notice_days} Days • **Priority Weak Areas:** {weak_str}\n")
    lines.append("### 📌 Executive Strategy")
    lines.append(f"- **Primary Focus:** Allocate 60% of daily prep time to targeted weak areas ({weak_str}) during the initial half.")
    lines.append("- **KT & Workload Balance:** Dedicate mornings or evenings (1.5 - 2 hrs) to undisturbed interview prep. Keep workplace knowledge transfer documented early.")
    lines.append("- **Interview Readiness:** Shift to 100% revision, company question patterns, and mock interviews during the final 20% of your notice period.\n")

    if notice_days <= 14:
        # Day-wise breakdown for short notice
        lines.append("### 🗓️ Day-by-Day Sprint Schedule\n")
        lines.append("#### **Day 1 - 3: Weak Area Foundation Sprint**")
        if is_dsa:
            lines.append("- **DSA Focus:** Revisit Arrays, Strings, Hash Maps, and Two Pointers. Solve 4-6 curated LeetCode Mediums.")
        if is_sql:
            lines.append("- **SQL Focus:** Practice Complex Joins, Window Functions (`ROW_NUMBER`, `DENSE_RANK`), and GROUP BY aggregations.")
        if is_sys:
            lines.append("- **System Design:** Review REST vs gRPC, Microservices architecture, Caching (Redis), and SQL vs NoSQL trade-offs.")
        if is_apt:
            lines.append("- **Aptitude:** Practice 20 speed math questions: Ratios, Percentages, and Time & Work fundamentals.")
        if is_hr:
            lines.append("- **Behavioral:** Draft 3 STAR stories: Conflict resolution, technical failure, and cross-team leadership.")
        lines.append("- **Deliverable:** Master 5 core concepts and fix initial gaps.\n")

        lines.append("#### **Day 4 - 7: Intermediate Drills & Problem Solving**")
        lines.append(f"- **Core Tech ({target_role}):** Deep-dive into language-specific internals (e.g., concurrency, event loops, memory management, indexes).")
        if is_dsa:
            lines.append("- **DSA:** Trees, Binary Search, and Graph BFS/DFS traversal patterns.")
        if is_sys:
            lines.append("- **System Design:** Design a URL Shortener or Rate Limiter. Focus on scalability, latency, and database schema.")
        lines.append("- **Daily Mock:** Take 1 timed 45-minute technical mock test under real interview conditions.\n")

        lines.append("#### **Day 8 - 11: STAR Behavioral & Company Round Focus**")
        lines.append("- **60-Second Pitch:** Perfect your 'Tell me about yourself' pitch using Present-Past-Future format.")
        lines.append("- **Resume Walkthrough:** Ensure you can explain every metric, architectural choice, and challenge on your resume.")
        lines.append("- **Live Coding Practice:** Practice coding without an IDE autocomplete to simulate interview environments.\n")

        lines.append("#### **Day 12 - 14: Rapid Revision & Final Mock Simulation**")
        lines.append("- **No New Topics:** Strictly revise previously solved problems, cheat sheets, and architectural diagrams.")
        lines.append("- **Full AI Simulator:** Run full-length AI behavioral and technical interview rounds on the platform.")
        lines.append("- **Mental Readiness:** Confirm tech stack setup, webcam, audio, and review top questions for your scheduled interviews.\n")
    else:
        # Week-wise breakdown for longer notice (15 - 90 days)
        weeks = max(3, min(notice_days // 7, 8))
        lines.append("### 🗓️ Week-by-Week Progressive Schedule\n")

        lines.append("#### **Week 1: Weak Area Immersion & Core Foundation**")
        lines.append(f"- **Target Weak Areas ({weak_str}):** Dedicate 90 minutes daily exclusively to your identified weak subjects.")
        if is_dsa:
            lines.append("  - DSA: Master Arrays, Two Pointers, Sliding Window, and Hash Tables (10 Medium problems).")
        if is_sql:
            lines.append("  - SQL: Master Subqueries, CTEs (Common Table Expressions), Window Functions, and Query Indexing.")
        if is_sys:
            lines.append("  - System Design: Understand Client-Server bottlenecks, Load Balancers, Horizontal vs Vertical scaling.")
        if is_apt:
            lines.append("  - Aptitude: Daily 25-minute drills on Quantitative Aptitude & Data Interpretation.")
        lines.append("- **Resume Polish:** Update your resume with quantifiable metrics and STAR bullet points.\n")

        lines.append("#### **Week 2: Deep Technical & Role-Specific Mastery**")
        lines.append(f"- **Target Role ({target_role}):** Deepen architectural patterns, API design, database transactions (ACID), and concurrency.")
        if is_dsa:
            lines.append("  - DSA: Binary Trees, Heaps, and Dynamic Programming basics.")
        if is_sys:
            lines.append("  - System Design: Design a Notification System, E-commerce Checkout, or Scalable Feed.")
        lines.append("- **Milestone Test:** Take a comprehensive platform assessment to gauge score improvement in weak areas.\n")

        lines.append("#### **Week 3: Behavioral Polishing & Target Company Question Banks**")
        lines.append("- **Behavioral Framework (STAR):** Write structured answers for 6 key behavioral questions (leadership, disagreement, deadline crunch, innovation).")
        lines.append("- **Company Prep Hub:** Solve past interview questions for your top target enterprises (TCS, Infosys, Microsoft, Amazon, etc.).")
        lines.append("- **Mock Interviews:** Conduct at least 2 full AI voice/chat mock interview rounds.\n")

        lines.append(f"#### **Week 4 to Day {notice_days}: High-Velocity Revision & Mock Simulator**")
        lines.append("- **Timed Coding & System Walkthroughs:** Practice explaining code out loud while writing it.")
        lines.append("- **Error Notebook Review:** Re-solve every question you struggled with in previous weeks.")
        lines.append("- **Offer & Negotiation Preparation:** Research market compensation bands for your experience level.")
        lines.append("- **Final Readiness Check:** Run platform AI Fluency and Readiness Analyzer before live company rounds.\n")

    lines.append("### 💡 Notice Period Productivity Checklist")
    lines.append("1. **Timeboxing:** Study in two focused 45-minute blocks (morning before work, evening after work).")
    lines.append("2. **Knowledge Transfer Control:** Wrap up company KT sessions before 4 PM so your evenings stay energized for prep.")
    lines.append("3. **Active Interview Pipeline:** Start applying and taking recruiter screening calls from the halfway mark of your notice period.")

    return "\n".join(lines)


# =========================================================================
# DYNAMIC COMPANY INTERVIEW QUESTION GENERATOR
# =========================================================================

def generate_company_questions(
    company: str,
    experience_level: str,
    role: str = "",
    question_type: str = "",
    count: int = 5,
    existing_questions: Optional[List[str]] = None
) -> List[Dict[str, Any]]:
    """
    Generates company-specific and level-appropriate interview questions using AI.
    Strictly prevents duplicates against existing questions.
    Returns an empty list on failure or missing API key without raising an exception.
    """
    ai_api_key = (
        os.getenv("AI_API_KEY") or
        os.getenv("OPENAI_API_KEY") or
        os.getenv("GEMINI_API_KEY") or
        os.getenv("GROQ_API_KEY")
    )

    if not ai_api_key:
        return []

    try:
        results = _call_external_llm_for_company_questions(
            company=company,
            experience_level=experience_level,
            role=role,
            question_type=question_type,
            count=count,
            existing_questions=existing_questions or [],
            api_key=ai_api_key
        )
        if isinstance(results, list):
            cleaned = []
            for item in results:
                if isinstance(item, dict) and item.get("question_text"):
                    cleaned.append({
                        "question_text": str(item["question_text"]).strip(),
                        "category": str(item.get("category", "Technical")).strip(),
                        "difficulty": str(item.get("difficulty", "medium")).strip().lower(),
                        "question_type": str(item.get("question_type", question_type or "technical_depth")).strip().lower(),
                        "sample_answer": str(item.get("sample_answer", "")).strip() or None
                    })
            return cleaned
        return []
    except Exception as e:
        print(f"[AI Service] Error in generate_company_questions: {e}")
        return []


def _call_external_llm_for_company_questions(
    company: str,
    experience_level: str,
    role: str,
    question_type: str,
    count: int,
    existing_questions: List[str],
    api_key: str
) -> Optional[List[Dict[str, Any]]]:
    """
    Calls LLM API with strict prompt instructions and JSON validation.
    """
    import urllib.request
    import urllib.error

    existing_sample = "\n- ".join(existing_questions[:25]) if existing_questions else "None"

    prompt = f"""Generate questions strictly matching the given experience level and company style. No duplicates of the given existing questions. Return strictly a JSON list.

Target Company: {company}
Experience Level: {experience_level}
Target Role: {role or 'Software Engineer'}
Question Type Focus: {question_type or 'mix of technical, behavioral, and scenario'}
Desired Count: {count}

Existing Questions (DO NOT duplicate any of these concepts or wording):
- {existing_sample}

Rules for Company Style & Level:
- Fresher (0-1 year): core fundamentals, basic CS concepts, aptitude/logic, project walkthrough, basic HR/relocation. No lead-level architecture.
- Junior (1-3 years): hands-on coding, debugging, real project responsibilities, tools, deadlines, why switching.
- Mid (3-5 years): architectural decisions, API design, performance optimization, tricky bugs, cross-functional collaboration.
- Senior (5-8 years): system design, production incidents, scaling tradeoffs, cost optimization, mentoring juniors.
- Lead (8+ years): enterprise architecture, high availability, tech roadmap, stakeholder leadership, conflict resolution, hiring.
- Company Style:
  * TCS: NQT/Ninja/Digital patterns, client delivery, project lifecycle.
  * Infosys: InfyTQ/Power Programmer style, software engineering process.
  * Wipro: NLTH pattern, technical + HR situational.
  * Accenture/Cognizant/Capgemini/HCL/Tech Mahindra: Enterprise delivery, client scenarios, modern tech stack.
  * Amazon: STAR behavioral aligned with Amazon Leadership Principles.
  * Google/Microsoft: Algorithmic problem solving, system design, technical ownership.

Format your output STRICTLY as a JSON list of objects:
[
  {{
    "question_text": "string",
    "category": "Technical",
    "difficulty": "medium",
    "question_type": "technical_depth",
    "sample_answer": "string"
  }}
]
"""
    # Check if Groq or OpenAI or Gemini
    is_groq = api_key.startswith("gsk_")
    url = "https://api.groq.com/openai/v1/chat/completions" if is_groq else "https://api.openai.com/v1/chat/completions"
    model = "llama-3.3-70b-versatile" if is_groq else "gpt-3.5-turbo"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "You are a technical interview panelist. Return ONLY a valid JSON array of question objects without markdown wrapping."
            },
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.4
    }

    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=headers,
        method="POST"
    )

    with urllib.request.urlopen(req, timeout=12) as response:
        res_data = json.loads(response.read().decode("utf-8"))
        content = res_data["choices"][0]["message"]["content"]
        
        # Clean any markdown code blocks
        clean_json = content.strip()
        if clean_json.startswith("```"):
            clean_json = re.sub(r"^```[a-zA-Z]*\n?", "", clean_json)
            clean_json = re.sub(r"\n?```$", "", clean_json)
        
        return json.loads(clean_json.strip())




