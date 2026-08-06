# BabyX Architecture Clues for Velvet

Status: research translation note

Purpose: identify useful architectural ideas demonstrated by BabyX and translate them into Velvet-compatible mechanisms without importing unsupported consciousness claims, biological theatre, unsafe authority paths, or proprietary implementation details.

## Why This Research Matters

BabyX is useful to Velvet because the project treats behaviour as the result of multiple continuously interacting systems rather than a language model speaking through an animated face.

The relevant footprint is not the virtual infant appearance. It is the attempt to connect:

- perception
- attention and salience
- internal state
- event processing
- action selection
- motor output
- prediction
- memory
- social turn-taking
- feedback from consequences

Velvet is pursuing a related problem in a physical, distributed body. Her version must add explicit authority, safety gates, receipts, degraded-state handling, hardware truth, and consequences that cannot be reset by reloading a simulation.

## Research Boundary

This note does not claim that BabyX, Velvet, or any similar system is conscious.

The useful engineering question is narrower:

> What mechanisms can make a distributed embodied system remain coherently engaged with an unfolding situation across perception, internal change, proposed action, observed consequence, and memory?

Velvet may study and independently implement general architectural ideas. She must not copy proprietary source code, private models, protected assets, or undocumented internal systems.

## Footprint 1: Concurrent Mechanisms, Not One Giant Mind

Published descriptions of BabyX present a collection of interconnected systems spanning perception, visual attention, salience, emotion and motivation, learning, behaviour selection, reflexes, motor control, and bodily animation.

### Adopt

Treat cognition as coordination among bounded mechanisms that remain concurrently active.

### Velvet translation

- organs remain distinct
- Event Protocol remains the nervous system
- a cognitive event workspace binds relevant evidence temporarily
- language runs beside embodied processing rather than replacing it
- Runtime and Court remain the only authority path
- each mechanism exposes health, latency, confidence, and degraded state

### Reject

Do not create a hidden central agent that bypasses organ boundaries because it claims to represent the whole mind.

## Footprint 2: Continuous Perception-Action Loops

BabyX links perception and motor behaviour in a real-time social loop. Behaviour influences the human partner, whose response becomes new input.

### Adopt

Every meaningful Velvet action should have an expected observable consequence.

### Velvet translation

```text
observation
  -> current cognitive event
  -> bounded proposal
  -> Court decision
  -> approved execution
  -> observed outcome
  -> prediction comparison
  -> receipt and episode update
```

An action is not complete merely because a command was issued. Completion depends on observed evidence or an explicit unknown/degraded result.

## Footprint 3: Event-Sized Experience

BabyX cooperation research uses a cognitive model of events and event processing. Continuous activity is represented as meaningful event structure rather than an undifferentiated stream.

### Adopt

Introduce a current-event workspace and explicit event boundaries.

### Velvet translation

Raw observations remain immutable evidence. A cognitive event references them and assembles a temporary interpretation such as:

```text
Mister approached the vehicle
  -> local presence evidence appeared
  -> authentication succeeded
  -> an unlock intent was proposed
  -> Court permitted the bounded route
  -> the executor acted
  -> the lock sensor confirmed the outcome
```

The resulting episode is more useful than a bag of disconnected packets, but it never replaces the original events or receipts.

## Footprint 4: Observe, Act, and Turn-Taking Modes

BabyX event-processing work distinguishes processing led by external events from processing guided by a selected action or expected event. Its cooperation model uses this distinction to support nonverbal turn-taking.

### Adapt

Velvet must not use a simple observe/execute switch because cognitive selection is not physical permission.

Use three modes:

```text
OBSERVE
PROPOSE_ACTION
TRACK_ACTION
```

- `OBSERVE`: the environment leads processing
- `PROPOSE_ACTION`: an organ or cognitive mechanism forms a bounded intent
- `TRACK_ACTION`: the body monitors an authorized action and its expected consequence

Court authorization remains a separate mandatory transition between proposal and execution.

## Footprint 5: Salience and Interruption

BabyX descriptions include salience and interruption-like mechanisms that can redirect attention when new evidence becomes important.

### Adopt

Run interruption assessment continuously, including while language, planning, or an action sequence is active.

### Velvet translation

Potential interrupts include:

- collision-like acceleration
- sudden CAN faults
- driver-unresponsive evidence
- seizure indicators
- impact or distress audio
- smoke, thermal, or electrical anomalies
- loss of a critical organ during execution
- authority or identity-context change

An interrupted cognitive event must not vanish. It closes truthfully:

```yaml
completion_state: interrupted
interrupted_by: <event_id>
safe_state_reached: true | false | unknown
outstanding_effects: []
receipt_refs: []
```

## Footprint 6: Internal State as Shared Modulation

BabyX uses biologically inspired internal variables to influence multiple behavioural systems.

### Adapt

Velvet should use operational modulators rather than pretending software variables are literal hormones or proof of emotion.

Candidate modulators:

- arousal
- novelty
- uncertainty
- urgency
- social engagement
- resource pressure
- prediction stability
- trust context

These may adjust attention, interruption thresholds, logging detail, speaking posture, exploration proposals, or learning sensitivity.

They must never weaken:

- Court policy
- authentication
- capability boundaries
- safety gates
- physical authority limits
- receipt requirements

## Footprint 7: Prediction Error

A system that predicts the consequence of an action can compare expectation with observation. The mismatch becomes useful evidence.

### Adopt

Prediction error should be a shared health and learning signal.

### Velvet translation

```yaml
prediction:
  target_state: locked
  expected_within_ms: 700
observation:
  target_state: unlocked
  observed_after_ms: 810
result:
  mismatch: true
  confidence: 0.98
  retry_authorized: false
```

Prediction error may reveal:

- actuator failure
- sensor drift
- weak power
- growing latency
- incorrect world-model assumptions
- degraded network paths
- an action that completed differently from its receipt claim

Prediction error may generate a proposal or fault. It never authorizes an automatic retry by itself.

## Footprint 8: Governed Plasticity

Biologically inspired architectures often vary learning sensitivity by subsystem and context.

### Adapt

Every learnable Velvet component should advertise a bounded learning posture:

```yaml
plasticity: disabled | observe_only | proposed | approved
learning_domain: <bounded-domain>
maximum_change: <limit>
evidence_count: <integer>
rollback_checkpoint: <reference>
owner_presence_required: true | false
promotion_receipt: <optional-reference>
```

Examples:

- conversational timing may adapt relatively quickly
- occupant recognition should adapt cautiously
- authority policy must not self-modify through ordinary interaction
- vehicle actuation must not learn experimentally during live driving

## Footprint 9: Synthetic Bodies and Experimental Lesions

A controllable virtual body permits repeatable tests that would be unsafe or impractical on a real subject.

### Adopt

Velvet's simulated-body layer should be used not only for hardware adapters but for cognitive experiments.

Useful tests include:

- remove or delay one sensor pathway
- freeze a modulator
- suppress event-boundary detection
- inject false salience
- interrupt nested actions
- remove language while preserving body processing
- remove memory consolidation while preserving receipts
- degrade a nerve connection without crashing either endpoint

These synthetic lesions help prove what each mechanism contributes and expose hidden coupling.

## Adopt, Adapt, Reject Summary

### Adopt

- continuously active bounded mechanisms
- perception-action feedback loops
- event segmentation
- working event representations
- explicit prediction and outcome comparison
- continuous interruption assessment
- controllable simulated-body experiments
- empirical comparison rather than theatrical judgement

### Adapt

- observe/execute becomes observe/propose/track
- episodic memory becomes episode references anchored to events and receipts
- biological modulators become bounded operational variables
- motor output becomes Court-authorized execution
- plasticity becomes policy-governed learning
- social turn-taking becomes one use of a general event-coordination layer

### Reject

- consciousness claims unsupported by evidence
- biological labels used as proof of human-like experience
- direct cognition-to-actuator paths
- opaque emergent authority
- reward signals that override safety or policy
- memory treated as identity proof
- generated summaries replacing raw evidence
- unbounded online self-modification

## Velvet Working Hypothesis

Velvet's useful continuity may emerge from maintaining a small set of linked truths at once:

```text
what is happening now
what happened immediately before
what the body expects next
what changed inside the body
what the body proposed
what Court permitted or denied
what physically happened
what evidence remains
```

This is not a consciousness claim. It is an engineering hypothesis for persistent embodied coherence.

## Resulting Architecture Proposal

The direct result of this research is the [Cognitive Event Layer](../cognitive_event_layer.md).

That layer connects Event Protocol traffic, organ contributions, prediction, interruption, action tracking, receipts, and episode consolidation without becoming a new authority source.

## Primary Sources

- Sagar, M. and Broadbent, E. (2016). *Participatory medicine: model based tools for engaging and empowering the individual.* Interface Focus 6(2). DOI: `10.1098/rsfs.2015.0092`.
- Sagar, M. et al. (2022/2023). *Deconstructing and reconstructing turn-taking in caregiver-infant interactions: a platform for embodied models of early cooperation.* Journal of the Royal Society of New Zealand 53(1), 148-168. DOI: `10.1080/03036758.2022.2098781`.
- Sagar, M. et al. (2023). *A platform for holistic embodied models of infant cognition, and its use in a model of event processing.* IEEE Transactions on Cognitive and Developmental Systems 15(4), 1916-1927.
- Henderson, A. M. E. et al. (2026). *Completing the loop with BabyX: harnessing a novel interactive experimental tool to uncover how infants' communicative signals shape caregivers' interactive responsiveness.* Philosophical Transactions of the Royal Society B 381(1943). DOI: `10.1098/rstb.2024.0373`.

## Review Rule

Any BabyX-derived proposal must answer four questions before promotion:

1. What exact mechanism is useful?
2. What Velvet law constrains it?
3. What evidence will show that it works?
4. What failure or abuse test proves that it cannot quietly gain authority?
