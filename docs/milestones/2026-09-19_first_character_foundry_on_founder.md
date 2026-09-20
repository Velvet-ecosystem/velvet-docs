# First Character Foundry Run on Founder

Date: 2026-09-19  
Hardware: UP Squared Founder board  
Host operating system: Ubuntu 20.04 development environment  
Python: pyenv Python 3.10.20

## Milestone

The physical Founder UP² opened and exercised Character Foundry from the Forge interface for the first time.

This was the first real Forge application brought up through the mapped Founder Forge workspace rather than a placeholder landing surface.

The working path was:

```text
Forge workstation
  -> Interface router
  -> Character Foundry scene
  -> Interface FoundryBridge
  -> Persona Continuity FoundryService
  -> local candidate workspace
```

## Commissioning Trail

The first Forge test reached the Character Foundry touchpoint but remained on Forge and reported:

```text
Scene not found: character_foundry
```

A direct import probe then established the actual dependency failure:

```text
ModuleNotFoundError: No module named 'velvet_persona'
```

The Forge routing itself was therefore not the fault. Founder did not yet have the canonical Persona Continuity package available to the Python environment running Interface.

Commissioning then:

1. confirmed Founder was running Python 3.10.20;
2. confirmed `velvet-persona-continuity` was not present in the local Velvet workspace;
3. cloned the canonical `Velvet-ecosystem/velvet-persona-continuity` repository to Founder;
4. installed that repository as an editable local package into the active pyenv Python environment;
5. verified `velvet_persona.foundry_service` resolved from the canonical local repository;
6. relaunched Founder with owner presence asserted for the development session;
7. opened Character Foundry successfully from its Forge workstation.

## Functional Proof

The session went beyond rendering the workspace.

On the physical touchscreen the operator:

- selected a Software Module candidate type;
- opened New Candidate;
- supplied a stable candidate ID;
- received a canonical software-module scaffold;
- edited candidate fields;
- reached the enabled Create Draft operation;
- pressed Create Draft, exercising the real Interface-to-Foundry service path.

The visible workspace retained the Foundry guardrails during the interaction:

```text
Authority             NONE
Capability grants     NONE
Court tokens          NONE
Execution             DISABLED
Actuation             DISABLED
Canonical memory write DISABLED
Lineage certification DISABLED
Automatic merge/deploy DISABLED
```

This proof does not grant any Runtime, Court, deployment, merge, lineage, memory, or physical authority.

## Architectural Lesson

A repository existing elsewhere in the ecosystem does not make its Python package available on Founder.

Character Foundry intentionally has no duplicate Interface implementation of candidate semantics. Interface depends on the canonical Persona Continuity service and fails closed when that service is absent.

For the current Founder development environment, the canonical source is installed editable so the import resolves directly into the checked-out Persona Continuity repository.

## What Was Proven

- the Forge Character Foundry touchpoint routes correctly;
- the trusted Character Foundry scene can register on physical Founder hardware;
- Interface can bind to the canonical Persona Continuity Foundry service;
- the real Qt Foundry workspace operates at the Founder's 1152 x 648 development surface;
- candidate scaffolding is reachable through touchscreen interaction;
- the Foundry's authority boundaries remain visibly disabled while editing;
- the Forge can host a real Velvet application, not only image-first navigation and placeholder workspaces.

## What Remains

This milestone does not claim final visual integration. The Character Foundry widget still needs later refinement for the Founder visual language and available screen area.

The broader Forge workspaces for Eleanor Engineering, Engineering Design, Module Lab, and Test Bench remain separate integration work.

Candidate persistence, reload/discard behavior, promotion handoff behavior, and longer-running operational tests should continue to be verified independently rather than inferred from this first application run.

## Final Receipt

> On 2026-09-19, Character Foundry became the first real Forge application exercised on the physical Founder UP². The missing canonical Persona Continuity dependency was identified rather than bypassed, installed into the active Founder Python environment, and the resulting Foundry workspace successfully reached its candidate-creation path while retaining zero execution and actuation authority.
