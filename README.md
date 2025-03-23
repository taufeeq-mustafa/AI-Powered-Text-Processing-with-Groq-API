# 🚀 AI-Powered Text Processing with Groq API

## Overview
The AI Resume Analyzer is a Python-based web application built with Streamlit and FastAPI. It leverages Groq’s AI model (GPT-4) to analyze resumes, assess job fit, and generate AI-powered cover letters. This tool helps job seekers improve their resumes by highlighting strengths, identifying weaknesses, and ensuring alignment with job descriptions.

The application provides:

* Resume Analysis – AI-driven insights on strengths, weaknesses, and missing sections.

* Job Match Evaluation – Compares a resume with a job description and provides a match percentage.

* AI Cover Letter Generation – Creates a tailored cover letter based on the resume and job description.

## Features

* AI-Powered Resume Analysis – Extracts key insights from PDF/DOCX resumes. 
* Job Match Scoring – Provides a match percentage and missing keywords for job descriptions.
* Cover Letter Generator – Automatically generates a personalized cover letter.
* Streamlit UI – A simple and user-friendly web interface for seamless interaction.
* FastAPI Backend – Efficient API for processing resumes and generating insights.
* Secure API Communication – Ensures data privacy with secure API handling.
* Secure API Communication – Ensures safe and encrypted requests to GROQ API.


## Project Structure
```
├── .env               # API Key 
├── app.py             # Streamlit Frontend   
├── backend.py         # Backend            
├── README.md          #Readme file
├── requirements.txt   # Project Requirements
```


## Setup Instructions

### Prerequisites

Ensure you have:
* Python 3.8+ installed.
* A valid GROQ API Key ([Get from here](https://console.groq.com/keys)).

### Clone Repository
```
git clone <https://github.com/taufeeq-mustafa/Smart-AI-Resume-Analyzer>
cd groq-text-summarizer
```
### Create & Activate a Virtual Environment
```
python -m venv venv  
venv\Scripts\activate  
```

### Install Dependancies
```
pip install -r requirements.txt
```
### Run the application
For Backend 
```
 python -m uvicorn backend:app --reload
```
For Streamlit
```
python -m streamlit run app.py
```




    
## License

[MIT](https://choosealicense.com/licenses/mit/)

