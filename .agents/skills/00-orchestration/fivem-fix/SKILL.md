---
name: fivem-fix
description: 'Run a root-cause-first FIX workflow for FiveM bugs. Use for errors, regressions, desync, NUI failures, event failures, entity issues, database problems, or performance regressions.'
---
# fivem-fix
## Purpose

Reproduce and isolate before patching. Prefer the smallest correction that fixes the root cause and add regression protection.
## Workflow
1. Capture exact symptom, logs, F8/server/NUI error, and reproduction steps when available.
2. Trace the failing path across UI/client/server/database/network boundaries.
3. Form a root-cause hypothesis and verify it against code or runtime evidence.
4. Implement a minimal patch that preserves unrelated behavior.
5. Add or update a regression test/check.
6. Verify resource restart, player reconnect, and ownership/state transitions when relevant.
7. Run security/performance review if the failure path is externally triggerable or hot.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not apply random defensive guards without explaining the root cause.
- Do not silence errors that should be handled.
- Do not broaden refactors during a bug fix unless required.

## Done criteria
- Root cause is identified.
- Regression is covered.
- Original reproduction no longer fails and adjacent paths still work.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
