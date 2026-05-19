from openai import OpenAI
from app.models import ResumeData, JobDescription
import os
import json
from app.core.config import (OPENAI_API_KEY, OPENAI_MODEL)
from app.logger import logger
from app.prompts.recruiter_prompt import (build_recruiter_prompt)

#print(OPENAI_API_KEY)
#client = OpenAI( api_key=os.getenv("OPENAI_API_KEY"))
client = OpenAI(
    api_key=OPENAI_API_KEY
)

def generate_recruiter_analysis(resume: ResumeData, jd: JobDescription):
    try:
        logger.info("Starting recruiter analysis")
        prompt = build_recruiter_prompt(resume, jd)

        response = client.chat.completions.create(
            model=OPENAI_MODEL,
            response_format={"type": "json_object"},
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.4
        )

        content = response.choices[0].message.content
        logger.info("Recruiter analysis completed")
        
        try:
            return json.loads(content)

        except Exception :
            return {
                "recruiter_summary":
                    "Unable to generate recruiter analysis.",

                "hire_recommendation":
                    "Unknown",

                "confidence_level":
                    "Low",

                "ats_risk":
                    "Unknown",

                "technical_gaps": [],

                "recruiter_questions": []
            }
    except Exception as e:
        logger.error(f"Recruiter analysis failed: {e}")
        return {
            "recruiter_summary":
                "Analysis unavailable.",

            "hire_recommendation":
                "Unknown",

            "confidence_level":
                "Low",

            "ats_risk":
                "Unknown",

            "technical_gaps": [],

            "recruiter_questions": []
        }