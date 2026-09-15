# Founder Vault Deployment Snapshot

This page records the current **deployment snapshot** of the Founder-node Velvet Vault observed on the UP Squared system during September 2026.

It is deployment evidence and reconciliation guidance. It does not redefine the public ownership map, create a new authority path, or replace repository-specific contracts in `velvet-runtime`, `velours_library`, `velvet-interface`, `velvet-receipts`, or Continuity.

## Verified physical deployment

The Founder currently has a dedicated external ext4 volume labeled:

```text
VELVET_VAULT
```

The physical deployment mount observed on the UP Squared is:

```text
/mnt/velvet-vault
```

The initial validated deployment had more than 900 GB available. The filesystem was writable and remounted successfully after reboot.

The current top-level deployment tree includes:

```text
/mnt/velvet-vault/
├── archive/
├── backups/
├── datasets/
├── evidence/
├── library/
├── logs/
├── maps/
├── media/
├── models/
├── staging/
├── tools/
└── vehicle/
```

The physical path is an installation choice. It does not replace the public service-facing `/srv/velvet` convention.

## Velour library root

The current physical Library root is:

```text
/mnt/velvet-vault/library
```

It contains the deployment shelves required by the current `velours_library` implementation, including:

```text
archive/
catalog/
incoming/
indexes/
packs/
receipts/
external/zim/
```

Additional deployment-oriented shelves may coexist for curation, imports, canonical project references, research material, repository snapshots, timelines, recovery, and quarantine. Their presence does not create additional canonical knowledge owners.

`velours_library` remains the canonical provenance-aware knowledge organ.

## Kiwix / ZIM shelf

Large offline website archives are retained as ZIM files under:

```text
/mnt/velvet-vault/library/external/zim/
```

This matches the `velours_library` contract that large ZIM archives remain on the external Kiwix shelf instead of being duplicated into the bounded per-document canonical archive.

The Founder deployment has begun populating this shelf with offline reference collections. This proves storage and acquisition activity only. It does **not** yet prove final `velour-zim` inventory, Kiwix serving, search behavior, Interface handoff, or long-running removable-storage recovery.

The intended deployment-side acceptance remains:

```text
velour-zim --root /mnt/velvet-vault/library init
velour-zim --root /mnt/velvet-vault/library status
velour-zim --root /mnt/velvet-vault/library inventory
```

A later explicit integrity pass may use `inventory --hash`; hashing very large ZIM collections is intentionally not automatic.

## Filesystem identity boundary

Current Runtime and Library contracts do not treat a directory path, capacity, filesystem label, marker file, or successful `statvfs()` call as removable-device identity.

Attached storage must be bound to an explicitly configured expected filesystem UUID. The real deployment UUID is local configuration and should not be hard-coded into public repository defaults or inferred automatically.

The Founder deployment therefore distinguishes:

```text
physical mount path
  != filesystem identity
  != knowledge trust
  != Runtime/Court authority
```

The current physical vault has been identified and mounted successfully at the OS level. Runtime and Library UUID-bound acceptance still require local configuration and negative-path testing against wrong/missing storage before that software boundary can be called deployment-accepted.

## Service-facing path versus physical mount

Public software documentation commonly uses `/srv/velvet` as a service-facing deployment convention.

The Founder currently uses `/mnt/velvet-vault` as the physical mount. Components may be pointed at the physical path directly through documented configuration or exposed through an explicit service-facing bind/configuration layer.

Documentation must not silently rewrite one path into the other or assume that a directory existing at `/srv/velvet` proves the expected removable filesystem is present.

## Receipt boundary

The deployment currently keeps two intentionally different receipt/evidence areas:

```text
/mnt/velvet-vault/library/receipts/
/mnt/velvet-vault/evidence/receipts/
```

`library/receipts/` is Library-local audit/provenance material produced by knowledge workflows. It must not be confused with canonical ecosystem execution/evidence receipts.

The top-level `evidence/` tree is the deployment area reserved for broader Velvet evidence such as canonical receipts, continuity records, manifests, and security/audit records.

A path name alone grants no trust or authority. Repository contracts remain authoritative about the meaning of the records stored there.

## Local operational records

The current deployment also maintains local operational helpers and status records, including:

```text
VAULT_INFO.txt
.vault-layout-version
vault-policy.json
vault-status.json
tools/vault-health.sh
tools/vault-manifest.sh
tools/vault-status.sh
backups/manifests/
```

These are deployment/operator records. They do not replace Runtime filesystem-identity verification, Library provenance, canonical Receipts, or Continuity.

## Current acceptance state

Observed and verified on the Founder deployment:

- the external ext4 vault mounts at the intended physical path;
- the filesystem is writable;
- the mount survives reboot through the configured system mount path;
- the broad vault and Library directory trees exist;
- local health/status/layout manifest tooling runs;
- the external ZIM shelf exists and has been populated with offline reference material.

Still requiring explicit on-device acceptance:

- Runtime `expected_filesystem_uuid` configuration and withdrawal/recovery behavior;
- matching Library vault filesystem-identity configuration;
- wrong-volume and missing-volume negative-path tests;
- `velour-zim` status/inventory against the real shelf;
- local `kiwix-serve` availability and loopback serving;
- catalog scan/ingestion against the real Library tree;
- Interface binding to the real Library root/catalog;
- removable-volume disconnect/reconnect recovery;
- complete Founder Library Reader navigation and Archive-room hotspot validation.

## Authority statement

The Vault is storage. Velour's Library turns approved local material into provenance-aware knowledge. Retrieval remains evidence for reasoning, not belief, permission, or physical authority.

A mounted drive, successful download, valid checksum, searchable ZIM, published Library item, or rendered Interface page must never reach around Runtime/Court to authorize consequential action.
