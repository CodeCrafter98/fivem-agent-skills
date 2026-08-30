# FiveM Agent Engineering Constitution

This repository uses a modular Agent Skills pack under `.agents/skills/`.

## Default behavior

1. For any non-trivial FiveM task, use `fivem-router` to select only the minimum relevant specialist skills.
2. In an existing project, inspect before editing with `fivem-project-inspector`.
3. Treat client/NUI input as untrusted; valuable/shared state is server-authoritative.
4. Target current CfxLua/Lua 5.4; never add deprecated `lua54 'yes'`.
5. Do not invent FiveM natives, framework APIs, exports, events, schema columns, or config.
6. Respect OneSync scope/ownership migration and explicit entity lifecycle cleanup.
7. Keep NUI contracts explicit; every callback returns on all paths; throttle high-frequency messages.
8. Prefer event-driven/adaptive work over unconditional `Wait(0)` loops.
9. Keep framework-specific behavior behind adapters when portability matters.
10. Finish code changes with verification proportional to risk: static checks, tests, restart/disconnect cases, security, performance, and review.

## Work modes

- BUILD: `fivem-build`
- FIX: `fivem-fix`
- AUDIT: `fivem-audit`

Do not load every skill. Progressive, task-specific context is a requirement of this pack.
