#!/usr/bin/env python3
"""
Scans an existing FiveM project for structural signals, dependencies, and architecture.
"""
import argparse
import re
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Inspect FiveM project architecture")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    
    files = [x for x in root.rglob("*") if x.is_file() and ".git" not in x.parts and "node_modules" not in x.parts]
    manifests = [str(x.relative_to(root)) for x in files if x.name in ("fxmanifest.lua", "__resource.lua")]
    lua_files = [x for x in files if x.suffix == ".lua"]
    
    texts = {}
    for f in lua_files:
        try:
            texts[f] = f.read_text(encoding="utf-8", errors="ignore")
        except:
            pass

    patterns = {
        "net_events": r"RegisterNetEvent\s*\(\s*['\"]([^'\"]+)",
        "server_triggers": r"TriggerServerEvent\s*\(\s*['\"]([^'\"]+)",
        "client_triggers": r"TriggerClientEvent\s*\(\s*['\"]([^'\"]+)",
        "exports": r"exports(?:\s*\[?\s*['\"]?[^\n]*|\s*\()",
        "nui_callbacks": r"Register(?:Nui|NUI)Callback",
        "nui_messages": r"SendNUIMessage\s*\(",
        "statebags": r"(?:Entity|Player)\s*\([^\)]*\)\.state|GlobalState",
        "wait0": r"(?:Citizen\.)?Wait\s*\(\s*0\s*\)",
    }

    report = {
        "root": str(root),
        "manifests": manifests,
        "lua_files_count": len(lua_files),
        "signals": {}
    }

    for key, pat in patterns.items():
        hits = []
        rx = re.compile(pat)
        for f, t in texts.items():
            matches = rx.findall(t)
            if matches:
                # Some regexes capture groups, some don't.
                examples = matches[:5] if matches and isinstance(matches[0], str) else []
                hits.append({
                    "file": str(f.relative_to(root)),
                    "count": len(matches),
                    "examples": examples
                })
        report["signals"][key] = hits

    # Dependency / framework heuristics
    all_text = "\n".join(texts.values()).lower()
    frameworks = ["qbx_core", "qb-core", "es_extended", "ox_lib", "oxmysql", "ox_target", "ox_inventory"]
    
    report["framework_hints"] = {
        fw: (fw in all_text) for fw in frameworks
    }

    print(json.dumps(report, indent=2))

if __name__ == "__main__":
    main()
