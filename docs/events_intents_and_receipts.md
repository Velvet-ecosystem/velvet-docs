# Events, Intents, and Receipts

Velvet separates what is noticed, what is interpreted, what is proposed, what is permitted, what is executed, and what is remembered.

```text
observation = what was noticed
cognitive event = a bounded interpretation of what appears to be unfolding
intent = what is proposed
authorization = what Court permits
execution = what an approved executor did
receipt = evidence of the decision or result
episode = a navigational memory object linked to evidence
```

## Observations

Observations describe state. They may carry confidence, freshness, provenance, and read-only safety claims.

They do not grant authority.

## Cognitive Events

A cognitive event temporarily associates observations, predictions, organ contributions, proposals, decisions, execution lifecycle records, and outcomes into a bounded representation of an unfolding situation.

A cognitive event is interpretation over evidence. It may be incomplete, contradicted, interrupted, stale, or wrong.

It must retain source references and must never replace the observations or receipts from which it was formed.

The Cognitive Event Layer may:

- describe what appears to be happening now
- propose event boundaries
- form explicit predictions
- track an authorized action and its expected consequence
- identify interruption candidates
- offer an evidence-linked episode proposal

It may not:

- authorize an intent
- mint a capability
- select or invoke an executor
- retry a physical action
- manufacture a receipt
- turn confidence, urgency, memory, or organ consensus into permission

See [Cognitive Event Layer](cognitive_event_layer.md).

## Intents

An intent is a structured proposal. It should contain a public route and bounded parameters, not raw executor names, hardware handles, shell commands, or capabilities.

Cognitive context may accompany an intent by reference, but the intent remains independently validated. Court must not trust a cognitive summary more than its source evidence.

## Authorization

Court evaluates identity, context, policy, capability, and requested scope.

Authorization belongs to Runtime, not the event bus, cognitive layer, memory system, interface, or language model.

## Execution

Only an approved executor may touch the owned subsystem, and only after the matching safety gate passes.

The Cognitive Event Layer may enter action-tracking posture only after independent authorization and execution-lifecycle evidence exists.

## Receipts

Receipts preserve evidence of decisions, denials, execution, and outcomes.

A receipt is not permission. Replaying a receipt must never produce a new physical action.

A cognitive episode may reference receipts. It cannot replace, rewrite, or strengthen them.

## Episodes

An episode is a compact memory-navigation object produced after an event closes. It may summarize actors, changes, proposals, decisions, executions, outcomes, prediction errors, interruptions, and source references.

Episodes help Velvet find and understand past situations. They are not execution evidence and do not prove identity.

## Canonical Flow

```text
observation or request event
  -> bounded cognitive event association where useful
  -> strict intent
  -> Court authorization
  -> signed capability token
  -> matching safety gate
  -> approved executor
  -> execution receipt
  -> result observation
  -> prediction comparison
  -> evidence-linked episode proposal
```

Every arrow preserves the distinction between interpretation, authority, execution, evidence, and memory.
