import streamlit as st
import requests
import io

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.title("📄 Smart AI Resume Analyzer")
st.write("Upload your resume, and AI will analyze it for strengths, weaknesses, and missing sections!")

uploaded_file = st.file_uploader("Upload your resume (PDF/DOCX)", type=["pdf", "docx"])

if uploaded_file:
    with st.spinner("Analyzing your resume... ⏳"):
        files = {"resume": uploaded_file}
        response = requests.post(f"{API_URL}/analyze_resume", files=files)
        analysis = response.json().get("resume_analysis", "Error processing resume.")

    st.subheader("📊 Resume Analysis")
    st.markdown(f"<div style='background:#E3E6F3;padding:10px;border-left:5px solid #2D336B;'>{analysis}</div>", unsafe_allow_html=True)

st.subheader("🎯 Job Match Evaluation")
resume_text = st.text_area("Paste your resume text here:")
job_desc = st.text_area("Paste the job description here:")

if st.button("Evaluate Job Match"):
    with st.spinner("Matching your resume with the job description... ⏳"):
        data = {"resume_text": resume_text, "job_desc": job_desc}
        response = requests.post(f"{API_URL}/match_job", data=data)
        match_score = response.json().get("match_score", "Error processing match.")

    st.markdown(f"<div style='background:#E3E6F3;padding:10px;border-left:5px solid #2D336B;'>{match_score}</div>", unsafe_allow_html=True)

st.subheader("📧 AI Cover Letter Generator")

if st.button("Generate Cover Letter"):
    with st.spinner("Generating AI-powered cover letter... ⏳"):
        data = {"resume_text": resume_text, "job_desc": job_desc}
        response = requests.post(f"{API_URL}/generate_cover_letter", data=data)
        cover_letter = response.json().get("cover_letter", "Error generating cover letter.")

    st.markdown(f"<div style='background:#E3E6F3;padding:10px;border-left:5px solid #2D336B;'>{cover_letter}</div>", unsafe_allow_html=True)
