# Surface Host Profile Seeds

Status: **foundation placeholders**

These seeds prevent the first Ubuntu Vehicle cleanup from becoming an accidental universal Linux policy. They name likely capability families for other Velvet bodies without claiming production readiness or prescribing exact daemons.

Each profile must later receive its own threat model, hardware adapters, distribution mappings, measurements, and acceptance tests.

## Home Host

Canonical name: `velvet-host-home`

Likely required capability families:

- reliable local networking
- local discovery where explicitly used
- message-bus or broker integration
- room and environmental sensor intake
- camera or intercom services where installed
- local media and voice support
- home-protocol bridges such as Matter, Thread, Zigbee, Z-Wave, or vendor-specific adapters where approved
- persistent local state and receipts
- graceful operation during internet loss

Likely optional capabilities:

- network storage
- containers
- local model runtime
- multi-room audio
- energy monitoring
- backup power telemetry

A Home profile must not inherit Vehicle assumptions that disable discovery, building-protocol bridges, or always-on room services.

## Forge Host

Canonical name: `velvet-host-forge`

Likely required capability families:

- USB and serial device access
- development and diagnostic tooling
- camera observation
- durable local project storage
- machine status intake
- safe job-state logging
- local networking
- explicit operator-presence handling

Likely optional capabilities:

- CNC adapters
- 3D printer services
- laser or cutting-machine adapters
- network storage
- CAD and slicing tools
- containers or isolated build environments
- inventory and parts tracking

A Forge profile may legitimately retain compilers, debuggers, printer services, device discovery, and larger toolchains that are unnecessary on a quiet vehicle host.

Machine availability never grants job-start authority. Tool execution remains behind Runtime, Court, safety, resource, and executor boundaries.

## Industrial Host

Canonical name: `velvet-host-industrial`

Likely required capability families:

- deterministic service supervision
- durable logging and receipt storage
- watchdog and health reporting
- strict network segmentation
- time synchronization appropriate to the installation
- industrial protocol adapters where approved
- local operation during upstream network loss
- explicit degraded-state reporting
- controlled update and rollback procedures

Likely optional capabilities:

- Modbus adapters
- OPC UA adapters
- MQTT brokers or bridges
- historian integration
- redundant storage
- redundant networking
- hardware security modules
- headless operation

An Industrial profile must not inherit desktop requirements merely because the UP Squared development host uses a graphical interface.

## Shared rule

These surfaces share doctrine, event, identity, Runtime, Court, receipt, and continuity boundaries. They do not share an identical package list.

```text
shared Velvet laws
      ↓
profile-specific capabilities
      ↓
distribution and hardware adapters
      ↓
named local installation
```

A surface profile describes the body it supports. It does not redefine Velvet's authority model.