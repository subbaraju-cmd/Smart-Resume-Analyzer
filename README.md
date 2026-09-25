# Smart Resume Analyzer | ATS Compatibility Screening Engine

# 🚀 Deployment Link
**Live Application URL:** **[https://smart-resume-analyzer-utj7.onrender.com](https://smart-resume-analyzer-utj7.onrender.com)**

---

An industry-grade, deterministic, keyword-based **Applicant Tracking System (ATS) Resume Analyzer** built with Python Flask. Evaluates resumes against target role keywords, checks section architecture, identifies skill gaps, and provides actionable suggestions with one-click PDF audit report export.

---

## Project Structure & Architecture

The codebase is organized into **feature-friendly backend modules** and **modular frontend component files** so any feature or UI element can be easily located and modified.

```
Smart-Resume-Analyzer/
├── core/                                # Backend Core Engine (Feature Modules)
│   ├── __init__.py                     # Master orchestrator combining all modules
│   ├── parser.py                       # Document text extraction (PDF & DOCX)
│   ├── section_analyzer.py             # Section taxonomy & contact verification
│   ├── ats_scorer.py                   # Keyword matching & ATS compatibility scoring
│   └── feedback_generator.py           # Suggestion engine & tailored bullet point examples
│
├── templates/                          # HTML Views
│   ├── index.html                      # Upload landing page
│   ├── result.html                     # Master analysis dashboard (assembles components)
│   └── components/                     # Modular Frontend Component Files
│       ├── header_banner.html          # Title, candidate meta, status, and download PDF button
│       ├── metrics_overview.html       # 5 KPI score cards (Role Match, Resume Score, etc.)
│       ├── keyword_match.html          # Matched Keywords, Missing Keywords, Detected Skills
│       ├── section_check.html          # Section & Contact Check checklist table
│       ├── suggestions.html            # Improvement Suggestions & Google X-Y-Z formula box
│       ├── example_bullets.html        # Bullet points for missing skills & Other Roles Match
│       ├── weak_vs_strong.html         # Weak vs Strong bullet points comparison
│       ├── action_verbs.html           # Recommended action verbs & formatting mistakes
│       ├── section_guide.html          # 6-card resume section guide
│       └── extracted_text.html         # Collapsible extracted text viewer
│
├── static/                             # Static Assets
│   ├── css/
│   │   ├── style.css                   # Main responsive stylesheet
│   │   └── print.css                   # Print and vector PDF export stylesheet
│   └── js/
│       ├── pdf_export.js               # One-click client-side PDF generator (html2pdf.js)
│       └── upload_handler.js           # File upload dropzone event handler
│
├── data/
│   └── job_roles.json                  # Database of job roles and required keywords
│
├── uploads/                            # Stored uploaded resumes
├── analyzer.py                         # Backward-compatible facade forwarding to core/
├── app.py                              # Flask application entrypoint and routes
└── README.md                           # Documentation & architecture guide
```

---

## Where to Edit Features & Components

| Feature / UI Element | File to Open | Description |
| :--- | :--- | :--- |
| **PDF & DOCX Parsing** | [`core/parser.py`](core/parser.py) | Text extraction using `pypdf` and `python-docx`. |
| **Contact & Section Checks** | [`core/section_analyzer.py`](core/section_analyzer.py) | Email syntax regex, telephone patterns, and section header detection. |
| **ATS Scoring & Keywords** | [`core/ats_scorer.py`](core/ats_scorer.py) | Boundary-aware keyword matching, skill extraction, and percentage scoring. |
| **Suggestions & Bullet Points** | [`core/feedback_generator.py`](core/feedback_generator.py) | Action items, Google X-Y-Z examples, and feedback rules. |
| **Job Roles & Skills Database** | [`data/job_roles.json`](data/job_roles.json) | Add/modify target roles and required technical skills. |
| **Top Banner & PDF Button** | [`templates/components/header_banner.html`](templates/components/header_banner.html) | Title, role tag, match status pill, and PDF download button. |
| **5 KPI Metric Cards** | [`templates/components/metrics_overview.html`](templates/components/metrics_overview.html) | Role Match %, Resume Score /100, Keywords Found, Action Verbs, Word Count. |
| **Keyword Match Chips** | [`templates/components/keyword_match.html`](templates/components/keyword_match.html) | Green `[MATCH]` and red `[GAP]` keyword badges. |
| **Section Checklist Table** | [`templates/components/section_check.html`](templates/components/section_check.html) | Email, Phone, LinkedIn, GitHub, and section headers table. |
| **Suggestions & Google Formula**| [`templates/components/suggestions.html`](templates/components/suggestions.html) | Actionable improvement tips and Google X-Y-Z formula. |
| **Example Bullets & Other Roles**| [`templates/components/example_bullets.html`](templates/components/example_bullets.html) | Ready-to-use bullet points for missing skills & cross-role comparisons. |
| **Weak vs Strong Phrasing** | [`templates/components/weak_vs_strong.html`](templates/components/weak_vs_strong.html) | Side-by-side phrasing transformation table. |
| **Action Verbs & Mistakes** | [`templates/components/action_verbs.html`](templates/components/action_verbs.html) | Recommended engineering verbs and formatting red flags. |
| **Resume Section Guide** | [`templates/components/section_guide.html`](templates/components/section_guide.html) | 6-card best practices guide for every resume section. |
| **Raw Extracted Text Stream** | [`templates/components/extracted_text.html`](templates/components/extracted_text.html) | Expandable raw text parsed by the backend engine. |
| **Styling & Layout** | [`static/css/style.css`](static/css/style.css) | Colors, typography, spacing, and responsive cards. |
| **PDF Export Engine** | [`static/js/pdf_export.js`](static/js/pdf_export.js) | Generates `ATS_Analysis_Report_<filename>.pdf`. |

---

## Running the Application

### 1. Activate Virtual Environment
```powershell
.\venv\Scripts\activate
```

### 2. Start the Server
```powershell
python app.py
```

### 3. Open in Browser
Visit **`http://127.0.0.1:5000`** in your web browser.
