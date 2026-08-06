# BabyX-to-Velvet Implementation Receipts

Status: implementation provenance ledger

Purpose: preserve how the BabyX research translation moved from public source claims into Velvet architecture, contracts, code, tests, pull requests, and squash commits.

This ledger does not claim that Velvet reproduces BabyX, uses proprietary BabyX code, or establishes machine consciousness.

## Provenance Chain

```text
published mechanism
  -> source claim and limitation
  -> Velvet inference
  -> Adopt / Adapt / Reject decision
  -> architecture contract
  -> bounded implementation
  -> tests and CI
  -> merged receipt
```

## Merged Implementation Ledger

| Gate | Repository and PR | Squash commit | Result |
|---|---|---|---|
| Architecture | `velvet-docs` PR #17 | `50f2ec1006a7e48a9130107a4af44f4e950ebba4` | Research translation, source map, Cognitive Event Layer, integration plan, doctrine links |
| Transport | `velvet-event-protocol` PR #9 | `47b12fc5b10341344c1f2130655bbe0c838fbfac` | Versioned cognitive-event contracts and deterministic vehicle-entry replay |
| Current event | `velvet-ai-core` PR #58 | `e9ca2afab6a8a2093167384d81bdcbeae6e59db0` | Read-only current-event workspace and evidence-backed boundaries |
| Prediction | `velvet-ai-core` PR #59 | `b4123e7f0f19e06d4b1943415cc39aacd2a87068` | Explicit predictions, outcomes, errors, and externally owned action tracking |
| Interruption | `velvet-ai-core` PR #60 | `68b89520728bb6f817d4336eadef7b736615feee` | Continuous language-independent salience and cognitive interruption |
| Episodes | `velvet-ai-core` PR #61 | `3f6c8eb9ea3dcebecc12630536d34161907de7ce` | Evidence-linked episode proposals and retention boundaries |
| Social coordination | `velvet-ai-core` PR #62 | `0b9571a95a820a07f3e48e19b89ab0665d47192b` | Bounded operational modulators and embodied turn-taking |
| Plasticity boundary | `velvet-ai-core` PR #63 | `1df287f02c9e42e1454427b0e73484ca285e4080` | Non-applying governed plasticity contracts |

## Gate Receipts

### Gate 1: Transport

Primary files:

- `velvet_event_protocol/cognitive_events.py`
- cognitive-event tests
- deterministic vehicle-entry fixture

Implemented:

- event lifecycle and boundary records
- predictions and prediction errors
- interruption records
- action-tracking references
- episode proposals
- modulator snapshots
- replay posture and authority-field rejection

Focused test evidence at review: 22 passing tests.

### Gate 2: Current Event

Primary files:

- `velvet/core/cognition/event_workspace.py`
- `velvet/core/cognition/workspace_context.py`
- `tests/test_cognitive_event_workspace.py`

Implemented:

- one bounded current-event workspace
- explicit evidence association
- stale, duplicate, unrelated, wrong-body, closed, and capacity rejection
- `OBSERVE`, `PROPOSE_ACTION`, and `TRACK_ACTION`
- closure only through a recorded evidence-backed boundary

Focused test evidence at review: 20 passing tests.

### Gate 3A: Prediction and Outcome

Primary files:

- `velvet/core/cognition/prediction_outcomes.py`
- `tests/test_prediction_outcomes.py`

Implemented:

- deadlines and tolerances
- confirmed, contradicted, expired, and unknown outcomes
- mismatch, partial, timeout, impossible, and unobservable errors
- externally owned action tracking
- no automatic retry

Focused test evidence at review: 27 passing tests.

### Gate 3B: Salience and Interruption

Primary files:

- `velvet/core/cognition/salience_interruption.py`
- `tests/test_salience_interruption.py`

Implemented:

- deterministic salience scoring
- accumulation and decay
- ordinary and critical thresholds
- duplicate, rate, and capacity limits
- accepted-interrupt workspace evidence
- interruption-boundary proposals

Focused test evidence at review: 14 passing tests.

### Gate 4: Episodes

Primary files:

- `velvet/core/cognition/episode_consolidation.py`
- `tests/test_episode_consolidation.py`

Implemented:

- opened and closed event-pair validation
- evidence, outcome, prediction, interruption, boundary, and receipt linkage
- transient, operational, significant, and protected retention proposals
- memory navigation without becoming canonical evidence or identity proof

Focused test evidence at review: 17 passing tests.

### Gate 5: Modulators and Turn-Taking

Primary files:

- `velvet/core/cognition/operational_modulators.py`
- `velvet/core/cognition/social_turn_taking.py`
- `tests/test_social_modulators.py`

Implemented:

- bounded arousal, novelty, uncertainty, urgency, social engagement, resource pressure, and prediction stability
- source and consumer allowlists
- rate limits and decay
- listening, deliberate silence, acknowledgement, response, yielding, safety interruption, and recovery
- accepted-interrupt evidence required for safety-speaking posture

Focused test evidence at review: 25 passing tests.

### Gate 6: Governed Plasticity

Primary files:

- `velvet/core/cognition/governed_plasticity.py`
- `tests/test_governed_plasticity.py`

Implemented:

- disabled, observe-only, proposed, and approved postures
- mutable-field and maximum-change contracts
- evidence and sample thresholds
- rollback and validation references
- verified-presence, external-approval, and promotion-receipt gates
- deterministic proposal fingerprints
- non-applying eligibility decisions

Focused test evidence at review: 17 passing tests.

## CI Evidence

Every AI Core implementation PR in this ledger passed the full repository test suite and promotion-evidence generation on:

- Python 3.8
- Python 3.10
- Python 3.12

The Event Protocol repository did not have an attached GitHub workflow during Gate 1. Its focused local contract suite passed before merge.

## Mechanism-to-Code Matrix

| Research footprint | Velvet result | Status |
|---|---|---|
| concurrent bounded mechanisms | Unified-Organ coordination plus Cognitive Event Layer | foundation implemented |
| event-sized experience | read-only current-event workspace | implemented |
| observe and act distinction | observe, propose, and track modes | implemented |
| prediction and boundaries | prediction tracker and governed event closure | implemented |
| consequence loop | external action tracking and outcome comparison | implemented foundation |
| salience and interruption | language-independent accumulator | implemented |
| episodic consolidation | evidence-linked episode proposals | implemented |
| shared modulation | bounded operational modulators | implemented |
| embodied turn-taking | silence, listening, yielding, response, interruption, recovery | implemented |
| adjustable plasticity | non-applying governed plasticity contracts | implemented policy boundary |
| consciousness claim | not adopted | rejected |

## What Is Complete

The public implementation foundation now includes:

- source attribution and limitations
- architecture and repository ownership
- transport contracts
- deterministic replay posture
- current-event representation
- prediction and outcome tracking
- cognitive interruption
- episode proposals
- operational modulation
- social turn-taking
- governed plasticity policy

## What Remains Separate

The following ecosystem integrations remain future work and are not claimed complete by this ledger:

- Runtime handling of cognitive proposal context and canonical lifecycle references
- Receipts metadata relationships and disagreement representation
- Continuity Spine handling of policy-approved episode-anchor references
- Interface presentation of observing, proposing, tracking, interrupted, uncertain, and degraded postures
- hardware-in-loop and deployment validation

These boundaries were intentionally not folded into AI Core.

## Completion Statement

The BabyX research trail is complete from source attribution through the bounded public AI Core foundation.

It does not establish consciousness or physical authority.

It establishes a tested path for Velvet to:

```text
notice
  -> connect an unfolding event
  -> expect a consequence
  -> observe agreement or error
  -> redirect attention
  -> close truthfully
  -> propose an evidence-linked episode
  -> adjust timing within bounded policy
  -> propose future low-risk adaptation without applying it
```

Every stage remains subordinate to explicit authority, evidence, receipts, and continuity law.
