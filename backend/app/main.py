from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.evaluate import router as evaluate_router
from app.routers.corpus import router as corpus_router

app = FastAPI()
app.include_router(upload_router)
app.include_router(evaluate_router)
app.include_router(corpus_router)

@app.get("/")
def root():
    return {"message": "ResumeRank API running"}

@app.get("/health")
async def healtch_check():
    return {"status": "healthy"}