from pathlib import Path
from typing import Any

from app.application.analyze.service import AnalyzeRepositoryService


class FakeRepositoryLoader:
    def __init__(self) -> None:
        self.calls = 0

    def load(self, path: Path) -> dict[str, Path]:
        self.calls += 1
        return {"repository": path}


class FakeDiscoveryService:
    def __init__(self) -> None:
        self.calls = 0

    def discover(
        self,
        repository: dict[str, Path],
    ) -> dict[str, dict[str, Path]]:
        self.calls += 1
        return {"facts": repository}


class FakeRulesService:
    def __init__(self) -> None:
        self.calls = 0

    def evaluate(
        self,
        facts: dict[str, dict[str, Path]],
    ) -> dict[str, dict[str, dict[str, Path]]]:
        self.calls += 1
        return {"rules": facts}


class FakeKnowledgeService:
    def __init__(self) -> None:
        self.calls = 0

    def build(
        self,
        repository: dict[str, Path],
        facts: dict[str, dict[str, Path]],
        rules: dict[str, dict[str, dict[str, Path]]],
    ) -> dict[str, Any]:
        self.calls += 1

        return {
            "repository": repository,
            "facts": facts,
            "rules": rules,
        }


def test_analyze_repository_pipeline() -> None:
    loader = FakeRepositoryLoader()
    discovery = FakeDiscoveryService()
    rules = FakeRulesService()
    knowledge = FakeKnowledgeService()

    service = AnalyzeRepositoryService(
        repository_loader=loader,
        discovery_service=discovery,
        rules_service=rules,
        knowledge_service=knowledge,
    )

    result = service.analyze(Path("."))

    assert loader.calls == 1
    assert discovery.calls == 1
    assert rules.calls == 1
    assert knowledge.calls == 1

    assert result.repository == {"repository": Path(".")}

    assert result.facts == {
        "facts": {
            "repository": Path("."),
        }
    }

    assert result.rules == {
        "rules": {
            "facts": {
                "repository": Path("."),
            }
        }
    }

    assert result.knowledge["repository"] == result.repository
    assert result.knowledge["facts"] == result.facts
    assert result.knowledge["rules"] == result.rules
