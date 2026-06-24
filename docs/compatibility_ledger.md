# Velvet Compatibility Ledger

This ledger records the difference between claimed compatibility and mechanically verified compatibility across the Velvet ecosystem.

It is not a marketing matrix. A repository enters a stronger support category only when its code, package boundary, and tests support that claim.

Last reviewed: 2026-06-24

## Evidence levels

### Full baseline CI

The repository installs and runs its relevant test suite on Python 3.8 in CI.

### Baseline contract CI

Python 3.8 validates the bounded compatibility contract and syntax-sensitive tooling, while the repository's full suite remains on newer preferred interpreters.

### Syntax guarded

Declared Python 3.8-facing files are parsed against Python 3.8 grammar, but the full package is not yet exercised on Python 3.8 CI.

### Unassessed

No ecosystem-level Python 3.8 compatibility claim has been verified yet.

## Current ledger

| Repository | Role | Python 3.8 status | Preferred lane | Evidence | Notes |
|---|---|---:|---:|---|---|
| `velvet-runtime` | boot, identity, Court, gates, executors, local gateway | Baseline contract CI | 3.10–3.12 full suite | Runtime PR #42, merge `ebdf4b357b0bb8463664a8787704a779f57adeee` | Python 3.8 validates the baseline dependency contract and compatibility tools. Physical UP² validation is still pending. |
| `velvet-interface` | bounded visible surfaces and boot status | Syntax guarded | current development lane | commit `94bd9ad2439fb65cf4f137891953d3259fb1566a` | Boot window syntax was restored to Python 3.8-compatible typing. Full Python 3.8 install-and-test CI is not yet recorded. |
| `velvet-event-protocol` | internal event transport and receipt-aware enforcement | Full baseline CI | 3.10 and 3.12 also tested | Event Protocol PR #3, merge `735dfbfe047987f4d94a31678e03ee61c9cfccf1` | Real installable package. Runtime-compatible `EventBus` and `EventEnforcer`. ACTUATION remains fail-closed. |
| `velvet-continuity-spine` | identity, lineage, proof records, drift and continuity | Full baseline CI | 3.10 and 3.12 also tested | Continuity PR #3, merge `ed01c89ad74004047ad235a7f73ff9de45b044d9` | Package-wide Python 3.8 syntax guard remains in the test suite. Hash, HMAC, lineage, and authority semantics remain unchanged. |
| `velvet-receipts` | append-only accountability and hash chains | Full baseline CI | 3.10 and 3.12 also tested | Receipts PR #2, merge `bff0e378d183a2e7828a140f1c4e8b52431d28c3` | Installable `velvet_receipts` package added while preserving root-level imports and receipt-chain behavior. |
| `velvet-vehicle-can` | receive-only CAN observation, learning and qualification | Full baseline CI | 3.10 and 3.12 also tested | Vehicle CAN PR #5, merge `d7b667e335437c35ed5e81dea977ec4c2bd2bdab` | Installable package. Hardware observation dependency remains optional. No transmit or actuation path was added. |
| `velvet-ai-core` | language, reasoning, personality and core proposals | Full baseline CI | 3.10 and 3.12 also tested | Core PR #9, merge `12012ba4f16a03383e3e5efb9f6ea31904a63a4b` | Package installs and imports on Python 3.8. A package-wide syntax guard is enforced. No model backend, cloud service, hardware access, or authority is required. |
| `velvet-docs` | canonical doctrine and ecosystem contracts | Not runtime-bearing | n/a | documentation review | Owns compatibility doctrine and this ledger, but does not define a Python runtime floor. |
| `business_agent_ecosystem` | autonomous business-agent workflows | Unassessed | unknown | pending audit | Not part of the UP² first-wake dependency chain. |

## Core capability separation

`velvet-ai-core` keeps its Python 3.8 baseline independent from heavy reasoning backends.

Baseline Core includes model-independent structures for proposals, identity concepts, personality configuration, memory abstractions, shared interfaces, descriptive schemas, and Runtime request formation.

Language models, speech engines, embeddings, vision models, accelerators, and hosted collaborators remain optional capability providers.

A backend may require newer Python or stronger hardware, but that requirement belongs to the backend adapter. It must not raise the floor of the entire Core package.

Missing optional capability should report locally:

```text
Core baseline: available
Local language model: unavailable
Voice reasoning: unavailable
Vision reasoning: unavailable
Runtime request formation: available
Physical authority: none
```

Optional reasoning backends may propose, explain, summarize, classify, or form candidate intents. They do not receive Court signing keys, executor registries, safety bypasses, or physical hardware authority.

## UP² baseline candidate

The current constrained-hardware software checkpoint is:

```text
up2-python38-baseline-2026-06-24
```

Frozen sources:

```text
velvet-runtime
  ebdf4b357b0bb8463664a8787704a779f57adeee

velvet-interface
  94bd9ad2439fb65cf4f137891953d3259fb1566a

velvet-event-protocol
  735dfbfe047987f4d94a31678e03ee61c9cfccf1

velvet-continuity-spine
  ed01c89ad74004047ad235a7f73ff9de45b044d9
```

The candidate remains:

```text
candidate-pending-hardware-validation
```

CI proves the software contracts. Only the physical UP² can prove the hardware wake-up.

## Compatibility laws

- A declared Python floor must match parseable and installable reality.
- Full support means tests, not intention.
- Required dependencies and optional capabilities must be separated.
- Missing optional capability must degrade locally.
- A newer interpreter may unlock capability, but must not silently broaden authority.
- Hardware support claims must name the evidence level.
- A historical hardware candidate must never be rewritten after freezing.

## Update rule

Update this ledger whenever:

- a repository changes its declared Python floor
- a package boundary is added or renamed
- a new baseline CI lane is introduced
- a hardware candidate is frozen or superseded
- an optional capability becomes required
- a repository is removed from or added to a first-wake dependency chain

Every update should point to the PR, merge commit, CI evidence, or hardware evidence that supports the stronger claim.
