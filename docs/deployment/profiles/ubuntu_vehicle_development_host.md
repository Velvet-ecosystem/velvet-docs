# Ubuntu Vehicle Development Host

Status: **foundation draft**

This profile defines the temporary Linux proving-ground posture for Velvet's UP Squared Founder node while Ubuntu remains in use before the planned Automotive Grade Linux deployment.

It is intentionally a development profile. It keeps the tools needed to inspect, test, and diagnose Velvet while reducing unrelated desktop and consumer background work.

## Identity

- canonical profile: `velvet-host-vehicle-development-ubuntu`
- surface: Vehicle
- current hardware target: UP Squared Founder
- current operating-system family: Ubuntu 20.04
- long-term vehicle target: Automotive Grade Linux
- physical authority: none

Ubuntu is a supported test and fallback host. It is not being promoted as the final vehicle operating system by this profile.

## Inheritance

```text
velvet-host-core
  + velvet-host-vehicle
  + ubuntu-systemd-adapter
  + up-squared-founder-adapter
  + development-overlay
```

The adapter and overlay names are contracts for later implementation. Their executable mappings do not yet live in `velvet-docs`.

## Required capabilities

- service supervision and predictable boot
- local user, group, device, and permission handling
- local storage for repositories, configuration, logs, and receipts
- wired networking for repository updates and local-node testing
- Git and Python runtime support
- desktop and display support required by the current PyQt interface
- audio playback and capture support
- USB device discovery
- serial and UART support
- timekeeping and timestamp support
- thermal and hardware-health visibility
- local logging and failed-service inspection
- SSH when explicitly enabled for bench administration

## Optional capabilities

- GNSS input
- passive CAN interfaces
- camera capture
- Bluetooth for explicit development work
- Wi-Fi for bench convenience
- container tooling
- local model runtime
- compiler and build toolchains
- remote diagnostic access through an approved local transport

Missing optional capability must be reported without widening permissions or invalidating unrelated tests.

## Development-only capabilities

- full desktop conveniences
- interactive package-management tools
- compilers, headers, debuggers, and profilers
- repository development dependencies
- manual test utilities
- temporary screen capture and diagnostic applications

These conveniences must not silently become requirements of a later production AGL image.

## Normally disabled or reviewed

The following are review categories, not automatic removal instructions:

- printing services where no printer workflow is declared
- consumer cloud account integrations
- desktop search and content indexing not used by Velvet
- crash-upload and telemetry services
- modem management where no cellular modem is present
- Bluetooth where no active test requires it
- local network discovery where the vehicle profile has no declared discovery consumer
- unused Snap applications and background refresh activity
- office, game, media-library, and consumer applications unrelated to the bench
- unattended service activation for packages with no named owner

A concrete package or daemon may be changed only after the audit identifies it, its dependencies, its owner, and its rollback path.

## Preserve by default

- systemd and core boot services
- D-Bus, udev, polkit, and local permission infrastructure
- NetworkManager until a replacement network contract exists
- display manager, X or equivalent display stack, and Qt dependencies used by the interface
- audio stack and device rules
- USB, serial, storage, and filesystem support
- Git, Python, and current Velvet dependencies
- thermal monitoring and hardware-health facilities
- SSH configuration when the bench depends on remote administration
- any unknown service until classified

## Measurement stages

Capture the same evidence at each stage:

1. Ubuntu idle before approved cleanup
2. Ubuntu idle after approved cleanup
3. complete `velvet-ai-core` test run
4. Runtime only
5. Runtime plus Interface
6. Runtime plus selected attached test hardware
7. unattended soak run

Minimum measurements:

- boot duration
- idle memory
- idle CPU activity
- process count
- enabled and running services
- failed services
- disk use
- network listeners
- temperature
- test duration
- Runtime and Interface startup duration

## Acceptance posture

The first cleanup pass is accepted only when:

- the host still boots normally
- wired networking works
- Git repository access works
- Python and the Native Brain tests work
- Runtime starts
- the PyQt interface starts
- audio and USB discovery remain available
- no new failed service appears without explanation
- before-and-after evidence is captured
- every applied change has a restoration command or package record

## Explicit non-goals

- no attempt to recreate AGL inside Ubuntu
- no extreme package minimization
- no kernel replacement during the first pass
- no CAN writes
- no relay, GPIO, shell, or physical executor authority
- no automatic purge based only on package name
- no claim that vehicle exclusions apply to Home, Forge, or Industrial surfaces

## Next implementation step

Create a read-only Ubuntu audit tool that emits a host inventory and benchmark bundle. A separate reviewed action plan may then propose service or package changes. Mutation must remain opt-in, dry-run first, and receipt-backed.

> This profile makes Ubuntu quiet enough to measure Velvet, not small enough to become Velvet's final vehicle OS.