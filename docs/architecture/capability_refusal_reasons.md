# Capability Refusal Reasons

Velvet records stable, safe explanations when a capability cannot proceed.

Canonical codes:

- `capability_unavailable`
- `capability_degraded`
- `authority_missing`
- `owner_presence_required`
- `simulated_target_only`
- `physical_target_locked`
- `safety_gate_active`
- `stale_sensor_data`
- `dependency_unhealthy`
- `court_denied`
- `vehicle_state_disallows`
- `maintenance_mode_required`
- `receipt_backend_unavailable`
- `manual_override_required`

A refusal contains the code, capability, target type, requesting caller, timestamp, safe public explanation, internal evidence reference, and receipt policy. Public explanations must not leak secrets or security-sensitive thresholds.

Refusal codes are machine-stable. Human wording may improve without changing the code. Unknown refusal states fail closed and are reported as a contract error.
