# Cognitive Event Layer Integration Plan

Status: cross-repository implementation plan

Purpose: translate the Cognitive Event Layer architecture into bounded repository work without creating a new sovereign service, bypassing Court, duplicating receipts, or allowing generated interpretation to replace source evidence.

## Integration Outcome

The completed integration should let Velvet maintain a truthful, temporary representation of an unfolding situation across observations, proposals, authorization, execution, outcomes, interruption, and memory.

The target path is:

```text
source observations
  -> event association
  -> current-event workspace
  -> explicit predictions
  -> bounded proposal
  -> Runtime and Court
  -> approved execution
  -> observed consequence
  -> prediction comparison
  -> evidence-linked episode proposal
```

The layer connects moments. It does not command the body.

## Layer Boundaries

### Evidence Layer

Owns raw observations, sensor packets, transport envelopes, timestamps, source identity, freshness, and provenance.

The Cognitive Event Layer reads this evidence by reference. It does not rewrite it.

### Cognitive Event Layer

Owns temporary interpretation of what appears to be happening now:

- event association
- working context
- boundary proposals
- predictions
- salience
- interruption records
- proposal context
- action tracking
- episode proposals

This layer may be wrong. Its confidence and contradictions must remain visible.

### Authority Layer

Runtime and Court own:

- identity and session context
- policy resolution
- capability issuance
- resource ownership
- safety gates
- executor approval
- replay protection

No cognitive state becomes permission.

### Execution Layer

Approved executors own bounded physical actions and their direct result reporting.

The Cognitive Event Layer may track execution. It may not perform it.

### Evidence and Continuity Layer

Receipts preserve decisions and outcomes. Riven preserves identity lineage and continuity anchors. Episode memory provides navigation across experience.

These are related but not interchangeable.

## Canonical Input Classes

The initial implementation should accept only versioned, typed inputs.

### Observation inputs

- standardized sensor packets
- decoded CAN observations
- presence observations
- audio-event observations
- visual-event observations
- module and connection health events
- resource-pressure observations
- interface or owner request events

### Authority inputs

- Court decision events
- capability issuance or denial events
- execution-contract lifecycle events
- safety-gate results

### Outcome inputs

- executor result events
- actuator-state observations
- receipt references
- contradiction and timeout events
- degraded or unknown outcome reports

### Continuity inputs

- boot and recovery boundaries
- verified body and installation identity
- replay mode indicators
- continuity anchor availability

## Canonical Output Classes

The layer may emit:

- `cognitive.event.opened`
- `cognitive.event.updated`
- `cognitive.event.boundary_proposed`
- `cognitive.event.closed`
- `cognitive.prediction.created`
- `cognitive.prediction.resolved`
- `cognitive.prediction.error`
- `cognitive.interrupt.candidate`
- `cognitive.interrupt.accepted`
- `cognitive.proposal.context`
- `cognitive.action.tracking_started`
- `cognitive.action.tracking_finished`
- `cognitive.episode.proposed`
- `cognitive.health.changed`

These are observations or proposals. None are authorization events.

## Cross-Repository Ownership

### `velvet-event-protocol`

Add transport schemas and envelopes for cognitive-event traffic.

Initial work:

- define cognitive event identifiers and correlation rules
- define boundary proposal schema
- define prediction and prediction-error schemas
- define interruption candidate and accepted-interrupt schemas
- define episode-proposal schema
- preserve trace, source, monotonic, and replay metadata
- reject unknown authority fields in cognitive messages

Required proof:

- schema validation is deterministic
- replay metadata cannot be confused with live execution
- cognitive messages cannot masquerade as Court decisions or capabilities

### `velvet-ai-core`

Own the read-only workspace and bounded reasoning mechanisms.

Initial work:

- `event_workspace.py`
- `event_segmenter.py`
- `prediction_tracker.py`
- `interrupt_accumulator.py`
- `episode_consolidator.py`
- `internal_modulators.py`
- read-only language query adapter

Required proof:

- no executor imports
- no shell, relay, CAN-write, or capability-minting paths
- deterministic mode produces stable transitions from stable fixtures
- language unavailability does not stop body processing

### `velvet-runtime`

Consume proposal context without surrendering authority.

Initial work:

- accept bounded intent candidates with cognitive correlation references
- return Court decision and execution lifecycle references
- expose action-tracking state without giving the cognitive layer executor handles
- reject cognitive urgency, confidence, memory, or consensus as authority
- ensure retries require a new authorized request

Required proof:

- high confidence cannot mint a capability
- urgency cannot bypass policy
- prediction error cannot cause an automatic physical retry
- replayed cognitive traffic cannot execute

### `velvet-receipts`

Preserve evidence relationships without absorbing cognitive interpretation as fact.

Initial work:

- permit cognitive-event and episode references as non-authoritative metadata
- preserve decision, execution, and outcome receipts independently
- represent disagreement between predicted, reported, and observed outcomes
- prohibit generated summaries from replacing receipt payloads

Required proof:

- removing episode memory does not remove receipts
- changing an interpretation does not rewrite historical receipts
- a receipt reference does not become a replayable command

### `velvet-continuity-spine`

Anchor selected completed episodes without treating them as identity proof.

Initial work:

- accept policy-approved episode anchor references
- record cognitive-layer version changes as lineage-relevant software transitions where appropriate
- preserve gaps caused by shutdown, failure, or unverified continuity
- distinguish current experience, remembered episode, and identity lineage

Required proof:

- copied episodes cannot create a successor identity
- missing memory does not silently create a fresh privileged identity
- replay and live experience remain distinguishable

### `velvet-interface`

Present cognitive posture without theatrical certainty.

Initial work:

- show listening, observing, proposing, tracking, interrupted, uncertain, and degraded postures
- expose why attention changed when appropriate
- show unresolved outcome and stale evidence states
- avoid presenting confidence as permission or fact

Required proof:

- the interface cannot initiate direct hardware access
- fluent text cannot hide contradiction or unknown outcome
- critical interruption remains visible even if conversation continues

### `velvet-docs`

Maintain the ecosystem contract, research provenance, implementation sequence, and promotion gates.

## Initial Schema Set

The first code sprint should define, but not yet optimize, these objects:

```text
CognitiveEvent
EventBoundaryProposal
Prediction
PredictionError
InterruptCandidate
InterruptRecord
ActionTrackingRecord
EpisodeProposal
InternalModulatorSnapshot
CognitiveConnectionHealth
```

All objects require:

- schema version
- stable identifier
- creation timestamp
- monotonic time where available
- source and node identity
- correlation identifiers
- confidence where interpretive
- freshness or expiry where temporal
- replay state
- health or degraded state
- source evidence references

## Worked Replay: Vehicle Entry

This is the first canonical integration fixture.

### Stage 1: Approach

Inputs:

- exterior presence detected
- recognized owner-like visual evidence at bounded confidence
- owner device or NFC evidence not yet present

Workspace:

```yaml
event_type: vehicle_entry
mode: OBSERVE
lifecycle_state: DEVELOPING
active_goal: unknown
confidence: bounded
```

No unlock proposal is permitted from visual resemblance alone.

### Stage 2: Authentication

Inputs:

- verified local presence factor
- body and installation identity verified
- owner context confirmed

The cognitive event records the relationship between the observations. Authentication remains owned by Runtime.

### Stage 3: Proposal

An organ or interface emits a bounded unlock intent candidate.

The workspace enters `PROPOSE_ACTION` and links the proposal. It does not execute or authorize it.

### Stage 4: Court Decision

Runtime evaluates identity, policy, current body state, replay protection, and route scope.

If denied, the cognitive event records the denial and expected non-action.

If permitted, Runtime issues the bounded execution path.

### Stage 5: Action Tracking

The workspace enters `TRACK_ACTION` only after authorization and execution lifecycle evidence arrives.

Prediction:

```yaml
subject: driver_door_lock
expected_state: unlocked
expected_within_ms: 700
retry_authorized: false
```

### Stage 6: Outcome

Possible endings:

- actuator-state observation confirms unlock
- executor reports failure
- receipt reports success but sensor contradicts it
- no observable outcome arrives before timeout
- an emergency interrupt supersedes the event

Each ending remains distinct.

### Stage 7: Episode Proposal

The completed episode links:

- approach evidence
- authentication result
- proposal
- Court decision
- execution contract
- observed outcome
- prediction result
- receipts

The episode may summarize the sequence. The sources remain canonical.

## Worked Replay: Emergency Interruption

During the vehicle-entry sequence, a high-confidence impact or medical-distress event arrives.

Required behaviour:

1. preserve the vehicle-entry workspace
2. close or suspend it as interrupted
3. record outstanding physical effects
4. open or join the emergency event
5. request any safeing action through Runtime and Court
6. continue receipt handling
7. prevent the conversational model from blocking interruption processing

The interrupted event may later resume only if its context, authority, and evidence remain valid.

## Social Turn-Taking Integration

BabyX research makes turn-taking useful because participation is not simply alternating text messages. Velvet should treat turn-taking as an event-coordination problem.

Initial signals may include:

- owner speech onset and offset
- gaze or face orientation where permitted
- touch or control interaction
- active driving demand
- current safety severity
- elapsed silence
- incomplete owner utterance likelihood
- Velvet speech state
- interruption priority
- owner or guest profile

Possible postures:

```text
LISTEN
HOLD_SILENCE
ACKNOWLEDGE
RESPOND
YIELD
INTERRUPT_FOR_SAFETY
RECOVER_TURN
```

These postures affect presentation and timing. They do not affect authority.

## Internal Modulator Integration

The initial modulator set remains intentionally small:

- arousal
- novelty
- uncertainty
- urgency
- social engagement
- resource pressure
- prediction stability
- trust context

Each consumer must be explicitly allowlisted.

Example allowed effects:

- lower the threshold for reviewing a novel observation
- increase logging detail during high uncertainty
- shorten a conversational response during high driving demand
- postpone nonessential speech during owner concentration

Forbidden effects:

- relaxing authentication
- widening an intent
- bypassing Court
- selecting an executor
- suppressing a receipt
- changing protected medical or safety policy

## Synthetic Lesion Matrix

The simulated-body test pack should include:

| Lesion | Expected result |
|---|---|
| language unavailable | event tracking and interrupts continue |
| event segmenter frozen | observations continue; workspace reports degraded state |
| prediction tracker removed | actions still require Court; outcome evidence remains |
| episode consolidator removed | receipts and current state remain intact |
| salience path delayed | health warning appears; critical direct safety paths remain independent |
| one organ floods contributions | rate limits and resource-abuse protections engage |
| connection lies about freshness | cross-check detects stale evidence or marks uncertainty |
| memory unavailable | identity and authority remain intact |

## Promotion Gates

### Gate 0: Documentation complete

- vocabulary stable
- boundaries reviewed
- research source and translation recorded
- no consciousness claim used as requirement

### Gate 1: Schemas only

- schemas validate
- authority-field confusion tests pass
- replay markers are explicit

### Gate 2: Read-only workspace

- deterministic replay works
- source references remain intact
- no executor access exists

### Gate 3: Prediction and interruption

- prediction errors remain observational
- interrupts preserve unfinished events
- language cannot block critical processing

### Gate 4: Episode proposals

- summaries remain subordinate to evidence
- retention policy is explicit
- Riven anchoring is selective and receipted

### Gate 5: Bounded adaptation

- default remains disabled or observe-only
- checkpoints and rollback exist
- authority and protected safety policy are immutable to ordinary learning

## Completion Definition

BabyX-derived integration is complete at the architecture level when:

- the research source and limits are recorded
- the Cognitive Event Layer has explicit ownership and schemas
- existing event, time, authority, receipt, memory, continuity, and interface doctrines reference the layer consistently
- the vehicle-entry and emergency-interruption fixtures define expected behaviour
- repository work is sequenced behind promotion gates
- no cognitive mechanism can silently become authority

Implementation may then proceed repository by repository without reopening the foundational question each time.

## Related Documents

- [BabyX Architecture Clues for Velvet](research/babyx_architecture_clues.md)
- [Cognitive Event Layer](cognitive_event_layer.md)
- [Events, Intents, and Receipts](events_intents_and_receipts.md)
- [Continuity and Identity](continuity_and_identity.md)
- [Ecosystem Overview](ecosystem_overview.md)
- [Temporal Logic Doctrine](../architecture/temporal_logic_doctrine.md)
