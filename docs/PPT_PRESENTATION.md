# Smart Resume Analyzer with AI-Based Feedback
## Capstone Project Presentation Deck (12 Slides)

---

### Slide 1: Title & Introduction
- **Slide Title:** Smart Resume Analyzer with AI-Based Feedback
- **Subtitle:** An Automated ATS Screening & Resume Optimization Engine
- **Presenter / Candidate:** subbaraju-cmd
- **Project Domain:** Artificial Intelligence, Natural Language Processing & Web Development
- **GitHub Repository:** `subbaraju-cmd/Smart-Resume-Analyzer`
- **Speaker Notes:**
  > "Good morning, respected evaluators and panel members. Today, I am presenting my Capstone project: The Smart Resume Analyzer with AI-Based Feedback. This project addresses a critical bottleneck in the modern hiring pipeline: automated Applicant Tracking System (ATS) resume screening."

---

### Slide 2: The Problem Statement
- **Slide Title:** Why Traditional Resume Screening Fails Candidates
- **Key Points:**
  - Over 75% of resumes are filtered out before reaching a human recruiter.
  - Inconsistent formatting, missing section headers, and low target keyword density cause automated rejections.
  - Existing online resume checkers give misleading scores by heavily weighting generic contact information even when candidate technical skills are absent.
  - Boundary matching issues: Standard keyword parsers fail on languages like C++, C#, and Node.js.
- **Speaker Notes:**
  > "In today's recruitment landscape, large companies receive thousands of resumes. Over 75% are filtered out by ATS algorithms. Most candidates don't know why they are rejected. Furthermore, existing online resume checkers often inflate scores, giving high marks to unqualified resumes simply because they included an email and a phone number."

---

### Slide 3: Proposed Solution & Core Innovation
- **Slide Title:** The Smart Resume Analyzer Engine
- **Key Points:**
  - Automated document parsing for both PDF and DOCX formats.
  - Multi-tier ATS compatibility scoring across 6 synchronized technical engineering roles.
  - Boundary-aware regex tokenization eliminating false positives on technical symbols.
  - Relevance guardrails: Hard-capped scoring that ensures 0% keyword matches never pass.
  - Actionable feedback powered by Google's X-Y-Z bullet point formula.
  - One-click vector PDF audit report generation.
- **Speaker Notes:**
  > "To solve this, we built a deterministic, recruiter-aligned ATS engine. It parses PDF and Word resumes, extracts plain text, audits contact info and standard sections, calculates realistic role-specific keyword match rates, and outputs actionable suggestions to help the applicant land interviews."

---

### Slide 4: System Architecture
- **Slide Title:** End-to-End Pipeline Architecture
- **Key Points:**
  - **Ingestion:** File upload via Flask (`/upload`) supporting `.pdf` and `.docx`.
  - **Extraction Layer (`core/parser.py`):** Multi-page plain text stream extraction.
  - **Audit Layer (`core/section_analyzer.py`):** Email validation, phone detection, social link detection, and section header verification.
  - **Scoring Layer (`core/ats_scorer.py`):** Lookaround regex token matching and 4-factor scoring.
  - **Feedback Layer (`core/feedback_generator.py`):** Tailored bullet points, weak vs strong phrasing, action verbs.
  - **Presentation Layer (`templates/components/`):** 1440px widescreen dashboard + html2pdf export.
- **Speaker Notes:**
  > "Here is our architecture. The application is completely decoupled into modular components. The document extraction feeds clean text into parallel audit modules: section verification and keyword scoring. The results then flow into our feedback generator and render on a responsive dashboard."

---

### Slide 5: Lookaround Regex & Token Matching
- **Slide Title:** Solving the ATS Keyword Boundary Problem
- **Key Points:**
  - Standard regex `\b` fails on programming languages with symbols:
    - `\bC++\b` fails because `+` is a non-word character.
    - `\bNode.js\b` fails due to the period.
  - Our Solution: Custom Lookaround Boundary:
    `(?<![a-zA-Z0-9])keyword(?![a-zA-Z0-9])`
  - Guarantees `Java` does not match `JavaScript`, and `C` does not match `CSS` or `C++`.
- **Speaker Notes:**
  > "A core technical challenge in resume parsing is token boundary accuracy. Standard word boundaries fail on tokens like C++ and Node.js. By developing custom lookaround boundary regular expressions, our engine accurately isolates technical keywords without false positives."

---

### Slide 6: Realistic Scoring Model
- **Slide Title:** Preventing Artificial Score Inflation
- **Key Points:**
  - **Score Formula:**
    - Role Match: 40 points
    - Technical Depth: 25 points
    - Section Architecture: 25 points
    - Contact Details: 10 points
  - **Strict Relevance Guardrails:**
    - 0% Keyword Match $\rightarrow$ Score capped at $\le 25/100$
    - $<25\%$ Keyword Match $\rightarrow$ Score capped at $\le 40/100$
    - $<50\%$ Keyword Match $\rightarrow$ Score capped at $\le 55/100$
- **Speaker Notes:**
  > "Many naive resume checkers award 70 points out of 100 to a Personal Trainer applying for a Web Developer role just because they have complete contact details and standard headers. Our engine introduces relevance guardrails: if your technical match is 0%, your score is hard-capped at 24/100. This mirrors real-world corporate ATS filtering."

---

### Slide 7: Actionable Feedback & Google X-Y-Z Formula
- **Slide Title:** Guiding the Candidate to Improvement
- **Key Points:**
  - Identifies matched keywords (green chips) and missing skill gaps (red chips).
  - Formulates bullet points using Google's formula:
    *"Accomplished [X], as measured by [Y], by doing [Z]"*.
  - Provides instant comparison of weak passive phrasing vs strong metric-driven phrasing.
  - Curated dictionary of high-impact engineering action verbs.
- **Speaker Notes:**
  > "Rather than just displaying a score, our application tells candidates exactly how to improve. We show them their missing skills and generate concrete examples using Google's famous X-Y-Z formula. We also provide side-by-side phrasing improvements to replace passive descriptions with quantified achievements."

---

### Slide 8: Modular Component-Based UI
- **Slide Title:** Clean, Maintainable Frontend Architecture
- **Key Points:**
  - Zero bloated monolith templates: The results page is divided into 10 reusable component templates in `templates/components/`.
  - Independent maintenance: Metric overview, keyword chips, section tables, and suggestion boxes can be modified without side effects.
  - Responsive 1440px dashboard optimized for readability.
- **Speaker Notes:**
  > "On the frontend, we followed modern software design patterns by breaking our user interface into 10 self-contained component templates. This makes the codebase clean, readable, and feature-friendly for long-term maintenance."

---

### Slide 9: Vector PDF Audit Report Export
- **Slide Title:** Client-Side Report Generation
- **Key Points:**
  - Integrated `html2pdf.js` with custom `static/css/print.css`.
  - Generates downloadable `ATS_Analysis_Report_<filename>.pdf` directly in the browser.
  - Zero server overhead or external headless browser dependencies.
  - Clean, professional styling suitable for sharing with mentors and career advisors.
- **Speaker Notes:**
  > "Candidates can export their full analysis report as a high-quality vector PDF with a single click. The generation occurs entirely on the client side using optimized print stylesheets, eliminating server-side rendering latency."

---

### Slide 10: Live Demonstration & Test Results
- **Slide Title:** Empirical Validation & Test Cases
- **Key Points:**
  - **Test Case 1:** Non-technical resume tested against Web Developer role $\rightarrow$ Correctly rejected with 0% match and 24/100 score.
  - **Test Case 2:** Standard developer resume tested against Python Developer role $\rightarrow$ 57.1% match, 68/100 score with missing libraries pinpointed.
  - **Test Case 3:** Senior engineer resume tested against AI Engineer role $\rightarrow$ 90% match, 91/100 score.
- **Speaker Notes:**
  > "We tested our engine across diverse candidate profiles. The results clearly demonstrate that our relevance guardrails prevent false positives while accurately reflecting technical competence across multiple engineering disciplines."

---

### Slide 11: Deployment & DevOps Architecture
- **Slide Title:** Production-Ready Cloud Architecture
- **Key Points:**
  - Automated deployment workflow on GitHub: `subbaraju-cmd/Smart-Resume-Analyzer`.
  - Production WSGI configuration with `gunicorn>=23.0.0` in `requirements.txt`.
  - `Procfile` configured for one-click deployment on Render, Railway, or Heroku.
  - Clean local virtual environment setup for local development.
- **Speaker Notes:**
  > "The project is fully production-ready. Our repository contains a pinned requirements.txt and Procfile configured with Gunicorn, enabling seamless automated deployment to cloud platforms like Render."

---

### Slide 12: Conclusion & Q&A
- **Slide Title:** Summary & Future Roadmap
- **Key Points:**
  - Successfully built a fast, deterministic, ATS-aligned resume screening web application.
  - Eliminated score inflation and regex token traps.
  - Provided candidates with clear, metric-driven improvement roadmaps.
  - Future Work: OCR for image scans and semantic similarity scoring with lightweight embeddings.
  - Thank you! Questions and feedback are welcome.
- **Speaker Notes:**
  > "In conclusion, the Smart Resume Analyzer provides a transparent, recruiter-aligned tool that helps job seekers navigate modern automated hiring systems. Thank you for your time, and I look forward to your questions."
