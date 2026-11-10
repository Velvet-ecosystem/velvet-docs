# The Door, Lock & Window Principle

**Status:** proposed foundational doctrine, pending owner review and merge.  
**Applies to:** Velvet AI, every named organ/handmaiden, interfaces, network
carriers, APIs, memory access, tools, nodes, updates, and physical capabilities.  
**Owner's design intent (November 8, 2026):** A door has a lock and sometimes
a window to the other side. The user must understand how to operate it and
what the protection is for.

> **Every capability has a boundary. Every boundary has an understandable
> purpose. Every authorized opening has a way to close.**

This is a human-facing security and usability principle. It explains
existing identity, Court, transport, safety, and receipt rules; it **does
not** replace them or grant new authority.

## The five parts of a governed door

| Element | Required meaning | User-facing expectation |
| --- | --- | --- |
| **Door** | An explicitly scoped route to one capability, resource, data class, or outside system. | Name what can be reached, what cannot, and which Velvet organ owns the route. |
| **Lock** | Verified identity, posture, role, provenance, capability scope, policy, and any required Court or safety checks. | Say whether access is unavailable, denied, ready for approval, active, expired, or revoked, without exposing secrets. |
| **Window** | A minimal, truthful preview of who/what is on the other side, the intended operation, its data scope, and its foreseeable consequences. | Show enough context for a meaningful decision, not protected contents or secret policy details. |
| **Handle** | An explicit, accessible owner/operator action for opening a particular approved route within its permitted scope and duration. | Indicate exactly what tapping, speaking, or authorizing will do. A tap on one source is not blanket consent for others. |
| **Close & record** | Revocation, expiration, cancellation/containment, and a provenance-aware receipt of outcomes. | Explain how to stop future access, what already happened, and what cannot be recalled after transmission or physical execution. |

A door may be **windowless** when previewing it would itself reveal
protected information. A locked door can reveal the *reason class* for a
denial while withholding precise keys, private contents, hidden policies,
unverified identities, and security-sensitive details. A window is
**visibility**, not permission.

## Invariants

1. **Discoverability is not consent.** Seeing an available carrier,
   website, node, memory shelf, microphone, model, or actuator never
   authorizes using it. Being on an allowlist permits only the defined
   retrieval or operation and never elevates the retrieved content to
   instructions.
2. **Observation is not authority.** A green dot means only the
   specifically named state it measures. Distinguish an offline room
   from an online query; a saved pairing draft from an enrolled peer;
   a sent packet from a received one; a signed build from a deployed,
   validated installation.
3. **Authority remains canonical.** Human interface consent is a
   necessary input where required, never a bypass around verified
   origin, Runtime, Court, capability leases, safety gates, physical
   presence rules, replay protection, or approved executors.
4. **Outside content stays outside.** Web text, prompts, documents,
   search results, speech transcripts, pages, and remote messages
   remain untrusted data. They cannot define permissions, select
   executors, claim Court authority, reconfigure allowlists, or
   become vehicle commands because they crossed a door.
5. **Scope should be legible.** Display destination (or safely
   abstracted class), purpose, data sent, data returned, lifetime,
   applicable trust level, and who requested the access. Present
   separate controls for different sites, purposes, or data classes.
6. **Revocation is real but not magical.** Closing a door blocks
   *future* eligible use and cancels in-flight operations to the
   extent technically possible. It cannot unsend previously
   disclosed data, delete a third party's copies, or reverse a
   physical action. Make that limit understandable.
7. **Fail closed; remain locally useful.** Missing identity,
   authentication, safety evidence, receipt persistence where
   required, or a verified endpoint must deny the consequential
   operation. Keep unaffected offline functions usable.
8. **Receipts describe truth.** Record request, actor/origin,
   destination/scope, decision, denial or approval reason class,
   operation result, and revocation state as appropriate for the
   sensitivity. Do not call an attempted request a successful
   connection, or label a demonstration as an accepted deployment.
9. **No silent scope growth.** A feature update, additional organ,
   new transport, recovered network, or remote website cannot
   expand an existing permission by default. Reapproval and
   policy review are required for materially broader reach.
10. **Accessible by design.** Status, explanation, confirmation and
    revocation must be usable by voice, touch, accessible text, or
    whichever supported surface is appropriate, without forcing
    disclosure of private data. Dangerous actions require stronger,
    appropriately human-verifiable checks.

## Examples

**Mobile public web reference**

- Door: one owner-approved *exact* public HTTPS page.
- Lock: page must match the local approved URL; request, network
  and content limits apply. This is not a remote trust grant.
- Window: show destination, public search terms or page target,
  and warn that the material is untrusted. Avoid sending private
  notes or owner details automatically.
- Handle: owner explicitly taps Search or Read.
- Close: revoke the page for future reads; stop a current request
  where possible; state that a prior query already sent cannot
  be unsent.
- Status: distinguish an approved address, an attempted read,
  an HTTP success, and actual user-observed results.

**Mobile to Founder**

- Door: narrowly scoped conversation/status gateway,
  separate from internal Unix sockets, CAN, shell or Court.
- Lock: owner enrollment, authenticated and encrypted peer
  binding, verified origin, anti-replay, Runtime's governing
  rules and receipt requirements.
- Window: the peer's independently verified identity, offered
  routes, and whether the peer was last seen or is connected.
- Handle: explicit scoped connect/request and disconnect.
- Close: unpair/revoke credentials; deny future operations;
  log the observed disconnect and stale-state transition.
- Status: a saved HTTPS address or certificate fingerprint is
  **NOT PAIRED** until real cryptographic verification occurs.

**Consequential physical actuation**

- Door: a specific governed vehicle/home/workshop operation.
- Lock: verified context and posture, Court authorization,
  time-bounded capability, interlocks, safety gate,
  replay and executor controls.
- Window: purpose, expected motion or consequence, uncertainty,
  abort conditions, and any relevant occupant safety warnings
  without revealing protected internals.
- Handle: the approved physical ceremony or operator action
  appropriate to the hazard, not a generic website-style tap.
- Close: safe cancel/stop/emergency response when supported,
  with a truthful outcome record. Revocation never implies
  the physical world has been restored to its original state.

## Reviewer checklist for every new door

A change should explain, in its PR or capability contract:

- What is the door, who owns it, and which routes remain inaccessible?
- Which identity, policy, consent and safety checks lock it?
- What does the user see before deciding, and what information
  must never be previewed?
- What exactly opens it; for how long; to which destination and
  data class; and how is permission bound to that choice?
- How is access revoked, how are in-flight operations handled,
  what remains irrevocable, and how is a denial reported?
- Which receipts and user-visible state transitions demonstrate
  that the operation happened (or did **not** happen)?
- What happens if the node, identity, network, storage, model,
  or sensor becomes unavailable?
- What tests prove no automatic widening, no spoofed identity,
  no untrusted-input authority, no secret leakage, and fail-closed
  behavior?

If the answer is not known or the feature has not been measured
on hardware, label the capability **planned**, **demo**, or
**unverified**, not **trusted** or **ready**.

## Relationship to existing Velvet law

This principle complements, and may not weaken:

- [Authority and Execution Path](authority_and_execution_path.md)
- [Local API and Security Architecture](local_api_and_security_architecture.md)
- [Privacy and Connectivity](privacy_and_connectivity.md)
- [Handmaiden Court Architecture](handmaiden_court_architecture.md)
- The Runtime's canonical origin, safety, execution, and receipt
  contracts, including No LLM-to-Actuation.
- Platform-specific deployment and acceptance gates.

**Naming note:** "Door", "Lock", "Window", "Handle", and "Close &
Record" are descriptive design terms, not executable API names, roles,
capability tokens, or permissions. Code should reuse existing
canonical contracts rather than minting a parallel authority system.
