# Velvet Jurisdiction and Product Requirements Watchlist

**Status:** Living applicability watchlist  
**Reviewed:** 2026-09-17  
**Compliance claim:** None  
**Purpose:** Identify non-EU jurisdictions and cross-cutting product requirements that may matter if Velvet moves from private retrofit work into supplied hardware, installed systems, connected services, or safety-relevant products.

## 1. Use this file by product, not by ecosystem

Do not ask whether "Velvet" as a whole complies with a jurisdiction.

For each proposed product/configuration, record:

1. where it will be supplied, installed, operated, or supported;
2. whether it is a vehicle, vehicle alteration, vehicle component/accessory, general electronic product, or software/service;
3. whether it transmits radio energy;
4. whether it is electrically/electronically connected to the vehicle;
5. whether it can affect steering, braking, throttle, restraint, lighting, visibility, driver monitoring, or other safety functions;
6. whether it stores, transmits, or processes personal, location, biometric, health-adjacent, or driving-behaviour data;
7. whether Velvet supplies only the product or also performs installation/modification;
8. whether updates or remote services remain under Velvet-business control after sale.

The applicable regulatory set is the answer to those questions, not the project name.

## 2. Canada — first commercial-home-market watch

### 2.1 Federal vehicle safety — Motor Vehicle Safety Act / CMVSS

Canada's Motor Vehicle Safety Act regulates manufacture/importation of prescribed vehicle classes and prescribed equipment and includes conformity evidence, records, defect/non-compliance notice, and remedy concepts.

Important scope caution for Velvet:

- the federal definition of regulated "equipment" is tied to equipment listed in Schedule I of the Act;
- a standalone Velvet electronic board therefore must not automatically be described as federally prescribed motor-vehicle equipment without classification work;
- Transport Canada also regulates new vehicles and companies modifying/adding equipment in ways that make specialty vehicles;
- in-use modifications to an already registered personal vehicle can engage provincial/territorial rules in addition to, or instead of, federal new-vehicle requirements.

Velvet action:

- classify each sellable board/system before making Canadian compliance claims;
- retain design/manufacturing/test/field-performance records regardless of whether a particular board is federally prescribed;
- preserve a defect/incident escalation path from the beginning.

Primary sources:
- https://laws-lois.justice.gc.ca/eng/acts/M-10.01/FullText.html
- https://tc.canada.ca/en/road-transportation/safety-standards-vehicles-tires-child-car-seats/safety-standards-vehicles

### 2.2 Provincial in-use vehicle rules — British Columbia reference case

A Canadian business case needs a province/territory layer. For British Columbia, the Motor Vehicle Act Regulations and Vehicle Inspection Regulation govern in-service safety and inspection matters. Steering and brake condition/performance are specifically regulated, and certain modified/reconstructed vehicles have inspection requirements.

Velvet relevance:

- Charlotte actuator work cannot be evaluated only against federal manufacturing rules;
- an installed system must preserve the roadworthiness/inspection requirements of the jurisdiction where the vehicle is operated;
- installation instructions should identify vehicle systems that must remain within OEM or applicable inspection specifications.

This BC entry is a reference case, not a claim that BC rules apply everywhere in Canada.

Primary sources:
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/26_58_00_multi
- https://www.bclaws.gov.bc.ca/civix/document/id/complete/statreg/268138823

### 2.3 Canada RF / EMC — ISED

Velvet products containing digital electronics or radios may fall under Innovation, Science and Economic Development Canada requirements independently of vehicle-safety classification.

Tracked items:

- **ICES-003 Issue 7** — RF-emission limits and administrative requirements for information-technology equipment/digital apparatus.
- **RSS-Gen Issue 6 (2026)** — general requirements for radio apparatus.
- **RSS-247 Issue 4** — certification requirements for common licence-exempt digital transmission / WLAN bands relevant to Wi-Fi/Bluetooth-class devices.

Velvet relevance:

- official I/O/gateway/controller boards;
- Wi-Fi/Bluetooth modules;
- cellular/other radio products according to their specific RSS;
- displays, compute nodes, and digital control devices.

Primary sources:
- https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/interference-causing-equipment-standards/ices/ices-003-information-technology-equipment-including-digital-apparatus
- https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-gen-general-requirements-compliance-radio-apparatus
- https://ised-isde.canada.ca/site/spectrum-management-telecommunications/en/devices-and-equipment/radio-equipment-standards/radio-standards-specifications-rss/rss-247-digital-transmission-systems-dtss-frequency-hopping-systems-fhss-and-licence-exempt-local

### 2.4 Canada privacy — connected-vehicle data

For a BC-based private business operating within BC, the BC Personal Information Protection Act is a primary privacy layer. PIPEDA can still matter for interprovincial/international personal-information flows and federally regulated activities.

The Office of the Privacy Commissioner of Canada formed a connected-cars working group with BC, Alberta and Quebec privacy regulators in 2026 and is specifically examining collection, use and disclosure of connected-vehicle personal information.

Velvet relevance:

- cabin cameras and microphones;
- location history;
- driver/occupant identity;
- driving behaviour;
- medical/guardian event evidence;
- remote communications;
- telemetry or diagnostics tied to an identifiable person.

Existing local-first/data-minimisation doctrine should be preserved as product requirements rather than treated merely as a preference.

Primary sources:
- https://www.oipc.bc.ca/about/legislation/
- https://www.priv.gc.ca/en/privacy-topics/privacy-laws-in-canada/the-personal-information-protection-and-electronic-documents-act-pipeda/pipeda_brief/
- https://www.priv.gc.ca/en/privacy-and-transparency-at-the-opc/proactive-disclosure/opc-parl-bp/srsr_20260416/is_srsr_20260416/

## 3. United States

### 3.1 Federal motor-vehicle safety / aftermarket modification

NHTSA administers the Federal Motor Vehicle Safety Standards (FMVSS) for new vehicles and applicable motor-vehicle equipment. After first retail sale, commercial modifiers such as manufacturers, distributors, dealers, rental companies and repair businesses are subject to the federal **"make inoperative"** prohibition: an installation must not knowingly disable or degrade a device or design element installed to comply with an applicable FMVSS.

Individual-owner modifications are treated differently at federal level, while state law may still apply.

Separate from a product being directly covered by an FMVSS, manufacturers of motor-vehicle equipment can have safety-defect notification/recall responsibilities.

Velvet relevance:

- preserve OEM-required safety functions;
- distinguish DIY owner installation from Velvet-business installation;
- identify which FMVSS-protected systems an installation can influence;
- create installation evidence and a safety-defect/recall process before commercial launch.

Primary sources:
- https://www.nhtsa.gov/interpretations/19-000881-30122-hestrin-interp-requestv3
- https://www.nhtsa.gov/vehicle-manufacturers/manufacturer-communications
- https://www.nhtsa.gov/recalls

### 3.2 U.S. vehicle cybersecurity guidance

NHTSA's 2022 Cybersecurity Best Practices for the Safety of Modern Vehicles are non-binding guidance but are an important U.S. engineering reference. NHTSA states they support a risk-based cybersecurity approach and considers industry standards including ISO/SAE 21434.

Velvet relevance:

- gateway segmentation;
- least privilege / Court capability control;
- secure update and recovery;
- logging/monitoring;
- incident response;
- protection of safety-critical paths.

Primary source:
- https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-09/cybersecurity-best-practices-safety-modern-vehicles-2022-tag.pdf

### 3.3 U.S. RF / FCC equipment authorization

RF devices marketed or imported into the United States are subject to FCC equipment-authorization rules. Intentional radiators such as Wi-Fi/Bluetooth transmitters generally require certification; many unintentional radiators use Supplier's Declaration of Conformity or other applicable authorization procedures.

Velvet relevance:

- Wi-Fi/Bluetooth/cellular/radio modules;
- wireless audio/control nodes;
- SDR-derived products if ever supplied as transmitting equipment;
- digital electronics with RF emissions.

Using an already-certified radio module can simplify a host design but does not remove the need to confirm the host/product integration rules that apply.

Primary sources:
- https://opendata.fcc.gov/Engineering-Technology/EAS-Equipment-Authorization-Grantee-Registrations/3b3k-34jp
- https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=44637&switch=P

### 3.4 U.S. connected-vehicle privacy / consumer protection

The FTC has explicitly treated precise geolocation and driving-behaviour data as sensitive connected-vehicle data. Its 2026 final GM/OnStar order followed allegations involving collection and disclosure without adequate notice/affirmative consent.

This is not a complete U.S. privacy map; state privacy laws must also be considered for a commercial product.

Velvet relevance:

- default local processing;
- purpose limitation;
- explicit consent where required;
- no hidden resale/secondary use;
- user deletion/export controls where required;
- clear separation of emergency use from commercial analytics.

Primary source:
- https://www.ftc.gov/news-events/news/press-releases/2025/01/ftc-takes-action-against-general-motors-sharing-drivers-precise-location-driving-behavior-data

## 4. United Kingdom

Great Britain operates its own vehicle type-approval framework. Vehicle/component manufacturers placing covered products on the GB market may need GB type approval. Individual Vehicle Approval and voluntary IVA provide routes for certain individual/modified vehicles.

The UK is also actively updating GB type approval; a consultation published 18 August 2026 proposes incorporating further EU/international developments.

Velvet relevance:

- a marketed vehicle system/component requires UK-specific classification rather than assuming EU approval automatically solves GB market access;
- modified complete vehicles can have a different approval path from standalone electronics;
- Northern Ireland can follow different approval routes from Great Britain.

Primary sources:
- https://www.gov.uk/vehicle-approval
- https://www.vehicle-certification-agency.gov.uk/vehicle-type-approval/gb-type-approval-scheme/
- https://www.gov.uk/government/consultations/updating-gb-type-approval-for-passenger-and-goods-vehicles

## 5. Australia

The Road Vehicle Standards Act 2018 regulates provision/importation of road vehicles and certain road-vehicle components. Australian Design Rules are the national standards for new vehicles; in-service compliance and modification rules also involve states/territories.

Current ADR families include steering, brake-assist and electronic-stability requirements. Vehicle Standards Bulletin 14 is the national code of practice used for light-vehicle construction/modification work, subject to state/territory implementation and limitations.

Radio/electronic products can also engage ACMA equipment rules and the Regulatory Compliance Mark (RCM) framework.

Velvet relevance:

- vehicle-control products require ADR/state modification analysis;
- RF products need Australian frequency/technical-rule checks rather than assuming North American bands are usable;
- product suppliers should plan evidence retention and labeling at design time.

Primary sources:
- https://www.legislation.gov.au/C2018A00163/latest/text
- https://www.infrastructure.gov.au/infrastructure-transport-vehicles/vehicles/vehicle-design-regulation/australian-design-rules/third-edition
- https://www.infrastructure.gov.au/infrastructure-transport-vehicles/vehicles/vehicle-design-regulation/rvs/bulletins
- https://www.acma.gov.au/step-2-show-your-product-complies
- https://www.acma.gov.au/step-5-label-your-product

## 6. Cross-jurisdiction product requirements

### 6.1 UNECE Regulation No. 10 — electromagnetic compatibility

UN R10 covers electromagnetic compatibility of vehicles and electrical/electronic components or separate technical units intended for vehicle fitment.

This belongs high on Velvet's product watchlist because EMC can matter to a CAN gateway, controller or radio box even when the product has no autonomous-driving authority.

Velvet engineering implications:

- conducted/radiated emissions;
- immunity to vehicle electromagnetic disturbances;
- wiring/harness and enclosure design;
- grounding/filtering/transient strategy;
- defined worst-case operating modes for tests;
- version-controlled hardware/BOM so tested construction can be reproduced.

Primary source:
- https://unece.org/transport/vehicle-regulations-wp29/standards/addenda-1958-agreement-regulations-0-20

### 6.2 EU Radio Equipment Directive

If a non-excluded Velvet product intentionally transmits/receives radio and is placed on the EU market, the Radio Equipment Directive can be relevant in addition to vehicle-specific law. The current consolidated Directive is dated 30 May 2026.

A 2026 EU regulation provides that the RED cybersecurity delegated regulation (EU) 2022/30 will be repealed from 11 December 2027 as the Cyber Resilience Act becomes fully applicable, avoiding duplicate cybersecurity regimes for the affected products.

Velvet implication: product classification must decide whether a particular vehicle product is governed by sector-specific vehicle rules, RED, CRA, or a combination/scope exclusion.

Primary sources:
- https://eur-lex.europa.eu/eli/dir/2014/53/oj
- https://eur-lex.europa.eu/eli/reg_del/2026/339/oj/eng

### 6.3 EU RoHS / WEEE

Commercial electrical/electronic products may also need environmental/product-lifecycle analysis independent of functional safety.

Tracked:
- Directive 2011/65/EU — restriction of hazardous substances in electrical/electronic equipment (RoHS);
- Directive 2012/19/EU — waste electrical/electronic equipment (WEEE).

Exact scope/exemptions must be checked for each Velvet product, especially where a product is specifically designed for vehicle installation.

Primary sources:
- https://eur-lex.europa.eu/eli/dir/2011/65/oj
- https://eur-lex.europa.eu/eli/dir/2012/19/oj

## 7. Product-family applicability matrix

| Velvet product concept | Vehicle safety | EMC/RF | Cyber/update | Privacy | Product/market lifecycle |
|---|---|---|---|---|---|
| Passive CAN reader | medium classification watch | high | medium | medium if tied to driver/vehicle identity | high if sold |
| Wired I/O / relay board | medium-high depending connected systems | high EMC | medium | low unless logging identity/data | high |
| Wi-Fi/Bluetooth gateway | medium | high RF + EMC | high | high if connected services | high |
| Audio/voice node | low-medium | high if wireless | medium | high for microphone/identity data | high |
| Cabin/driver monitoring node | high if used for intervention | high | high | very high | high |
| Charlotte actuator controller | very high | high | very high | medium-high | very high |
| Home/forge Velvet node | generally non-vehicle | product-specific RF/EMC/electrical | high if networked | high | consumer/industrial rules by intended use |

This is a triage matrix, not a legal classification.

## 8. Near-term design changes justified by this watchlist

No manifesto change is indicated.

The useful engineering additions are:

- give every official Velvet hardware design a declared **intended use** and **prohibited use**;
- assign a stable hardware revision and BOM;
- preserve testable EMC/grounding/filtering provisions;
- prefer certified radio modules where appropriate while recording integration constraints;
- define installation boundaries against OEM safety systems;
- create privacy/data-flow sheets for any product with cameras, microphones, location, identity or telemetry;
- create a defect/field-incident workflow before selling safety-relevant hardware;
- preserve per-market labeling/documentation fields without hard-coding one jurisdiction into the core architecture;
- make Eleanor's requirement records jurisdiction-aware while keeping the underlying Velvet doctrine jurisdiction-neutral.

## 9. Next research passes

Priority order:

1. **Canada deep pass** — federal + BC product/install/privacy implications for the first realistic Velvet commercial configurations.
2. **U.S. deep pass** — FMVSS/make-inoperative/defect-recall/FCC plus state in-use modification and privacy layers.
3. **EMC/electrical qualification plan** — UN R10, ISED, FCC and practical pre-compliance bench strategy.
4. **UK/Australia detail pass** if those become target markets.
5. **Product-specific dossiers** once the first sellable Velvet board is defined.

Each deep pass should create a dated history record and should never imply applicability until the intended product/configuration is defined.
