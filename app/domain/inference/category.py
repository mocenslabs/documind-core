"""Observation categories."""

from __future__ import annotations

from enum import StrEnum


class ObservationCategory(StrEnum):
    """Observation category."""

    ARCHITECTURE = "architecture"

    SECURITY = "security"

    DEVOPS = "devops"

    DATABASE = "database"

    TESTING = "testing"

    DOCUMENTATION = "documentation"

    PERFORMANCE = "performance"

    MAINTAINABILITY = "maintainability"

    GENERAL = "general"
