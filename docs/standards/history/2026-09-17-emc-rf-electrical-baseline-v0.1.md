# EMC / RF / Automotive Electrical Baseline Snapshot — 2026-09-17 / v0.1

**Record type:** Historical qualification snapshot  
**Rewrite policy:** Immutable after merge except factual correction with explicit correction note.  
**Compliance claim:** None.

## Why this snapshot exists

This snapshot records Velvet's first dedicated EMC, RF and automotive electrical qualification pass before an official sellable Velvet vehicle board has been finalized.

The purpose is to show that qualification concerns were incorporated into the hardware-product process before commercialization rather than added only after a failed regulatory or customer test.

## Standards/current-state observations

At this review date:

- UNECE lists UN Regulation No. 10 Revision 6 with Amendments 1 through 4.
- CISPR 25:2021 is the current IEC publication for protection of on-board receivers from vehicle/component radio disturbances.
- ISO 11452-2:2019 remains published while a fourth edition is under development.
- ISO 7637-2:2011 remains current after confirmation in 2025, with an amendment under development.
- ISO 7637-3:2016 remains current.
- ISO 10605:2023 is current and was confirmed in 2025, with an amendment under development.
- ISO 16750-2/3/4/5 have 2023 editions relevant to electrical/environmental robustness.
- ISO 11898-2:2026 was published in May 2026 and is the current high-speed CAN physical-layer edition.
- Canada uses ICES-003 Issue 7 for applicable digital apparatus and RSS-Gen Issue 6 (2026) as the current general radio-apparatus specification; RSS-247 Issue 4 (2025) covers common licence-exempt WLAN/digital-transmission bands.

## Velvet decisions recorded at this baseline

Before official-board production:

1. EMC/electrical qualification will be considered from PCB revision zero.
2. Harness, connector, enclosure, ground and antenna configuration are part of the qualified product, not afterthoughts.
3. Controlled BOM identity will include EMC-critical parts.
4. Power disturbance shall never create new physical authority.
5. Reset/recovery shall return safety-relevant outputs to defined safe/inactive/degraded states until normal authority is re-established.
6. Cheap pre-compliance screening will be used to find ordinary mistakes, but will not be represented as formal certification.
7. High-energy transient/immunity tests requiring specialized equipment will use suitable commercial equipment or competent labs rather than improvised destructive setups.
8. Radio-module certification will not be treated as blanket approval of the host product.
9. The current CAN physical-layer standard will be checked at each official-board release rather than frozen indefinitely.
10. Formal evidence will be linked to exact hardware/software/BOM/harness configuration.

## Historical purpose

Future product reviews should be able to distinguish:

```text
prototype hardware habits
  -> 2026-09-17 qualification baseline
  -> first official-board design
  -> pre-compliance evidence
  -> formal qualification
  -> production revision
  -> field evidence
```

No later formal test result should be backdated or implied to have existed at this baseline.
