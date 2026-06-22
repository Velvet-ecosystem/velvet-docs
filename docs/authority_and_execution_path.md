# Authority and Execution Path

Velvet separates reasoning, authority, safety, execution, and memory into distinct layers.

```text
brain proposes
  -> Court authorizes
  -> safety gates approve conditions
  -> approved executors act
  -> receipts remember
```

## Why the Split Exists

A language model is useful for interpretation, conversation, planning, and intent formation. It is not a safe hardware authority.

The offline LLM therefore sits behind the local API and may not directly control:

- shell commands
- files
- relays
- CAN writers
- actuators
- vehicle controls
- privileged updates

## Required Path

Every meaningful action follows:

```text
input
  -> verified identity and context
  -> strict intent schema
  -> policy and authority check
  -> signed capability token
  -> matching safety gate
  -> approved executor
  -> receipts
```

## Choke-Point Rules

Velvet prefers a few narrow enforcement points over scattered informal checks.

Core rules:

```text
no valid receipt = deny actuation
no verified physical presence = deny deep privilege elevation
no trusted signature = reject update
```

## Remote Access Boundary

Remote clients may:

- observe
- request
- receive results

Remote access must not be treated as equivalent to verified local physical presence.

Deep authority requires an in-body physical ceremony defined by the installation, such as a combination of presence, touch, NFC, local voice, and protected sequence knowledge.

## Events and Receipts

Events are information. Receipts are evidence.

Neither one grants authority by itself.

A result event may report that an approved executor acted. A receipt may prove that a decision or action was recorded. Any new physical action still requires a fresh trip through the authority path.
