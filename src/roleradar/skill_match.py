# match the required skills with the candidate skills and return the matched skills
from .models import Candidate, Job, SkillMatchResult

def calculate_skill_match(
    candidate: Candidate,
    job: Job
) -> SkillMatchResult:
    """Compare a candidate's skills against a role's requirements."""
  
    #1. normalize the candidate skills to lowercase and remove duplicates, this is why we use a set
    candidate_normalized = set()
    
    for skill in candidate.skills:
        cleaned_skill = skill.strip().lower()
        candidate_normalized.add(cleaned_skill)

    #2. remove duplicate requirements
    required_normalized = {}

    for skill in job.required_skills:
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
        score = round(
            len(matched_skills) / len(required_normalized) * 100,
            2,
        )

    result = SkillMatchResult(
        matched_skills= sorted(matched_skills),
        missing_skills=sorted(missing_skills),
        score=score,
    )

    return result
    

if __name__ == "__main__":
    candidate = Candidate(
        name="Alex",
        skills = ["fastapi", "Python", "SQL"],
    )  

    job = Job(
        title = "AI Engineer",
        required_skills = ["Python", "FastAPI", "RAG", "Python"],
    )

    result = calculate_skill_match(
        candidate=candidate,
        job=job,
    )
    
    print(f"Candidate: {candidate.name}")
    print(f"Job Title: {job.title}")
    print(result)