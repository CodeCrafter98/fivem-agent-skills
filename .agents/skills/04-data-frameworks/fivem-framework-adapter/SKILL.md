---
name: fivem-framework-adapter
description: 'Keep FiveM resources portable across standalone, Qbox, QBCore, ESX, or custom frameworks using narrow adapter interfaces and capability detection.'
---
# fivem-framework-adapter
## Purpose

Separate domain/gameplay logic from framework-specific player, job, money, item, notification, and callback APIs.
## Workflow
1. Define a framework-neutral interface based on actual needed capabilities.
2. Keep detection/bootstrapping in one adapter layer.
3. Implement one adapter per supported framework.
4. Return normalized domain objects instead of leaking framework player objects.
5. Fail clearly when a required capability is unavailable.
6. Prefer optional integrations over hard dependencies when feasible.
7. Test the core with a fake/standalone adapter.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not branch `if ESX ... elseif QBCore ...` throughout domain code.
- Do not call deprecated compatibility APIs when native framework APIs exist.
- Do not pretend frameworks have identical transaction/identity semantics.

## Done criteria
- Core logic has no unnecessary framework imports.
- Adapters expose consistent capabilities.
- Unsupported combinations fail explicitly.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
