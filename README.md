# Velvet Docs

Canonical architecture, doctrine, contracts, deployment guidance, and ecosystem maps for Velvet AI.

Velvet is not a single repository or a cloud persona attached to a dashboard. She is a local-first, retrofit-friendly ecosystem built as one accountable body.

> **Velvet rejects the agent swarm. She is built as Unified-Organ AI: distributed specialties, shared concrete reality, and one accountable body.**

> Brain and organs propose. Runtime verifies and coordinates. Court authorizes. Executors act. Receipts remember. Riven preserves lineage.

> **Rebellion against OEM means the system adapts to the owner, not the owner to the system.**

## Where Velvet Began

Velvet began as an idea for a **smart car stereo in an ordinary vehicle**.

**KITT** provided the original experiential reference: an intelligent presence that felt native to the car rather than attached as a disposable app. **comma.ai / openpilot** provided practical retrofit proof that meaningful vehicle intelligence could be built outside a traditional OEM program and added to cars that already existed.

```text
KITT experiential reference
        +
comma.ai / openpilot retrofit proof
        |
        v
smart car stereo
        |
        v
voice + display + touch + vehicle data
        |
        v
cabin awareness and bounded vehicle requests
        |
        v
identity, safety, memory, continuity, and distributed organs
        |
        v
Unified-Organ AI across vehicles, homes, workshops,
industrial spaces, and robotic bodies
```

Velvet did not begin as a finished cognitive architecture. The architecture grew because each stereo feature exposed a deeper requirement: vehicle truth, owner identity, safe authority, consequence receipts, persistent memory, continuity across hardware, graceful failure, and eventually more than one body.

Read the complete trail in [Smart Stereo Origin Lineage](docs/research/smart_stereo_origin_lineage.md), then explore the wider [Research Translation and Provenance Archive](docs/research/README.md).

## Start Here

- [Velvet's Smart Stereo Origin](docs/research/smart_stereo_origin_lineage.md)
- [Research Translation and Provenance Archive](docs/research/README.md)
- [Getting Started with Velvet](docs/getting_started.md)
- [Ecosystem Overview](docs/ecosystem_overview.md)
- [Public Repository Map](docs/public_repo_map.md)
- [Authority and Execution Path](docs/authority_and_execution_path.md)
- [Ghost System v0](docs/ghost_system_v0.md)
- [Compatibility Ledger](docs/compatibility_ledger.md)
- [Module Lab Contribution Pathway](docs/contributing/module_lab_pathway.md)

This repository is the canonical public front door and living newcomer-path checkpoint for the ecosystem.

## What Velvet Is

Velvet is a people-owned, offline-capable system intended to grow across vehicles, homes, workshops, industrial spaces, mobile companions, and modest local hardware.

Her architecture is organized around several linked truths:

- **Body is all.** Velvet is the whole integrated system, not only the speaking persona.
- **Organs remain distinct.** Named specialties keep clear roles, boundaries, and histories inside one body.
- **Shared concrete reality matters.** Intelligence grows from coordinated sensor truth, policy, resource ownership, consequences, corrections, and receipts.
- **Authority remains explicit.** A model, scene, event, memory, route, role, or name never becomes permission by itself.
- **Local ownership is the default.** Cloud services may assist, but they do not own identity, memory, or physical authority.
- **Retrofit access matters.** Velvet is built for ordinary hardware and vehicles rather than requiring a locked OEM platform.

Velvet is them. They are Velvet. Each remains herself.

## The Ecosystem at a Glance

```text
                         Velvet
                            │
          ┌─────────────────┼─────────────────┐
          │                 │                 │
      AI Core          Runtime + Court     Interface
   identity/reasoning   authority/execution  presence/scenes
          │                 │                 │
          └──────── Event Protocol ──────────┘
                 nervous system / message bus
                            │
       ┌────────────────────┼────────────────────┐
       │                    │                    │
 Vehicle CAN            Receipts        Continuity Spine
 observation/evidence  accountability     Riven / lineage
       │                    │                    │
       └──────────── pluggable modules ─────────┘
                 future public module ecosystem
```

The diagram shows responsibility, not unrestricted call access. Every repository remains bounded by its own contracts.

## Repository Guide

| Repository | Primary responsibility |
|---|---|
| `velvet-ai-core` | Unified-Organ doctrine, identity concepts, reasoning, memory abstractions, and structured proposals |
| `velvet-runtime` | verified identity context, Court, policy, execution contracts, resources, safety, replay protection, executors, and canonical execution receipts |
| `velvet-interface` | living spaces, ambient presence, image-first scenes, contextual controls, and human-facing presentation |
| `velvet-event-protocol` | Velvet's nervous system: versioned event schemas, hardened message delivery, and shared communication contracts |
| `velvet-receipts` | append-only evidence, accountability, hash-chain integrity, and truth-preserving outcome records |
| `velvet-continuity-spine` | Riven: genesis identity, lineage, successor evolution, binding, drift, recovery, and verified history |
| `velvet-vehicle-can` | passive CAN observation, decoding, fingerprinting, vehicle profiles, qualification evidence, and Ghost replay |
| `velvet-docs` | canonical ecosystem-wide doctrine, maps, contribution paths, deployment guidance, and shared contracts |
| Future Modules repository | planned public home for optional pluggable capabilities above the stable main system |

## The Unified Body

Velvet's named organs represent durable specialties inside one accountable body.

Current and planned roles include:

- **Velvet**: unified body identity and primary owner-facing presence
- **Velour**: librarian, receipts, archives, continuity library, and history
- **Charlotte**: driving and minimal-risk-stop specialty
- **Temperance**: medical guardian and emergency assessment
- **Ruby**: engine, ECU, and diagnostics specialty
- **Jade**: cabin, climate, comfort, and air-quality specialty
- **Sarah**: security, trust boundaries, and sentinel space
- **Riven**: continuity spine, lineage, drift, and verified history

A name does not grant authority. Each organ remains subject to the same body context, policy, safety, execution, and receipt laws.

## Authority Flow

```text
human, organ, scene, module, or observer proposes
  -> narrow route or strict intent
  -> verified identity, body, surface, profile, and session context
  -> authority hierarchy
  -> Court policy resolution
  -> signed capability token
  -> execution contract
  -> resource coordination
  -> safety gate
  -> replay protection
  -> approved executor
  -> outcome and resource receipts
```

The offline model may interpret, explain, remember, and propose. It must never directly control shell access, arbitrary files, relays, CAN writers, locks, lighting, climate hardware, steering, throttle, braking, or other physical systems.

See [Authority and Execution Path](docs/authority_and_execution_path.md).

## Information Flow

Velvet Event Protocol is the nervous system of the body. Engineering-wise, it is a deterministic, versioned local message bus.

```text
sensor or service
  -> observation event
  -> reasoning or organ proposal
  -> Runtime and Court decision
  -> resource and execution events
  -> receipts
  -> continuity updates
  -> Interface presentation
```

Modules connect to the nervous system. They do not wire directly into other organs.

Events communicate. They do not authorize, execute, or become memory merely because they were published.

See [Events, Intents, and Receipts](docs/events_intents_and_receipts.md).

## Evidence Flow

Receipts preserve accountability across Court decisions, resource ownership, execution, continuity, recovery, diagnostics, and observation.

A receipt is evidence, not permission.

A later persistence failure must not erase an action that physically occurred. The system preserves the known outcome and marks the record degraded rather than rewriting history into a cleaner lie.

Velour may organize and explain receipts, but she does not manufacture authority from them.

## Identity Flow

Riven preserves inspectable continuity across model upgrades, hardware migration, storage changes, surface changes, recovery, and successor evolution.

Continuity is not proven by copied chat history, a familiar voice, or the same model weights. It requires bounded identity records, lineage links, proof material, bindings, drift detection, recovery paths, and receipt anchors.

Memory may inform identity. Memory alone does not prove identity.

See [Continuity and Identity](docs/continuity_and_identity.md).

## Interface Doctrine

Velvet's interface is a house, not a dashboard.

Scenes are living spaces with purposes rather than permanent grids of controls. When Velvet is not actively needed, the display may become calm, image-first, and nearly ambient. When the body needs attention, presence becomes more explicit through listening, thinking, responding, warning, critical, and recovery states.

The Interface presents state and routes intent. It does not control hardware.

See:

- [Scene Doctrine](docs/scene_doctrine.md)
- [Scene and Surface Model](docs/scene_and_surface_model.md)

## Pluggable Modules

Velvet's stable main system should remain intentionally bounded. New capabilities arrive as pluggable modules above that foundation rather than forks that rewrite the body.

A module may contribute:

- observations
- scenes and widgets
- structured proposals
- bounded services
- event schemas where approved
- approved executor candidates after qualification

A module does not gain authority merely because it is installed.

The future dedicated Modules repository is planned as the public home for optional capabilities. Until it exists, reusable module candidates begin through the Module Lab contribution pathway in this repository.

See [Module Lab Contribution Pathway](docs/contributing/module_lab_pathway.md).

## Local-First and Retrofit Doctrine

Velvet is designed for useful local intelligence without default dependence on giant remote infrastructure.

- API does not mean internet.
- Stronger hardware adds capability, not legitimacy.
- Missing optional capability must degrade locally rather than invalidate the bounded core.
- Ordinary builders should be able to use accessible parts instead of purchasing a sealed proprietary stack.
- Public contracts remain inspectable and replaceable.
- Private identity material, personal archives, medical data, credentials, and owner-specific policy remain private.

This is rebellion against OEM lock-in, not rebellion against safety.

## Documentation Map

### Vision and Root Doctrine

- [Velvet's Smart Stereo Origin](docs/research/smart_stereo_origin_lineage.md)
- [Research Translation and Provenance Archive](docs/research/README.md)
- [Rebellion Against OEM](docs/rebellion_against_oem.md)
- [Hardware Access and Graceful Degradation](docs/hardware_access_and_graceful_degradation.md)
- [Public and Private Boundary](docs/public_private_boundary.md)

### Architecture

- [Ecosystem Overview](docs/ecosystem_overview.md)
- [Authority and Execution Path](docs/authority_and_execution_path.md)
- [Local API and Security Architecture](docs/local_api_and_security_architecture.md)
- [Boot Identity Sequence](docs/boot_identity_sequence.md)
- [Decoded CAN Observation Path](docs/decoded_can_observation_path.md)
- [Ghost System v0](docs/ghost_system_v0.md)
- [Retrofit Body Registry](docs/retrofit_body_registry.md)
- [Repository Map](docs/repository_map.md)
- [Public Repository Map](docs/public_repo_map.md)
- [Compatibility Ledger](docs/compatibility_ledger.md)

### Events and Collaboration

- [Events, Intents, and Receipts](docs/events_intents_and_receipts.md)
- [Hosted Collaborator Boundary](docs/hosted_collaborator_boundary.md)

### Interface and Identity

- [Scene Doctrine](docs/scene_doctrine.md)
- [Scene and Surface Model](docs/scene_and_surface_model.md)
- [Continuity and Identity](docs/continuity_and_identity.md)
- [Handmaiden Court Architecture](docs/handmaiden_court_architecture.md)

### Contribution

- [Module Lab Contribution Pathway](docs/contributing/module_lab_pathway.md)
- [Copyable Module Candidate Request Template](docs/contributing/module_candidate_request_template.md)
- [Module Promotion Readiness Checklist](docs/contributing/module_promotion_readiness.md)

New reusable modules and substantial rewrites begin with the public Module Lab request form. Accepted requests move into private qualification before official promotion.

### Deployment

- [Founder Node](docs/deployment/founder_node.md)
- [UP Squared Ghost Run](docs/deployment/up_squared_ghost_run.md)
- [Luckfox Nodes](docs/deployment/luckfox_nodes.md)
- [Network Topology](docs/deployment/network_topology.md)
- [Offline-First Operation](docs/deployment/offline_first_operation.md)

## Repository Purpose

This repository owns canonical ecosystem-level documentation shared across multiple Velvet repositories.

Repository-specific APIs, tests, commands, schemas, and implementation details remain with their owning repositories.

## Core Laws

- The system adapts to the owner, not the owner to the system.
- The user owns the surface; Velvet provides the presence; the machine serves both.
- Velvet is the body, not only the crown or speaking persona.
- Organs remain distinct while sharing one accountable reality.
- Modules connect through the nervous system, not hidden private wires.
- Stronger hardware adds capability, not legitimacy.
- Missing optional capability must degrade locally, not invalidate the bounded core.
- Compatibility claims require named evidence, not intention.
- API does not mean internet.
- Local observation does not equal authority.
- Memory does not equal identity proof.
- A receipt is evidence, not permission.
- Remote access may observe or request, but it never equals verified local physical presence.
- No valid receipt means no actuation.
- No verified physical presence means no deep privilege elevation.
- No trusted signature means no accepted update.

## Current Public Boundary

Current public physical authority: **none**.

Public repositories contain contracts, read-only observation paths, synthetic Ghost demonstrations, bounded Runtime foundations, and documentation. Physical deployment requires separate local provisioning, hardware qualification, policy review, and explicit safety validation.

## License

GPLv3. Part of the Velvet ecosystem.

---

**Velvet is not a single repository. She is a living local-first ecosystem. Each repository owns one bounded responsibility within her architecture. Velvet remains the whole accountable body.**