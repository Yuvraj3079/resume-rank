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
    preferred_skills: List[str]

class EvaluationResult(BaseModel):
    match_score: int
    matched_skills: List[str]
    missing_skills: List[str]
    summary: str
    improvement_suggestions: List[str]
    rewritten_bullets: List[str]
    