# Low-Power Status Surfaces

A removable local status surface can preserve useful evidence after a crash or power loss.

Candidate traits include e-paper or another persistent display, low power draw, local-only operation, removable or magnetic mounting, microSD or local cache, and a visible last-updated timestamp.

Useful fields include node health, current faults, harness identification, bench-test steps, last receipt ID, recovery code, power state, module lifecycle state, offline maintenance note, and last known safe status.

The surface is a witness, not a controller. Displayed information may be stale and must say so. It cannot authorize recovery, unlock physical targets, expose secrets, or imply that the node remains healthy merely because the last message survived.
