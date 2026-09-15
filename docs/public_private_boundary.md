# Public and Private Boundary

Velvet is public where code helps people understand, test, and contribute safely. Velvet is private where disclosure would expose vehicle-control risk, medical assumptions, installation secrets, or unfinished authority paths.

This repository-level public/private boundary is distinct from **owner data privacy**. Public source code does not imply public owner data, and network connectivity does not imply permission to upload owner information. See [Privacy and Connectivity](privacy_and_connectivity.md).

## Public by default

Doctrine, architecture maps, non-authoritative event schemas, receipt formats, read-only observations, synthetic fixtures, mock executors, display-only panels, continuity markers, contributor templates, sanitized deployment guidance, and safe simulation guides may be public when tested and documented.

## Private until qualified

Real actuator control, CAN transmission, emergency pull-over behavior, medical monitoring, installation wiring, credentials, signing keys, capability tokens, owner-only authority, private handmaiden internals, and sensitive live receipts remain private until deliberately reviewed and promoted.

## Documenting private work without publishing it

Public documentation may name a private repository or bounded private domain when doing so is useful to explain architecture, ownership, maturity, or an authority boundary. That documentation does **not** publish the repository, grant public support status, expose its implementation, or promote it into the machine-readable public responsibility map.

A public description of a private capability should stay at the minimum useful level: purpose, non-purpose, authority boundary, maturity, and the explicit publication status. Sensitive implementation details remain private.

Sanitized deployment snapshots may record facts such as service-facing path conventions, physical mount conventions, verified storage behavior, broad directory roles, or outstanding acceptance work. They should not publish credentials, signing material, owner-specific policy, secrets, or local identifiers that are not intentionally part of the public contract.

## Core rules

Observation is not authority. A receipt is evidence, not permission. A surface may display state or request an intent, but it may not directly actuate hardware. Hosted collaborators may draft and review, but they do not own continuity, secrets, Court authority, or hardware control.

For owner information, **connectivity is a capability, not consent**. A reachable cloud, phone, peer, gateway, or radio path does not by itself authorize tracking, telemetry export, or disclosure.

## Promotion checklist

Before a private capability becomes public, it needs a named repository owner, intended scope, threat model, failure mode, offline behavior, tests, documentation, receipt behavior, authority boundary, hardware-risk review, and rollback path.

> Public Velvet proves the architecture. Private Velvet protects unfinished physical authority.
