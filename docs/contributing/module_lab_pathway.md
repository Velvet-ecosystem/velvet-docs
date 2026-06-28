# Module Lab Contribution Pathway

The Velvet ecosystem welcomes outside ideas, research, adapters, experiments, fixes, and reusable module proposals.

New reusable modules and substantial module rewrites do not move directly into active ecosystem paths. They begin with a public request, then enter the private Velvet Module Lab only after initial review.

## Pathway

1. **Public request** — submit the Module Lab request form in `velvet-docs`.
2. **Initial review** — maintainers check scope, safety, fit, and whether private follow-up is needed.
3. **Private intake** — accepted requests receive a formal intake record inside the private Module Lab.
4. **Qualification** — the candidate is assessed for provenance, boundaries, deterministic behavior, compatibility, failure handling, and tests.
5. **Promotion decision** — the candidate is promoted, held for more work, retained as reference material, or declined with a recorded reason.

A public request is not approval. Acceptance into the lab means the contribution may be assessed and tested. It does not make the code production-ready, officially promoted, or authorized for active control.

## What belongs on the public request

Provide enough information for initial triage:

- candidate name
- short purpose
- contribution type
- intended Velvet surfaces
- expected inputs and outputs
- hardware, platform, or external dependencies
- requested permissions or authority
- current implementation and test status
- public repository, demonstration, or documentation links when available
- whether private follow-up is required

## Do not submit publicly

Do not place any of the following in a public request:

- passwords, tokens, credentials, or private keys
- personal or medical records
- proprietary source code you do not have permission to share
- private repository contents
- security-sensitive deployment details
- personal addresses, phone numbers, or other private identifying information

State that private follow-up is required instead.

## What the Module Lab checks

The private qualification process may include:

- source and authorship tracking
- single-responsibility and ownership review
- input, output, and configuration contracts
- authority and hardware-boundary review
- deterministic fixtures
- accepted, rejected, and failure-path tests
- compatibility with supported Python and runtime versions
- receipt expectations
- compatible Velvet surfaces
- promotion review and destination records

## Review outcomes

A candidate may be classified as:

- reference
- donor
- repair
- rewrite
- promotion candidate
- declined

These labels describe technical readiness and ecosystem fit. They do not erase authorship or the useful intent of a contribution.

## Official status

Only a completed promotion review can make a candidate an official reusable Velvet module.

The governing principle is:

**Open contribution, controlled adoption.**

Use the repository's **Module Lab Request** issue form to begin.
