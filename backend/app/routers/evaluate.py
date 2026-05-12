from fastapi import APIRouter 
from app.models import ResumeData, JobDescription
from app.services.comparator import compare_resume_to_jb

router = APIRouter()

@router.post("/evaluate")
async def evaluate_resume(resume: ResumeData, jd: JobDescription):
    result = compare_resume_to_jb(resume, jd)
    return result