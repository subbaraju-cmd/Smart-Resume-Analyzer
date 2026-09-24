"""
Core ATS Engine Package
Provides modular services for document parsing, section auditing, ATS scoring, and feedback generation.
"""

from .parser import extract_pdf_text, extract_docx_text, extract_text_from_file
from .section_analyzer import analyze_contact_info, analyze_sections, calculate_document_metrics
from .ats_scorer import (
    load_job_roles,
    extract_skills,
    calculate_role_match,
    calculate_resume_score,
    audit_impact_metrics,
    ALL_SKILLS,
    ACTION_VERBS
)
from .feedback_generator import generate_recommendations, SAMPLE_BULLET_POINTS


def analyze_resume(resume_text: str, target_role: str = None) -> dict:
    """
    Master orchestrator for complete ATS resume analysis:
    1. Extracts document metrics (words, chars, lines).
    2. Verifies contact information (email, phone, LinkedIn, GitHub).
    3. Audits standard resume sections.
    4. Extracts technical skills against master taxonomy.
    5. Audits action verbs and quantifiable metrics.
    6. Matches target role keywords and computes ATS compatibility.
    7. Calculates overall structural score.
    8. Generates prioritized, rule-based recommendations and examples.
    """
    job_roles = load_job_roles()

    # 1. Document metrics
    doc_metrics = calculate_document_metrics(resume_text)

    # 2. Contact info verification
    contact_info = analyze_contact_info(resume_text)

    # 3. Section detection
    sections = analyze_sections(resume_text, contact_info)

    # 4. Technical skills extraction
    detected_skills = extract_skills(resume_text)

    # 5. Impact metrics & action verbs
    impact_info = audit_impact_metrics(resume_text)

    # 6. Target role ATS matching
    role_match = calculate_role_match(resume_text, target_role, job_roles)

    # 7. Structural & Role-Weighted Scoring
    score = calculate_resume_score(
        contact_info=contact_info,
        sections=sections,
        detected_skills=detected_skills,
        ats_score=role_match["ats_score"],
        matched_skills_count=len(role_match["matched_skills"])
    )

    # 8. Recommendation generation
    recommendations = generate_recommendations(
        target_role=target_role,
        role_match=role_match,
        contact_info=contact_info,
        sections=sections,
        metrics=doc_metrics,
        impact_info=impact_info,
        detected_skills=detected_skills,
        job_roles=job_roles
    )

    return {
        "score": score,
        "ats_score": role_match["ats_score"],
        "target_role": target_role,
        "matched_skills": role_match["matched_skills"],
        "missing_skills": role_match["missing_skills"],
        "detected_skills": detected_skills,
        "sections": sections,
        "email_found": contact_info["email_found"],
        "email_value": contact_info["email_value"],
        "phone_found": contact_info["phone_found"],
        "phone_value": contact_info["phone_value"],
        "linkedin_found": contact_info["linkedin_found"],
        "github_found": contact_info["github_found"],
        "feedback": recommendations["all_feedback"],
        "role_recommendations": recommendations["role_recommendations"],
        "structural_recommendations": recommendations["structural_recommendations"],
        "impact_recommendations": recommendations["impact_recommendations"],
        "formatting_recommendations": recommendations["formatting_recommendations"],
        "tailored_examples": recommendations["tailored_examples"],
        "role_comparisons": role_match["role_comparisons"],
        "metrics": {
            "word_count": doc_metrics["word_count"],
            "char_count": doc_metrics["char_count"],
            "line_count": doc_metrics["line_count"],
            "skills_count": len(detected_skills),
            "matched_count": len(role_match["matched_skills"]),
            "missing_count": len(role_match["missing_skills"]),
            "action_verbs_count": impact_info["action_verbs_count"],
            "quant_metrics_count": impact_info["metric_count"],
            "sections_present": sum(sections.values()),
            "total_sections": len(sections)
        }
    }
