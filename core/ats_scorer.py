import re
import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JOB_ROLES_FILE = os.path.join(BASE_DIR, "data", "job_roles.json")


def load_job_roles() -> dict:
    """Loads target roles and required skills from the data directory."""
    if os.path.exists(JOB_ROLES_FILE):
        with open(JOB_ROLES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}


ALL_SKILLS = [
    "Python", "Java", "C++", "C", "C#", "JavaScript", "TypeScript",
    "HTML", "CSS", "SQL", "MySQL", "PostgreSQL", "MongoDB",
    "Flask", "Django", "FastAPI", "React", "Node.js", "Angular", "Vue",
    "Machine Learning", "Deep Learning", "Artificial Intelligence",
    "Data Science", "Data Analytics", "Data Visualization",
    "Pandas", "NumPy", "Scikit-learn", "TensorFlow", "PyTorch", "NLP", "Computer Vision",
    "Git", "GitHub", "Docker", "Kubernetes", "AWS", "Azure", "GCP",
    "Linux", "Power BI", "Tableau", "Excel", "Statistics", "ETL", "CI/CD",
    "REST API", "Bootstrap", "Tailwind", "Terraform"
]

ACTION_VERBS = [
    "developed", "engineered", "designed", "implemented", "optimized",
    "built", "architected", "deployed", "automated", "created", "spearheaded",
    "integrated", "reduced", "accelerated", "streamlined", "analyzed",
    "trained", "delivered", "modeled", "configured", "orchestrated"
]


def keyword_present(keyword: str, text: str) -> bool:
    """Checks for keyword presence using lookaround boundaries to avoid false substrings."""
    kw = keyword.strip().lower()
    pattern = re.escape(kw)
    prefix = r'(?<![a-zA-Z0-9])'
    suffix = r'(?![a-zA-Z0-9])'
    return bool(re.search(prefix + pattern + suffix, text, re.IGNORECASE))


def extract_skills(resume_text: str) -> list:
    """Extracts all recognized technical skills from the master taxonomy."""
    text_lower = resume_text.lower()
    return [skill for skill in ALL_SKILLS if keyword_present(skill, text_lower)]


def audit_impact_metrics(resume_text: str) -> dict:
    """Detects strong action verbs and quantitative metrics (e.g. percentages, latency, users)."""
    text_lower = resume_text.lower()
    detected_verbs = [v for v in ACTION_VERBS if keyword_present(v, text_lower)]
    metrics_matches = re.findall(
        r"\b\d+(?:\.\d+)?%|\b\d+\s*(?:k|m|ms|sec|seconds|hours|users|records|queries)\b|\$\d+",
        text_lower
    )
    return {
        "action_verbs": detected_verbs,
        "action_verbs_count": len(detected_verbs),
        "metric_count": len(metrics_matches)
    }


def calculate_role_match(resume_text: str, target_role: str, job_roles: dict) -> dict:
    """Calculates ATS keyword match, gap, and cross-role comparison percentages."""
    text_lower = resume_text.lower()
    matched_skills = []
    missing_skills = []
    ats_score = 0
    role_comparisons = {}

    for role, req_skills in job_roles.items():
        role_matched = [s for s in req_skills if keyword_present(s, text_lower)]
        role_pct = round((len(role_matched) / len(req_skills)) * 100) if req_skills else 0
        role_comparisons[role] = {
            "matched_skills": role_matched,
            "percentage": role_pct
        }

    if target_role and target_role in job_roles:
        required_keywords = job_roles[target_role]
        matched_skills = [s for s in required_keywords if keyword_present(s, text_lower)]
        missing_skills = [s for s in required_keywords if s not in matched_skills]
        ats_score = round((len(matched_skills) / len(required_keywords)) * 100) if required_keywords else 0
    elif target_role:
        matched_skills = extract_skills(resume_text)
        missing_skills = []
        ats_score = 50

    return {
        "ats_score": ats_score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "role_comparisons": role_comparisons
    }


def calculate_resume_score(contact_info: dict,
                           sections: dict,
                           detected_skills: list,
                           ats_score: int = 0,
                           matched_skills_count: int = 0) -> int:
    """
    Calculates a realistic, weighted overall resume score out of 100:
    1. Role Keyword Alignment (Weight: 40 pts): Derived directly from target role ATS match.
    2. Technical Skill Depth (Weight: 25 pts): Breadth of verified technical skills.
    3. Section Architecture (Weight: 25 pts): Standard sections (Education, Experience, Projects, Certifications).
    4. Contact Prerequisites (Weight: 10 pts): Baseline email, phone, and professional profiles.

    Relevance Guardrails:
    - If 0 keywords match the target role, overall score is capped at 25/100 (candidate is unqualified).
    - If keyword match is under 25%, overall score is capped at 40/100.
    - If keyword match is under 50%, overall score is capped at 55/100.
    """
    # 1. Role Keyword Alignment (Max 40 pts)
    role_points = round((ats_score / 100.0) * 40)

    # 2. Technical Skill Depth (Max 25 pts)
    skill_count = len(detected_skills)
    if matched_skills_count == 0:
        skill_points = 0
    elif skill_count >= 6:
        skill_points = 25
    elif skill_count >= 4:
        skill_points = 18
    elif skill_count >= 2:
        skill_points = 12
    elif skill_count >= 1:
        skill_points = 6
    else:
        skill_points = 0

    # 3. Section Architecture (Max 25 pts)
    section_points = 0
    if sections.get("Education"):
        section_points += 7
    if sections.get("Experience"):
        section_points += 8
    if sections.get("Projects"):
        section_points += 7
    if sections.get("Certifications"):
        section_points += 3

    # 4. Contact Information (Max 10 pts)
    contact_points = 0
    if contact_info.get("email_found"):
        contact_points += 3
    if contact_info.get("phone_found"):
        contact_points += 3
    if contact_info.get("linkedin_found") or contact_info.get("github_found"):
        contact_points += 4

    total_score = role_points + skill_points + section_points + contact_points

    # Relevance Guardrails: Contact info and generic headers must not inflate an irrelevant resume
    if matched_skills_count == 0 or ats_score == 0:
        total_score = min(total_score, 25)
    elif ats_score < 25:
        total_score = min(total_score, 40)
    elif ats_score < 50:
        total_score = min(total_score, 55)

    return min(max(total_score, 0), 100)

