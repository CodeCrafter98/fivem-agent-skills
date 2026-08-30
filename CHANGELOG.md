# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.1] - 2026-08-30

### Fixed
- **YAML Parser Compatibility**: Quoted all YAML frontmatter descriptions to fix a strict parsing bug that caused `skills.sh` to only discover 35 of 43 skills.
- **Portable References**: Fixed broken `references/official-sources.md` path in all skills when installed standalone. Replaced with domain-specific reference files that travel with each skill.
- **NUI Contract**: Hardened `nuiFetch` in the `nui-bridge` template to properly catch and normalize timeout, network, HTTP, and JSON parse errors instead of leaking exceptions.
- **Context Duplication**: Replaced the duplicated 900-byte "Non-negotiable engineering rules" block in all 43 skills with a compact "Standalone safety" section, reducing total skill byte size by ~39%.

### Added
- **Expanded Validator**: `scripts/validate_skills.py` now checks structural integrity, manifest consistency, version matching, portable references, Python syntax, and eval schemas.
- **Installer Improvements**: `install.py` and `install.ps1` now support `--dry-run`, `--verify`, and generate a `.agents/fivem-agent-skills.json` installation receipt.
- **Community Files**: Added `CONTRIBUTING.md`, `SECURITY.md`, and issue/PR templates.
- **CI Enhancements**: Added installer smoke tests for both Linux and Windows environments.

## [1.0.0] - 2026-08-15

### Added
- Initial release of FiveM Agent Skills.
- 43 specialized skills across 8 engineering domains.
- `fivem-router` for progressive disclosure of expertise.
- `fivem-project-inspector` for existing repository analysis.
- Orchestration modes: BUILD, FIX, AUDIT.
- Security-first and OneSync-aware engineering constraints.
- NUI, database, and framework (Qbox, QBCore, ESX) integration guidance.
- Deterministic helper scripts for project, UI, performance, and security scanning.
- Python and PowerShell installer scripts.
- Evals harness with 10 regression scenarios.
