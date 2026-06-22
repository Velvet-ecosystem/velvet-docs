# Local API and Security Architecture

Velvet is local-API-first, not internet-first.

API means a narrow local contract between trusted clients and Runtime. It does not mean cloud control.

```text
CLI / voice / UI / mobile / sensors / handmaidens
                    |
              local API gateway
                    |
       identity -> intent -> Court
                    |
              safety gate
                    |
          approved executor
                    |
                 receipt
```

## Core Boundary

The offline language model sits behind the local API as a language and reasoning engine. It may propose intent. It may not directly control:

- shell
- files
- relays
- CAN writers
- actuators
- privileged updates
- vehicle controls

## Narrow Choke Points

Security is concentrated at a few hard boundaries:

- identity and context verification
- strict intent validation
- Court policy and authority
- signed capability tokens
- matching safety gates
- approved executors
- replay protection
- receipts

## Remote Access

Tailscale or another transport may carry requests securely, but transport is not authority.

Remote clients may observe or request. They must never equal verified local physical presence.

## Physical Ceremony

Deep authority requires an installation-defined local ceremony, potentially combining presence, NFC, touch, local voice, and protected sequence knowledge.

## Enforcement Laws

```text
no valid receipt = deny actuation
no verified physical presence = deny deep privilege elevation
no trusted signature = reject update
```
