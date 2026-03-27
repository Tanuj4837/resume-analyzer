import PyPDF2
import re
import random

# --- Extract text from PDF ---
def extract_text(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


# --- Simple ATS scoring ---
def analyze_resume(text):
    keywords = [
        "python", "machine learning", "nlp", "data",
        "project", "api", "sql", "react", "llm"
    ]

    found = []
    score = 0

    for word in keywords:
        if re.search(word, text.lower()):
            found.append(word)
            score += 10

    score = min(score, 100)
    return score, found


# --- Fake AI feedback (replace with API later) ---
def generate_feedback(text):
    suggestions = [
        "Add more quantified achievements (e.g., improved performance by 30%)",
        "Include more AI/ML related keywords",
        "Improve project descriptions with impact",
        "Add GitHub links for credibility",
        "Use action verbs like Developed, Built, Implemented"
    ]
    return random.sample(suggestions, 3)
