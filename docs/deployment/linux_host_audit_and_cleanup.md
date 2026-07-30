# Linux Host Audit and Cleanup Workflow

This workflow prepares a Linux host for honest Velvet measurements without turning cleanup into an unreviewed package purge.

The first supported use is the Ubuntu 20.04 UP Squared Vehicle Development Host. The method is intentionally reusable for later Home, Forge, Industrial, and other Linux surfaces.

## Safety posture

- audit is read-only by default
- no package is removed automatically
- no service is disabled automatically
- unknown services are preserved
- all proposed changes name the active host profile
- dependency and reverse-dependency information is inspected before package removal
- changes require human confirmation
- rollback instructions are captured before mutation
- changes and benchmark results receive receipts

## Stage 1: identify the host

Capture:

- hardware model
- operating-system release
- kernel
- architecture
- init system
- package managers
- desktop or headless posture
- active Velvet surface profile
- hardware adapters
- local overrides

A cleanup report without a named profile is incomplete.

## Stage 2: capture the untouched baseline

The audit implementation should collect at least:

```text
uname and operating-system release
CPU and memory summary
disk and filesystem use
boot duration and boot blame
enabled, running, and failed services
processes sorted by CPU and memory
network listeners
package inventory
Snap, Flatpak, and container inventory where present
USB, serial, audio, display, and network interfaces
thermal state
recent high-priority journal errors
```

Raw output should be preserved alongside a normalized summary.

## Stage 3: classify services and packages

Every discovered item is classified against the active profile:

- required
- optional
- development-only
- normally-disabled
- forbidden
- unclassified

Classification should include:

- discovered name
- package or owner
- purpose
- activation method
- current state
- dependencies
- reverse dependencies where available
- profile reason
- proposed action
- rollback method

Inactive does not automatically mean removable. Installed does not automatically mean enabled.

## Stage 4: propose a bounded change set

A proposal may include:

- disable a service while retaining its package
- mask a service only when explicitly justified
- remove an unused application package
- remove an unused service package
- stop background refresh for a package system
- reduce log retention
- clear disposable caches
- preserve an item pending investigation

The proposal must explain expected benefit, likely risk, and restoration method.

Prefer the least destructive useful action. Disabling a service is often more reversible than removing a package.

## Stage 5: dry run

Before applying changes, show:

- exact commands
- packages to be removed
- dependency removals
- services to stop or disable
- files or caches to delete
- disk space expected to change
- reboot requirements
- rollback commands

Package-manager dry-run output must be saved rather than summarized away.

## Stage 6: apply in small batches

Changes should be grouped by purpose, for example:

1. disposable cache and old-log cleanup
2. unused consumer applications
3. unused peripheral services
4. discovery or connectivity services not required by the active profile
5. package-system background activity

Reboot and verify between batches when service ownership or boot behavior could be affected.

## Stage 7: health verification

For the Ubuntu Vehicle Development Host, verify at least:

- normal boot
- wired networking
- Git access
- Python imports
- complete `velvet-ai-core` test suite
- Runtime startup
- Interface startup
- audio availability
- USB and serial discovery
- display operation
- no unexplained failed services

A lower idle-memory number does not compensate for a broken body capability.

## Stage 8: compare measurements

Repeat the original baseline commands and compare like with like.

Useful comparisons include:

- boot duration
- idle memory
- idle CPU activity
- process count
- enabled and running service count
- disk use
- network listener count
- temperature
- Native Brain test duration
- Runtime startup duration
- Interface startup duration

Claims should state the host, profile, operating-system version, measurement stage, and environmental conditions.

## Stage 9: receipt and rollback readiness

The final bundle should contain:

- host inventory
- active profile
- before-state
- proposed changes
- dry-run output
- approved changes
- applied commands
- after-state
- health verification
- benchmark comparison
- known limitations
- rollback instructions

## First UP Squared pass

The first pass should remain conservative:

1. capture the untouched Ubuntu baseline
2. clean disposable package caches and old logs
3. inspect printing, discovery, modem, Bluetooth, telemetry, indexing, Snap, and unused consumer applications
4. propose rather than immediately remove uncertain items
5. apply only obvious low-risk changes
6. reboot
7. rerun Velvet tests, Runtime, and Interface
8. preserve the result as the first Vehicle Development Host evidence set

The goal is a quieter proving ground, not a heroic minimization contest.