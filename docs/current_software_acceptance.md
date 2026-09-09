# Current software compatibility acceptance

The [2026-09-07 manifest](../compatibility/current-2026-09-07.json) fixes the exact
public source inputs for the current bounded software proof. The
[ledger](compatibility_ledger.md) distinguishes repository-level evidence,
integration evidence, private companions and hardware acceptance.

The [2026-09-09 CI evidence](../compatibility/evidence/software-integration-2026-09-09.json) records the implementation commit, actual PR test checkout, run URLs, Python patch versions and executed suite counts. All eight pinned/candidate jobs passed. The test checkout is GitHub's synthetic PR merge commit; the PR remains unmerged.

## What is exercised

The primary command discovers 50 tests: eight new current integration checks,
ten manifest/replay guardrails, four unchanged distributed Ghost tests and the
28 accepted Repair 4 Core-to-Language evidence checks. Python 3.8, 3.10, 3.11 and
3.12 run the same integration command.

| Required path | Real components and assertions |
|---|---|
| Startup policy loading | Runtime development bootstrap, real Continuity genesis and real body/session/capability loaders; guest, non-present, observe.telemetry only, authorization still required. Hardware input and key bytes are disposable synthetic fixtures. |
| Ordinary typed conversation | Runtime body bridge/file reader → Core → Language; current synthetic cabin temperature, source reference, no authority or acoustic output. |
| Library retrieval | Real Library publication/catalog, authenticated HTTP handler/client on loopback, Runtime normalizer, Core and Language; source IDs/hashes preserved and catalog unchanged by retrieval. |
| Library unavailable/lost | Library directory moved within a temporary fixture; actual retrieval fails, Core is unavailable, old source references are absent and body conversation continues. No replacement Library root appears. |
| Restored retrieval | Same Library object, server, client and conversation resume after the original directory returns, with the original source references. |
| Service degradation | Revoked peer secret produces real HTTP 401 and no authentication bypass; absent body snapshot preserves LocalConversationError to the caller while Library questions continue; restoring the file recovers body facts. |
| Read-only receipt/evidence trail | Real Event Protocol Ghost lifecycle, canonical Receipts construction/logger and five-record chain verification; verification does not mutate the ledger. Library audit hashes queries and remains separate, non-canonical retrieval evidence. |

An insufficient-evidence case also forbids invented references. The existing
28 Repair 4 acceptance cases continue to cover corroboration, negation,
conditions, subjects, measurements and unresolved evidence. No production
conversation, Library, receipt or authority semantics change in this repair.

The separate component suites exercise Interface, Vehicle CAN and
Communications on 3.8/3.12, and Audio Studio plus Communications on 3.11. Audio's
intentional >=3.11 requirement is preserved; acoustic models and devices are
outside this job. These suites do not imply a new cross-repository audio or
network production integration.

## Exact inputs while repairs are unmerged

Each public repository entry records an exact observed main `commit`, ordered
`repairs` with exact `base_commit`/`commit` pairs, and `expected_tree`. Base/head
pairs are necessary because an accepted PR can contain multiple commits and
can have branched before later main changes. Replaying only its final commit,
or diffing its head against a newer unrelated main, would lose or undo work.

The preparer creates new detached checkouts, applies those explicit deltas to
their indexes and checks their resulting Git trees. It never authors a
production commit, merges a branch/PR, modifies an existing checkout, pushes or
changes protection. Already-present complete deltas are recorded explicitly.
A conflict or pinned-tree mismatch fails preparation and retains input
evidence. There is no automatic conflict resolution or manifest promotion.

The source commits and resulting tree together identify the tested composition.
The checkout's base HEAD alone must not be described as containing all repairs.
Historical records remain unchanged; the previous ledger is preserved in full.

## Running the pinned proof

From the Docs repository, with the selected Python interpreter:

```sh
python acceptance/prepare_sources.py --destination "$PWD/.acceptance-deps"
python -m pip install 'pytest==8.3.5' 'PyYAML>=6,<7' \
  -e .acceptance-deps/velvet-ai-core -e .acceptance-deps/velvet-language \
  -e .acceptance-deps/velours_library -e .acceptance-deps/velvet-receipts \
  -e .acceptance-deps/velvet-event-protocol -e .acceptance-deps/velvet-continuity-spine
python -m pytest acceptance tests .acceptance-deps/velvet-ai-core/acceptance -q -ra --junitxml=integration.xml
```

The destination must not already exist. For offline use, `--mirror-root` may
point to local repositories already containing every recorded commit; it creates
separate detached worktrees. No existing index or worktree is reset. Set
`VELVET_ACCEPTANCE_DEPS` if the prepared root is outside the default location.

## Dependency-change coverage

`Distributed Ghost Integration` now runs on acceptance/manifest changes,
relevant main pushes, manual dispatch and a six-hour schedule at minute 23.
Every run separates two modes:

- **pinned** replays the reviewed manifest and requires its exact tree hashes;
- **candidate** resolves each public dependency's main once, records its full
  SHA, reapplies the explicitly recorded repairs and runs the same proof.

This polls dependency changes without cross-repository write tokens, secret
dispatch credentials or new hooks in every organ. It is not an immediate
required check on every upstream PR. Manual dispatch can test one upstream
commit through `dependency_override=known-public-repository=full-commit-SHA`;
the preparer also accepts that exact override locally. Other candidate inputs
are recorded, not treated as moving reproducible pins.

Scheduled events require this workflow to be on the default branch and can be
delayed or dropped by GitHub. Until Mister merges the PR, the scheduled trigger
is proposed configuration, not an active monitor. PR runs exercise both code
paths now. [GitHub workflow-event documentation](https://docs.github.com/actions/using-workflows/events-that-trigger-workflows#schedule).

Each job preserves `tested-inputs.json`, the exact Docs harness commit,
interpreter/package versions, preparation log and JUnit files. Failed
preparation is retained too. A changed dependency may fail because a contract
regressed or an accepted overlay no longer applies; investigate before adding
a **new** reviewed manifest. Candidate results never rewrite the current or
historical record. After repairs merge, a future record can pin the resulting
main commits directly and remove redundant overlays in that new record.

## Limits

This is software-only acceptance using temporary state, synthetic sources,
development identity fixtures and loopback HTTP. No production UUID, keys,
identity history, private data, physical vault, LAN hardware, UP², Pi/Octo or
vehicle is accessed. Library disappearance here is a directory/service test;
Repair 5's simulated kernel/device identity tests remain the storage-identity
evidence. This pass does not assert hardware hotplug acceptance.

Missing body snapshots retain the existing error contract; no new UI fallback
is introduced. Library retrieval audit is not converted into canonical
conversation receipts. The Ghost's canonical workload receipts retain their
existing meanings. The private Persona repository is recorded as separately
validated rather than imported into a public job. No physical execution or
new authority follows from any passing result.
