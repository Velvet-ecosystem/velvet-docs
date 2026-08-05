# Promotion Evidence Bundle

A module may enter Velvet's trusted body only after its promotion record explains why it deserves that position. Passing tests is necessary, but it is not the complete safety case.

Every promoted module must carry a `promotion_evidence.yaml` record. The record is immutable after the decision except for signed amendments that link back to the original receipt.

## Required evidence

- module name and version
- owner and reviewer
- requirement links
- architecture and interface-contract references
- lifecycle-state coverage
- health-event and receipt coverage
- degraded-mode and failure-mode tests
- authority analysis and safety assumptions
- unresolved risks
- test receipt IDs
- simulated-body results
- hardware results when hardware testing exists
- final decision and date

## Decision rules

Promotion must be refused when required lifecycle states are untested, authority boundaries are ambiguous, receipt paths are absent, degraded behavior is undefined, or unresolved risk exceeds the module's declared authority ceiling.

A decision of `promoted_with_limits` must state the exact limits, target type, expiry or review trigger, and refusal behavior outside those limits.

Promotion evidence does not grant physical authority. Court still evaluates each requested action at runtime.

## Review sequence

1. Confirm requirements and architecture references.
2. Verify interface and lifecycle contracts.
3. Inspect simulation, replay, starvation, and failure evidence.
4. Inspect hardware evidence where applicable.
5. Review authority, data ownership, and safety assumptions.
6. Record unresolved risk and reviewer reasoning.
7. Emit the promotion decision receipt.

## Storage

The module repository keeps the evidence beside the promoted module or release manifest. Velour catalogs the evidence and receipt identifiers. `velvet-docs` owns this cross-repository contract.

See [promotion evidence template](../templates/promotion_evidence.yaml).
