from fastapi import APIRouter 
from app.models import ResumeData, JobDescription
from app.models import EvaluationRequest
from app.services.comparator import compare_resume_to_jb

router = APIRouter()

@router.post("/evaluate")
async def evaluate_resume(request: EvaluationRequest):
    return compare_resume_to_jb(
    request.resume,
    request.jd
)