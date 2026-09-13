# Velvet Docs

Canonical architecture, doctrine, contracts, deployment guidance, and ecosystem maps for Velvet AI.

Velvet is not a single repository or a cloud persona attached to a dashboard. She is a local-first, retrofit-friendly ecosystem built as one accountable body.

> **Velvet rejects the agent swarm. She is built as Unified-Organ AI: distributed specialties, shared concrete reality, and one accountable body.**

> Brain and organs propose. Runtime verifies and coordinates. Court authorizes. Executors act. Receipts remember. Riven preserves lineage.

> **Rebellion against OEM means the system adapts to the owner, not the owner to the system.**

## Where Velvet Began

Velvet began as an idea for a **smart car stereo in an ordinary vehicle**.

**KITT** provided the original experiential reference: an intelligent presence native to the car. **comma.ai / openpilot** provided practical retrofit proof that meaningful vehicle intelligence could be built outside a traditional OEM program and added to cars that already existed.

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
identity, safety, memory, continuity, communications,
knowledge, language, audio, and distributed organs
        |
        v
Unified-Organ AI across vehicles, homes, workshops,
industrial spaces, mobile systems, and robotic bodies
```

Velvet did not begin as a finished cognitive architecture. The architecture grew because each feature exposed a deeper requirement: vehicle truth, owner identity, safe authority, consequence receipts, persistent memory, continuity across hardware, truthful language, local speech, privacy-preserving communication, provenance-aware knowledge, graceful failure, and eventually more than one body.

Read the complete trail in [Smart Stereo Origin Lineage](docs/research/smart_stereo_origin_lineage.md), then explore the wider [Research Translation and Provenance Archive](docs/research/README.md).

## Start Here

- [Getting Started with Velvet](docs/getting_started.md)
- [Ecosystem Overview](docs/ecosystem_overview.md)
- [Repository Map](docs/repository_map.md)
- [Public Repository Map](docs/public_repo_map.md)
- [Library, Vault, and Reader Path](docs/library_vault_and_reader_path.md)
- [Machine-Readable Ecosystem Map](ecosystem.yaml)
- [Machine-Readable Ecosystem Guide](docs/machine_readable_ecosystem.md)
- [Ecosystem JSON Schema](schemas/velvet-ecosystem.schema.json)
- [Authority and Execution Path](docs/authority_and_execution_path.md)
- [Ghost System v0](docs/ghost_system_v0.md)
- [Compatibility Ledger](docs/compatibility_ledger.md)
- [Module Lab Contribution Pathway](docs/contributing/module_lab_pathway.md)
- [Smart Stereo Origin Lineage](docs/research/smart_stereo_origin_lineage.md)
- [Research Translation and Provenance Archive](docs/research/README.md)

This repository is the canonical public front door and living newcomer-path checkpoint for the ecosystem.

The September 2026 compatibility record remains a frozen exact-source proof record. Newer Character Foundry Interface, Library Reader, and private Cyberdeck library-tooling changes post-date that composition and are not retroactively covered by it.

## What Velvet Is

Velvet is a people-owned, offline-capable system intended to grow across vehicles, homes, workshops, industrial spaces, mobile companions, local knowledge archives, communications links, and modest local hardware.

Her architecture is organized around several linked truths:

- **Body is all.** Velvet is the whole integrated system, not only the speaking persona.
- **Organs remain distinct.** Named specialties keep clear roles, boundaries, and histories inside one body.
- **Shared concrete reality matters.** Intelligence grows from coordinated sensor truth, policy, resource ownership, consequences, corrections, and receipts.
- **Authority remains explicit.** A model, scene, event, memory, route, role, transport, or name never becomes permission by itself.
- **Local ownership is the default.** Cloud services may assist, but they do not own identity, memory, or physical authority.
- **Retrofit access matters.** Velvet is built for ordinary hardware and vehicles rather than requiring a locked OEM platform.
- **Connectivity is a capability, not consent.** Reachability never silently becomes tracking, disclosure, trust, or authority.
- **Emergency priority removes avoidable delay, not governance.** Verified life-safety work can go first while Court, safety, executor, and receipt boundaries remain intact.

Velvet is them. They are Velvet. Each remains herself.

## The Ecosystem at a Glance

Event Protocol and Communications now have deliberately different jobs. Event Protocol is the local governed nervous system inside one body. Communications owns cross-node and cross-body carriage after a bounded payload reaches that boundary.

```text
                               Velvet
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
        AI Core             Runtime + Court          Interface
   reasoning / memory       authority / policy      scenes / intent
            │                     │                     │
            └────────────── Event Protocol ─────────────┘
                    local governed nervous system
                ┌──────────────┼──────────────┐
                │              │              │
          Vehicle CAN       Receipts       Language
          observation       evidence       expression
                               │              │
                         Continuity Spine   Audio Studio
                           Riven / lineage   local speech I/O

approved cross-body payload
        -> Communications
        -> LAN / secure overlay / LoRa / Meshtastic / other carrier
        -> separately governed Velvet peer

provenance-aware knowledge
        -> Velour's Library
        -> canonical catalog / retrieval evidence
        -> read-only Interface presentation or Core reasoning
        -> never automatic belief or authority
```

The diagram shows responsibility, not unrestricted call access. Every repository remains bounded by its own contracts.

## Repository Guide

| Repository | Primary responsibility |
|---|---|
| `velvet-ai-core` | Unified-Organ doctrine, reasoning, memory primitives, belief/context handling, learning/reflection boundaries, and structured proposals |
| `velvet-runtime` | verified body/identity context, Court, capability policy, emergency-first scheduling, incident Court binding, execution contracts, safety, replay protection, executors, and execution receipts |
| `velvet-interface` | living spaces, ambient presence, image-first scenes, contextual controls, trusted workspace presentation, and read-only catalog-backed Library presentation |
| `velvet-event-protocol` | versioned local event schemas and hardened message delivery inside one governed body |
| `velvet-communications` | transport-neutral cross-node/cross-body carriage, V2V federation, carrier selection/fallback, relays, degraded/off-grid delivery, Beacon of Hope, and communications privacy boundaries |
| `velvet-language` | meaning-before-speech language, bounded conversation, truthful expression, deterministic critical/emergency wording, and optional generative assistance |
| `velvet-audio-studio` | local microphone capture, Vosk transcription, Piper synthesis, channel leases, speaker routing, priority/preemption, and audio-output evidence |
| `velours_library` | canonical provenance-aware local knowledge archive, guarded ingestion, source lifecycle, retrieval evidence, portable packs, quarantine, and adoption |
| `velvet-receipts` | append-only evidence, accountability, hash-chain integrity, and truth-preserving outcome records |
| `velvet-continuity-spine` | Riven: genesis identity, lineage, successor evolution, binding, drift, recovery, and verified history |
| `velvet-vehicle-can` | passive CAN observation, decoding, fingerprinting, vehicle profiles, qualification evidence, and Ghost replay |
| `velvet-docs` | canonical ecosystem-wide doctrine, maps, contribution paths, deployment guidance, and shared contracts |
| `.github` | organization profile and public contributor-facing defaults |
| `business_agent_ecosystem` | public adjacent application/reference ecosystem; not a replacement for the shared authority or body organs |

The private experimental/deployment repositories remain intentionally outside this public responsibility map until their own publication gates are met. Current private examples include Persona Continuity, Cyberdeck, Navigation, Home, Medical Mobility, Retrofit Architecture, and Module Lab.

## The Unified Body

Velvet's named organs represent durable specialties inside one accountable body.

Current and planned roles include:

- **Velvet**: unified body identity and primary owner-facing presence
- **Velour**: librarian, archives, knowledge provenance, receipts, and history
- **Charlotte**: driving and minimal-risk-stop specialty
- **Temperance**: medical guardian and emergency assessment
- **Ruby**: engine, ECU, and diagnostics specialty
- **Jade**: cabin, climate, comfort, and air-quality specialty
- **Sarah**: security, trust boundaries, and sentinel space
- **Riven**: continuity spine, lineage, drift, and verified history

A name does not grant authority. Each organ remains subject to the same body context, policy, safety, execution, and receipt laws.

## Authority Flow

The ordinary consequential path remains:

```text
human, organ, scene, module, or observer proposes
  -> narrow route or strict intent
  -> verified identity, body, surface, profile, and session context
  -> canonical Court authority
  -> Court policy resolution
  -> bounded capability token
  -> execution contract
  -> resource coordination
  -> safety gate
  -> replay protection
  -> approved executor
  -> measured outcome and receipts
```

The offline model may interpret, explain, remember, and propose. It must never directly control shell access, arbitrary files, relays, CAN writers, locks, lighting, climate hardware, steering, throttle, braking, or other physical systems.

See [Authority and Execution Path](docs/authority_and_execution_path.md).

## Emergency Continuity

Verified emergencies now receive a dedicated life-safety scheduling lane without bypassing governance.

```text
verified emergency / accident / trusted manual emergency start
  -> life-safety rank 0
  -> responder request remains authority-free evidence
  -> incident-action policy
  -> capability + logical-target resolver
  -> incident-scoped emergency Court identity
  -> strict Court Intent
  -> Court authorization
  -> future safety / executor / hardware binding
  -> measured result + receipts
```

The incident receives its own temporary Court identity. It does not borrow the owner's active session. A responder's voice, carrier, or phone connection does not itself create authority.

Current public Runtime work reaches Court authorization for bounded logical visibility/access requests. **Court authorization is permission to approach the executor boundary; it is not proof that anything moved.** Real vehicle executor binding and measured physical action remain future work.

## Information Flow

Velvet Event Protocol is the nervous system **inside one governed body**. Engineering-wise, it is a deterministic, versioned local message bus.

```text
sensor or local service
  -> observation event
  -> reasoning or organ proposal
  -> Runtime and Court decision
  -> local result / evidence event
  -> receipts
  -> continuity updates
  -> Interface / Language / Audio
```

Cross-body traffic is different:

```text
approved bounded payload
  -> velvet-communications
  -> selected carrier
  -> peer endpoint
  -> receiving body's identity / relationship / Runtime / Court checks
```

Modules connect to the local nervous system. They do not wire directly into other organs. Events communicate; they do not authorize, execute, or become memory merely because they were published.

## Communications and Privacy

Velvet Communications exists for V2V, cross-node/cross-body carriage, carrier selection/fallback, relays, degraded links, off-grid delivery, and emergency communication continuity.

Its central laws include:

> **The message belongs to Velvet. The carrier is replaceable.**

> **Connectivity is a capability, not consent.**

Normal operation is private/local by default. A reachable network, phone, radio, Home node, mesh, or peer does not authorize continuous location upload, owner tracking, medical-state export, cabin telemetry, or physical action.

Beacon of Hope provides a bounded last-resort off-grid emergency fallback. A sent or heard beacon is not proof that emergency services received it. The future Owner Emergency Bridge may use a paired owner phone as a carrier without turning that phone into an authority source.

## Language and Audio

`velvet-language` transforms verified meaning into truthful human language. Language competence may grow through governed experience, and generative models remain optional rather than foundational. Generative freedom decreases as consequence increases; emergency expression becomes deterministic or nearly deterministic.

`velvet-audio-studio` owns the local acoustic device boundary: capture, Vosk transcription, Piper synthesis, channel leases, speaker routing, priority/preemption, and output evidence. The software path is ahead of final Raspberry Pi + Audio Injector Octo physical acceptance, and the documentation says so explicitly.

Language owns wording. Audio owns acoustic rendering. Neither gains Runtime/Court authority merely because Velvet can speak.

## Knowledge and Velour

`velours_library` is the canonical shared local-first knowledge archive. It preserves source evidence, acquisition/transformation history, lifecycle state, provenance, retrieval location, and portable knowledge-pack history.

> **Retrieval is not belief.**

> **Derived text is not the canonical source payload.**

A source can be found, cited, moved, superseded, or adopted without silently becoming trusted world truth or execution authority. Reasoning remains responsible for what it concludes from the shelves.

Current implementation support is deliberately split by responsibility:

```text
Velour's canonical Library
  -> provenance + catalog + retrieval evidence

private Cyberdeck deployment tooling
  -> bounded local adapters
  -> PDF / EPUB / HTML / ZIM handling
  -> scan-first batch shelving
  -> website mirror integrity
  -> local Kiwix planning

public Interface
  -> Scroll-backed read-only Library Reader
  -> catalog-first search / metadata / preview
```

Private deployment tooling does not become a second Library organ. The Interface does not mutate the canonical source/catalog or turn a rendered page into trusted truth.

See [Library, Vault, and Reader Path](docs/library_vault_and_reader_path.md).

## Evidence and Continuity

Receipts preserve accountability across Court decisions, resource ownership, execution, continuity, recovery, diagnostics, communication outcomes, and observations.

A receipt is evidence, not permission.

Riven preserves inspectable continuity across model upgrades, hardware migration, storage changes, surface changes, recovery, and successor evolution. Memory may inform identity; memory alone does not prove identity.

## Interface Doctrine

Velvet's interface is a house, not a dashboard.

Scenes are living spaces with purposes rather than permanent grids of controls. The Interface presents state and routes intent. It does not control hardware.

The current public Interface also includes trusted full-screen workspaces:

- **Character Foundry** is registered in the Founder launcher as a fail-closed client over its canonical backend. Permanent Forge-room hotspot placement remains on-device work.
- **Library Reader** is a read-only Scroll-backed catalog browser/reader. Its scene, catalog-aware provider, and reusable registration helper are merged; the final main Founder-launcher registration call and Archive-room hotspot remain follow-on work.

A visible workspace is not authority. Character Foundry cannot grant capabilities or merge/deploy a candidate, and Library Reader content cannot grant trust or physical permission.

See [Scene Doctrine](docs/scene_doctrine.md), [Scene and Surface Model](docs/scene_and_surface_model.md), and [Library, Vault, and Reader Path](docs/library_vault_and_reader_path.md).

## Pluggable Modules

Velvet's stable main system remains intentionally bounded. New capabilities arrive as pluggable modules above that foundation rather than forks that rewrite the body.

A module may contribute observations, scenes and widgets, structured proposals, bounded services, approved event schemas, or executor candidates after qualification. A module does not gain authority merely because it is installed.

The Module Lab remains private while reusable module candidates begin through the public [Module Lab Contribution Pathway](docs/contributing/module_lab_pathway.md).

## Local-First and Retrofit Doctrine

- API does not mean internet.
- Stronger hardware adds capability, not legitimacy.
- Missing optional capability must degrade locally rather than invalidate the bounded core.
- Ordinary builders should be able to use accessible parts instead of purchasing a sealed proprietary stack.
- Public contracts remain inspectable and replaceable.
- Private identity material, personal archives, medical data, credentials, and owner-specific policy remain private.

This is rebellion against OEM lock-in, not rebellion against safety.

## Documentation Map

### Vision and Root Doctrine

- [Smart Stereo Origin](docs/research/smart_stereo_origin_lineage.md)
- [Research Translation and Provenance Archive](docs/research/README.md)
- [Rebellion Against OEM](docs/rebellion_against_oem.md)
- [Hardware Access and Graceful Degradation](docs/hardware_access_and_graceful_degradation.md)
- [Public and Private Boundary](docs/public_private_boundary.md)

### Architecture

- [Ecosystem Overview](docs/ecosystem_overview.md)
- [Repository Map](docs/repository_map.md)
- [Public Repository Map](docs/public_repo_map.md)
- [Library, Vault, and Reader Path](docs/library_vault_and_reader_path.md)
- [Authority and Execution Path](docs/authority_and_execution_path.md)
- [Local API and Security Architecture](docs/local_api_and_security_architecture.md)
- [Boot Identity Sequence](docs/boot_identity_sequence.md)
- [Decoded CAN Observation Path](docs/decoded_can_observation_path.md)
- [Ghost System v0](docs/ghost_system_v0.md)
- [Retrofit Body Registry](docs/retrofit_body_registry.md)
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

### Deployment

- [Founder Node](docs/deployment/founder_node.md)
- [UP Squared Ghost Run](docs/deployment/up_squared_ghost_run.md)
- [Luckfox Nodes](docs/deployment/luckfox_nodes.md)
- [Network Topology](docs/deployment/network_topology.md)
- [Offline-First Operation](docs/deployment/offline_first_operation.md)

## Repository Purpose

This repository owns canonical ecosystem-level documentation shared across multiple Velvet repositories. Repository-specific APIs, tests, commands, schemas, and implementation details remain with their owning repositories.

## Core Laws

- The system adapts to the owner, not the owner to the system.
- The user owns the surface; Velvet provides the presence; the machine serves both.
- Velvet is the body, not only the crown or speaking persona.
- Organs remain distinct while sharing one accountable reality.
- Modules connect through the nervous system, not hidden private wires.
- Event Protocol is local governed messaging; Communications is cross-node/cross-body carriage.
- Connectivity is capability, not consent.
- Stronger hardware adds capability, not legitimacy.
- Missing optional capability must degrade locally, not invalidate the bounded core.
- Compatibility claims require named evidence, not intention.
- API does not mean internet.
- Local observation does not equal authority.
- Retrieval does not equal belief.
- Derived text does not equal the canonical source payload.
- Memory does not equal identity proof.
- A receipt is evidence, not permission.
- Request origin is evidence, not authority.
- Emergency priority shortens the path to a decision; it does not remove the gates that make the decision safe.
- Court authorization is not measured execution.
- Remote access may observe or request, but it never equals verified local physical presence.
- No valid receipt means no actuation.
- No trusted signature means no accepted update.

## Current Public Boundary

Current public physical authority: **none**.

Public repositories now contain local event, reasoning, language, audio, communications, knowledge, continuity, receipt, interface, CAN-observation, and Runtime/Court foundations. Runtime can make bounded logical Court decisions, including incident-scoped emergency authorization, but the public ecosystem does not claim production vehicle actuation.

Public Interface code can now present a registered Character Foundry workspace and a catalog-backed Library Reader implementation. Those surfaces remain authority-free. The Library Reader's final main Founder-launcher registration call and permanent Archive hotspot are not yet claimed complete, and the public docs do not claim completed on-device Luckfox commissioning.

Physical deployment requires separate local provisioning, hardware qualification, policy review, executor binding, explicit safety validation, and measured physical feedback.

## License

GPLv3. Part of the Velvet ecosystem.

---

**Velvet is not a single repository. She is a living local-first ecosystem. Each repository owns one bounded responsibility within her architecture. Velvet remains the whole accountable body.**