"""Tests for builtin path-based normalization rules."""

from pathlib import PurePosixPath

import pytest

from app.application.knowledge.service import KnowledgeService
from app.application.rules.builtin_rules import (
    DockerComposeRule,
    DockerfileRule,
    GitHubActionsRule,
    ManagePyRule,
    PackageJsonRule,
    PyprojectTomlRule,
    RequirementsTxtRule,
    ViteConfigRule,
    builtin_rules,
)
from app.application.rules.service import RuleEngineService
from app.domain.discovery.facts import FoundDirectory, FoundFile, RawFact
from app.domain.knowledge.entities import (
    CIPlatform,
    Container,
    Framework,
    Knowledge,
    Technology,
)
from app.domain.rules.interfaces import Rule


@pytest.mark.parametrize(
    ("rule", "fact", "expected"),
    [
        (
            PyprojectTomlRule(),
            FoundFile(PurePosixPath("pyproject.toml")),
            Technology(name="Python", source=PurePosixPath("pyproject.toml")),
        ),
        (
            RequirementsTxtRule(),
            FoundFile(PurePosixPath("requirements.txt")),
            Technology(name="Python", source=PurePosixPath("requirements.txt")),
        ),
        (
            PackageJsonRule(),
            FoundFile(PurePosixPath("package.json")),
            Technology(name="Node.js", source=PurePosixPath("package.json")),
        ),
        (
            ManagePyRule(),
            FoundFile(PurePosixPath("manage.py")),
            Framework(name="Django", source=PurePosixPath("manage.py")),
        ),
        (
            DockerfileRule(),
            FoundFile(PurePosixPath("Dockerfile")),
            Container(name="Docker", source=PurePosixPath("Dockerfile")),
        ),
        (
            DockerComposeRule(),
            FoundFile(PurePosixPath("docker-compose.yml")),
            Container(
                name="Docker Compose",
                source=PurePosixPath("docker-compose.yml"),
            ),
        ),
        (
            GitHubActionsRule(),
            FoundDirectory(PurePosixPath(".github/workflows")),
            CIPlatform(
                name="GitHub Actions",
                source=PurePosixPath(".github/workflows"),
            ),
        ),
        (
            ViteConfigRule(),
            FoundFile(PurePosixPath("vite.config.ts")),
            Framework(name="Vite", source=PurePosixPath("vite.config.ts")),
        ),
    ],
)
def test_builtin_rule_produces_expected_knowledge(
    rule: Rule,
    fact: RawFact,
    expected: Knowledge,
) -> None:
    """Produce the expected knowledge for each supported path pattern."""
    assert rule.apply([fact]) == [expected]


def test_rule_engine_and_knowledge_service_compose_independent_rules() -> None:
    """Collect knowledge without coupling rules to each other."""
    facts: list[RawFact] = [
        FoundFile(PurePosixPath("package.json")),
        FoundDirectory(PurePosixPath(".github/workflows")),
    ]
    service = KnowledgeService(rule_engine=RuleEngineService(rules=builtin_rules()))

    assert service.build(facts) == [
        Technology(name="Node.js", source=PurePosixPath("package.json")),
        CIPlatform(
            name="GitHub Actions",
            source=PurePosixPath(".github/workflows"),
        ),
    ]
