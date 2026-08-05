# Internal GitHub Action Pinning Policy

Workflow reuse must execute the code intended for the commit under test.

## Same-repository reuse

Prefer relative reusable-workflow references such as `./.github/workflows/example.yml` when the caller and called workflow are in the same repository. GitHub resolves that form from the same commit as the caller. Local composite actions may use repository-relative paths after checkout and must be covered by the same commit review.

## Cross-repository and external reuse

- Pin external actions and reusable workflows to a full commit SHA.
- Record the human-readable release tag in a comment or dependency record.
- Treat organization-internal cross-repository reuse as a dependency and pin it unless an explicitly reviewed release channel says otherwise.
- Never replace a SHA with a floating default branch for convenience.

## Compatibility record

Track runner type and version, minimum supported runner version, internal action or workflow path, resolution mode, fallback behavior, permissions, and whether the dependency is local, organization-internal, or external.

Self-hosted runners must remain current enough to support the workflow features they execute. A runner compatibility failure blocks the workflow; it does not justify falling back to unpinned code.
