import chromadb
from app.services.embeddings import generate_embedding

client = chromadb.Client()
collection = client.get_or_create_collection(name = "resumes")

def add_resume(resume_id: str, resume_text: str):
    embedding = generate_embedding(resume_text)
    collection.add(
        ids = [resume_id],
        documents = [resume_text],
        embeddings = [embedding]
    )

def search_resumes(jd_text: str, top_k: int = 3):
    embedding = generate_embedding(jd_text)
    
    results = collection.query(
        query_embeddings = [embedding],
        n_results = top_k
    )
    return results