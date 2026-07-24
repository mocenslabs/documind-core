"""Builtin path-based normalization rules."""

from collections.abc import Sequence
from pathlib import PurePosixPath

from app.domain.discovery.facts import FoundDirectory, FoundFile, RawFact
from app.domain.knowledge.entities import (
    CIPlatform,
    Container,
    Framework,
    Knowledge,
    Technology,
)
from app.domain.rules.interfaces import Rule


class PyprojectTomlRule(Rule):
    """Detect Python from a pyproject.toml file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Python knowledge for each matching file."""
        return [
            Technology(name="Python", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "pyproject.toml"
        ]


class RequirementsTxtRule(Rule):
    """Detect Python from a requirements.txt file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Python knowledge for each matching file."""
        return [
            Technology(name="Python", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "requirements.txt"
        ]


class PackageJsonRule(Rule):
    """Detect Node.js from a package.json file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Node.js knowledge for each matching file."""
        return [
            Technology(name="Node.js", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "package.json"
        ]


class ManagePyRule(Rule):
    """Detect Django from a manage.py file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Django knowledge for each matching file."""
        return [
            Framework(name="Django", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "manage.py"
        ]


class DockerfileRule(Rule):
    """Detect Docker from a Dockerfile."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Docker knowledge for each matching file."""
        return [
            Container(name="Docker", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "Dockerfile"
        ]


class DockerComposeRule(Rule):
    """Detect Docker Compose from a docker-compose.yml file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Docker Compose knowledge for each matching file."""
        return [
            Container(name="Docker Compose", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name == "docker-compose.yml"
        ]


class GitHubActionsRule(Rule):
    """Detect GitHub Actions from its workflow directory."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce GitHub Actions knowledge for each matching directory."""
        return [
            CIPlatform(name="GitHub Actions", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundDirectory)
            and fact.path == PurePosixPath(".github/workflows")
        ]


class ViteConfigRule(Rule):
    """Detect Vite from a vite.config.* file."""

    def apply(self, facts: Sequence[RawFact]) -> list[Knowledge]:
        """Produce Vite knowledge for each matching file."""
        return [
            Framework(name="Vite", source=fact.path)
            for fact in facts
            if isinstance(fact, FoundFile) and fact.path.name.startswith("vite.config.")
        ]


def builtin_rules() -> tuple[Rule, ...]:
    """Return the independent rules provided by the MVP."""
    return (
        PyprojectTomlRule(),
        RequirementsTxtRule(),
        PackageJsonRule(),
        ManagePyRule(),
        DockerfileRule(),
        DockerComposeRule(),
        GitHubActionsRule(),
        ViteConfigRule(),
    )
