#!/usr/bin/env python3
from pathlib import Path
import re, sys

root = Path(__file__).resolve().parents[1]
skills_root = root / '.agents' / 'skills'
errors=[]; count=0
for p in sorted(skills_root.rglob('SKILL.md')):
    count += 1
    text=p.read_text(encoding='utf-8')
    m=re.match(r'^---\n(.*?)\n---\n', text, re.S)
    if not m:
        errors.append(f'{p}: missing YAML frontmatter')
        continue
    fm=m.group(1)
    name=re.search(r'^name:\s*(.+)$', fm, re.M)
    desc=re.search(r'^description:\s*(.+)$', fm, re.M)
    if not name or not desc:
        errors.append(f'{p}: name/description required')
        continue
    n=name.group(1).strip()
    d=desc.group(1).strip()
    if n != p.parent.name:
        errors.append(f'{p}: name {n!r} != parent {p.parent.name!r}')
    if not re.fullmatch(r'[a-z0-9-]+', n):
        errors.append(f'{p}: invalid skill name')
    if len(d) > 1024:
        errors.append(f'{p}: description exceeds 1024 characters')
    for section in ['## Purpose','## Workflow','## Done criteria','## Output contract']:
        if section not in text:
            errors.append(f'{p}: missing {section}')

if errors:
    print('\n'.join(errors))
    sys.exit(1)
print(f'OK: {count} skills validated.')
