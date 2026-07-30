from app.application.inference.service import (
    InferenceService,
)
from app.domain.inference.category import (
    ObservationCategory,
)
from app.domain.inference.confidence import Confidence
from app.domain.inference.entities import Observation
from app.domain.inference.interfaces import InferenceEngine
from app.domain.inference.priority import Priority
from app.domain.inference.severity import Severity
from app.domain.knowledge.graph import KnowledgeGraph


class FakeInferenceEngine(InferenceEngine):
    def infer(
        self,
        graph: KnowledgeGraph,
    ) -> list[Observation]:
        return [
            Observation(
                code="demo",
                title="Demo",
                description="Demo observation",
                severity=Severity.INFO,
                priority=Priority.LOW,
                category=ObservationCategory.GENERAL,
                confidence=Confidence.CERTAIN,
            )
        ]


def test_inference_service() -> None:
    service = InferenceService(
        engine=FakeInferenceEngine(),
    )

    response = service.infer(
        KnowledgeGraph(),
    )

    assert len(response.observations) == 1
