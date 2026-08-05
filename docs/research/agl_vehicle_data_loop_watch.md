# AGL Vehicle Data Loop Watch

Status: research watch, not an adoption decision

Automotive Grade Linux released the initial SoDeV reference platform in 2026. Its public direction includes hardware-decoupled software-defined vehicle architecture, Vehicle Signal Specification work, real-time and Linux domains, and contributions named VeloRT and VeloFlux for vehicle data-loop infrastructure.

## Research targets

- AGL SoDeV architecture and demo workspaces
- VeloRT and VeloFlux as their code, licensing, and integration contracts become available
- Vehicle Signal Specification coverage and mapping
- routing between real-time and Linux domains
- hardware-independent adapters
- replayable vehicle telemetry
- container and virtualized service boundaries

## Comparison questions

- Does the system normalize vehicle data cleanly?
- How are timestamps, latency, ordering, and clock domains handled?
- Can telemetry be captured and replayed deterministically?
- What are the licensing and redistribution constraints?
- How are partial failure, stale data, and degraded service represented?
- Can adapters remain local-first and retrofit-friendly?
- Does the design support Unified-Organ AI, or only a generic SDV service graph?
- Which patterns strengthen Event Protocol without replacing its identity, authority, health, and receipt semantics?

## Rule

Do not replace Velvet Event Protocol, Court, receipts, or the simulated-body path by resemblance alone. Build a comparison matrix, run replay experiments, and adopt only bounded patterns with explicit evidence.
