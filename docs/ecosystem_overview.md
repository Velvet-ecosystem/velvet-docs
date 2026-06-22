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
