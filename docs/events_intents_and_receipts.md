# Events, Intents, and Receipts

Velvet separates what is noticed, what is proposed, what is permitted, what is executed, and what is remembered.

```text
observation = what was noticed
intent = what is proposed
authorization = what Court permits
execution = what an approved executor did
receipt = evidence of the decision or result
```

## Observations

Observations describe state. They may carry confidence, freshness, provenance, and read-only safety claims.

They do not grant authority.

## Intents

An intent is a structured proposal. It should contain a public route and bounded parameters, not raw executor names, hardware handles, shell commands, or capabilities.

## Authorization

Court evaluates identity, context, policy, capability, and requested scope.

Authorization belongs to Runtime, not the event bus.

## Execution

Only an approved executor may touch the owned subsystem, and only after the matching safety gate passes.

## Receipts

Receipts preserve evidence of decisions, denials, execution, and outcomes.

A receipt is not permission. Replaying a receipt must never produce a new physical action.

## Canonical Flow

```text
observation or request event
  -> strict intent
  -> Court authorization
  -> signed capability token
  -> matching safety gate
  -> approved executor
  -> execution receipt
  -> result event
```
