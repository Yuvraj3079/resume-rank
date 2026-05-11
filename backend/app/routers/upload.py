from fastapi import APIRouter, UploadFile
from pypdf import PdfReader
from io import BytesIO

from app.services.extractor import extract_resume_data

router = APIRouter()

@router.post("/upload")
async def upload_resume(file: UploadFile):
    contents = await file.read()
    print("upload working")
    reader = PdfReader(BytesIO(contents))
    text = ""
    
    for page in reader.pages:
        text += page.extract_text()
    
    extracted_data = extract_resume_data(text)
    
    return extracted_data
    