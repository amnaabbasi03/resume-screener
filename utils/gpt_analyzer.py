import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load .env file
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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

    Return output in this format:
    Fit Score: XX
    Matched Skills: ...
    Missing Skills: ...
    Recommendation: ...
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=800,
    )
    return response.choices[0].message.content

