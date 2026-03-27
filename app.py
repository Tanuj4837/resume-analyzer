import streamlit as st
from utils import extract_text, analyze_resume, generate_feedback

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer (ATS Optimizer)")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    text = extract_text(uploaded_file)

    st.subheader("📌 Extracted Resume Text")
    st.write(text[:1000])

    score, keywords = analyze_resume(text)

    st.subheader("📊 ATS Score")
    st.progress(score)
    st.write(f"Score: {score}%")

    st.subheader("🔍 Detected Keywords")
    st.write(keywords)

    st.subheader("💡 AI Suggestions")
    feedback = generate_feedback(text)
    st.write(feedback)
