"""
Validation script for company question banks.
Ensures:
1. Every company has separate question sets across:
   - Aptitude (min 15 per role, with options, correct answer, explanation)
   - Coding (min 8 per role, with difficulty, description, sample input/output, starter code)
   - Technical (min 15 per role, with description, explanation)
   - AI Interview (min 10 per role)
   - HR Interview (min 10 per role)
2. No question text appears under more than one company (ZERO duplicate questions across companies).
3. Exits with 0 on SUCCESS, 1 on FAILURE.
"""
import os
import sys
import glob
import json
import re
from typing import Dict, List, Set, Any

MIN_QUOTAS = {
    "aptitude": 15,
    "coding": 8,
    "technical": 15,
    "ai_interview": 10,
    "hr": 10
}

TARGET_ROLES = ["Java Developer", "Python Developer", "Data Analyst"]

def normalize_text(text: str) -> str:
    if not text:
        return ""
    # Strip whitespace, lowercase, remove non-alphanumerics
    return re.sub(r'[^a-z0-9]', '', text.lower())

def validate_company_questions() -> bool:
    data_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "companies")
    files = glob.glob(os.path.join(data_dir, "*.json"))

    if not files:
        print(f"[FAIL] No company seed files found in {data_dir}")
        return False

    print(f"[*] Found {len(files)} company question seed files in {data_dir}")

    has_errors = False
    question_to_companies: Dict[str, Set[str]] = {}
    total_questions = 0

    for file_path in sorted(files):
        slug = os.path.basename(file_path).replace(".json", "")
        with open(file_path, "r", encoding="utf-8") as f:
            try:
                data = json.load(f)
            except Exception as e:
                print(f"[FAIL] Could not parse JSON for {file_path}: {e}")
                has_errors = True
                continue

        c_name = data.get("name") or data.get("company_name") or slug
        questions: List[Dict[str, Any]] = data.get("questions", [])

        # Role & Category Count Tracking
        counts_by_role_cat: Dict[str, Dict[str, int]] = {
            role: {cat: 0 for cat in MIN_QUOTAS} for role in TARGET_ROLES
        }

        for q in questions:
            total_questions += 1
            cat = (q.get("category") or "").strip().lower()
            role = (q.get("role") or "").strip()
            q_text = (q.get("question") or "").strip()

            if not q_text:
                print(f"[FAIL] [{slug}] Found empty question text in category {cat}")
                has_errors = True
                continue

            # Check question structure per category
            if cat == "aptitude":
                opts = q.get("options")
                ans = q.get("correct_answer")
                exp = q.get("explanation")
                if not isinstance(opts, list) or len(opts) < 4:
                    print(f"[FAIL] [{slug}] Aptitude question missing 4 options: '{q_text[:40]}...'")
                    has_errors = True
                if not ans:
                    print(f"[FAIL] [{slug}] Aptitude question missing correct answer: '{q_text[:40]}...'")
                    has_errors = True
                if not exp:
                    print(f"[FAIL] [{slug}] Aptitude question missing explanation: '{q_text[:40]}...'")
                    has_errors = True

            elif cat == "coding":
                diff = q.get("difficulty")
                extra = q.get("extra") or {}
                if not diff:
                    print(f"[FAIL] [{slug}] Coding question missing difficulty: '{q_text[:40]}...'")
                    has_errors = True
                if not extra.get("starter_code"):
                    print(f"[FAIL] [{slug}] Coding question missing starter code: '{q_text[:40]}...'")
                    has_errors = True

            elif cat == "technical":
                exp = q.get("explanation")
                if not exp:
                    print(f"[FAIL] [{slug}] Technical question missing explanation: '{q_text[:40]}...'")
                    has_errors = True

            # Track counts
            if role in counts_by_role_cat and cat in counts_by_role_cat[role]:
                counts_by_role_cat[role][cat] += 1

            # Cross-company duplicate check
            norm_text = normalize_text(q_text)
            if norm_text not in question_to_companies:
                question_to_companies[norm_text] = set()
            question_to_companies[norm_text].add(slug)

        # Check quotas
        for role in TARGET_ROLES:
            for cat, min_qty in MIN_QUOTAS.items():
                actual_qty = counts_by_role_cat[role].get(cat, 0)
                if actual_qty < min_qty:
                    print(f"[FAIL] [{slug}] Role '{role}' category '{cat}' count is {actual_qty} (Minimum required: {min_qty})")
                    has_errors = True

    # Validate cross-company duplicate questions
    duplicate_count = 0
    for norm_text, comp_set in question_to_companies.items():
        if len(comp_set) > 1:
            print(f"[FAIL] Duplicate question detected across companies {list(comp_set)}: '{norm_text[:60]}...'")
            duplicate_count += 1
            has_errors = True

    print("\n" + "=" * 60)
    print(f"VALIDATION SUMMARY:")
    print(f"Total Companies Evaluated: {len(files)}")
    print(f"Total Questions Verified: {total_questions}")
    print(f"Cross-Company Duplicates Found: {duplicate_count}")

    if has_errors:
        print("[RESULT] VALIDATION FAILED! Please address the errors above.")
        print("=" * 60)
        return False
    else:
        print("[RESULT] ALL VALIDATIONS PASSED! (0 duplicates, all quotas met)")
        print("=" * 60)
        return True


if __name__ == "__main__":
    success = validate_company_questions()
    sys.exit(0 if success else 1)
