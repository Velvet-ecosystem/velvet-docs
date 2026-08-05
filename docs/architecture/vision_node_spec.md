# Future Vision Node Specification

A serious vision node separates camera transport from interpretation and reports its own limits.

## Required boundaries

- camera deserialization
- synchronized timestamping and clock quality
- video inference
- CAN and vehicle-context input
- sensor fusion
- health and error counters
- optional raw recording
- compressed event output
- privacy policy
- degraded-camera handling
- thermal and power reporting

## Rules

Queen receives fused observations by default. Raw video is requested explicitly for a bounded purpose. Every camera reports timestamp quality, frame drops, transport errors, and current health. Frame loss becomes a health event. Loss of one camera degrades locally rather than collapsing the whole vision stack. Privacy filtering occurs before storage or export when the use case permits it.

Vision observations are evidence. They do not identify a person, declare a seat empty, or grant physical authority alone.
