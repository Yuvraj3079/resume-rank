import chromadb
from uuid import uuid4
from datetime import datetime
from app.services.embeddings import generate_embedding

client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_or_create_collection(name = "resumes")

def add_resume(resume_text: str, candidate_name: str, skills: list, experience_count: int):
    embedding = generate_embedding(resume_text)
    results = collection.query(query_embeddings = [embedding], n_results=1)
    
    if(results["distances"] and results["distances"][0] and results["distances"][0][0] < 0.05):
        return {
            "duplicate": True
        }

    resume_id = str(uuid4())
    
    collection.add(
        ids = [resume_id],
        documents = [resume_text],
        embeddings = [embedding],
        metadatas=[{
            "candidate_name": candidate_name,
            "skills": ",".join(skills),
            "experience_count": experience_count,
            "uploaded_at": str(datetime.utcnow())
        }]
    )
    return {
        "duplicate": False,
        "resume_id": resume_id
    }

def search_resumes(jd_text: str, top_k: int = 3):
    embedding = generate_embedding(jd_text)
    
    results = collection.query(
        query_embeddings = [embedding],
        n_results = top_k
    )
    return results