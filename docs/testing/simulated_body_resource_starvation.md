# Simulated Body Resource Starvation

The simulated body must reproduce contention and noisy-but-valid behavior, not only malformed sensor values.

Fake adapters shall support valid packets at unsafe frequency, delayed acknowledgements, queues that never drain, bounded memory-pressure signals, reconnect loops, online/degraded flapping, partially unavailable handmaidens, and locks held beyond their permitted duration.

Each scenario declares resource budget, protected service classes, expected throttle or isolation behavior, health event, receipt type, recovery trigger, and maximum recovery time. Simulation and hardware paths use the same Event Protocol, health, and receipt contracts.

A successful test proves Class 0 and Class 1 service continuity, truthful degradation, bounded data loss, and no authority widening during fallback.
