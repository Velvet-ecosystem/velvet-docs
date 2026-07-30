# Founder Node

The Founder node is Velvet's primary local compute body. It hosts the main Runtime, local API gateway, core interface services, and approved integrations for the installation.

## Responsibilities

- boot identity and continuity checks
- Runtime route provisioning
- Court and safety integration
- approved executor hosting
- primary scene and surface services
- local language and reasoning integration
- receipt emission and result publication

## Host profile

The Founder role does not require one universal operating-system image. Each installation resolves an explicit host profile for its surface, hardware, operating system, development posture, and local overrides.

The current UP Squared bench uses the [Ubuntu Vehicle Development Host](profiles/ubuntu_vehicle_development_host.md). The long-term vehicle target remains Automotive Grade Linux.

See [Host Profile Doctrine](host_profiles.md) and the [Deployment Index](README.md).

## Boundary

The language model remains behind Runtime. It does not directly control privileged services or physical hardware.

A host profile makes capabilities available. It does not grant authority to use them.

## Degraded Operation

When another node is unavailable, Founder should report explicit degraded state rather than impersonating the missing role or widening permissions.

Detailed installation procedures remain with the repository that owns each service. This page defines the ecosystem role.