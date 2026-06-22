# Luckfox Nodes

Velvet may distribute bounded roles across low-power wired nodes.

Typical roles include:

- Librarian and continuity support
- parked security observation
- OEM and body integration support
- auxiliary sensing
- wake and watchdog duties

## Role Isolation

Each node should expose only the services needed for its role. A node does not gain broader authority merely because it is on the trusted local network.

## Identity

Every node requires a stable identity and explicit installation binding before privileged participation.

## Failure Behaviour

A missing or degraded node should produce visible degraded state. Another node must not silently inherit its permissions.

## Communication

Handmaidens and services may exchange structured local messages. Messages describe observations or requests. Runtime remains the authority boundary for meaningful action.
