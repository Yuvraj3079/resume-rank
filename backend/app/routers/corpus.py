from fastapi import APIRouter
from fastapi import Query

from app.services.vectorscore import (add_resume, search_resumes)

router = APIRouter()

@router.post("/corpus/add")
async def add_resume_to_corpus():

    sample_resumes = [

        (
            "resume_1",
            """
            Python backend developer with FastAPI,
            Docker, PostgreSQL, and REST API experience.
            """
        ),

        (
            "resume_2",
            """
            Frontend React engineer focused on UI/UX,
            Tailwind CSS, and responsive design.
            """
        ),

        (
            "resume_3",
            """
            DevOps engineer experienced in AWS,
            Kubernetes, CI/CD pipelines, and cloud infrastructure.
            """
        ),

        (
            "resume_4",
            """
            Software engineer skilled in backend APIs,
            database optimization, and scalable systems.
            """
        ),

        (
            "resume_5",
            """
            Data analyst with expertise in Excel,
            Power BI, SQL, and dashboards.
            """
        )
    ]

    for resume_id, resume_text in sample_resumes:

        add_resume(
            resume_id,
            resume_text
        )

    return {
        "message": "All resumes added"
    }

@router.get("/corpus/search")
async def search_corpus(jd : str = Query(...)):

    

    results = search_resumes(jd)

    return results
     