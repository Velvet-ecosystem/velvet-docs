# Model Capability Adapter

Velvet organs depend on named capabilities, not vendor model names.

Initial capability names are `reasoning-small`, optional `reasoning-large`, `vision-local`, `code-review`, `speech-transcription`, `speech-synthesis`, `memory-summarizer`, `safety-classifier`, `document-parser`, and `local-embedding`.

Each capability declares preferred local engine, fallback engine, offline availability, cloud-permission requirement, maximum authority level, data-retention rule, receipt requirement, and refusal behavior.

## Rules

- Vendor and model names remain adapter configuration.
- Calling modules request a capability and constraints.
- Offline operation is preferred and must be truthful.
- Cloud fallback is unavailable unless the active policy explicitly grants it.
- Model output never becomes physical authority by itself.
- A missing or unsuitable engine returns a stable refusal, not a silent substitution.
- Engine selection and fallback use are receipt-backed when policy requires.
- Retirement of a hosted model changes adapter configuration, not every organ contract.
