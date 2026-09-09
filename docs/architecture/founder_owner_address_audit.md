# Founder / Owner / Address Boundary Audit

Status: audit-only draft. No production behavior change.

Date: 2026-09-08

## Purpose

This audit maps where Founder-specific human relationship data is currently mixed with public Velvet architecture, and defines a safe future migration that removes Founder-House personalization from public defaults **without resetting established Founder-House continuity**.

The immediate goal is not to change code. It is to establish the compatibility boundary before any later Core, Runtime, Interface, Persona, or Riven implementation work.

## Architectural rule

> Remove Founder-House personalization from public defaults without resetting established Founder-House continuity.

For the current Founder deployment, the established local relationship should remain available as deployment/profile state, including the existing preferred address `Mister`, provided the existing trusted profile and continuity records can be migrated safely.

A new downstream installation must not inherit `Mister` as the unknown user's default identity or title.

## Concepts that must remain separate

The current architecture already contains most of the required separation. Future work should preserve these as distinct concepts:

1. **Velvet system identity**: who Velvet is.
2. **Human principal identity**: which human a record refers to.
3. **Profile**: the human's role/context in a deployment, such as owner, driver, guest, technician, or emergency helper.
4. **Relationship class**: how Velvet relates to that human, such as primary owner or household member. This is descriptive relationship state, not a Court grant.
5. **Display name**: a presentation label for the person.
6. **Preferred address**: how Velvet should address the person, such as `Mister`.
7. **Pronunciation / contextual address**: optional presentation metadata.
8. **Verification state**: whether the current session identity claim has been verified.
9. **Physical presence**: whether the human is physically present.
10. **Authority profile / capability context**: Runtime policy selection and governed authorization inputs.
11. **Court authority**: actual action authority. None of the naming or relationship fields above grant this by themselves.

## Findings

### F-01: AI Core currently embeds Founder-specific address data inside constitutional Self

Repository: `velvet-ai-core`

File: `velvet/core/native_brain/self_orientation.py`

Current `SelfIdentity` contains:

```text
name = Velvet
body_model = unified-organ
owner_title = Mister
```

`owner_title` is also included in `SelfIdentity.fingerprint()` and exposed in `SelfOrientation.summary()`.

Impact:

- `Mister` is currently a public Core default rather than deployment relationship state.
- Because `owner_title` participates in the identity fingerprint, deleting or changing it can look like constitutional identity drift to `NoDriftIntegrityGate`.
- A future migration cannot safely be a simple field deletion or text replacement.

Classification: **production public-default coupling / migration-sensitive**.

Required future treatment: versioned Core compatibility migration. Move human relationship/address context out of constitutional Self while preserving continuity/no-drift meaning across the transition.

### F-02: Runtime already has the correct profile/session boundary

Repository: `velvet-runtime`

Files:

- `services/profile_binding.py`
- `docs/profile_session_binding.md`

`ProfileBinding` already separates:

- `profile_id`
- `profile_type`
- `display_name`
- `address_preference`
- `authority_profile`

`SessionBinding` separately carries:

- `session_id`
- selected profile
- `verification_state`
- `physical_presence`
- `owner_verified`

Owner verification requires a valid active owner profile, a verified session, and physical presence. Unknown, claimed, or unverified profiles fall back to the active guest profile.

The Runtime documentation explicitly states that a name, address preference, hidden scene, or wake phrase grants no authority.

Classification: **good existing foundation**.

Required future treatment: extend rather than replace this model.

### F-03: Runtime public example config embeds Founder-specific data

Repository: `velvet-runtime`

File: `config/profile_registry.example.json`

The public example currently defines:

```text
profile_id: primary_owner
profile_type: owner
display_name: Mister
address_preference: Mister
authority_profile: owner_present
```

Impact:

- the example correctly demonstrates the existing schema;
- however, downstream builders may copy it and unintentionally inherit Founder-House presentation data.

Classification: **public example leakage, not live proof of a deployment**.

Required future treatment: after a compatible migration exists, replace the public example with neutral placeholder data while preserving the real Founder deployment's local profile state.

### F-04: Runtime already propagates address preference into continuity context

Repository: `velvet-runtime`

File: `services/continuity_activation.py`

Continuity receipts are enriched with profile and session context, including `profile_id`, `profile_type`, `address_preference`, session verification state, physical presence, and `owner_verified`.

Impact:

- a future UI/Core consumer does not need to invent another owner-title source;
- the existing verified Runtime context is already the natural source for deployment-specific address presentation.

Classification: **existing migration path**.

Required future treatment: preserve receipt/provenance semantics while exposing only the presentation-safe fields needed by consumers.

### F-05: Runtime normalizes profile text to lowercase

Repository: `velvet-runtime`

File: `services/profile_binding.py`

The helper used to load profile text currently normalizes whitespace and lowercases all required text, including `display_name` and `address_preference`.

Impact:

- comparison/normalization is deterministic;
- but presentation capitalization is lost, so `Mister` becomes `mister` in the loaded binding.

Classification: **presentation/normalization gap**.

Required future treatment: preserve a case-retaining display value separately from normalized comparison keys. Do not use presentation casing as authentication material.

### F-06: A stable principal-reference concept already exists in contactless verification

Repository: `velvet-runtime`

Files:

- `services/contactless_token_registry.py`
- `services/contactless_token_adapter.py`
- `docs/founder_contactless_token_adapter.md`

Contactless records already distinguish:

- pseudonymous `principal_ref`
- human-readable `label`
- `role_hint`
- token evidence

The current documentation correctly states that `principal_ref` and `role_hint` are claims/evidence for later multi-factor evaluation, not Court grants.

Classification: **useful existing identity-reference concept**.

Required future treatment: evaluate whether profile records should reference a stable human/principal identifier rather than using profile IDs or names as the only durable human referent. Do not make the contactless registry the owner of human identity.

### F-07: Interface contains live Founder-specific presentation literals

Repository: `velvet-interface`

Files:

- `velvet_interface/boot_status.py`
- `velvet_interface/surfaces/pyqt/written_conversation_widget.py`

Current production presentation contains literal Founder text:

```text
Waiting for Mister
Mister> <written turn>
```

Impact:

- current Founder UI works as intended;
- public deployment presentation is not yet profile-derived.

Classification: **production presentation coupling**.

Required future treatment: once the compatible Runtime/Core boundary is available, inject a verified/profile-derived address label. If no suitable verified presentation context exists, use a neutral fallback such as `Waiting for user` / `You>` rather than guessing the owner.

### F-08: Historical Founder validation records should remain historical

Repositories include `velvet-runtime`, `velvet-interface`, `velvet-ai-core`, `velvet-docs`, and several deployment/experimental repos.

Many runbooks and validation snapshots record the real Founder posture:

```text
Interface: Waiting for Mister
```

Other documentation names Mister when describing actual Founder tests, approval history, or project lineage.

Classification: **historical/deployment record**.

Required future treatment: preserve these records. They are evidence of what the Founder deployment actually did and should not be rewritten into generic language merely to make current public defaults neutral.

### F-09: Public doctrine already says address preference is not authority

Repository: `velvet-ai-core`

File: `docs/naming_and_binding.md`

Current doctrine already separates system identity, instance name, surface, body, human address preference, and authority binding. It explicitly states that address preference is personalization rather than proof of authority and lists owner, driver, maintenance, guest, passenger, technician, and emergency-helper profiles.

Classification: **correct doctrine already present**.

Required future treatment: implementation should be brought into alignment with this existing doctrine rather than rewriting the doctrine.

### F-10: Owner/guest continuity doctrine already protects the relationship boundary

Repository: `velvet-docs`

File: `docs/research/persistent_self_owner_guest_lineage.md`

The recovered doctrine says owner and guest separation affects forms of address, disclosure, personal-memory access, interface paths, conversational familiarity, and approval expectations, but a claimed owner label in conversation is not owner verification.

Classification: **correct continuity doctrine already present**.

Required future treatment: preserve this distinction during migration.

## Founder-specific references that do not all mean the same thing

A global search for `Mister` returns several classes that must not be treated as one cleanup task:

| Class | Example | Future posture |
| --- | --- | --- |
| Public production default | Core `SelfIdentity.owner_title` | migrate |
| Public production presentation | Interface `Waiting for Mister`, `Mister>` | profile-drive later |
| Public example config | Runtime profile example | neutralize later |
| Runtime tests/fixtures | profile and continuity tests | generalize where appropriate after migration |
| Founder validation/runbooks | verified boot and UP² records | preserve history |
| Founder relationship/persona material | Velour relationship wording | preserve in Founder/private overlay unless intentionally generalized |
| Historical approval/provenance | docs that say Mister approved/reviewed | preserve history |
| Generic safety example | `Mister said yes last month` is not authority | may remain as an example, though generic wording is optional |

## Missing/under-specified fields for the long-term human relationship model

The present Runtime profile schema is strong but does not yet explicitly model all of the desired human relationship data.

Potential future fields, subject to separate contract review:

```text
principal_ref              stable human/principal reference
display_name               case-preserving presentation name
address_preference         case-preserving preferred form of address
relationship_class         e.g. primary_owner, household_member, guest
pronunciation              optional presentation metadata
contextual_addresses       optional context-specific address choices
profile_type               owner / driver / guest / technician / etc.
authority_profile          Runtime policy selector, separate from relationship
status                     active / disabled / retired
```

`relationship_class`, names, titles, pronunciation, and contextual addresses must remain authority-neutral.

## Proposed future migration sequence

This sequence is intentionally **not implemented by this audit**.

### Stage 1: Freeze compatibility expectations

Before changing Core or Runtime, add tests/contracts proving:

- a brand-new installation does not inherit `Mister`;
- an existing Founder profile retains `Mister` after migration;
- a claimed name/title never grants owner status;
- owner verification remains verified-profile + verified-session + physical-presence based;
- guest fallback remains fail-closed;
- changing an address preference does not change authority.

### Stage 2: Introduce stable, case-preserving human presentation state

Extend Runtime/profile contracts so normalized comparison values and case-preserving display/address values are not accidentally the same field representation.

If a stable `principal_ref` is introduced into the profile registry, it should reference human identity without becoming an authority token.

### Stage 3: Migrate the existing Founder deployment in place

For an already verified Founder deployment:

- preserve the existing owner/profile relationship;
- preserve `Mister` as the preferred address;
- preserve existing continuity/receipts;
- do **not** force first-time enrollment merely because public defaults are being cleaned up;
- require normal governed enrollment only if privileged identity binding cannot actually be proven from existing trusted state.

The migration must be idempotent and receipted where it changes persistent binding records.

### Stage 4: Decouple Core Self from human address preference

Move Founder/user relationship presentation out of `SelfIdentity`.

Because `owner_title` currently contributes to the Self fingerprint, this requires an explicit fingerprint/no-drift compatibility transition. A later implementation must define how old fingerprints remain recognizable across the schema change instead of making every existing Founder deployment appear to have identity drifted.

Core may consume verified relationship/address context for reasoning or expression, but that context should not become constitutional Velvet identity or authority.

### Stage 5: Move Interface presentation to verified profile context

Replace production literals such as `Waiting for Mister` and `Mister>` with presentation derived from the active verified/profile context.

Fallback must be neutral when no appropriate address preference is available.

### Stage 6: Neutralize public examples and new-install defaults

Only after the compatibility path exists:

- change public example owner names/titles to neutral placeholders;
- ensure new install/enrollment asks the human how they want to be addressed;
- store that preference locally;
- keep security enrollment and presentation preference as separate operations.

### Stage 7: Preserve historical Founder records

Do not rewrite old validation logs, runbooks, receipts, or historical project records simply because new defaults become deployment-neutral.

History is evidence, not a template.

## Acceptance tests for the eventual implementation

A later implementation should not be accepted unless it proves all of the following:

1. Fresh install does not assume the user is Mister.
2. Existing Founder deployment still addresses the established owner as Mister after migration.
3. Founder does not have to repeat first-time setup solely because the public default changed.
4. Owner verification requirements are unchanged or strengthened, never weakened.
5. A spoken/typed claim such as `I am Mister` or `I am the owner` grants nothing by itself.
6. Address preference can change without changing Velvet's constitutional identity fingerprint.
7. Address preference can change without changing capability/Court authority.
8. Guest fallback never inherits Founder relationship state or private address context accidentally.
9. Case-preserving presentation survives normalization needed for comparison/security logic.
10. Interface uses verified/profile-derived presentation or a neutral fallback.
11. Existing historical Founder records remain unchanged.
12. Migration is idempotent and does not silently create duplicate owner/principal records.
13. Riven lineage remains Velvet lineage; human address preference is not repurposed as lineage proof.
14. Tests distinguish human identity, profile, relationship, presentation, verification, physical presence, authority profile, and Court authority.

## Non-goals for this branch

This audit branch does not:

- edit `SelfIdentity`;
- change the No-Drift fingerprint;
- alter Runtime profile or session schemas;
- alter the Founder profile registry;
- change NFC/contactless identity mapping;
- alter Interface strings;
- change owner/guest behavior;
- enroll or re-enroll any human;
- alter Riven lineage;
- alter Court or capability policy;
- modify Astra repair branches;
- merge anything to `main`.

## Recommended ownership for later implementation

- **AI Core**: remove human address preference from constitutional Self using an explicit compatibility migration.
- **Runtime**: canonical active profile/session/principal relationship context, presentation-safe address data, verification and physical-presence binding.
- **Riven / Continuity Spine**: record lineage-worthy migration events only; do not own address preference.
- **Receipts**: persist governed binding/profile migration outcomes where required.
- **Persona Continuity**: consume relationship context within scope; do not grant authority from familiarity.
- **Language**: express the selected address appropriately.
- **Interface**: display verified/profile-derived address labels.
- **Docs**: preserve historical Founder evidence and document public/deployment separation.

## Stop line

Do not implement the migration from this document while the current Astra repair sequence is still open. Rebase/reconcile after the repair baseline is accepted, then open narrowly scoped implementation branches in dependency order.
