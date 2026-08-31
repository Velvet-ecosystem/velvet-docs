# Velvet Ecosystem Overview

Velvet is not a single chatbot, application, or dashboard. It is a local-first ecosystem of bounded services, surfaces, organs, hardware bodies, memory, policy, communications, knowledge, and receipts.

The central architectural split is simple:

```text
reasoning and language
  -> interpret, explain, and propose

identity, Runtime, and Court
  -> decide authority and policy

safety gates and approved executors
  -> perform bounded action

receipts and continuity
  -> preserve evidence and lineage
```

Urgency can change scheduling. It does not erase those boundaries.

## Main Layers

### Identity and Continuity

Velvet must know which installation, body, owner context, and lineage are active before privileged work begins.

Owned primarily by:

- `velvet-continuity-spine`
- identity, body, profile, session, and Court-context services in `velvet-runtime`

Memory may inform identity. Memory alone does not prove identity.

### Runtime and Authority

Runtime is the local authority and execution nervous system. It owns strict routes/intents, capability context, Court policy, signed bounded tokens, resource coordination, safety gates, approved executors, replay protection, and execution evidence.

Owned primarily by:

- `velvet-runtime`
- `velvet-receipts`

### Local Event Protocol

Event Protocol carries structured observations, requests, decisions, outcomes, and lifecycle changes **inside one governed body**. Events describe what happened or what is requested. They do not create authority.

Owned by:

- `velvet-event-protocol`

Event Protocol does not own cross-body V2V carriage, carrier selection, relays, or off-grid routing.

### Communications and Federation

Communications begins at the cross-node/cross-body boundary. It carries bounded Velvet payloads between separately governed nodes or bodies without changing their meaning, trust, or authority.

Owned by:

- `velvet-communications`

Its responsibilities include:

- V2V envelopes and peer addressing;
- carrier capability descriptions and selection;
- bounded retries, TTL, hop limits, replay suppression, and store-and-forward;
- degraded/off-grid carriage;
- adapters for local IP, secure overlays, LoRa, Meshtastic, private LoRaWAN/ChirpStack, serial, cellular, and future carriers;
- Beacon of Hope emergency-fallback contracts;
- communications privacy/disclosure boundaries.

Core laws:

> **The message belongs to Velvet. The carrier is replaceable.**

> **Connectivity is a capability, not consent.**

Discovery is not trust. Relay is not authority. Carrier availability is not permission to transmit owner data.

### Core Intelligence

Reasoning, belief/context handling, canonical memory primitives, reflection, learning/plasticity boundaries, and structured proposals live in:

- `velvet-ai-core`

Core may interpret, remember, learn within governed boundaries, and propose. It does not authorize or execute physical action.

### Language

Language receives verified meaning and bounded context and turns them into truthful human expression.

Owned by:

- `velvet-language`

Language does not own canonical truth, memory, authority, or audio hardware. Generative assistance is optional, and generative freedom decreases as consequence increases. Critical/emergency expression is deterministic or nearly deterministic.

### Audio

Audio Studio owns the shared local acoustic hardware/software boundary.

Owned by:

- `velvet-audio-studio`

It coordinates microphone capture, bounded local Vosk transcription, Piper synthesis, channel leases, routing, priority/preemption, speaker delivery, and audio-output evidence. Software contracts are implemented; final Raspberry Pi + Audio Injector Octo physical acceptance remains separate evidence work.

Language owns wording. Audio owns rendering. Neither gains Runtime/Court authority merely because Velvet can speak.

### Knowledge and Library

Velour's Library is the canonical provenance-aware local knowledge archive.

Owned by:

- `velours_library`

It owns guarded ingestion, source preservation, provenance, source lifecycle, retrieval evidence, portable knowledge packs, quarantine, adoption, and pack lifecycle.

> **Retrieval is not belief.**

A retrieved passage is evidence for reasoning, not automatic world truth or execution authority.

### Cognitive Event Layer

The Cognitive Event Layer binds related observations into a bounded representation of what appears to be happening now. It may track event boundaries, predictions, interruptions, authorized-action outcomes, and evidence-linked episode proposals.

It is connective tissue inside the Unified-Organ body, not a new sovereign agent or authority source.

```text
observations
  -> current cognitive event
  -> bounded proposal
  -> Runtime and Court
  -> approved execution
  -> observed outcome and receipts
  -> episode consolidation
```

Owned across bounded responsibilities by:

- `velvet-event-protocol`
- `velvet-ai-core`
- `velvet-runtime`
- `velvet-receipts`
- `velvet-continuity-spine`

See [Cognitive Event Layer](cognitive_event_layer.md).

### Vehicle Observation

Vehicle CAN observation is receive-only by default. Raw evidence and decoded interpretation remain separate products.

Owned by:

- `velvet-vehicle-can`
- read-only observation routes in `velvet-runtime`

### Interface and Surfaces

Scenes and widgets render context and route intent. They do not actuate hardware directly.

Owned by:

- `velvet-interface`

## Emergency Continuity Path

Verified emergencies can enter a life-safety lane ahead of ordinary work while preserving governance.

```text
verified emergency / accident / trusted manual emergency start
  -> life-safety rank 0
  -> responder request remains authority-free evidence
  -> incident-action policy
  -> canonical capability + logical target resolver
  -> incident-scoped emergency Court identity
  -> strict Court Intent
  -> Court authorization
  -> future safety / executor / physical target binding
  -> measured execution
  -> receipts
```

Important boundaries:

- rank 0 means **consider first**, not **approve automatically**;
- unverified emergency claims receive no life-safety priority;
- the emergency incident gets its own Court identity rather than borrowing the owner's active session;
- responder voice, phone connection, or carrier remains provenance, not authority;
- visibility and rescue-access use separate least-privilege Court policy families;
- steering, throttle, braking, shifting, propulsion, and engine control remain outside the responder-conversation path;
- Court authorization is not execution.

The public path currently stops before a real emergency lock/light executor, hardware safety binding, and measured vehicle actuation.

See Runtime's `emergency_first_action_eligibility.md`, `incident_action_policy.md`, `incident_action_resolver.md`, and `incident_court_binding.md` for the implementation contracts.

## Information Boundary: Local vs Cross-Body

```text
inside one governed body
-----------------------
sensor/service
  -> Event Protocol
  -> Core / Runtime / Language / Interface / Audio
  -> Receipts / Continuity

cross-body or cross-node
------------------------
approved bounded payload
  -> Communications
  -> selected carrier
  -> peer endpoint
  -> receiving body's own identity / relationship / Runtime / Court checks
```

Transport never upgrades authority.

## Velvet Coin and Drive-Fi

Velvet Coin and Drive-Fi are acknowledged as an early economic, ownership, participation, safety, and evidence branch of the ecosystem.

The coin remains live outside Velvet's present operational architecture and may retain potential future utility or value. It is not currently a Runtime dependency, authority source, safety mechanism, active reward system, or physical-control path. Potential value is not guaranteed value, and live status does not mean approved integration.

Coin and wallet integration was deliberately deferred while Velvet built the identity, Court, receipts, continuity, sensor confidence, package trust, anti-replay, anti-gaming, privacy, and dispute-evidence foundations that accountable value would require.

See [Velvet Coin and Drive-Fi Origin Lineage](research/velvet_coin_drivefi_origin_lineage.md).

## Canonical Execution Law

```text
input
  -> verified identity and context
  -> strict intent schema
  -> Court authority and policy check
  -> bounded capability token
  -> matching safety gate
  -> approved executor
  -> measured outcome
  -> execution receipt
  -> result event
```

Any shortcut around this path is a doctrine violation.

## Observation Is Not Actuation

Velvet may observe the host, vehicle, room, body, passenger state, environment, carrier state, or retrieved knowledge without gaining permission to control them.

Observation paths must remain explicitly bounded. If an observation later motivates action, a new intent begins at the authority boundary.
