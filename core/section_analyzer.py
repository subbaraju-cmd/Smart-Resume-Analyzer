import re


SECTION_KEYWORDS = {
    "Education": [
        "education", "academic", "b.tech", "bachelor", "master",
        "degree", "university", "college", "school", "gpa", "cgpa"
    ],
    "Skills": [
        "skills", "technical skills", "core competencies",
        "technologies", "programming languages", "tools"
    ],
    "Projects": [
        "projects", "academic projects", "key projects", "personal projects"
    ],
    "Experience": [
        "experience", "work experience", "professional experience",
        "internship", "employment", "job history"
    ],
    "Certifications": [
        "certification", "certifications", "certificate",
        "licensed", "courses", "credentials"
    ]
}


def analyze_contact_info(resume_text: str) -> dict:
    """Verifies and extracts contact info (email, telephone, LinkedIn, GitHub)."""
    text_lower = resume_text.lower()

    email_match = re.search(
        r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}",
        resume_text
    )
    email_found = bool(email_match)
    email_value = email_match.group(0) if email_match else None

    phone_match = re.search(
        r"(?:\+?\d{1,3}[\s-]?)?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}|\b(?:\+91[\s-]?)?[6-9]\d{9}\b",
        resume_text
    )
    phone_found = bool(phone_match)
    phone_value = phone_match.group(0) if phone_match else None

    linkedin_found = bool(re.search(r"linkedin\.com/in/|linkedin", text_lower))
    github_found = bool(re.search(r"github\.com/|github", text_lower))

    return {
        "email_found": email_found,
        "email_value": email_value,
        "phone_found": phone_found,
        "phone_value": phone_value,
        "linkedin_found": linkedin_found,
        "github_found": github_found
    }


def analyze_sections(resume_text: str, contact_info: dict) -> dict:
    """Detects standard resume sections based on keyword taxonomy."""
    text_lower = resume_text.lower()

    has_contact = (
        contact_info["email_found"] or
        contact_info["phone_found"] or
        contact_info["linkedin_found"] or
        contact_info["github_found"]
    )

    sections = {
        "Contact Information": has_contact,
        "Education": False,
        "Skills": False,
        "Projects": False,
        "Experience": False,
        "Certifications": False
    }

    for section, keywords in SECTION_KEYWORDS.items():
        for keyword in keywords:
            pattern = r'(?<![a-zA-Z0-9])' + re.escape(keyword) + r'(?![a-zA-Z0-9])'
            if re.search(pattern, text_lower, re.IGNORECASE):
                sections[section] = True
                break

    return sections


def calculate_document_metrics(resume_text: str) -> dict:
    """Computes word count, character count, and non-empty line count."""
    words = resume_text.split()
    lines = [line for line in resume_text.splitlines() if line.strip()]
    return {
        "word_count": len(words),
        "char_count": len(resume_text),
        "line_count": len(lines)
    }
