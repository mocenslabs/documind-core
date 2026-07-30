"""Inference severity."""

from __future__ import annotations

from enum import StrEnum


class Severity(StrEnum):
    """Observation severity."""

    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
