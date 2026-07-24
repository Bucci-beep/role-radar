from dataclasses import dataclass

# dataclass gives related information a clear structure, RoleRadar can work 
# with objects that describe what the data means

@dataclass
class Candidate:
    name: str
    skills: list[str]

@dataclass
class Job:
    title: str
    required_skills: list[str]

@dataclass
class SkillMatchResult:
    matched_skills: list[str]
    missing_skills: list[str]
    score: float