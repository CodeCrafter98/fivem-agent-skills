---
name: fivem-dui
description: 'Implement and review Direct-rendered UI (DUI) for in-world screens, terminals, vehicle displays, signs, TVs, and runtime textures.'
---
# fivem-dui
## Purpose

Use DUI when an interface must exist on a world surface, while managing browser/runtime-texture lifecycle carefully.
## Workflow
1. Confirm DUI is actually needed versus fullscreen NUI.
2. Create browser/DUI objects and runtime textures with explicit ownership.
3. Map the texture to the intended render target/material.
4. Define update/input strategy and interaction distance.
5. Throttle updates for offscreen/far-away displays.
6. Destroy DUI/runtime resources on teardown and resource stop.
7. Handle missing texture/model targets without leaking browser instances.

## Standalone safety

- Treat client/NUI input as untrusted. Security-sensitive state is server-authoritative.
- Never invent natives, framework APIs, events, exports, or schema. Verify against project code or official docs.
- Completion requires verification proportional to risk.

## Skill-specific guardrails
- Do not create one expensive DUI browser per entity without capacity analysis.
- Do not leave DUI handles alive after entity/resource destruction.
- Do not assume world-screen input maps automatically.

## Done criteria
- DUI lifecycle is bounded.
- Render/update cost is measured.
- Fallback behavior is defined.

## Output contract

When this skill materially affects a task, leave a concise implementation/review note covering: decisions made, files/contracts affected, risks checked, and verification performed. Do not dump the skill text into the user-facing answer.

## Reference policy

Prefer project source and authoritative documentation over memory for version-sensitive APIs. When documentation and installed project code disagree, target the installed version.
