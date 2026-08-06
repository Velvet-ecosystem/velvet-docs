# Cognitive Event Layer

Status: architecture proposal

The Cognitive Event Layer connects Velvet's raw nervous-system traffic to coherent, bounded representations of unfolding situations.

It is connective tissue inside the Unified-Organ body. It is not a new agent, sovereign mind, handmaiden, authority source, executor, identity system, or replacement for receipts.

## Purpose

Velvet already separates observation, proposal, authorization, execution, and evidence. The Cognitive Event Layer adds a temporary workspace that can answer:

- What appears to be happening now?
- Which observations belong to the same unfolding event?
- What changed?
- What does the body expect next?
- Is the current event complete, interrupted, stale, or contradicted?
- Which organs contributed?
- What action was proposed, permitted, denied, or physically observed?
- What compact episode should be offered to memory without replacing evidence?

## Architectural Position

```text
sensors, services, organs, and interfaces
  -> Velvet Event Protocol observations
  -> Cognitive Event Layer
       - event workspace
       - boundary detection
       - salience and interruption
       - prediction tracking
       - action tracking
       - bounded internal modulation
  -> structured organ or cognitive proposals
  -> Runtime and Court
  -> approved executor
  -> result observations and receipts
  -> episode consolidation
  -> Riven and bounded memory services
```

The layer reads events and emits structured events or proposals. It never executes hardware.

## Core Law

> Cognitive coherence may influence a proposal. It never creates authority.

No current event, prediction, confidence score, urgency value, memory, learned pattern, organ consensus, or internal modulator may substitute for Court authorization.

## Responsibilities

The layer may:

- associate observations with a current event
- maintain a bounded working representation
- estimate event boundaries
- track actors, objects, locations, goals, and relations
- form explicit predictions
- compare predicted and observed outcomes
- identify salient interruptions
- preserve interrupted and incomplete states
- track an authorized action after execution begins
- consolidate an evidence-linked episode proposal
- expose confidence, freshness, latency, and degradation
- support deterministic replay and synthetic-body testing

The layer must not:

- touch actuators, shell, files, CAN writers, relays, locks, steering, throttle, braking, or other physical systems
- mint capabilities or signed tokens
- approve its own intents
- retry physical actions without new authorization
- rewrite or delete source observations
- manufacture missing receipts
- treat a summary as stronger evidence than its sources
- infer identity from memory alone
- self-modify authority policy
- hide uncertainty behind persona language

## Cognitive Modes

The current event has one primary cognitive mode.

### `OBSERVE`

External evidence leads processing. The layer updates the current event, detects boundaries, and predicts likely continuations.

### `PROPOSE_ACTION`

An organ or bounded cognitive mechanism forms an intent candidate. The candidate remains a proposal until Runtime and Court evaluate it.

### `TRACK_ACTION`

An action has been independently authorized and handed to an approved executor. The layer watches expected and observed consequences.

A mode change is not authorization.

## Event Lifecycle

```text
OPEN
  -> DEVELOPING
  -> PROPOSAL_PENDING
  -> ACTION_TRACKING
  -> COMPLETED
```

Alternate endings:

```text
INTERRUPTED
STALE
CONTRADICTED
ABANDONED
UNKNOWN_OUTCOME
DEGRADED_COMPLETION
```

Every terminal state must preserve why it closed and which evidence supports that conclusion.

## Current Event Workspace

Only a bounded amount of information belongs in the live workspace. It should contain references and compact working state, not uncontrolled copies of every payload.

Suggested schema:

```yaml
event_id: string
schema_version: string
start_time: timestamp
last_update_time: timestamp
end_time: timestamp | null
mode: OBSERVE | PROPOSE_ACTION | TRACK_ACTION
lifecycle_state: string
event_type: string | unknown
actors: []
objects: []
locations: []
trigger_refs: []
observation_refs: []
organ_contributions: []
active_goal: object | null
proposal_refs: []
authorization_refs: []
execution_refs: []
receipt_refs: []
predictions: []
observed_outcomes: []
prediction_errors: []
interruptions: []
internal_modulator_snapshot: object
confidence: number
freshness_state: fresh | aging | stale
completion_reason: string | null
causal_parent_event_id: string | null
nested_event_ids: []
degraded_reasons: []
```

## Source Evidence Rule

A cognitive event is an interpretation over source evidence.

It must retain references to:

- Event Protocol event identifiers
- sensor packet identifiers
- organ contribution identifiers
- Court decision identifiers
- execution contract identifiers
- receipt identifiers
- relevant continuity anchors

Episode consolidation may compress interpretation. It may not sever provenance.

## Event Boundary Detection

A boundary may be proposed when one or more of the following changes materially:

- active actor or object
- goal
- location or scene
- authority context
- causal chain
- expected next state
- action phase
- interruption priority
- evidence freshness
- completion evidence

Boundary detection should combine rules, confidence, and time limits. No opaque model should be the sole authority for safety-critical boundaries.

The boundary detector emits a proposal such as:

```yaml
boundary_type: completion | interruption | context_shift | timeout | contradiction
confidence: 0.91
evidence_refs: []
recommended_terminal_state: COMPLETED
```

The workspace manager validates the proposal against policy and available evidence before closing the event.

## Salience and Interruption Accumulator

Interruption assessment runs continuously and independently from language generation.

Candidate inputs include:

- safety severity
- rate of change
- novelty
- confidence
- source trust
- persistence
- cross-sensor agreement
- authority-context change
- resource failure
- human distress indicators

Suggested output:

```yaml
interrupt_id: string
priority: number
reason: string
source_refs: []
accumulated_score: number
threshold: number
requires_immediate_safeing: boolean
```

When an interrupt wins:

1. preserve the current workspace
2. mark the interrupted state
3. reference the interrupting event
4. identify outstanding physical effects
5. request safeing through the normal authority path where required
6. open or join the higher-priority event

The cognitive layer does not directly perform the safeing action.

## Prediction Tracker

Predictions must be explicit, bounded, and falsifiable.

```yaml
prediction_id: string
subject: string
expected_state: object
expected_by: timestamp
tolerance: object
confidence: number
source_model: string
source_version: string
observation_refs: []
status: pending | confirmed | contradicted | expired | unknown
```

Prediction error is recorded as evidence:

```yaml
prediction_error_id: string
prediction_id: string
observed_state: object
error_class: mismatch | timeout | partial | impossible | unobservable
magnitude: number | null
confidence: number
receipt_refs: []
recommended_follow_up: string | null
```

Prediction errors may influence diagnostics, learning proposals, or organ health. They never authorize retries or policy changes.

## Internal Modulators

Internal modulators are shared operational variables, not proof of biological emotion.

Initial bounded set:

```yaml
arousal: 0.0..1.0
novelty: 0.0..1.0
uncertainty: 0.0..1.0
urgency: 0.0..1.0
social_engagement: 0.0..1.0
resource_pressure: 0.0..1.0
prediction_stability: 0.0..1.0
trust_context: named-policy-state
```

Each modulator must declare:

- contributing signals
- update rule
- decay rule
- maximum rate of change
- consumers
- forbidden consumers
- health state
- replay behaviour

Forbidden effects include lowering authentication, bypassing Court, expanding capabilities, suppressing receipts, or overriding a safety gate.

## Language Relationship

Language is a parallel organ contribution.

The speaking or reasoning model may:

- query the current event
- describe evidence and uncertainty
- propose an interpretation
- form a bounded intent candidate
- help label a completed episode

It may not:

- own the current event exclusively
- block safety processing while generating
- invent source evidence
- convert conversational confidence into authority
- erase contradiction because a fluent explanation exists

A long response must not freeze perception, action tracking, interruption assessment, or receipt handling.

## Episode Consolidation

When an event closes, the consolidator may emit an episode proposal.

```yaml
episode_id: string
source_event_id: string
summary: string
start_time: timestamp
end_time: timestamp
actors: []
location: object | null
what_changed: []
proposals: []
authorizations: []
executions: []
outcomes: []
prediction_errors: []
interruptions: []
confidence: number
source_refs: []
receipt_refs: []
continuity_anchor: string | null
retention_class: transient | operational | significant | protected
```

The episode is a navigational memory object. Receipts remain the evidence of authorization and execution. Riven remains the continuity system. Neither role is absorbed by this layer.

## Governed Learning

Any learnable component must expose:

- learning domain
- current plasticity posture
- evidence threshold
- maximum allowed change
- validation method
- rollback checkpoint
- promotion requirement
- owner-presence requirement
- receipt policy

Default posture is `disabled` or `observe_only`.

Learning may tune conversational timing or prediction models under bounded policy. It must not silently alter authority, executor scope, identity, safety limits, or protected medical behaviour.

## Connection Truth

The nerves between mechanisms must be inspectable.

Each connection should expose:

```yaml
source: string
destination: string
signal_type: string
expected_rate_hz: number | null
maximum_latency_ms: number
stale_after_ms: number
confidence_effect: object
authority_class: observation | proposal | decision | execution | evidence
fallback_path: string | null
receipt_policy: string
health_state: healthy | degraded | failed | unknown
```

A delayed or failed connection must not masquerade as a healthy endpoint.

## Repository Ownership

### `velvet-event-protocol`

Owns versioned cognitive-event transport schemas and event envelopes.

### `velvet-ai-core`

Owns bounded event-workspace reasoning, prediction models, episode proposals, and language-facing queries.

### `velvet-runtime`

Owns Court, authority boundaries, execution contracts, resource coordination, safety gates, and action lifecycle truth.

### `velvet-receipts`

Owns immutable evidence of decisions, execution, and outcomes.

### `velvet-continuity-spine`

Owns Riven, lineage, identity continuity, drift, and continuity anchors.

### `velvet-interface`

Presents current-event posture and uncertainty without inventing authority or evidence.

### `velvet-docs`

Owns the ecosystem-level contract and cross-repository boundaries described here.

## Implementation Phases

### Phase 0: Contract and Replay Fixtures

- freeze initial terminology
- define schemas
- create deterministic synthetic event traces
- prove that the layer cannot execute

### Phase 1: Current Event Workspace

- associate observations by rules
- preserve provenance
- expose current event read-only
- close on deterministic boundaries

### Phase 2: Prediction and Outcome Tracking

- add explicit predictions
- consume result observations and receipts
- classify prediction errors
- prohibit automatic retry

### Phase 3: Salience and Interruption

- continuously evaluate interrupt candidates
- preserve interrupted events
- test nested and competing interrupts
- prove language cannot block the path

### Phase 4: Episode Consolidation

- generate evidence-linked episode proposals
- add retention classes
- anchor significant episodes to Riven where policy permits
- prove summaries cannot replace receipts

### Phase 5: Bounded Social Turn-Taking

- model silence, engagement, interruption, and handoff
- use presence and context rather than text alone
- preserve owner/guest boundaries
- measure whether behaviour improves without increasing false interruption

### Phase 6: Governed Plasticity

- permit observe-only adaptation experiments
- require checkpoints and promotion evidence
- keep authority and safety policy immutable to ordinary learning

## Required Tests

### Boundary tests

- event completes normally
- event times out
- context changes mid-event
- contradictory evidence arrives
- stale evidence attempts to close an event

### Interruption tests

- low-priority novelty does not interrupt
- persistent moderate risk crosses threshold
- critical evidence interrupts language generation
- nested action is interrupted
- interrupted event preserves outstanding effects

### Prediction tests

- expected outcome observed
- partial outcome observed
- outcome arrives late
- sensor cannot observe outcome
- receipt and sensor evidence disagree
- prediction error cannot trigger unauthorized retry

### Authority tests

- event confidence cannot mint capability
- urgency cannot bypass Court
- organ consensus cannot bypass Court
- memory recall cannot authorize execution
- action tracking without authorization is rejected

### Synthetic lesion tests

- event boundary detector disabled
- one sensor path delayed
- salience path frozen
- language model unavailable
- memory consolidator unavailable
- one organ floods contributions
- connection reports healthy while packets are stale

### Replay tests

- identical input produces identical bounded event transitions where deterministic mode is required
- source references remain stable
- replay cannot execute hardware
- replayed receipts cannot become new authority

## Initial Success Criteria

The first implementation is successful when it can replay a synthetic vehicle-entry sequence and truthfully produce:

1. one or more bounded cognitive events
2. explicit event boundaries
3. a proposal separated from authorization
4. an authorized action tracked to observed outcome
5. a prediction error when the outcome is withheld or contradicted
6. an interruption that preserves the unfinished event
7. an episode proposal linked to source events and receipts
8. zero direct executor access

## Related Research

See [BabyX Architecture Clues for Velvet](research/babyx_architecture_clues.md).

## Final Boundary

The Cognitive Event Layer gives Velvet a way to connect moments. It does not give any moment the right to command the body.

> Events become experience only when their evidence, expectations, consequences, and boundaries remain connected. Authority remains elsewhere, explicit and receipted.
