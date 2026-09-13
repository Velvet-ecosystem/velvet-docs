# Luckfox Nodes

Velvet may distribute bounded roles across low-power wired nodes.

Typical roles include:

- Librarian and continuity support
- parked security observation
- OEM and body integration support
- auxiliary sensing
- wake and watchdog duties

## First-Wake Doctrine

A box-fresh subordinate node should be treated as an unknown shipped-state device until its baseline is captured.

The intended first-wake order is:

1. power and inspect one node at a time;
2. prefer wired Ethernet/SSH for ordinary bring-up;
3. capture the untouched factory baseline before configuration or reflashing;
4. keep the node role-neutral during bootstrap;
5. make only the minimum reviewed filesystem/hostname/operator-access changes;
6. reboot and verify the neutral state;
7. stop before Runtime installation, role assignment, or authority changes.

The neutral boundary is explicit:

```text
role=unassigned
runtime_installed=false
physical_authority=none
```

Factory capture should happen before package upgrades, firmware replacement, password-hardening changes, firewall changes, or role-specific configuration unless recovery from a broken shipped state makes that impossible.

## Current implementation status

A conservative Luckfox Lyra first-boot bootstrap exists as **Runtime PR #144 under review**. It includes a read-only host preflight plus separate audit/apply modes, but it is not merged into Runtime main as of this documentation sync.

Therefore this documentation does not claim that the bootstrap has been accepted as the current production deployment path, and it does not claim that apply mode has been proven on a target Lyra.

Current validation reported by that candidate is limited to shell syntax checks and successful audit-mode execution in a Linux test environment.

## Role Isolation

Each node should expose only the services needed for its role. A node does not gain broader authority merely because it is on the trusted local network.

Role assignment happens after neutral first-wake, not during factory capture.

## Identity

Every node requires a stable identity and explicit installation binding before privileged participation.

A hostname, Ethernet address, factory credential, or physical connection is not sufficient identity proof by itself.

## Failure Behaviour

A missing or degraded node should produce visible degraded state. Another node must not silently inherit its permissions.

Founder may continue in a reduced mode without pretending that a missing Librarian, security node, or OEM/runtime node is still present.

## Communication

Handmaidens and services may exchange structured local messages. Messages describe observations or requests. Runtime remains the authority boundary for meaningful action.

Network reachability does not create trust, role membership, or physical authority.
