SAMPLE_BULLET_POINTS = {
    "SQL": "Authored performant SQL queries (CTEs, window functions) to extract and process 500K+ transactional records, reducing execution latency by 35%.",
    "Python": "Engineered automated Python data ingestion pipelines and ETL scripts, eliminating 12 hours of weekly manual reporting.",
    "Excel": "Constructed advanced Excel financial models utilizing Power Query, VLOOKUP, and pivot tables to evaluate departmental revenue variances.",
    "Power BI": "Built interactive Power BI executive dashboards connecting live SQL databases, tracking 15+ KPIs for business stakeholder review.",
    "Tableau": "Designed self-service Tableau visualization workbooks across 8 data sources, increasing stakeholder reporting adoption by 40%.",
    "React": "Engineered responsive, accessible single-page applications using React and state management hooks, cutting initial page load time by 30%.",
    "Node.js": "Developed asynchronous RESTful APIs using Node.js and Express, supporting 10,000+ daily client requests with sub-100ms response times.",
    "HTML": "Structured semantic HTML5 templates adhering to WCAG 2.1 accessibility standards and responsive mobile-first architectures.",
    "CSS": "Crafted responsive CSS/Sass design systems utilizing modern flexbox and grid layouts across cross-browser environments.",
    "Git": "Maintained collaborative codebase governance utilizing Git branching workflows, pull request code reviews, and version tagging.",
    "REST API": "Designed, secured, and documented RESTful microservice endpoints with OAuth2 authentication and JSON schema validation.",
    "Machine Learning": "Formulated predictive Machine Learning models using Scikit-learn, improving customer churn prediction precision by 18%.",
    "Deep Learning": "Architected convolutional and transformer deep learning architectures, achieving 94.2% validation accuracy on unstructured data.",
    "TensorFlow": "Trained and deployed deep neural networks using TensorFlow and Keras, leveraging GPU acceleration for 4x faster convergence.",
    "PyTorch": "Implemented PyTorch deep learning pipelines with custom dataset loaders and mixed-precision training for distributed inference.",
    "Scikit-learn": "Executed end-to-end data preprocessing, cross-validation, and hyperparameter tuning utilizing Scikit-learn Pipelines.",
    "NLP": "Built end-to-end Natural Language Processing (NLP) tokenization and sentiment classification pipelines analyzing 20K+ customer reviews.",
    "Docker": "Containerized multi-service application architectures using Docker and Docker Compose, standardizing local development and staging parity.",
    "Kubernetes": "Orchestrated container deployment, auto-scaling, and rolling updates across Kubernetes clusters with zero application downtime.",
    "AWS": "Architected serverless cloud workloads using AWS Lambda, S3, and RDS, lowering monthly infrastructure operational costs by 22%.",
    "Azure": "Deployed enterprise cloud infrastructure and virtual networks on Microsoft Azure with role-based access control (RBAC).",
    "CI/CD": "Constructed automated GitHub Actions CI/CD deployment pipelines, reducing release deployment cycles from 2 hours to 8 minutes.",
    "Linux": "Administered production Linux servers (Ubuntu/CentOS), configuring systemd background daemons, security firewalls, and shell scripts."
}


def generate_recommendations(target_role: str,
                             role_match: dict,
                             contact_info: dict,
                             sections: dict,
                             metrics: dict,
                             impact_info: dict,
                             detected_skills: list,
                             job_roles: dict) -> dict:
    """Generates structured suggestions and tailored bullet point examples."""
    role_recommendations = []
    structural_recommendations = []
    impact_recommendations = []
    formatting_recommendations = []
    tailored_examples = []

    ats_score = role_match["ats_score"]
    missing_skills = role_match["missing_skills"]

    # Role Keyword Gap Recommendations
    if target_role and target_role in job_roles:
        if missing_skills:
            role_recommendations.append(
                f"Missing critical technical keywords for {target_role}: {', '.join(missing_skills)}. Integrate these tools into project and experience bullet points."
            )
        if ats_score < 50:
            role_recommendations.append(
                f"Low target keyword alignment ({ats_score}%). ATS parsers typically filter resumes below 60-70% match thresholds for {target_role} postings."
            )
        elif ats_score >= 75:
            role_recommendations.append(
                f"High target keyword alignment ({ats_score}%). Contextualize these tools with measurable project outcomes and architecture details."
            )

        for ms in missing_skills[:3]:
            if ms in SAMPLE_BULLET_POINTS:
                tailored_examples.append({
                    "skill": ms,
                    "example": SAMPLE_BULLET_POINTS[ms]
                })

    # Structural Integrity Recommendations
    if not contact_info["email_found"]:
        structural_recommendations.append("Missing email address. Standard ATS parsers require an identifiable email address in the header.")
    if not contact_info["phone_found"]:
        structural_recommendations.append("Missing contact telephone number. Provide a standard format contact number.")
    if not (contact_info["linkedin_found"] or contact_info["github_found"]):
        structural_recommendations.append("Missing professional portfolio links. Include active URLs for GitHub and LinkedIn.")

    if not sections.get("Education"):
        structural_recommendations.append("Missing explicit Education heading. Standardize section title to 'Education' to ensure parser indexing.")
    if not sections.get("Skills"):
        structural_recommendations.append("Missing dedicated Technical Skills section. Create a distinct section titled 'Technical Skills' with categorized tools.")
    if not sections.get("Projects"):
        structural_recommendations.append("Missing Projects section. Include at least 2 relevant technical projects with technology stack details.")
    if not sections.get("Experience"):
        structural_recommendations.append("Missing Work Experience / Internship section. Detail roles with employment dates, organization name, and responsibilities.")
    if not sections.get("Certifications"):
        structural_recommendations.append("Missing Certifications. Add verified industry credentials or professional coursework to strengthen qualification proof.")

    # Impact & Action Verbs Recommendations
    if impact_info["action_verbs_count"] < 5:
        impact_recommendations.append(
            f"Low action verb frequency ({impact_info['action_verbs_count']} detected). Start technical bullet points with strong action verbs (e.g., 'Engineered', 'Architected', 'Optimized', 'Deployed') instead of passive phrases like 'worked on' or 'responsible for'."
        )
    if impact_info["metric_count"] < 2:
        impact_recommendations.append(
            "Low quantifiable achievement metrics detected. Integrate numerical measurements (percentages, latency cuts, throughput, user volumes) using the Google X-Y-Z formula."
        )

    # Formatting & Document Volume Recommendations
    word_count = metrics["word_count"]
    if word_count < 250:
        formatting_recommendations.append(f"Resume text is short ({word_count} words). Recommended entry-to-mid-level resume length is 350-650 words.")
    elif word_count > 900:
        formatting_recommendations.append(f"Resume text is lengthy ({word_count} words). Keep non-executive technical resumes concise (under 800 words).")

    if len(detected_skills) < 4:
        formatting_recommendations.append("Low overall technical keyword density. List core languages, frameworks, databases, and deployment platforms explicitly.")

    all_feedback = role_recommendations + structural_recommendations + impact_recommendations + formatting_recommendations
    if not all_feedback:
        all_feedback.append("Document fulfills standard ATS parsing parameters and contains expected section architecture.")

    return {
        "all_feedback": all_feedback,
        "role_recommendations": role_recommendations,
        "structural_recommendations": structural_recommendations,
        "impact_recommendations": impact_recommendations,
        "formatting_recommendations": formatting_recommendations,
        "tailored_examples": tailored_examples
    }
