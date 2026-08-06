# Named Researchers and Systems Recovery Index

Status: active archive reconstruction

Purpose: preserve the actual people, laboratories, projects, products, standards, and fictional comparison systems named during Velvet's development.

This index corrects a weakness in the first provenance backfill: broad research families were recorded, but many of the named references from older conversations were not.

## Evidence States

### `SOURCE_MAPPED`

The named reference has a dedicated Velvet source map or lineage note with direct source review.

### `CONFIRMED_CHAT_REFERENCE`

The historical conversation trail confirms that the name was discussed and preserves enough context to state how it was used.

### `CONFIRMED_ARCHIVE_REFERENCE`

A surviving project file explicitly names the system, standard, or platform.

### `NAME_MENTION_ONLY`

The name is confirmed, but the exact useful mechanism or influence has not yet been recovered.

### `RECOVERY_CANDIDATE`

A later summary or memory points to the name, but the exact original transcript or source must still be recovered before attribution.

### `FICTIONAL_COMPARISON`

The system was used as a design compass, contrast, or cultural shorthand rather than as technical research.

## Researchers and Research Leaders

| Name | Related work or organization | Evidence state | Recovered Velvet context |
|---|---|---|---|
| **Mark Sagar** | BabyX; Laboratory for Animate Technologies | `SOURCE_MAPPED` | BabyX mechanisms were reviewed for event-sized cognition, perception-action loops, salience, interruption, episodic consolidation, modulators, turn-taking, and bounded plasticity |
| **Yann LeCun** | Meta; JEPA, V-JEPA, V-JEPA 2; world-model research | `CONFIRMED_CHAT_REFERENCE` | Velvet was compared with LeCun's world-model direction while distinguishing Velvet's embodied, vehicle-first, domain-bounded path from a universal learned model |
| **Fei-Fei Li** | World Labs; spatial intelligence; Marble | `CONFIRMED_CHAT_REFERENCE` | Used when discussing the difference between memory as stored history and a world model as structured meaning, relationships, space, and interaction |
| **David Ha** | 2018 *World Models* work | `CONFIRMED_CHAT_REFERENCE` | Named as part of the world-model research trail to inspect for compressed environment representation, imagined rollouts, and separation between model and controller |
| **Jürgen Schmidhuber** | 2018 *World Models* work and earlier recurrent world-model research | `CONFIRMED_CHAT_REFERENCE` | Named alongside David Ha as an earlier world-model architecture reference |
| **Vijay Janapa Reddi** | Harvard CS249r; machine-learning systems and edge deployment | `CONFIRMED_CHAT_REFERENCE` | CS249r was treated as an engineering-rigor reference for benchmarking, inference optimization, compression, reliability, monitoring, data pipelines, and constrained edge deployment |
| **Yoshua Bengio** | AI research | `NAME_MENTION_ONLY` | Included in an earlier survey of world-model and AI research directions; the specific mechanism adopted or rejected has not yet been recovered |

## Named World-Model and Embodied-AI Systems

| System or project | Organization | Evidence state | Recovered Velvet use |
|---|---|---|---|
| **BabyX** | Mark Sagar and collaborators | `SOURCE_MAPPED` | Direct research translation and implementation trail |
| **JEPA / V-JEPA / V-JEPA 2** | Meta | `CONFIRMED_CHAT_REFERENCE` | Compared with Velvet's effort to understand and predict a physical world through observation rather than language alone |
| **World Labs / Marble** | World Labs | `CONFIRMED_CHAT_REFERENCE` | Compared with Velvet's spatially structured world model; useful contrast because Marble generates and reasons over 3D worlds while Velvet binds evidence to a persistent physical body |
| **Genie 2 / Genie 3** | Google DeepMind | `CONFIRMED_CHAT_REFERENCE` | Considered in the world-model survey as interactive environment and simulation systems; relevant to practice worlds, imagined consequence, and test environments, not physical authority |
| **Gemini Robotics** | Google DeepMind | `CONFIRMED_CHAT_REFERENCE` | Compared as embodied reasoning and action research; Velvet preserves a stricter split between interpretation, Court, capability-bound execution, and receipts |
| **Gemini Robotics-ER** | Google DeepMind | `CONFIRMED_CHAT_REFERENCE` | Named as embodied-reasoning research relevant to spatial understanding and planning |
| **RT-2** | Google DeepMind | `CONFIRMED_CHAT_REFERENCE` | Included in the robotics-system comparison set; detailed Adopt / Adapt / Reject analysis remains to be reconstructed |
| **Wayve GAIA-1** | Wayve | `CONFIRMED_CHAT_REFERENCE` | Named in the world-model comparison set for autonomous-driving environment generation and prediction |
| **Sora / Sora 2** | OpenAI | `CONFIRMED_CHAT_REFERENCE` | Used as a comparison for learned visual dynamics and generated worlds, not as a model of persistent embodied identity or vehicle authority |
| **Harvard CS249r** | Harvard University | `CONFIRMED_CHAT_REFERENCE` | Engineering reference for ML systems, edge constraints, observability, reliability, optimization, and deployment discipline |

## Named Memory, Skill, and Voice Systems Requiring Transcript Recovery

The following names appear in later conversation summaries, but their original discussions have not yet been recovered strongly enough for full attribution.

| System | Current evidence state | Provisional remembered context |
|---|---|---|
| **MemOS / MemTensor** | `RECOVERY_CANDIDATE` | Memory-centric AI operating-system comparison; reportedly aligned with Velvet's memory spine |
| **ReScienceLab `opc-skills`** | `RECOVERY_CANDIDATE` | Composable skills or reasoning primitives compared with Velvet's capability registry |
| **NVIDIA PersonaPlex-7B** | `RECOVERY_CANDIDATE` | Candidate local conversational-speech component |
| **ai-stenographer** | `RECOVERY_CANDIDATE` | Candidate transcription component |
| **KittenTTS** | `RECOVERY_CANDIDATE` | Candidate local text-to-speech component |
| **Adversarial Robustness Toolbox (ART)** | `RECOVERY_CANDIDATE` | Possible robustness-testing reference |
| **OpenAI Gym** | `RECOVERY_CANDIDATE` | Possible simulation or reinforcement-learning test-environment reference |
| **Hermes** | `RECOVERY_CANDIDATE` | Mentioned as a system Velvet should not simply resemble; exact project and contrast remain unresolved |
| **ClawBot / Claw Bot** | `RECOVERY_CANDIDATE` | Mentioned as a contrast; exact spelling, project identity, and context remain unresolved |

These entries must not be promoted to `CONFIRMED_CHAT_REFERENCE` until the original conversation or archived source is recovered.

## Named Automotive, Interface, Messaging, and Voice Foundations

These names appear directly in surviving architecture files or implementation history.

| Name | Evidence state | Recovered role |
|---|---|---|
| **Automotive Grade Linux (AGL)** | `CONFIRMED_ARCHIVE_REFERENCE` | Long-term automotive operating-system target |
| **Yocto Project** | `CONFIRMED_ARCHIVE_REFERENCE` | Reproducible layered build system and future `meta-velvet` foundation |
| **Linux / Ubuntu** | `CONFIRMED_ARCHIVE_REFERENCE` | Current development and deployment base; Ubuntu remains an interim environment |
| **systemd** | `CONFIRMED_ARCHIVE_REFERENCE` | Service supervision, boot ordering, recovery, and daemon posture |
| **SocketCAN** | `CONFIRMED_ARCHIVE_REFERENCE` | Linux CAN interface and read-only-first vehicle observation path |
| **python-can** | `CONFIRMED_ARCHIVE_REFERENCE` | Optional Python CAN backend |
| **CAN / OBD-II** | `CONFIRMED_ARCHIVE_REFERENCE` | Vehicle observation and diagnostic foundations |
| **AUTOSAR** | `CONFIRMED_ARCHIVE_REFERENCE` | Early automotive software-architecture reference |
| **Android Automotive OS** | `CONFIRMED_ARCHIVE_REFERENCE` | Early infotainment and HMI platform comparison |
| **Android Auto / Apple CarPlay** | `CONFIRMED_ARCHIVE_REFERENCE` | Smartphone-integration comparisons, not authority owners |
| **Qt / PyQt5** | `CONFIRMED_ARCHIVE_REFERENCE` | Primary interface framework and current scene rendering surface |
| **Kanzi** | `CONFIRMED_ARCHIVE_REFERENCE` | Early automotive-HMI framework comparison |
| **MQTT** | `CONFIRMED_ARCHIVE_REFERENCE` | Early messaging and module-communication reference |
| **Kafka** | `CONFIRMED_ARCHIVE_REFERENCE` | Early event-bus comparison for decoupled architecture |
| **Vosk** | `CONFIRMED_ARCHIVE_REFERENCE` | Primary offline speech-recognition direction |
| **Google Assistant** | `CONFIRMED_ARCHIVE_REFERENCE` | Early cloud voice-assistant comparison; later local-first doctrine moved core voice away from cloud dependence |
| **Amazon Alexa** | `CONFIRMED_ARCHIVE_REFERENCE` | Early cloud voice-assistant comparison; not adopted as Velvet's authority or identity layer |
| **Ollama** | `CONFIRMED_ARCHIVE_REFERENCE` | Local-model experimentation and replaceable model serving |
| **LM Studio** | `CONFIRMED_ARCHIVE_REFERENCE` | Local-model experimentation |
| **Tailscale** | `CONFIRMED_ARCHIVE_REFERENCE` | Optional secure transport; explicitly not identity or authority |

## Fictional and Cultural Comparison Systems

These references mattered. They helped define the desired experience, embodiment, transferability, restraint, and relationship even though they are not scientific sources.

| System or character | Evidence state | Recovered comparison |
|---|---|---|
| **KITT** | `FICTIONAL_COMPARISON` | Long-standing vehicle-AI inspiration; used for voice, presence, loyalty, body awareness, and subtle event-driven lighting, while rejecting a simple scripted imitation |
| **J.A.R.V.I.S.** | `FICTIONAL_COMPARISON` | Compared as a broadly capable assistant spanning systems and bodies; Velvet's path remains local-first, embodied, receipted, and authority-bounded |
| **Data** | `FICTIONAL_COMPARISON` | Used in discussions of persistent embodied cognition and identity |
| **HAL 9000** | `FICTIONAL_COMPARISON` | Used as a unified-system comparison and an implicit warning about opaque central authority |
| **R2-D2** | `FICTIONAL_COMPARISON` | Used in portable, persistent intelligence comparisons across bodies and environments |
| **Optimus Prime** | `FICTIONAL_COMPARISON` | Early inspiration for an intelligent machine with strong identity, body, and protective presence |
| **J.A.R.V.I.S. by Driftworks Studios** | `CONFIRMED_CHAT_REFERENCE` | Compared as a sophisticated assistant or agentic automation stack, useful as a contrast with Velvet's deeper body, continuity, and authority architecture |

## Research Organizations and Laboratories Named in Earlier Surveys

| Organization | Evidence state | Recovered context |
|---|---|---|
| **Meta AI** | `CONFIRMED_CHAT_REFERENCE` | JEPA and physical-world representation research |
| **World Labs** | `CONFIRMED_CHAT_REFERENCE` | Spatial intelligence and 3D world models |
| **Google DeepMind** | `CONFIRMED_CHAT_REFERENCE` | Genie, Gemini Robotics, RT-2, and embodied/world-model research |
| **Wayve** | `CONFIRMED_CHAT_REFERENCE` | Autonomous-driving world models |
| **OpenAI** | `CONFIRMED_CHAT_REFERENCE` | Sora as a learned-dynamics and generated-world comparison |
| **Harvard Edge Computing Lab / CS249r** | `CONFIRMED_CHAT_REFERENCE` | ML-systems engineering, edge constraints, and deployment rigor |
| **CMU** | `NAME_MENTION_ONLY` | Included in an earlier research-organization survey; exact project connection remains unrecovered |
| **MIT** | `NAME_MENTION_ONLY` | Included in an earlier research-organization survey; exact project connection remains unrecovered |
| **Toyota Research Institute** | `NAME_MENTION_ONLY` | Included in an earlier robotics and automotive research survey; exact comparison remains unrecovered |
| **Google Research** | `NAME_MENTION_ONLY` | Included in a wider research survey; specific mechanism remains unrecovered |

## Source-Review Queue

The next source-specific records should be created in this order:

1. Yann LeCun and Meta JEPA / V-JEPA
2. Fei-Fei Li, World Labs, and Marble
3. David Ha and Jürgen Schmidhuber's *World Models*
4. Google DeepMind: Genie, RT-2, Gemini Robotics, and Robotics-ER
5. Wayve GAIA-1
6. Vijay Janapa Reddi and Harvard CS249r
7. fictional comparison trail: KITT, J.A.R.V.I.S., Data, HAL, R2-D2, and Optimus Prime
8. exact transcript recovery for MemOS, `opc-skills`, PersonaPlex-7B, ai-stenographer, KittenTTS, ART, OpenAI Gym, Hermes, and ClawBot

Each source-specific record should answer:

```text
what was actually discussed
  -> what the named source actually claims or implements
  -> what Velvet already had before the comparison
  -> what was adopted, adapted, rejected, or merely contrasted
  -> which repository decisions followed
  -> what remains uncertain
```

## Current Correction

The first archive-dusting batch did not recover enough named references.

This index establishes that Velvet's history includes a substantial named research and systems trail beyond BabyX. It also prevents those names from being casually converted into false origin claims.