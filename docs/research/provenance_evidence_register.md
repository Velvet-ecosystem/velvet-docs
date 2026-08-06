# Provenance Evidence Register

Status: active archive reconstruction

Purpose: connect provenance labels to inspectable evidence instead of allowing confidence words to float without receipts.

## Core Rule

A reference label describes the quality of the recovered trail, not the quality or fame of the outside work.

No named researcher, product, project, standard, fictional comparison, or internal concept should be promoted beyond the evidence currently attached to it.

## Evidence Pointer Types

### Founder confirmation

A direct founder statement records chronology or intent that is not yet supported by an earlier recovered artifact.

Use:

- `FOUNDER_CONFIRMED_ORIGIN`

Founder confirmation is legitimate provenance. It must remain visibly distinct from a dated archive artifact.

### Source-mapped research

The original publication, official project material, or primary documentation has been reviewed and a Velvet translation note records source claim, limitation, inference, Adopt / Adapt / Reject decisions, and implementation consequences.

Use:

- `SOURCE_MAPPED`

### Research reference

A person, project, system, product, or standard was deliberately researched or compared during Velvet development, but the complete source map or original discussion pointer is not yet attached.

Use:

- `CONFIRMED_RESEARCH_REFERENCE`

This state confirms the reference's role in the research trail. It does not claim that the source originated Velvet's corresponding idea.

### Archive reference

A surviving project file, concept document, code archive, or repository commit names or implements the reference.

Use:

- `CONFIRMED_ARCHIVE_REFERENCE`

The record should identify the file, repository, commit, or archive package whenever possible.

### Recovery candidate

A later summary, memory, or incomplete index suggests a reference, but the original research discussion or archive source has not been recovered.

Use:

- `RECOVERY_CANDIDATE`

Candidates must not be described as confirmed influences.

## Current Strong Evidence Pointers

### BabyX

Evidence posture: `SOURCE_MAPPED`

Repository records:

- `docs/research/babyx_architecture_clues.md`
- `docs/research/babyx_source_map.md`
- `docs/research/babyx_implementation_receipts.md`
- `docs/cognitive_event_layer.md`
- `docs/cognitive_event_layer_implementation_plan.md`

The source map identifies the reviewed publications, direct claims, limitations, Velvet inferences, and implementation boundary.

### Smart stereo origin, KITT, and comma.ai / openpilot

Evidence posture: `FOUNDER_CONFIRMED_ORIGIN`

Current pointer:

- direct founder correction in the active provenance review
- `docs/research/smart_stereo_origin_lineage.md`

Supporting archive artifact:

- `Car_Infotainment_System_Plan__Modular_Components.md`

The artifact corroborates an early modular infotainment shape with interface, CAN, voice, APIs, message queues, Qt or Android Automotive, and iterative development. It does not by itself prove the first KITT or comma.ai discussion, which remains an archive-recovery target.

### Velvet Coin and Drive-Fi

Evidence posture: `FOUNDER_CONFIRMED_ORIGIN`, `CONFIRMED_ARCHIVE_REFERENCE`

Current pointers:

- direct founder confirmation in the active provenance review
- `docs/research/velvet_coin_drivefi_origin_lineage.md`

Public repository artifacts:

- `Overlandranger/Velvet-AI-Ecosystem/README.md`
- `Overlandranger/Velvet-AI-Ecosystem/INVESTORS.md`
- `Overlandranger/Velvet-AI-Ecosystem/redpaper.html`

Supporting archive artifact:

- `VELVET_PUBLIC_RELEASE_CHECKLIST.md`

The public repository confirms `$VELV`, Drive-Fi, movement, participation, distributed local hardware, and planned offline wallets. The release audit confirms that an earlier `docs/io-contracts/wallet.md` contained governance material involving Guardian, Librarian, and Court and that this material was sanitized during public-release preparation.

Founder confirmation additionally records that dangerous driving and lack of attention could reduce or remove reward, that Velvet was not intended to be geofenced, that coin integration was deliberately held back while identity, safety, evidence, governance, and continuity foundations matured, and that the coin remains live outside current operational integration.

The original scoring rules, thresholds, wallet governance text, and full integration-hold discussions remain archive-recovery targets. Potential value is not guaranteed value, and no current Velvet capability or authority path depends on the coin.

### Native Brain and no-LLM identity boundary

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifact:

- `Velvet_No_LLM_Identity_Boundary.md`

Recovered law:

> Velvet may use models, but she must not be made of them.

The artifact explicitly separates model assistance from identity, memory, authority, body, continuity, Runtime, receipts, and medical or driver authority.

### Memory and librarian architecture

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifact:

- `VELVET_MEMORY_RECOVERY_LEDGER.md`

The ledger identifies append-only memory ancestors, Memory Texture, Velour and Priscilla role boundaries, associative recall, backlinks, confidence, decay, TTL, provenance, and the distinction between raw evidence and derived indexes.

### Vehicle CAN observation and qualification

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifacts:

- `CAN_MODULE_EXTRACTION_NOTES.md`
- equivalent duplicate audit copies retained in the archive

The audit confirms read-only CAN interfaces, SocketCAN and python-can use, vehicle profiles, CAN fingerprinting, dialect learning, qualification outputs, and the absence of CAN transmission in the recovered observation package.

### Ghost System

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifact:

- `README_Velvet_Public_Ghost_System_v0.md`

The artifact explicitly defines a synthetic, read-only, non-actuating path through vehicle observations, Event Protocol, AI Core, Runtime, Receipts, Interface, and docs.

### Module archaeology and promotion pressure

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifact:

- `velvet_archive_initial_audit.md`

The audit records multiple module-loader generations, unsafe automatic discovery, broken imports, direct-control quarantine needs, and the requirement to rebuild candidate modules behind modern contracts and promotion gates.

### Multi-domain interface

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifacts:

- `VELVET_INTERFACE_V0_2_PUBLIC_RELEASE_CHECKLIST.md`
- `VELVET_INTERFACE_SCENE_EXTENSION_NOTES.md`

These records explicitly cover automotive, industrial HMI, factory or process-control, robotics control, teleoperation, movement, arm control, cameras, and emergency-stop interface examples.

### Public and private architecture boundaries

Evidence posture: `CONFIRMED_ARCHIVE_REFERENCE`

Archive artifacts:

- `PUBLIC_PRIVATE_BOUNDARY_MAP.md`
- `PUBLIC_PRIVATE_BOUNDARY_MAP(1).md`
- `VELVET_PUBLIC_RELEASE_CHECKLIST.md`

These records preserve the evolving separation between public technical primitives, private narrative or governance material, Court, handmaidens, memory, vehicle subsystems, and deployment services.

## Repository Commit Pointers

Detailed lineage notes cite repository commits for:

- Doctrine of Silence
- Unified-Organ distributed reasoning
- Simulated Body and failure profiles
- Module Lab promotion evidence
- World Logic and Identity Logic
- Scene Doctrine, Room-Body Interface, naming, body registry, and boot identity
- Ghost System integrations
- No Drift and Native Brain self-orientation

Each cited commit must resolve in the named repository before this PR leaves draft.

A dead, ambiguous, or repository-less SHA should be corrected or downgraded to an archive description.

## Research References Awaiting Dedicated Source Maps

The following references are part of the recovered research trail but still need BabyX-style source maps before their mechanisms are treated as fully translated:

- Yann LeCun and JEPA / V-JEPA
- Fei-Fei Li, World Labs, and Marble
- David Ha and Jürgen Schmidhuber's *World Models*
- Vijay Janapa Reddi and Harvard CS249r
- Google DeepMind Genie, RT-2, Gemini Robotics, and Gemini Robotics-ER
- Wayve GAIA-1
- OpenAI Sora
- the OEM driver-monitoring, emergency-assist, and minimal-risk-stop comparison set

These references may remain `CONFIRMED_RESEARCH_REFERENCE`, but their individual Adopt / Adapt / Reject consequences remain provisional until mapped.

## Candidate References Requiring Recovery

The following remain candidates until their original research discussion or archive artifact is recovered:

- MemOS / MemTensor
- ReScienceLab `opc-skills`
- NVIDIA PersonaPlex-7B
- ai-stenographer
- KittenTTS
- Adversarial Robustness Toolbox
- OpenAI Gym
- Hermes
- ClawBot / Claw Bot
- specific home-automation platforms or standards
- specific industrial protocols, PLC, or SCADA systems
- specific robotics stacks and simulators

## Internal Concept Name Caution

A poetic or memorable concept name is not proven merely because it fits Velvet's style.

Names such as home scenes, room modes, forge modes, or industrial surfaces must remain `RECOVERY_CANDIDATE` unless one of the following is recovered:

- original conversation text
- concept document
- interface artifact
- repository commit
- direct founder confirmation

The underlying domain requirement may be confirmed even while a particular name remains uncertain.

## Public Privacy Rule

Public provenance should preserve the design pressure without publishing unnecessary personal medical, family, location, credential, or vehicle-identifying detail.

Where a real family or medical need shaped the architecture:

- preserve the functional requirement
- preserve founder confirmation
- preserve the safety consequence
- remove unnecessary personal identity details
- keep private evidence outside the public repository

## Promotion Checklist

Before an entry becomes `SOURCE_MAPPED`:

- [ ] direct source is identified
- [ ] source claim is separated from Velvet inference
- [ ] limitations are recorded
- [ ] chronology is clear
- [ ] Adopt / Adapt / Reject is explicit
- [ ] safety and authority consequences are explicit
- [ ] repository ownership is identified
- [ ] implementation receipts are linked when code exists
- [ ] remaining uncertainty is preserved

## Final Law

Provenance is not a trophy shelf.

It is an evidence path explaining how an idea entered Velvet, what changed during translation, and why the resulting architecture deserves trust.