# Hostile Peripheral Tests

A device on the expected wire is not automatically an honest organ.

Test I2C, SPI, USB, UART, CAN, and GPIO interrupt paths against impossible response lengths, unreleased buses, endless interrupts, valid headers with oversized payloads, compromised trusted peripherals, slow replies, stale data marked fresh, replayed packets with rewritten timestamps, false healthy states, and driver-lockup attempts.

## Acceptance

- unsafe data is rejected before authority evaluation;
- the bus recovers or the device is isolated;
- protected services remain responsive;
- a health event names the bus, device, and failure class;
- a receipt links evidence and recovery outcome;
- suspicious input cannot satisfy Court or safety-gate requirements.

Hardware tests must state voltage, bus speed, driver version, adapter revision, timeout, recovery method, and whether the target was physical or simulated.
