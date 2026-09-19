# Velvet Manufacturing and Quality-System Baseline

**Status:** Living manufacturing / quality-system reference  
**Baseline:** MQS v0.1  
**Reviewed:** 2026-09-17  
**Compliance claim:** None  
**Purpose:** Define the minimum company machinery needed to turn a Velvet design into a repeatable, traceable, supportable product without forcing the project into premature OEM bureaucracy.

## 1. Core doctrine

Velvet does not need to become a Tier-1 automotive supplier to learn from good manufacturing discipline.

The working rule is:

> **Standardize the evidence, not the soul.**

A future Velvet product should preserve the project's open, repairable, owner-controlled character while still being able to answer:

- what exact unit was built;
- from which design revision;
- with which parts and suppliers;
- using which firmware/software/calibration;
- by which manufacturing/test process;
- with which measuring equipment;
- what passed or failed;
- what changed later;
- which customers/vehicles may be affected by a defect;
- and what corrective action was taken.

The quality system exists to make those answers reconstructable.

## 2. Current quality-management landscape

### 2.1 ISO 9001:2026 — current general QMS baseline

ISO published **ISO 9001:2026** on 2026-09-16. It replaces ISO 9001:2015 and is now the current edition.

The 2026 edition retains the familiar quality-management structure while sharpening areas including leadership, quality culture, risk/opportunity handling, organizational knowledge, digitalization, supply-chain resilience and continual improvement.

**Velvet use now:** engineering reference and future-business framework.

**Velvet position:** certification is not currently required merely to build or sell a Velvet product. Adopt the useful process discipline first; consider certification when customers, scale, contracts, insurers, supply-chain position or business goals justify it.

Primary sources:
- https://www.iso.org/standard/9001
- https://www.iso.org/news/2026/09/ISO9001-2026

### 2.2 ISO 10012:2026 — measurement management

ISO 10012:2026, published in February 2026, addresses measurement-management systems and confidence in measurement results used for design, development, production, testing and service.

This is directly useful for:

- multimeters;
- oscilloscopes;
- torque tools;
- crimp-force/crimp-height tools;
- calipers/micrometers;
- power supplies;
- CAN test equipment;
- thermal measurement;
- RF/EMC pre-compliance equipment;
- automated production fixtures.

**Velvet rule:** a test result is only as useful as the measurement chain that produced it.

Primary source:
- https://www.iso.org/standard/10012

### 2.3 ISO 10007:2017 — configuration management

ISO 10007:2017 remains the current published configuration-management guideline, confirmed in 2023. ISO is developing a fourth edition.

Its concept is particularly useful for Velvet because a "product" may include hardware, firmware, software, calibration, harness, enclosure and vehicle profile.

Primary sources:
- https://www.iso.org/standard/70400.html
- https://www.iso.org/standard/92170.html

### 2.4 ISO 19011:2026 — auditing management systems

ISO 19011:2026 was published in May 2026 and provides current guidance for management-system auditing.

Velvet does not need an army of clipboard goblins. But periodic internal audits are useful once products ship because they test whether the documented process is actually being followed.

Primary source:
- https://www.iso.org/standard/19011

## 3. Automotive-supply-chain reference without premature certification

### 3.1 IATF 16949:2016 remains the current published automotive QMS standard

IATF continues to operate IATF 16949:2016 while developing Revision 2.

In July 2026, IATF reported five major Revision 2 priorities:

- simplification / clarity / efficiency;
- software quality assurance;
- Tier-N supply-chain management;
- launch management;
- customer-specific requirements.

IATF's current planning targets publication of the second edition around **mid-2027**, subject to change.

**Velvet use now:** reference for where automotive customers may eventually push the quality system.

**Do not pursue IATF certification simply because Velvet goes commercial.** It becomes materially relevant if Velvet enters an OEM/Tier automotive supply chain or a customer contract requires it.

Primary sources:
- https://www.iatfglobaloversight.org/iatf-169492016/about/
- https://www.iatfglobaloversight.org/wp/wp-content/uploads/2026/07/Stakeholder-Communique-SC-2026-005_IATF-16949-2nd-Edition-status.pdf

### 3.2 IATF certification rules

IATF Rules 6th Edition became effective 2025-01-01 and governs the recognized certification scheme.

That is useful to track, but it should not be confused with ordinary internal quality-system practice.

Primary source:
- https://www.iatfglobaloversight.org/news/1-april-2024-rules-6th-publication/

## 4. AIAG automotive core-tool references

### 4.1 APQP 3rd Edition

AIAG's APQP 3rd Edition was released in 2024. It added stronger treatment of sourcing, change management, program metrics, risk mitigation, gated management and part traceability.

**Velvet use:** borrow the gated product-launch structure for official hardware.

Primary source:
- https://www.aiag.org/training-and-resources/manuals/details/APQP-3

### 4.2 Control Plan 1st Edition

AIAG separated the Control Plan into its own first edition in 2024 and introduced stronger launch-control guidance including "Safe Launch."

**Velvet use:** define which manufacturing characteristics/tests are controlled at each process step, especially during pilot batches and early production.

Primary source:
- https://www.aiag.org/training-and-resources/manuals/details/CP-1

### 4.3 PPAP 4th Edition

AIAG currently lists PPAP 4th Edition / 2nd printing as the production-part-approval reference.

**Velvet use:** not required for direct-to-consumer aftermarket products unless a customer requires it, but useful as a mental model for proving that the production process can repeatedly make the released design.

Primary source:
- https://www.aiag.org/training-and-resources/manuals

### 4.4 AIAG & VDA FMEA

The AIAG & VDA FMEA Handbook remains an automotive reference for Design FMEA, Process FMEA and supplemental monitoring/system-response FMEA.

**Velvet use:** Eleanor can use a simplified DFMEA/PFMEA method well before any customer formally demands the handbook.

Primary source:
- https://www.aiag.org/training-and-resources/manuals/details/FMEAAV-1

## 5. Electronics and harness workmanship references

### 5.1 J-STD-001J

IPC lists **J-STD-001 Revision J (2024)** as the current requirements standard for soldered electrical/electronic assemblies.

### 5.2 IPC-A-610J

IPC lists **IPC-A-610 Revision J (2024)** as the current acceptability standard for electronic assemblies.

### 5.3 IPC/WHMA-A-620E

IPC/WHMA-A-620 Revision E remains the current cable/wire-harness acceptability standard in IPC's revision table.

### 5.4 Printed-board quality

IPC's current revision table lists **IPC-6012F (2024)** for qualification/performance of rigid printed boards and **IPC-A-600M (2025)** for printed-board acceptability.

**Velvet use:** official board/harness purchase drawings should eventually state the workmanship/acceptability standard and class actually required. Do not write "IPC Class 3 everywhere" merely because it sounds expensive and impressive.

Primary source:
- https://www.ipc.org/ipc-document-revision-table

## 6. Velvet production maturity levels

### Q0 — bench experiment

Examples:
- breadboard;
- dev board;
- hand-wired test rig;
- one-off module.

Required:
- basic source/design identity;
- known power limits;
- test notes;
- clearly marked not-for-sale / prototype state.

No production claim.

### Q1 — engineering prototype

Examples:
- first Eleanor PCB;
- prototype harness;
- enclosure mockup.

Required:
- hardware revision;
- BOM;
- schematics/layout source;
- firmware/software version;
- build notes;
- known deviations;
- basic functional test.

### Q2 — pilot / beta

Examples:
- 5–50 controlled units;
- internal/tester fleet.

Required:
- released drawing/BOM package;
- controlled substitutions;
- serialized units;
- build traveler;
- manufacturing test;
- test-fixture version;
- nonconformance log;
- field-return route;
- safe-launch controls.

### Q3 — sellable aftermarket product

Required:
- formal released configuration;
- intended/prohibited use;
- supplier qualification;
- incoming inspection plan;
- manufacturing work instructions;
- workmanship criteria;
- calibrated/controlled measurements where relevant;
- 100% end-of-line safety/functional tests where appropriate;
- serial/lot traceability;
- packaging/label control;
- product documentation;
- field-incident and corrective-action process;
- regulatory-market dossier;
- warranty/service process.

### Q4 — safety-relevant vehicle product

Add:
- DFMEA/PFMEA;
- safety characteristics;
- stronger supplier/change control;
- independent release review;
- test coverage tied to hazards;
- calibration/configuration lock;
- component/harness qualification evidence;
- failure-injection testing;
- stricter deviation authorization;
- field safety escalation;
- recall readiness.

### Q5 — OEM / Tier supply programme

Add only when required:
- applicable customer-specific requirements;
- IATF 16949 / customer QMS expectations;
- APQP/Control Plan/PPAP deliverables;
- customer portals/scorecards;
- formal production validation;
- sub-tier quality deployment;
- customer-defined special-process assessments.

Q5 is **not** the default goal for direct aftermarket Velvet products.

## 7. Product identity: the foundation

Every sellable Velvet item needs a stable identity.

Minimum identity:

```text
product_family
part_number
hardware_revision
serial_number_or_lot
bom_revision
pcb_revision
firmware_version
software_version
bootloader_version_if_applicable
calibration_version_if_applicable
harness_revision
enclosure_revision
radio_module_and_antenna_config_if_applicable
manufacture_date
manufacturing_site_or_builder
test_fixture_version
final_test_record
```

For safety-relevant products, bind the identity into Riven/Receipts where practical.

### MQS-ID-001 — unique product identity

Every Q3+ official Velvet product shall carry a stable product/part identifier and a serial or controlled lot identity sufficient to determine the released build configuration.

### MQS-ID-002 — exact software/configuration identity

Where software or calibration affects function, the shipped unit record shall identify the exact released software/firmware/calibration configuration.

## 8. Design release and change control

### MQS-CHG-001 — released baseline

A product may not enter Q3 production from a mutable development branch.

Release shall identify:

- approved schematic/layout;
- approved mechanical files;
- approved BOM;
- approved firmware/software;
- manufacturing instructions;
- test specification;
- required regulatory/qualification evidence;
- open deviations.

### MQS-CHG-002 — engineering change record

Every production-affecting change shall record:

- reason;
- affected products/revisions;
- design files changed;
- risk/hazard impact;
- compatibility impact;
- supplier/manufacturing impact;
- test/requalification required;
- disposition of old inventory;
- effective serial/lot/date.

### MQS-CHG-003 — no silent substitute

A supplier or assembler may not silently substitute an electrically, mechanically, thermally, RF/EMC or safety-relevant component without engineering review.

"Equivalent" in a distributor search result is not configuration control.

## 9. Supplier and purchasing controls

### MQS-SUP-001 — approved supplier/part source

For controlled production parts retain:

- manufacturer;
- manufacturer part number;
- approved distributor/source;
- datasheet/revision;
- lifecycle status;
- counterfeit/traceability risk where relevant;
- incoming verification requirement.

### MQS-SUP-002 — critical supplier classification

Classify suppliers/parts by consequence:

- ordinary commodity;
- function-critical;
- EMC/power critical;
- safety critical;
- sole-source/high-obsolescence risk.

Supplier controls scale with consequence.

### MQS-SUP-003 — incoming inspection

Define what must be checked before material reaches production.

Possible checks:

- identity/label;
- quantity;
- physical damage;
- PCB fabrication report/coupons where required;
- connector/keying;
- harness wire/terminal identity;
- critical dimensions;
- certificates/test records where contractually required.

Do not inspect everything because paperwork feels productive. Inspect where the risk model says incoming defects matter.

## 10. Manufacturing traveler / build record

Each serialized or controlled-lot Q2+ product should have a build record capable of showing:

- unit/lot identity;
- released work instruction revision;
- board/harness/enclosure revisions;
- material lot identifiers where necessary;
- operator/assembler;
- date;
- special process;
- rework/repair;
- deviations;
- in-process checks;
- final test;
- disposition.

Electronic records are preferred where they improve traceability.

### MQS-BUILD-001 — no orphan unit

No Q3+ shipped unit shall exist without a build/test record linked to its product identity.

## 11. Workmanship and special processes

Use explicit acceptance criteria instead of "looks good."

Possible references:

- J-STD-001J for soldered assemblies;
- IPC-A-610J for assembly acceptability;
- IPC/WHMA-A-620E for harnesses;
- appropriate PCB fabrication standard/class.

### MQS-WORK-001 — workmanship class declared

The product drawing/manufacturing package shall declare the applicable workmanship requirements and class where used.

### MQS-WORK-002 — controlled rework

Rework/repair shall be:

- performed to approved instructions;
- recorded when product integrity/traceability can be affected;
- reinspected/retested;
- prevented from silently changing configuration identity.

## 12. Production test strategy

A compliance lab does not replace production test.

Formal qualification proves the design/configuration under defined conditions.

Production test asks whether **this particular unit** was built correctly.

### Q3 minimum test families

As applicable:

- input current / gross short check;
- protected power-up;
- supply-rail verification;
- firmware identity;
- secure/verified boot check where implemented;
- storage/memory check;
- CAN TX/RX/listen-only check;
- Ethernet/network interfaces;
- digital/analog I/O;
- relay/driver outputs under safe simulated load;
- sensor interfaces;
- audio I/O;
- radio-module identity/basic function;
- watchdog/reset recovery;
- safe-output state during boot/reset;
- serial/label verification.

### MQS-TEST-001 — test fixture is configuration-controlled

Automated/manual production test fixtures shall have:

- fixture ID;
- hardware revision;
- test-software version;
- test specification revision;
- known calibration/verification state.

### MQS-TEST-002 — raw result retention

For Q3+ products retain enough underlying result data to distinguish pass/fail history from a manually typed "PASS."

## 13. Measurement and calibration

### MQS-MEAS-001 — fit-for-purpose measurement

Every quality-critical measurement shall have:

- defined required accuracy/resolution;
- appropriate equipment;
- known calibration/verification status;
- defined environment/method where necessary.

### MQS-MEAS-002 — out-of-tolerance impact review

If measuring equipment is later found inaccurate/out of tolerance, assess whether previously accepted products could have been incorrectly accepted.

That review itself becomes a retained quality record.

## 14. Nonconformance and quarantine

### MQS-NC-001 — failed material cannot drift back into production

Nonconforming material/product shall have:

- clear physical or electronic identification;
- quarantine/control;
- documented disposition.

Allowed dispositions can include:

- rework;
- repair;
- use-as-is under approved deviation;
- return to supplier;
- scrap.

Safety-related use-as-is decisions require explicit engineering authority.

### MQS-NC-002 — deviation expires

Temporary deviations shall have:

- reason;
- scope;
- affected quantity/serials;
- risk review;
- approval;
- expiration/closure condition.

No immortal "temporary" deviation.

## 15. Corrective action / CAPA-lite

Velvet does not need a bureaucracy cannon for every crooked label.

Use graded corrective action.

### Level A — local correction

One-off obvious issue with no systemic/safety implication.

Record as needed; fix it.

### Level B — structured root cause

Repeated issue, process escape, supplier defect or customer return.

Record:

- problem;
- containment;
- root cause;
- correction;
- corrective action;
- effectiveness check.

### Level C — safety / systemic CAPA

Potential safety defect, widespread escape, regulatory issue or recurring systemic failure.

Requires:

- formal incident leader;
- affected-population analysis;
- stop-ship/containment decision;
- regulatory/recall assessment;
- verified corrective action;
- management closure.

### MQS-CAPA-001 — effectiveness must be checked

"Changed the instruction" is not corrective action evidence by itself. Confirm that recurrence risk was actually reduced.

## 16. Safe launch / pilot production

Borrow the useful concept from modern automotive Control Plan practice without pretending Velvet is already an OEM supplier.

For initial production or major changes, use a temporary enhanced-control period:

- smaller controlled batch;
- extra inspection/test coverage;
- tighter review of field feedback;
- no silent supplier substitutions;
- rapid stop-ship authority;
- release only after defined evidence.

### MQS-LAUNCH-001 — safe-launch exit criteria

A new product/revision shall not leave enhanced launch controls merely because the planned calendar date arrived.

Exit requires the defined quality evidence.

## 17. Software and firmware industrialization

Hardware quality records must include software.

### MQS-SW-001 — reproducible release

A production firmware/software release shall identify:

- source commit/tag;
- dependency/lock state;
- build environment/toolchain where needed;
- artifact hash;
- signing state if used;
- configuration/calibration inputs;
- test results;
- release approval.

### MQS-SW-002 — manufacturing image controlled

The image/flashing package used by manufacturing shall be released and version-controlled separately from development workspaces.

### MQS-SW-003 — update ancestry retained

If field updates exist, preserve shipped version -> update version -> rollback/recovery ancestry through Riven/Receipts or an equivalent production ledger.

## 18. Serial, lot and label strategy

Do not let identity become an Etsy sticker problem.

A future label scheme should reserve fields for:

- Velvet product name;
- part number;
- revision;
- serial/lot;
- regulatory IDs/marks where applicable;
- voltage/current;
- manufacturer/business identity;
- country of origin where required;
- QR/DataMatrix linking to public support/product record where useful.

Security-sensitive secrets do not belong in public label data.

## 19. Field returns / FRACAS

Create a Failure Reporting, Analysis and Corrective Action style loop without requiring that specific acronym externally.

```text
field symptom
  -> intake
  -> preserve unit/configuration
  -> reproduce
  -> classify severity
  -> root cause
  -> affected-population search
  -> corrective action
  -> verification
  -> service bulletin / recall if applicable
  -> feed lesson back to Eleanor
```

### MQS-FIELD-001 — preserve returned evidence

A returned safety-relevant unit shall not be immediately reflashed/repaired in a way that destroys the original failure state before evidence capture.

## 20. Service bulletins and recall readiness

### MQS-FIELD-002 — controlled service communication

Service bulletins shall identify:

- affected product/revisions;
- symptom;
- safety consequence if any;
- diagnostic method;
- corrective action;
- parts/software required;
- superseded guidance.

### MQS-RECALL-001 — traceability rehearsal

Before Q4 product launch, conduct a tabletop exercise:

> "Serials X through Y have a safety defect. Can we identify affected configurations, customers/distributors, fix instructions and evidence within hours rather than archaeological weeks?"

If not, traceability is inadequate.

## 21. Training and competence

### MQS-COMP-001 — competence for consequential work

People performing:

- soldering;
- harness crimping;
- programming;
- final safety test;
- inspection;
- calibration;
- deviation approval

shall have documented competence appropriate to the work.

A certificate can support competence but does not replace observed capability.

## 22. Internal audits and management review

At early scale, keep this small.

Suggested cadence after commercial launch:

- quarterly lightweight process review;
- annual full internal quality-system review;
- event-triggered audit after serious escape/safety incident;
- supplier audit when risk/performance justifies it.

The audit asks:

- are we doing what our released process says;
- does that process still control the real risk;
- what has escaped;
- what is becoming obsolete;
- what customers/field evidence are telling us.

## 23. Quality metrics that actually matter

Avoid metric theatre.

Useful early metrics:

- first-pass yield;
- rework rate;
- final-test failure by category;
- supplier defect rate;
- field return rate;
- safety-critical escape count;
- repeat failure/root-cause recurrence;
- software rollback/update failure;
- time to identify affected population;
- CAPA closure effectiveness;
- warranty/field cost by failure mode.

A beautiful dashboard hiding bad units is decorative furniture.

## 24. Suggested product record tree

```text
quality/
  qms/
    policy/
    procedures/
    audits/
    management_reviews/
    training/
  products/
    <product_id>/
      intended_use/
      requirements/
      design_release/
      risk/
      bom/
      suppliers/
      drawings/
      firmware_software/
      qualification/
      control_plan/
      work_instructions/
      fixtures/
      incoming_inspection/
      build_records/
      final_test/
      deviations/
      nonconformance/
      capa/
      field_returns/
      service_bulletins/
      recalls/
      obsolescence/
  suppliers/
  calibration/
  templates/
```

This does not have to live in `velvet-docs`; it is a proposed future business/QMS information architecture.

## 25. Eleanor release gates

Suggested gates:

- **QG-REQ-FROZEN** — product requirements/intended use reviewed;
- **QG-DFMEA-REVIEWED** — design risk reviewed where required;
- **QG-DESIGN-RELEASED** — production design baseline locked;
- **QG-SUPPLIERS-APPROVED** — critical suppliers/parts accepted;
- **QG-PROCESS-READY** — work instructions/control plan/fixtures ready;
- **QG-PILOT-PASSED** — pilot build evidence acceptable;
- **QG-QUALIFICATION-PASSED** — required EMC/electrical/regulatory qualification complete;
- **QG-SAFE-LAUNCH-EXIT** — enhanced launch controls may end;
- **QG-PRODUCTION-RELEASED** — normal production approved.

No gate name grants safety authority by itself. Gates are engineering/business release evidence.

## 26. What this changes in Velvet now

No manifesto change.

No need to seek ISO 9001 or IATF certification now.

The immediate value is to design Eleanor's future hardware workflow so that even a cheap official Velvet board can have:

- stable revision identity;
- BOM control;
- supplier/source record;
- serial/lot traceability;
- known workmanship criteria;
- controlled firmware image;
- repeatable final test;
- retained build record;
- nonconformance route;
- field-return learning loop.

That makes the official product better without making DIY Velvet illegal, inaccessible or intentionally difficult.

## 27. Current 2026 watch items

1. **ISO 9001:2026** was published 2026-09-16 and is now the current ISO QMS baseline.
2. **ISO 10012:2026** is now current for measurement-management systems.
3. **ISO 19011:2026** is now current for management-system audit guidance.
4. **ISO 10007:2017** remains current but a fourth edition is under development.
5. **IATF 16949:2016** remains the published automotive QMS standard while Revision 2 is planned around mid-2027.
6. IATF Revision 2 specifically emphasizes software quality assurance, lower-tier supply-chain management and launch management, all relevant to a hardware+software Velvet product.
7. AIAG APQP 3rd Edition and Control Plan 1st Edition are the modern automotive product-launch/control-plan references.
8. IPC lists J-STD-001J and IPC-A-610J as current 2024 revisions, with IPC/WHMA-A-620E current for harness workmanship.

## 28. Next linked pass

Recommended next pass:

> **First official Velvet product family / board architecture dossier**

Rather than continuing to accumulate generic standards indefinitely, pick the first plausible official product family and apply everything learned:

- intended use;
- prohibited use;
- regulatory classification by market;
- Q maturity target;
- hardware architecture;
- connector/harness rules;
- power/EMC strategy;
- software/update identity;
- manufacturing tests;
- labeling;
- qualification plan;
- field-support path.

A strong candidate is a **passive-first Velvet vehicle gateway / CAN + governed I/O family**, because it exercises the architecture without starting with Charlotte's highest-risk actuator authority.
