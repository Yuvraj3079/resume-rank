from pydantic import BaseModel
from typing import List

class Experience(BaseModel):
    company: str
    role: str

class ResumeData(BaseModel):
    name: str
    skills: List[str]
    experience: List[Experience]
