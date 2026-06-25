# Memory Retrieval Path

Velvet memory retrieval is a cross-repository read-only path. No single repository owns the whole flow.

## Responsibility map

- `velvet-ai-core` owns immutable memory records, associations, confidence, salience, ranking, and read-only retrieval.
- `velvet-event-protocol` owns public-safe memory reference and recall-result event contracts.
- `velvet-runtime` owns the bounded `memory-recall` route, Court-bound capability, named safety gate, approved executor, and conditional gateway publication.
- `velvet-receipts` owns public-safe receipt context links to memory event identifiers.
- `velvet-continuity-spine` owns bounded memory anchors for identity, lineage, recovery, and drift evidence.
- `velvet-interface` may present recall results later, but must consume Runtime output rather than importing Core retrieval directly.

## Flow

```text
immutable memory records
        |
        v
Core association + confidence + salience + ranking
        |
        v
read-only retrieval results
        |
        v
Event Protocol public-safe reference contract
        |
        v
Runtime memory-recall route
        |
        +--> Receipts memory link
        |
        +--> Continuity memory anchor
        |
        v
Interface presentation
```

## Boundaries

Recall relevance does not establish truth.

Memory references do not grant authority.

Runtime does not own or mutate memory.

Receipts do not copy private memory payloads.

Continuity anchors do not store private memory content.

Interface does not bypass Runtime.

No route is published unless a local recall provider is explicitly provisioned.
