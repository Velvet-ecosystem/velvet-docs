# Authority and Execution Path

Velvet separates reasoning, requester evidence, authority, safety, execution, and memory into distinct layers.

```text
brain / organ / human proposes
  -> Runtime verifies context
  -> Court authorizes
  -> safety gates approve conditions
  -> approved executors act
  -> measured outcomes return
  -> receipts remember
```

Urgency may change scheduling. It does not collapse these stages.

## Why the Split Exists

A language model is useful for interpretation, conversation, planning, and intent formation. It is not a safe hardware authority.

The offline LLM therefore sits behind the local API and may not directly control:

- shell commands;
- arbitrary files;
- relays;
- CAN writers;
- actuators;
- vehicle controls;
- privileged updates.

The same rule applies to Language, Audio, Interface, Communications, Library retrieval, memories, events, and named organs. Useful context is not authority.

## Ordinary Required Path

Every consequential action follows a bounded path equivalent to:

```text
input / proposal
  -> verified identity, body, profile, session, and surface context
  -> strict intent schema
  -> canonical Court authority + policy check
  -> bounded capability token
  -> execution contract
  -> resource coordination
  -> matching safety gate
  -> replay protection
  -> approved executor
  -> measured outcome
  -> receipts
```

No presentation, transport, speech, memory, or reasoning layer may skip to the executor.

## Request Origin Is Evidence, Not Authority

Velvet records where a request came from, including local surfaces, remote clients, peer bodies, communications transports, and emergency responder conversation.

Origin may matter to policy, but it does not itself create permission.

Examples:

- a Tailscale peer is reachable, not automatically trusted;
- a LoRa/Meshtastic participant is heard, not automatically a Velvet peer;
- a phone carrier can carry a request without becoming the owner;
- a responder can ask Velvet to act without inheriting owner authority;
- a connected call does not prove a responder heard or accepted the result.

## Local Events vs Cross-Body Carriage

Inside one governed body, Event Protocol carries structured local events. Between nodes/bodies/deployments, Communications carries bounded cross-body payloads.

```text
local service
  -> Event Protocol
  -> Runtime / Core / Language / Interface / Audio

approved cross-body payload
  -> Communications
  -> carrier
  -> receiving body's governed ingress
```

Neither event delivery nor communications delivery grants authority by itself.

## Emergency-First Scheduling

When an emergency, accident, or trusted manual emergency protocol start is active and verified, life-safety work may receive priority ahead of ordinary work.

```text
verified active incident
  -> life-safety priority rank 0
  -> preempt ordinary work
  -> expedited incident policy evaluation
```

Rank 0 means **consider this first**. It does not mean **approve this automatically**.

Emergency priority shortens the software path to a decision. It does not bypass:

- incident identity binding;
- requester/proposal provenance;
- Court;
- capability scope;
- safety/interlocks;
- approved executor selection;
- replay protections;
- required receipt persistence;
- measured execution feedback.

An unverified or mismatched emergency claim receives no life-safety priority.

## Responder Emergency Action Path

Responder conversation uses a deliberately different intake from an ordinary owner/local-session request.

```text
responder asks
  -> proposal-only responder intake
  -> authority = none
  -> verified active emergency / rank 0
  -> incident-action policy
  -> canonical capability + logical target resolver
  -> incident-scoped emergency Court binding
  -> strict Court Intent
  -> Court authorization
  -> future safety / executor / physical target binding
  -> future measured execution
```

The active owner session is not inherited by the responder request.

### Incident-scoped Court identity

The emergency binder creates a temporary incident identity with canonical `emergency` Court authority only after the incident and upstream policy/resolver gates are satisfied.

The responder remains provenance, not authority. Court authority comes from the verified incident posture and explicit emergency policy, not from the responder's voice, caller ID, carrier, or the owner's prior session.

### Least privilege inside emergency mode

The current public Runtime separates bounded emergency policy families, including logical visibility and rescue-access requests.

Motion, steering, braking, throttle, shifting, propulsion, and engine-control requests are not eligible through responder conversation. They remain part of separate driving/emergency-maneuver safety architecture.

### Court authorization is not execution

A successful Court decision may produce a short-lived bounded capability token. That token is permission to approach the executor boundary.

It is **not**:

- proof a door unlocked;
- proof hazards illuminated;
- an executor selection;
- a CAN/GPIO/relay command;
- measured physical feedback.

The current public emergency path stops before real vehicle-specific emergency executors.

## Communications and Emergency Disclosure

Communications provides carriage, not authority.

> **Connectivity is a capability, not consent.**

A healthy cell, IP, Home, phone, LoRa, Meshtastic, or other carrier does not authorize background tracking or unrestricted disclosure.

Emergency disclosure is incident-scoped and progressive. Beacon of Hope can provide a bounded last-resort off-grid fallback, but transmission/hearing/relay truth must remain distinct from upstream emergency-service acknowledgement.

The future Owner Emergency Bridge may use a paired owner phone as a carrier. The phone does not become Velvet's authority.

## Speech Boundary

Language may interpret or express a request; Audio may capture or speak it. Neither layer grants authority.

For emergency responder conversation, deterministic language can preserve known/inferred/stale/unavailable truth while protected values remain withheld from the expression object when policy says not to disclose them.

Speech may report a decision or measured result. It must not claim an action occurred merely because Court authorized it or a carrier attempted delivery.

## Knowledge and Memory Boundary

Library retrieval and memory may inform reasoning, but neither is authority.

- retrieval is not belief;
- memory is not identity proof;
- a historical receipt is not permission for a new action;
- a previous emergency does not create standing future emergency authority.

A new consequential action still begins at the current authority boundary.

## Choke-Point Rules

Velvet prefers a few narrow enforcement points over scattered informal checks.

Core rules include:

```text
no valid required receipt = deny consequential actuation
no trusted signature = reject update
no verified context = deny privilege that requires it
Court authorization != measured execution
request origin != requester authority
connectivity != consent
```

## Remote Access Boundary

Remote clients may:

- observe bounded approved state;
- request actions;
- receive results.

Remote access must not be treated as equivalent to verified local physical presence when a policy requires that evidence.

Emergency policy may deliberately use a separate verified incident authority class, but that still does not turn a remote requester into the owner or remove safety/Court gates.

## Events and Receipts

Events are information. Receipts are evidence.

Neither one grants authority by itself.

A result event may report that an approved executor acted. A receipt may prove that a decision or action was recorded. Any new physical action still requires a fresh trip through the authority path.

## Public Boundary

The public ecosystem currently demonstrates bounded logical Court authorization, including incident-scoped emergency authorization, but does not claim production physical vehicle control.

Physical deployment requires vehicle-specific executor binding, hardware qualification, safety validation, replay/token consumption at the executor boundary, measured feedback, and evidence that the actual hardware did what the system reports.
