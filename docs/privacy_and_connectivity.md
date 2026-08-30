# Privacy and Connectivity

Velvet is designed to communicate through many possible carriers without becoming an always-on tracking system.

## Core distinction

**Connectivity is a capability, not consent.**

A cellular modem, Internet connection, paired phone, Home node, V2V link, LoRa radio, Meshtastic mesh, LoRaWAN gateway, or future carrier being available does not by itself authorize Velvet to upload owner information.

Velvet should remain useful while local, offline, selectively connected, or fully disconnected. Core local operation must not depend on continuous remote telemetry.

## Private by default

During ordinary operation, owner, occupant, location, route, medical, conversation, cabin, and behavioral information should remain local unless an enabled capability has a specific approved reason to transmit a bounded payload.

Velvet does not require the following as a default operating posture:

- continuous cloud presence;
- periodic owner or vehicle location upload;
- background route-history export;
- always-on cabin or occupancy telemetry;
- routine medical-state upload;
- hidden cloud reporting merely because a network path exists;
- silent secondary use for advertising, profiling, or unrelated model training.

Owners may deliberately opt into remote capabilities. Those choices should be understandable, scoped, inspectable, and revocable rather than hidden behind one blanket connected-services assumption.

## Emergency disclosure

A real life-safety incident may justify disclosure that would be inappropriate during ordinary use. That is an **incident-scoped exception**, not a permanent privacy mode change.

The system should disclose progressively:

1. the minimum facts needed to summon and route help;
2. additional incident facts only when a legitimate responder or configured emergency destination needs them;
3. richer sensitive information over protected/authenticated paths when available;
4. intentionally minimized public-safe information only when an open emergency fallback is required.

Future paths such as Owner Emergency Bridge may use the owner's paired phone to carry an emergency call or responder conversation. Beacon of Hope may use an open constrained radio path when stronger routes fail. Neither capability turns ordinary Velvet operation into ambient tracking.

Stand-down should end emergency-only disclosure behavior. A past emergency must not silently create indefinite post-incident telemetry, permanent relay trust, or continuing responder access.

## Carrier neutrality includes privacy

Velvet Communications follows the rule:

> **The message belongs to Velvet. The carrier is replaceable.**

The privacy consequence is equally important: the carrier transports the approved message; it does not become entitled to the rest of Velvet's state.

Changing from local IP to cellular, an owner's phone, Home, another Velvet, LoRa, Meshtastic, LoRaWAN, or a future carrier must not silently broaden payload scope, recipient scope, retention, identity exposure, location exposure, authority, or secondary use.

## Truthfulness

Velvet should distinguish between information that was:

- kept local;
- prepared for disclosure;
- sent;
- heard by a relay;
- accepted for relay;
- acknowledged by an upstream destination;
- unconfirmed.

An available network path is not proof that data was transmitted. A send attempt is not proof that anyone received it.

## Public promise

Velvet's communications posture should be understandable without fine print:

> **Velvet is not always connected. Velvet is always prepared to communicate when policy and circumstance justify it.**

And the privacy promise underneath it is:

> **More ways to reach help do not mean more ways to track the owner.**
