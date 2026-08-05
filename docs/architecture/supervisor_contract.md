# Supervisor Contract for Linux Nodes

Every major Linux node must name a smaller supervisor or reflex service that can detect failures the supervised operating system may be unable to report about itself.

## Responsibilities

- observe boot and shutdown progress
- monitor voltage, temperature, and heartbeat evidence
- request bounded watchdog recovery
- preserve a declared safe state
- count recovery attempts and enforce cooldown
- buffer local fault receipts
- preserve minimum services
- escalate to Queen and isolate an unhealthy node when recovery is exhausted

## Required fields

- supervised node
- supervisor node
- permitted recovery requests
- required health evidence
- maximum recovery attempts
- cooldown period
- minimum services that survive
- escalation condition
- isolation condition
- receipt type
- manual-override requirement

## Laws

The supervisor may preserve or reduce the node's safety posture, never widen it. Recovery attempts are bounded, receipt-backed, and separated by cooldown. A frozen node cannot certify its own return to physical authority. Loss of the supervisor is itself a degraded health state.

Class 0 and Class 1 services receive protection before comfort, indexing, experiments, or entertainment. When safe recovery cannot be proven, the supervisor isolates the node and reports the failure rather than repeating recovery forever.
