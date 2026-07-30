"""Inference suggested actions."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SuggestedAction:
    """Suggested action for an observation."""

    title: str

    description: str
