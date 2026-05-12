from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.evaluate import router as evaluate_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(evaluate_router)

@app.get("/")
def root():
    return {"message": "ResumeRank API running"}