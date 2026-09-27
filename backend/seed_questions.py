# -*- coding: utf-8 -*-
"""
Database Seeder for Company Preparation Questions.

Combines seed question batches across 13 major companies:
- Batch 1: TCS, Infosys, Wipro, Accenture (160 questions)
- Batch 2: Cognizant, Capgemini, HCL, Tech Mahindra (160 questions)
- Batch 3: Amazon, Google, Microsoft, Deloitte, IBM (200 questions)
Total: 520 hand-curated, company-specific questions (40 questions per company,
8 questions per experience level across all 5 canonical levels).

Viva explanation:
- seed_questions_if_empty(): Called on server startup. Checks if the `questions` table
  has 0 rows; if so, populates all 520 curated questions safely.
- Question hashes and (company, question_hash) unique constraints prevent duplicates.
"""

import sys
import logging
from backend.models import QuestionModel
from backend.data.seed_data_batch1 import BATCH_1_DATA
from backend.data.seed_data_batch2 import BATCH_2_DATA
from backend.data.seed_data_batch3 import BATCH_3_DATA

logger = logging.getLogger("seed_questions")
logging.basicConfig(level=logging.INFO)

# Merge all three batches into one comprehensive dataset
SEED_QUESTIONS_DATA = {
    **BATCH_1_DATA,
    **BATCH_2_DATA,
    **BATCH_3_DATA
}


def seed_questions(force: bool = False):
    """
    Seeds the questions table with curated company questions.

    Args:
        force: If True, attempts to insert even if table is not empty
               (unique constraints prevent duplicate insertions).

    Returns:
        dict: Summary of {inserted: int, skipped: int, total_in_db: int}
    """
    total_existing = QuestionModel.get_total_count()
    if total_existing > 0 and not force:
        logger.info(f"Questions table already contains {total_existing} questions. Skipping seed.")
        return {"inserted": 0, "skipped": 0, "total_in_db": total_existing}

    inserted = 0
    skipped = 0

    for company, levels in SEED_QUESTIONS_DATA.items():
        for level, q_list in levels.items():
            for item in q_list:
                res = QuestionModel.insert(
                    company=company,
                    experience_level=level,
                    role=item.get("role", "Software Engineer"),
                    question_type=item.get("question_type", "technical_depth"),
                    category=item.get("category", "Technical"),
                    question_text=item.get("question_text", ""),
                    sample_answer=item.get("sample_answer", ""),
                    difficulty=item.get("difficulty", "medium"),
                    source="curated_seed"
                )
                if res:
                    inserted += 1
                else:
                    skipped += 1

    total_in_db = QuestionModel.get_total_count()
    logger.info(f"Seeding completed. Inserted: {inserted}, Skipped: {skipped}, Total in DB: {total_in_db}")
    return {"inserted": inserted, "skipped": skipped, "total_in_db": total_in_db}


def seed_questions_if_empty():
    """
    Convenience hook for application startup (Flask / FastAPI).
    Runs seed_questions only if database has 0 questions.
    """
    try:
        count = QuestionModel.get_total_count()
        if count == 0:
            logger.info("Questions table is empty. Running initial seeding...")
            return seed_questions(force=True)
        else:
            logger.info(f"Questions table has {count} records. No seeding needed.")
            return {"inserted": 0, "skipped": 0, "total_in_db": count}
    except Exception as e:
        logger.error(f"Error checking or seeding questions: {e}")
        return {"error": str(e)}


if __name__ == "__main__":
    force_run = "--force" in sys.argv
    print(f"Running seed_questions(force={force_run})...")
    summary = seed_questions(force=force_run)
    print(f"Result: {summary}")
