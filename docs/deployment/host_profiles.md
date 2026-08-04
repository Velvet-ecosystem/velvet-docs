# Velvet Host Profile Doctrine

Velvet may inhabit vehicles, homes, workshops, industrial spaces, development benches, and other local bodies. Those surfaces do not require identical operating-system services.

A **host profile** is the explicit contract between one Velvet surface and the Linux or AGL host supporting it. It states what capabilities the surface requires, what is optional, what should normally remain absent, and how the host is measured.

A host profile is not a universal package-removal list.

> The host should carry what its body needs, not every daemon its distribution happened to install.

## Why profiles exist

A quiet host gives more honest measurements, fewer background failures, a smaller attack surface, and clearer degraded-state reporting. It also prevents one surface's assumptions from being imposed on another.

Examples:

- a vehicle host may need display, audio, GNSS, serial, CAN, watchdog, and power-state support
- a home host may need local discovery, message brokers, camera services, Matter or Thread bridges, and media services
- a forge host may need USB and serial tooling, CNC or printer services, cameras, network storage, and development tools
- an industrial host may need durable logging, watchdogs, Modbus or OPC UA adapters, stricter network policy, and no desktop at all

Removing a service because one profile does not need it must never become a claim that the service is unnecessary everywhere.

## Core laws

1. **Capability before daemon name.** Profiles describe required capabilities first. Distribution adapters map those capabilities to concrete packages and services.
2. **No universal purge.** A cleanup candidate is valid only within a named profile and inspected host.
3. **Audit before change.** Read-only inventory and baseline measurement happen before any package removal or service disablement.
4. **Dry run before mutation.** Proposed changes must be shown before they are applied.
5. **Rollback must exist.** Every applied change records what changed and how to restore it.
6. **Unknown means preserve.** If ownership or purpose is unclear, the service remains until classified.
7. **Local override is explicit.** Site-specific needs may extend a profile without silently weakening its security or authority boundaries.
8. **Missing optional capability degrades locally.** It does not invalidate the shared core.
9. **Host capability does not grant Velvet authority.** A running daemon, attached device, package, socket, user group, or kernel module is availability only.
10. **Measurements are named evidence.** Compatibility and efficiency claims require captured before-and-after results.

## Profile layers

A deployment resolves its host posture from ordered layers:

```text
velvet-host-core
  + surface profile
  + hardware adapter
  + optional development overlay
  + explicit local override
```

Later layers may add requirements or narrow optional behavior. They may not erase core security, receipt, identity, Court, or authority requirements.

### Core layer

The core layer defines services common to any supported host, such as:

- boot and service supervision
- local identity and permissions support
- device discovery through the operating system
- reliable timekeeping appropriate to the installation
- local logging and health reporting
- networking only where the installation requires it
- Python or packaged runtime support where applicable
- storage required for configuration and receipts

The core layer does not require a desktop, cloud account, package format, network manager, or exact init implementation unless a specific platform adapter does.

### Surface layer

The surface layer declares capabilities belonging to Vehicle, Home, Forge, Industrial, Mobile Companion, Development, or another named body.

### Hardware adapter

The hardware adapter maps a profile onto concrete hardware, for example UP Squared Founder, Luckfox node, x86 industrial PC, ARM home hub, or a future AGL target.

### Development overlay

Development tools, desktop conveniences, compilers, debuggers, and interactive diagnostics belong in an explicit overlay. They are not silently treated as production requirements.

### Local override

A local override records installation-specific additions such as a particular camera stack, network storage service, building protocol bridge, or accessibility service. It must be inspectable and receipt-backed where changes are applied.

## Capability classes

Every profile classifies host capabilities as one of:

- **required**: the profile cannot meet its declared role without it
- **optional**: supported when present, with explicit degraded behavior when absent
- **development-only**: useful for build, diagnosis, or bench work but not required in production
- **normally-disabled**: not expected for the profile and suitable for review
- **forbidden**: conflicts with the profile's security or deployment posture
- **unclassified**: preserved until ownership and purpose are understood

A capability class is not automatically a package action. Concrete daemon or package changes require a distribution adapter and host audit.

## Host lifecycle

```text
inventory
  -> classify
  -> capture baseline
  -> propose changes
  -> dry run
  -> human approval
  -> apply bounded changes
  -> reboot or restart where required
  -> verify health
  -> capture after-state
  -> compare and receipt
```

The default tool mode must be read-only audit.

## Baseline evidence

A host profile should define measurements appropriate to its body. Common evidence includes:

- operating-system and kernel identity
- enabled and running services
- failed services
- package and container inventory
- boot duration
- idle CPU activity
- idle memory use
- disk use
- process count
- network listeners
- device interfaces
- thermal state
- Velvet test and startup duration

Measurements should be captured at named stages, for example:

1. distribution idle before cleanup
2. distribution idle after approved cleanup
3. Native Brain tests
4. Runtime only
5. Runtime plus Interface
6. Runtime plus attached surface hardware

## Distribution adapters

The canonical profile remains distribution-neutral. A distribution adapter may map capabilities to:

- systemd units
- OpenRC services
- Debian or Ubuntu packages
- RPM packages
- Snap or Flatpak applications
- containers
- AGL services and recipes
- kernel modules and device rules

An adapter must state its supported operating-system family and version range. It must not infer that a package is safe to remove merely because a daemon is currently inactive.

## Repository ownership

`velvet-docs` owns the ecosystem doctrine, profile contract, canonical profile names, and cross-surface boundaries.

Executable audit and cleanup tooling should live with the installer, Runtime deployment tooling, or another explicitly named implementation owner. Hardware-specific mappings remain with their owning repository or adapter.

## Authority boundary

Host profiles govern availability, resource posture, and deployment evidence. They do not grant model, organ, Runtime route, module, scene, user, or device authority.

A host may expose CAN, GPIO, shell, serial, camera, network, or building-control capability while Velvet's public physical authority remains none.

> A capable host is not an authorized act.