# Distributed Body Ghost Run

This integration proof exercises Velvet's public distributed-body contracts together without granting physical authority.

## Proven path

```text
synthetic coolant observation
  -> Native Brain integrated heartbeat
  -> proposal-only work intent
  -> Runtime verified node registry
  -> specialist-first placement and workload lease
  -> Event Protocol advertisement, offer, acceptance, and completion
  -> canonical Receipts evidence
  -> important result returned to the Queen
  -> Runtime lease closed
```

The run checks out and imports the actual public repositories:

- `velvet-ai-core`
- `velvet-runtime`
- `velvet-event-protocol`
- `velvet-receipts`

It does not copy their contracts into a private integration model.

## Scenario

Ruby's specialist Linux node advertises `thermal-pattern-analysis` and `local-pattern-detection`. The Queen also advertises the required capability as a fallback.

Native Brain observes a synthetic coolant trend and produces a bounded `PROPOSE_WORK` intent. Runtime receives a separate `WorkRequirement`, verifies the body-bound advertisements, and selects Ruby's specialist node rather than defaulting to the Queen.

The specialist performs deterministic arithmetic over three synthetic samples. The result is marked important and routed back to the Queen with the corresponding receipt identifiers.

## Authority boundary

The proof intentionally stops before real execution authority.

```text
Native Brain intent: proposal only
Runtime lease: placement only
Event Protocol: transport only
Receipts: evidence only
Ghost specialist: synthetic computation only
Queen result: awareness only
physical authority: none
```

The harness asserts:

```text
canonical: false
execution_authorized: false
actuation_authorized: false
authority: none
```

A Runtime placement lease does not authorize the work. This Ghost proof uses a deterministic synthetic function rather than an approved physical executor.

## Lifecycle

The expected event and receipt sequence is:

```text
NODE_ADVERTISEMENT_PUBLISHED  # Ruby
NODE_ADVERTISEMENT_PUBLISHED  # Queen fallback
WORK_OFFERED
WORK_ACCEPTED
WORK_COMPLETED
```

Every event is validated by `velvet-event-protocol`. Every event becomes a distributed-work receipt through the canonical Runtime receipt gateway.

## Running locally

Check out the four public dependency repositories and place their roots on `PYTHONPATH`, then run:

```bash
python -m unittest tests/test_distributed_body_ghost_run.py -v
python ghost/distributed_body_run.py
```

GitHub Actions performs those checkouts automatically in `Distributed Ghost Integration`.

## What this proves

This is the first executable ecosystem-wide proof of the rule:

> Native Brain describes the work. Runtime chooses and leases the organ. Event Protocol carries the lifecycle. Receipts preserve the evidence. Important results return to the Queen. Authority remains separate.

It also proves that the Queen does not absorb narrow work merely because she is capable of doing it.

## What this does not prove

The run does not include:

- Court authorization
- signed capability tokens
- an approved hardware executor
- network discovery
- CAN transmission
- relay or actuator access
- canonical memory writes
- permanent Riven lineage changes

Those boundaries are deliberate. Ordinary workload placement and completion are operational evidence, not body ancestry.
