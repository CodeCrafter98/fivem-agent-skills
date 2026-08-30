#!/usr/bin/env python3
from pathlib import Path
import re, json, argparse
p=argparse.ArgumentParser(); p.add_argument('root', nargs='?', default='.'); a=p.parse_args()
root=Path(a.root).resolve()
files=[x for x in root.rglob('*') if x.is_file() and '.git' not in x.parts and 'node_modules' not in x.parts]
manifest=[str(x.relative_to(root)) for x in files if x.name=='fxmanifest.lua']
lua=[x for x in files if x.suffix=='.lua']
texts={}
for f in lua:
    try: texts[f]=f.read_text(encoding='utf-8',errors='ignore')
    except: pass
patterns={
 'net_events': r"RegisterNetEvent\s*\(\s*['\"]([^'\"]+)",
 'server_triggers': r"TriggerServerEvent\s*\(\s*['\"]([^'\"]+)",
 'client_triggers': r"TriggerClientEvent\s*\(\s*['\"]([^'\"]+)",
 'exports': r"exports(?:\s*\[?\s*['\"]?[^\n]*|\s*\()",
 'nui_callbacks': r"RegisterNuiCallback|RegisterNUICallback",
 'nui_messages': r"SendNUIMessage\s*\(",
 'statebags': r"(?:Entity|Player)\s*\([^\)]*\)\.state|GlobalState",
 'wait0': r"Wait\s*\(\s*0\s*\)|Citizen\.Wait\s*\(\s*0\s*\)",
}
report={'root':str(root),'manifests':manifest,'lua_files':len(lua),'signals':{}}
for k,pat in patterns.items():
    hits=[]
    rx=re.compile(pat)
    for f,t in texts.items():
        ms=rx.findall(t)
        if ms: hits.append({'file':str(f.relative_to(root)),'count':len(ms),'examples':ms[:10] if isinstance(ms[0] if ms else '',str) else []})
    report['signals'][k]=hits
# dependency hints
alltext='\n'.join(texts.values()).lower()
report['framework_hints']={k:(k in alltext) for k in ['qbx_core','qb-core','es_extended','ox_lib','oxmysql','ox_target','ox_inventory']}
print(json.dumps(report, indent=2))
