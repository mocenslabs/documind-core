"""Knowledge graph."""

from __future__ import annotations

from dataclasses import dataclass, field

from app.domain.knowledge.relationships import (
    KnowledgeRelationship,
)


@dataclass(slots=True)
class KnowledgeGraph:
    """Repository knowledge graph."""

    nodes: set[str] = field(default_factory=set)

    relationships: list[KnowledgeRelationship] = field(default_factory=list)

    def add_node(
        self,
        node: str,
    ) -> None:
        """Register a graph node."""

        self.nodes.add(node)

    def add_relationship(
        self,
        relationship: KnowledgeRelationship,
    ) -> None:
        """Register a graph edge."""

        self.relationships.append(
            relationship,
        )

    def has_node(
        self,
        node: str,
    ) -> bool:
        """Return whether a node exists."""

        return node in self.nodes

    def neighbors(
        self,
        node: str,
    ) -> tuple[str, ...]:
        """Return adjacent nodes."""

        adjacent: set[str] = set()

        for relationship in self.relationships:
            if relationship.source == node:
                adjacent.add(
                    relationship.target,
                )

            if relationship.target == node:
                adjacent.add(
                    relationship.source,
                )

        return tuple(
            sorted(adjacent),
        )

    def outgoing(
        self,
        node: str,
    ) -> tuple[KnowledgeRelationship, ...]:
        """Return outgoing relationships."""

        return tuple(
            relationship
            for relationship in self.relationships
            if relationship.source == node
        )

    def incoming(
        self,
        node: str,
    ) -> tuple[KnowledgeRelationship, ...]:
        """Return incoming relationships."""

        return tuple(
            relationship
            for relationship in self.relationships
            if relationship.target == node
        )
