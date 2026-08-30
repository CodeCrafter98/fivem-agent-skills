#!/usr/bin/env python3
from pathlib import Path
import re, argparse
p=argparse.ArgumentParser(); p.add_argument('root', nargs='?', default='.'); a=p.parse_args(); root=Path(a.root).resolve()
patterns=[('wait0',re.compile(r'\b(?:Citizen\.)?Wait\s*\(\s*0\s*\)')),('thread',re.compile(r'\b(?:Citizen\.)?CreateThread\s*\(')),('nui_message',re.compile(r'\bSendNUIMessage\s*\(')),('state_write',re.compile(r'\.state(?::set|\s*\[|\s*\.)'))]
for f in root.rglob('*.lua'):
    if '.git' in f.parts or 'node_modules' in f.parts: continue
    lines=f.read_text(encoding='utf-8',errors='ignore').splitlines()
    for i,line in enumerate(lines,1):
        for name,rx in patterns:
            if rx.search(line): print(f'{name}\t{f.relative_to(root)}:{i}\t{line.strip()[:180]}')
