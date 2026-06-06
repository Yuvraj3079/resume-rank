from fastapi import FastAPI
from app.routers.upload import router as upload_router
from app.routers.evaluate import router as evaluate_router
from app.routers.corpus import router as corpus_router
from app.routers.jd import router as jd_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(upload_router)
app.include_router(evaluate_router)
app.include_router(corpus_router)
app.include_router(jd_router)
@app.get("/")
def root():
    return {"message": "ResumeRank API running"}

@app.get("/health")
async def healtch_check():
    return {"status": "healthy"}

app.add_middleware(

    CORSMiddleware,

    allow_origins=[
        "http://localhost:5173"
    ],

    allow_credentials=True,

    allow_methods=["*"],

    allow_headers=["*"],
)