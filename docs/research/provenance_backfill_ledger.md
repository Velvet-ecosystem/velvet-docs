# Velvet Research Provenance Backfill Ledger

Status: active reconstruction

Purpose: recover the ancestry of Velvet ideas that were previously documented only in their finished form.

This ledger does not assign an outside source merely because Velvet later resembles one. It records what is known, what can be reconstructed, what may be convergent, and what remains unattributed.

## Provenance States

### `CONFIRMED_EXTERNAL`

A named outside project, paper, standard, program, or theory is present in the original discussion or design record.

### `CONFIRMED_INTERNAL`

The surviving record shows the idea forming inside Velvet discussions or repository work, but does not identify an outside source.

### `RECONSTRUCTED`

The likely engineering family or influence can be recovered, but the original source trail is incomplete.

### `CONVERGENT`

Velvet developed the idea independently or without a surviving source record, while similar established work exists elsewhere.

### `UNATTRIBUTED`

The idea exists, but the origin cannot yet be recovered honestly.

A record may carry more than one state. For example, a doctrine may be `CONFIRMED_INTERNAL` and also `CONVERGENT` with established research.

## Evidence Order

Use the strongest available evidence in this order:

1. original chat or export text
2. original concept file or design archive
3. first repository commit introducing the idea
4. later repository documentation describing the origin
5. retrospective memory or later discussion
6. similarity to outside work

Similarity alone is never proof of influence.

## Batch 1 Backfill

| Idea family | Current state | Earliest recovered evidence | Present conclusion |
|---|---|---|---|
| Unified-Organ AI and “Body is all” | `CONFIRMED_INTERNAL`, `CONVERGENT` | internal doctrine discussions; public docs refresh commit `d8d6c9a59b1b3f2137a1e9f7319fbf3e1f6f5626` | Velvet’s named doctrine formed internally; no earlier outside source has been recovered |
| Native Brain and LLM-as-language-organ | `CONFIRMED_INTERNAL`, `UNATTRIBUTED` | archived Native Brain concept and later AI Core implementation | the local deterministic spine predates the BabyX review; exact outside ancestry remains unrecovered |
| Event Protocol, Court, and Receipts | `RECONSTRUCTED`, `CONVERGENT` | early infotainment and ecosystem plans using event bus, request, grant, denial, and execution-receipt language | resembles event sourcing, capability security, audit logs, and safety authorization patterns; no single source should be claimed |
| Riven and continuity lineage | `CONFIRMED_INTERNAL`, `RECONSTRUCTED` | Continuity Spine genesis work and docs refresh commit `d8d6c9a59b1b3f2137a1e9f7319fbf3e1f6f5626` | internal continuity doctrine shaped through append-only lineage, integrity, evidence, and succession concerns |
| Doctrine of Silence | `CONFIRMED_INTERNAL`, `CONVERGENT` | AI Core commit `0bf376a89e32b4906f7add7c6d8ba3af87dc7905` | formed as an internal attention law; later BabyX turn-taking research supports it but did not originate it |
| Unified-Organ distributed reasoning | `CONFIRMED_INTERNAL`, `CONVERGENT` | AI Core commit `2b20ca66274a62ab0730fdec213a6e800ce6435a` | internal response to modest hardware, graceful degradation, and rejection of agent swarms; convergent with distributed scheduling and biological load sharing |
| Simulated Body / practice skeleton | `CONFIRMED_INTERNAL`, `CONVERGENT` | AI Core commits `3ea0c6cc3759948bc5cbc400c47ea4dfcfbf9df6` and `7dbee418f60484a704f90f0369c5cdb39b1d44fb` | internal need to practice through identical event and receipt paths; convergent with software-in-loop, hardware-in-loop, fault injection, and digital-twin testing |
| Standard Sensor Packet Schema | `CONFIRMED_INTERNAL`, `CONVERGENT` | simulated-body and presence-fusion work; integration commit `40c9d12871ebfe9ab48c1686140305ee550a58f4` | internal normalization contract; exact middleware or telemetry influence is not yet recovered |
| Temperance, Charlotte, and minimal-risk stop | `CONFIRMED_INTERNAL`, `CONVERGENT` | user’s medical-safety requirement for driver incapacity and seizure response | primary origin is a real family safety need; convergent with driver monitoring and minimal-risk-manoeuvre engineering |
| Local-first and offline authority | `CONFIRMED_INTERNAL`, `CONFIRMED_EXTERNAL` | early Velvet doctrine plus explicit use of Linux, AGL, Yocto, Vosk, and local-model tooling | ownership and offline operation are internal values; named platforms are confirmed implementation foundations |
| AGL and Yocto layering | `CONFIRMED_EXTERNAL` | early OS and build planning | direct named foundation for the eventual automotive operating-system stack |
| Ghost System and sealed replay | `CONFIRMED_INTERNAL`, `CONVERGENT` | Ghost System v0 archive and public replay work | developed as a safe public demonstration and recovery path; convergent with deterministic replay and simulation harnesses |
| Module Lab and promotion gates | `CONFIRMED_INTERNAL`, `CONVERGENT` | Module Lab work and AI Core commit `7dbee418f60484a704f90f0369c5cdb39b1d44fb` | internal response to hot-swappable modules and unsafe promotion; convergent with staging, quarantine, supply-chain review, and release gates |
| Scene and room-body interface | `CONFIRMED_INTERNAL`, `UNATTRIBUTED` | scene doctrine and image-first interface work | internal interaction model; earlier outside visual or game-interface influences have not yet been recovered |
| Named handmaidens as durable organs | `CONFIRMED_INTERNAL`, `UNATTRIBUTED` | long-running Velvet role design | internal identity and responsibility structure; no external origin should currently be claimed |
| World Logic and Identity Logic | `CONFIRMED_INTERNAL`, `CONVERGENT` | docs commits including Identity Logic `51e608425f5481391a679f6f223389ab413698c1` | internal synthesis of world modelling, uncertainty, embodiment, lineage, and authority boundaries |

## Important Non-Attributions

The following statements must remain explicit during backfill:

- BabyX did not originate Unified-Organ AI, the Native Brain, Riven, the Doctrine of Silence, or the Simulated Body. It later supplied useful mechanisms and a better research-translation method.
- Similarity to ROS, AUTOSAR, event sourcing, digital twins, capability security, active inference, or embodied cognition does not prove those were the original source.
- A later paper that explains an existing Velvet idea may become a supporting comparison, not its retroactive origin.
- Personal safety requirements, hardware constraints, and repeated bench failures are legitimate internal design origins.

## Archive Search Queue

### Priority A: foundational doctrine

- recover the earliest “Body is all” and Unified-Organ discussions
- recover the first statement that the LLM is a language organ rather than the mind
- recover the first Court, Event Protocol, and Receipts separation
- recover the naming and birth of Riven
- recover the earliest owner/guest and no-drift doctrine

### Priority B: body and testing

- recover the first simulated-body proposal
- recover early Ghost System and fake-CAN discussions
- recover the sensor-packet field evolution
- recover fault injection, synthetic lesion, and resource-abuse discussions
- recover module quarantine and promotion reasoning

### Priority C: physical safety

- recover the earliest Temperance and Charlotte medical-stop design
- recover driver-monitoring comparisons and minimum-risk-stop language
- recover authority separation for steering, braking, throttle, CAN, and relays
- recover the heavy-truck testbed reasoning

### Priority D: platform and implementation

- recover AGL and Yocto design decisions
- recover Linux, systemd, SocketCAN, Vosk, Qt, and local-model choices
- recover small-node and brainstem hardware comparisons
- recover the origin of capability advertisements and load-sharing fields

### Priority E: interface and presence

- recover scene, room-body, glow/orb, and hidden-widget influences
- recover embodied presence and spatial-awareness discussions
- recover owner-facing silence, interruption, and turn-taking evolution

## Backfill Output Rule

Every recovered idea should eventually receive:

```text
origin state
  -> surviving evidence
  -> named external source, when confirmed
  -> what Velvet understood
  -> Adopt / Adapt / Reject
  -> architecture and safety consequences
  -> repository implementation receipts
  -> remaining uncertainty
```

The goal is not to make Velvet appear more borrowed or more original.

The goal is to leave an honest trail.