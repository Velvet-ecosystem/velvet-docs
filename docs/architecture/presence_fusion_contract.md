# Presence Fusion Contract

Presence is a fused estimate, not one sensor's declaration.

## Sources

NFC, capacitive touch, voice phrase, seat radar, seat pressure, camera/person sense, microphone localization, future UWB, an optional local companion, ignition and door state, and manual override may contribute evidence.

Each observation records source, spatial source, zone, timestamp, freshness, confidence, range confidence, living-motion evidence, optional identity claim, owner-match confidence, failure mode, spoofing risk, and the purposes for which the source is permitted.

## Rules

- No single sensor unlocks the vehicle by itself.
- No single sensor declares a seat empty by itself.
- Stale evidence cannot authorize action.
- Access, safety, personalization, and medical escalation use separate thresholds and source requirements.
- Identity evidence and spatial-presence evidence remain distinct.
- A source may contribute to one purpose while being forbidden for another.
- Contradictory observations lower confidence and emit a health event when persistent.
- Manual override is explicit, bounded, and receipt-backed.

## Outputs

The fusion layer returns a purpose-specific confidence, contributing sources, rejected observations and reasons, freshness boundary, contradiction count, and whether the minimum source diversity was met. Court remains responsible for authorization.
