# Velvet Regulatory Scope and Traceability

**Status:** Living engineering reference  
**Baseline:** v0.1  
**Reviewed:** 2026-09-17  
**Purpose:** Record the relationship between Velvet's existing architecture, likely future product/deployment scopes, and automotive regulatory or standards frameworks.

## 1. Intent

Velvet's design objective is not to replace OEM engineering for the sake of replacement. The project studies existing vehicle architecture, preserves useful OEM protections and intent, exposes capabilities that can be safely accessed, and adds new functionality where the retrofit can be justified and evidenced.

The working doctrine is:

> **Preserve OEM intent. Extend OEM capability. Improve where justified. Prove every safety-relevant deviation.**

This document is a traceability and planning record, not a declaration that Velvet, the 2008 Tiburon prototype, or any future Velvet hardware is certified, approved, type-approved, or conformant with a named standard.

## 2. Why this exists now

Many Velvet mechanisms were conceived before this formal standards map existed. They arose from theory work around OEM architecture, retrofit constraints, failure handling, authority, local processing, updates, event evidence, emergency intervention, and long-term maintainability.

The purpose of this baseline is to document that prior work honestly, identify where it aligns with formal automotive practice, and expose the areas where Velvet still needs engineering evidence or additional controls.


## 2.1 Recovered pre-standards theory anchors

The following project decisions predate this formal standards review. They are preserved as historical pointers showing that several current controls grew from Velvet's own retrofit/OEM/safety theory work before they were mapped to named regulatory frameworks.

| Recovered period | Earlier Velvet decision or theory | Later standards relevance |
|---|---|---|
| **2025-04-24 to 2025-04-25** | OEM-only operation was retained as a fallback/override path for valet, mechanic, debugging, safe mode and emergency use. The custom system was expected to fail back to direct OEM operation rather than strand the vehicle behind Velvet. | Functional-safety thinking, fail-safe/degraded operation, altered-system analysis, OEM-interface preservation; later useful when reading ISO 26262 and EU vehicle-approval boundaries. |
| **2025-04-27** | OEM controls were kept primary while Velvet's UI and enhanced functions operated in parallel. Window-control theory explicitly kept the normal OEM switches working while adding bounded enhanced behaviour. | Supports the current preserve-OEM-intent doctrine, retrofit boundary definition, safe integration and foreseeable-misuse analysis. |
| **2025-04-28** | Early hardware-control theory used electrically separated chains such as UP Squared GPIO -> opto-isolator -> driver -> relay/motor rather than driving vehicle loads directly from compute. | Fault containment, interface isolation, electrical integration and safety-related hardware design. |
| **2025-05-06** | Local/LAN delegation was split by consequence: fast, critical or sensitive commands stayed local while bulk/passive work could travel over LAN, with common message schemas and fallback logic. | Cybersecurity zoning, least authority, communications boundaries, degraded operation and later R155 / ISO/SAE 21434 reasoning. |
| **2025-05-10** | An emergency protocol already described slowing/safeing the vehicle, disabling non-critical systems and entering a minimal-function state rather than treating emergency mode as unrestricted autonomy. | Functional safety, minimal-risk behaviour, emergency intervention, driver availability and later SOTIF reasoning. |
| **2025-05-15** | MCP2515/TJA1050 CAN interfacing was selected initially around observation of vehicle data, with write capability treated as a later step rather than an automatic right of connection. | Passive-first qualification, network threat reduction, bus/interface ownership and staged authority relevant to R155 / ISO/SAE 21434. |
| **2025-10** | AGL/OEM integration theory explored Velvet as a non-intrusive user-space extension, OEM PKI/TLS compatibility, owner-controlled keys, local proofs, selective disclosure and session data purge for shared vehicles. | Automotive cybersecurity, identity, privacy, lifecycle trust and software/update architecture. |
| **2026, before this review** | Court, capability-bearing execution, Receipts, Riven lineage, Ghost's non-actuating simulation posture, Charlotte/Temperance minimal-risk doctrine and Eleanor's validation lifecycle became explicit ecosystem architecture. | Provides the immediate internal foundation for R155/R156, ISO 26262, ISO 21448, ISO/PAS 8800 and ISO 24089 mapping. |

These entries establish chronology, not compliance. The older decisions were made for practical Velvet engineering reasons. Formal standards mapping was added later to test, sharpen and document those decisions.

Existing research lineage files preserve related internal evolution, including:

- `docs/research/smart_stereo_origin_lineage.md` for retrofit/OEM origin and the growth from vehicle data into authorization, safety, receipts, rollback and emergency doctrine;
- `docs/research/event_authority_receipt_lineage.md` for the observation -> proposal -> authorization -> execution -> receipt separation;
- `docs/research/medical_minimal_risk_lineage.md` for Temperance/Charlotte, multimodal corroboration, minimal-risk stopping and simulation requirements;
- `docs/research/riven_continuity_lineage.md` for append-only lineage, provenance, integrity and update/configuration continuity.

## 3. Existing Velvet foundations relevant to the standards map

The current documented architecture already contains several concepts that are directly useful when reasoning about formal automotive requirements:

| Velvet area | Existing documented intent | Standards relevance |
|---|---|---|
| **Court / Runtime authority** | Explicit identity, context, policy resolution, capability tokens, execution contracts, safety gates, and bounded executors | Supports separation of authority, controlled execution, fault containment, human oversight, and auditable safety/security decisions |
| **Receipts** | Append-only evidence and outcome records | Supports traceability, update records, incident evidence, verification history, and audit preparation |
| **Riven / Continuity Spine** | Identity, lineage, successor evolution, integrity and verified history | Useful for software/configuration lineage, trusted identity, rollback reasoning, and update provenance |
| **Velour / Library** | Provenance-aware local archive and retained history | Useful for engineering evidence, standards references, design rationale, test records, and historical reconstruction |
| **Charlotte** | Driving specialty with bounded states and minimal-risk-stop goals | Relevant to functional safety, SOTIF, driver availability, intervention logic, operational design limits, and automated-control evidence |
| **Temperance** | Independent medical/guardian assessment and escalation | Relevant to monitoring independence, escalation boundaries, human-state sensing, intervention criteria, and privacy |
| **Ruby** | Engine/ECU/diagnostics specialty | Relevant to vehicle integration, ECU interaction, diagnostics, control boundaries, and fault handling |
| **Eleanor** | Engineering lifecycle from requirements through design, validation, manufacturing and revision | Natural owner for standards translation, hazard work, requirements traceability, validation plans, and engineering receipts |
| **Local-first architecture** | Core identity, memory and operation remain local; cloud is optional | Supports privacy, attack-surface reduction, predictable degraded operation, and data minimisation |
| **Passive-first vehicle integration** | Observe and qualify vehicle truth before granting write authority | Supports staged risk reduction and preserves OEM behaviour while a vehicle profile is being learned |

These are architectural correspondences only. Each item still needs implementation-specific requirements, test evidence, configuration identity, and review before any conformance claim could be considered.

## 4. Primary regulatory and standards landscape

### 4.1 Regulation (EU) 2018/858 — vehicle approval and market surveillance

Tracks approval and market-surveillance requirements for motor vehicles, trailers, systems, components, and separate technical units.

**Velvet relevance:** low for a private research prototype, but increasingly important if Velvet hardware or retrofit systems are supplied to others, marketed as vehicle equipment, or affect regulated systems.

Primary source: https://eur-lex.europa.eu/eli/reg/2018/858/2026-08-02/eng

### 4.2 Regulation (EU) 2019/2144 — General Safety Regulation

Covers general vehicle-safety/type-approval requirements and brings multiple active-safety, driver-monitoring, event-data and automated-vehicle topics into the EU framework.

**Velvet relevance:** Charlotte, Temperance, driver availability, emergency intervention, recording policy, and future automated-control features.

Primary source: https://eur-lex.europa.eu/eli/reg/2019/2144/2026-08-02/eng

### 4.3 UN Regulation No. 155 — Cyber Security and Cyber Security Management System

Establishes vehicle cybersecurity and cybersecurity-management requirements, including lifecycle risk management, monitoring and response.

**Velvet relevance:** Court, gateway isolation, threat modelling, capability control, incident evidence, supplier/dependency tracking, update security, and ongoing vulnerability handling.

Primary source: https://unece.org/transport/documents/2021/03/standards/un-regulation-no-155-cyber-security-and-cyber-security

### 4.4 UN Regulation No. 156 — Software Update and Software Update Management System

Establishes software-update management requirements and records around software identity, update safety, integrity, compatibility and lifecycle control.

**Velvet relevance:** Riven, receipts, exact-version manifests, update packages, rollback, configuration identity, qualification evidence, and controlled deployment.

Primary source: https://unece.org/transport/documents/2021/03/standards/un-regulation-no-156-software-update-and-software-update

### 4.5 ISO/SAE 21434:2021 — Road vehicles: Cybersecurity engineering

Defines lifecycle cybersecurity-engineering requirements for vehicle electrical/electronic systems.

**Velvet relevance:** threat analysis, risk treatment, security requirements, verification, lifecycle monitoring, and structured cybersecurity evidence.

Status note: ISO lists the 2021 edition as under systematic review in 2026.

Primary source: https://www.iso.org/standard/70918.html

### 4.6 ISO 26262:2018 series — Road vehicles: Functional safety

Addresses functional safety of safety-related electrical/electronic systems. The standard explicitly recognises alterations to existing released systems and allows the safety lifecycle to be tailored according to the alteration.

**Velvet relevance:** steering, braking, throttle, power control, watchdogs, independent shutdown paths, fault detection, degraded states, actuator authority, and safety cases around altered OEM systems.

Primary source: https://www.iso.org/standard/68383.html

### 4.7 ISO 21448:2022 — Safety of the intended functionality (SOTIF)

Addresses hazards caused by insufficiencies of intended functionality or performance, especially where complex sensing and situational awareness matter.

**Velvet relevance:** driver monitoring, camera/radar perception, sensor fusion, uncertainty, false positives/negatives, emergency intervention, and Charlotte's decision boundaries.

2026 watch item: ISO lists an Edition 2 working draft intended to replace the 2022 edition, with explicit applicability to emergency-intervention and driving-automation functions.

Primary sources:  
https://www.iso.org/standard/77490.html  
https://www.iso.org/standard/93071.html

### 4.8 ISO/PAS 8800:2024 — Road vehicles: Safety and artificial intelligence

Addresses safety-related automotive systems using AI, including risk from AI output insufficiencies and errors.

**Velvet relevance:** any future safety-related AI used by Charlotte, Temperance, perception modules, prediction modules, or other functions whose output can influence vehicle safety.

**Important scope note:** the PAS is written for series-production road vehicles. Velvet should use it as an engineering reference until a specific product/deployment scope establishes direct applicability.

Primary source: https://www.iso.org/standard/83303.html

### 4.9 ISO 24089:2023 + Amendment 1:2024 — Software update engineering

Covers software-update engineering at organisational, project, infrastructure, vehicle/system, and update-package levels.

**Velvet relevance:** Riven, manifests, deployment tooling, update compatibility, update receipts, safe installation, rollback, and configuration history.

Primary sources:  
https://www.iso.org/standard/77796.html  
https://www.iso.org/standard/87522.html

### 4.10 Regulation (EU) 2024/1689 as amended in 2026 — EU AI Act

AI used as a safety component of a regulated product can fall into the high-risk framework when the legal classification conditions are met. The 2026 amendment changed application timing for Article 6(1)/Annex I product-related high-risk systems to 2 August 2028.

**Velvet relevance:** not every Velvet model or feature is automatically high-risk. The question becomes material if an AI function is placed on the market or put into service as a safety component in a product whose applicable legislation and conformity-assessment path trigger the Act.

Primary source: https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng

### 4.11 Regulation (EU) 2024/2847 — Cyber Resilience Act

The CRA generally applies to products with digital elements, but its scope excludes products to which Regulation (EU) 2019/2144 applies.

**Velvet relevance:** do not automatically stack CRA obligations on top of vehicle-sector requirements. Applicability must be determined at the product/component level, especially for non-vehicle Velvet products that may sit outside the 2019/2144 vehicle framework.

Primary source: https://eur-lex.europa.eu/eli/reg/2024/2847/2024-11-20/eng

## 5. Deployment-scope map

### Level 1 — Research / personal prototype

Examples: bench testing, passive CAN observation, private UI/voice development, non-commercial experiments.

Focus now:

- use standards as engineering references;
- preserve OEM behaviour unless a test explicitly requires controlled alteration;
- record design decisions and test evidence;
- establish exact software/hardware configuration identity;
- avoid unsupported compliance claims.

### Level 2 — Non-safety retrofit

Examples: audio, interface, read-only vehicle data, comfort controls, cabin sensing that does not drive safety intervention.

Additional focus:

- electrical safety and vehicle integration;
- privacy/data minimisation;
- power and fault isolation;
- clear separation from safety-critical control networks;
- secure software/configuration management.

### Level 3 — Connected / updateable retrofit

Examples: network gateway, remote communications, updateable ECU-adjacent module, vehicle-to-home services.

Additional focus:

- cybersecurity lifecycle;
- secure boot and update authenticity where supported;
- software/configuration identity;
- rollback/recovery;
- vulnerability monitoring;
- explicit remote-authority boundaries;
- evidence of update compatibility and outcome.

### Level 4 — Marketed hardware / retrofit kit

Examples: official Velvet I/O boards, harnesses, gateway modules, packaged retrofit controllers.

Additional focus:

- intended-use definition;
- product classification and applicable law by market;
- component/system boundary;
- installation requirements;
- misuse analysis;
- technical documentation;
- manufacturing traceability;
- verification and conformity-assessment planning where required.

### Level 5 — Safety-relevant intervention

Examples: driver-state monitoring that triggers vehicle action, collision-avoidance intervention, medical-event response that changes vehicle behaviour.

Additional focus:

- formal hazard analysis;
- independence of monitoring and actuation paths;
- sensor/perception insufficiency analysis;
- false-positive and false-negative consequences;
- human override and handback;
- deterministic degraded behaviour;
- operational limits;
- safety validation and evidence retention.

### Level 6 — Vehicle dynamic control / automation

Examples: Charlotte commanding steering, brake, throttle, clutch, or automated minimal-risk manoeuvres.

Additional focus:

- defined operational design domain;
- safety goals and safety case;
- functional-safety lifecycle;
- SOTIF analysis;
- cybersecurity and update assurance;
- actuator authority and independent inhibition;
- OEM-system interaction analysis;
- fault injection and scenario validation;
- legal/type-approval analysis before road deployment or commercial supply.

## 6. Current strengths to preserve

These are project choices worth retaining as standards work becomes more formal:

- local operation must remain possible when cloud services disappear;
- network reachability must never silently become authority;
- a model can propose but must not directly own unrestricted physical execution;
- vehicle integration should progress from observation to qualification before write authority;
- emergency priority may remove avoidable delay but must not bypass safety, authority, or receipt boundaries;
- software and hardware lineage should remain reconstructable;
- OEM protections should be retained unless a documented engineering reason justifies a change;
- privacy-sensitive sensing should process locally where practical and retain only what is necessary for the defined purpose;
- standards-derived controls should be translated into Velvet-native requirements rather than bolted on as a separate compliance layer.

## 7. Gaps and future engineering goals

The following are goals, not claims of current completion.

### A. Formal requirements traceability

Create stable requirement IDs linking:

`source principle -> Velvet requirement -> subsystem -> implementation -> test -> evidence/receipt -> review status`

Owner: Eleanor + Velour.

### B. Hazard and risk records

Create reusable hazard-analysis templates for:

- loss of steering authority;
- unintended steering;
- unintended braking/throttle;
- sensor disagreement;
- driver-monitoring false positive/negative;
- compute freeze/reboot;
- network compromise;
- update failure;
- corrupt configuration;
- power brownout/key-off transitions;
- OEM gateway/CAN interaction faults.

Owner: Eleanor, with Charlotte/Temperance/Ruby domain input.

### C. Configuration identity

Define a canonical vehicle/build manifest containing at minimum:

- vehicle profile;
- installed Velvet nodes;
- hardware revisions;
- firmware/software versions;
- model/perception versions where safety relevant;
- calibration versions;
- active capability policy;
- safety-critical configuration hashes;
- update/rollback ancestry.

Owner: Riven + Receipts + Runtime.

### D. Update assurance

Move from repository history alone to an explicit update lifecycle including:

- package identity;
- authenticity/integrity verification;
- compatibility preconditions;
- power/state preconditions;
- staged deployment;
- failure recovery;
- rollback policy;
- post-update qualification;
- retained update receipt.

Owner: Riven + Runtime + Eleanor.

### E. Defined operational design limits

For Charlotte and any intervention system, explicitly define where a function is permitted to operate and what conditions force degradation or disengagement.

Owner: Charlotte + Eleanor.

### F. Safety-related AI evidence

For any AI output that can influence vehicle safety, record:

- intended function;
- training/data provenance as applicable;
- known limitations;
- confidence/uncertainty handling;
- fallback behaviour;
- scenario coverage;
- regression evidence;
- version identity;
- post-deployment monitoring plan.

Owner: Eleanor + relevant organ + Velour.

### G. OEM-interface dossier

For each supported vehicle, preserve:

- OEM network/topology findings;
- known gateways and domain boundaries;
- observed message ownership;
- diagnostic paths;
- fail-safe/fallback behaviour discovered during testing;
- interfaces Velvet intentionally leaves untouched;
- every justified deviation from OEM behaviour.

Owner: Ruby + Vehicle CAN + Eleanor.

## 8. Evidence policy

A future compliance or conformity claim must be narrower than the evidence supporting it.

Do not say:

- "Velvet is ISO 26262 compliant" because a safety gate exists;
- "Velvet meets R156" because Git records versions;
- "Velvet is AI Act compliant" because events are logged.

Instead record precise statements such as:

- "Runtime documents an authority gate corresponding to this safety/security objective";
- "Riven records software lineage, but update-package compatibility testing remains open";
- "Charlotte has a defined minimal-risk-stop state model; road-level validation against a formal scenario set has not yet been completed."

The paper trail should make missing evidence visible rather than smoothing it over.

## 9. Review cadence

Review this area when any of the following happens:

- Velvet moves into a new deployment level;
- official Velvet vehicle hardware is designed for sale or distribution;
- steering/brake/throttle authority changes;
- driver/medical monitoring begins commanding intervention;
- the update architecture changes materially;
- a tracked regulation or standard is revised;
- a new jurisdiction is targeted;
- a safety/security incident exposes a missing requirement.

Each review creates a new dated file under `history/`.
