from app.models import ResumeData, JobDescription, EvaluationResult
from app.services.rewriter import generate_rewrite_suggestions
from app.logger import logger
from sentence_transformers import util
from app.services.embeddings import generate_embedding
from app.services.ai_enhancer import (generate_ai_insights)

def compare_resume_to_jb(resume: ResumeData, jd: JobDescription):
    
    resume_text = " ".join(resume.skills)
    
    jd_text = " ".join(
        jd.required_skills + jd.preferred_skills
    )
    
    resume_embedding = generate_embedding(resume_text)
    jd_embedding = generate_embedding(jd_text)
    
    semantic_similarity = util.cos_sim(resume_embedding, jd_embedding)
    
    semantic_score = int(semantic_similarity.item() * 100)
    logger.info(f"Semantic Score: {semantic_score}")
    
    resume_skills = set(skill.lower() for skill in resume.skills)
    required_skills = set(skill.lower() for skill in jd.required_skills)
    matched_skills = sorted( list(resume_skills.intersection(required_skills)))    
    
    if len(required_skills) == 0:
        skills_score = 0
    else:
        skills_score = int((len(matched_skills) / len(required_skills)) * 100 )
    
    experience_score = min(len(resume.experience) * 20,100)
    
    overall_score = max(0,
        min(
            int(
                skills_score * 0.5 +
                semantic_score * 0.3 +
                experience_score * 0.2
            ), 100 )
        )
    
    missing_critical_skills = []

    for skill in jd.required_skills:

        if skill.lower() not in resume_skills:

            missing_critical_skills.append(skill)
    
    missing_secondary_skills = []

    for skill in jd.preferred_skills:

        if skill.lower() not in resume_skills:

            missing_secondary_skills.append(skill)

    weaknesses = []
    
    if len(missing_critical_skills) > 2:

        weaknesses.append(
            "Missing several required technical skills."
        )

    if semantic_score < 60:

        weaknesses.append(
            "Resume language does not strongly align with the job description."
        )

    strengths = []
    if skills_score > 70:

        strengths.append(
            "Strong alignment with required technical stack."
        )

    if semantic_score > 75:

        strengths.append(
            "Resume language closely matches the role requirements."
        )
        
    ai_results = generate_ai_insights(resume, jd, matched_skills, missing_critical_skills)
    logger.info(f"AI results: {ai_results}")
    
    return EvaluationResult(

        overall_score = overall_score,

        skills_score = skills_score,
        experience_score = experience_score,
        semantic_score = semantic_score,

        matched_skills = matched_skills,

        missing_critical_skills = missing_critical_skills,

        missing_secondary_skills = missing_secondary_skills,

        strengths = strengths,
        weaknesses = weaknesses,

        interview_risks = ai_results["interview_risks"],

        improvement_suggestions = ai_results["improvement_suggestions"],

        rewritten_bullets = ai_results["rewritten_bullets"]
    )
    
    
    
    