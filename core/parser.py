import os
from pypdf import PdfReader
from docx import Document


def extract_pdf_text(file_path: str) -> str:
    """Extracts text content from all pages of a PDF document."""
    text = []
    reader = PdfReader(file_path)
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text).strip()


def extract_docx_text(file_path: str) -> str:
    """Extracts text content from paragraphs of a DOCX document."""
    document = Document(file_path)
    text = []
    for paragraph in document.paragraphs:
        if paragraph.text.strip():
            text.append(paragraph.text.strip())
    return "\n".join(text).strip()


def extract_text_from_file(file_path: str) -> str:
    """Convenience router to extract text based on file extension."""
    ext = file_path.rsplit(".", 1)[-1].lower()
    if ext == "pdf":
        return extract_pdf_text(file_path)
    elif ext == "docx":
        return extract_docx_text(file_path)
    raise ValueError(f"Unsupported file format: .{ext}")
