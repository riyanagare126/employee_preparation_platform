"""
Catalog Builder Utilities.
Provides structured builder functions to assemble complete role-based catalogs
(Java Developer, Python Developer, Data Analyst) for any enterprise.
"""

from typing import Dict, List, Any

def create_aptitude_question(
    q_text: str,
    options: List[str],
    correct_answer: str,
    explanation: str,
    difficulty: str = "Medium",
    section: str = "Quantitative & Analytical"
) -> Dict[str, Any]:
    return {
        "question": q_text,
        "options": options,
        "correct_answer": correct_answer,
        "explanation": explanation,
        "difficulty": difficulty,
        "section": section
    }

def create_coding_problem(
    title: str,
    q_text: str,
    sample_input: str,
    sample_output: str,
    starter_java: str,
    starter_python: str,
    starter_analyst: str,
    explanation: str,
    difficulty: str = "Medium",
    topic: str = "Algorithms",
    time_comp: str = "O(N)",
    space_comp: str = "O(1)"
) -> Dict[str, Any]:
    return {
        "title": title,
        "question": q_text,
        "sample_input": sample_input,
        "sample_output": sample_output,
        "starter_code_java": starter_java,
        "starter_code_python": starter_python,
        "starter_code_analyst": starter_analyst,
        "explanation": explanation,
        "difficulty": difficulty,
        "topic": topic,
        "time_complexity": time_comp,
        "space_complexity": space_comp
    }

def create_technical_question(
    q_text: str,
    explanation: str,
    topic: str,
    difficulty: str = "Medium"
) -> Dict[str, Any]:
    return {
        "question": q_text,
        "explanation": explanation,
        "topic": topic,
        "difficulty": difficulty
    }

def create_ai_question(
    q_text: str,
    explanation: str,
    rubric: str,
    difficulty: str = "Medium"
) -> Dict[str, Any]:
    return {
        "question": q_text,
        "explanation": explanation,
        "rubric": rubric,
        "difficulty": difficulty
    }

def create_hr_question(
    q_text: str,
    explanation: str,
    dimension: str,
    difficulty: str = "Medium"
) -> Dict[str, Any]:
    return {
        "question": q_text,
        "explanation": explanation,
        "dimension": dimension,
        "difficulty": difficulty
    }
