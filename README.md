
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

```bash
git clone https://github.com/yourusername/resume-screener.git
cd resume-screener
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

Create a `.env` file in the root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Then run the app:

```bash
streamlit run app.py
```

---

## 🌐 Deployment

This app is deployed on **Streamlit Community Cloud**. To deploy your own version:

1. Push this project to GitHub
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud) → "New App"
3. Set the repo, branch, and path to `app.py`
4. Add your `OPENAI_API_KEY` in **Secrets**

---

## 🙌 Contributing

Feel free to fork and improve this tool. PRs welcome!

---

## 📄 License

MIT License
