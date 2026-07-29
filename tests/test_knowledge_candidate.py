from pathlib import PurePosixPath

from app.domain.knowledge.entities import KnowledgeCandidate


def test_candidate_fields() -> None:
    candidate = KnowledgeCandidate(
        category="framework",
        value="Django",
        confidence=0.95,
        source=PurePosixPath("README.md"),
    )

    assert candidate.category == "framework"
    assert candidate.value == "Django"
    assert candidate.confidence == 0.95
