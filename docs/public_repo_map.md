# Public Repository Map

Ghost System v0 is a synthetic, read-only public loop that proves Velvet can observe, validate, interpret, route, receipt, display, and preserve continuity without opening a physical vehicle bus.

```text
velvet-vehicle-can
  -> velvet-event-protocol
  -> velvet-ai-core
  -> velvet-runtime
  -> velvet-receipts
  -> velvet-interface
  -> velvet-continuity-spine
```

| Repository | Ghost System v0 responsibility | Hard boundary |
|---|---|---|
| `velvet-vehicle-can` | produce synthetic vehicle-shaped observations | no transmit or actuation |
| `velvet-event-protocol` | validate `vehicle.can.ghost_observation` | events describe, not authorize |
| `velvet-ai-core` | summarize and create description-only proposals | no executor selection or capability grant |
| `velvet-runtime` | route through Court, safety gates, and a non-physical executor | no `can0` or privileged hardware path |
| `velvet-receipts` | record evidence that the path stayed synthetic and non-actuating | receipt is evidence, not permission |
| `velvet-interface` | render sanitized Ghost CAN state | no command surface or actuator bridge |
| `velvet-continuity-spine` | record a public-safe Ghost Run lineage marker | no private memory or hardware authority |
| `velvet-docs` | maintain the cross-repository map and safety language | documentation does not replace implementation evidence |
| `.github` | organization profile and contributor defaults | no Runtime behavior |

## Repository ownership rules

Event language belongs in Event Protocol. Receipt rules belong in Receipts. Court, routes, gates, and executors belong in Runtime. Vehicle observation belongs in Vehicle CAN. Presentation belongs in Interface. Interpretation belongs in AI Core. Identity and lineage belong in Continuity Spine. Cross-repository doctrine belongs here.

## Public scope

In scope: synthetic fixtures, read-only telemetry, validation, description-only proposals, non-physical Runtime routing, receipts, display-only panels, continuity markers, and an UP Squared dry run with no car wiring.

Out of scope: CAN injection, actuator control, medical takeover logic, hidden owner privilege paths, private handmaiden internals, secrets, keys, tokens, installation wiring, and hardware maps.

## Success test

```text
jarred Tiburon fixture
  -> vehicle.can.ghost_observation
  -> Court-approved read-only route
  -> non-actuating receipt
  -> display-only panel
  -> Ghost Run continuity record
```

If a demo needs real wiring, secrets, or private repositories, it is not Ghost System v0.
