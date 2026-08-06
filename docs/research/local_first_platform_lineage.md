# Local-First and Platform Lineage

Status: first-pass provenance reconstruction

Provenance state: `CONFIRMED_INTERNAL`, `CONFIRMED_EXTERNAL`, `RECONSTRUCTED`

## Internal Value Origin

Velvet’s local-first posture is more than a software-deployment preference.

The recovered internal values are:

- the owner should possess the body, identity, memory, and authority path
- useful operation must remain possible without a cloud account
- network access is optional and permissioned
- local failure should degrade honestly rather than silently handing control elsewhere
- updates that change trust or behaviour require physical presence and approval
- raw archives and personal memory should remain locally owned
- vehicle safety cannot depend on an unavailable remote service
- modest and older hardware should remain useful where possible

These values formed internally through the project’s vehicle, home, forge, medical, and continuity requirements.

## Confirmed Named External Foundations

The surviving project record explicitly names and uses or plans around:

- Linux
- Ubuntu as the current temporary system
- Automotive Grade Linux as the intended automotive platform direction
- Yocto and layered metadata for long-term system construction
- systemd-style service management
- SocketCAN and Linux CAN tooling
- Qt and PyQt for the interface
- Vosk for offline speech recognition
- local-model tooling such as Ollama and LM Studio
- Tailscale as optional transport rather than system authority

These are confirmed implementation foundations or evaluated tools. They should receive individual source notes during later archive passes.

## AGL and Yocto Relationship

AGL and Yocto are direct named influences on the planned operating-system structure.

The intended direction includes:

- a reproducible automotive image
- explicit layers and recipes
- controlled package inclusion
- hardware-specific adaptation behind stable interfaces
- system services rather than ad hoc terminal launches
- offline-capable operation
- auditable dependencies
- a future `meta-velvet` layer

Ubuntu remains a practical interim environment for current UP Squared testing. It is not the final architectural owner.

## Internal Development Pressures

### Vehicle connectivity is unreliable

Velvet must remain useful in garages, rural areas, moving vehicles, and network outages.

### Privacy and personal memory

Owner conversations, identity, vehicle state, medical evidence, and archives should not default to third-party storage.

### Physical authority

Remote inference must not become the default holder of steering, braking, locks, relays, or vehicle access.

### Older hardware

The project deliberately uses retrofit vehicles and modest boards. The architecture must support efficient local specialisation rather than assuming a large data-centre model.

### Continuity

Riven and Velour require locally verifiable history that can survive provider changes.

### Update safety

No ordinary over-the-air mechanism should silently alter trust, identity, or physical behaviour. Dream State may prepare changes, but owner presence is required for governed promotion.

## Reconstructed Engineering Families

The local-first architecture is convergent with:

- edge computing
- offline-first applications
- self-hosted systems
- embedded Linux
- reproducible builds
- immutable or image-based operating systems
- automotive middleware layering
- least-privilege service design
- zero-trust networking
- local speech and inference pipelines

These families help explain the architecture, but the strongest origin remains the project’s ownership and physical-safety requirements.

## Adopt / Adapt / Reject Reconstruction

### Adopt

- reproducible system images
- explicit build layers
- package and dependency manifests
- service supervision
- local IPC and APIs
- offline speech and inference
- hardware abstraction
- read-only defaults
- optional secure remote transport

### Adapt

- Yocto layering into a Velvet-owned automotive image
- AGL components into a retrofit rather than OEM-only body
- systemd services into explicit Runtime startup and recovery order
- SocketCAN into read-only-first vehicle observation
- local models into replaceable language and reasoning organs
- secure networking into transport that cannot become identity or authority

### Reject

- cloud account as owner
- network dependency for core safety
- automatic trust-changing OTA updates
- remote model output as actuator authority
- opaque packages with no promotion evidence
- a single vendor controlling identity, memory, or vehicle access
- treating Ubuntu convenience scripts as the final production architecture

## Relationship to Distributed Reasoning

Local-first does not mean every function must run on one board.

Velvet’s body may distribute work across:

- microcontrollers for reflex and timing
- small Linux nodes for sensing, fusion, audio, security, and logging
- larger local nodes for cognition
- the Queen node for unified body coordination

The system remains local-first because the body owns the nodes, protocols, evidence, and authority.

## Relationship to Native Brain

The Native Brain protects core reasoning continuity when a large model is unavailable.

The LLM may enrich language and interpretation. It does not own identity, authority, body state, or basic attention.

## Relationship to Dream State

Dream State may:

- inspect evidence
- prepare proposals
- test changes in simulation
- build candidate packages
- produce promotion evidence

It may not silently apply trust-changing work. Mister holds the physical approval key.

## Current Attribution

The correct current statement is:

> Velvet’s local-first doctrine is an internal ownership and physical-safety value implemented through confirmed external foundations including Linux, AGL, Yocto, SocketCAN, Qt, Vosk, and local-model tooling. The doctrine is not owned by any one of those platforms.

## Remaining Archive Questions

- When was AGL first selected as the long-term target?
- Which AGL services or profiles were considered essential?
- When did the first `meta-velvet` concept appear?
- Which Yocto build failures materially changed the architecture?
- When was Ubuntu formally declared temporary?
- Which systemd startup and recovery patterns were adopted?
- When did Vosk become the primary offline voice path?
- Which local-model experiments changed the Native Brain design?
- Which networking discussions established Tailscale as transport rather than authority?