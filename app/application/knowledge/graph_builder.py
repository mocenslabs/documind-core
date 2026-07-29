"""Knowledge graph builder."""

from __future__ import annotations

from app.domain.knowledge.graph import KnowledgeGraph
from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)


class KnowledgeGraphBuilder:
    """Build a knowledge graph."""

    def build(
        self,
        relationships: tuple[
            KnowledgeRelationship,
            ...,
        ],
    ) -> KnowledgeGraph:
        """Build graph."""

        graph = KnowledgeGraph()

        for relationship in relationships:
            graph.add_node(
                relationship.source,
            )

            graph.add_node(
                relationship.target,
            )

            graph.add_relationship(
                relationship,
            )

        return graph
