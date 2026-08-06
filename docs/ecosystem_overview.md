# Velvet Ecosystem Overview

Velvet is not a single chatbot, application, or dashboard. It is a local-first ecosystem of bounded services, surfaces, handmaidens, hardware bodies, memory, policy, and receipts.

The central architectural split is simple:

```text
language and reasoning
  -> propose intent

identity and Court
  -> decide authority

safety gates and approved executors
  -> perform bounded action

receipts and continuity
  -> preserve evidence and lineage
```

## Main Layers

### Identity and Continuity

Velvet must know which installation, body, owner context, and lineage are active before privileged work begins.

Owned primarily by:

- `velvet-continuity-spine`
- identity and continuity services in `velvet-runtime`

### Runtime and Authority

Runtime is the local nervous system. It hosts strict routes, policy checks, signed capability tokens, safety gates, approved executors, replay protection, and receipt emission.

Owned primarily by:

- `velvet-runtime`
- `velvet-receipts`

### Event Transport

Events carry observations, requests, decisions, outcomes, and lifecycle changes. They describe what happened or what is requested. They do not create authority.

Owned by:

- `velvet-event-protocol`

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

The layer may improve coherence. It cannot mint capabilities, authorize itself, execute hardware, retry actions, replace receipts, or treat memory as identity proof.

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

### Core Intelligence

Velvet's conversational identity, role logic, memory use, handmaiden coordination, and reasoning live behind the local API boundary.

Owned primarily by:

- `velvet-ai-core`

## Velvet Coin and Drive-Fi

Velvet Coin and Drive-Fi are acknowledged as an early economic, ownership, participation, safety, and evidence branch of the ecosystem.

The coin remains live outside Velvet's present operational architecture and may retain potential future utility or value. It is not currently a Runtime dependency, authority source, safety mechanism, active reward system, or physical-control path. Potential value is not guaranteed value, and live status does not mean approved integration.

Coin and wallet integration was deliberately deferred while Velvet built the identity, Court, receipts, continuity, sensor confidence, package trust, anti-replay, anti-gaming, privacy, and dispute-evidence foundations that accountable value would require.

The early reward concept included reducing or removing reward for dangerous driving or lack of attention. It did not grant software permission over where the owner could travel and did not establish OEM-style geofencing.

The coin is therefore:

- historically foundational
- externally live
- architecturally dormant
- deliberately deferred rather than abandoned

See [Velvet Coin and Drive-Fi Origin Lineage](research/velvet_coin_drivefi_origin_lineage.md).

## Canonical Execution Law

```text
input
  -> identity and context check
  -> strict intent schema
  -> Court authority and policy check
  -> safety gate
  -> approved executor
  -> execution receipt
  -> result event
```

Any shortcut around this path is a doctrine violation.

## Observation Is Not Actuation

Velvet may observe the host, vehicle, room, body, passenger state, or environment without gaining permission to control them.

Observation paths must remain explicitly marked:

```text
status: observation-only
read_only: true
actuation_granted: false
actuation_performed: false
```

If an observation later motivates action, a new intent must begin at the authority boundary.
