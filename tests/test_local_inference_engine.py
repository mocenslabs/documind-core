from app.domain.knowledge.graph import KnowledgeGraph
from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)
from app.infrastructure.inference.local_engine import (
    LocalInferenceEngine,
)


def test_local_engine() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")
    graph.add_node("Docker")

    graph.add_relationship(
        KnowledgeRelationship(
            source="Django",
            target="Docker",
            relation="related_to",
        )
    )

    engine = LocalInferenceEngine()

    observations = engine.infer(graph)

    assert len(observations) == 2
