<div align="center">

# FiveM Agent Skills

### Production-grade Agent Skills for AI-assisted FiveM development

**43 specialized skills · CfxLua · OneSync · NUI/DUI · Security · Performance · Qbox · QBCore · ESX**

A modular, reusable Agent Skills toolkit that gives modern AI coding agents deep FiveM-specific engineering knowledge — from resource architecture and Lua development to networking, custom UIs, framework integration, security auditing, performance optimization, testing, and production releases.

**Designed for Codex · Cursor · Google Antigravity · Agent Skills compatible tooling**

</div>

---

## Overview

FiveM development has engineering constraints that generic Lua or web-development prompts do not understand well enough.

A production-quality FiveM resource needs more than syntactically correct Lua.

It must account for:

* client/server trust boundaries
* FiveM and GTA natives
* CfxLua runtime behavior
* OneSync entity ownership and migration
* network IDs and replication
* state bags
* entity lifecycle management
* NUI and CEF behavior
* Lua ↔ frontend communication
* database consistency
* framework-specific APIs
* malicious client input
* resource restarts
* player disconnects
* runtime performance
* backwards compatibility

**FiveM Agent Skills turns these concerns into specialized, reusable skills that AI coding agents can load only when they are relevant.**

Instead of relying on a single oversized prompt such as:

> "You are an expert FiveM developer."

the toolkit provides focused engineering capabilities with explicit responsibilities, workflows, validation rules, and boundaries.

---

# Why FiveM Agent Skills?

General-purpose coding agents are increasingly capable, but FiveM combines several domains that require specialized context.

A seemingly simple feature may involve:

```text
Lua
+
GTA V natives
+
FiveM client runtime
+
FiveM server runtime
+
OneSync
+
network ownership
+
NUI / CEF
+
TypeScript
+
database persistence
+
framework APIs
+
security boundaries
```

Loading all of that guidance into every prompt would waste context and reduce agent focus.

FiveM Agent Skills instead uses **progressive disclosure**.

```text
User task
   │
   ▼
fivem-router
   │
   ▼
fivem-project-inspector
   │
   ▼
Minimum relevant specialist skills
   │
   ├── Architecture
   ├── Lua
   ├── Networking
   ├── UI
   ├── Framework
   ├── Gameplay
   └── Database
   │
   ▼
Security / Performance / Testing / Review
   │
   ▼
Verified implementation
```

The goal is simple:

> **Load the smallest sufficient set of expertise for the task.**

---

# Key Features

### 43 specialized FiveM skills

The toolkit covers the complete resource-development lifecycle across eight engineering domains.

### Intelligent skill routing

`fivem-router` determines which specialists are actually relevant instead of loading the complete skill library into every task.

### Existing-project awareness

`fivem-project-inspector` analyzes an existing repository before modifications are made.

It can identify:

* frameworks
* dependencies
* resource boundaries
* events
* exports
* NUI architecture
* database access
* coding conventions
* networking patterns
* potential risk areas

### Production-oriented workflows

Dedicated orchestration modes are included for:

```text
BUILD
FIX
AUDIT
```

### Security-first architecture

The toolkit assumes:

```text
Client input = untrusted
NUI input    = untrusted
Network data = untrusted

Server-owned state = authority
```

Security guidance covers authorization, economy abuse, forged events, entity spoofing, replay attacks, race conditions, SQL injection, exposed secrets, and other common attack surfaces.

### OneSync-aware networking

Dedicated skills cover:

* network IDs
* ownership
* ownership migration
* server-created entities
* scopes
* state bags
* routing buckets
* entity lockdown
* replication
* entity cleanup

### Modern custom UI development

The UI stack covers:

* FiveM NUI
* CEF
* TypeScript
* React / Vue / Svelte / Vanilla
* typed Lua ↔ frontend contracts
* NUI callbacks
* focus management
* DUI
* runtime textures
* responsive game UI
* UI performance
* premium FiveM UX patterns

### Framework portability

Framework-specific code can be isolated behind adapters instead of being spread throughout the resource.

Supported domains include:

* Standalone
* Qbox
* QBCore
* ESX
* ox ecosystem
* custom frameworks

### Performance-aware engineering

Guidance includes:

* `resmon`
* FiveM profiler
* hot loops
* native call frequency
* Lua allocations
* network event frequency
* state bag traffic
* entity churn
* database queries
* NUI message frequency
* frontend rendering

### Deterministic helper tools

Some skills include scripts that discover potential issues or architecture signals without relying exclusively on model reasoning.

### Regression evals

The repository includes evaluation scenarios for common FiveM engineering failures and routing decisions.

---

# Skill Architecture

The package currently contains **43 skills** grouped into eight domains.

## 00 — Orchestration

| Skill                     | Purpose                                              |
| ------------------------- | ---------------------------------------------------- |
| `fivem-router`            | Selects the minimum relevant skill chain             |
| `fivem-project-inspector` | Inspects existing FiveM projects before modification |
| `fivem-build`             | Production-minded workflow for new functionality     |
| `fivem-fix`               | Root-cause-first debugging workflow                  |
| `fivem-audit`             | Comprehensive resource audit                         |

---

## 01 — Core Engineering

| Skill                         | Purpose                                                   |
| ----------------------------- | --------------------------------------------------------- |
| `fivem-resource-architecture` | Resources, manifests, modules, dependencies and lifecycle |
| `fivem-cfxlua`                | Modern CfxLua / Lua 5.4 engineering                       |
| `fivem-native-expert`         | FiveM and GTA native selection and validation             |
| `fivem-client-gameplay`       | Client-side gameplay and presentation                     |
| `fivem-server-authority`      | Server-authoritative state and validation                 |
| `fivem-events`                | Event, callback and export architecture                   |

---

## 02 — Networking

| Skill                    | Purpose                                    |
| ------------------------ | ------------------------------------------ |
| `fivem-onesync`          | OneSync networking and ownership           |
| `fivem-statebags`        | Efficient replicated state                 |
| `fivem-entity-lifecycle` | Creation, ownership, migration and cleanup |
| `fivem-routing-buckets`  | Instances, buckets and lockdown policies   |

---

## 03 — UI & Frontend

| Skill                  | Purpose                                        |
| ---------------------- | ---------------------------------------------- |
| `fivem-nui`            | FiveM fullscreen NUI and CEF                   |
| `fivem-nui-bridge`     | Typed Lua ↔ frontend communication             |
| `fivem-ui-design`      | Premium game-first FiveM UI/UX                 |
| `fivem-dui`            | In-world browser surfaces and runtime textures |
| `fivem-frontend-stack` | TypeScript and frontend-framework engineering  |

---

## 04 — Data & Frameworks

| Skill                     | Purpose                                           |
| ------------------------- | ------------------------------------------------- |
| `fivem-database`          | Persistence, queries, transactions and migrations |
| `fivem-framework-adapter` | Framework-neutral resource architecture           |
| `fivem-ox-ecosystem`      | ox_lib, ox_target, ox_inventory and oxmysql       |
| `fivem-qbox`              | Qbox / QBX integration                            |
| `fivem-qbcore`            | QBCore integration                                |
| `fivem-esx`               | ESX integration                                   |

---

## 05 — Game Systems

| Skill                  | Purpose                                       |
| ---------------------- | --------------------------------------------- |
| `fivem-vehicles`       | Vehicle systems and persistence               |
| `fivem-vehicle-ai`     | Following, escort, convoy and driving AI      |
| `fivem-peds-ai`        | Ped behavior and task systems                 |
| `fivem-interactions`   | Targets, zones and interaction systems        |
| `fivem-zones-raycasts` | Spatial queries, raycasts and shape tests     |
| `fivem-input-controls` | Keyboard, controller and FiveM input handling |

---

## 06 — Quality Engineering

| Skill                 | Purpose                                       |
| --------------------- | --------------------------------------------- |
| `fivem-security`      | Security auditing and hardening               |
| `fivem-performance`   | Runtime and network performance               |
| `fivem-debugging`     | Systematic root-cause diagnosis               |
| `fivem-testing`       | Static, unit, integration and in-game testing |
| `fivem-code-review`   | Evidence-based engineering review             |
| `fivem-observability` | Logs, diagnostics, tracing and metrics        |

---

## 07 — Production

| Skill                       | Purpose                                         |
| --------------------------- | ----------------------------------------------- |
| `fivem-config-localization` | Configuration, locales and feature flags        |
| `fivem-compatibility`       | Runtime, framework and dependency compatibility |
| `fivem-release`             | Versioning and production releases              |
| `fivem-documentation`       | Developer and operator documentation            |
| `fivem-resource-packaging`  | Clean distributable resource packages           |

---

# Orchestration Modes

Three explicit workflows are available when you want to control the type of engineering process.

## BUILD

For new functionality.

```text
Understand
   ↓
Inspect
   ↓
Architect
   ↓
Define contracts
   ↓
Implement
   ↓
Secure
   ↓
Test
   ↓
Profile
   ↓
Review
```

Example:

```text
BUILD a secure vehicle garage with a React NUI, Qbox and oxmysql.
```

---

## FIX

For regressions and bugs.

```text
Reproduce
   ↓
Isolate
   ↓
Observe
   ↓
Trace
   ↓
Identify root cause
   ↓
Apply minimal patch
   ↓
Regression test
   ↓
Verify
```

Example:

```text
FIX this OneSync vehicle duplication issue after resource restart.
```

The goal is to avoid:

```text
error
↓
random patch
↓
new error
↓
random patch
```

---

## AUDIT

For existing resources.

```text
Architecture
Security
Networking
Entity lifecycle
Performance
Database
NUI
Framework integration
Compatibility
Testing
Release readiness
```

Example:

```text
AUDIT this resource for exploits, networking problems, resmon issues and unsafe NUI callbacks.
```

Findings should be classified by severity:

```text
BLOCKER
HIGH
MEDIUM
LOW
```

---

# Installation

## Recommended: project-local installation

Project-local installation is recommended because the skills become part of the repository and travel with the codebase.

Clone or download this repository, then run:

```bash
python scripts/install.py \
  --scope project \
  --dest /path/to/your-fivem-project
```

The installer places the skills into the target repository using the portable Agent Skills layout.

Typical result:

```text
your-fivem-project/
├── AGENTS.md
└── .agents/
    ├── AGENTS.md
    └── skills/
        ├── fivem-router/
        ├── fivem-cfxlua/
        ├── fivem-onesync/
        ├── fivem-nui/
        ├── fivem-security/
        └── ...
```

The installer intentionally flattens the source categories into individual skill directories for broad agent compatibility.

Existing unrelated skills are not deleted.

Existing same-named skills are skipped unless explicitly replaced using:

```bash
python scripts/install.py \
  --scope project \
  --dest /path/to/your-fivem-project \
  --force
```

---

## Global installation

Install the skills for all local projects:

```bash
python scripts/install.py --scope global
```

This installs the skill library into:

```text
~/.agents/skills/
```

---

## Google Antigravity compatibility

For an additional global Antigravity-compatible installation:

```bash
python scripts/install.py \
  --scope global \
  --antigravity-compat
```

---

## Windows PowerShell

Project installation:

```powershell
.\scripts\install.ps1 -Scope Project -Dest C:\path\to\your\fivem-project
```

Global installation:

```powershell
.\scripts\install.ps1 -Scope Global -AntigravityCompat
```

---

# Agent Compatibility

## OpenAI Codex

Recommended project scope:

```text
<project>/.agents/skills/
```

Recommended user scope:

```text
~/.agents/skills/
```

Codex can select skills automatically when the task matches a skill description or they can be invoked explicitly.

Using project-local skills is recommended for shared repositories and remote development environments.

---

## Cursor

Cursor supports project and user Agent Skills.

The portable project layout used by this toolkit is:

```text
<project>/.agents/skills/
```

Project-local installation is recommended when Cloud Agents or other remote environments need access to the same skills.

---

## Google Antigravity

Workspace skills can use:

```text
<project>/.agents/skills/
```

Global skills can use the Antigravity user skill location supported by the installer.

Antigravity uses skill metadata for progressive disclosure and loads the full skill instructions only when relevant.

---

## Other Agent Skills compatible tools

The individual skills follow the open `SKILL.md` model:

```text
skill-name/
├── SKILL.md
├── scripts/
├── references/
└── assets/
```

Compatibility with additional agents depends on their supported discovery paths and Agent Skills implementation.

---

# Usage

You normally do **not** need to manually name individual skills.

Describe the FiveM task naturally.

Example:

```text
Create a secure garage system with a modern React UI.
Vehicles should be loaded from the database and spawned server-authoritatively.
```

The routing system is designed to identify the relevant chain, such as:

```text
fivem-router
↓
fivem-project-inspector
↓
fivem-resource-architecture
↓
fivem-database
↓
fivem-nui
↓
fivem-nui-bridge
↓
fivem-ui-design
↓
fivem-vehicles
↓
fivem-server-authority
↓
fivem-security
↓
fivem-performance
↓
fivem-testing
```

A small UI adjustment should require substantially less context:

```text
fivem-router
↓
fivem-project-inspector
↓
fivem-ui-design
```

---

# Example Tasks

### Build a resource

```text
BUILD a production-ready police impound system using Qbox, oxmysql and a React NUI.
```

### Diagnose networking

```text
FIX vehicles disappearing or duplicating when network ownership changes.
```

### Security review

```text
AUDIT all RegisterNetEvent handlers and NUI callbacks for exploitable trust boundaries.
```

### Optimize performance

```text
Find the source of high idle resmon usage and optimize it without changing behavior.
```

### Vehicle AI

```text
Build a convoy system where AI vehicles follow a lead vehicle while maintaining realistic spacing and recovering from obstructions.
```

### Custom UI

```text
Create a premium motorsport-inspired vehicle management interface using TypeScript and React while keeping CEF rendering cost low.
```

---

# Engineering Principles

The toolkit encodes several core FiveM engineering principles.

## Server authority

Valuable or shared game state should be validated and mutated by trusted server logic.

Never trust client claims involving:

```text
money
items
permissions
job roles
prices
rewards
ownership
entity identity
coordinates
cooldowns
```

---

## Explicit trust boundaries

Treat these as untrusted inputs:

```text
NUI
↓
Client
↓
Network
↓
Server validation
```

---

## Network-safe entity handling

Avoid passing local entity handles across network boundaries.

Prefer:

```text
Network ID
+
server validation
+
entity existence checks
+
ownership-aware logic
```

---

## Lifecycle-aware systems

Entity systems must account for:

```text
creation
↓
networking
↓
ownership
↓
migration
↓
scope changes
↓
disconnect
↓
resource restart
↓
cleanup
```

---

## State bags are state, not databases

Use replicated state for small pieces of relevant synchronization data.

Avoid treating state bags as high-frequency nested object stores.

---

## Typed NUI communication

Prefer explicit request/response contracts between Lua and the frontend.

Example conceptual contract:

```text
garage:getVehicles
request  → {}
response → Vehicle[]

garage:spawnVehicle
request  → vehicleId
response → success | error
```

Every NUI callback must complete its response path.

---

## Measure performance

Do not declare code "optimized" based on appearance alone.

Inspect relevant evidence such as:

```text
resmon
profiler
event frequency
state replication
entity count
database query frequency
NUI message frequency
frontend renders
```

---

# Deterministic Helper Scripts

Some skills include small analysis tools.

They produce **investigation leads, not automatic conclusions**.

## Project inspection

```text
fivem-project-inspector/scripts/scan_project.py
```

Detects signals such as:

* manifests
* Lua files
* framework usage
* network events
* NUI callbacks
* NUI messages
* state bags
* hot-loop candidates

---

## Security attack surface

```text
fivem-security/scripts/scan_attack_surface.py
```

Surfaces potential network and UI entry points for manual review.

---

## Performance candidates

```text
fivem-performance/scripts/scan_hotpaths.py
```

Finds patterns that may deserve profiling, including:

* zero-wait loops
* threads
* high-frequency NUI messages
* replicated state writes

---

## NUI discovery

```text
fivem-nui-bridge/scripts/scan_nui.py
```

Maps NUI callbacks, frontend requests and Lua ↔ browser communication.

---

# Templates

Reusable starter templates are included under:

```text
templates/
```

## Resource starter

```text
templates/resource-starter/
```

Provides a clean modern FiveM resource foundation.

## NUI bridge

```text
templates/nui-bridge/
```

Provides an example typed Lua/TypeScript communication contract.

## Framework adapter

```text
templates/framework-adapter/
```

Provides guidance for keeping domain logic independent from Qbox, QBCore, ESX or custom framework APIs.

---

# Evals

The repository contains harness-neutral regression scenarios under:

```text
evals/cases/
```

Current evaluation domains include:

* insecure network events
* server authority
* NUI callback completion
* OneSync behavior
* state bag usage
* vehicle AI
* resource restart behavior
* framework portability
* performance
* release packaging

Evals are intended to answer an important question:

> Does the agent produce better FiveM engineering decisions with these skills than without them?

New recurring failure patterns should become new eval cases.

---

# Validation

Validate the complete skill library with:

```bash
python scripts/validate_skills.py
```

The repository also includes CI validation for pushes and pull requests.

Validation checks should ensure that skills remain structurally valid and discoverable.

---

# Repository Structure

```text
fivem-agent-skills/
│
├── .agents/
│   ├── AGENTS.md
│   └── skills/
│       ├── 00-orchestration/
│       ├── 01-core/
│       ├── 02-networking/
│       ├── 03-ui/
│       ├── 04-data-frameworks/
│       ├── 05-game-systems/
│       ├── 06-quality/
│       └── 07-production/
│
├── .github/
│   └── workflows/
│
├── adapters/
│   ├── antigravity/
│   ├── codex/
│   └── cursor/
│
├── evals/
│   └── cases/
│
├── references/
│
├── scripts/
│   ├── install.py
│   └── validate_skills.py
│
├── templates/
│   ├── framework-adapter/
│   ├── nui-bridge/
│   └── resource-starter/
│
├── AGENTS.md
├── LICENSE
├── README.md
├── VERSION
└── skills-manifest.json
```

The source tree groups skills by engineering domain for maintainability.

The installer deploys them into a flat skill-discovery layout where appropriate.

---

# Adding a New Skill

A new skill should solve a specific engineering problem rather than duplicate generic instructions.

Recommended structure:

```text
fivem-example-skill/
├── SKILL.md
├── references/
├── scripts/
└── assets/
```

At minimum, `SKILL.md` should contain valid metadata:

```yaml
---
name: fivem-example-skill
description: Clearly explain what this skill does and exactly when an agent should use it.
---
```

A good skill should define:

1. when it should trigger
2. when it should not trigger
3. its engineering responsibilities
4. its boundaries
5. required validation
6. expected outputs
7. relevant failure modes

Avoid giant catch-all skills.

If a new capability represents a distinct engineering concern, prefer a focused specialist and let `fivem-router` compose it with existing skills.

---

# Contributing

Contributions are welcome.

High-value contributions include:

* corrections to outdated FiveM behavior
* new regression evals
* improved security patterns
* improved OneSync guidance
* framework compatibility updates
* new deterministic analysis tools
* improved NUI patterns
* reproducible performance findings
* missing specialist skills

Before submitting changes:

```bash
python scripts/validate_skills.py
```

When fixing a recurring agent failure, consider adding an eval that reproduces the failure.

---

# Versioning

FiveM Agent Skills follows semantic versioning.

```text
MAJOR.MINOR.PATCH
```

### PATCH

Corrections and non-breaking skill improvements.

### MINOR

New skills, capabilities, templates or compatible workflows.

### MAJOR

Breaking structural changes or major compatibility changes.

Current release:

```text
v1.0.0
```

---

# Design Philosophy

FiveM Agent Skills is intentionally opinionated about engineering quality, but not about project architecture where multiple valid solutions exist.

The toolkit favors:

```text
understand before editing

root cause before patching

server authority before client trust

contracts before implicit behavior

measurement before optimization

lifecycle before happy-path spawning

framework adapters before lock-in

verification before completion
```

The objective is not to make AI agents write more code.

The objective is to make them produce **better FiveM engineering decisions**.

---

# Roadmap

Potential future areas include:

* additional framework adapters
* advanced voice/radio systems
* phone development patterns
* inventory architecture
* advanced dispatch systems
* large-server scaling patterns
* UI component recipes
* additional security evals
* multi-client integration harnesses
* automated compatibility testing
* broader Agent Skills ecosystem distribution
* plugin-based distribution for supported agent platforms

Contributions and real-world failure cases are especially valuable for deciding what should be added next.

---

# Disclaimer

FiveM Agent Skills is an independent open-source community project.

It is not affiliated with, endorsed by, or sponsored by Cfx.re, Rockstar Games, Take-Two Interactive, Qbox, QBCore, ESX, Overextended, OpenAI, Cursor, or Google.

Product names, project names and trademarks belong to their respective owners.

The toolkit provides development guidance and automation instructions. Generated code should still be reviewed and tested before use on production servers.

---

# License

Released under the **MIT License**.

See [LICENSE](LICENSE) for the full license text.

---

<div align="center">

### Build better FiveM resources with better agent context.

**FiveM Agent Skills**

</div>
