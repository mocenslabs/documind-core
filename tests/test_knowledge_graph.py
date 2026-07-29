from app.domain.knowledge.graph import (
    KnowledgeGraph,
)
from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)


def test_graph() -> None:
    graph = KnowledgeGraph()

    relationship = KnowledgeRelationship(
        source="Django",
        target="PostgreSQL",
        relation="related_to",
    )

    graph.add_node("Django")
    graph.add_node("PostgreSQL")
    graph.add_relationship(relationship)

    assert len(graph.nodes) == 2
    assert len(graph.relationships) == 1
