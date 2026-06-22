# Repository Map

This page defines the primary responsibility of each public Velvet ecosystem repository.

## `velvet-ai-core`

Owns conversational identity, local reasoning integration, role logic, memory use, and core AI coordination.

Does not directly authorize or execute hardware.

## `velvet-runtime`

Owns the local execution nervous system:

- strict intent routes
- capability context
- Court policy integration
- signed capability tokens
- safety gates
- approved executors
- replay protection
- execution receipts
- local observation routes

## `velvet-vehicle-can`

Owns receive-only CAN observation, vehicle fingerprints, local profiles, signal definitions, and conservative decoding.

Transmit-capable work must remain isolated from default observation paths.

## `velvet-event-protocol`

Owns structured event schemas, transport boundaries, source enforcement, and receipt-aware delivery.

Events describe. They do not authorize.

## `velvet-interface`

Owns scene, surface, router, and widget contracts for multi-surface presentation and intent routing.

Scenes and widgets do not actuate hardware directly.

## `velvet-receipts`

Owns receipt formats, integrity, verification, and evidence-preserving records.

A receipt proves recording. It does not create permission.

## `velvet-continuity-spine`

Owns genesis identity, lineage, successor evolution, continuity verification, and tamper-evident identity history.

## `velvet-docs`

Owns canonical cross-repository architecture, doctrine, ecosystem maps, contributor orientation, and deployment guidance spanning multiple components.

Repo-specific implementation details remain with the owning repository.

## `.github`

Owns organization-level profile material, shared issue or pull-request templates, and public contributor-facing defaults.

## Dependency Direction

A useful conceptual dependency direction is:

```text
continuity and identity
  -> Runtime authority
  -> executors and receipts
  -> events and observations
  -> interfaces and surfaces
```

No downstream presentation layer may reach backward around Runtime to gain direct hardware authority.
