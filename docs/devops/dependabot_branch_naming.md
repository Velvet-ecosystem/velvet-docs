# Dependabot Branch Naming

Velvet uses predictable dependency-update branch names so CI rules, webhook filters, and Velour's archive indexing remain stable.

Preferred visible pattern:

```text
dependabot/<ecosystem>/<package>
```

Examples include `dependabot/pip/requests`, `dependabot/github_actions/actions-checkout`, and `dependabot/npm/vite`.

GitHub owns the `dependabot/` prefix and generated package spelling. Configure `pull-request-branch-name.separator: "/"` where an explicit separator is useful. Repository automation must match the actual generated convention rather than rewriting branches after creation.

Use lowercase where the ecosystem permits it, avoid custom random suffixes, and document any CI or webhook exception. Stable names improve cataloging but do not replace dependency verification or SHA pinning.
