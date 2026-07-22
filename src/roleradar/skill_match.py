# match the required skills with the candidate skills and return the matched skills
from models import Candidate, Job

def calculate_skill_match(
    required_skills: list[str],
    candidate_skills: list[str],
) -> dict:
    """Compare a candidate's skills against a role's requirements."""
  
    #1. normalize the candidate skills to lowercase and remove duplicates, this is why we use a set
    candidate_normalized = set()
    
    for skill in candidate_skills:
        cleaned_skill = skill.strip().lower()
        candidate_normalized.add(cleaned_skill)

    #2. remove duplicate requirements
    required_normalized = {}

    for skill in required_skills:
        cleaned_skill = skill.strip().lower()

        if cleaned_skill not in required_normalized:
            required_normalized[cleaned_skill] = skill.strip()

    # match the skills
    matched_skills = []
    missing_skills = []

    for cleaned_skill in required_normalized:
        original_skill = required_normalized[cleaned_skill]

        if cleaned_skill in candidate_normalized:
            matched_skills.append(original_skill)
        else:
            missing_skills.append(original_skill)
    
    # calculate the score/ match percentage
    if len(required_normalized) == 0:
        score = 100.0
    else:
        score = round(len(matched_skills) / len(required_normalized) * 100,2)

    result= {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "score": score,
    }

    return result
    
candidate = Candidate(
    name="Alex",
    skills = ["fastapi", "Python", "SQL"],
)  

job = Job(
    title = "AI Engineer",
    required_skills = ["Python", "FastAPI", "RAG", "Python"],
)  

result = calculate_skill_match(
    required_skills=job.required_skills,
    candidate_skills=candidate.skills,
)

print(f"Candidate: {candidate.name}")
print(f"Job Title: {job.title}")
print(result)