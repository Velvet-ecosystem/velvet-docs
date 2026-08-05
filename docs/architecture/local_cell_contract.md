# Complete Local Cell Contract

Each major Velvet node behaves as a complete local cell rather than a helpless remote terminal.

A cell declares minimum local storage, cached configuration, local health logic, bounded autonomy, reconnect and reconciliation behavior, receipt buffering, safe offline mode, authority ceiling, and degraded operation.

## Laws

- Queen and the internet are both optional dependencies at runtime.
- Disconnection never widens authority.
- Local work continues only inside the declared ceiling.
- Receipts buffer locally with ordering and integrity evidence.
- Reconnection reconciles state explicitly; it does not overwrite newer truth silently.
- Conflicts, stale configuration, exhausted storage, and receipt gaps are reported as degraded health.
- A cell must explain what it can preserve alone, what it refuses, and what requires Queen or physical presence.

The local-cell contract extends distributed load sharing. It does not create independent identities or an agent swarm; each cell remains an organ of one accountable body.
