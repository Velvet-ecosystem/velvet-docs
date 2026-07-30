# UP Squared Ghost Run

This guide defines the first public-safe dry run for the UP Squared Founder node. The goal is not to control a car. The goal is to prove Ghost System v0 on the hardware that will eventually host the main Runtime.

## Safety boundary

Do not connect vehicle CAN, relays, actuator drivers, lighting, locks, HVAC, pedals, steering, throttle, clutch, or shifter hardware. Do not add production signing keys or capability tokens. Treat the UP Squared as a bench computer carrying a jarred vehicle fixture.

## Host preparation

The current bench host follows the [Ubuntu Vehicle Development Host](profiles/ubuntu_vehicle_development_host.md).

Before performance measurements, capture the untouched host baseline and follow the [Linux Host Audit and Cleanup Workflow](linux_host_audit_and_cleanup.md). Cleanup must remain profile-scoped, dry-run first, reversible, and separate from the Ghost safety proof.

## Public repository order

```text
velvet-docs
velvet-event-protocol
velvet-receipts
velvet-vehicle-can
velvet-ai-core
velvet-runtime
velvet-interface
velvet-continuity-spine
```

## Repository smoke paths

```bash
# velvet-vehicle-can
python -m velvet_vehicle_can.ghost_can_demo --pretty

# velvet-event-protocol
python examples/ghost_can_observation.py

# velvet-ai-core
python examples/ghost_can_core_proposal.py

# velvet-runtime
python3 velvet_cli.py can-ghost --max-frames 4

# velvet-receipts
python examples/ghost_can_receipt.py

# velvet-interface
python examples/ghost_can_panel.py

# velvet-continuity-spine
python examples/record_ghost_run.py
```

Each repository README remains the source of truth for current installation and test commands.

## Successful first run

A successful run proves that a synthetic observation is accepted, summarized, routed through Court and a read-only gate, receipted, displayed, and recorded in continuity, while no physical bus is opened and no actuation occurs.

Failures should remain boring and local: a missing fixture, rejected unsafe payload, unavailable route, refused receipt, or blocked display. The run must never require root, attempt CAN transmission, touch hardware, or accept an authority claim.

## Visual result

The official Velvet v0 Drive artwork may be used as the background for the display proof. The Ghost CAN panel remains a separate overlay labeled `GHOST CAR v0`, `SYNTHETIC`, and `READ ONLY`. The image is a visual foundation, not evidence of a functioning control surface.

The ghost proves shape. It does not prove road readiness.