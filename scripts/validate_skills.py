#!/usr/bin/env python3
"""
FiveM Agent Skills — Package Validator v1.0.1

Validates skill structure, manifest integrity, version consistency,
portable references, Python syntax, eval cases, and templates.

Exit code 0 = all checks pass. Non-zero = at least one failure.
"""
from pathlib import Path
import json, re, sys, py_compile, tempfile

root = Path(__file__).resolve().parents[1]
skills_root = root / '.agents' / 'skills'
errors = []


def err(msg: str):
    errors.append(msg)


def section(title: str):
    print(f'\n--- {title} ---')


# ─── 1. Skill Structure ───────────────────────────────────────────────

section('Skill structure')

skill_dirs = []
skill_names = []

for skill_md in sorted(skills_root.rglob('SKILL.md')):
    skill_dir = skill_md.parent
    skill_dirs.append(skill_dir)

    text = skill_md.read_text(encoding='utf-8')

    # Frontmatter
    fm_match = re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not fm_match:
        err(f'{skill_md}: missing YAML frontmatter')
        continue

    fm = fm_match.group(1)
    name_match = re.search(r'^name:\s*(.+)$', fm, re.M)
    desc_match = re.search(r"^description:\s*['\"]?(.+?)['\"]?\s*$", fm, re.M)

    if not name_match:
        err(f'{skill_md}: missing name in frontmatter')
        continue
    if not desc_match:
        err(f'{skill_md}: missing description in frontmatter')
        continue

    name = name_match.group(1).strip().strip("'\"")
    desc = desc_match.group(1).strip().strip("'\"")

    # Name matches directory
    if name != skill_dir.name:
        err(f'{skill_md}: name {name!r} != directory {skill_dir.name!r}')

    # Valid characters
    if not re.fullmatch(r'[a-z0-9-]+', name):
        err(f'{skill_md}: invalid skill name characters: {name!r}')

    # Duplicate names
    if name in skill_names:
        err(f'{skill_md}: duplicate skill name: {name!r}')
    skill_names.append(name)

    # Description length
    if len(desc) > 1024:
        err(f'{skill_md}: description exceeds 1024 characters ({len(desc)})')
    if len(desc) < 20:
        err(f'{skill_md}: description suspiciously short ({len(desc)} chars)')

    # YAML quoting — descriptions with colons must be quoted to avoid YAML parse errors
    raw_desc_line = re.search(r'^description:\s*(.+)$', fm, re.M)
    if raw_desc_line:
        raw_val = raw_desc_line.group(1).strip()
        # Check if the value contains a colon followed by a space (YAML mapping indicator)
        unquoted_val = raw_val.strip("'\"")
        if ': ' in unquoted_val and not (raw_val.startswith("'") or raw_val.startswith('"')):
            err(f'{skill_md}: description contains ": " but is not quoted — will break strict YAML parsers (skills.sh)')

    # Required sections
    for section_name in ['## Purpose', '## Workflow', '## Done criteria', '## Output contract']:
        if section_name not in text:
            err(f'{skill_md}: missing section {section_name}')

    # Standalone safety or engineering rules
    if '## Standalone safety' not in text and '## Non-negotiable engineering rules' not in text:
        err(f'{skill_md}: missing standalone safety or engineering rules section')

skill_count = len(skill_dirs)
print(f'Found {skill_count} skills')


# ─── 2. Manifest Integrity ────────────────────────────────────────────

section('Manifest integrity')

manifest_path = root / 'skills-manifest.json'
if not manifest_path.exists():
    err('skills-manifest.json not found')
else:
    try:
        manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
    except json.JSONDecodeError as e:
        err(f'skills-manifest.json: invalid JSON: {e}')
        manifest = None

    if manifest:
        # skill_count
        if manifest.get('skill_count') != skill_count:
            err(f'skills-manifest.json: skill_count={manifest.get("skill_count")} but found {skill_count} skills')

        manifest_skills = manifest.get('skills', [])
        manifest_names = [s['name'] for s in manifest_skills]

        # No duplicates in manifest
        if len(manifest_names) != len(set(manifest_names)):
            err('skills-manifest.json: duplicate skill names')

        # Match filesystem
        fs_names = set(skill_names)
        mf_names = set(manifest_names)
        missing = fs_names - mf_names
        phantom = mf_names - fs_names
        if missing:
            err(f'skills-manifest.json: missing skills: {", ".join(sorted(missing))}')
        if phantom:
            err(f'skills-manifest.json: phantom skills (in manifest but not filesystem): {", ".join(sorted(phantom))}')

        # Category validation
        for entry in manifest_skills:
            cat = entry.get('category', '')
            name = entry.get('name', '')
            expected_path = skills_root / cat / name
            if not expected_path.exists():
                err(f'skills-manifest.json: category path mismatch for {name}: {cat}/{name} does not exist')

        # Exact count for v1.0.1
        if skill_count != 43:
            err(f'Expected exactly 43 skills for v1.0.1, found {skill_count}')


# ─── 3. Version Integrity ─────────────────────────────────────────────

section('Version integrity')

version_file = root / 'VERSION'
if version_file.exists():
    file_version = version_file.read_text(encoding='utf-8').strip()
    if manifest and manifest.get('version') != file_version:
        err(f'VERSION ({file_version}) != skills-manifest.json version ({manifest.get("version")})')
    print(f'VERSION: {file_version}')
else:
    err('VERSION file not found')


# ─── 4. Local References ──────────────────────────────────────────────

section('Local references')

ref_pattern = re.compile(r'`((?:references|scripts|assets)/[^`]+)`')

for skill_dir in skill_dirs:
    skill_md = skill_dir / 'SKILL.md'
    text = skill_md.read_text(encoding='utf-8')
    for match in ref_pattern.finditer(text):
        ref_path = match.group(1)
        # Check if the referenced file exists within the skill directory
        full_path = skill_dir / ref_path
        if not full_path.exists():
            err(f'{skill_md}: references {ref_path!r} but file does not exist in skill package')

ref_errors_before = len([e for e in errors if 'does not exist in skill package' in e])
print(f'Checked portable references ({ref_errors_before} broken)')


# ─── 5. Python Script Syntax ──────────────────────────────────────────

section('Python scripts')

py_files = list(skills_root.rglob('*.py')) + list((root / 'scripts').rglob('*.py'))
py_ok = 0
for py_file in py_files:
    try:
        py_compile.compile(str(py_file), doraise=True)
        py_ok += 1
    except py_compile.PyCompileError as e:
        err(f'{py_file}: Python syntax error: {e}')

print(f'{py_ok}/{len(py_files)} Python scripts compile OK')


# ─── 6. Eval Cases ────────────────────────────────────────────────────

section('Eval cases')

eval_dir = root / 'evals' / 'cases'
eval_names = []
if eval_dir.exists():
    for eval_file in sorted(eval_dir.glob('*.json')):
        try:
            case = json.loads(eval_file.read_text(encoding='utf-8'))
        except json.JSONDecodeError as e:
            err(f'{eval_file}: invalid JSON: {e}')
            continue

        # Required fields
        for field in ['name', 'prompt', 'expected_skills']:
            if field not in case:
                err(f'{eval_file}: missing required field {field!r}')

        name = case.get('name', '')
        if name in eval_names:
            err(f'{eval_file}: duplicate eval name {name!r}')
        eval_names.append(name)

        # Expected skills exist
        for skill in case.get('expected_skills', []):
            if skill not in skill_names:
                err(f'{eval_file}: expected skill {skill!r} does not exist')

        # Assertions
        assertions = case.get('assertions', [])
        if not isinstance(assertions, list):
            err(f'{eval_file}: assertions must be a list')

        # Forbidden patterns
        forbidden = case.get('forbidden_patterns', [])
        if not isinstance(forbidden, list):
            err(f'{eval_file}: forbidden_patterns must be a list')

    print(f'{len(eval_names)} eval cases validated')
else:
    print('No eval cases directory found')


# ─── 7. Templates ─────────────────────────────────────────────────────

section('Templates')

templates_dir = root / 'templates'
if templates_dir.exists():
    # Check expected template dirs
    for tpl in ['resource-starter', 'nui-bridge', 'framework-adapter']:
        tpl_dir = templates_dir / tpl
        if not tpl_dir.exists():
            err(f'templates/{tpl}: directory not found')

    # Check fxmanifest.lua does NOT contain deprecated lua54
    for fxm in templates_dir.rglob('fxmanifest.lua'):
        text = fxm.read_text(encoding='utf-8')
        if "lua54 'yes'" in text or 'lua54 "yes"' in text or "lua54('yes')" in text:
            err(f'{fxm}: contains deprecated lua54 directive')

    # resource-starter checks
    starter = templates_dir / 'resource-starter'
    if starter.exists():
        if not (starter / 'fxmanifest.lua').exists():
            err('templates/resource-starter: missing fxmanifest.lua')

    # nui-bridge checks
    nui = templates_dir / 'nui-bridge'
    if nui.exists():
        for expected in ['nui.ts', 'client.lua']:
            if not (nui / expected).exists():
                err(f'templates/nui-bridge: missing {expected}')

    print('Template checks complete')
else:
    print('No templates directory found')


# ─── Summary ──────────────────────────────────────────────────────────

section('Summary')

if errors:
    print(f'\nFAILED: {len(errors)} error(s)\n')
    for e in errors:
        print(f'  ✗ {e}')
    sys.exit(1)
else:
    print(f'\nOK: {skill_count} skills validated, {len(py_files)} scripts compiled, {len(eval_names)} evals checked.')
    sys.exit(0)
