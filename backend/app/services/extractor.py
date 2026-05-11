from openai import OpenAI
from dotenv import load_dotenv
from app.models import ResumeData
import os
import json

load_dotenv()

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

SYSTEM_PROMT = """
Extract the resume into structured JSON.

Use EXACTLY this schema:

{
  "name": "string",
  "skills": ["skill1", "skill2"],
  "experience": [
    {
      "company": "string",
      "role": "string"
    }
  ]
}

IMPORTANT:
- Use the field name 'role'
- Do NOT use 'job_title'
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


