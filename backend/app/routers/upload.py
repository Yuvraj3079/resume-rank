from fastapi import APIRouter, UploadFile, File, HTTPException
from pypdf import PdfReader
from io import BytesIO
from app.logger import logger
from app.services.extractor import extract_resume_data

router = APIRouter()

MAX_FILE_SIZE = 5 * 1024 * 1024

@router.post("/upload")
async def upload_resume(file: UploadFile = File(...)):
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF resumes are allowed"
        )
    
    content = await file.read()
    
    if len(content) > MAX_FILE_SIZE:
        raise HTTPException(
            status_code=400,
            detail="File more than 5MB"
        )
    if len(content) == 0:
        raise HTTPException(
            status_code=400,
            detail="Empty file uploaded"
        )
    #logger.info(content)
    try:
        pdf = PdfReader(BytesIO(content))
        extracted_text = ""
        
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                extracted_text += page_text + "\n"
        
        extracted_text = " ".join(extracted_text.split())
        return {
            "filename": file.filename,
            "content": extracted_text
        }
    except Exception as e:
        logger.info(e)
        raise HTTPException(
            status_code=400,
            detail="Failed to parse PDF"
        ) 
