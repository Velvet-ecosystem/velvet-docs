# Velvet briefing integration map

Date: 2026-08-29
Source: daily build briefings after Update Pack 2
Status: planning contracts, not live authority code

## Intent

This document maps the newer briefing-derived ideas to the Velvet repositories that should own them. The goal is to turn useful research signals into reviewable contracts before implementation. No item here grants physical authority by itself. Authority remains owned by Court and runtime gates.

## Integration rule

A contract may describe what Velvet should eventually do, but implementation must still pass repo-specific review, tests, receipts, and promotion gates. Physical control remains disabled unless explicitly implemented behind the proper Court and adapter boundaries.

## Repo ownership map

| Area | Primary repo | Supporting repos | Notes |
|---|---|---|---|
| Time Integrity and Holdover | velvet-event-protocol | velvet-runtime, velvet-receipts | Defines clock truth, drift, timestamp confidence, and holdover decay. |
| Asynchronous Sensor Truth | velvet-event-protocol | velvet-ai-core, velvet-vehicle-can, velvet-receipts | Preserve native sensor timing before fusion creates derived observations. |
| Telemetry Reconciliation | velvet-event-protocol | velvet-receipts, velvet-runtime | Compare measurements that should agree and emit contradiction evidence. |
| Event Evidence | velvet-receipts | velvet-event-protocol, velvet-runtime | Triggered evidence capture around anomalies, not endless recording. |
| Dispatch-Time Authority | velvet-runtime | velvet-event-protocol, velvet-receipts | Recheck authority immediately before physical adapter dispatch. |
| Retry Budget | velvet-runtime | velvet-event-protocol | Prevent reconnect storms and synchronized panic across handmaidens. |
| Execution Placement | velvet-ai-core | velvet-runtime, velvet-receipts | Separate who decides from where compute actually runs. |
| Inference Cost Receipt | velvet-receipts | velvet-ai-core, velvet-runtime | Record compute, latency, heat, memory, energy, fallback, and model/provider used. |
| Deterministic Vehicle Gateway | velvet-vehicle-can | velvet-runtime, velvet-event-protocol | Normalize noisy physical vehicle buses before Queen sees them. |
| Network Evolution Matrix | velvet-vehicle-can | velvet-docs | Compare CAN, CAN-FD, CAN XL, 100BASE-T1, 10BASE-T1S, ordinary LAN, LoRa, Wi-Fi, and legacy wiring. |
| Sensor Trust Aging | velvet-event-protocol | velvet-ai-core, velvet-receipts | Online status is not the same thing as deserved belief. |
| Belief State | velvet-ai-core | velvet-event-protocol | Preserve uncertainty until corroboration is strong enough to commit. |
| Observation Latency | velvet-ai-core | velvet-event-protocol, velvet-runtime | Measure when a perception becomes actionable, not only FPS. |
| Mixed-Criticality Resource Control | velvet-runtime | velvet-event-protocol | Admit work only if compute, power, thermals, network, and storage can afford it. |
| Health Trend | velvet-event-protocol | velvet-receipts, velvet-docs | Track whether organs are improving, stable, or worsening. |
| Topology and Trust Drift | velvet-vehicle-can | velvet-event-protocol | Expected neighbors, missing nodes, unexpected nodes, and drifting measurement bias. |
| Node Commissioning | velvet-receipts | Modules, velvet-runtime | Birth certificate for physical organs. |
| Failure Domain | velvet-runtime | velvet-docs, velvet-vehicle-can | Redundancy must record shared fuses, regulators, clocks, switches, storage, cooling, and configuration. |
| Reflex Compute | velvet-ai-core | velvet-runtime, velvet-vehicle-can | Deterministic perception lane before high-level reasoning. |
| Activation Ladder | velvet-ai-core | velvet-event-protocol | Passive sensor to low-power trigger to reflex to normal perception to high-level reasoning. |
| Power-Loss Transaction | velvet-runtime | velvet-receipts | Flush state, mark unfinished work, and shut down cleanly when supply collapses. |
| Power Supervisor | velvet-runtime | velvet-vehicle-can | Rails, wake sources, brownout, watchdogs, CAN wake, recovery attempts. |
| Power Path Measurement | velvet-runtime | velvet-docs | Measure source, protection, conversion, branch current, transients, module voltage, and heat. |
| Physical Capability Descriptor | velvet-runtime | velvet-event-protocol | What an organ can measure, change, tolerate, and refuse. Discoverability never grants authority. |
| Sensor Escalation | velvet-event-protocol | velvet-ai-core | Sentinel, normal, diagnostic sensing modes. |
| Distributed Measurement Cluster | velvet-event-protocol | velvet-vehicle-can, velvet-ai-core | Local monitor produces validated summaries with raw-on-demand evidence. |
| Protected Reserve / Borrowable Resource | velvet-runtime | velvet-ai-core | Idle protected reserve is not automatically free. |
| Credential Destination Policy | velvet-receipts | velvet-runtime | A secret declares who can use it and where it may go. |
| Camera Quality Health | velvet-event-protocol | velvet-ai-core, velvet-interface | A live camera can still be a poor witness. |
| Useful Work per Watt/GB | velvet-ai-core | velvet-docs | Evaluate validated workload per watt and memory footprint. |
| Compute Reassignment | velvet-docs | velvet-runtime | Demote old hardware into specialist, supervisor, logger, replay, bench, or retired roles. |
| Component / Storage Substitution | velvet-docs | velvet-runtime | Track substitutes and boot/storage recovery paths before supply tightens. |
| Node Provisioning Fixture | Modules | velvet-receipts, velvet-runtime | Provision identity, firmware, keys, electrical sanity, and receipts before body installation. |
| Promotion Evidence | Modules | velvet-receipts, velvet-docs | A module needs evidence, not only a passing test. |

## Recommended implementation order

1. Event truth layer: Time Integrity, Holdover, Asynchronous Sensor Truth, Sensor Trust Aging, Telemetry Reconciliation.
2. Runtime safety layer: Dispatch-Time Authority, Retry Budget, Mixed-Criticality Resource Control, Power-Loss Transaction.
3. Vehicle boundary layer: Deterministic Vehicle Gateway, Network Evolution Matrix, Topology Integrity.
4. Local AI layer: Belief State, Execution Placement, Inference Cost, Reflex Compute, Activation Ladder.
5. Evidence layer: Event Evidence, Node Commissioning, Credential Destination, Health Trend, Failure Domain.
6. Hardware discipline layer: Power Path Measurement, Compute Reassignment, Useful Work per Watt/GB, Provisioning Fixture.

## Public/private rule

Public repos may describe general architecture, contracts, and safe simulation behavior. Private repos may keep sensitive module details, medical integration specifics, actual hardware identity, unreleased wiring maps, security-sensitive provisioning material, and any owner-specific operational details.

## Non-goals for this pass

- No actuator enablement.
- No production physical-control code.
- No vendor lock-in.
- No replacement of Event Protocol, Court, Riven, or receipts without review.
- No automatic discovery of hardware as trusted authority.
