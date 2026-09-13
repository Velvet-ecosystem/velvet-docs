# Founder Node

The Founder node is Velvet's primary local compute body. It hosts the main Runtime, local API gateway, core interface services, and approved integrations for the installation.

## Responsibilities

- boot identity and continuity checks
- Runtime route provisioning
- Court and safety integration
- approved executor hosting
- primary scene and surface services
- local language and reasoning integration
- local knowledge/catalog presentation
- receipt emission and result publication

## Host profile

The Founder role does not require one universal operating-system image. Each installation resolves an explicit host profile for its surface, hardware, operating system, development posture, and local overrides.

The current UP Squared bench uses the [Ubuntu Vehicle Development Host](profiles/ubuntu_vehicle_development_host.md). The long-term vehicle target remains Automotive Grade Linux.

See [Host Profile Doctrine](host_profiles.md) and the [Deployment Index](README.md).

## Current trusted workspace surfaces

The public Interface now contains trusted full-screen workspace surfaces in addition to the ordinary image-first rooms.

- **Character Foundry** is registered in the Founder launcher and fails closed behind its supplied owner/maintenance access boundary. Its canonical candidate semantics remain in the separate Persona Continuity backend. Permanent Forge-room hotspot placement remains an on-device task.
- **Library Reader** is implemented as a read-only Scroll-backed scene with catalog-aware browsing. Its reusable registration helper is merged, but the final main Founder-launcher registration call and permanent Archive-room hotspot remain follow-on work.

Neither workspace grants Runtime/Court authority or physical execution rights.

See [Library, Vault, and Reader Path](../library_vault_and_reader_path.md).

## Vault binding

The Library Reader helper uses `/srv/velvet` as a service-facing default. That path is not a requirement for the physical mount location of a removable or installation-specific vault.

Deployments may bind the real local vault/catalog explicitly with:

```text
VELVET_LIBRARY_ROOT
VELVET_LIBRARY_CATALOG
```

The deployment must preserve the distinction between:

- physical storage mount;
- service-facing library root;
- canonical catalog location;
- derived search/preview material.

A source preview or extracted text is not a replacement for the canonical source payload.

## Boundary

The language model remains behind Runtime. It does not directly control privileged services or physical hardware.

A host profile makes capabilities available. It does not grant authority to use them.

A library file, search result, Character Foundry candidate, or visible Interface control likewise does not create authority.

## Degraded Operation

When another node, vault, helper, or backend is unavailable, Founder should report explicit degraded state rather than impersonating the missing role, inventing replacement content, or widening permissions.

Detailed installation procedures remain with the repository that owns each service. This page defines the ecosystem role.
