# Data Replay Requirement for Hardware Adapters

Every adapter declares support for raw capture, normalized capture, replay into Event Protocol, replay into Native Brain, timestamp-preserving playback, speed-adjusted playback, fault injection, privacy filtering, and receipt linking.

At minimum, a promoted adapter should provide normalized capture and deterministic replay unless the hardware or privacy model makes that impossible. Exceptions require reviewer reasoning and an alternate diagnostic path.

Replay packets retain original observation time and add replay time, replay session ID, source receipt, speed factor, and physical-or-simulated target. Replayed data is always marked simulated and cannot unlock physical authority.

Replay lets Velvet debug vehicle, truck, home, forge, and bench behavior without demanding live hardware for every investigation.
