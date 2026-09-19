# Manufacturing and Quality-System Baseline Snapshot — 2026-09-17 / MQS v0.1

**Record type:** Historical manufacturing/quality snapshot  
**Rewrite policy:** Immutable after merge except factual correction with explicit correction note.  
**Compliance claim:** None.

## Why this snapshot exists

This snapshot records the point where Velvet's standards work moved from regulatory/product qualification into repeatable manufacturing and field-support discipline.

At this date there is no released mass-production official Velvet board and no claim of ISO 9001 or IATF 16949 certification.

The purpose is to preserve what manufacturing discipline the project deliberately chose **before** commercial scale required it.

## Current external reference state

At this review date:

- ISO 9001:2026 was published on 2026-09-16 and replaced ISO 9001:2015.
- ISO 10012:2026 is the current measurement-management standard.
- ISO 19011:2026 is the current management-system auditing guideline.
- ISO 10007:2017 remains the current configuration-management guideline while a fourth edition is under development.
- IATF 16949:2016 remains the published automotive QMS standard.
- IATF announced in July 2026 that Revision 2 work is underway with planned mid-2027 publication, emphasizing simplification, software quality assurance, Tier-N supply-chain management, launch management and customer-specific requirements.
- IATF Rules 6th Edition has been effective since 2025-01-01 for the certification scheme.
- AIAG APQP 3rd Edition and Control Plan 1st Edition were released in 2024.
- AIAG continues to list PPAP 4th Edition as the current production-part-approval reference.
- IPC lists J-STD-001J / IPC-A-610J as current assembly/soldering revisions and IPC/WHMA-A-620E as the current harness-acceptability revision.

## Velvet manufacturing decisions recorded at this baseline

1. Quality discipline will be scaled to product consequence rather than copied wholesale from an OEM supplier.
2. ISO 9001 concepts are useful immediately; certification is not assumed necessary.
3. IATF 16949 is a future OEM/Tier/customer-requirement path, not the default direct-aftermarket business model.
4. Every sellable official product will have reproducible hardware/software/configuration identity.
5. No production unit should ship without a build/test record linked to serial/lot identity.
6. BOM substitutions that can affect function, safety, EMC, thermal behaviour, fit or qualification require engineering review.
7. The test fixture and manufacturing image are configuration-controlled products in their own right.
8. Formal qualification proves a design/configuration; production test verifies an individual unit.
9. Nonconforming material requires controlled disposition and cannot silently return to production.
10. Corrective action will be graded to consequence, with formal safety/systemic escalation when required.
11. Pilot/safe-launch controls will be used for initial production and major changes.
12. Returned safety-relevant units will preserve failure evidence before repair/reflash where practicable.
13. Recall readiness will be tested before safety-relevant commercial launch.
14. Electronics/harness workmanship will use explicit published acceptance criteria where appropriate.
15. Open-source/repairable product philosophy is retained; manufacturing quality does not require artificial lock-in.

## Historical significance

Future reviewers should be able to trace:

```text
DIY prototype
  -> standards/regulatory reviews
  -> 2026-09-17 manufacturing baseline
  -> first official product design
  -> pilot build
  -> qualification
  -> production release
  -> field history
  -> corrective actions / later revisions
```

Later certifications, customer-specific requirements, PPAPs, audits or manufacturing evidence shall not be represented as though they already existed at this baseline.
