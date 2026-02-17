import streamlit as st
import tempfile

from src.parser import extract_text
from src.preprocess import preprocess
from src.scorer import compute_match_analysis

st.set_page_config(page_title="Resume Match Scorer", layout="centered")

st.title("📄 Job Application Resume Match Scorer")

resume_file = st.file_uploader("Upload Resume (PDF or TXT)", type=["pdf", "txt"])

st.header("Upload OR Type Job Description")

jd_file = st.file_uploader("Upload Job Description (PDF or TXT)", type=["pdf", "txt"])

jd_text_input = st.text_area("Or type/paste Job Description here", height=200)


if st.button("Calculate Match Score"):

    if resume_file is None:
        st.warning("Please upload resume.")
    elif jd_file is None and jd_text_input.strip() == "":
        st.warning("Upload or type job description.")
    else:

        # Save resume temp
        with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_resume:
            tmp_resume.write(resume_file.read())
            resume_path = tmp_resume.name

        resume_raw = extract_text(resume_path)
        resume_processed = preprocess(resume_raw)

        # Job Description processing
        if jd_file is not None:
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp_jd:
                tmp_jd.write(jd_file.read())
                jd_path = tmp_jd.name

            jd_raw = extract_text(jd_path)
        else:
            jd_raw = jd_text_input

        jd_processed = preprocess(jd_raw)

        # 🔥 CORRECT WAY (NO result["score"])
        score, explanation, matched_keywords, missing_keywords = compute_match_analysis(
            resume_processed, jd_processed
        )

        st.subheader("📊 Match Score")
        st.success(f"{score}%")

        st.subheader("🧠 Why this Score?")
        st.info(explanation)

        st.subheader("✅ Matching Skills")
        for word in matched_keywords:
            st.write(f"- {word}")

        st.subheader("❌ Missing Skills")
        for word in missing_keywords:
            st.write(f"- {word}")
