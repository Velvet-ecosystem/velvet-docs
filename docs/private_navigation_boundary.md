# Private Navigation Boundary

`velvet-navigation` is currently a private, early-architecture repository for local-first navigation, positioning, offline routing, map data, trip context, and route-intent services.

Its current navigation persona/role is **Nancy**.

## Current scope

Nancy and `velvet-navigation` may own or propose contracts for:

- positioning normalization;
- destination requests;
- route planning;
- navigation progress;
- map/provider abstraction;
- offline routing;
- machine-readable route context;
- human-facing navigation instructions that remain separate from machine-facing route state.

Initial contract names include:

```text
position_fix
navigation_request
route_plan
navigation_progress
navigation_intent
driver_route_context
```

The design is intentionally provider-agnostic so GNSS hardware, map sources, routing engines, geocoders, and UI surfaces can change without redefining the navigation domain.

## Authority boundary

Navigation information is not driving authority.

Nancy and `velvet-navigation` do **not** command:

- steering;
- throttle;
- braking;
- clutch;
- shifting;
- other vehicle actuators.

Any downstream component capable of affecting vehicle motion must independently satisfy its own identity, capability, Court, safety, executor, and physical-control contracts.

A route plan, navigation intent, destination interpretation, or driver route context is information/proposal state only.

## Public/private status

`velvet-navigation` remains private and is therefore intentionally outside the canonical public repository responsibility list in `ecosystem.yaml`.

Public documentation may record that the private navigation domain exists and describe its authority boundary without presenting the repository as a public-supported organ or physically accepted deployment.

Publication of the repository, if desired later, should be an explicit gate rather than an accidental consequence of documenting its existence.

## Current maturity

Current status is early architecture and contract definition.

No statement in this document claims:

- a production routing engine;
- complete offline map coverage;
- accepted GNSS hardware integration;
- live route guidance acceptance;
- vehicle-control authority;
- autonomous-driving capability.

Those require their own implementation and acceptance evidence.
