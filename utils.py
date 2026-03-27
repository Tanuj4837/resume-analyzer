import PyPDF2
import re

# --- Extract text ---
def extract_text(file):
    text = ""
    try:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            content = page.extract_text()
            if content:
                text += content
    except:
        return ""
    return text


# --- ATS scoring ---
def analyze_resume(text):
    keywords = [
        "python", "machine learning", "nlp", "data",
        "project", "api", "sql", "react", "llm",
        "deep learning", "pandas", "tensorflow"
    ]

    text = text.lower()

    found = [k for k in keywords if k in text]

    score = int((len(found) / len(keywords)) * 100)
    return score, found


# --- Smart feedback (AI-like logic) ---
def generate_feedback(text):
    text = text.lower()
    feedback = []

    # Section checks
    if "project" not in text:
        feedback.append("Add project experience to showcase practical skills")

    if "experience" not in text:
        feedback.append("Include internship or work experience")

    if "github" not in text:
        feedback.append("Add GitHub profile link for credibility")

    if "%" not in text:
        feedback.append("Include quantified achievements (e.g., improved performance by 30%)")

    # Skill checks
    if "machine learning" not in text and "ai" not in text:
        feedback.append("Include AI/ML related keywords if relevant")

    if "sql" not in text:
        feedback.append("Add database-related skills like SQL")

    # fallback (ensure at least 3)
    extra = [
        "Use strong action verbs like Developed, Built, Implemented",
        "Improve formatting and structure for readability",
        "Tailor resume according to job description"
    ]

    feedback.extend(extra)

    return feedback[:3]
