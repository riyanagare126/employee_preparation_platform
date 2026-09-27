"""
Company Question Catalogs (Enterprise 2026 Edition)
Provides rich, realistic, company-tailored questions for all 20 enterprises:
Google, Amazon, Microsoft, TCS, Infosys, Accenture, Wipro, Cognizant, Capgemini,
Deloitte, Oracle, IBM, Red Hat, HCLTech, Tech Mahindra, LTIMindtree, Persistent,
SAP, EY, PwC.
"""

from typing import Dict, List, Any
import copy

# Base domain knowledge definitions for generating high quality, realistic questions
# Each company has distinct hiring test formats and architecture focus.

from scripts.company_data_part1 import (
    GOOGLE_DATA, AMAZON_DATA, MICROSOFT_DATA, TCS_DATA, INFOSYS_DATA
)
from scripts.company_data_part2 import (
    ACCENTURE_DATA, WIPRO_DATA, COGNIZANT_DATA, CAPGEMINI_DATA, DELOITTE_DATA
)
from scripts.company_data_part3 import (
    ORACLE_DATA, IBM_DATA, REDHAT_DATA, HCLTECH_DATA, TECHMAHINDRA_DATA
)
from scripts.company_data_part4 import (
    LTIMINDTREE_DATA, PERSISTENT_DATA, SAP_DATA, EY_DATA, PWC_DATA
)

ALL_COMPANY_CATALOGS = {
    "google": GOOGLE_DATA,
    "amazon": AMAZON_DATA,
    "microsoft": MICROSOFT_DATA,
    "tcs": TCS_DATA,
    "infosys": INFOSYS_DATA,
    "accenture": ACCENTURE_DATA,
    "wipro": WIPRO_DATA,
    "cognizant": COGNIZANT_DATA,
    "capgemini": CAPGEMINI_DATA,
    "deloitte": DELOITTE_DATA,
    "oracle": ORACLE_DATA,
    "ibm": IBM_DATA,
    "redhat": REDHAT_DATA,
    "hcltech": HCLTECH_DATA,
    "techmahindra": TECHMAHINDRA_DATA,
    "ltimindtree": LTIMINDTREE_DATA,
    "persistent": PERSISTENT_DATA,
    "sap": SAP_DATA,
    "ey": EY_DATA,
    "pwc": PWC_DATA,
}

def get_catalog_for_company(slug: str, name: str, tag: str, focus: str, hr_tips: str) -> Dict[str, Any]:
    """Retrieves or builds the rich, authentic question bank for the given company."""
    slug_clean = slug.strip().lower()
    if slug_clean in ALL_COMPANY_CATALOGS:
        return ALL_COMPANY_CATALOGS[slug_clean]

    # Fallback to TCS catalog if company not found
    return ALL_COMPANY_CATALOGS["tcs"]
