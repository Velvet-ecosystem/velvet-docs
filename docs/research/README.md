# Velvet Research Translation Records

This directory preserves how outside research, systems, and theories are translated into Velvet architecture without erasing attribution, limitations, or the difference between a source claim and a Velvet decision.

## BabyX Research Trail

Read in this order:

1. [BabyX Architecture Clues for Velvet](babyx_architecture_clues.md)
   - identifies useful mechanisms
   - records Adopt / Adapt / Reject boundaries

2. [BabyX Research Source Map](babyx_source_map.md)
   - separates source claims, limitations, Velvet inferences, and Velvet decisions

3. [BabyX-to-Velvet Implementation Receipts](babyx_implementation_receipts.md)
   - maps the research translation into repositories, pull requests, squash commits, code, tests, CI evidence, and remaining integration work

## Research Rule

A finished Velvet doctrine should not hide where an outside idea came from or how it was transformed.

The preferred trail is:

```text
source
  -> direct claim
  -> limitation
  -> Velvet inference
  -> Adopt / Adapt / Reject
  -> architecture decision
  -> implementation receipt
```

Later archive-dusting work will use this pattern to reconstruct earlier influences where the original trail is incomplete.
