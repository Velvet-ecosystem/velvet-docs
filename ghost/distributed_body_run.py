# SPDX-License-Identifier: GPL-3.0-only
"""Cross-repository Ghost proof for Velvet's distributed body.

This harness imports the real public contracts from AI Core, Runtime, Event
Protocol, and Receipts. It performs deterministic synthetic analysis only. It
never authorizes speech, memory, execution, CAN, hardware, or actuation.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Tuple

from distributed_work_events import (
    NODE_ADVERTISEMENT_PUBLISHED,
    WORK_ACCEPTED,
    WORK_COMPLETED,
    WORK_OFFERED,
    NodeAdvertisement as EventNodeAdvertisement,
    WorkLifecycleRecord,
    build_distributed_work_event,
    build_node_advertisement_event,
    validate_distributed_work_event,
)
from runtime_receipts import runtime_receipt_from_envelope
from services.distributed_work_coordinator import (
    DistributedWorkCoordinator,
    NodeAdvertisement,
    NodeAvailability,
    NodeTier,
    VerifiedNodeRegistry,
    WorkRequirement,
)
from velvet.core.native_brain.attention import AttentionContext
from velvet.core.native_brain.cognition import ObservationEnvelope
from velvet.core.native_brain.curiosity import CuriosityContext
from velvet.core.native_brain.expectations import ExpectationContext
from velvet.core.native_brain.integrated_cycle import (
    IntegratedCognitiveCycle,
    IntegratedCycleContext,
    IntegratedCycleOutcome,
)
from velvet.core.native_brain.intents import IntentContext, IntentKind
from velvet.core.native_brain.judgment import JudgmentContext
from velvet.core.native_brain.patterns import PatternContext
from velvet.core.native_brain.presence import PresenceContext
from velvet.core.native_brain.self_orientation import (
    PersonalityProfile,
    PreferenceProfile,
    SelfIdentity,
    SelfOrientation,
)


@dataclass(frozen=True)
class QueenReturnedResult:
    work_id: str
    source_node_id: str
    source_organ: str
    summary: str
    important: bool
    receipt_ids: Tuple[str, ...]
    authority: str = "none"


@dataclass(frozen=True)
class DistributedGhostRunResult:
    cognitive_outcome: str
    intent_statement: str
    placed_node_id: str
    placed_organ: str
    placement_mode: str
    lifecycle_events: Tuple[str, ...]
    receipt_events: Tuple[str, ...]
    queen_result: QueenReturnedResult
    runtime_completed: bool
    canonical: bool = False
    execution_authorized: bool = False
    actuation_authorized: bool = False
    authority: str = "none"

    def to_dict(self) -> Mapping[str, Any]:
        return {
            "cognitive_outcome": self.cognitive_outcome,
            "intent_statement": self.intent_statement,
            "placed_node_id": self.placed_node_id,
            "placed_organ": self.placed_organ,
            "placement_mode": self.placement_mode,
            "lifecycle_events": self.lifecycle_events,
            "receipt_events": self.receipt_events,
            "queen_result": {
                "work_id": self.queen_result.work_id,
                "source_node_id": self.queen_result.source_node_id,
                "source_organ": self.queen_result.source_organ,
                "summary": self.queen_result.summary,
                "important": self.queen_result.important,
                "receipt_ids": self.queen_result.receipt_ids,
                "authority": self.queen_result.authority,
            },
            "runtime_completed": self.runtime_completed,
            "canonical": self.canonical,
            "execution_authorized": self.execution_authorized,
            "actuation_authorized": self.actuation_authorized,
            "authority": self.authority,
        }


def run_distributed_ghost() -> DistributedGhostRunResult:
    """Run one thought-to-specialist-to-Queen synthetic workload."""

    work_id = "ghost:thermal-analysis:001"
    body_id = "founder-up2"

    identity = SelfIdentity()
    orientation = SelfOrientation(
        identity=identity,
        personality=PersonalityProfile(traits={"patient": 0.9}),
        preferences=PreferenceProfile(values={}),
        continuity_verified=True,
        runtime_context_verified=True,
        active_body=body_id,
        active_surface="vehicle",
    )
    observation = ObservationEnvelope(
        event_type="vehicle.coolant.observed",
        source="ruby.sensor",
        payload={"celsius": 94.0, "synthetic_samples": [89.0, 91.0, 94.0]},
        confidence=0.95,
    )
    cycle_context = IntegratedCycleContext(
        presence=PresenceContext(),
        attention=AttentionContext(
            repetition_count=5,
            corroborating_sources=2,
            historical_matches=3,
            owner_relevance=0.8,
            novelty=0.6,
        ),
        curiosity=CuriosityContext(explanation_available=True),
        judgment=JudgmentContext(
            candidate_claim="coolant rises after extended idle",
            source_reliability=0.95,
            evidence_completeness=0.95,
            freshness=1.0,
            corroborating_sources=3,
        ),
        pattern=PatternContext(
            candidate_statement="coolant tends to rise after extended idle",
            observation_key="vehicle.coolant.after-idle",
            scope=body_id,
            support_count=6,
            independent_contexts=4,
            corroborating_sources=3,
        ),
        expectation=ExpectationContext(
            expected_statement="coolant may rise again when extended idle conditions return",
            triggering_conditions=("engine-idling", "cooling-load-present"),
            evidence_references=("receipt:coolant-1", "receipt:coolant-2"),
            evaluated_at=100.0,
            horizon_seconds=300.0,
            review_after_seconds=120.0,
        ),
        intent=IntentContext(
            proposed_statement="run bounded thermal-pattern analysis",
            intent_kind=IntentKind.PROPOSE_WORK,
            objective="explain the synthetic coolant rise without actuation",
            evidence_references=("receipt:coolant-1", "receipt:coolant-2"),
            constraints=("ghost-only", "local-only", "no-actuation"),
            evaluated_at=100.0,
            expires_after_seconds=300.0,
            consequential=False,
            reversible=True,
        ),
    )
    cognitive = IntegratedCognitiveCycle(identity).run(
        orientation,
        observation,
        cycle_context,
    )
    if cognitive.outcome is not IntegratedCycleOutcome.INTENT_CANDIDATE:
        raise AssertionError("Native Brain did not produce the bounded work intent")
    if cognitive.intent is None or cognitive.intent.candidate is None:
        raise AssertionError("Native Brain intent candidate is missing")
    intent = cognitive.intent.candidate
    if not intent.requires_runtime_placement or intent.runtime_placement_authorized:
        raise AssertionError("intent did not preserve the Runtime authority boundary")

    registry = VerifiedNodeRegistry(body_id=body_id)
    ruby_node = NodeAdvertisement(
        node_id="ruby-lyra-01",
        body_id=body_id,
        organ="ruby",
        tier=NodeTier.SPECIALIST_LINUX,
        capabilities=("thermal-pattern-analysis", "local-pattern-detection"),
        current_load=0.25,
        health=0.96,
        availability=NodeAvailability.AVAILABLE,
        last_heartbeat=100.0,
        accepted_work_classes=("thermal-analysis",),
        max_concurrent_tasks=2,
    )
    queen_node = NodeAdvertisement(
        node_id="velvet-founder-up2",
        body_id=body_id,
        organ="velvet",
        tier=NodeTier.QUEEN,
        capabilities=("thermal-pattern-analysis", "whole-system-coordination"),
        current_load=0.20,
        health=0.98,
        availability=NodeAvailability.AVAILABLE,
        last_heartbeat=100.0,
        accepted_work_classes=("thermal-analysis",),
        max_concurrent_tasks=4,
    )
    for node in (ruby_node, queen_node):
        decision = registry.register(node)
        if not decision.accepted:
            raise AssertionError("verified Ghost node registration failed")

    coordinator = DistributedWorkCoordinator(registry)
    requirement = WorkRequirement(
        work_id=work_id,
        work_class="thermal-analysis",
        required_capabilities=("thermal-pattern-analysis",),
        preferred_capabilities=("local-pattern-detection",),
        allow_queen_fallback=True,
        consequential=False,
    )
    placement = coordinator.place(requirement, now=100.0, lease_seconds=60.0)
    if not placement.placed or placement.lease is None:
        raise AssertionError("Runtime did not place the bounded Ghost workload")
    lease = placement.lease
    if lease.node_id != ruby_node.node_id:
        raise AssertionError("Runtime failed to prefer the narrow specialist")
    if lease.execution_authorized or lease.court_authorized or lease.authority != "none":
        raise AssertionError("Runtime placement lease gained forbidden authority")

    events = []
    receipts = []
    for node in (ruby_node, queen_node):
        event = build_node_advertisement_event(
            source="runtime.node-registry",
            advertisement=_event_advertisement(node),
        )
        events.append(event)
        receipts.append(_receipt_for(event, node.node_id))

    offered = build_distributed_work_event(
        source="runtime.distributed-work",
        record=WorkLifecycleRecord(
            event_type=WORK_OFFERED,
            work_id=work_id,
            work_class=requirement.work_class,
            required_capabilities=requirement.required_capabilities,
            fallback_options=placement.alternatives,
            court_authorization_required=False,
        ),
    )
    accepted = build_distributed_work_event(
        source="runtime.distributed-work",
        parent_event_id=offered.event_id,
        record=WorkLifecycleRecord(
            event_type=WORK_ACCEPTED,
            work_id=work_id,
            work_class=requirement.work_class,
            required_capabilities=requirement.required_capabilities,
            node_id=lease.node_id,
            organ=lease.organ,
            placement_mode=lease.mode.value,
            lease_id=lease.lease_id,
            lease_expires_at=lease.expires_at,
            fallback_options=placement.alternatives,
            court_authorization_required=lease.court_authorization_required,
        ),
    )
    events.extend((offered, accepted))
    receipts.extend((_receipt_for(offered, work_id), _receipt_for(accepted, work_id)))

    summary = _ghost_thermal_analysis((89.0, 91.0, 94.0))
    completed = build_distributed_work_event(
        source="ruby.ghost-specialist",
        parent_event_id=accepted.event_id,
        record=WorkLifecycleRecord(
            event_type=WORK_COMPLETED,
            work_id=work_id,
            work_class=requirement.work_class,
            required_capabilities=requirement.required_capabilities,
            node_id=lease.node_id,
            organ=lease.organ,
            placement_mode=lease.mode.value,
            lease_id=lease.lease_id,
            result_status="completed",
            important_result=True,
            escalate_to_queen=True,
            court_authorization_required=False,
        ),
    )
    events.append(completed)
    completion_receipt = _receipt_for(completed, work_id)
    receipts.append(completion_receipt)
    runtime_completed = coordinator.complete(work_id=work_id, node_id=lease.node_id)

    for event in events:
        validate_distributed_work_event(event)
    if not completed.payload["important_result"] or not completed.payload["escalate_to_queen"]:
        raise AssertionError("important result was not routed back to the Queen")

    queen_result = QueenReturnedResult(
        work_id=work_id,
        source_node_id=lease.node_id,
        source_organ=lease.organ,
        summary=summary,
        important=True,
        receipt_ids=tuple(receipt.receipt_id for receipt in receipts),
    )
    return DistributedGhostRunResult(
        cognitive_outcome=cognitive.outcome.value,
        intent_statement=intent.statement,
        placed_node_id=lease.node_id,
        placed_organ=lease.organ,
        placement_mode=lease.mode.value,
        lifecycle_events=tuple(event.event_type for event in events),
        receipt_events=tuple(receipt.event for receipt in receipts),
        queen_result=queen_result,
        runtime_completed=runtime_completed,
    )


def _event_advertisement(node: NodeAdvertisement) -> EventNodeAdvertisement:
    return EventNodeAdvertisement(
        node_id=node.node_id,
        body_id=node.body_id,
        organ=node.organ,
        tier=node.tier.value,
        capabilities=node.capabilities,
        current_load=node.current_load,
        health=node.health,
        availability=node.availability.value,
        last_heartbeat=node.last_heartbeat,
        max_concurrent_tasks=node.max_concurrent_tasks,
        current_tasks=node.current_tasks,
        accepted_work_classes=node.accepted_work_classes,
        refused_work_classes=node.refused_work_classes,
        overflow_capabilities=node.overflow_capabilities,
        temporary_absorption_capabilities=node.temporary_absorption_capabilities,
        fallback_options=("queen-fallback",),
        body_verified=node.body_verified,
        continuity_verified=node.continuity_verified,
    )


def _receipt_for(event: Any, subject_id: str):
    document = event.to_dict()
    return runtime_receipt_from_envelope(
        {
            "event_type": document["event_type"],
            "source": document["source"],
            "subject_id": subject_id,
            "payload": document["payload"],
        }
    )


def _ghost_thermal_analysis(samples: Tuple[float, ...]) -> str:
    if len(samples) < 2:
        raise ValueError("at least two synthetic samples are required")
    delta = round(samples[-1] - samples[0], 1)
    direction = "rising" if delta > 0 else "falling" if delta < 0 else "stable"
    return (
        f"Synthetic coolant trend is {direction}; delta={delta:+.1f} C across "
        f"{len(samples)} samples. Observation only; no response was executed."
    )


if __name__ == "__main__":
    import json

    print(json.dumps(run_distributed_ghost().to_dict(), indent=2, sort_keys=True))
