# Velvet Standards Decision Provenance

**Status:** Living chronology and evidence index  
**Baseline:** v0.1  
**Purpose:** Preserve when safety, OEM-integration, authority, privacy, update, and retrofit ideas entered Velvet, who introduced them, what evidence exists, and how later standards mapping relates to them.

## 1. Why this file exists

Velvet's standards archive should preserve more than the current design. It should preserve the path by which the design was reached.

That matters for future engineering and regulatory decisions because a later reviewer may need to distinguish:

- a requirement that existed before a named standards review;
- a design proposal that was discussed but not yet adopted;
- an implemented control;
- a tested/qualified control;
- a later reconstruction of older intent;
- an external industry or standards publication that post-dates or pre-dates Velvet's internal work.

This file is a chronology and due-diligence aid. It is not a patent novelty opinion, legal opinion, certification record, or claim that Velvet originated an idea before the automotive industry.

## 2. Evidence classes

Use the strongest available class for each historical statement.

- **P0 — contemporaneous founder/user requirement:** dated user-authored instruction, decision, acceptance, or constraint from the original discussion.
- **P1 — contemporaneous implementation evidence:** dated source commit, hardware record, test, receipt, design file, issue, PR, photo, or other artifact showing the idea existed in implementation.
- **P2 — contemporaneous design proposal:** dated engineering proposal from the original session. Record whether the founder explicitly accepted it.
- **P3 — later reconstruction with supporting records:** later lineage/research document that reconstructs an earlier design from multiple sources.
- **P4 — recollection/pointer awaiting source recovery:** useful clue, but not strong enough for a formal chronology claim until the underlying source is recovered.

Where practical, retain the original source or a durable reference to it. A summary of a chat is weaker evidence than the original exported conversation.

## 3. Chronology discipline

The purpose of this archive is to preserve timing, rationale, evidence state, and later regulatory relevance. It is not intended to establish priority over OEMs, standards bodies, suppliers, researchers, or other projects.


## 3.1 Business and IP evidentiary purpose

This chronology may also support future business due diligence by showing that Velvet concepts, requirements, architecture, code, tests, and product decisions were independently developed over time and were not created retrospectively after a dispute or regulatory inquiry.

That evidentiary purpose has limits:

- repository history can support authorship, chronology, independent development, and design intent;
- copyright protects original expression such as code, documentation, drawings, and other fixed works, not an abstract idea by itself;
- trademarks protect source-identifying names, logos, and other brand indicators;
- patents, industrial designs, and trade secrets have separate eligibility, filing, disclosure, ownership, and territorial rules;
- public disclosure that is useful as provenance can also affect patent or trade-secret options, so potentially patentable or confidential commercial work should be reviewed before publication;
- no chronology entry should be described as proving exclusive ownership of a general engineering concept unless the applicable IP right actually supports that statement.

The goal is therefore twofold:

1. preserve trustworthy evidence that Velvet was independently conceived, designed, implemented, and revised over time; and
2. avoid overstating what that evidence legally protects.

This archive should be useful to future counsel, investors, regulators, assessors, contributors, and maintainers without pretending to substitute for formal IP registration, contracts, or legal analysis.

### Internal chronology claim

Safe form:

> Velvet had a documented requirement for OEM-only fallback by 2025-04-24.

Use this when an internal dated source supports the statement.

### Standards relationship claim

Safe form:

> That earlier requirement later proved relevant to functional-safety, degraded-operation, and retrofit-integration analysis.

This records correspondence without pretending the standard caused the design.

### External chronology reference

When an external regulation, standard, OEM publication, supplier design, paper, or public system later becomes relevant, record its publication/effective date only as context for the Velvet decision history.

Where useful, record:

- the dated Velvet requirement, proposal, implementation, or test;
- the reason for the Velvet decision at that time;
- the external publication/effective date;
- the narrow concept that later became relevant;
- what changed in Velvet, if anything, after the formal review;
- uncertainty or missing evidence.

The objective is to show the project’s contemporaneous reasoning and evolution so a future regulatory review can distinguish pre-existing engineering decisions from controls added specifically because a later requirement applied.

## 4. Recovered chronology anchors

| Date | Provenance | Historical evidence | Present-day relevance |
|---|---|---|---|
| **2025-04-24** | **P0** | Founder required parallel Velvet/OEM connections and an OEM-only valet/override path so the vehicle could start and operate without Velvet interference. OEM controls were to remain functional. | OEM preservation, fallback/degraded operation, retrofit boundaries, altered-system safety reasoning. |
| **2025-04-27 to 2025-04-28** | **P0** | Founder required the regular OEM controls to remain first/primary while the UI added special features; OEM buttons were to remain stock and observed rather than replaced. | Preserve-OEM-intent doctrine, human override, foreseeable use, retrofit integration. |
| **2025-04-28** | **P2, acceptance not independently recovered** | Engineering proposal used a separated control chain: UP Squared GPIO -> opto-isolator -> driver -> relay/direct load. | Electrical isolation, fault containment, hardware-interface safety. |
| **2025-05-06** | **P0** | Founder accepted dual-mode delegation: fast/critical/sensitive commands local; bulk/passive monitoring and background work over LAN, while retaining a common command structure. | Network zoning, least authority, degraded operation, cybersecurity architecture. |
| **2025-05-10** | **P0/P1 pointer** | Founder described `velvet_emergency_protocol.rpy`: fail-safe slows/safes the vehicle, disables non-critical systems, enters a minimal-function state, and allows critical commands only. Recover the original file/commit if available and promote to full P1. | Minimal-risk behaviour, emergency state management, functional safety, driver-unavailability intervention. |
| **2025-05-15** | **P0 + P2** | Founder identified MCP2515/TJA1050 CAN hardware. In the same design period the staged plan began with passive CAN listening/sniffing; command transmission was treated as a later step. | Passive-first qualification, network-risk reduction, staged control authority. |
| **2025-05-18** | **P0** | Founder stated Velvet should be the passenger and learn first, with driving later; the contemporaneous design posture was “watch and whisper, not act—yet.” | Observation before authority, staged validation, SOTIF/perception evidence mindset. |
| **2025-09-28** | **P0** | Founder reaffirmed that Velvet was intended to be built on Automotive Grade Linux rather than merely run as terminal scripts, with AGL as the automotive integration foundation. | Automotive platform integration, lifecycle packaging, service isolation, future OEM-facing architecture. |
| **2025-10-12** | **P2** | Engineering proposals explored non-intrusive AGL/user-space extension, OEM or independent PKI roots, TLS, local processing, owner-controlled keys, selective-disclosure attestations, and ephemeral shared-vehicle sessions. | Cybersecurity, identity, privacy, data minimisation, trust boundaries. |
| **2025-10-20 to 2025-10-22** | **P2 / design-document pointer** | Redpaper/manifesto work described per-node keys, local authentication/encryption, off-cloud operation, parallel OEM integration, and preservation of switches/stereo while Velvet used CAN/GPIO signals in parallel. Recover exact source artifacts where available. | R155/ISO 21434-style lifecycle security concerns; preserve-OEM-intent doctrine. |
| **2026-03-21** | **P0** | Founder accepted observation-first constraints for later autonomy work, including scoped proofs, owner arbitration, emergency disclosure that closes/audits, and zero action authority during early observation. | Controlled learning/observation, privacy, bounded authority, auditability. |
| **2026-05 onward** | **P1/P3** | Public architecture increasingly codified Core-proposes / Court-authorizes / executors-act / Receipts-remember, fail-closed startup, read-only or quarantined vehicle paths, and explicit no-direct-LLM-to-actuator rules. | Authority separation, cybersecurity, functional safety, AI oversight, assurance evidence. |
| **2026-07-10** | **P1** | Ghost System v0 explicitly demonstrated synthetic/read-only CAN observation with no physical bus opened, no CAN transmission, no actuation, and no authority grant. | Safe simulation, qualification separation, evidence that demonstration does not imply live authority. |
| **2026-09-17** | **P1** | Formal EU/UNECE/ISO standards mapping began in `docs/standards/`. | First formal standards baseline. Earlier entries should not be rewritten as though they were created from this review. |

## 5. Evidence promotion workflow

Historical pointers should become stronger over time without rewriting the past.

```text
P4 recollection
  -> recover original source
P3 reconstruction
  -> link original chat / commit / file / test
P2 proposal
  -> record explicit acceptance or rejection
P0 founder requirement
  -> link implementation if one exists
P1 implementation
  -> link test / qualification / receipt
```

A later implementation date does not erase an earlier requirement date. Keep both.

## 6. External regulatory/reference ledger

When an external standard, regulation, OEM publication, supplier design, academic paper, or public product becomes relevant to an earlier Velvet decision, create a reference entry containing:

- external source title;
- publisher / OEM / standards body;
- publication or effective date;
- exact source URL or archive reference;
- dated Velvet evidence and provenance class;
- the original Velvet rationale or problem being solved;
- external publication/effective date;
- the narrow concept that became relevant;
- similarities and material differences;
- whether the external material caused a design change, confirmed an existing approach, or revealed a gap;
- reviewer/date.

The purpose is historical accuracy, regulatory due diligence, and reconstructing design intent.

## 7. Regulatory applicability decisions

If a future review determines that an EU/UNECE requirement or automotive standard applies to a Velvet product or function, use this provenance record alongside the technical evidence to answer:

1. What was the intended function at the time?
2. What hazards or misuse cases had already been identified?
3. What controls existed before the applicability decision?
4. What controls were added because of the formal requirement?
5. Which OEM behaviours were intentionally preserved?
6. Which deviations were deliberate, who approved them, and what evidence justified them?
7. What remained unknown or unverified?
8. What version of hardware/software was actually assessed?

The answer should be reconstructable from dated evidence rather than founder memory alone.

## 8. Related files

- `velvet_regulatory_scope.md` — current regulatory/standards scope and gap map.
- `standards_manifest.yaml` — machine-readable standards index.
- `history/` — immutable dated standards snapshots.
- `../research/smart_stereo_origin_lineage.md` — origin and retrofit lineage.
- `../research/event_authority_receipt_lineage.md` — authority/receipt evolution.
- `../research/medical_minimal_risk_lineage.md` — emergency/minimal-risk lineage.
- `../research/riven_continuity_lineage.md` — continuity and provenance lineage.
