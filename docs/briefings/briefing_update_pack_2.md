# Velvet Briefing-Derived Update Pack 2

Status: accepted architecture and implementation planning

This pack moves Velvet from modules that merely operate toward organs that can prove why they belong in the body. Every node, sensor, model, dependency, workflow, and interface must expose truthful capability, bounded authority, failure evidence, degraded behavior, and receipts.

## Governing pattern

A Velvet organ must:

1. declare what it can do;
2. identify who currently owns the capability and who may call it;
3. prove lifecycle, health, failure, degraded-mode, and receipt coverage before promotion;
4. survive partial disconnection without silently widening authority;
5. refuse unsafe or unavailable work with a stable reason;
6. preserve evidence when resources, power, buses, peripherals, or dependencies misbehave.

Availability is not authority. A healthy-looking peripheral is not automatically truthful. A green test is evidence, not the whole safety case.

## Documents in this pack

### Promotion and authority

- [Promotion Evidence Bundle](../testing/promotion_evidence_bundle.md)
- [Runtime Capability Registry](../architecture/runtime_capability_registry.md)
- [Capability Refusal Reasons](../architecture/capability_refusal_reasons.md)
- [Minimum Service Classes](../architecture/minimum_service_classes.md)

### Presence, cognition, and memory

- [Presence Fusion Contract](../architecture/presence_fusion_contract.md)
- [Model Capability Adapter](../architecture/model_capability_adapter.md)
- [Dream State Memory Schedule](../architecture/dream_state_memory_schedule.md)
- [Vision Node Specification](../architecture/vision_node_spec.md)

### Node autonomy and hardware truth

- [Supervisor Contract](../architecture/supervisor_contract.md)
- [Complete Local Cell Contract](../architecture/local_cell_contract.md)
- [Operational Data Ownership](../architecture/operational_data_ownership.md)
- [Component Substitute Tracking](../hardware/component_substitute_tracking.md)
- [Camera Interface Requirements](../hardware/camera_interface_requirements.md)
- [Remote Sensor Pod Topology](../roadmap/remote_sensor_pod_topology.md)
- [Low-Power Status Surfaces](../roadmap/low_power_status_surfaces.md)

### Adversarial and acceptance testing

- [Hostile Peripheral Tests](../testing/hostile_peripheral_tests.md)
- [Power-Envelope Acceptance](../testing/power_envelope_acceptance.md)
- [Resource-Abuse Test Pack](../testing/resource_abuse_test_pack.md)
- [Simulated Body Resource Starvation](../testing/simulated_body_resource_starvation.md)
- [Data Replay Requirement](../testing/data_replay_requirement.md)

### Security, dependencies, and process

- [Dependabot Malware Policy](../security/dependabot_malware_policy.md)
- [Vulnerability Reporting](../security/vulnerability_reporting.md)
- [Internal Action Pinning Policy](../devops/internal_action_pinning_policy.md)
- [Dependabot Branch Naming](../devops/dependabot_branch_naming.md)
- [AGL Vehicle Data Loop Watch](../research/agl_vehicle_data_loop_watch.md)

## Implementation priority

1. Promotion Evidence Bundle
2. Runtime Capability Registry
3. Presence Fusion Contract
4. Supervisor Contract
5. Hostile Peripheral Testing
6. Power-Envelope Acceptance Tests
7. Resource-Abuse Test Pack
8. Complete Local Cell Contract
9. Operational Data Ownership
10. Model Capability Adapter
11. Vulnerability Reporting
12. Remote Sensor Pod and Camera Requirements
13. Dream State Memory Schedule
14. Component Substitute Tracking
15. Dependabot malware and branch-naming policies

## Boundary

These documents define contracts, evidence, and refusal posture. They do not grant physical authority, bypass Court, promote a module, enable cloud access, or make simulated targets equivalent to physical targets.
