"""Parser domain."""

from .entities import (
    DocumentSection,
    ParsedDocument,
)
from .interfaces import Parser

__all__ = [
    "DocumentSection",
    "ParsedDocument",
    "Parser",
]
