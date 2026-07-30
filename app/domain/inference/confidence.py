"""Inference confidence."""

from __future__ import annotations

from enum import IntEnum


class Confidence(IntEnum):
    """Confidence level for an observation."""

    LOW = 25

    MEDIUM = 50

    HIGH = 75

    CERTAIN = 100
