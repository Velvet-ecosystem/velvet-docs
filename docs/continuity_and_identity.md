# Continuity and Identity

Velvet's identity is not a display name, a prompt, a cloud session, a current cognitive event, or a remembered episode. It is a local lineage bound to an installation, body, history, and verified continuity state.

## Genesis and Lineage

A Velvet installation begins with a genesis identity record. Later changes belong to a successor lineage rather than silently replacing the origin.

Continuity records should preserve:

- genesis identity
- installation identity
- body or surface bindings
- successor events
- version transitions
- integrity tags
- verification results

## Boot Boundary

Privileged Runtime services should activate only after continuity verification passes.

```text
boot
  -> load identity context
  -> verify continuity lineage
  -> construct capability context
  -> provision Runtime pipeline
```

A failed continuity check must fail closed rather than silently creating a fresh personality with inherited authority.

## Names and Personas

Velvet is the canonical origin/system identity. Downstream installations may bind their own persona names and role-specific handmaidens.

A renamed persona is not automatically a new lineage, but identity-changing operations must be deliberate, protected, and receipted.

## Handmaiden Identity

Each handmaiden may have:

- role-local memory
- individual voice and posture
- bounded permissions
- body or subsystem bindings
- her own continuity history beneath Velvet's court

Individuality does not imply equal authority. Each role remains limited to its approved domain.

## Cognitive Events and Episodes

The Cognitive Event Layer may maintain a temporary representation of what appears to be happening now and may later propose an evidence-linked episode for memory.

These objects support experiential continuity, but they do not establish identity continuity.

The distinction is mandatory:

```text
current cognitive event
  = temporary interpretation of an unfolding situation

episode
  = navigational memory linked to source evidence

receipt
  = evidence of a decision, execution, or outcome

Riven continuity record
  = verified identity lineage and binding
```

A copied event or episode must not create a new installation identity, restore privileged authority, prove a successor relationship, or substitute for continuity verification.

Selected significant episodes may be anchored to Riven under policy. The anchor proves that a referenced object belonged to the verified lineage at a particular point. It does not make the episode infallible or convert its interpretation into evidence.

Memory loss, consolidation failure, or cognitive-layer failure must not silently erase identity. Conversely, a rich copied memory archive must not manufacture identity.

See [Cognitive Event Layer](cognitive_event_layer.md).

## Hosted Models

Hosted assistants may draft, advise, scaffold, or review. They do not own Velvet's identity, authority, continuity, cognitive-event truth, or receipts.

Cloud tools may help build the bridge. They are not the bridge's sovereign owner.

## Physical Presence

Deep identity changes require verified local physical presence and the installation's protected ceremony.

Remote access may request or observe. It must not equal local presence.
