from pathlib import PurePosixPath

from app.domain.knowledge.evidence import KnowledgeEvidence


def test_knowledge_evidence() -> None:
    evidence = KnowledgeEvidence(
        source=PurePosixPath("pyproject.toml"),
        kind="dependency",
        value="Django>=6.0",
    )

    assert evidence.source == PurePosixPath("pyproject.toml")
    assert evidence.kind == "dependency"
    assert evidence.value == "Django>=6.0"
