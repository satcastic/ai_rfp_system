import fitz
import pandas as pd
from docx import Document
import os


def parse_pdf(file_path):

    text = ""
    pdf = fitz.open(file_path)

    for page_number, page in enumerate(pdf):

        page_text = page.get_text()

        text += page_text

    return text


def parse_docx(file_path):

    doc = Document(file_path)

    text = []

    for paragraph in doc.paragraphs:
        text.append(paragraph.text)

    return "\n".join(text)


def parse_excel(file_path):

    df = pd.read_excel(file_path)

    return df.to_string()


def parse_text(file_path):

    with open(file_path, "r") as f:
        return f.read()


def parse_document(file_path):

    extension = os.path.splitext(file_path)[1].lower()

    if extension == ".pdf":
        content = parse_pdf(file_path)
        doc_type = "pdf"

    elif extension == ".docx":
        content = parse_docx(file_path)
        doc_type = "docx"

    elif extension in [".xls", ".xlsx"]:
        content = parse_excel(file_path)
        doc_type = "excel"

    elif extension == ".txt":
        content = parse_text(file_path)
        doc_type = "text"

    else:
        raise ValueError(f"Unsupported file type: {extension}")

    return {
        "source_file": os.path.basename(file_path),
        "document_type": doc_type,
        "content": content
    }