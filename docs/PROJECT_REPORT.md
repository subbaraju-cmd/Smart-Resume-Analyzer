# Smart Resume Analyzer with AI-Based Feedback
## Academic Capstone Project Report

**Candidate / Author:** subbaraju-cmd  
**Project Track:** Artificial Intelligence, Natural Language Processing & Full-Stack Web Development  
**GitHub Repository:** [https://github.com/subbaraju-cmd/Smart-Resume-Analyzer](https://github.com/subbaraju-cmd/Smart-Resume-Analyzer)  
**Submission Date:** September 2026  

---

## 1. Executive Summary & Abstract

In contemporary automated recruitment workflows, corporate talent acquisition systems process hundreds of applicants per opening through Applicant Tracking Systems (ATS). A large percentage of qualified candidate resumes are rejected prematurely due to layout extraction parsing failures, non-standard section naming, or insufficient target-role keyword density.

The **Smart Resume Analyzer** is an automated, web-based recruitment analytics application built using **Python Flask**, **pypdf**, and **python-docx**. The system parses unstructured resume documents (.pdf and .docx), performs multi-stage text extraction, conducts contact information and structural section auditing, calculates a realistic, multi-factor ATS compatibility score against role-specific technical taxonomies, identifies skill gaps, and generates actionable phrasing recommendations and an exportable vector PDF report.

Unlike non-deterministic, cost-prohibitive large language model APIs, the system utilizes deterministic boundary-aware regular expression token matching and strict relevance guardrails. This eliminates false-positive substring matches and prevents artificial score inflation for unqualified resumes.

---

## 2. Problem Statement & Objectives

### 2.1 The Problem
Job seekers often submit generic resumes to specialized technical job openings without tailoring their skills and impact statements. Traditional resume checkers suffer from two major flaws:
1. **Unreliable Scoring:** Rewarding generic structural sections or contact details with high scores even when the candidate possesses 0% of the required technical skills for the role.
2. **Regex Substring Traps:** Standard word-boundary tokenizers fail on programming languages and technical terms containing symbols (e.g., `C++`, `Node.js`, `CI/CD`).

### 2.2 Project Objectives
- Build an end-to-end web application supporting PDF and DOCX document uploads.
- Implement an automated extraction pipeline that sanitizes text without third-party external API dependencies.
- Build an ATS keyword matching engine covering multiple engineering roles: Data Analyst, Web Developer, AI Engineer, Cloud Engineer, Python Developer, and Data Scientist.
- Enforce realistic scoring logic with relevance guardrails preventing unqualified resumes from passing.
- Provide tailored improvement feedback, including Google's X-Y-Z formula for bullet points.
- Provide a responsive 1440px widescreen dashboard and one-click PDF export functionality.

---

## 3. System Architecture & Methodology

The application follows a modular, decoupled architecture:

```
[Candidate Document (PDF / DOCX)]
               │
               ▼
   [core/parser.py] ──> Multi-format Document Extraction Engine
               │
               ▼ Clean Text Stream
   ┌───────────┴────────────────────────┐
   │                                    │
   ▼                                    ▼
[core/section_analyzer.py]      [core/ats_scorer.py]
• Contact verification          • Boundary-aware keyword matching
• Email syntax regex            • Role taxonomy match percentage
• Phone number parsing          • Technical depth & skill detection
• Section taxonomy check        • Weighted score calculation
   │                                    │
   └───────────┬────────────────────────┘
               │
               ▼
   [core/feedback_generator.py]
   • Google X-Y-Z formula recommendations
   • Tailored bullet points for missing skills
   • Weak vs Strong phrasing comparisons
   • Action verb taxonomy
               │
               ▼
   [Flask Presentation Layer (app.py + templates/components/)]
   • 1440px High-Density Interactive Dashboard
   • Client-side Vector PDF Generation (html2pdf.js)
```

---

## 4. Module-by-Module Technical Implementation

### 4.1 Document Extraction (`core/parser.py`)
- **PDF Extraction:** Uses `pypdf.PdfReader` to extract stream buffers across all document pages.
- **DOCX Extraction:** Uses `python-docx` to iterate across document paragraphs and table cells.
- **Fallback Mechanisms:** Catches empty files, malformed metadata, and scanned documents, returning explicit user-facing error notices.

### 4.2 Contact & Section Analysis (`core/section_analyzer.py`)
- **Email Validation:** RFC-compliant regex pattern verifying standard email syntax.
- **Phone Detection:** Standardized regex supporting international country codes, 10-digit formats, and hyphenated separators.
- **Portfolio Links:** Detection for LinkedIn and GitHub profiles.
- **Section Taxonomy:** Audits 5 essential sections: Contact Information, Summary/Objective, Education, Experience/Work History, and Skills.

### 4.3 ATS Compatibility Engine (`core/ats_scorer.py`)
- **Lookaround Boundary Matching:** Traditional word boundaries (`\b`) fail on tokens with special characters. The engine uses lookaround patterns:
  `(?<![a-zA-Z0-9])keyword(?![a-zA-Z0-9])`
  This accurately isolates `C++`, `Node.js`, and `.NET` without false positives.
- **Realistic Scoring Model:**
  $$\text{Final Score} = \text{Role Match (40\%)} + \text{Technical Depth (25\%)} + \text{Section Architecture (25\%)} + \text{Contact Details (10\%)}$$
- **Relevance Guardrails:**
  - If Role Match is 0%, Final Score is hard-capped at $\le 25/100$.
  - If Role Match is $< 25\%$, Final Score is capped at $\le 40/100$.
  - If Role Match is $< 50\%$, Final Score is capped at $\le 55/100$.
  This guarantees that an unqualified resume (e.g., Personal Trainer applying for a Web Developer role) cannot achieve a passing score merely by having complete contact info and generic headers.

### 4.4 Actionable Feedback Engine (`core/feedback_generator.py`)
- **Google X-Y-Z Framework:** Recommends bullet point formulation: *"Accomplished [X], as measured by [Y], by doing [Z]"*.
- **Skill Gap Examples:** Dynamically suggests ready-to-use resume bullet points for every missing keyword detected for the chosen target role.
- **Weak vs Strong Phrasing:** Provides a side-by-side comparison illustrating how passive descriptions can be transformed into high-impact metric statements.

---

## 5. Evaluation, Testing & Results

| Test Case | Target Role | Key Skills Present | Role Match % | Old Score | Realistic Score | Evaluation Result |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Personal Trainer Resume** | Web Developer | None (0 keywords) | 0.0% | 65/100 (Flawed) | **24/100** | Capped at guardrail threshold; correctly flagged as unqualified. |
| **Junior Python Developer** | Python Developer | Python, Git, SQL, Flask | 57.1% | 68/100 | **68/100** | Balanced score acknowledging baseline competence with missing keywords. |
| **Senior AI Engineer** | AI Engineer | PyTorch, TensorFlow, NLP, Docker, Python, Git | 90.0% | 88/100 | **91/100** | High match reflects comprehensive technical alignment. |

---

## 6. Deployment Specifications

- **Application Server:** Python 3.14 / Flask 3.0+
- **Production WSGI Server:** `gunicorn` (version $\ge$ 23.0.0) configured via `Procfile` (`web: gunicorn app:app`).
- **Dependencies:** Specified strictly in `requirements.txt`.
- **Target Cloud Platforms:** Render, Railway, or Heroku with automatic deployment triggers from the GitHub `main` branch.

---

## 7. Conclusion & Future Enhancements

The **Smart Resume Analyzer** provides an open-source, deterministic, and recruiter-aligned platform that bridges the gap between candidate submissions and corporate ATS filtering. Future enhancements include:
1. Optical Character Recognition (OCR) integration (e.g., Tesseract) for scanned image-based PDF resumes.
2. Semantic similarity scoring via lightweight on-device sentence embeddings (e.g., MiniLM) to identify contextual synonyms.
3. Multi-page layout parsing to detect multi-column table hierarchies.
