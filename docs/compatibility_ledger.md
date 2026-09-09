# Velvet Compatibility Ledger

Last reviewed: 2026-09-09; post-merge source set captured 2026-09-09. This records bounded software evidence, not acceptance of the installed physical ecosystem.

The current reproducible source set is [post-merge-software-integration-2026-09-09](../compatibility/post-merge-2026-09-09.json). All eleven accepted repair PRs are merged. The new record pins the actual resulting main commits with empty repair overlays. Each resulting tree matches the accepted repairs; Communications also includes its accepted README correction.

The [post-merge evidence](../compatibility/evidence/post-merge-2026-09-09.json) records merge commits, main CI, candidate source/tree checks and executed counts. [Current software acceptance](current_software_acceptance.md) defines the commands and limits. The [previous manifest](../compatibility/current-2026-09-07.json) and all historical records are preserved unchanged.

**Audio lease-timing qualification remains unresolved.** The existing real-clock heartbeat test once returned CLAIM_LOST instead of PROCESSED. [Original failed job](https://github.com/Velvet-ecosystem/velvet-docs/actions/runs/34294532999/job/102288162655). Passing post-merge suites do not resolve its unproven timing cause; Audio code and fail-closed lease rejection are unchanged.

## Current ledger

“Full baseline CI” means the relevant repository suite runs on Python 3.8. “Baseline contract CI” means focused Founder gates run on 3.8 while the full Runtime suite runs on newer interpreters. Component CI and bounded cross-repository acceptance are separate claims.

| Repository | Responsibility | Python baseline and supported CI | Current evidence scope |
|---|---|---|---|
| velvet-runtime | Boot composition, Court/capability and execution governance | 3.8 baseline contract; full 3.10–3.12 | Repairs [#137](https://github.com/Velvet-ecosystem/velvet-runtime/pull/137), [#141](https://github.com/Velvet-ecosystem/velvet-runtime/pull/141), [#142](https://github.com/Velvet-ecosystem/velvet-runtime/pull/142); real startup loaders, conversation and Ghost acceptance. Observation-only posture retained. |
| velvet-ai-core | Reasoning, interpretation, memory and proposals | Full 3.8 / 3.10 / 3.12 | Repairs [#76](https://github.com/Velvet-ecosystem/velvet-ai-core/pull/76), [#77](https://github.com/Velvet-ecosystem/velvet-ai-core/pull/77); 28 evidence-agreement acceptance cases replayed alongside current real Library integration. |
| velvet-event-protocol | Local event schemas, delivery and enforcement | Full 3.8 / 3.10 / 3.12 | [#18](https://github.com/Velvet-ecosystem/velvet-event-protocol/pull/18) fixes complete discovery; real Ghost lifecycle validation. Events grant no authority. |
| velvet-receipts | Outcome/decision evidence and hash chains | Full 3.8 / 3.10 / 3.12 | Real canonical Ghost receipt construction, persistence and chain verification. Retrieval audit remains distinct from canonical receipts. |
| velvet-continuity-spine | Riven identity and lineage | Full 3.8 / 3.10 / 3.12 | Real disposable development genesis feeds startup-policy acceptance. No production identity or permanent lineage is created. |
| velvet-interface | Presentation and requests | Full baseline 3.8 / 3.10 / 3.12 | [#41](https://github.com/Velvet-ecosystem/velvet-interface/pull/41) includes the previously omitted compatibility case; complete headless suite replayed on 3.8/3.12. Qt/device acceptance remains separate. |
| velvet-language | Bounded human-facing wording | Full 3.8 / 3.10 / 3.11 / 3.12 | Real ConversationGateway and realizer used for typed body facts, Library evidence, unavailable and restored retrieval. No acoustic device claim. |
| velvet-audio-studio | Acoustic/device boundary | Intentional minimum **3.11**; full suite on 3.11 | Separate 240-case software suite; no speech-model, Pi/Octo, kernel or multichannel hardware acceptance in this pass. Never installed in the Founder 3.8 lane. |
| velvet-communications | Peer/network carriage | Full 3.8 / 3.11; additional acceptance replay on 3.12 | Separate 39-case software suite; authenticated local-IP delivery and bounded RPC already implemented. HMAC authentication is not encryption; protected-path claims require a configured confidential underlay. |
| velours_library | Source custody, ingestion and retrieval | Full 3.8 / 3.12 | [#13](https://github.com/Velvet-ecosystem/velours_library/pull/13) adds production vault identity checks; real published-source retrieval over authenticated loopback HTTP, loss/recovery and privacy-minimal audit exercised here. |
| velvet-vehicle-can | Receive-only observation and qualification | Full baseline 3.8; also 3.10 / 3.11 / 3.12 | Separate complete software suite replayed on 3.8/3.12. No CAN interface, transmission or physical-control acceptance. |
| velvet-persona-continuity | Private persona recall/policy contracts | Separately validated in Repair 3 | Merged [#4](https://github.com/Velvet-ecosystem/velvet-persona-continuity/pull/4), actual main and accepted repair head recorded separately. Private source is neither fetched nor implied to be exercised by the public workflow. |
| velvet-docs | Canonical doctrine and compatibility/integration evidence | Not production-runtime-bearing; acceptance 3.8 / 3.10 / 3.11 / 3.12 | Owns the source manifest, replay harness and ledger. This does not assign production orchestration to Docs. |
| business_agent_ecosystem | Adjacent business workflows | Unassessed by this compatibility set | Outside the Founder/conversation acceptance chain. No stronger claim added. |

## Preserved historical checkpoint

The complete previous ledger is preserved byte-for-byte at [compatibility-ledger-2026-06-24.md](../compatibility/history/compatibility-ledger-2026-06-24.md), including its original evidence links and exact frozen sources for `up2-python38-baseline-2026-06-24`.

That historical candidate remains `candidate-pending-hardware-validation`. The new software manifest does not replace its contents or convert it into a hardware-accepted record. Existing deployment receipts and frozen Runtime dependency manifests are unchanged.

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
