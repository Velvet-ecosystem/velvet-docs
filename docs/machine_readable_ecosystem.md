# Machine-Readable Ecosystem Map

Velvet's human-readable architecture maps remain canonical narrative documentation. The root-level [`ecosystem.yaml`](../ecosystem.yaml) is a structured discovery layer for AI systems, code assistants, search/indexing tools, automation, and contributors that need a compact representation of the same repository boundaries.

## Purpose

The machine-readable map exists so a tool entering one Velvet repository does not need to infer the entire ecosystem from scattered README files or repository names.

It provides:

- ecosystem identity and architecture model;
- canonical documentation locations;
- architecture invariants;
- repository ownership and explicit non-ownership boundaries;
- conceptual local and cross-body flow;
- public/private publication posture;
- stable discovery keywords.

## Authority

`ecosystem.yaml` is descriptive metadata. It does not grant permissions, capabilities, trust, execution rights, or physical authority.

When structured metadata and implementation appear to disagree, treat the disagreement as a documentation or integration issue and inspect the owning repository plus the canonical cross-repository doctrine before changing behavior.

The hierarchy for interpretation is:

1. implemented safety and authority contracts in the owning repository;
2. canonical cross-repository doctrine in `velvet-docs`;
3. repository-specific documentation;
4. `ecosystem.yaml` as the compact discovery/index representation.

The structured map should therefore summarize established doctrine rather than silently invent new architecture.

## Machine Consumption

Tools may use the YAML to answer questions such as:

- Which repository owns a responsibility?
- Which repository must not receive a proposed feature?
- Is a component evidence, authority, transport, expression, or presentation?
- What is the expected conceptual dependency direction?
- Which documentation should be read before editing a repository?
- Which terms are useful when indexing or classifying the project?

Tools must not interpret adjacency in the YAML as unrestricted call access. They must not infer physical authority from visibility, events, communications, language, memory, retrieval, receipts, interface requests, or repository membership.

## Update Rule

Update `ecosystem.yaml` whenever any of the following materially changes:

- a public repository is added, renamed, archived, or removed;
- primary repository responsibility changes;
- an architecture invariant changes;
- the canonical documentation location changes;
- a public/private publication boundary changes;
- a responsibility split between Event Protocol, Communications, Language, Audio, Library, Runtime/Court, Receipts, Continuity, Interface, or Vehicle CAN changes.

A change to the structured map should accompany the human documentation change that justifies it. Do not use the YAML as a back door for architecture redesign.

## Per-Repository Discovery

A future optional refinement is a tiny repository-local metadata file that points back to the canonical ecosystem map and declares only local ownership. Such files should reference, not duplicate, ecosystem-wide doctrine.

Example shape:

```yaml
ecosystem: velvet
repository: velvet-runtime
canonical_map: https://github.com/Velvet-ecosystem/velvet-docs/blob/main/ecosystem.yaml
canonical_docs: https://github.com/Velvet-ecosystem/velvet-docs
```

This is intentionally not required yet. The root ecosystem map should settle first so repository-local pointers do not multiply an unstable format.
