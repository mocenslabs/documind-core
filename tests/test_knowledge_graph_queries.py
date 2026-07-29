from app.domain.knowledge.graph import (
    KnowledgeGraph,
)
from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)


def test_graph_queries() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Django")
    graph.add_node("PostgreSQL")
    graph.add_node("Docker")

    graph.add_relationship(
        KnowledgeRelationship(
            source="Django",
            target="PostgreSQL",
            relation="related_to",
        )
    )

    graph.add_relationship(
        KnowledgeRelationship(
            source="Django",
            target="Docker",
            relation="related_to",
        )
    )

    assert graph.has_node("Django")

    assert graph.neighbors("Django") == (
        "Docker",
        "PostgreSQL",
    )

    assert len(graph.outgoing("Django")) == 2

    assert len(graph.incoming("PostgreSQL")) == 1
