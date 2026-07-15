# Ghost System v0

Ghost System v0 is the first public Velvet loop that behaves like a small sealed vehicle system without touching a real vehicle.

It is a jarred car: synthetic CAN observations, public-safe validation, Core interpretation, Runtime routing, receipts, display, and continuity. It proves the architecture without granting physical authority.

## Canonical loop

```text
synthetic CAN fixture
  -> receive-only observation
  -> vehicle.can.ghost_observation
  -> description-only Core proposal
  -> Runtime Court and safety gate
  -> non-actuating executor result
  -> receipt
  -> display-only Ghost CAN panel
  -> Ghost Run continuity record
```

## Required safety claims

```text
read_only: true
synthetic_fixture: true
physical_bus_opened: false
hardware_bus_opened: false
can_transmission_attempted: false
can_transmission_performed: false
actuation_granted: false
actuation_performed: false
authority_granted: false
```

## What the loop may show

- vehicle speed
- engine RPM
- ignition and door state
- simulated O2 fault
- confidence values
- fixture identity
- receipt identifier
- Ghost Run continuity identifier

These values are demo evidence only. They are not proof of a real vehicle condition.

## What the loop must not do

Ghost System v0 must not open `can0`, require a physical CAN interface, transmit frames, select real hardware targets, expose shell handles, carry authority in event payloads, touch actuators, or imply emergency or medical readiness.

## Repository responsibilities

- `velvet-vehicle-can`: produces synthetic, receive-only vehicle observations.
- `velvet-event-protocol`: defines and validates the canonical event.
- `velvet-ai-core`: summarizes and remembers the observation without selecting an executor.
- `velvet-runtime`: routes the observation through Court, gates, and the non-physical executor path.
- `velvet-receipts`: records evidence that the path stayed synthetic and non-actuating.
- `velvet-interface`: displays sanitized state without exposing controls.
- `velvet-continuity-spine`: records that a sealed Ghost Run became part of the public lineage.

## Official v0 display artwork

The official Velvet v0 Drive scene is the preferred visual foundation for the Ghost Car display. It remains artwork, not a control surface. Live Ghost data should appear as a clearly separate observation overlay marked `GHOST CAR v0`, `SYNTHETIC`, and `READ ONLY`.

The overlay may show speed, RPM, ignition, door state, simulated fault state, receipt status, and continuity status. It must not add actuator controls or imply that the visual concept image itself is a working hardware interface.

## Public safety sentence

> Ghost System v0 is synthetic, read-only, and non-actuating. It proves the public Velvet loop without physical vehicle authority.

## Graduation rule

Ghost System v0 does not become a live vehicle system by changing one flag. Real hardware requires separate private qualification, physical-presence checks, kill-switch behavior, Court policy, safety gates, receipts, and installation-specific evidence.

The jar may rattle. It is not allowed to drive away.
