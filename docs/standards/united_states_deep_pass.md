# United States Deep Pass

**Status:** Living engineering/regulatory applicability reference  
**Baseline:** US v0.1  
**Reviewed:** 2026-09-17  
**Compliance claim:** None  
**Purpose:** Translate current U.S. federal and selected state-level requirements/guidance into practical product-development questions for future Velvet hardware, software, installations, connected services, ECU integration, and safety-relevant vehicle functions.

## 1. Core finding

The United States is not one approval system for Velvet.

A future U.S. Velvet product can encounter several independent layers:

- NHTSA motor-vehicle safety law;
- Federal Motor Vehicle Safety Standards (FMVSS), where a particular vehicle/equipment item is covered;
- safety-defect/recall obligations even where no FMVSS directly applies;
- the federal "make inoperative" restriction for specified commercial actors that alter already-built vehicles;
- pre-first-retail vehicle-alterer certification duties;
- EPA emissions anti-tampering/defeat-device law;
- FCC equipment authorization for digital/radio products;
- FTC consumer-protection, connected-vehicle privacy, and warranty law;
- state roadworthiness/modification/installer/insurance rules;
- state privacy laws;
- state autonomous-vehicle testing/deployment rules where the product actually meets those definitions.

The practical U.S. question is:

> **What is the product, who installs it, when in the vehicle lifecycle is it installed, what OEM/FMVSS/emissions systems can it affect, what data does it process, and in which state is it used?**

## 2. Motor-vehicle-equipment classification is broader than Canada

### 2.1 Safety Act definition

Under 49 U.S.C. Chapter 301, "motor vehicle equipment" includes:

- original vehicle systems/parts/components;
- similar parts/components sold for replacement or improvement;
- accessories or additions to a motor vehicle;
- certain safety devices intended to protect road users.

NHTSA has long treated vehicle-specific aftermarket accessories/additions as potentially falling within this definition.

**Velvet implication:** a future U.S.-market Velvet CAN gateway, I/O controller, driver-monitoring module, actuator controller, or vehicle-specific interface may be motor vehicle equipment even if no FMVSS directly prescribes technical requirements for that exact product.

Primary references:
- https://www.nhtsa.gov/document/motor-vehicle-safety-unrelated-unmodified-provisions
- https://www.nhtsa.gov/interpretations/10315

### 2.2 No applicable FMVSS does not mean no NHTSA obligations

NHTSA interpretations repeatedly distinguish:

1. whether an FMVSS directly applies to the product; and
2. whether the product is nevertheless motor vehicle equipment subject to safety-defect notification/remedy duties.

This is a critical U.S. distinction for Velvet.

A product may have:

- **no direct FMVSS certification requirement**, yet
- still be **motor vehicle equipment**, and
- still carry **safety-defect/recall responsibilities**.

**Velvet rule:** never write "not regulated by NHTSA" merely because no direct FMVSS was found.

## 3. Part 566 manufacturer identification

49 CFR Part 566 currently requires identification filings from:

- manufacturers of motor vehicles; and
- manufacturers of motor vehicle equipment to which an FMVSS applies.

The filing includes manufacturer identity and a description of covered products and is due within 30 days after beginning manufacture of a new covered type.

**Velvet implication:** Part 566 is not automatically triggered merely because a product qualifies broadly as motor vehicle equipment; it is specifically tied to motor vehicles and equipment to which a motor vehicle safety standard applies.

Primary source:
- https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-566

## 4. "Make inoperative" and the installer distinction

### 4.1 Commercial installers carry a different burden from owners

49 U.S.C. 30122 prohibits specified commercial actors from knowingly making inoperative a device or design element installed in compliance with an applicable FMVSS.

NHTSA identifies the relevant actors as including:

- manufacturers;
- distributors;
- dealers;
- motor vehicle repair businesses.

NHTSA interpretations also state that this federal prohibition does not apply in the same way to an individual owner modifying their own vehicle, though state law may still regulate the result.

**This makes the business model matter.**

```text
Mister installs experimental hardware in Mister's own Tiburon
    !=
Velvet business sells owner-installed hardware
    !=
Velvet business installs hardware for customer
    !=
Velvet business alters a new vehicle before first retail sale
```

The same board can therefore create different federal duties depending on the transaction and installation role.

Primary sources:
- https://www.nhtsa.gov/interpretations/30122-make-inoperative-alan-nappier-april-14
- https://www.nhtsa.gov/interpretations/22250
- https://www.nhtsa.gov/interpretations/lcddvd1

### 4.2 Internal U.S. installation rule

Before a Velvet-business installation:

- identify every FMVSS-related device/design element plausibly affected;
- identify OEM functions involved;
- document pre-install condition where relevant;
- define the expected post-install behaviour;
- verify that the installation does not knowingly degrade the compliant safety function;
- retain exact product/software/calibration/install evidence.

This is product/install due diligence, not a claim that every affected system requires a new FMVSS certification.

## 5. Altering a certified vehicle before first retail sale

49 CFR 567.7 imposes a substantially different obligation when a person alters a certified vehicle before first retail sale, beyond specified minor/readily attachable changes.

The alterer must:

- determine continued conformity of the altered vehicle with applicable Federal motor-vehicle safety, bumper, and theft-prevention standards affected by the alteration;
- assume certification responsibility for the alteration; and
- apply the required additional alterer label.

**Velvet implication:** a future OEM/upfitter/specialty-vehicle programme is categorically different from selling a retrofit box to the owner of a used vehicle.

Primary source:
- https://www.ecfr.gov/current/title-49/subtitle-B/chapter-V/part-567/section-567.7

## 6. Safety defects, recall, and field evidence

### 6.1 Aftermarket motor-vehicle equipment can carry recall obligations

NHTSA has repeatedly stated that aftermarket motor-vehicle equipment can be subject to notification and remedy duties under 49 U.S.C. 30118-30120 even where no FMVSS directly applies to the product.

If the manufacturer or NHTSA determines that a safety-related defect exists, the manufacturer can be responsible for:

- notifying affected purchasers/owners;
- identifying the affected population;
- providing a free remedy;
- reporting the recall as required.

Replacement-equipment manufacturers can therefore carry direct recall responsibility.

Primary references:
- https://www.nhtsa.gov/interpretations/GF004887
- https://www.nhtsa.gov/interpretations/10439
- https://www.nhtsa.gov/interpretations/gf009226

### 6.2 Product identity must support a recall

A future Velvet product should be able to answer:

- which hardware revisions are affected;
- which BOM lots are affected;
- which firmware/software versions are affected;
- which vehicle profiles/installations are affected;
- which serials/customers were supplied where records are lawfully retained;
- what exact field symptom/hazard exists;
- what corrective action applies.

**Velvet rule:** if we cannot identify the affected population, we are not production-ready.

### 6.3 Manufacturer communications can become regulatory evidence

NHTSA requires manufacturers to submit applicable communications sent broadly to dealers/distributors/owners/purchasers concerning defects, failures, malfunctions and similar unintended deviations.

A future business should therefore treat service bulletins, safety notices and field-fix communications as controlled regulatory records rather than casual Discord posts.

Primary reference:
- https://www.nhtsa.gov/nhtsa-datasets-and-apis

## 7. Vehicle cybersecurity and automated-driving posture

### 7.1 NHTSA cybersecurity guidance

NHTSA's 2022 Cybersecurity Best Practices remain a U.S. engineering reference for risk-based vehicle cybersecurity. They are guidance, not a blanket certification scheme.

For Velvet this reinforces:

- least privilege;
- network segmentation;
- protected safety-critical paths;
- vulnerability management;
- secure update/recovery;
- incident detection/response;
- retained evidence.

Primary source:
- https://www.nhtsa.gov/sites/nhtsa.gov/files/2022-09/cybersecurity-best-practices-safety-modern-vehicles-2022-tag.pdf

### 7.2 ADS rules are actively evolving

NHTSA is actively implementing its Automated Vehicle Framework and rulemakings that modernize FMVSS for automated-driving-system vehicles.

State roles remain material for licensing, registration, insurance, testing permissions and road operation.

**Charlotte implication:** do not freeze a 2026 U.S. ADS classification into architecture. Maintain a U.S. watch and classify the actual function at trial/product time.

Primary sources:
- https://www.nhtsa.gov/vehicle-safety/automated-vehicle-safety
- https://www.nhtsa.gov/vehicle-manufacturers/automated-driving-systems
- https://www.nhtsa.gov/press-releases/fmvss-updates-brake-pedal-requirements

### 7.3 California demonstrates the state layer

California DMV currently operates separate permit categories for:

- AV testing with a safety driver;
- driverless testing;
- deployment.

In April 2026 California adopted expanded AV regulations including heavy-duty automated vehicles.

This should be treated as a **state example**, not a universal U.S. requirement and not an automatic classification of Charlotte.

Primary sources:
- https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/
- https://www.dmv.ca.gov/portal/vehicle-industry-services/autonomous-vehicles/autonomous-vehicle-testing-permit-holders/
- https://www.dmv.ca.gov/portal/news-and-media/new-autonomous-vehicle-regulations-strengthen-oversight-and-enforcement-authorize-trucks-and-transit/

## 8. EPA emissions and Ruby/ECU boundaries

### 8.1 Separate emissions axis

NHTSA safety compliance does not resolve EPA emissions compliance.

The Clean Air Act prohibits tampering with required vehicle/engine emissions controls and prohibits manufacturing/selling/installing defeat devices intended to bypass, defeat or render required emissions controls inoperative.

The prohibition can reach both hardware and software.

**Velvet doctrine for Ruby:**

> **Diagnostics and lawful calibration research do not silently become emissions-control defeat authority.**

Primary sources:
- https://www.epa.gov/enforcement/epa-tampering-policy-epa-enforcement-policy-vehicle-and-engine-tampering-and
- https://www.epa.gov/enforcement/national-enforcement-and-compliance-initiative-stopping-aftermarket-defeat-devices
- https://www.epa.gov/enforcement/enforcement-alert-clean-air-act-prohibits-defeat-devices-vehicles-engines

### 8.2 Reasonable-basis evidence must exist before the conduct

EPA's current tampering enforcement policy describes circumstances where the agency generally does not take enforcement action if a person has a documented reasonable basis to conclude the conduct will not adversely affect emissions.

The policy specifically emphasizes contemporaneous documentation and treats OBD-related conduct with additional caution.

**Velvet implication:** "we tested it later and it seemed fine" is weaker than a documented pre-sale/pre-install emissions basis.

### 8.3 2026 federal aftermarket certification development

In July 2026 EPA recognized SEMA's Certified Emissions (SC-E) programme as an alternative path that businesses may use to demonstrate federal Clean Air Act compliance for qualifying aftermarket vehicle products.

This should be tracked as a **current 2026 federal pathway**, not hard-coded permanently into Velvet.

Primary source:
- https://www.epa.gov/newsreleases/epa-implements-new-freedom-fix-presidential-memorandum-gives-sema-greenlight-certify

### 8.4 California retains its own emissions aftermarket layer

California's CARB aftermarket-parts programme requires exemptions for applicable emission-related add-on/modified parts. CARB issues an Executive Order when the part is shown not to increase emissions for the approved application.

ECM programmers/signal modifications are an explicit CARB application category.

**Velvet implication:** Ruby ECU/tune products require a California-specific analysis even if a federal emissions path exists.

Primary sources:
- https://ww2.arb.ca.gov/our-work/programs/aftermarket-performance-and-add-parts
- https://ww2.arb.ca.gov/manufacturers-aftermarket-parts

## 9. FCC RF/digital-product layer

Part 15 devices generally require equipment authorization before importation/marketing where applicable.

Current FCC material states broadly:

- most intentional radiators require Certification;
- most unintentional radiators can use Supplier's Declaration of Conformity or Certification;
- Part 15 devices must not cause harmful interference and must accept interference.

This cross-links to the existing Velvet EMC/RF qualification plan.

Primary references:
- https://docs.fcc.gov/public/attachments/FCC-26-51A1.pdf
- https://apps.fcc.gov/oetcf/kdb/forms/FTSSearchResultPage.cfm?id=21079&switch=P

## 10. Connected-vehicle privacy and consumer protection

### 10.1 FTC connected-vehicle enforcement

The FTC's final 2026 GM/OnStar order followed allegations involving collection/use/sale of precise geolocation and driving-behaviour data without adequate notice and affirmative consent.

The final order includes requirements specific to that case, including consent, access/deletion and geolocation/driver-data controls.

**Do not treat the GM order as a universal statute applying identically to every Velvet product.**

Instead treat it as strong current evidence that the FTC considers deceptive or unfair connected-vehicle data practices within its consumer-protection remit.

Primary sources:
- https://www.ftc.gov/legal-library/browse/cases-proceedings/2423052-general-motors-llc-et-al-matter
- https://search.ftc.gov/news-events/news/press-releases/2026/01/ftc-finalizes-order-settling-allegations-gm-onstar-collected-sold-geolocation-data-without-consumers

### 10.2 California privacy watch

The CCPA can apply to qualifying businesses meeting its statutory thresholds and treats categories such as precise geolocation and health information as sensitive personal information.

As of the current threshold adjustment, one route into the definition of covered "business" is annual gross revenue of at least $26.625 million; other volume/revenue tests can independently apply.

A small early Velvet business may therefore be outside the CCPA's principal "business" thresholds while still being subject to other California laws and contractual/privacy obligations.

Primary sources:
- https://cppa.ca.gov/faq
- https://cppa.ca.gov/regulations/pdf/ccpa_statute_eff_20260101.pdf

### 10.3 Washington My Health My Data is unusually relevant to Temperance

Washington's My Health My Data Act applies beyond traditional HIPAA-covered healthcare and expressly includes categories such as:

- vital signs and bodily measurements;
- biometric data;
- health-status information;
- inferred/derived health information;
- certain precise-location information associated with seeking healthcare.

It contains privacy-policy, consent, processor/security, deletion/rights and geofence provisions, and it expressly applies to small businesses with adjusted compliance timing already in effect.

**Temperance implication:** a commercial Velvet service that receives linked driver/occupant heartbeat, medical-event or health-inference data from Washington consumers must be specifically reviewed against this law.

Primary sources:
- https://app.leg.wa.gov/RCW/default.aspx?cite=19.373
- https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.010
- https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.030
- https://app.leg.wa.gov/RCW/default.aspx?cite=19.373.050

## 11. Warranty and right-to-repair

### 11.1 Velvet's open/repairable model fits U.S. warranty law reasonably well

The Magnuson-Moss Warranty Act and FTC rules govern written warranties on consumer products.

FTC guidance states that warrantors generally may not condition warranty coverage on use of branded parts/services unless the identified item/service is provided free or a narrow legal exception applies.

**Velvet implication:** an official product warranty should not casually say "warranty void if opened" or require Velvet-only repair parts/service where federal anti-tying rules prohibit that.

Primary sources:
- https://www.ftc.gov/business-guidance/resources/businesspersons-guide-federal-warranty-law
- https://www.ftc.gov/news-events/news/press-releases/2024/07/ftc-warns-companies-stop-warranty-practices-harm-consumers-right-repair

### 11.2 Repairability is not immunity from misuse exclusions

Open/repairable does not mean Velvet must warrant:

- damage actually caused by incompatible parts;
- unsafe modifications;
- improper installation;
- use outside documented electrical/environmental limits;
- unsupported actuator configurations.

Warranty terms should distinguish **cause-based exclusions** from blanket anti-repair tying.

## 12. Lawful access to OEM software and data

### 12.1 Current DMCA vehicle exemptions

The current U.S. Copyright Office rule includes temporary exemptions covering:

- circumvention of access controls on lawfully acquired motorized land vehicles where necessary for diagnosis, repair or **lawful modification** of a vehicle function; and
- access/storage/sharing of operational, diagnostic and telematics data by owners/lessees or those acting on their behalf.

The rule also explicitly states that the exemption is **not** a safe harbor from other laws, including DOT and EPA regulations.

**Velvet significance:** this is a useful legal reference for owner-controlled diagnosis/repair/lawful modification, but it does not convert unlawful safety/emissions conduct into lawful conduct.

Primary sources:
- https://www.copyright.gov/title37/201/37cfr201-40.html
- https://www.copyright.gov/1201/2024/

The exemption is temporary and the Copyright Office has begun the next triennial renewal process, so this item must remain on the legal watchlist.

## 13. State-overlay method

Do not attempt one giant permanent 50-state document.

Before U.S. launch/testing/installation in a state, create a state annex covering at minimum:

- vehicle equipment/roadworthiness rules;
- modification/inspection rules;
- repair-business/installer licensing if applicable;
- insurance notification/requirements;
- automated-driving test/deployment rules if relevant;
- consumer/privacy laws;
- biometric/health/location-data rules;
- emissions/inspection rules;
- warranty/service contract rules beyond federal minimums;
- product-liability considerations;
- local restrictions relevant to the intended product.

Suggested first annexes:

1. Washington;
2. California;
3. Oregon;
4. the first actual customer/test state.

## 14. U.S. product-by-product triage

| Velvet product concept | NHTSA/Safety Act | Installer concern | EPA | FCC | Privacy | State overlay |
|---|---|---|---|---|---|---|
| Passive CAN reader | Likely classification review as vehicle accessory/equipment | Low-medium; must not impair safety systems | Low unless emissions/OBD behaviour altered | High if digital/wireless | Medium-high if logs linked vehicle/user data | Yes |
| Wired I/O/relay board | Motor-vehicle-equipment review; safety-defect duties may attach | High depending connected function | Low-medium if ECU/emissions interfaces exist | Digital-emissions rules | Low-medium | Yes |
| Wi-Fi/Bluetooth gateway | Motor-vehicle-equipment review | Medium | Usually low | Very high | High | Yes |
| Audio/voice node | Accessory/equipment review | Medium for visibility/controls/safe install | Low | High if wireless | High for mic/transcript data | Yes |
| Driver-monitoring warning-only node | Strong safety/equipment relevance | Medium-high | Low | High | Very high | Yes |
| Temperance medical-event service | Safety/equipment relevance rises if vehicle action follows | High if professionally installed | Low | Product-specific | Very high; WA health-data review | Yes |
| Charlotte actuator controller | Very high | Very high | Medium if powertrain/OBD/emissions affected | Product-specific | Medium-high | Very high |
| Ruby ECU programmer/tune | High classification/defect review | High | **Very high** | Product-specific | Medium | **Very high**, especially California |
| Home/forge Velvet node | Generally outside NHTSA | N/A | N/A | Product-specific | High | General state consumer/privacy law |

This is triage, not legal classification.

## 15. Eleanor U.S. requirement candidates

### US-PROD-001 — Safety Act classification record

Before U.S. sale/import/install, retain a dated classification memo stating whether the product is:

- motor vehicle equipment;
- subject to one or more direct FMVSS;
- replacement equipment;
- part of a vehicle alteration;
- or outside the identified NHTSA product path.

### US-INSTALL-001 — Installer-role declaration

Every U.S. installation procedure shall state whether it is intended for:

- owner DIY;
- independent repair shop;
- Velvet-authorized installer;
- dealer/distributor;
- pre-first-retail alterer.

The compliance assessment shall use the actual role.

### US-INSTALL-002 — Make-inoperative review

For any commercial installation, identify affected FMVSS-related safety functions/design elements and retain evidence that the installation does not knowingly render them inoperative.

### US-RECALL-001 — U.S. safety-defect readiness

For motor-vehicle equipment, maintain:

- traceable production/version identity;
- customer/distribution records as legally appropriate;
- field-incident intake;
- defect escalation;
- affected-population analysis;
- remedy planning;
- NHTSA reporting/recall workflow.

### US-COMMS-001 — Controlled manufacturer communications

Safety/service bulletins and broad field communications shall be versioned, retained and reviewed for applicable NHTSA submission duties.

### US-EPA-001 — Emissions/OBD boundary

No production feature shall intentionally bypass, defeat or render inoperative required emissions-control/OBD functions without documented legal/compliance basis for the exact product/use.

### US-EPA-002 — Contemporaneous emissions basis

Where a product affects an emissions-related element, preserve the engineering/compliance basis **before** manufacture/sale/installation where required.

### US-FCC-001 — Equipment authorization gate

No U.S.-market radio/digital configuration shall be marketed before the applicable FCC authorization path, labeling and integration obligations are resolved.

### US-PRIV-001 — Connected-data purpose map

For any U.S. connected service, document:

- data category;
- purpose;
- collection trigger;
- local/cloud location;
- retention;
- sharing;
- consent/choice;
- state-specific sensitivity.

### US-PRIV-002 — No hidden insurance/consumer-reporting reuse

Driver behaviour/location data collected for a Velvet user feature shall not silently become insurance, consumer-reporting or unrelated commercial data.

### US-WARR-001 — Repair-compatible warranty

Consumer warranty terms shall be reviewed for Magnuson-Moss/FTC anti-tying compliance and shall use cause-based exclusions rather than blanket third-party-repair prohibitions.

### US-OEM-ACCESS-001 — Lawful-modification scope record

Any circumvention/access-control work shall record:

- lawful ownership/access basis;
- diagnostic/repair/lawful-modification purpose;
- software/data actually accessed;
- other legal boundaries, including DOT/EPA;
- version/date of the applicable Section 1201 exemption.

### US-STATE-001 — State launch annex

No state shall be treated as covered merely because federal review is complete. Create a dated state annex before commercial installation, road testing or safety-relevant operation there.

## 16. What this changes in Velvet today

Again, very little changes in the manifesto.

The U.S. pass strengthens existing Velvet design choices:

- preserve OEM safety function unless a justified/validated change is made;
- keep owner DIY and business installation as distinct deployment modes;
- maintain exact hardware/software/build identity;
- keep passive observation separate from authority;
- treat field incidents and non-actions as receipts;
- local-first privacy reduces unnecessary business custody of data;
- Ruby diagnostics remain separate from emissions defeat;
- open/repairable hardware is compatible with a repair-friendly warranty strategy;
- lawful OEM access must remain separate from authority to violate safety/emissions law.

The main additions are commercial process:

- NHTSA classification memos;
- make-inoperative review;
- U.S. defect/recall readiness;
- emissions/OBD product gate;
- FCC gate;
- connected-data/state-privacy mapping;
- repair-compatible warranty review;
- state launch annexes.

## 17. Open questions before first U.S. launch

Resolve against the actual first product:

1. Is the product motor vehicle equipment under 49 U.S.C. 30102?
2. Does a direct FMVSS apply to the product?
3. Is Part 566 manufacturer identification required?
4. Is the product owner-installed or commercially installed?
5. Can installation affect an FMVSS-related design element?
6. Is Velvet involved before first retail sale of the vehicle?
7. What defect/recall record set must be maintained?
8. Does the product touch emissions calibration, OBD, catalyst/SCR/DPF/EGR/fuel/ignition logic?
9. Does the product use an intentional radio or digital oscillator subject to FCC rules?
10. What personal/location/voice/video/biometric/health-adjacent data crosses the vehicle boundary?
11. Which state(s) will the product be sold/installed/tested in?
12. Does Charlotte functionality trigger state AV testing/deployment rules?
13. What warranty is offered and is it repair-compatible?
14. Does any OEM access require reliance on a temporary Section 1201 exemption?
15. What insurance/product-liability programme applies to the exact product/service/install role?

## 18. Next linked pass

Recommended next pass:

> **Hardware/product manufacturing and quality-system baseline**

That should translate the regulatory archive into practical company machinery:

- product IDs/serials;
- BOM and supplier control;
- incoming inspection;
- change control;
- manufacturing test;
- calibration identity;
- nonconformance/CAPA;
- field incidents;
- service bulletins;
- recall readiness;
- traceability from shipped unit back to exact build evidence.

This would be the bridge from "standards-aware design" to "a company can repeatedly build and support the same thing."
