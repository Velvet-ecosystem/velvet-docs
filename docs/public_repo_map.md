# Public Repository Map

This page maps the current public Velvet ecosystem and the boundaries between its repositories.

The public surface now extends beyond the original Ghost System v0 chain. Ghost remains a useful synthetic proof path, but the public ecosystem also includes Language, Audio Studio, Communications, and Velour's Library.

## Current Public Body Map

```text
                               Velvet
                                  │
            ┌─────────────────────┼─────────────────────┐
            │                     │                     │
        AI Core             Runtime + Court          Interface
   reasoning / memory       authority / policy      scenes / intent
            │                     │                     │
            └────────────── Event Protocol ─────────────┘
                    local governed nervous system
                ┌──────────────┼──────────────┐
                │              │              │
          Vehicle CAN       Receipts       Language
          observation       evidence       expression
                               │              │
                         Continuity Spine   Audio Studio
                           Riven / lineage   local speech I/O

approved cross-body payload
  -> Communications
  -> selected carrier / relay / degraded route
  -> separately governed Velvet peer

provenance-aware knowledge
  -> Velour's Library
  -> retrieval evidence
  -> reasoning without automatic belief
```

## Repository Responsibilities

| Repository | Public responsibility | Hard boundary |
|---|---|---|
| `velvet-ai-core` | reasoning, memory primitives, belief/context handling, reflection/learning boundaries, structured proposals | no Court or physical execution authority |
| `velvet-runtime` | identity/body context, Court, policy, emergency-first scheduling, incident Court binding, resources, safety, approved executor boundary, execution evidence | Court authorization is not measured execution |
| `velvet-event-protocol` | versioned local event schemas and hardened delivery inside one governed body | local events communicate; they do not authorize or own cross-body carriage |
| `velvet-communications` | V2V/cross-body envelopes, carrier selection/fallback, relay, degraded/off-grid delivery, Beacon of Hope, privacy/disclosure contracts | carrier/reachability does not create identity, trust, consent, or authority |
| `velvet-language` | meaning-before-speech expression, bounded conversation, deterministic critical/emergency wording | expression does not create truth or authority |
| `velvet-audio-studio` | local capture, Vosk, Piper, audio leases/routing, priority/preemption, output evidence | audio devices do not create command authority; final Octo hardware acceptance remains pending |
| `velours_library` | guarded knowledge ingestion, provenance, lifecycle, retrieval evidence, portable packs/quarantine/adoption | retrieval is not belief or authority |
| `velvet-vehicle-can` | passive CAN observation, decoding, fingerprints, vehicle profiles, qualification evidence, Ghost replay | no public CAN transmit/actuation authority |
| `velvet-interface` | scenes, surfaces, widgets, presentation, intent routing | no direct hardware control |
| `velvet-receipts` | append-only evidence, integrity, verification, truth-preserving outcome records | receipt is evidence, not permission |
| `velvet-continuity-spine` | Riven identity lineage, successor evolution, drift, recovery, verified history | memory alone does not prove identity |
| `velvet-docs` | canonical cross-repo doctrine, maps, newcomer and deployment guidance | documentation does not replace implementation evidence |
| `.github` | organization profile and contributor-facing defaults | no Runtime behavior |
| `business_agent_ecosystem` | adjacent public application/reference ecosystem | not a replacement for shared body/authority organs |

## Local Events vs Communications

This distinction is canonical:

```text
within one governed body
  -> velvet-event-protocol

between nodes / bodies / deployments
  -> velvet-communications
  -> carrier
  -> receiving body's governed ingress
```

A valid Communications envelope proves only that a bounded payload passed the communications contract. The receiving body must still perform its own identity, relationship, Runtime, Court, capability, safety, and receipt checks.

> **The message belongs to Velvet. The carrier is replaceable.**

> **Connectivity is a capability, not consent.**

## Emergency Continuity in the Public Runtime

The public Runtime now proves an authority-preserving emergency decision chain:

```text
verified active emergency / accident / trusted manual emergency start
  -> life-safety rank 0
  -> responder request as authority-free evidence
  -> incident-action policy
  -> canonical capability + logical target
  -> incident-scoped emergency Court identity
  -> strict Court Intent
  -> Court authorization
  -> future safety / executor / hardware binding
  -> future measured physical result
```

Important public boundaries:

- emergency priority means **consider first**, not **approve automatically**;
- the incident does not reuse the owner's active session;
- responder identity/transport remains provenance, not Court authority;
- bounded visibility and rescue-access policies are separated;
- motion/powertrain requests do not travel through responder conversation;
- no public emergency executor currently opens a real vehicle door or switches real vehicle lights;
- public physical authority remains none.

## Privacy and Off-Grid Communications

`velvet-communications` may eventually carry approved messages over local IP, secure overlays, LoRa, Meshtastic, private LoRaWAN/ChirpStack, cellular, serial, or another approved carrier.

More carriers do not create more permission to report owner data.

Beacon of Hope is a bounded emergency fallback for situations where protected ordinary paths are unavailable. A message being sent, heard, or relayed is not the same as an upstream emergency destination acknowledging it.

The future Owner Emergency Bridge may use a paired owner phone as a carrier. The phone does not become Velvet's authority and a connected call does not bypass the rest of the system.

## Language, Audio, and Knowledge

Public Language and Audio now form a real local speech architecture:

```text
verified meaning
  -> velvet-language
  -> truthful expression / speech request
  -> velvet-audio-studio
  -> local synthesis + routing
  -> output evidence
  -> Runtime / Receipts
```

The software audio path is implemented and testable, while final Raspberry Pi + Audio Injector Octo signal-path acceptance remains explicitly unproven.

Velour's Library provides a separate knowledge path:

```text
source
  -> guarded acquisition / staging
  -> provenance + lifecycle
  -> retrieval evidence
  -> Core reasoning
```

Library retrieval never silently becomes belief, identity proof, or authority.

## Ghost System v0

Ghost System v0 remains the synthetic, read-only public loop that proves Velvet can observe, validate, interpret, route, receipt, display, and preserve continuity without opening a physical vehicle bus.

```text
velvet-vehicle-can
  -> velvet-event-protocol
  -> velvet-ai-core
  -> velvet-runtime
  -> velvet-receipts
  -> velvet-interface
  -> velvet-continuity-spine
```

| Repository | Ghost System v0 responsibility | Hard boundary |
|---|---|---|
| `velvet-vehicle-can` | produce synthetic vehicle-shaped observations | no transmit or actuation |
| `velvet-event-protocol` | validate local Ghost observation events | events describe, not authorize |
| `velvet-ai-core` | summarize and create description-only proposals | no executor selection or capability grant |
| `velvet-runtime` | route through Court, safety gates, and a non-physical executor | no privileged physical vehicle path |
| `velvet-receipts` | record evidence that the path stayed synthetic and non-actuating | receipt is evidence, not permission |
| `velvet-interface` | render sanitized Ghost state | no command surface or actuator bridge |
| `velvet-continuity-spine` | record a public-safe Ghost Run lineage marker | no private memory or hardware authority |

## Public Scope

In scope now:

- synthetic fixtures and read-only telemetry;
- bounded Runtime/Court foundations;
- incident-scoped logical emergency authorization;
- deterministic/local language and speech contracts;
- transport-neutral V2V and emergency communications contracts;
- privacy/disclosure doctrine;
- provenance-aware local knowledge/retrieval contracts;
- receipts, continuity, and public interface foundations.

Still out of public physical scope:

- CAN injection;
- production actuator control;
- real responder door/light executor binding;
- steering/throttle/brake/shifter execution;
- hidden owner privilege paths;
- private medical deployment logic;
- deployment credentials, secrets, owner data, private peer maps, or installation wiring.

## Maintenance Rule

The organization profile (`.github/profile/README.md`) and the canonical `velvet-docs` front door/maps should be updated in the same documentation pass whenever:

- a repository changes public/private status;
- repository ownership boundaries materially change;
- a new canonical public organ appears;
- the authority path gains or removes a major governed stage;
- privacy/communications doctrine changes in a way newcomers should see immediately.

The front door should never lag far enough behind implementation that a newcomer learns an architecture Velvet no longer uses.
