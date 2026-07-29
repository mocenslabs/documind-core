"""Knowledge relationship entities."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class KnowledgeRelationship:
    """Relationship between two knowledge candidates."""

    source: str
    target: str
    relation: str
