# Decoded CAN Observation Path

Velvet keeps raw CAN evidence, decoded interpretation, event transport, and display as separate layers.

```text
vehicle CAN bus
  -> kernel listen-only CAN interface
  -> receive-only observer
  -> raw bounded frames
  -> approved local vehicle profile
  -> conservative signal decoder
  -> Runtime can-signals executor
  -> decoded observation event
  -> display-only interface widget
```

## 1. Raw Evidence

`velvet-vehicle-can` receives frames through a listen-only configuration.

Raw observation remains available separately through Runtime's `can-observe` route.

This path answers:

> What frames were actually seen?

It must not be replaced by decoded summaries, because interpretation can be incomplete or wrong while the raw evidence remains useful.

## 2. Vehicle Profile

A local vehicle profile maps known frame locations to named signals.

The profile is installation-specific evidence. It is not permission to transmit or control the vehicle.

A missing or invalid profile causes decoded observation to fail closed.

## 3. Conservative Decoder

The decoder converts selected bytes into bounded scalar observations using profile definitions such as:

- CAN identifier
- byte offset and length
- endianness
- signedness
- scale and offset
- confidence

Decoded outputs retain source frame identity, timestamp, raw value, interpreted value, and confidence.

## 4. Runtime Observation Route

`velvet-runtime` exposes decoded values through the separate `can-signals` route.

The route:

- gathers bounded receive-only frames
- loads the approved local profile
- filters by minimum confidence
- limits the number of published signals
- overrides all safety declarations at the Runtime boundary
- produces receipts through the normal Runtime pipeline

It always publishes:

```text
mode: read-only
status: observation-only
actuation_granted: false
actuation_performed: false
```

## 5. Event Contract

`velvet-event-protocol` carries individual decoded values as `DECODED_CAN_SIGNAL_OBSERVED` events.

The event includes:

- signal name
- scalar value
- confidence
- observation timestamp
- source profile
- optional unit

It forbids fields representing authority or execution, including executor names, routes, capabilities, tokens, hardware targets, commands, shell operations, and actuation claims.

## 6. Interface Contract

`velvet-interface` receives sanitized observations through `ObservationWidget`.

The widget does not decode CAN or load profiles. It only displays bounded observations and derives presentation state:

- `validated` for higher-confidence values
- `provisional` for lower-confidence values
- `fresh`, `stale`, or `unknown` freshness

These labels are visual guidance only. They never grant authority.

## Hard Boundary

A displayed vehicle signal cannot become a control command by changing fields inside the observation.

If an observation motivates action, Velvet must start a new strict intent:

```text
observation
  -> reasoning proposes intent
  -> Court authorizes
  -> safety gate evaluates
  -> approved executor acts
  -> receipts record
```

## Owning Repositories

- `velvet-vehicle-can`: receive-only observation, profiles, decoding
- `velvet-runtime`: receipted raw and decoded observation routes
- `velvet-event-protocol`: decoded observation transport contract
- `velvet-interface`: display-only observation model and widget contract
