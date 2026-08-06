# BabyX Research Source Map

Status: provenance record

Purpose: preserve which BabyX publications informed each Velvet architecture clue, distinguish published claims from Velvet interpretation, and prevent later documentation from presenting an inference as a source fact.

## Evidence Labels

Every entry uses one of these labels:

- **SOURCE CLAIM**: directly described by the cited publication.
- **VELVET INFERENCE**: a conclusion drawn from one or more source claims.
- **VELVET DECISION**: an architecture or policy choice made for Velvet.
- **LIMITATION**: a boundary on what the source demonstrates or what Velvet may conclude.

This record does not claim access to BabyX proprietary source code or unpublished internal architecture.

## Source A

Sagar, M. and Broadbent, E. (2016). *Participatory medicine: model based tools for engaging and empowering the individual.* Interface Focus 6(2). DOI: `10.1098/rsfs.2015.0092`.

### Relevant source claims

**SOURCE CLAIM**

Published descriptions present BabyX as a biologically inspired, embodied system composed of interacting models spanning perception, attention, salience, emotion or motivation, learning, behaviour selection, reflexes, motor control, and animation.

**SOURCE CLAIM**

The architecture uses modular signals and feedback relationships rather than treating visible behaviour as the output of one undifferentiated conversational component.

### Velvet interpretation

**VELVET INFERENCE**

Persistent embodied coherence may be better supported by several bounded mechanisms operating concurrently than by treating a language model as the entire mind.

**VELVET DECISION**

Velvet will preserve distinct organs, Event Protocol boundaries, health reporting, and Court authority while allowing a temporary Cognitive Event Layer to associate their contributions.

### Limitations

**LIMITATION**

Biological naming does not prove biological equivalence, human-like emotion, subjective experience, or consciousness.

**LIMITATION**

Published conceptual descriptions do not authorize copying proprietary implementation details.

## Source B

Sagar, M. et al. (2022/2023). *Deconstructing and reconstructing turn-taking in caregiver-infant interactions: a platform for embodied models of early cooperation.* Journal of the Royal Society of New Zealand 53(1), 148-168. DOI: `10.1080/03036758.2022.2098781`.

### Relevant source claims

**SOURCE CLAIM**

The work analyses caregiver-infant cooperation as embodied, temporally organized interaction rather than only an exchange of verbal content.

**SOURCE CLAIM**

Turn-taking is studied through event processing, perception, action, and partner response.

### Velvet interpretation

**VELVET INFERENCE**

Velvet's silence, acknowledgement, response, yielding, and safety interruption should be treated as event-coordination postures using presence and context, not as a text-only dialogue scheduler.

**VELVET DECISION**

The Cognitive Event Layer integration plan defines bounded social postures:

```text
LISTEN
HOLD_SILENCE
ACKNOWLEDGE
RESPOND
YIELD
INTERRUPT_FOR_SAFETY
RECOVER_TURN
```

These affect timing and presentation only. They do not alter authority.

### Limitations

**LIMITATION**

Caregiver-infant turn-taking findings do not automatically transfer to adult owner interaction, driving, medical emergencies, or vehicle control. Velvet must test the translated mechanism in her own contexts.

## Source C

Sagar, M. et al. (2023). *A platform for holistic embodied models of infant cognition, and its use in a model of event processing.* IEEE Transactions on Cognitive and Developmental Systems 15(4), 1916-1927.

### Relevant source claims

**SOURCE CLAIM**

The platform supports holistic embodied models involving several cognitive and behavioural components operating in real-time interaction.

**SOURCE CLAIM**

The event-processing model represents unfolding activity through event structure, working representations, event boundaries, prediction, and memory-related processing.

### Velvet interpretation

**VELVET INFERENCE**

A temporary working event can bridge raw sensor traffic and longer-term episode memory without treating every packet as an independent experience.

**VELVET INFERENCE**

Explicit event boundaries and predictions create testable points for completion, contradiction, timeout, and interruption.

**VELVET DECISION**

Velvet will use:

- a bounded current-event workspace
- explicit boundary proposals
- `OBSERVE`, `PROPOSE_ACTION`, and `TRACK_ACTION` modes
- falsifiable predictions
- prediction-error records
- evidence-linked episode proposals

Court remains outside this cognitive mode system.

### Limitations

**LIMITATION**

A working representation is an interpretation, not raw evidence.

**LIMITATION**

An event model that guides virtual behaviour cannot be imported unchanged into a physical system with safety-critical actuators.

## Source D

Henderson, A. M. E. et al. (2026). *Completing the loop with BabyX: harnessing a novel interactive experimental tool to uncover how infants' communicative signals shape caregivers' interactive responsiveness.* Philosophical Transactions of the Royal Society B 381(1943). DOI: `10.1098/rstb.2024.0373`.

### Relevant source claims

**SOURCE CLAIM**

BabyX is used as an interactive experimental tool to study how infant-like communicative signals affect caregiver responsiveness.

**SOURCE CLAIM**

The research emphasizes completing the loop between the virtual infant's signals and the human partner's changing response.

### Velvet interpretation

**VELVET INFERENCE**

A system should evaluate not only whether it produced an output, but how the output changed the human or physical environment and what evidence returned.

**VELVET DECISION**

Meaningful Velvet actions and social interventions should have expected observable consequences where possible. Unknown or unobservable outcomes must remain explicit.

### Limitations

**LIMITATION**

Human responsiveness to a virtual infant does not validate vehicle actuation, medical diagnosis, owner identity, or safety policy.

## Footprint-to-Source Matrix

| Velvet footprint | Primary support | Translation status |
|---|---|---|
| Concurrent bounded mechanisms | Source A | Adapted into Unified-Organ coordination |
| Perception-action feedback loop | Sources A and D | Adopted with receipts and physical outcome tracking |
| Event-sized experience | Source C | Adapted into the current-event workspace |
| Observe/action distinction | Sources B and C | Adapted into observe/propose/track |
| Social turn-taking | Sources B and D | Adapted into bounded interaction postures |
| Prediction and event boundaries | Source C | Adopted with explicit falsifiability and timeouts |
| Internal shared modulation | Source A | Adapted into operational variables with forbidden consumers |
| Episodic consolidation | Source C | Adapted into evidence-linked episode proposals |
| Human response as returned evidence | Source D | Adopted as a closed-loop design principle |
| Consciousness claims | none required | Rejected as an architecture requirement |

## Translation Chain

The complete research trail is:

```text
published BabyX mechanism
  -> source claim recorded
  -> limitation recorded
  -> Velvet inference identified
  -> Adopt / Adapt / Reject decision
  -> Velvet law applied
  -> repository ownership assigned
  -> test and promotion gate defined
```

## What Is Not Claimed

This source map does not claim:

- that BabyX is conscious
- that Velvet will become conscious by using similar mechanisms
- that Velvet reproduces BabyX's neural models
- that the source publications prove Velvet's implementation will work
- that biological terminology grants scientific legitimacy to a software variable
- that virtual-body results are sufficient evidence for physical authority

## Derived Velvet Documents

- [BabyX Architecture Clues for Velvet](babyx_architecture_clues.md)
- [Cognitive Event Layer](../cognitive_event_layer.md)
- [Cognitive Event Layer Integration Plan](../cognitive_event_integration_plan.md)
- [Ecosystem Overview](../ecosystem_overview.md)
- [Events, Intents, and Receipts](../events_intents_and_receipts.md)
- [Continuity and Identity](../continuity_and_identity.md)
- [Temporal Logic Doctrine](../../architecture/temporal_logic_doctrine.md)

## Review Rule

When a future BabyX source is added, the update must state:

1. what the source directly claims
2. what limitation applies
3. what Velvet infers
4. what Velvet decides
5. which document, schema, test, or repository changes as a result

A citation beside a finished doctrine is not enough. The transformation must remain inspectable.
