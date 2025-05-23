
# Resume Screener & Fit Analyzer

[Live App →](https://amnaabbasi03-resume-screener1.streamlit.app)  
*A fast, AI-powered tool to evaluate how well a resume matches a job description.*

---

## 🔍 Overview

This tool helps recruiters quickly evaluate resumes by:

- Generating a **Fit Score** (0–100)
- Highlighting **key skills matched** and **missing**
- Providing a short **AI-generated recommendation** to aid decision-making

No more manual reviews. Just upload a resume and paste the job description — and let AI do the rest.

---

## 🛠 Tech Stack

- **Frontend:** Streamlit
- **Resume Parsing:** PyMuPDF
- **AI Matching & Analysis:** OpenAI GPT API
- **Secrets Management:** `python-dotenv` / Streamlit Secrets

---

## 📸 Screenshots

![Input](https://github.com/user-attachments/assets/c568f4ae-5f52-43c6-ad47-1eca98ad3216)

*Input section: Upload a resume & job description*

![Output](https://github.com/user-attachments/assets/d77dcff5-accb-45d7-8287-8913528abbbf)

*Output: Fit Score, Skill Match Summary, and Recommendation*

---

## 🚀 Getting Started (Local Development)

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```

### 2. Create a `.env` file

Create a file named `.env` in the project root and add the following:

```env
OPENAI_API_KEY=your-openai-key-here
```

> 💡 You can refer to `.env.example` for guidance.

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Start the Streamlit app

```bash
streamlit run app.py
```

The app will open in your default browser.  
You can upload a resume and paste the job description in the text box and it will display:

- Fit Score 
- Matching skills
- Missing skills 
- Recommendation  

---

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own version:

1. Push this project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → "New App"
3. Set the repo, branch, and path to `app.py`
4. Add your `OPENAI_API_KEY` in **Secrets**

---

##  Use Cases

1. Screen hundreds of resumes in minutes using AI-powered job fit analysis.
2. Shortlist top candidates instantly with Fit Scores and skill matching.
3. Compare resumes against job descriptions to identify strengths and gaps.
4. Speed up hiring for staffing agencies by matching resumes to client needs.
5. Guide internal candidates by showing how well they fit new roles.
6. Optimize resumes for ATS by highlighting missing keywords (future feature).
7. Empower career coaches with AI insights for resume improvement.
8. Streamline campus recruitment with quick-fit evaluations for student resumes.

## 🙌 Contributing

Feel free to fork and improve this tool. PRs welcome!
