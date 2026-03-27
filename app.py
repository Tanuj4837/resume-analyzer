import streamlit as st
from utils import extract_text, analyze_resume, generate_feedback

st.set_page_config(page_title="AI Resume Analyzer")

st.title("📄 AI Resume Analyzer (ATS + AI Feedback)")

uploaded_file = st.file_uploader("Upload your Resume (PDF)", type=["pdf"])

if uploaded_file:
    try:
        with st.spinner("Processing resume..."):
            text = extract_text(uploaded_file)

        if not text or not text.strip():
            st.error("❌ Could not extract text from PDF. Try another file.")
        else:
            st.subheader("📌 Resume Preview")
            st.write(text[:800])

            score, keywords = analyze_resume(text)

            st.subheader("📊 ATS Score")
            st.progress(int(score))   # ✅ fixed
            st.write(f"{score}% Match")

            st.subheader("🔍 Keywords Found")
            st.write(", ".join(keywords) if keywords else "None")

            st.subheader("🤖 AI Suggestions")
            feedback = generate_feedback(text)

            for f in feedback:
                st.write(f"• {f}")

    except Exception as e:
        st.error("⚠️ Something went wrong while processing the file.")
