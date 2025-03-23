from fastapi import FastAPI, File, UploadFile, Form
import pdfplumber
import docx
from langchain_community.chat_models import ChatOpenAI
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

from langchain.schema import HumanMessage
import os

load_dotenv()

app = FastAPI()


llm = ChatOpenAI(openai_api_key=os.getenv("OPENAI_API_KEY"), model="gpt-4")


def extract_text_from_resume(file):
    """Extracts text from PDF or DOCX resumes."""
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            return "\n".join([page.extract_text() for page in pdf.pages if page.extract_text()])
    elif file.filename.endswith(".docx"):
        doc = docx.Document(file.file)
        return "\n".join([para.text for para in doc.paragraphs])
    return ""

@app.post("/analyze_resume")
async def analyze_resume(resume: UploadFile = File(...)):
    """Processes resume and provides AI insights."""
    resume_text = extract_text_from_resume(resume)
    
    response =llm.invoke([
        HumanMessage(content=f"Analyze this resume. Provide strengths, weaknesses, and missing sections:\n\n{resume_text}")
    ])
    
    return {"resume_analysis": response.content}

@app.post("/match_job")
async def match_job(resume_text: str = Form(...), job_desc: str = Form(...)):
    """Compares resume with job description and gives match score."""
    response = llm([
        HumanMessage(content=f"Compare this resume:\n{resume_text}\nWith this job description:\n{job_desc}\nProvide a match percentage and missing keywords.")
    ])
    
    return {"match_score": response.content}

@app.post("/generate_cover_letter")
async def generate_cover_letter(resume_text: str = Form(...), job_desc: str = Form(...)):
    """Generates a cover letter based on resume and job description."""
    response = llm.invoke([
    {"role": "system", "content": "Analyze the resume..."},
    {"role": "user", "content": resume_text}
])
    
    return {"cover_letter": response.content}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
