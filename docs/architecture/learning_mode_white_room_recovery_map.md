# Learning Mode, White Room, and Dream Layer Recovery Map

## Purpose

This document preserves Velvet's historical self-learning architecture and maps it onto the modern ecosystem after repository archaeology and implementation audit.

It is a recovery and ownership map. It does not create a new authority model.

## Core distinctions

- **Learning Mode** is the governed maintenance state that orchestrates deliberate study.
- **White Room** is the bounded internal cognitive workspace where evidence is compared and candidate understanding is formed.
- **Dream Layer / Dream State** is the slower consolidation phase that revisits accumulated material.
- **self-LM** is the developmental goal: Velvet becomes more capable offline through experience, memory, associations, reflection, governed plasticity, and optional local models.
- **Web Leash** governs outside-network access. It is an input boundary, not the learning system.
- **Web Surface** is user-facing rendering, not a cognitive owner.

## Historical placement

Learning Mode belongs in Velvet's maintenance/back-room architecture, historically described as the Legs, rather than in the front-facing interface.

The durable placement remains:

> Web Surface at the front. Learning machinery down in the Legs. White Room behind the door. Dream Layer deeper still.

The front may expose controls, status, results, Library material, and optional web content. The orchestrator remains internal maintenance machinery.

## Recovery findings

The original architecture was not simply missing. Much of it was implemented incrementally because other parts of Velvet needed the same cognitive machinery first.

The audit found existing modern foundations for:

- bounded cognitive workspaces
- attention and interruption
- deterministic curiosity
- judgment
- pattern and expectation tracking
- contradiction-aware evidence work
- episode consolidation
- Dream State policy
- governed cognitive plasticity
- confidence and freshness
- deterministic associations and backlinks
- memory admission and reviewed promotion
- distributed proposal-only work placement
- Runtime resource protection
- provenance-rich offline Library retrieval

The remaining Learning Mode work is therefore primarily orchestration and integration, not construction of a second brain.

## Native Brain generation ownership

AI Core contains two Native Brain generations.

### Canonical active family

`velvet/core/native_brain/`

This is the canonical Native Brain package for new production-facing cognition. It contains the modern bounded cognition cycle, attention, curiosity, judgment, patterns, expectations, intent candidates, presence, distributed-body proposals, safety boundaries, and related local cognition.

`velvet/core/cognition/` is the canonical deeper cognitive-workspace layer for event workspace, workspace context, consolidation, prediction outcomes, interruption/salience, governed plasticity, and Learning Session orchestration.

### Legacy tested recovery source

`ai_brain/native_brain/`

This earlier deterministic family remains valuable lineage and regression evidence. It preserves the original decision spine, receipt reflection, proposal-only learning, Doctrine of Silence, evidence fusion/freshness, consequence reasoning, and simulated-body practice concepts.

It is not a second canonical runtime brain. New canonical code must not import it as a shortcut. Useful behavior should be deliberately re-expressed under current contracts.

## Ownership and status map

| Historical concept | Modern destination | Audited status |
|---|---|---|
| Learning Mode | `velvet-ai-core` session contracts + `velvet-runtime` eligibility/lifecycle | Session supervisor and Runtime eligibility exist on feature branches; full integration still staged |
| White Room | `velvet/core/cognition` cognitive workspace | Substantially implemented; Learning Mode coordinates existing workspace rather than creating another engine |
| Dream Layer | Dream State policy + episode consolidation + memory consolidation policy | Substantial policy/machinery exists; Learning Mode/Dream integration remains bounded and proposal-only |
| self-LM | governed plasticity + memory lifecycle + associations + optional local models | Bounded modern descendant exists; no uncontrolled self-modification |
| Web Leash / Collar | Runtime/Gateway network capability policy | Remains separate from Learning Mode |
| Web Surface | `velvet-interface` | Separate user-facing capability |
| Curiosity Engine | modern `CuriosityEngine` + Curiosity Budget doctrine | Implemented as deterministic, bounded curiosity machinery |
| Thought Gate | attention, salience, integrated cognition, proposal gating | Function substantially distributed across modern cognition rather than one old-named module |
| Knowledge Intake | memory intake + Library guarded ingestion/admission | Superseded by modern owners |
| Observation Memory | evidence plane + sensor/event records + memory intake | Modern architecture present |
| Knowledge Cards | structured memories / knowledge projections | Evolved form |
| Knowledge Compressor | episode/Dream consolidation proposals | Core functionality substantially represented; no silent canonical rewriting |
| Concept Graph / Memory Veins | deterministic association plane/index | Partially implemented; richer typed/multi-hop graph remains future work |
| Confidence System | confidence + freshness + evidence history | Implemented foundation |
| Conflict Resolver | workspace contradictions + reflection + Persona conflict indexing | Substantial modern equivalent exists |
| Learning Journal | Event Protocol lifecycle + Receipts + reflection evidence | Learning Session event/receipt families staged on feature branches |
| self-LM metrics | learning evaluation/regression layer | Still a later explicit evaluation concern |
| Speaker Reliability | provenance/evidence-quality policy | Remains bounded and should never become hidden source authority |
| Velour / Librarian | `velours_library` + memory indexing + provenance | Modern role established |
| Court | authority boundary | Established |
| Riven | continuity and lineage protection | Established |

## Operating states

### NORMAL

Observe, recall, preserve evidence, and act only through existing authority. Unresolved questions or learning candidates may be retained for later bounded study.

### LEARNING

A bounded maintenance session:

1. Select an unresolved question or explicit study task.
2. Ask Runtime whether a maintenance window is eligible.
3. Allocate bounded session limits.
4. Gather eligible evidence from memory, sensors, Library, conversations, receipts, or separately authorized external material.
5. Associate one or more existing cognitive workspaces with the session.
6. Run bounded reflection/cognition over supporting and conflicting evidence.
7. Form candidate explanations, questions, associations, confidence revisions, revalidation requests, negative-learning notes, or no-change results.
8. Submit candidates through existing review/admission paths.
9. Publish lifecycle evidence through Event Protocol and preserve appropriate Receipts.
10. Close, pause, degrade, or abort the session cleanly.

**Autonomous study is not autonomous promotion.**

A session may finish with uncertainty, conflicting evidence, a revalidation request, insufficient evidence, or no change.

### DREAM

A lower-priority consolidation state may revisit accumulated evidence and candidate understanding to:

- strengthen or weaken associations
- identify stale knowledge
- find contradictions
- consolidate repeated episodes into proposals
- build backlinks and knowledge projections
- reduce retrieval noise
- prepare revalidation tasks

Dream work produces proposals and evidence. It does not silently rewrite receipts, doctrine, identity, capability, or physical authority.

## Learning Session implementation

The current AI Core feature branch defines a finite Learning Session supervisor rather than another cognition loop.

The session tracks bounded lifecycle states including proposed, eligibility check, open, studying, review pending, paused, degraded, completed, aborted, and insufficient evidence.

It coordinates existing cognitive workspaces and candidate outputs while explicitly refusing:

- canonical memory writes
- Runtime placement authority
- Court authority
- execution authority
- physical actuation authority

Readable study objectives remain inside Core. Transport projection exposes stable subject/evidence references and lifecycle facts rather than raw internal study prose.

## White Room boundary

Eligible inputs include:

- immutable evidence and receipts
- admitted memories
- sensor observations
- Library retrieval evidence
- documentation and research material
- previously captured web material
- separately authorized live web material
- specialist-organ reports

Outputs remain proposals such as:

- candidate explanations
- association proposals
- contradiction records
- confidence revisions
- unanswered questions
- revalidation requests
- knowledge projections
- negative-learning candidates
- no-change conclusions

White Room output does not automatically become trusted knowledge, doctrine, identity, capability, or physical authority.

## Runtime maintenance eligibility

Runtime owns the question:

> Is this actually an appropriate moment for Velvet to study?

The staged Runtime eligibility contract requires explicit evidence for operational posture, power posture, background resources, higher-priority work, critical health, continuity, and freshness.

Unknown or stale conditions fail closed.

Important asymmetric rules are preserved:

- fresh GNSS movement may prove `ACTIVE`; zero speed does not prove `QUIET`
- low/critical vehicle power may veto background learning; healthy voltage alone does not grant `BACKGROUND_OK`
- continuity reuses the existing verified boot gate
- resource posture reuses the existing Resource Guard
- critical health is derived only from explicitly named, fresh body evidence

Learning Mode does not invent parked state, power permission, or system priority from one convenient sensor.

## Distributed work

Learning Mode does not create a second work-placement system.

Native Brain may propose bounded reasoning work. Runtime's existing distributed-work layer remains the owner of node selection, leases, handoff, degradation, recovery, and result return.

A Learning Session may retain distributed-work references without granting placement or execution authority itself.

### Ghost boundary

Ghost remains the fake-car / simulated-vehicle system.

Ghost evidence and fixtures may be studied, but their simulated provenance must remain explicit through the Learning Session, Event Protocol, and Receipts.

Ghost handlers must not be repurposed into general Learning Mode workers. Real Library-backed study requires its own reviewed read-only consumer/worker seam.

## Library-backed offline study

Velour's Library is already ready to serve as an offline evidence source.

The Library owns:

- guarded ingestion
- provenance
- source trust metadata
- canonical source hashes
- deterministic chunk identities
- retrieval methods and scores
- source locations
- lifecycle and staleness warnings
- reference-only evidence bundles

Retrieval is not belief.

Learning Mode may consume published Library evidence in a bounded cognitive workspace, but the Library remains the librarian, not the learner.

The first integration must be read-only. A Learning study worker must not gain permission merely through study to stage/publish sources, change trust, alter lifecycle, adopt packs, activate revisions, remove material, or rewrite provenance.

Long-lived Learning Session state should preserve stable Library evidence references rather than silently copying retrieved passages into canonical memory.

Retrieval score and trust class are evidence metadata, not truth confidence.

## Event Protocol and Receipts

Learning Mode lifecycle uses the shared ecosystem nervous system rather than a private event lane.

A versioned Learning Session Event Protocol family is staged for:

- proposed
- eligibility checked
- opened
- studying
- review pending
- paused
- degraded
- insufficient evidence
- completed
- aborted

The Event Protocol contract carries sparse references and lifecycle facts rather than raw prompts, Library pages, web content, model output, or authority material.

The matching Receipts family preserves durable evidence that the session and transition occurred. A Learning Receipt does **not** prove that the session's conclusion became truth or that any candidate was promoted.

The first Event Protocol pull request completed its repository CI successfully before downstream integration.

## Web relationship

```text
External web
    |
Web Leash / network authority
    |
Web Surface or governed fetch
    |
untrusted external evidence
    |
optional capture / Library admission
    |
White Room / Learning Mode
```

Web access is one possible source path. The developmental architecture must continue to function offline.

## Repository ownership

- `velvet-ai-core`: Learning Session contracts/supervisor, canonical Native Brain reasoning interfaces, cognitive-workspace integration, candidate structures, curiosity/novelty, confidence/freshness interactions.
- `velvet-runtime`: maintenance eligibility, lifecycle hosting, resource/priority/interruption posture, distributed work placement, provider/network availability, health/failure behavior.
- `velvet-persona-continuity`: memory admission effects, persona-scoped learning implications, consolidation proposals, reconstruction effects, identity-drift protections.
- `velours_library`: curated offline knowledge, provenance, retrieval evidence, and source lifecycle. It supplies material but is not the learner.
- `velvet-event-protocol`: shared Learning Session lifecycle transport.
- `velvet-receipts`: durable Learning Session lifecycle evidence.
- `velvet-interface`: status, controls, results, Library viewer, Web Surface. It does not host the learning engine.
- Court/capability owner: hard authority boundary.
- Continuity Spine / Riven: identity and lineage protection.

## Current staged implementation

At the time of this recovery update, the Learning Mode work is intentionally isolated on feature branches pending review/integration:

- AI Core: Learning Session supervisor, transport-safe projection, Native Brain generation ownership, Library-study evidence boundary
- Runtime: fail-closed maintenance eligibility and conservative posture-source projections
- Event Protocol: versioned Learning Session lifecycle family
- Receipts: canonical Learning Session lifecycle receipt family
- Docs: this recovery/ownership map

Implementation branches have been reduced to clean single-commit changesets before dependency-order integration. Runtime was restacked on the newer main containing automatic self-health reporting so the two efforts do not overwrite one another.

## What is genuinely still later work

The remaining architecture is narrower than the original recovery list:

1. integrate and validate the staged cross-repository Learning Mode stack in dependency order
2. define or reuse the final whole-body owners that can positively prove maintenance `QUIET`, background-power permission, and priority `CLEAR` where those are not already supplied by later work
3. add the reviewed read-only Runtime worker/consumer seam for real Library-backed study when execution placement is needed
4. connect candidate outcomes to existing memory admission/promotion paths without creating duplicate stores
5. add explicit Learning Mode evaluation/regression metrics
6. enrich typed/multi-hop concept relationships only if real use cases require more than current deterministic associations
7. add optional local/provider-assisted reflection only after deterministic paths remain proven
8. revisit Web Leash/Web Surface separately from the learning architecture

## Design laws

**Learning Mode = orchestrator/state. White Room = workspace.**

**Autonomous study is not autonomous promotion.**

**Retrieval is evidence, not belief.**

**Simulation remains simulation.**

**Reflection before change.**

**Internet access may expand what Velvet can encounter. It must never be the thing that makes Velvet capable of learning.**
