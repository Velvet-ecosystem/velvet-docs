# Power-Envelope Acceptance Tests

Every node and module declares expected current bands for boot peak, idle, normal activity, degraded mode, recovery, sleep, shutdown leakage, and unexpected wake events.

Acceptance records supply voltage, regulator, measurement method, sample rate, ambient temperature, attached peripherals, software revision, and test receipt.

Failure evidence includes current above or below the expected band, repeated spikes, failure to enter sleep, a stuck peripheral, a runaway loop, regulator distress, a shorted accessory, or a silent module still drawing active current.

Power evidence is health evidence, not authority. A current reading may trigger degradation or isolation policy, but it cannot directly grant or widen physical control.
