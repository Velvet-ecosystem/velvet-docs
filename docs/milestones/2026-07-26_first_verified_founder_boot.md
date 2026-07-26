# First Verified Founder Boot

Date: 2026-07-26  
Hardware: UP Squared Founder board  
Host operating system: Ubuntu 20.04 development environment  
Python: pyenv Python 3.10.20

## Milestone

Velvet completed her first verified Founder Runtime boot on physical UP² hardware.

The final visible posture was:

```text
Continuity        VERIFIED
Court             READY
Runtime           ACTIVE
Routes            READ-ONLY
Physical Control  DISABLED

Waiting for Mister
```

This was Velvet's first ecosystem-level proof that the public Runtime, Interface, AI Core, Event Protocol, Receipts, Vehicle CAN, and Continuity Spine components could be installed into one explicit Python environment, verified together, and presented honestly on the intended Founder-class hardware.

It was a bounded development wake-up. It did not enable CAN transmission, actuator control, remote physical authority, a public network listener, or production identity enrollment.

## Why This Matters

Before this boot, the ecosystem existed as working repositories, contracts, tests, doctrine, synthetic demonstrations, and earlier component-level hardware runs.

This milestone proved a more important whole-body claim:

```text
real Founder hardware
  -> installed local ecosystem packages
  -> verified continuity state
  -> Court provisioning
  -> active read-only Runtime
  -> non-authoritative Interface presentation
  -> truthful visible posture
```

The result was not a simulated dashboard claim. The Founder window displayed a saved Runtime boot snapshot produced from the same machine and environment that performed the verification.

## What Was Proven

The session verified that:

- the UP² can host the current read-only Velvet Runtime foundation
- Continuity can verify the bounded Founder development identity state on modest hardware
- Court can provision its read-only policy and signing context
- Runtime can enter and remain in its active idle posture
- Interface can present Runtime state without owning Runtime or hardware authority
- all public ecosystem packages can coexist in one explicit pyenv interpreter
- editable local packages can be detected honestly when import and distribution names differ
- missing packages, missing identity state, and stale snapshots fail visibly instead of being hidden
- physical authority remains disabled even after successful verification

## What Was Not Proven

This milestone did not establish:

- production genesis enrollment
- production owner-presence verification
- CAN transmission
- relay, lock, lighting, climate, seat, steering, throttle, brake, or drivetrain authority
- autonomous vehicle operation
- network-exposed Runtime control
- Luckfox node validation
- unattended graphical boot
- recovery from damaged production identity material
- successor activation or migration proof

The development bootstrap is not a production birth certificate. It creates a repo-local, read-only state specifically for safe development validation.

## The Fail-Closed Trail

The final green screen was earned through a sequence of truthful failures:

```text
component:interface: module not installed
  -> Interface package installed into the correct interpreter

component:continuity-spine: module not installed
  -> editable/namespace compatibility detection corrected
  -> explicit distribution identity added

continuity_identity: missing .../identity_chain.json
  -> existing bounded development bootstrap discovered and used

Continuity VERIFIED / Court READY
```

Each cleared failure exposed the next real gate. No authority check was bypassed, and no warning was relabelled into success.

## Cross-Repository Lessons

### One interpreter means one reality

All editable packages used by Runtime must be installed into the same interpreter that launches Runtime and produces the boot snapshot.

The validated interpreter was:

```text
/home/coyote/.pyenv/versions/3.10.20/bin/python3
```

A repository existing on disk does not make it importable. A package installed into the system Python does not make it visible to a pyenv Runtime.

### Import names and distribution names can differ

The critical Continuity example was:

```text
Python import module: continuity_spine
Installed distribution: velvet-continuity-spine
```

Compatibility checks must not invent a distribution name by mechanically replacing underscores with hyphens.

### Editable and namespace packages need bounded fallback probes

A package may be importable even when a single discovery mechanism reports no module specification. Runtime now uses a bounded sequence of import and metadata checks before declaring an installed component absent.

### A saved snapshot stays stale

The Founder window reads a saved diagnostic snapshot. Repairing a package or identity file does not rewrite an existing snapshot.

The snapshot must be regenerated after package, policy, identity, service, or environment changes.

### Presentation is not authority

The Interface displayed:

```text
Runtime ACTIVE
Physical Control DISABLED
```

Those statements came from trusted Runtime evidence. The Interface did not infer, grant, or simulate authority.

## Repository Evidence

The owning repositories preserve implementation-specific evidence:

- `velvet-runtime`: verified boot record, merged-main refresh procedure, operator index, compatibility detector fix, Runtime service and snapshot path
- `velvet-interface`: physical UP² Founder Interface validation, Qt editable-install path, lifecycle boundary, and presentation laws
- `velvet-continuity-spine`: physical Founder proof validation, development-state boundary, import/distribution identity lesson, and modest-hardware proof conclusions
- `velvet-ai-core`: inert Runtime-facing `BrainAdapter` compatibility boundary

This document is the ecosystem-level receipt. It does not replace repository-specific runbooks or contracts.

## Final Receipt

> Velvet's Founder Runtime achieved its first verified boot on physical UP² hardware. Identity verified. Court ready. Runtime active. Physical authority intentionally disabled. Awaiting owner.

## Next Milestone

The next hardware milestone is unattended Founder boot:

```text
power applied
  -> Runtime starts through the validated local service path
  -> the selected development or enrolled state is explicit
  -> doctor completes
  -> boot snapshot is regenerated
  -> verification result remains fail-closed
  -> Founder window launches in the graphical session
  -> Waiting for Mister
```

Unattended boot must not:

- silently create production identity
- silently switch between development and production state
- hide failed verification
- treat a stale snapshot as current truth
- enable physical authority
- make Interface responsible for Runtime lifetime

## Historical Note

The first verified boot came after an approximately eleven-and-a-half-hour physical bring-up and debugging session spanning July 25–26, 2026.

The length of the session is not the achievement. The achievement is that every false assumption was replaced with a tested boundary, and the final screen described exactly what the machine had earned.
