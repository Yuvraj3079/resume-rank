from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="Python FastAPI React developer"
)

embedding = response.data[0].embedding

print(len(embedding))
print(embedding[:10])