#!/usr/bin/env python3
from pathlib import Path
import re, argparse
p=argparse.ArgumentParser(); p.add_argument('root', nargs='?', default='.'); a=p.parse_args(); root=Path(a.root).resolve()
for f in root.rglob('*'):
    if not f.is_file() or '.git' in f.parts or 'node_modules' in f.parts: continue
    if f.suffix.lower() not in {'.lua','.ts','.tsx','.js','.jsx'}: continue
    text=f.read_text(encoding='utf-8',errors='ignore')
    for rx,kind in [(r"Register(?:Nui|NUI)Callback\s*\(\s*['\"]([^'\"]+)",'lua-callback'),(r"fetch\s*\(\s*`?['\"]?https://\$\{[^}]+\}/([^`'\"$]+)",'ui-fetch'),(r"SendNUIMessage\s*\(",'nui-message')]:
        for m in re.finditer(rx,text):
            line=text.count('\n',0,m.start())+1
            val=m.group(1) if m.groups() else ''
            print(f'{kind}\t{f.relative_to(root)}:{line}\t{val}')
