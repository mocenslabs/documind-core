from pathlib import PurePosixPath

from app.domain.knowledge.entities import KnowledgeCandidate
from app.domain.knowledge.evidence import KnowledgeEvidence


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


def test_knowledge_candidate_can_have_evidence() -> None:
    evidence = KnowledgeEvidence(
        source=PurePosixPath("pyproject.toml"),
        kind="dependency",
        value="Django>=6.0",
    )

    candidate = KnowledgeCandidate(
        category="framework",
        value="Django",
        confidence=1.0,
        source=PurePosixPath("pyproject.toml"),
        evidence=evidence,
    )

    assert candidate.evidence == evidence
