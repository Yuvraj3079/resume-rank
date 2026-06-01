def build_recruiter_prompt(resume, jd):

    return f"""
    You are a senior technical recruiter.

    Analyze this candidate against the role.

    Evaluate:

    - Technical alignment
    - Missing capabilities
    - ATS compatibility
    - Hiring confidence
    - Potential interview concerns

    Resume Skills:
    {resume.skills}

    Experience:
    {[exp.role for exp in resume.experience]}

    Required Skills:
    {jd.required_skills}

    Preferred Skills:
    {jd.preferred_skills}

    Return ONLY valid JSON.

    {{

        "recruiter_summary": "...",

        "hire_recommendation": "...",

        "confidence_level": "...",

        "ats_risk": "...",

        "technical_gaps": ["..."],

        "recruiter_questions": ["..."]
    }}
    """