# Event Protocol, Court, and Receipts Lineage

Status: first-pass provenance reconstruction

Provenance state: `RECONSTRUCTED`, `CONVERGENT`, with confirmed internal implementation history

## Recovered Architectural Law

Velvet separates four things that earlier prototypes and ordinary automation systems often collapse:

```text
observation or request
  -> interpretation and proposal
  -> authorization
  -> execution
  -> receipt and consequence
```

The current ecosystem expresses this separation through:

- Event Protocol for typed observations and lifecycle records
- AI Core and organs for interpretation and bounded proposals
- Runtime for verified context and coordination
- Court for authorization
- approved executors for physical or privileged action
- Receipts for immutable decision, execution, and outcome evidence

## Earliest Recovered Design Family

Archived system plans used an auditable event-bus structure with concepts resembling:

- `ActionRequest`
- `ActionGrant`
- `ActionDenial`
- `ExecutionReceipt`
- read-only observation paths
- explicit execution boundaries

The same planning period discussed CAN, OBD-II, AUTOSAR, Qt, Android Automotive, offline speech, local AI, and vehicle-control boundaries.

This confirms that the architecture developed through practical vehicle-system design rather than appearing fully formed in one later doctrine document.

## What Is Confirmed

The following are confirmed internal Velvet decisions:

- events do not grant authority
- model confidence does not grant authority
- memory does not grant authority
- owner recognition evidence does not itself execute an action
- capability-bearing execution must be separate from interpretation
- denied actions and non-actions deserve records
- receipts preserve what was decided, attempted, observed, contradicted, or left unknown
- replay and simulation must not be confused with live execution

## Likely Engineering Families

The architecture is convergent with or likely informed by several established engineering families:

### Event-driven architecture

Components communicate through explicit events rather than hidden direct calls.

### Event sourcing and append-only audit logs

History is preserved as records rather than rewritten into a convenient present state.

### Capability-based security

Possessing information or producing a request is different from holding a narrow capability to perform an action.

### Policy and mechanism separation

Court-like policy decisions remain distinct from the executors and mechanisms that perform work.

### Safety-case and assurance records

Important actions require evidence explaining why they were allowed, denied, attempted, completed, or left uncertain.

### Automotive request and actuation boundaries

Observation, diagnosis, command authorization, bus access, and actuator execution remain separate concerns.

These are engineering-family comparisons. No surviving record currently proves that a single named source originated Velvet’s complete chain.

## Why Court Exists

Court is not merely an access-control function.

It exists because the same proposed action can have different legitimacy depending on:

- verified owner or guest context
- active body and installation identity
- current session and continuity state
- route and parameter scope
- safety posture
- resource ownership
- replay state
- emergency doctrine
- current physical evidence

Court makes policy accountable. It does not perform the action.

## Why Receipts Exist

Receipts developed beyond ordinary logs because Velvet needed to preserve:

- decisions to act
- decisions not to act
- denials and their reasons
- capability and route references
- executor outcomes
- sensor-confirmed consequences
- contradictions between report and observation
- unknown outcomes
- simulation posture
- continuity and lineage links

A receipt is not a replayable command and not a memory summary.

## Adopt / Adapt / Reject Reconstruction

### Adopt

- typed event envelopes
- append-only evidence
- explicit authorization decisions
- narrow execution contracts
- deterministic replay markers
- trace and correlation identifiers
- records for denial and non-action

### Adapt

- general event buses into authority-free observation transport
- capability security into owner-doctrine and Court-governed physical action
- audit logs into linked decision, execution, outcome, and contradiction receipts
- automotive command paths into retrofit-friendly local APIs
- event sourcing into a system where summaries remain subordinate to source evidence

### Reject

- events that contain their own permission
- clients selecting executors or hardware targets
- LLM-generated commands entering hardware directly
- confidence or consensus becoming authority
- receipt records that can be replayed as actions
- summaries replacing source observations
- silent mutation of past records

## Internal Development Pressures

This architecture appears to have hardened through repeated practical failures and risks:

- direct module wiring created fragile authority paths
- early prototypes mixed local orchestration with authoritative Runtime language
- CAN and relay access required a single protected route
- simulated demonstrations needed to be visibly incapable of physical execution
- private-repository audits found stale write-capable paths and authority drift
- module hot-swapping required capability and promotion boundaries
- emergency systems required standing doctrine without uncontrolled autonomy

## Relationship to Ghost System

Ghost System v0 is an important internal receipt in this lineage.

It joined synthetic CAN, Runtime routing, interface display, Event Protocol, and Receipts in a sealed loop while explicitly declaring that no physical bus was opened, no CAN transmission was attempted, no actuation occurred, and no authority was granted.

Ghost therefore demonstrates how the architecture was used as a safety and recovery mechanism before the Cognitive Event Layer existed.

## Relationship to BabyX

BabyX later contributed event-sized cognition, prediction, interruption, and episode mechanisms.

Those mechanisms sit above the existing authority chain:

```text
Cognitive Event Layer proposes and tracks
  -> Runtime verifies
  -> Court authorizes
  -> executor acts
  -> Receipts preserve
```

BabyX did not originate Court, Receipts, or Velvet’s execution law.

## Remaining Archive Questions

- Which chat first used the word “Court” for authority arbitration?
- When were decision, authorization, execution, and receipt first drawn as separate boxes?
- Was event sourcing named explicitly in early discussions?
- Were capability-security systems or object-capability models discussed directly?
- Which AUTOSAR, Android Automotive, or vehicle-gateway comparisons materially changed the design?
- When did receipts expand from logs into consequence and contradiction evidence?

Until recovered, the correct statement is:

> Velvet’s authority and receipt architecture is a confirmed internal implementation, reconstructed as convergent with event-driven systems, append-only audit practice, capability security, policy-mechanism separation, and automotive safety boundaries. No single external origin is currently proven.