from app.application.inference.rule_engine import (
    InferenceRuleEngine,
)
from app.domain.inference.category import (
    ObservationCategory,
)
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.priority import Priority
from app.domain.inference.rules import InferenceRule
from app.domain.inference.severity import Severity
from app.domain.knowledge.graph import KnowledgeGraph


def test_rule_engine() -> None:
    graph = KnowledgeGraph()

    graph.add_node("Python")

    engine = InferenceRuleEngine(
        (
            InferenceRule(
                node="Python",
                observation=Observation(
                    code="python",
                    title="Python",
                    description="Python detected.",
                    severity=Severity.INFO,
                    priority=Priority.LOW,
                    category=ObservationCategory.GENERAL,
                    confidence=Confidence.CERTAIN,
                ),
            ),
        )
    )

    observations = engine.evaluate(graph)

    assert len(observations) == 1
