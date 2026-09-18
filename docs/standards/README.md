# Velvet Standards and Regulatory Archive

This directory is the canonical Velvet area for automotive standards, regulatory scope, and the history of how those requirements relate to the ecosystem.

Velvet did not begin as a compliance project. The architecture grew from retrofit engineering, OEM study, local-first design, safety reasoning, authority control, traceability, and repeated theory work about failure, intervention, updates, privacy, and accountability. This archive records where that existing design converges with formal automotive requirements and where future work is still needed.

## Core doctrine

**Preserve OEM intent. Extend OEM capability. Improve where justified. Prove every safety-relevant deviation.**

Velvet is not built to oppose the OEM. The aim is to understand and unlock an existing vehicle, retain useful manufacturer protections and design intent, and improve or extend capability where a retrofit can do so responsibly.

Standards are used here as engineering references, design constraints, gap detectors, and evidence frameworks. They do not replace Velvet's architecture and they do not create a compliance or certification claim by themselves.

## What this directory records

- which regulations and standards may become relevant to different Velvet deployment levels;
- which Velvet architectural choices already address similar concerns;
- which areas remain conceptual, planned, unverified, or absent;
- why a design decision was made at a particular point in project history;
- what evidence would be needed before claiming conformance, approval, certification, or legal applicability;
- future engineering goals that Eleanor can turn into requirements, tests, and receipts.

## Files

- [`velvet_regulatory_scope.md`](velvet_regulatory_scope.md) — living scope map, present architecture correspondence, gaps, and future goals.
- [`decision_provenance.md`](decision_provenance.md) — dated internal decision chronology, evidence classes, and external-reference discipline for due-diligence history.
- [`jurisdiction_product_watchlist.md`](jurisdiction_product_watchlist.md) — Canada, U.S., UK, Australia, EMC/RF, privacy, and product-market applicability watchlist.
- [`canada_bc_deep_pass.md`](canada_bc_deep_pass.md) — first detailed Canada + British Columbia product, installation, cybersecurity, privacy, and in-use vehicle applicability pass.
- [`emc_rf_electrical_qualification_plan.md`](emc_rf_electrical_qualification_plan.md) — automotive EMC, RF, power-transient, ESD, CAN physical-layer, pre-compliance, and formal-qualification path for official hardware.
- [`standards_manifest.yaml`](standards_manifest.yaml) — machine-readable index of tracked regulations and standards.
- [`history/`](history/) — dated, immutable snapshots of Velvet's regulatory/standards understanding. New reviews create new snapshots rather than rewriting old ones.

## Status language

Use these terms consistently:

- **documented** — the Velvet architecture or repository documentation contains the concept.
- **implemented** — code or hardware implementing the concept exists and has an identifiable version.
- **tested** — documented evidence demonstrates a defined test was performed.
- **qualified** — evidence has been reviewed against a stated Velvet acceptance criterion.
- **conformant** — use only when a defined standard's applicable requirements have actually been assessed.
- **approved / certified / type-approved** — use only when the relevant legal or certification process has been completed by the appropriate authority or assessor.

Similarity to a requirement is not certification.

## Deployment levels

The same Velvet ecosystem can sit under very different regulatory umbrellas depending on what is being built or sold. Track applicability by deployment level rather than treating the whole project as one product.

1. **Research / personal prototype** — experimental bench or private-vehicle work.
2. **Non-safety retrofit** — observation, interface, audio, comfort, logging, or convenience functions without safety-critical control authority.
3. **Connected / updateable retrofit** — networked gateways, remote services, update infrastructure, or security-sensitive vehicle integration.
4. **Marketed hardware / retrofit kit** — Velvet boards, harnesses, modules, or systems supplied to others.
5. **Safety-relevant intervention** — monitoring or functions whose failure or intervention can affect vehicle safety.
6. **Vehicle dynamic control / automation** — steering, braking, throttle, minimal-risk manoeuvres, or automated-driving functions.

A component may move between levels as its intended use changes.

## Maintenance rule

Every substantive standards review should:

1. update the living scope document;
2. update the machine-readable manifest;
3. add a dated snapshot under `history/`;
4. preserve prior snapshots unchanged;
5. record primary sources and the review date;
6. avoid reproducing copyrighted standards text beyond what is necessary for identification or a short quotation;
7. distinguish legal requirements from voluntary engineering standards and from Velvet's own internal doctrine;
8. update the decision-provenance ledger when a historical source, implementation artifact, or external comparison is recovered.

## Current baseline

Initial baseline: **2026-09-17 / v0.1**.

The initial review tracks EU vehicle type-approval and general-safety law, UNECE cybersecurity and software-update regulations, functional safety, SOTIF, automotive cybersecurity engineering, software-update engineering, automotive AI safety, the EU AI Act, and related product-cybersecurity boundary questions.
