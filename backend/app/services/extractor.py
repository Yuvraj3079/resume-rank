from openai import OpenAI # type: ignore
from dotenv import load_dotenv # type: ignore
from app.models import ResumeData
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMT = """
You are an enterprise ATS resume parser.

Extract structured candidate information from the resume.

Rules:
- Return ONLY valid JSON
- Infer technical skills when appropriate
- Normalize technologies
- Remove duplicates
- Use professional naming conventions

Use EXACTLY this schema:

{
  "name": "string",

  "skills": [
    "Python",
    "FastAPI",
    "Docker"
  ],

  "experience": [
    {
      "company": "string",
      "role": "string"
    }
  ]
}

Normalization examples:
- reactjs → React
- nodejs → Node.js
- amazon web services → AWS
- postgres → PostgreSQL

IMPORTANT:
- Use field name 'role'
- Never use 'job_title'
- Return valid JSON only
"""

def extract_resume_data(resume_text: str):
    
    response = client.chat.completions.create(
        model = "gpt-4o-mini",
        response_format = {"type": "json_object"},
        messages = [
            {
                "role": "system",
                "content": SYSTEM_PROMT
            },
            {
                "role": "user",
                "content": resume_text
            }
        ]
    )    
    
    content = response.choices[0].message.content
    data = json.loads(content)
    validated_data = ResumeData(**data)
    print(validated_data.model_dump())
    return validated_data


