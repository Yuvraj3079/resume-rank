from openai import OpenAI
import json

from app.models import JobDescription
from app.core.config import OPENAI_API_KEY, OPENAI_MODEL
from app.logger import logger

client = OpenAI(
    api_key=OPENAI_API_KEY
)

SYSTEM_PROMPT = """
You are an expert ATS job description parser.

Extract structured job description data from raw job posting text.

Return ONLY valid JSON.

Use EXACTLY this schema:

{
  "title": "string",
  "required_skills": ["skill1", "skill2"],
  "preferred_skills": ["skill1", "skill2"]
}

Rules:
- Extract only real skills, tools, technologies, frameworks, platforms, methodologies, or role-relevant capabilities.
- Do not include soft filler like "team player", "communication", or "fast-paced environment" unless clearly listed as a requirement.
- Normalize skill names.
- Remove duplicates.
- Keep skill names concise.
- If the title is unclear, infer the most likely role title.
- Put must-have skills in required_skills.
- Put nice-to-have skills in preferred_skills.
- Return valid JSON only.

Normalization examples:
- reactjs → React
- nodejs → Node.js
- amazon web services → AWS
- postgres → PostgreSQL
- ci cd → CI/CD
"""

def extract_job_description(jd_text: str):
    try:
        logger.info("Starting job description extraction")

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": jd_text
                }
            ],
            temperature=0.2
        )

        content = response.choices[0].message.content
        data = json.loads(content)

        validated_data = JobDescription(**data)

        logger.info("Job description extraction completed")

        return validated_data

    except Exception as e:
        logger.error(f"Job description extraction failed: {e}")

        return JobDescription(
            title="Unknown Role",
            required_skills=[],
            preferred_skills=[]
        )