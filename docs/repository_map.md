# Repository Map

This page defines the primary responsibility of each public Velvet ecosystem repository.

## `velvet-ai-core`

Owns Unified-Organ reasoning, belief/context handling, canonical memory primitives, reflection, learning/plasticity boundaries, and structured proposals.

Does not directly authorize or execute hardware.

## `velvet-runtime`

Owns the local authority and execution nervous system:

- verified body, profile, session, and surface context;
- strict intent routes;
- capability context and canonical Court authority;
- Court policy resolution;
- emergency-first life-safety scheduling;
- incident-action policy, logical capability/target resolution, and incident-scoped Court binding;
- bounded capability tokens;
- resource coordination and safety gates;
- approved executors;
- replay protection;
- measured execution outcomes and execution receipts;
- local observation routes.

Court authorization is not execution. Executor/safety/hardware binding remains a separate boundary.

## `velvet-event-protocol`

Owns structured event schemas, source enforcement, and hardened **local** event delivery inside one governed body.

Events describe. They do not authorize.

Event Protocol does **not** own V2V federation, cross-body carrier selection, relays, store-and-forward between bodies, or off-grid routing. Those belong to Communications.

## `velvet-communications`

Owns transport-neutral cross-node and cross-body carriage:

- V2V envelopes and peer addressing;
- carrier capability descriptions and selection;
- bounded acknowledgements/retries, TTL, hop limits, replay suppression, and store-and-forward;
- degraded/off-grid routing;
- adapters for local IP, secure overlays, LoRa, Meshtastic, private LoRaWAN/ChirpStack, serial, cellular, and future carriers;
- Beacon of Hope emergency-fallback contracts;
- communication-delivery truth and degradation evidence;
- communications privacy/disclosure boundaries.

Authenticated local-IP TCP delivery and bounded request/reply RPC are already
implemented. They provide authentication, integrity and replay handling, not
payload encryption. A protected-path advertisement requires an explicitly
configured confidential underlay. Radio adapter contracts and physical
LAN/LoRa/Meshtastic acceptance remain distinct from that software implementation.

Core laws:

**The message belongs to Velvet. The carrier is replaceable.**

**Connectivity is a capability, not consent.**

A carrier connects. It does not create identity, trust, authority, or blanket disclosure permission.

## `velvet-language`

Owns the language/expression boundary:

- bounded conversation acts and turn context;
- reference resolution and response strategy;
- meaning-before-speech realization;
- truthful uncertainty/fallback language;
- deterministic or nearly deterministic critical/emergency expression;
- governed language-experience evidence;
- optional provider-neutral generative assistance.

Language receives verified meaning and turns it into expression. It does not own canonical truth, memory, Runtime/Court authority, audio devices, or physical action.

## `velvet-audio-studio`

Owns the shared local acoustic device boundary:

- multichannel microphone capture;
- bounded VAD/utterance capture;
- local Vosk transcription and wake/privacy gating;
- local Piper synthesis;
- audio channel leases and routing;
- priority/preemption behavior;
- persistent playback ownership;
- output evidence and Runtime handoff;
- hardware adapters such as the Audio Injector Octo reference path.

Software contracts are implemented. Final Raspberry Pi + Audio Injector Octo physical acceptance remains separate evidence work.

## `velours_library`

Owns Velour's canonical local-first, provenance-aware knowledge archive:

- guarded staging/ingestion;
- source evidence and provenance;
- source lifecycle and supersession;
- retrieval evidence and locations;
- approved remote acquisition boundaries;
- deterministic portable knowledge packs;
- quarantine, adoption, and pack lifecycle.

`velours_library` owns the knowledge/provenance contract. It does not own every deployment helper or the human presentation surface. Current private Cyberdeck tools may prepare local files, and `velvet-interface` may render catalog entries, without creating a second canonical Library.

Retrieval is not belief. Library evidence grants no Runtime/Court authority.

See [Library, Vault, and Reader Path](library_vault_and_reader_path.md).

## `velvet-vehicle-can`

Owns receive-only CAN observation, vehicle fingerprints, local profiles, signal definitions, qualification evidence, Ghost replay, and conservative decoding.

Transmit-capable work must remain isolated from default observation paths. Current public CAN transmission authority is none.

## `velvet-interface`

Owns scene, surface, router, widget, and trusted full-screen workspace presentation contracts.

Current public Interface capabilities include:

- image-first rooms and contextual touch surfaces;
- the registered Character Foundry workspace, which remains a thin fail-closed client over its canonical backend;
- the read-only Scroll-backed Library Reader and canonical-catalog preview provider;
- a reusable Library Reader registration helper for Founder integration.

The final main Founder-launcher call for the Library Reader and the permanent Archive-room hotspot remain follow-on deployment/UI placement work.

Scenes, widgets, readers, and workspaces do not actuate hardware directly. Presentation does not create knowledge trust, capability, Court authority, merge/deploy permission, or physical control.

## `velvet-receipts`

Owns receipt formats, integrity, verification, append-only evidence, and truth-preserving outcome records.

A receipt is evidence, not permission.

## `velvet-continuity-spine`

Owns Riven: genesis identity, lineage, successor evolution, continuity verification, binding, drift, recovery, and tamper-evident verified history.

Memory may inform identity. Memory alone does not prove identity.

## `velvet-docs`

Owns canonical cross-repository architecture, doctrine, ecosystem maps, contributor orientation, public/private boundaries, and deployment guidance spanning multiple components.

Repo-specific implementation details remain with the owning repository.

## `.github`

Owns organization-level profile material, shared issue/pull-request templates, and public contributor-facing defaults.

The organization profile should stay synchronized with `velvet-docs` whenever public architecture or repository ownership materially changes.

## `business_agent_ecosystem`

A public adjacent application/reference ecosystem. It can reuse Velvet doctrines and contracts where appropriate, but it is not a substitute for the shared Runtime/Court, Event Protocol, Communications, Language, Audio, Library, Receipts, or continuity organs.

## Private / Experimental Repositories

Private repositories remain outside the canonical public responsibility map until their own publication gates are met.

Current examples include:

- **Persona Continuity**: private identity/persona continuity, memory-privacy, and Character Foundry backend work. The public Interface may present a Foundry client without making this private repository a public-supported organ.
- **Cyberdeck**: private deployment/operator tooling for local vault format adapters, batch shelving, website-mirror integrity, and local Kiwix planning. It does not replace `velours_library` as the canonical knowledge owner.
- **Navigation**: private navigation planning/prototyping. Its existence does not create route authority or driving authority.
- **Home**, **Medical Mobility**, **Retrofit Architecture**, **Module Lab**, and interface/voice/showcase experiments: bounded private or experimental surfaces and deployment work.

Their existence does not grant public support, trust, Runtime/Court authority, or physical deployment readiness.

## Dependency Direction

A useful conceptual flow is:

```text
observation / retrieval / human input
  -> local Event Protocol or bounded ingress
  -> Core / Language / Runtime interpretation and proposal
  -> verified identity + Court policy
  -> safety + approved executor
  -> measured outcome + Receipts
  -> Continuity

cross-body payload only when policy permits
  -> Communications
  -> carrier
  -> receiving body's own governed ingress
```

A useful knowledge/presentation subflow is:

```text
canonical source + provenance
  -> Velour's Library catalog / retrieval evidence
  -> read-only Interface presentation or Core retrieval
  -> no automatic belief or authority
```

No presentation, language, audio, communications, memory, library, or observation layer may reach around Runtime/Court to gain physical authority.

## Emergency Authority Boundary

Verified emergency work may receive life-safety rank 0, but the responder request remains evidence rather than authority.

```text
verified incident
  -> rank 0
  -> incident policy
  -> capability + logical target
  -> incident-scoped Court identity
  -> Court authorization
  -> safety / executor / measured execution
```

The incident identity is not the owner's active session. Court authorization is not proof of physical execution.
