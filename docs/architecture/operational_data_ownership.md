# Operational Data Ownership

Data ownership begins at adapter design, before logs scatter across tools, nodes, and vendor services.

Every hardware adapter documents raw-data availability, normalized output, local retention, export format, replay support, vendor-cloud dependency, survival if the vendor disappears, ownership, inspection rights, local-model training permission, privacy constraints, and export receipts.

## Default posture

- local ownership and local retention
- no vendor-cloud requirement unless explicitly accepted
- raw capture optional but declared
- normalized capture and replay expected where technically practical
- privacy filtering before export
- exports are deliberate, scoped, and receipt-backed
- training use is separate from operational use and requires explicit permission

An adapter that cannot preserve useful data without its vendor must expose that dependency as a degraded survivability risk before promotion.
