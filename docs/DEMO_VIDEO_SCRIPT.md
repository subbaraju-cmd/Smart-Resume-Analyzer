# Smart Resume Analyzer with AI-Based Feedback
## Video Demonstration Recording Script & Storyboard (3 - 5 Minutes)

Use this guide to record your project demonstration video. You can record using OBS Studio, Loom, or Windows Game Bar (Win + G).

---

### Segment 1: Introduction & Project Overview (0:00 - 0:45)
- **On Screen:**
  - Browser open at `http://127.0.0.1:5000` (or live Render deployment URL).
  - Clean landing page with role dropdown and drag-and-drop file upload zone.
- **What to Say:**
  > "Hello everyone. My name is subbaraju-cmd, and this is the demonstration of my Capstone project: The Smart Resume Analyzer with AI-Based Feedback.
  >
  > In today's competitive job market, over 75% of resumes are filtered out by automated Applicant Tracking Systems (ATS) before a human recruiter ever sees them. Many candidates struggle to understand why their applications are rejected.
  >
  > The Smart Resume Analyzer is an automated web platform built with Python Flask that parses PDF and Word resumes, audits contact details and structural sections, matches technical keywords against real-world engineering taxonomies, and provides actionable recommendations to optimize candidate resumes."

---

### Segment 2: Testing an Unqualified Resume (Demonstrating Guardrails) (0:45 - 1:45)
- **On Screen:**
  - Select "Web Developer" from the Target Job Role dropdown.
  - Upload a non-technical resume (e.g., Personal Trainer or generic resume without web development skills).
  - Click "Analyze Resume".
  - Result dashboard loads.
- **What to Say:**
  > "First, let's test a common flaw found in many online resume checkers: artificial score inflation.
  >
  > Here, I have selected the Web Developer role and uploaded a non-technical resume. Notice our results:
  > - The Role Match is 0.0%.
  > - Even though this candidate has a valid email, phone number, and standard section headers, our system does NOT award a passing score.
  > - Thanks to our relevance guardrails, the overall Resume Score is capped at 24 out of 100.
  > - The dashboard clearly displays the missing technical skills in red chips: JavaScript, React, HTML, CSS, Git, and REST APIs.
  > This realistic scoring reflects how actual corporate ATS filters operate."

---

### Segment 3: Testing a Strong Technical Resume (1:45 - 2:45)
- **On Screen:**
  - Click "Upload Another Resume" button to return to the home page.
  - Select "Python Developer" or "AI Engineer".
  - Upload a technical resume with relevant experience (`Resume_1.pdf`).
  - Click "Analyze Resume".
  - Result dashboard displays high match metrics.
- **What to Say:**
  > "Now, let's analyze a qualified candidate resume for the Python Developer role.
  >
  > As you can see:
  > - The 5 KPI score cards immediately provide an overview: Role Match is over 70%, and the overall Resume Score is 80+.
  > - Under Keyword Match, matched keywords are highlighted in green, showing strong alignment in Python, Git, and SQL, while missing libraries like Docker and Celery are highlighted in red.
  > - Our Section & Contact Check verifies the email syntax, phone number, LinkedIn link, and the presence of essential sections like Education, Experience, and Skills."

---

### Segment 4: Actionable Feedback & PDF Export (2:45 - 3:30)
- **On Screen:**
  - Scroll down through the Suggestions section.
  - Point to Google's X-Y-Z formula box: *"Accomplished [X] as measured by [Y] by doing [Z]"*.
  - Show the Weak vs Strong phrasing transformation table.
  - Scroll to the top and click the "Download PDF Report" button.
  - Show the generated vector PDF opening in the browser.
- **What to Say:**
  > "What truly makes this tool powerful is the actionable feedback engine.
  >
  > Instead of leaving the candidate with just a number, we provide:
  > - Ready-to-use bullet points tailored specifically to the missing skills.
  > - Bullet formulation using Google's proven X-Y-Z formula.
  > - A side-by-side comparison of weak passive phrasing versus strong, metric-driven phrasing.
  > - A comprehensive list of strong action verbs to replace overused terms.
  >
  > Finally, candidates can click 'Download PDF Report' in the top right to instantly generate and download a clean, print-ready vector PDF report of their audit."

---

### Segment 5: Architecture, GitHub Repository & Conclusion (3:30 - 4:00)
- **On Screen:**
  - Show the GitHub repository: `https://github.com/subbaraju-cmd/Smart-Resume-Analyzer`.
  - Briefly show the clean modular directory structure (`core/`, `templates/components/`, `data/`).
- **What to Say:**
  > "Behind the scenes, the project is built with clean, modular architecture: decoupled Python modules in `core/` for parsing, auditing, and scoring, and 10 isolated HTML component templates on the frontend.
  >
  > The complete source code, documentation, and deployment files are publicly available on GitHub at `subbaraju-cmd/Smart-Resume-Analyzer`.
  >
  > Thank you for watching my Capstone presentation!"
