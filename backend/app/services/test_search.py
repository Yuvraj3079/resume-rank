from app.services.vectorscore import (search_resumes)

results = search_resumes(

    "Python FastAPI AWS engineer"
)

print(results)