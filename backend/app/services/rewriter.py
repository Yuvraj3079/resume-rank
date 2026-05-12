import json
from openai import OpenAI

from app.config import settings

client = OpenAI(api_key = settings.OPENAI_API_KEY)

def generate_rewrite_suggestions(resume_text: str, missing_skills: list[str]):
    prompt = f""" 
            You are a professional resume coach.

            The candidate is missing these skills:

            {missing_skills}

            Resume:

            {resume_text}

            Generate:
            1. Three improvement suggestions
            2. Two rewritten resume bullet points

            Return STRICT JSON only.

            Example:

            {{
                "improvement_suggestions": [
                    "...",
                    "...",
                    "..."
                ],
                "rewritten_bullets": [
                    "...",
                    "..."
                ]
            }}
            """
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.3
    )
    content = response.choices[0].message.content
    
    return json.loads(content)