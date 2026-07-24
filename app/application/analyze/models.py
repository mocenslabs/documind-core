"""Application models for repository analysis."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True, slots=True)
class AnalysisResult:
    """Aggregates the complete repository analysis."""

    repository: Any
    facts: Any
    rules: Any
    knowledge: Any
