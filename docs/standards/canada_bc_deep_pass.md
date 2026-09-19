# Canada + British Columbia Deep Pass

**Status:** Living engineering/regulatory applicability reference  
**Baseline:** CA-BC v0.1  
**Reviewed:** 2026-09-17  
**Compliance claim:** None  
**Purpose:** Translate current Canadian federal and British Columbia requirements/guidance into practical product-development questions for future Velvet hardware, software, installations, connected services, and safety-relevant vehicle functions.

## 1. Core finding

Canada does not present one single "Velvet certification" path.

The regulatory treatment changes materially depending on whether Velvet is:

- private research on an already-owned vehicle;
- a standalone electronic product sold to an owner/installer;
- a company-performed aftermarket installation;
- part of a vehicle altered before first retail sale;
- a connected service processing personal information;
- a radio/digital electronic product;
- a safety-relevant intervention system;
- or a higher-level automated-driving system.

The correct future question is therefore:

> **What exactly are we supplying, installing, controlling, updating, and retaining data from, and in what province/territory?**

## 2. Federal vehicle-safety scope

### 2.1 Motor Vehicle Safety Act scope must be classified precisely

The Motor Vehicle Safety Act (MVSA) regulates manufacture/importation of vehicles and defined motor-vehicle equipment.

At the 2026-09-17 review date, the Act defines **equipment** as equipment listed in Schedule I and designed for use in/on a vehicle. Schedule I currently lists:

1. tires; and
2. equipment for use in the restraint of children and disabled persons.

That means a standalone Velvet CAN gateway, I/O board, compute node, audio controller, camera node, or actuator controller should **not automatically be described as "motor vehicle equipment" under the MVSA definition**.

However, the same hardware can become relevant to the federal vehicle regime through a different path, for example if a company alters/assembles a regulated vehicle before sale to the first retail purchaser. Under the Act, "manufacture" of a vehicle includes assembling or altering it before first retail sale.

**Velvet rule:** classify the commercial transaction and installation stage before assigning federal vehicle-law obligations.

Primary source:
- https://laws-lois.justice.gc.ca/eng/acts/m-10.01/FullText.html

### 2.2 New vehicle / pre-first-retail alteration

Transport Canada states that vehicles made for sale in Canada and imported vehicles must meet the Canada Motor Vehicle Safety Standards (CMVSS), and that the Motor Vehicle Safety Regulations also apply to companies modifying or adding equipment to make specialty vehicles.

This becomes relevant if a future Velvet business:

- builds or imports complete vehicles;
- converts vehicles before first retail sale;
- supplies a system as part of a specialty-vehicle manufacturing process;
- partners with an OEM/upfitter at the pre-sale stage.

This is a very different compliance posture from selling an owner-installed board for an already-registered used vehicle.

Primary source:
- https://tc.canada.ca/en/road-transportation/safety-standards-vehicles-tires-child-car-seats/safety-standards-vehicles

### 2.3 Records and defect logic

For companies/products that fall within the MVSA vehicle/equipment regime, the Act includes requirements around records related to design, manufacture, testing and field performance, as well as defect/non-compliance notices and corrective action.

Even where a particular standalone Velvet product is ultimately outside the MVSA's defined "equipment" scope, the recordkeeping pattern is worth adopting as internal business doctrine:

```text
design identity
  -> manufacturing identity
  -> verification/test evidence
  -> field-performance evidence
  -> incident/defect triage
  -> affected-version identification
  -> corrective action
  -> retained receipt
```

**Velvet business principle:** build this evidence chain voluntarily before a product category forces us to.

### 2.4 Federal innovation / exemptions are vehicle-level tools

The MVSA allows the Minister, in defined circumstances, to exempt a vehicle model from a prescribed standard to promote new safety features or technologies where overall safety is not substantially diminished.

This is **not** a general-purpose permission slip for experimental retrofit electronics, but it is useful evidence that the Canadian federal framework has an explicit mechanism for new vehicle technologies where the regulated vehicle model and conditions fit.

## 3. Connected and automated vehicle policy

### 3.1 Safety Framework 2.0

Transport Canada's **Safety Framework for Connected and Automated Vehicles 2.0** (2025) is highly relevant to Charlotte and later Velvet control products even where a specific requirement is not yet mandatory.

Transport Canada describes Canada's approach as a mixture of:

- legislation/regulations;
- federal oversight;
- non-regulatory guidance and tools;
- research/testing;
- provincial/territorial responsibilities;
- international standards/alignment.

The Framework explicitly includes advanced driver-assistance systems within its connected/automated-vehicle umbrella and notes that provinces/territories retain responsibilities including driver licensing, vehicle registration, insurance/liability, maintenance, and roadway operation.

**Velvet implication:** federal product/safety analysis never replaces the BC in-use/installation analysis.

Primary source:
- https://tc.canada.ca/en/road-transportation/innovative-technologies/connected-automated-vehicles/canada-s-safety-framework-connected-automated-vehicles-20

### 3.2 Transport Canada safety-assessment posture

Transport Canada provides voluntary guidance for testing automated-driving systems and a Safety Assessment for Automated Driving Systems.

For future Charlotte road trials, these should be treated as Canadian reference material alongside ISO/UNECE work, not as a substitute for provincial permission or formal product classification.

**Internal target:** before any higher-authority Charlotte road trial, create a Canada-specific trial dossier covering:

- intended automated function;
- operational design domain/limits;
- driver/operator responsibilities;
- fallback/minimal-risk behaviour;
- remote assistance/control if any;
- cybersecurity;
- data collection;
- incident response;
- test-vehicle safety;
- public/occupant communication;
- change/configuration identity.

## 4. Canadian vehicle cybersecurity

### 4.1 Vehicle Cyber Security Guidance

Transport Canada's guidance is technology-neutral and lifecycle-oriented. Its core pattern is:

- identify/manage cybersecurity risk;
- protect vehicle systems;
- detect/monitor/respond;
- recover safely and quickly.

This aligns well with Velvet's existing Court/capability, Runtime, Riven, Receipts, gateway boundaries and local-first doctrine.

**But alignment is not qualification.** For a sellable connected vehicle product, Eleanor should translate the guidance into explicit product requirements and verification evidence.

Primary source:
- https://tc.canada.ca/en/road-transportation/innovative-technologies/connected-automated-vehicles/vehicle-cyber-security

### 4.2 VCAT should become a future pre-release exercise

Canada's Vehicle Cyber Security Assessment Tool (VCAT) is voluntary and aimed primarily at vehicle manufacturers and Tier 1/2 suppliers, while Transport Canada notes it may apply to other motor-vehicle stakeholders.

A future Velvet connected gateway or safety-relevant controller should complete an internal VCAT-style assessment before commercial release, even if submission to Transport Canada is not legally required.

**Proposed gate:** `CA-CYBER-VCAT-REVIEWED`.

Primary source:
- https://tc.canada.ca/en/road-transportation/innovative-technologies/connected-automated-vehicles/canada-s-vehicle-cyber-security-assessment-tool-vcat

## 5. British Columbia in-use vehicle layer

### 5.1 BC rules govern the vehicle that actually drives on the road

British Columbia's Motor Vehicle Act Regulations are an in-use layer that remains relevant after federal new-vehicle manufacturing obligations end.

For example:

- vehicles driven on highways must have compliant brakes;
- service-brake performance requirements apply;
- brake tubing/hoses must not impede or adversely affect operation;
- steering components may not be damaged/defective beyond allowed limits;
- steering must operate freely through its range.

**Velvet implication:** a Charlotte brake/steering actuator is not merely an electronics product. Its installation must leave the complete vehicle able to satisfy the applicable in-use mechanical/performance requirements.

Primary source:
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/26_58_00

### 5.2 Do not overstate BC modified-vehicle inspection triggers

BC has a specific regulatory Part for salvaged, modified and reconstructed vehicles. Its listed application triggers include defined modifications such as substantial suspension-height changes, carrying-capacity changes and seating-capacity changes.

Therefore:

> Do not state that every Velvet retrofit automatically requires a BC "modified vehicle inspection."

Instead, determine the actual trigger for the specific build and separately confirm that all ordinary in-use equipment/performance rules remain satisfied.

The Vehicle Inspection Regulation incorporates the current Vehicle Inspection Manual for required inspections.

Primary sources:
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/26_58_00
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/268138823

### 5.3 Proposed BC installation dossier

For any safety-relevant Velvet installation in BC, preserve:

- vehicle VIN/profile and original equipment configuration;
- exact Velvet hardware/software/calibration versions;
- affected OEM systems;
- installation drawings and harness routing;
- reversible/removable features;
- OEM controls retained;
- brake/steering/throttle/clutch interface description;
- failure-state behaviour;
- independent inhibition / power-removal method;
- post-install mechanical inspection results;
- post-install brake/steering functional checks;
- road-test plan and boundaries;
- installer identity/date;
- photos and receipts;
- any required inspection/approval reference.

This is an internal due-diligence dossier unless/until a specific legal requirement says otherwise.

## 6. Privacy: BC first, PIPEDA where applicable

### 6.1 PIPA-BC is the default private-sector layer for activities within BC

BC's Personal Information Protection Act applies broadly to organizations, subject to its exceptions. An organization is responsible for personal information under its control and must designate one or more people responsible for compliance.

It requires, among other things:

- disclosure of collection purposes;
- collection/use/disclosure only for purposes a reasonable person would consider appropriate;
- consent or a valid statutory exception;
- access rights;
- reasonable security arrangements;
- appropriate retention/destruction.

For an ordinary BC private business handling personal information within BC, PIPA-BC will generally be central. PIPEDA can still apply to interprovincial/international personal-information flows and other federal contexts.

Primary sources:
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/00_03063_01
- https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/r_o_p/prov-pipeda/

### 6.2 Velvet-specific data inventory

Treat these as potentially personal/sensitive data when tied or reasonably linkable to an individual:

- account/owner identity;
- voice recordings/transcripts;
- cabin video/images;
- face/occupant features;
- seat occupancy and behavioural signals;
- location and route history;
- driving style/telemetry;
- contacts/communications;
- diagnostics tied to a user/vehicle;
- emergency event records;
- health-adjacent sensor/event information;
- remote access/session records.

**Current architectural advantage:** Velvet's local-first design can minimize business custody of data if products are designed so raw cabin/location/medical-adjacent information does not need to leave the owner's system.

That advantage should become an explicit product requirement, not marketing fluff.

### 6.3 Retention has an important BC nuance

PIPA-BC requires reasonable safeguards. It also requires destruction/de-identification when the purpose and legal/business need for retention have ended.

However, where an organization uses personal information to make a decision that directly affects an individual, section 35 requires retention for at least one year so the individual has a reasonable opportunity to access it.

**Velvet implication:** "delete everything instantly" is not always the correct commercial privacy policy. Retention needs a purpose-specific schedule.

### 6.4 Connected-car scrutiny is increasing

In 2026, the federal Privacy Commissioner described a connected-cars working group involving the federal office and privacy regulators in BC, Alberta and Quebec, focused on collection, use and disclosure of connected-vehicle personal information.

This makes privacy-by-design a live Canadian regulatory concern, not merely an imported EU idea.

Primary source:
- https://www.priv.gc.ca/en/privacy-and-transparency-at-the-opc/proactive-disclosure/opc-parl-bp/srsr_20260416/is_srsr_20260416/

## 7. Consumer-product boundary

The Canada Consumer Product Safety Act (CCPSA) excludes vehicles as defined by the MVSA and an integral vehicle part as assembled/altered before first retail sale, including a replacement/altering part.

That exclusion should **not** be casually applied to every Velvet product.

A standalone consumer electronic device that is not properly within the vehicle/integral-part exclusion may need separate CCPSA analysis. Conversely, a product that truly falls within the vehicle exclusion may be outside that Act.

This is another reason product classification must happen before marketing.

For non-vehicle Velvet home/forge consumer products, CCPSA incident-reporting, recordkeeping and product-safety obligations can become independently relevant.

Primary sources:
- https://laws-lois.justice.gc.ca/eng/acts/c-1.68/fulltext.html
- https://www.canada.ca/en/health-canada/services/consumer-product-safety/legislation-guidelines/acts-regulations/canada-consumer-product-safety-act.html

## 8. Product-by-product Canada/BC triage

| Product concept | Federal vehicle law | BC in-use/install | Cyber | Privacy | Other product law |
|---|---|---|---|---|---|
| Passive CAN reader, owner-installed | MVSA prescribed-equipment status unlikely under current Schedule I; confirm actual product classification | Must not cause complete vehicle to violate in-use requirements | Medium/high if networked | Medium if logs identify owner/vehicle | ISED/EMC/RF; CCPSA classification may need review |
| Wired Velvet I/O/relay board | Same classification caution | High if connected to safety/lighting/visibility/actuation systems | Medium | Low unless it stores identifiable data | EMC/electrical/product classification |
| Wi-Fi/Bluetooth vehicle gateway | Same classification caution | Installation must preserve vehicle safety | High | High if telemetry/location/account data crosses gateway | ISED radio + digital apparatus requirements |
| Audio/voice node | Usually not itself prescribed MVSA equipment; classify | Avoid interference with required controls/visibility and safe operation | Medium | High for microphones/transcripts/identity | ISED if wireless; consumer-product analysis as applicable |
| Driver-monitoring node, warning only | Product classification required | Must not create unsafe distraction/installation condition | High | Very high | Safety evidence rises even before direct actuation |
| Temperance-triggered intervention | High regulatory/safety attention even if board itself is not Schedule-I "equipment" | Very high | Very high | Very high | Formal testing/road-deployment analysis required |
| Charlotte steering/brake/throttle controller | Treat as safety-critical vehicle alteration/product program | Very high; complete vehicle performance matters | Very high | Medium/high | CAV/ADS guidance, insurer/testing permissions, product liability analysis |
| Velvet home/forge node | Usually outside vehicle law | N/A | High if networked | High | CCPSA/electrical/radio rules by product |

This is triage only, not a legal classification.

## 9. Canada/BC requirement candidates for Eleanor

Create future stable requirement IDs from these candidates.

### CA-PROD-001 — Intended-use declaration

Every commercial Velvet product shall have a versioned intended-use statement and prohibited/unsupported uses.

### CA-PROD-002 — Classification record

Before sale/import/installation, retain a dated record of the Canadian product/vehicle regulatory classification and the rationale/source used.

### CA-CONFIG-001 — Reproducible build identity

Every official product shall have a stable hardware revision, BOM, firmware/software identity and relevant calibration/configuration identity.

### CA-INSTALL-001 — OEM safety preservation

Installation instructions shall identify OEM safety functions/interfaces affected by installation and shall define how required OEM function is preserved or how any deviation is validated.

### CA-FIELD-001 — Incident/defect intake

Create a field-incident process capable of identifying product version, vehicle/application, hazard, reproduction status, affected population and corrective action.

### CA-CYBER-001 — Lifecycle cybersecurity file

Connected vehicle products shall have a documented risk, safeguard, monitoring/response, recovery and update-security record aligned to Transport Canada cybersecurity guidance.

### CA-CYBER-002 — VCAT review

Safety-relevant or materially connected vehicle products should complete a VCAT-style review before release.

### BC-VEH-001 — Complete-vehicle roadworthiness

A safety-relevant installation shall include evidence that the affected brake/steering/other regulated vehicle functions remain within applicable BC roadworthiness requirements.

### BC-PRIV-001 — Data-flow inventory

Any commercial Velvet product/service processing personal information shall maintain a data-flow inventory identifying collection, purpose, storage, access, disclosure and deletion/retention.

### BC-PRIV-002 — Local-first minimization

Where technically practical, raw cabin, location, behavioural and health-adjacent data shall remain local unless a defined owner-authorized or legally permitted purpose requires transfer.

### BC-PRIV-003 — Retention schedule

Retention shall be purpose-specific and account for legal/business needs, access rights and section 35 decision-related retention where applicable.

### CA-DOC-001 — Evidence retention

Engineering, test, manufacturing, field-performance, incident and corrective-action evidence shall be retained according to a defined lifecycle schedule.

## 10. What this changes in Velvet today

Very little architectural change is justified.

The review **reinforces** existing choices:

- local-first data handling;
- owner/guest authority separation;
- passive-first CAN qualification;
- Court/capability boundaries;
- Riven configuration lineage;
- Receipts and immutable decision/outcome evidence;
- Ghost/non-actuating simulation;
- preserve-OEM-control doctrine;
- explicit emergency/minimal-risk states.

The main additions are business/process layers:

- product classification;
- intended/prohibited use;
- reproducible BOM/build identity;
- installation dossier;
- privacy data-flow/retention records;
- field defect/incident workflow;
- Canada-specific cybersecurity review;
- jurisdiction-specific roadworthiness evidence.

## 11. Open questions before a first Canadian product launch

Do not close these generically. Resolve them for the actual first product.

1. Is the product a vehicle part/integral part, a general consumer electronic product, a radio apparatus, or a combination for Canadian law?
2. Who installs it: owner, independent shop, approved installer, or Velvet business?
3. Is the target vehicle already sold/registered, or is Velvet involved before first retail sale?
4. Which OEM/BC-regulated functions can the installation affect?
5. Does the product retain or transmit personal data?
6. Does it contain intentional radio transmitters?
7. Does Velvet retain remote update/control capability after sale?
8. What is the field defect/corrective-action process?
9. What insurance/product-liability posture applies to this exact product/service?
10. Does the intended road test require additional provincial/insurer/permit engagement?

## 12. Next linked pass

After this Canada/BC deep pass:

> **EMC / RF / electrical qualification plan**

That pass should connect UN R10, ISED ICES/RSS, practical automotive transient/immunity testing, certified radio-module integration, harness/grounding rules and pre-compliance bench tests directly to Eleanor's official-board workflow.
