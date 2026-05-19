from openai import OpenAI # type: ignore
import os
import json

client = OpenAI(
    api_key = os.getenv("OPENAI_API_KEY")
)

def generate_ai_insights(resume, jd, matched_skills, missing_skills):
    prompt = f"""
        You are an expert technical recruiter
        and resume strategist.

        Analyze this candidate against
        the target role.

        Resume Skills:
        {resume.skills}

        Experience:
        {resume.experience}

        Target Role:
        {jd.title}

        Required Skills:
        {jd.required_skills}

        Missing Skills:
        {missing_skills}

        Matched Skills:
        {matched_skills}

        Tasks:

        1. Generate 3 strong rewritten
        resume bullets tailored toward
        the target role.

        2. Generate 3 interview risks
        the candidate may face.

        3. Generate 3 improvement suggestions.

        Rules:
        - Be realistic
        - Do NOT invent fake experience
        - Do NOT invent fake technologies
        - Keep outputs concise
        - Sound like a real recruiter

        Return ONLY valid JSON.

        JSON format:

        {{
        "rewritten_bullets": [],
        "interview_risks": [],
        "improvement_suggestions": []
        }}
        """
        
    response = client.chat.completions.create(
        model ="gpt-4o-mini",
        response_format={"type": "json_object"},
        messages = [
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature = 0.4
    )
    content = response.choices[0].message.content
    
    try:
        parsed = json.loads(content)
    except Exception:
        parsed = {
        "rewritten_bullets": [],
        "interview_risks": [],
        "improvement_suggestions": []
        }
    return parsed
