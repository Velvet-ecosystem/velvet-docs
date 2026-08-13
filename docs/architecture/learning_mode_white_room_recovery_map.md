# Learning Mode, White Room, and Dream Layer Recovery Map

## Purpose

This document preserves the historical self-learning architecture and assigns modern ownership before implementation. It is a recovery map, not a new runtime authority model.

## Core distinctions

- **Learning Mode** is the governed maintenance state that orchestrates deliberate study.
- **White Room** is the bounded internal workspace where evidence is compared and candidate understanding is formed.
- **Dream Layer / Dream State** is the slower consolidation phase that revisits accumulated material.
- **self-LM** is the developmental goal: Velvet becomes more capable offline through experience, memory, associations, reflection, and optional local models.
- **Web Leash** governs outside-network access. It is an input boundary, not the learning system.
- **Web Surface** is user-facing rendering, not a cognitive owner.

## Historical placement

Learning Mode belongs in Velvet's maintenance/back-room architecture, historically described as the Legs, rather than in the front-facing interface. The front exposes controls, state, results, Library material, and optional web content. The orchestrator remains internal maintenance machinery.

## Ownership map

| Historical concept | Modern destination | Status |
|---|---|---|
| Learning Mode | `velvet-ai-core` contracts + `velvet-runtime` lifecycle | Missing as complete orchestrator |
| White Room | Native Brain reflection workspace | Concept survives; implementation incomplete |
| Dream Layer | Native Brain + Persona Continuity consolidation | Doctrine present; engine incomplete |
| self-LM | Native Brain + memory + associations + optional local models | Evolved |
| Web Leash / Collar | Runtime/Gateway network capability policy | Evolve separately from learning |
| Web Surface | `velvet-interface` | New user-facing capability |
| Curiosity Engine | Curiosity Budget + Learning Mode scheduler | Partially present |
| Thought Gate | Native Brain attention/proposal gate | Missing or unverified |
| Knowledge Intake | Memory intake + Library admission | Mostly superseded |
| Observation Memory | Evidence plane + sensor/event records | Architecture present; adapter unverified |
| Knowledge Cards | Structured memories / knowledge projections | Evolve |
| Knowledge Compressor | Dream/consolidation proposals | Missing or unverified |
| Concept Graph / Memory Veins | Core association plane/index | Partially implemented |
| Confidence System | Core confidence + freshness + evidence history | Largely implemented |
| Conflict Resolver | Reflection + conflict workflow | Partial |
| Learning Journal | Receipts + reflection records | Evolve |
| self-LM metrics | Learning evaluation/regression layer | Missing |
| Speaker Reliability | Provenance/evidence-quality policy | Unverified; bounded and explainable only |
| Velour / Librarian | Library + memory indexing + provenance | Modern role established |
| Court | Authority boundary | Modern owner established |
| Riven | Continuity and lineage protection | Modern owner established |

## Operating states

### NORMAL

Observe, recall, record evidence, and act only through existing authority. Unresolved learning candidates may be queued for later work.

### LEARNING

A bounded maintenance session:

1. Select an unresolved question or explicit study task.
2. Allocate bounded resources.
3. Gather eligible evidence from memory, sensors, Library, conversations, or separately authorized web material.
4. Open a White Room workspace.
5. Run Reflection over supporting and conflicting evidence.
6. Form hypotheses, questions, confidence, freshness, and limitations.
7. Produce candidate learning.
8. Submit candidates through existing admission policy.
9. Write receipts and close the workspace cleanly.

Autonomous study is not autonomous promotion. A session may finish with uncertainty, a revalidation request, or an unpromoted candidate.

### DREAM

A lower-priority consolidation state that may strengthen or weaken associations, identify stale knowledge, find contradictions, summarize repeated episodes into proposals, build backlinks, reduce retrieval noise, and prepare revalidation tasks.

Dream work produces proposals and receipts rather than silently rewriting durable evidence.

## White Room boundary

Eligible inputs include immutable evidence, receipts, admitted memories, sensor observations, Library material, documentation, previously captured web material, separately authorized live web material, and specialist-organ reports.

Outputs are proposals such as candidate explanations, association proposals, contradiction records, confidence revisions, unanswered questions, revalidation requests, knowledge projections, and negative-learning candidates.

White Room output does not automatically become trusted knowledge, doctrine, identity, capability, or physical authority.

## Web relationship

```text
External web
    |
Web Leash / network authority
    |
Web Surface or governed fetch
    |
untrusted evidence
    |
optional capture / Library admission
    |
White Room / Learning Mode
```

Web access is one possible source path. The developmental architecture must continue to function offline.

## Repository ownership

- `velvet-ai-core`: Learning Mode and Reflection contracts, curiosity/novelty interfaces, candidate-understanding structures, confidence/freshness interactions, learning evaluation contracts.
- `velvet-runtime`: session start/stop/suspend/resume, resource budgets, priority and interruption handling, provider availability, process isolation, health and failure behavior.
- `velvet-persona-continuity`: memory admission effects, persona-scoped learning implications, consolidation proposals, reconstruction effects, identity-drift protections.
- `velours_library`: curated offline knowledge and provenance. It supplies material but is not the learner.
- `velvet-interface`: status, controls, results, Library viewer, Web Surface. It does not host the learning engine.
- `velvet-receipts`: durable records of important learning transitions and outcomes.
- Court/capability owner: hard authority boundary.
- Continuity Spine / Riven: identity and lineage protection.

## Already available

Modern Velvet already provides much of the required foundation: append-only evidence and memory records, provenance-aware admission, confidence and freshness concepts, deterministic associations and backlinks, bounded recall packets, reversible salience, receipts, Runtime and Court boundaries, Continuity Spine, Learning and Judgment Doctrine, Reflection/Dream-State doctrine, Curiosity Budget doctrine, and Library architecture.

These should be extended rather than duplicated.

## Missing centerpiece

The primary missing component is the **Learning Mode Orchestrator**.

It is not another memory store, reasoning model, browser, or Library. It is the maintenance-layer conductor that coordinates existing organs into a bounded learning session.

## Implementation order

1. Preserve this ownership map and historical terminology.
2. Inspect surviving White Room, Learning Mode, self-LM, Dream Layer, curiosity, thought-gate, and knowledge-compressor artifacts before replacing them.
3. Define a versioned Learning Session contract in Core.
4. Define Runtime lifecycle, resource, and interruption semantics.
5. Define White Room input/output boundaries.
6. Connect candidate outputs to existing admission and receipt paths.
7. Add deterministic synthetic-evidence tests.
8. Add Library-backed offline learning fixtures.
9. Add optional provider-assisted reflection only after the deterministic path is proven.
10. Revisit Web Leash and Web Surface as separate source/interface projects once Learning Mode ownership is stable.

## Design rule

Internet access may expand what Velvet can encounter. It must never be the thing that makes Velvet capable of learning.
