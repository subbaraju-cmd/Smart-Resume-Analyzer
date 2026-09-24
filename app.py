import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

from core import (
    analyze_resume,
    load_job_roles,
    extract_pdf_text,
    extract_docx_text
)

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"pdf", "docx"}

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def home():
    job_roles = list(load_job_roles().keys())
    return render_template("index.html", job_roles=job_roles)


@app.route("/upload", methods=["POST"])
def upload_resume():
    job_roles = list(load_job_roles().keys())
    job_role = request.form.get("job_role", "").strip()

    if not job_role:
        return render_template(
            "index.html",
            job_roles=job_roles,
            error="Please select a target job role before analyzing."
        ), 400

    if "resume" not in request.files:
        return render_template(
            "index.html",
            job_roles=job_roles,
            error="Please select a resume file (PDF or DOCX)."
        ), 400

    file = request.files["resume"]

    if not file or file.filename == "":
        return render_template(
            "index.html",
            job_roles=job_roles,
            error="No resume file was selected. Please choose a file."
        ), 400

    if not allowed_file(file.filename):
        return render_template(
            "index.html",
            job_roles=job_roles,
            error="Unsupported file format. Please upload a PDF or DOCX document."
        ), 400

    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(file_path)

    try:
        extension = filename.rsplit(".", 1)[1].lower()
        if extension == "pdf":
            resume_text = extract_pdf_text(file_path)
        else:
            resume_text = extract_docx_text(file_path)
    except Exception as e:
        return render_template(
            "index.html",
            job_roles=job_roles,
            error=f"Error reading document: {e}"
        ), 500

    if not resume_text or not resume_text.strip():
        return render_template(
            "index.html",
            job_roles=job_roles,
            error="Document uploaded successfully, but no text could be extracted. Please ensure the document is not a scanned image or photo."
        ), 400

    # Master ATS Resume Analysis
    analysis = analyze_resume(resume_text, target_role=job_role)

    return render_template(
        "result.html",
        filename=filename,
        resume_text=resume_text,
        analysis=analysis,
        job_role=job_role
    )


if __name__ == "__main__":
    app.run(debug=True)