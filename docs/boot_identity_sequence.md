# Boot Identity Sequence

Privileged Velvet services should not wake into authority before identity and continuity are verified.

```text
boot
  -> load installation identity
  -> verify genesis and successor lineage
  -> verify body and surface bindings
  -> verify trusted configuration and signatures
  -> construct capability context
  -> provision Runtime routes and gates
  -> expose local clients
```

## Fail-Closed Rules

Boot must stop or remain observation-only when:

- continuity verification fails
- identity records conflict
- the active body binding is unknown
- trusted signatures are missing or invalid
- required safety configuration is unavailable

Velvet must not silently create a fresh identity while inheriting old authority.

## Successor Lineage

Intentional identity evolution belongs in an explicit successor event. The origin remains preserved rather than overwritten.

## Body Binding

An installation may inhabit several surfaces, but privileged body bindings must be explicit. A newly detected device is not automatically trusted hardware.

## Runtime Provisioning

Only after identity and continuity pass should Runtime construct routes, capability context, safety gates, and approved executors.

Observation-only services may start earlier when their isolation is proven and they cannot gain actuation authority.
