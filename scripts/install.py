#!/usr/bin/env python3
"""Safely install FiveM Agent Skills without deleting unrelated existing skills."""
from pathlib import Path
import argparse, shutil

root = Path(__file__).resolve().parents[1]
src_skills = root / '.agents' / 'skills'
parser=argparse.ArgumentParser()
parser.add_argument('--scope', choices=['project','global'], required=True)
parser.add_argument('--dest', help='Target project root for --scope project')
parser.add_argument('--antigravity-compat', action='store_true', help='Also install a compatibility copy to ~/.gemini/config/skills')
parser.add_argument('--force', action='store_true', help='Replace only conflicting FiveM skill directories; never deletes unrelated skills')
a=parser.parse_args()

def iter_skills():
    for skill_md in sorted(src_skills.rglob('SKILL.md')):
        yield skill_md.parent

def install_skills(target_root: Path):
    target_root.mkdir(parents=True, exist_ok=True)
    installed=skipped=0
    for skill_dir in iter_skills():
        dst = target_root / skill_dir.name
        if dst.exists():
            if not a.force:
                print(f'SKIP existing: {dst}')
                skipped += 1
                continue
            shutil.rmtree(dst)
        shutil.copytree(skill_dir, dst)
        installed += 1
    print(f'Installed {installed} skills into {target_root}; skipped {skipped}.')

if a.scope == 'project':
    if not a.dest: raise SystemExit('--dest is required for project scope')
    dest=Path(a.dest).expanduser().resolve()
    install_skills(dest/'.agents'/'skills')
    # Antigravity can consume .agents/AGENTS.md; do not overwrite project instructions accidentally.
    ag_dir=dest/'.agents'; ag_dir.mkdir(parents=True, exist_ok=True)
    ag_target=ag_dir/'AGENTS.md'
    if not ag_target.exists() or a.force:
        shutil.copy2(root/'.agents'/'AGENTS.md', ag_target)
        print(f'Installed FiveM instructions -> {ag_target}')
    else:
        print(f'SKIP existing: {ag_target} (merge {root / ".agents" / "AGENTS.md"} manually if desired)')
    root_target=dest/'AGENTS.md'
    if not root_target.exists():
        shutil.copy2(root/'AGENTS.md', root_target)
        print(f'Installed root instructions -> {root_target}')
    else:
        print(f'SKIP existing: {root_target} (do not overwrite project AGENTS.md automatically)')
else:
    home=Path.home()
    install_skills(home/'.agents'/'skills')
    if a.antigravity_compat:
        install_skills(home/'.gemini'/'config'/'skills')
