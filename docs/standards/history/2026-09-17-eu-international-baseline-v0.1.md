# Regulatory Baseline Snapshot — 2026-09-17 / v0.1

**Record type:** Historical snapshot  
**Rewrite policy:** Immutable after merge except for factual correction with an explicit correction note.  
**Compliance claim:** None.

## Why this snapshot was created

By September 2026 Velvet already contained substantial architecture around explicit authority, local-first operation, receipts, lineage, controlled execution, emergency intervention, vehicle observation, update history, and separate engineering/safety responsibilities.

A review of current EU, UNECE and ISO material showed that many of those independently developed project choices correspond to concerns formal automotive frameworks also address. This snapshot was created to preserve that point in project history before standards work became a more formal Eleanor responsibility.

## Project position at this date

Velvet's guiding position is not anti-OEM replacement. The project intends to understand an OEM vehicle, preserve useful OEM protections and system intent, unlock capabilities where appropriate, and improve or extend the system only where the change can be justified.

Adopted doctrine:

> **Preserve OEM intent. Extend OEM capability. Improve where justified. Prove every safety-relevant deviation.**

The standards programme is therefore intended to sharpen Velvet, expose missing engineering work, and produce traceable evidence. It is not intended to reshape Velvet into a checklist-driven clone of an OEM architecture.

## Existing project concepts noted during this review

At this date the documented ecosystem already included:

- Court/Runtime authority and capability gating;
- bounded executors and safety gates;
- append-only receipts;
- Riven identity and lineage;
- Velour's provenance-aware archive role;
- passive-first vehicle/CAN qualification;
- Charlotte as the driving/minimal-risk-stop specialty;
- Temperance as an independent medical/guardian specialty;
- Ruby as the engine/ECU/diagnostics specialty;
- Eleanor as the engineering lifecycle owner;
- local-first operation and optional cloud assistance;
- explicit separation between intelligence proposing an action and physical execution authority.

These were recorded as architectural correspondences, not as proof of standards conformance.


## Recovered historical pointers predating the formal standards map

The v0.1 review also recovered earlier founder requirements, engineering proposals, and implementation pointers showing that the design concerns existed before the September 2026 standards exercise. Their provenance strength is recorded in `../decision_provenance.md`.

- **2025-04-24 to 2025-04-25:** OEM-only fallback and override theory preserved direct OEM operation for valet, mechanic, debugging, safe-mode and emergency use. Velvet was not intended to make basic OEM control dependent on the custom stack.
- **2025-04-27:** OEM controls remained primary while Velvet enhancements operated in parallel. This became an early form of the later preserve-OEM-intent doctrine.
- **2025-04-28:** a contemporaneous engineering proposal favoured opto-isolated/driver-separated control paths between general-purpose compute and vehicle loads; explicit founder acceptance of that exact chain remains to be sourced.
- **2025-05-06:** local-versus-LAN delegation separated critical/sensitive local action from bulk or passive network work.
- **2025-05-10:** emergency-system theory included a slow/safe path, non-critical system stand-down and minimal-function posture.
- **2025-05-15:** early CAN hardware selection was framed around observing and learning vehicle state first, with active control treated as a later and more consequential authority step.
- **2025-10:** contemporaneous AGL/OEM engineering proposals explored non-intrusive extension, OEM/independent trust mechanisms, local proofs, owner-held identity material, selective disclosure and temporary-session cleanup.
- **2026 before this review:** Event Protocol/Court/Receipts, Riven, Ghost simulation boundaries, Charlotte/Temperance minimal-risk doctrine and Eleanor's engineering lifecycle made those older instincts explicit and testable.

These are chronology anchors, not retrospective claims that the project had already implemented a named standard. They are retained so later standards work cannot accidentally rewrite the project's history as though the architecture was copied from a compliance checklist.

Related repository lineage: `smart_stereo_origin_lineage.md`, `event_authority_receipt_lineage.md`, `medical_minimal_risk_lineage.md`, and `riven_continuity_lineage.md`.

## Standards and regulations placed on the initial watchlist

The initial baseline tracks:

- Regulation (EU) 2018/858 — vehicle approval and market surveillance;
- Regulation (EU) 2019/2144 — General Safety Regulation;
- UN Regulation No. 155 — cybersecurity and cybersecurity management systems;
- UN Regulation No. 156 — software update and software update management systems;
- ISO/SAE 21434:2021 — automotive cybersecurity engineering;
- ISO 26262:2018 series — functional safety;
- ISO 21448:2022 — SOTIF, plus its 2026 Edition 2 working-draft watch item;
- ISO/PAS 8800:2024 — safety and artificial intelligence;
- ISO 24089:2023 and Amendment 1:2024 — software update engineering;
- Regulation (EU) 2024/1689 as amended in 2026 — EU AI Act applicability watch;
- Regulation (EU) 2024/2847 — Cyber Resilience Act scope boundary watch.

## Important observations captured at baseline

1. A personal research retrofit, a marketed Velvet board, and a safety-critical vehicle-control product cannot be treated as the same regulatory object.
2. Applicability must be determined by intended use, market, product/component boundary, and control authority.
3. Similarity between a Velvet mechanism and a standard's objective is useful engineering evidence but is not certification.
4. Riven and Receipts provide a promising base for software/configuration traceability, but a formal update-management lifecycle requires additional defined evidence and tests.
5. Charlotte and Temperance require substantially more formal hazard, SOTIF, operational-limit, sensor-failure, override, and validation work before safety-related intervention could be treated as qualified.
6. Future official Velvet boards should be designed with product classification, installation constraints, traceability, security lifecycle, and OEM interface boundaries in mind from the beginning.
7. Safety-related AI should have versioned limitations, uncertainty handling, scenario evidence, fallback behaviour, and retained validation records.
8. The standards archive should preserve historical states rather than rewriting prior understanding to match later project maturity.

## Initial future-work direction

Eleanor should eventually translate relevant external requirements and engineering principles into Velvet-native requirement IDs and link them through:

`source -> Velvet requirement -> subsystem -> implementation -> test -> evidence/receipt -> review status`

Velour should retain the supporting research and dated evidence. Riven/Receipts should provide configuration and outcome lineage where appropriate. Domain organs such as Charlotte, Temperance and Ruby should supply domain-specific hazard and validation evidence without becoming their own authority to approve safety-critical execution.

## Primary-source review date

Primary public sources were checked on **2026-09-17**. The living files under `docs/standards/` should be updated when tracked documents change, while this snapshot remains preserved as the project's v0.1 historical record.
