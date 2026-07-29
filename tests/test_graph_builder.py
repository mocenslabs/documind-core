from app.application.knowledge.graph_builder import (
    KnowledgeGraphBuilder,
)
from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)


def test_build_graph() -> None:
    builder = KnowledgeGraphBuilder()

    graph = builder.build(
        (
            KnowledgeRelationship(
                source="Django",
                target="PostgreSQL",
                relation="related_to",
            ),
        )
    )

    assert "Django" in graph.nodes
    assert "PostgreSQL" in graph.nodes

    assert len(graph.relationships) == 1
    assert graph.has_node("Django")
    assert graph.has_node("PostgreSQL")

    assert graph.neighbors("Django") == ("PostgreSQL",)
