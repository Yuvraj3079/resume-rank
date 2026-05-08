from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ResumeRank API running"}