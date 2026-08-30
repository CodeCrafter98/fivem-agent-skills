#!/usr/bin/env python3
from pathlib import Path
import re, argparse
p=argparse.ArgumentParser(); p.add_argument('root', nargs='?', default='.'); a=p.parse_args(); root=Path(a.root).resolve()
checks=[
 ('network_event', re.compile(r"RegisterNetEvent\s*\(\s*['\"]([^'\"]+)")),
 ('nui_callback', re.compile(r"Register(?:Nui|NUI)Callback\s*\(\s*['\"]([^'\"]+)")),
 ('server_event_trigger', re.compile(r"TriggerServerEvent\s*\(\s*['\"]([^'\"]+)")),
]
for f in root.rglob('*.lua'):
    if '.git' in f.parts or 'node_modules' in f.parts: continue
    text=f.read_text(encoding='utf-8',errors='ignore')
    lines=text.splitlines()
    for kind,rx in checks:
        for i,line in enumerate(lines,1):
            m=rx.search(line)
            if m: print(f'{kind}\t{f.relative_to(root)}:{i}\t{m.group(1)}')
