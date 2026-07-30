"""Observation priority."""

from __future__ import annotations

from enum import IntEnum


class Priority(IntEnum):
    """Observation priority."""

    LOW = 1
    MEDIUM = 2
    HIGH = 3
    CRITICAL = 4
