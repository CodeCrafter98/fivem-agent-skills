# FiveM Agent Skills

A production-oriented, reusable Agent Skills pack for **FiveM development with CfxLua/Lua 5.4, OneSync, NUI/DUI, custom TypeScript UIs, databases, Qbox/QBCore/ESX, ox ecosystem, gameplay AI, security, performance, testing, and release engineering**.

**Version:** 1.0.0  
**Skills:** 43  
**Canonical format:** `.agents/skills/<skill>/SKILL.md`

## Why this pack exists

Generic "expert Lua developer" prompts are not enough for FiveM. Correct FiveM work depends on explicit client/server trust boundaries, GTA natives, OneSync ownership/scope, entity lifecycle, NUI callback behavior, framework semantics, and runtime performance. This pack separates those concerns into progressively loaded specialist skills.

## Architecture

```text
FiveM task
   ↓
fivem-router
   ↓
fivem-project-inspector (existing repos)
   ↓
minimum relevant specialist chain
   ↓
security / performance / testing / review as risk requires
```

The pack intentionally **does not load every skill on every task**.

## Skill groups

- `00-orchestration` — router, inspector, BUILD, FIX, AUDIT
- `01-core` — resource architecture, CfxLua, natives, client gameplay, server authority, events
- `02-networking` — OneSync, state bags, entity lifecycle, routing buckets
- `03-ui` — NUI, typed bridge, UI design, DUI, frontend stack
- `04-data-frameworks` — database, framework adapter, ox, Qbox, QBCore, ESX
- `05-game-systems` — vehicles, vehicle AI, peds AI, interactions, zones/raycasts, controls
- `06-quality` — security, performance, debugging, testing, code review, observability
- `07-production` — config/i18n, compatibility, release, documentation, packaging

See `references/routing-matrix.md` for signal → skill mapping.

## Installation

### Best option: project-local (recommended)

Copy this pack's `.agents/` directory and `AGENTS.md` into your FiveM repository, or run:

```bash
python /path/to/fivem-agent-skills/scripts/install.py --scope project --dest /path/to/your-fivem-repo
```

Project-local skills are versioned with the codebase and are available to remote/cloud agents that clone the repo.

### Global user installation

```bash
python scripts/install.py --scope global
```

This merges the FiveM skills into `~/.agents/skills` without deleting unrelated installed skills. Existing same-named skills are skipped unless `--force` is supplied. For an explicit Antigravity compatibility copy:

```bash
python scripts/install.py --scope global --antigravity-compat
```

Windows PowerShell:

```powershell
.\scripts\install.ps1 -Scope Project -Dest C:\path\to\repo
.\scripts\install.ps1 -Scope Global -AntigravityCompat
```

### Cursor

Current Cursor supports Agent Skills under `.agents/skills/`, `.cursor/skills/`, and compatible Claude/Codex skill locations. Prefer `.agents/skills/` so the repository remains portable.

### Google Antigravity

Current Antigravity workspace skills use `.agents/skills/<skill>/SKILL.md`; user-global skills can also live under `~/.gemini/config/skills/`. The installer supports both.

### Codex

Use the same `.agents/skills/` pack in the project (and `AGENTS.md` at the repository root). This avoids maintaining Codex-specific duplicates and keeps project skills visible to agents operating from the repo.

## Usage

You normally do **not** need to name specialist skills. Ask for the FiveM task. `fivem-router` is designed to select the smallest sufficient chain.

Explicit modes are also useful:

```text
BUILD a secure garage resource with a React NUI.
FIX this OneSync vehicle duplication bug after resource restart.
AUDIT this resource for exploits, resmon, networking, and NUI issues.
```

## FiveM baseline encoded by the pack

- Current CfxLua uses Lua 5.4; deprecated `lua54 'yes'` is not added.
- Client/NUI input is untrusted; valuable/shared state is server-authoritative.
- OneSync code accounts for scope and ownership migration.
- State bags are used for small replicated facts, not high-frequency nested databases.
- NUI callbacks always reply; UI communication uses explicit JSON contracts.
- Entity cleanup is designed for resource stop, disconnect, scope loss, and retries.
- Performance work is measurement-driven (`resmon`/profiler where possible).

## Deterministic helper scripts

Selected skills include small static scanners for project inventory, network attack-surface discovery, hot-path leads, and NUI contract discovery. They intentionally produce **leads, not conclusions**; the agent must inspect surrounding code and runtime evidence.

## Agent-specific adapters

`adapters/` contains optional Cursor, Antigravity, and Codex notes. The canonical skill source remains `.agents/skills/`; avoid maintaining divergent copies.

## Validation

```bash
python scripts/validate_skills.py
```

CI runs the same validator on pushes and pull requests.

## Evals

`evals/cases/` contains harness-neutral regression scenarios for routing, security, NUI, OneSync, AI vehicles, performance, framework portability, and release packaging. See `evals/README.md`.

## Templates

- `templates/resource-starter/` — clean modern FiveM Lua resource skeleton
- `templates/nui-bridge/` — Lua/TypeScript callback contract example
- `templates/framework-adapter/` — framework-neutral adapter guidance

## Maintenance

FiveM, frameworks, coding agents, and their skill discovery rules evolve. Refresh `references/official-sources.md`, update only affected skills, add an eval for every discovered recurring failure, and bump `VERSION` according to compatibility impact.

## License

MIT.
