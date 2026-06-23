# Getting Started with Velvet

This page is the canonical front door for the public Velvet ecosystem.

Velvet is not a single application or a chatbot wrapper. It is an offline-first, local-API-first ecosystem in which cognition proposes, policy authorizes, executors act, and receipts preserve evidence.

> Brain proposes. Court authorizes. Executors act. Receipts remember.

## Current Status

Velvet is alpha software under active development.

The public repositories currently provide architecture, doctrine, contracts, tests, read-only Runtime observation paths, interface scenes, receipt handling, continuity foundations, event schemas, and conservative CAN observation.

Current public physical authority is intentionally limited. Newcomers should begin with documentation, tests, simulation, and read-only Runtime paths before considering hardware integration.

## Choose Your Path

### I want to understand Velvet

Start with:

1. [Ecosystem Overview](ecosystem_overview.md)
2. [Repository Map](repository_map.md)
3. [Authority and Execution Path](authority_and_execution_path.md)
4. [Rebellion Against OEM](rebellion_against_oem.md)

### I want to run something

Begin with `velvet-runtime`.

The present safe entry path is the read-only Runtime CLI and its tests. Follow that repository's README, run the startup doctor, then exercise Runtime status and host telemetry before adding optional CAN observation.

Expected progression:

```text
clone Runtime
  -> create a local Python environment
  -> install repository requirements
  -> run tests
  -> run the startup doctor
  -> launch read-only Runtime paths
  -> inspect generated receipts
```

A one-command development bootstrap is a tracked Runtime milestone. Until it lands, the Runtime README remains the source of truth for exact commands and required local state.

### I want to build a surface or interface

Read:

1. [Scene Doctrine](scene_doctrine.md)
2. [Scene and Surface Model](scene_and_surface_model.md)
3. the `velvet-interface` README and examples

Interfaces express state and route intent. They do not directly actuate hardware.

### I want to work with vehicle data

Read:

1. [Decoded CAN Observation Path](decoded_can_observation_path.md)
2. the `velvet-vehicle-can` README
3. the Runtime CAN observation documentation

Begin receive-only. Kernel listen-only mode and conservative decoding are part of the safety boundary.

### I want to contribute

Choose the repository that owns the boundary you are changing. Use the [Repository Map](repository_map.md) before opening a pull request.

Cross-repository changes must identify:

- the owning contract
- affected repositories
- compatibility impact
- test impact
- receipt or continuity impact
- documentation impact

## The Public Repository Set

- `velvet-ai-core`: cognition, identity, memory use, and coordination
- `velvet-runtime`: local execution nervous system and authority enforcement
- `velvet-interface`: scenes, surfaces, widgets, and intent routing
- `velvet-vehicle-can`: receive-only CAN observation and conservative decoding
- `velvet-event-protocol`: shared event schemas and transport boundaries
- `velvet-receipts`: receipt formats, integrity, and verification
- `velvet-continuity-spine`: genesis identity, lineage, and continuity
- `velvet-docs`: canonical cross-repository doctrine and orientation

## Safety Boundary

For public development, the default order is:

```text
document
  -> test
  -> simulate
  -> observe
  -> authorize narrowly
  -> execute only through approved paths
  -> preserve receipts
```

Do not bypass Runtime, Court authorization, safety gates, approved executors, physical-presence requirements, or receipt persistence to make a demonstration appear complete.

## Getting-Started Flag

This page is a living ecosystem checkpoint.

It must be reviewed whenever any of the following changes:

- the first recommended repository
- installation or bootstrap commands
- supported Python versions
- Runtime startup flow
- public demo capabilities
- hardware support
- authority or safety boundaries
- repository ownership
- compatibility requirements

A feature is not fully public-facing until a newcomer can discover it from this page or from the repository path linked here.

## Near-Term Completion Checklist

- [ ] one-command development Runtime bootstrap
- [ ] reproducible simulation or demo path
- [ ] exact clean-machine prerequisites
- [ ] expected first successful output
- [ ] sample request and receipt walkthrough
- [ ] links from organization profile and primary repository READMEs
- [ ] cross-repository compatibility check
- [ ] periodic newcomer-path verification

As Velvet climbs, this flag climbs with it.