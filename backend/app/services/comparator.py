from app.models import ResumeData, JobDescription, EvaluationResult
from app.services.rewriter import generate_rewrite_suggestions

def compare_resume_to_jb(resume: ResumeData, jd: JobDescription):
    resume_skills = set(skill.lower() for skill in resume.skills)
    required_skills = set(skill.lower() for skill in jd.required_skills)
    matched_skills = list(resume_skills.intersection(required_skills))
    missing_skills = list(required_skills - resume_skills)
    #check if the LLM is providing a valid response
    if len(required_skills) == 0:
        score = 0
    else:
        score = int(len(matched_skills) / len(required_skills) * 100)
    
    #print(f"Score: {score}", flush=True)
    rewrite_data = generate_rewrite_suggestions(resume_text=str(resume), missing_skills=missing_skills)
    
    return EvaluationResult(match_score = score,
                            matched_skills = matched_skills,
                            missing_skills = missing_skills,
                            summary = f"Candidate matches {len(matched_skills)} out of {len(required_skills)} required skills",
                            improvement_suggestions = rewrite_data["improvement_suggestions"],
                            rewritten_bullets = rewrite_data["rewritten_bullets"])
    
    
    