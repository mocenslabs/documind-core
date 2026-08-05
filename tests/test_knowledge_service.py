from pathlib import PurePosixPath

from app.application.knowledge.service import KnowledgeService
from app.application.rules.builtin_rules import builtin_rules
from app.application.rules.service import RuleEngineService
from app.domain.discovery.facts import FoundFile


def test_knowledge_service_normalizes_duplicate_technologies() -> None:
    service = KnowledgeService(
        rule_engine=RuleEngineService(
            rules=builtin_rules(),
        ),
    )

    facts = [
        FoundFile(PurePosixPath("package.json")),
        FoundFile(PurePosixPath("frontend/package.json")),
        FoundFile(PurePosixPath("admin/package.json")),
    ]

    knowledge = service.build(facts)

    node_candidates = [item for item in knowledge if item.name == "Node.js"]

    assert len(node_candidates) == 1
    assert node_candidates[0].source == PurePosixPath("package.json")
