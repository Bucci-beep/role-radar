# RoleRadar

RoleRadar is an evidence-based AI career agent built with Python. It compares job requirements with a candidate’s skills, identifies gaps, and will evolve into an agentic system that produces grounded learning and interview-preparation plans.

The project is being developed incrementally—from deterministic Python fundamentals to production-minded agentic AI engineering.

## Why RoleRadar?

Job descriptions are often lengthy, inconsistent, and difficult to compare. Candidates may also struggle to distinguish between skills they possess and skills they can demonstrate with credible evidence.

RoleRadar aims to turn that unstructured information into a clear, explainable analysis.

The completed system will:

- extract structured requirements from job descriptions;
- compare requirements with candidate skills and project evidence;
- identify matched and missing capabilities;
- recommend focused learning and portfolio improvements;
- generate technical interview questions;
- ground its recommendations in evidence;
- require human approval for important actions.

## Current milestone

The first milestone is a deterministic Python skill-matching engine.

```python
from roleradar import calculate_skill_match

result = calculate_skill_match(
    required_skills=["Python", "FastAPI", "RAG", "Python"],
    candidate_skills=["fastapi", "Python", "SQL"],
)

print(result)
```

Output:

```python
{
    "matched": ["FastAPI", "Python"],
    "missing": ["RAG"],
    "score": 66.67,
}
```

The matcher currently supports:

- case-insensitive comparison;
- duplicate removal;
- whitespace handling;
- empty input handling;
- alphabetically sorted results;
- structured dictionary output;
- automated testing of important edge cases.

## Engineering principle

RoleRadar begins with deterministic Python because an LLM should not perform work that conventional software can complete more reliably, quickly, and cheaply.

The project will use:

- deterministic code for calculations and validation;
- LLMs for interpreting unstructured language;
- tools for controlled interaction with external systems;
- evaluations to measure non-deterministic behaviour;
- human approval for sensitive or consequential actions.

This separation is essential when building dependable AI agents.

## Project structure

```text
role-radar/
├── src/
│   └── roleradar/
│       ├── __init__.py
│       └── skill_matcher.py
├── tests/
│   └── test_skill_matcher.py
├── .gitignore
├── pyproject.toml
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Bucci-beep/role-radar.git
cd role-radar
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

On Windows:

```powershell
python -m venv .venv
.venv\Scripts\activate
```

Install the project and development dependencies:

```bash
python -m pip install -e ".[dev]"
```

## Running the tests

```bash
pytest
```

The current test suite covers:

- normal skill matching;
- case-insensitive comparison;
- duplicate requirements;
- empty requirement lists;
- empty candidate profiles;
- surrounding whitespace;
- protection against modifying input lists.

## Roadmap

- [x] Build deterministic skill-matching engine
- [x] Add automated tests for core edge cases
- [ ] Create typed job and candidate models
- [ ] Extract structured requirements from job descriptions
- [ ] Integrate an LLM with validated structured output
- [ ] Add agent tools and controlled workflows
- [ ] Expose the application through FastAPI
- [ ] Store jobs, profiles, and analysis history in SQL
- [ ] Add retrieval with evidence citations
- [ ] Create an agent-evaluation and regression-test suite
- [ ] Add tracing, security guardrails, and human approval
- [ ] Package the application with Docker
- [ ] Deploy an interactive demonstration

## Skills demonstrated

As the project develops, it will demonstrate:

- Python data structures and functions;
- object-oriented and modular design;
- type hints and automated testing;
- API design with FastAPI;
- SQL and data modelling;
- LLM APIs and structured output;
- tool calling and agent orchestration;
- retrieval-augmented generation;
- AI evaluation and observability;
- prompt-injection and data-leakage controls;
- human-in-the-loop workflow design;
- containerisation and deployment.

## Development approach

Every milestone should answer three questions:

1. What real problem does this feature solve?
2. Why was this implementation chosen?
3. How do the tests or evaluations demonstrate that it works?

The goal is not to create another generic chatbot. The goal is to build a small but defensible AI product whose behaviour can be explained, tested, and improved.

## Status

RoleRadar is currently under active development as a portfolio and learning project.