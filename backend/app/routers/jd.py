from fastapi import APIRouter, HTTPException

from app.models import JobDescriptionParseRequest
from app.services.jd_extractor import extract_job_description

router = APIRouter()

@router.post("/parse-jd")
async def parse_job_description(request: JobDescriptionParseRequest):
    if not request.jd_text.strip():
        raise HTTPException(
            status_code=400,
            detail="Job description text cannot be empty"
        )

    result = extract_job_description(request.jd_text)

    return result.model_dump()