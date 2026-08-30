---
name: fivem-frontend-stack
description: 'Engineer modern FiveM NUI frontends with TypeScript and an appropriate framework/build tool while controlling bundle size, render frequency, state, accessibility, and CEF compatibility.'
---
# fivem-frontend-stack
## Purpose

Choose React/Vue/Svelte/vanilla based on UI complexity, not habit, and ship a compact production build compatible with FiveM CEF.
## Workflow
1. Prefer TypeScript for non-trivial UI contracts.
2. Keep framework-independent NUI transport in a small module.
3. Use local component state for ephemeral UI and a store only when shared state warrants it.
4. Avoid SSR/server-only assumptions; NUI is a client-side embedded browser.
5. Code-split only when it meaningfully improves load/cost.
6. Use transform/opacity animations where possible.
7. Build to a deterministic directory declared by the resource manifest.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not add a full framework for a tiny static HUD without reason.
- Do not depend on browser APIs unavailable in target CEF without verification.
- Do not ship source maps/secrets unintentionally.

## Done criteria
- Production build is reproducible.
- Bundle/runtime cost is reasonable.
- Transport, state, and presentation are separated.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
