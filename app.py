import streamlit as st
import fitz  # PyMuPDF
import os
import json
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(page_title="Resume Screener & Fit Analyzer", layout="centered")

st.title("📄 Resume Screener & Fit Analyzer")
st.write("Upload a resume and paste the job description to get a fit score, matched/missing skills, and a recommendation.")

# --- Upload Resume PDF ---
uploaded_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description", height=200)

# --- Extract Resume Text ---
def extract_text_from_pdf(uploaded_file):
    with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
        text = ""
        for page in doc:
            text += page.get_text()
    return text

# --- Analyze using GPT ---
def analyze_resume(resume_text, job_description):
    prompt = f"""
You are a recruitment assistant AI. Given the job description and resume, perform the following:
1. Fit Score (0 to 100)
2. Key Skills Matched
3. Key Skills Missing
4. Summary Recommendation

Job Description:
{job_description}

Resume:
{resume_text}

Return output as JSON in this format:
{{
  "fit_score": 85,
  "matched_skills": ["Python", "Data Analysis"],
  "missing_skills": ["Leadership", "Project Management"],
  "recommendation": "The candidate is a strong fit but lacks experience in leadership roles."
}}
"""
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800
    )
    return json.loads(response.choices[0].message.content)

# --- Main logic ---
if st.button("🔍 Analyze Resume"):
    if not uploaded_file or not job_description:
        st.warning("Please upload a resume and paste the job description.")
    else:
        with st.spinner("Analyzing resume..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            result = analyze_resume(resume_text, job_description)

            # Color for score
            fit_score = result["fit_score"]
            color = "green" if fit_score >= 75 else "orange" if fit_score >= 50 else "red"

            st.markdown(f"""
### 📝 Resume Fit Analysis

**🔢 Fit Score:** <span style='color:{color}; font-weight:bold;'>{fit_score}%</span><br><br>

**✅ Matched Skills:**  
{', '.join(result['matched_skills'])}

**❌ Missing Skills:**  
{', '.join(result['missing_skills'])}

**📌 Recommendation:**  
> {result['recommendation']}
""", unsafe_allow_html=True)

