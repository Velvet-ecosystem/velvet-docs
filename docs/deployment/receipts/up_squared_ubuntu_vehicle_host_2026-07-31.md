# UP Squared Ubuntu Vehicle Host Receipt

Date: **2026-07-31**

Status: **first evidence-backed host-profile specimen**

This document summarizes the public-safe results of applying the draft Ubuntu Vehicle Development Host profile to the UP Squared Founder node.

The raw receipt archives remain local because they contain detailed process, package, hardware, network, and host inventory. This summary preserves the measured outcome without publishing unnecessary machine-specific detail.

## Host identity

- hardware: UP Squared Founder
- memory visible to Linux: 3.7 GiB
- operating system: Ubuntu 20.04.6 LTS
- surface profile: Vehicle development
- long-term vehicle operating-system target: Automotive Grade Linux
- physical authority during validation: none

## Validation sequence

The host was changed only after read-only inventory and clean-idle receipts were captured.

1. record untouched host inventory
2. record clean idle with the browser closed
3. identify and correct duplicate Velvet Runtime launch paths
4. disable unused printing, modem-management, and automatic crash-submission services
5. prevent GNOME Software and Update Notifier background autostart
6. mask PackageKit while preserving APT and unattended-security timers
7. audit Snap dependencies
8. replace four utility Snaps with native Ubuntu packages
9. remove Snap infrastructure
10. reboot after each material stage and capture proof

Every mutation was isolated, reviewed, and paired with a restoration path or package record.

## Runtime correction

The audit found two launch paths for the same Runtime command:

- an older per-user `velvet-dev.service`
- the canonical machine-level `velvet-runtime.service`

The per-user launcher was disabled. Reboot proof confirmed one Runtime process managed by the machine-level service.

This was a host-cleanliness issue, not a Runtime authority failure.

## Measured result

| Measurement | Before | Final | Difference |
|---|---:|---:|---:|
| Clean-idle used memory | 910 MiB | 608 MiB | 302 MiB lower |
| Clean-idle available memory | 2.4 GiB | 2.7 GiB | about 0.3 GiB higher |
| Total boot duration | 36.221 s | 32.641 s | 3.580 s faster |
| Userspace boot duration | 15.305 s | 11.704 s | 3.601 s faster |
| Root filesystem used | 9.6 GiB | 8.3 GiB | about 1.3 GiB recovered |
| Snap SquashFS mounts | 15 | 0 | all removed |
| Failed systemd units | 0 | 0 | unchanged |

The clean-idle comparison excludes Firefox. Initial inventory captured with the browser open is retained as host evidence but is not used as the memory baseline.

CPU settled at approximately 97 to 99 percent idle during the final sample. Swap remained unused.

## Preserved capabilities

Validation confirmed that the following remained available:

- normal graphical boot
- Firefox through the native Ubuntu package path
- Velvet Runtime through `velvet-runtime.service`
- APT and DPKG
- `apt-daily` and `apt-daily-upgrade` timers
- native GNOME Calculator, Characters, Logs, and System Monitor
- networking, display, audio, Bluetooth, storage, thermal management, and device infrastructure

No CAN writers, relays, GPIO executors, or other physical-authority paths were introduced.

## Removed or suppressed background work

The evidence-backed Vehicle development posture now excludes:

- CUPS printing and printer discovery
- ModemManager where no cellular modem is declared
- Whoopsie and Kerneloops submission services
- Apport automatic-report path and forwarding socket
- GNOME Software background autostart
- Update Notifier background autostart and user paths
- PackageKit D-Bus activation
- Snap applications, support runtimes, loop mounts, and daemon infrastructure

These are profile-specific decisions. Home, Forge, Industrial, and other surfaces must not inherit them without their own declared capability requirements and receipts.

## Remaining boot observations

The final `systemd-analyze blame` sample listed these longest units:

- `plymouth-quit-wait.service`: 8.604 s
- `NetworkManager-wait-online.service`: 6.848 s
- `gdm.service`: 1.645 s

Blame durations may overlap and do not prove that disabling a unit will reduce total boot by the same amount.

`NetworkManager-wait-online` remains preserved because the current Runtime unit participates in the network-online boot relationship. Any change requires a separate Runtime startup and degraded-network contract, followed by its own receipt-backed test.

Plymouth and the graphical display path also remain preserved until their relationship to the current interface startup is evaluated.

## Acceptance result

The first host-profile cleanup is accepted as a **bench validation result** because:

- the host boots normally
- Velvet Runtime starts once
- physical authority remains disabled
- APT security timers remain present
- native desktop utilities and Firefox remain available
- no failed systemd units were introduced
- disk, boot, memory, and CPU evidence was captured
- each material stage survived reboot

This receipt validates the profile method on one machine. It does not claim that the same package or service choices are correct for every Ubuntu installation, every UP Squared configuration, or another Velvet surface.

> The profile did not make Ubuntu into AGL. It made Ubuntu quiet enough to hear Velvet clearly.