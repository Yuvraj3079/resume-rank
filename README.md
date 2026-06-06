**AI Resume Intelligence Platform**

An AI-powered resume intelligence and candidate evaluation platform built with FastAPI, React, OpenAI, Sentence Transformers, and ChromaDB.

**Overview**

This project allows users to upload a resume PDF, paste a full job description, and evaluate candidate-job fit in one click. The system extracts structured resume data, parses job descriptions, calculates ATS-style scores, performs semantic similarity matching, generates recruiter-style hiring insights, identifies skill gaps, and produces AI-powered resume improvement suggestions.

**Features**

- Resume PDF upload and text extraction
- AI-powered resume parsing
- LinkedIn job description parsing
- One-click candidate evaluation
- ATS-style scoring
- Semantic similarity scoring using Sentence Transformers
- Recruiter-style AI analysis
- Skill gap detection
- Interview risk generation
- AI resume rewrite suggestions
- ChromaDB vector storage
- Duplicate resume detection
- React dashboard with reusable components

**Tech Stack**

    **Backend**
      - FastAPI
      - Python
      - OpenAI API
      - Sentence Transformers
      - ChromaDB
      - Pydantic
      - Loguru

    **Frontend**
      - React
      - Vite
      - Tailwind CSS
      - LocalStorage

**Architecture**

Resume PDF Upload
        ↓
PDF Text Extraction
        ↓
AI Resume Parser
        ↓
Structured Resume Data
        ↓
LinkedIn Job Description Parser
        ↓
Deterministic Scoring + Semantic Similarity
        ↓
Recruiter AI Analysis
        ↓
AI Resume Rewrite Suggestions
        ↓
ChromaDB Vector Storage
        ↓
React Dashboard

**Setup**

**1. Clone the repository**

        gh repo clone Yuvraj3079/resume-rank
        cd resume-rank

**2. Backend setup**
        cd backend
        python -m venv ../.venv
        source ../.venv/Scripts/activate
        pip install -r requirements.txt

        Create a .env file inside the backend folder:
        OPENAI_API_KEY=your_openai_api_key_here

        Start the backend server:

        python -m uvicorn app.main:app --reload

        Backend will run at: http://127.0.0.1:8000

        API docs: http://127.0.0.1:8000/docs

**3. Frontend setup**

        Open a new terminal:

        cd frontend
        npm install
        npm run dev

        Frontend will run at: http://localhost:5173

**4. Usage**

Upload a resume PDF.
Paste a full job description.
Click **Evaluate Candidate**.
View the candidate score, skill gaps, recruiter summary, interview risks, and AI rewrite suggestions.