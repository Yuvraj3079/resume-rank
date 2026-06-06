from pydantic import BaseModel
from typing import List

class Experience(BaseModel):
    company: str
    role: str

class ResumeData(BaseModel):
    name: str
    skills: List[str]
    experience: List[Experience]
    
class JobDescription(BaseModel):
    title: str
    required_skills: List[str]
    preferred_skills: List[str] = []

class EvaluationRequest(BaseModel):
    resume: ResumeData
    jd: JobDescription
    
class EvaluationResult(BaseModel):
    overall_score: int
    
    skills_score: int
    experience_score: int
    semantic_score: int
    
    matched_skills: List[str]
    
    missing_critical_skills: List[str]
    missing_secondary_skills: List[str]
    
    strengths: List[str]
    weaknesses: List[str]
    
    interview_risks: List[str]
    
    improvement_suggestions: List[str]
    rewritten_bullets: List[str]
    
    

class RecruiterAnalysis(BaseModel):
    #Recruiter Analysis
    recruiter_summary: str
    hire_recommendation: str
    confidence_level: str
    ats_risk: str
    technical_gaps: List[str]
    recruiter_questions: List[str]
class JobDescriptionParseRequest(BaseModel):
    jd_text: str