---
name: fivem-observability
description: 'Add practical FiveM observability: structured logs, debug modes, metrics/counters, event tracing, correlation IDs, diagnostics commands, and privacy-conscious telemetry.'
---
# fivem-observability
## Purpose

Make production issues diagnosable without flooding console or leaking sensitive player data.
## Workflow
1. Define log levels and a config-gated debug mode.
2. Add structured context: resource/module/action/source/entity/request ID.
3. Correlate NUI/client/server requests where debugging cross-boundary flows.
4. Count/rate important events and denials for abuse/performance diagnosis.
5. Provide admin/debug commands for state snapshots when useful.
6. Redact tokens, secrets, and unnecessary personal data.
7. Avoid per-frame logging.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not log secrets or full sensitive identifiers unnecessarily.
- Do not turn debug logging on permanently by default.
- Do not spam high-frequency logs without sampling/rate limits.

## Done criteria
- Errors are traceable across boundaries.
- Production logging volume is bounded.
- Sensitive data is minimized.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
