"""Local repository parser."""

from __future__ import annotations

from pathlib import PurePosixPath

from app.domain.parser.entities import (
    DocumentSection,
    ParsedDocument,
)
from app.domain.parser.interfaces import Parser
from app.domain.scanner.entities import ScanDocument


class LocalParser(Parser):
    """Normalize scanned repository documents."""

    def parse(
        self,
        document: ScanDocument,
    ) -> ParsedDocument:
        """Parse a scanned document into a normalized structure."""

        language = self._detect_language(document.path)

        title = self._extract_title(
            document.path,
            document.content,
        )

        sections = self._extract_sections(
            document.content,
        )

        return ParsedDocument(
            path=document.path,
            language=language,
            title=title,
            plain_text=document.content.strip(),
            sections=tuple(sections),
            metadata=self._extract_metadata(
                document.path,
                document.content,
            ),
        )

    def _detect_language(
        self,
        path: PurePosixPath,
    ) -> str:
        """Infer document language from filename."""

        name = path.name.lower()

        if name.endswith(".md"):
            return "markdown"

        if name.endswith(".toml"):
            return "toml"

        if name.endswith(".json"):
            return "json"

        if name.endswith(".yml") or name.endswith(".yaml"):
            return "yaml"

        if name == "dockerfile":
            return "dockerfile"

        if name.endswith(".txt"):
            return "text"

        return "plain"

    def _extract_title(
        self,
        path: PurePosixPath,
        content: str,
    ) -> str:
        """Extract a human-readable title."""

        if path.suffix == ".md":
            for line in content.splitlines():
                line = line.strip()

                if line.startswith("# "):
                    return line[2:].strip()

        return path.name

    def _extract_sections(
        self,
        content: str,
    ) -> list[DocumentSection]:
        """Extract Markdown headings."""

        sections: list[DocumentSection] = []

        current_heading = ""
        current_level = 0
        current_lines: list[str] = []

        for line in content.splitlines():
            stripped = line.strip()

            if stripped.startswith("#"):
                if current_heading:
                    sections.append(
                        DocumentSection(
                            heading=current_heading,
                            level=current_level,
                            content="\n".join(current_lines).strip(),
                        )
                    )

                current_level = len(stripped) - len(stripped.lstrip("#"))
                current_heading = stripped[current_level:].strip()
                current_lines = []

                continue

            current_lines.append(line)

        if current_heading:
            sections.append(
                DocumentSection(
                    heading=current_heading,
                    level=current_level,
                    content="\n".join(current_lines).strip(),
                )
            )

        return sections

    def _extract_metadata(
        self,
        path: PurePosixPath,
        content: str,
    ) -> dict[str, str]:
        """Extract lightweight metadata from a repository document."""

        metadata: dict[str, str] = {}

        metadata["filename"] = path.name
        metadata["extension"] = path.suffix or "<none>"
        metadata["size"] = str(len(content))

        lines = content.splitlines()

        metadata["lines"] = str(len(lines))

        if lines:
            metadata["first_line"] = lines[0].strip()

        return metadata
