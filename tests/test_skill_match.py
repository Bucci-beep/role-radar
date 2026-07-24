from roleradar.models import Candidate, Job
from roleradar.skill_match import calculate_skill_match

def test_calculate_skill_match() -> None:
    candidate = Candidate(
        name="Alex",
        skills=["fastapi", "Python", "SQL"],
    )

    job = Job(
        title="AI Engineer",
        required_skills=["Python", "FastAPI", "RAG", "Python"],
    )

    result = calculate_skill_match(
        candidate=candidate, job=job,
    )

    assert result.matched_skills == ["FastAPI", "Python"]
    assert result.missing_skills == ["RAG"]
    assert result.score == 66.67



