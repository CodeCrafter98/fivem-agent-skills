#!/usr/bin/env python3
"""Safely install FiveM Agent Skills without deleting unrelated existing skills."""
from pathlib import Path
import argparse, shutil, json, datetime

root = Path(__file__).resolve().parents[1]
src_skills = root / '.agents' / 'skills'
version_file = root / 'VERSION'
version = version_file.read_text(encoding='utf-8').strip() if version_file.exists() else 'unknown'

parser = argparse.ArgumentParser(
    description='Install FiveM Agent Skills into a project or globally.',
    epilog='Preferred installation method: npx skills add CodeCrafter98/fivem-agent-skills'
)
parser.add_argument('--scope', choices=['project', 'global'], required=True,
                    help='Install scope: project (into --dest) or global (~/.agents/skills)')
parser.add_argument('--dest', help='Target project root (required for --scope project)')
parser.add_argument('--antigravity-compat', action='store_true',
                    help='Also install to ~/.gemini/config/skills for Antigravity global discovery')
parser.add_argument('--force', action='store_true',
                    help='Replace existing FiveM skill directories (never deletes unrelated skills)')
parser.add_argument('--dry-run', action='store_true',
                    help='Show what would be installed without making changes')
parser.add_argument('--verify', action='store_true',
                    help='Run post-install validation')
parser.add_argument('--version', action='version', version=f'FiveM Agent Skills v{version}')
args = parser.parse_args()


def iter_skills():
    """Yield each skill directory (contains SKILL.md)."""
    for skill_md in sorted(src_skills.rglob('SKILL.md')):
        yield skill_md.parent


def install_skills(target_root: Path) -> tuple[int, int, list[str]]:
    """Install skills into target_root. Returns (installed, skipped, skill_names)."""
    if not args.dry_run:
        target_root.mkdir(parents=True, exist_ok=True)

    installed = 0
    skipped = 0
    names = []

    for skill_dir in iter_skills():
        dst = target_root / skill_dir.name
        names.append(skill_dir.name)

        if dst.exists():
            if not args.force:
                if not args.dry_run:
                    print(f'  SKIP  {skill_dir.name}')
                skipped += 1
                continue
            if not args.dry_run:
                shutil.rmtree(dst)

        if args.dry_run:
            print(f'  WOULD INSTALL  {skill_dir.name} -> {dst}')
        else:
            shutil.copytree(skill_dir, dst)
        installed += 1

    action = 'Would install' if args.dry_run else 'Installed'
    print(f'\n  {action} {installed} skills into {target_root}; skipped {skipped}.')
    return installed, skipped, names


def write_receipt(target_dir: Path, skill_names: list[str]):
    """Write an installation receipt for traceability."""
    if args.dry_run:
        return

    receipt_path = target_dir / '.agents' / 'fivem-agent-skills.json'
    receipt_path.parent.mkdir(parents=True, exist_ok=True)
    receipt = {
        'package': 'fivem-agent-skills',
        'version': version,
        'source': 'https://github.com/CodeCrafter98/fivem-agent-skills',
        'installed_at': datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'skill_count': len(skill_names),
        'skills': sorted(skill_names),
    }
    receipt_path.write_text(json.dumps(receipt, indent=2) + '\n', encoding='utf-8')
    print(f'  Receipt -> {receipt_path}')


def verify_installation(target_root: Path, expected_count: int):
    """Basic post-install verification."""
    found = list(target_root.rglob('SKILL.md'))
    fivem_skills = [p for p in found if p.parent.name.startswith('fivem-')]
    print(f'\n  Verify: {len(fivem_skills)} FiveM skills found in {target_root}')
    if len(fivem_skills) < expected_count:
        print(f'  WARNING: expected at least {expected_count} FiveM skills')


# ─── Main ──────────────────────────────────────────────────────────────

print(f'FiveM Agent Skills v{version}')
print(f'Source: {root}')
print()

if args.scope == 'project':
    if not args.dest:
        raise SystemExit('Error: --dest is required for project scope')

    dest = Path(args.dest).expanduser().resolve()
    print(f'Installing to project: {dest}')

    installed, skipped, names = install_skills(dest / '.agents' / 'skills')
    write_receipt(dest, names)

    # Install .agents/AGENTS.md
    ag_dir = dest / '.agents'
    if not args.dry_run:
        ag_dir.mkdir(parents=True, exist_ok=True)
    ag_target = ag_dir / 'AGENTS.md'
    if not ag_target.exists() or args.force:
        if not args.dry_run:
            shutil.copy2(root / '.agents' / 'AGENTS.md', ag_target)
            print(f'  Installed FiveM instructions -> {ag_target}')
        else:
            print(f'  WOULD INSTALL  .agents/AGENTS.md -> {ag_target}')
    else:
        print(f'  SKIP  {ag_target} (merge manually if desired)')

    # Install root AGENTS.md only if none exists (do not overwrite project instructions)
    root_target = dest / 'AGENTS.md'
    if not root_target.exists():
        if not args.dry_run:
            shutil.copy2(root / 'AGENTS.md', root_target)
            print(f'  Installed root instructions -> {root_target}')
        else:
            print(f'  WOULD INSTALL  AGENTS.md -> {root_target}')
    else:
        print(f'  SKIP  {root_target} (will not overwrite project AGENTS.md)')

    if args.verify and not args.dry_run:
        verify_installation(dest / '.agents' / 'skills', installed)

else:
    home = Path.home()
    print(f'Installing globally for user: {home}')

    installed, skipped, names = install_skills(home / '.agents' / 'skills')

    if args.antigravity_compat:
        print('\nAntigravity compatibility:')
        install_skills(home / '.gemini' / 'config' / 'skills')

    if args.verify and not args.dry_run:
        verify_installation(home / '.agents' / 'skills', installed)

print('\nDone.')
