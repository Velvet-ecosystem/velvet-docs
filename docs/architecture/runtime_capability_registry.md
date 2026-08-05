# Runtime Capability Registry

Velvet reasons from a live registry of truthful capabilities, not a static menu of attractive command names.

Each registration contains:

- capability name
- current and fallback owners
- availability and health state
- authority level
- physical or simulated target
- input requirements and output effects
- refusal reason
- last heartbeat and staleness limit
- receipt type
- allowed and forbidden callers

## Rules

- Unavailable capabilities cannot be invoked.
- Stale registrations are treated as unavailable.
- Degraded capabilities declare their exact limits.
- Simulated capabilities never unlock physical actuators.
- A fallback owner must independently meet the capability contract.
- Native Brain may ask what exists and propose a call. Court decides whether that call may act.
- Registry presence proves availability only. It never grants authority.
- Every refusal uses a stable refusal code and may emit a receipt according to policy.

## Relationship to existing Runtime services

The registry complements capability context, safety-gate registration, executor manifests, and Court authorization. It does not replace them. Capability context proposes what a session may need; the registry reports what currently exists; Court and safety gates decide whether execution is allowed.

## Failure posture

Duplicate owners, contradictory target types, missing heartbeat evidence, invalid authority levels, or ambiguous caller lists fail closed. The registry must remain readable during degraded operation so Class 0 and Class 1 services can inspect what survived.
