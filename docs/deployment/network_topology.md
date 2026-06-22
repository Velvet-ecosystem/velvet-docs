# Network Topology

Velvet's core nodes use a local wired network as the default trust fabric.

```text
Founder node
  -> local Ethernet switch
      -> Librarian / security node
      -> Runtime / OEM node
      -> approved maintenance client
```

## Principles

- wired links are preferred for core nodes
- node identity must be explicit
- network reachability does not equal authority
- services expose narrow local APIs rather than broad shell access
- Tailscale or another overlay is transport only
- remote presence never equals local physical presence

## Failure Isolation

A node should fail without silently transferring its authority to another node.

Observation, continuity, Runtime, and hardware execution roles should remain distinguishable so degraded operation can be explicit and safe.

## Segmentation

Vehicle CAN, Velvet internal networking, maintenance access, and optional internet access should remain separate trust zones.

A network path may carry a request. Runtime still decides whether the request is authorized.
