---
name: fivem-router
description: 'Route FiveM development tasks to the minimum relevant specialist skills. Use for any FiveM resource work, feature, bug, audit, UI, networking, framework, database, gameplay, security, or performance task.'
---
# fivem-router
## Purpose

Act as the orchestration layer. Inspect the task and repository context, select the smallest sufficient skill chain, and prevent irrelevant skills from bloating context.
## Workflow
1. Classify the request as BUILD, FIX, AUDIT, REVIEW, or EXPLAIN.
2. Detect domains: resource architecture, Lua, natives, client/server, events, OneSync, state bags, entities, NUI/UI/DUI, database/framework, gameplay, security, performance, testing/release.
3. Load `fivem-project-inspector` first for non-trivial work in an existing repository.
4. Select only specialists with a concrete responsibility in the task.
5. For code changes, finish with security/performance/testing/code-review when materially relevant.
6. State assumptions only when they affect implementation; otherwise inspect instead of asking.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not activate every skill by default.
- Do not let framework-specific skills leak into standalone resources.
- Do not let UI specialists make server-authority decisions.
- Do not mark work complete without verification evidence.

## Done criteria
- Routing is minimal, complete, and justified.
- No critical specialist domain is omitted.
- The final chain includes validation appropriate to risk.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. See `references/routing-matrix.md` in this skill for signal-to-skill mapping. When documentation and installed project code disagree, target the installed version.
