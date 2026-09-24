"""
analyzer.py - Backward-compatible facade for core ATS engine.
Forwards calls to the modular core package:
- core.parser: text extraction
- core.section_analyzer: contact and section detection
- core.ats_scorer: keyword matching and score calculation
- core.feedback_generator: suggestions and bullet point examples
"""

from core import (
    analyze_resume,
    load_job_roles,
    ALL_SKILLS,
    ACTION_VERBS,
    SAMPLE_BULLET_POINTS
)

__all__ = [
    "analyze_resume",
    "load_job_roles",
    "ALL_SKILLS",
    "ACTION_VERBS",
    "SAMPLE_BULLET_POINTS"
]