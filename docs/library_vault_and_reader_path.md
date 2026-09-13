# Library, Vault, and Reader Path

This page records the current cross-repository path from offline source material to Velour's catalog and the Founder read-only Library Reader.

It is an implementation map, not a new authority path.

## Canonical Ownership

The public ownership boundary remains:

- `velours_library` owns the canonical provenance-aware knowledge archive, source lifecycle, retrieval evidence, portable packs, quarantine, and adoption;
- `velvet-interface` owns presentation of library state and read-only human interaction;
- private deployment/operator tooling may prepare or inspect local vault content, but it does not replace `velours_library` as the canonical knowledge owner;
- Runtime and Court remain the authority boundary for consequential action. Library content, a successful search, or a rendered page never creates authority.

> **Retrieval is not belief.**

> **Derived text is not the canonical source payload.**

The original local source remains the canonical retained object. Extracted text, indexes, previews, and rendered views are derived material for search and presentation.

## Current Merged Software Path

### Canonical library and catalog

`velours_library` remains the public knowledge organ. Its catalog and publication/retrieval contracts preserve provenance and source identity across lookup and reasoning.

The current Interface reader consumes the canonical on-disk catalog contract when it is available rather than importing Library implementation code directly.

The default catalog location beneath a configured vault root is:

```text
catalog/items.jsonl
```

A deployment may override the catalog location explicitly.

### Private Cyberdeck deployment tooling

The private `velvet-cyberdeck` repository currently carries bounded local operator/deployment tooling for files already stored in a Velvet vault. This is an implementation aid, not a new canonical knowledge organ.

Merged capabilities include:

- deterministic adapter selection;
- plain-text family handling, including text, Markdown, JSON, YAML, CSV, and log-like material;
- inert HTML/XHTML text extraction with active/script/style content excluded from extraction;
- bounded EPUB extraction following the declared package/spine rather than arbitrary ZIP member order;
- PDF text extraction through a local `pdftotext` helper when present, invoked directly without a shell;
- explicit unavailable/pending extraction state when a required local helper is absent;
- re-indexing of pending items after an adapter/helper becomes available, while refusing checksum-mismatched source payloads;
- ZIM recognition as a Kiwix-owned archive rather than flattening the archive into loose files;
- a local Kiwix serve plan that defaults to loopback and blocks external links unless explicitly changed;
- deterministic integrity manifests for complete downloaded website trees;
- read-only scan-first discovery for uncatalogued supported files already inside the vault;
- idempotent in-place batch cataloguing without copying the original vault payload a second time;
- partial-failure reporting so one bad file does not erase successful imports.

The Cyberdeck tools do not grant trust, belief, identity, Court authority, execution permission, or physical control.

## Downloaded Website Mirrors

A downloaded website is a directory tree, not just one HTML page.

The current website-bundle path records the exact local tree with:

```text
relative path + byte size + SHA-256
```

The records are sorted into a deterministic tree hash. The reserved manifest file is excluded from the payload hash so writing the manifest does not change the identity of the mirror it describes.

Verification distinguishes:

- changed files;
- missing files;
- unexpected files.

Symlinks are rejected instead of followed, hashing is streamed, and file-count/per-file/whole-tree limits bound the crawl.

A valid website manifest proves that the retained local bytes still match the recorded mirror. It does **not** prove that the site is truthful, current, safe, or authoritative.

WARC remains a separate future archival format. A normal mirrored directory should not be mislabeled as a WARC capture.

## ZIM and Kiwix

Large offline collections such as Wikipedia-style ZIM archives should stay ZIM archives.

The current tooling therefore treats ZIM as a dedicated local-reader handoff:

```text
verified catalogued ZIM
  -> local Kiwix plan
  -> loopback service by default
  -> Library Reader handoff
```

The default Kiwix plan is loopback-only and blocks external links. A LAN bind requires an explicit deployment decision. The library tooling plans the command; it does not silently start a daemon.

## Founder Library Reader

`velvet-interface` now contains a read-only, Scroll-backed Library Reader.

The scene uses the reusable `workspace_scroll.png` artwork as the Velvet workspace frame and a neutral inner document viewport for source content that needs its own page styling.

Current reader behavior includes:

- catalog-first browsing when `catalog/items.jsonl` is available;
- bounded filesystem preview as a bench/fallback path;
- shelf/search matching across title, path, collection, source, subjects, and tags;
- source metadata and extraction-state display;
- direct preview of text-family content;
- inert local HTML presentation with external-link opening disabled;
- explicit `PDF TEXT` / `EPUB TEXT` presentation when canonical derived text is available;
- ZIM recognition as a Kiwix handoff rather than pretending ZIM is an ordinary text document;
- rejection of catalog payloads or extracted-text paths that resolve outside the configured vault root;
- fail-closed access through the scene's supplied access provider.

The Interface does not mutate the source file or canonical catalog, execute scripts, open external links automatically, grant capability, or become a Court authority source.

## Vault Root Convention

The reusable Library Reader registration helper defaults to the service-facing convention:

```text
/srv/velvet
```

That is a software convention, not a requirement that the physical storage device be mounted there.

Deployments may use:

```text
VELVET_LIBRARY_ROOT
VELVET_LIBRARY_CATALOG
```

to bind the Interface to the installation's real local vault and catalog.

A removable disk may be mounted somewhere else and exposed to Velvet through an explicit bind/symlink/configuration choice. Documentation must not infer one installer's physical mount path from the service-facing default.

## Current Founder Integration Status

As of this documentation sync:

- the Library Reader scene is merged;
- the canonical catalog-aware preview provider is merged;
- the reusable registration helper is merged;
- the Scroll-backed UI and standalone preview launcher are merged;
- the final call that registers the Library Reader in the main Founder launcher remains follow-on work;
- the permanent Archive-room entry hotspot remains an on-device placement task and should be mapped from the real artwork/display rather than guessed in source code.

This distinction matters: **the reader exists, but the normal Founder navigation doorway is not yet complete.**

## Character Foundry Neighbor

The same reusable Scroll workspace is also used by the Character Foundry surface.

The public Interface now contains and registers the trusted Character Foundry scene in the Founder launcher. Its canonical candidate semantics and persistence remain behind the private Persona Continuity boundary. The Interface does not duplicate those semantics.

Character Foundry remains authority-free proposal tooling:

- no capability grant;
- no Court token;
- no automatic merge or deployment;
- no lineage certification;
- no canonical memory write;
- no actuation.

The permanent Forge-room hotspot remains an on-device placement task.

## Recommended Vault Workflow

The intended local workflow is:

```text
download or copy into staging / vault
  -> preserve original payload
  -> checksum / bundle verification where applicable
  -> read-only shelf scan
  -> review
  -> bounded catalog import in place
  -> extract/index derived text where supported
  -> retry pending extraction when helpers become available
  -> canonical catalog
  -> read-only Interface presentation
  -> retrieval evidence for reasoning
```

For unattended work, failure should remain visible and recoverable. The system should not delete originals, invent replacements, or silently convert an extraction failure into a successful shelf record.

## Remaining On-Device Validation

The merged software does not prove the complete Founder deployment.

Still requiring real-device evidence includes:

- the actual vault root/catalog binding on the Founder installation;
- presence and behavior of local PDF/Kiwix helpers on that host;
- real ZIM discovery and Kiwix browsing;
- batch scan/import against the actual vault tree;
- real downloaded-website mirror verification;
- full-screen Library Reader behavior at Founder resolution;
- final Founder launcher registration;
- Archive-room hotspot placement and navigation;
- removable-storage failure/recovery behavior under the real installation.

None of those remaining checks changes the public authority boundary.

## Compatibility Record Boundary

The September 2026 post-merge compatibility record in this repository is a frozen evidence record for the source composition it names.

The later Library Reader, Character Foundry Interface, and Cyberdeck library-tooling changes described here post-date that frozen acceptance composition. They must not be retroactively described as covered by the older compatibility manifest merely because their individual CI is green.

A future ecosystem compatibility record may pin and test a newer source composition without rewriting the historical record.
