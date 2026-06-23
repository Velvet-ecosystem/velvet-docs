# Hardware Access and Graceful Degradation

Velvet must not become a new hardware gatekeeper while claiming to resist old ones.

The ecosystem should run on the smallest practical user-owned hardware, preserve its core safety and continuity laws there, and expand when stronger hardware is available.

> Stronger hardware adds capability. It does not add legitimacy.

## Core rule

A device is a valid Velvet body when it can preserve the bounded core:

- identity and continuity
- Court and policy checks
- receipts and evidence
- local CLI or local API access
- bounded observation
- explicit capability reporting
- fail-closed behavior

A missing GPU, newer interpreter, camera, accelerator, optional package, or abundant memory must not invalidate the whole system when the bounded core can still operate safely.

## No hardware caste system

Velvet must not split into a lesser identity for older boards and a real identity for newer machines.

A modest board may provide:

```text
Runtime core: available
Continuity: available
Court: available
Receipts: available
Minimal Interface: available
Local language model: limited
Vision: unavailable
Actuation: disabled
```

A stronger machine may add richer language, vision, scenes, concurrent handmaidens, and faster inference. Both remain Velvet.

## Capability tiers

Repositories should declare capability tiers rather than one ecosystem-wide hardware floor.

A typical contract may define:

```text
baseline:
  safe bootstrap
  identity and continuity
  Court checks
  receipts
  read-only Runtime
  minimal Interface

preferred:
  richer local models
  advanced voice
  vision
  world-model processing
  additional concurrent services
```

The baseline must remain useful, observable, and safe. The preferred tier must not silently broaden authority.

## Graceful degradation

Degradation must be explicit, local, and receiptable.

Good behavior:

```text
baseline Runtime ready: true
preferred capability tier: unavailable
vision: unavailable
optional CAN observation: unavailable
```

Bad behavior:

```text
system unavailable because optional accelerator is missing
```

Missing optional capability must disable that capability only. It must not silently substitute cloud dependence, remote authority, weaker policy, or unsafe hardware access.

## Language and runtime compatibility

Interpreter requirements belong to the narrowest component that truly needs them.

A repository that claims Python 3.8 support must parse and run its baseline path on Python 3.8. Newer syntax or libraries may be used only when the package raises its declared floor or isolates them behind a newer optional capability.

The current Runtime model uses:

```text
Python 3.8–3.12: baseline capability lane
Python 3.10–3.12: preferred capability lane
```

This is a compatibility policy, not a promise that every future optional module will support every interpreter. Each exception must be explicit and local.

## Repository obligations

Every implementation repository should:

1. Declare its actual minimum runtime and hardware assumptions.
2. Separate required dependencies from optional capabilities.
3. Report capability loss without pretending a feature exists.
4. Keep safety, identity, Court, and receipts in the lowest practical tier.
5. Avoid syntax that contradicts the declared interpreter floor.
6. Test the baseline contract in CI when practical.
7. Never grant authority merely because stronger hardware is present.

## Security remains unchanged

Graceful degradation never means graceful weakening.

Older hardware does not receive broader shortcuts. Newer hardware does not receive automatic authority.

The execution law remains:

```text
input
  -> identity and context
  -> strict intent
  -> Court and policy
  -> safety
  -> approved executor
  -> receipt
```

No valid receipt means no surviving mutation or actuation.

## Original promise

Velvet began as a retrofit rebellion, not a demand that the user buy a new machine.

She should be able to inhabit an old car, a modest board, a cyberdeck, a workshop terminal, a home surface, or a powerful compute node without losing her identity or forcing the owner into a vendor-defined body.
