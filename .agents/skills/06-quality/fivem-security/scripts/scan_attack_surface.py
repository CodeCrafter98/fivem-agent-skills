#!/usr/bin/env python3
"""
Scans a FiveM project for potential security attack surfaces.
Useful for identifying network boundaries and NUI callbacks that require validation.
"""
import argparse
import re
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Scan FiveM project for attack surfaces")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    
    # Attack surface definitions
    checks = {
        "network_events": re.compile(r"RegisterNetEvent\s*\(\s*['\"]([^'\"]+)"),
        "nui_callbacks": re.compile(r"Register(?:Nui|NUI)Callback\s*\(\s*['\"]([^'\"]+)"),
        "server_event_triggers": re.compile(r"TriggerServerEvent\s*\(\s*['\"]([^'\"]+)")
    }

    results = {key: [] for key in checks}

    for file_path in root.rglob("*.lua"):
        if ".git" in file_path.parts or "node_modules" in file_path.parts:
            continue
        
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            lines = text.splitlines()
            
            for line_idx, line in enumerate(lines, 1):
                for kind, pattern in checks.items():
                    match = pattern.search(line)
                    if match:
                        results[kind].append({
                            "file": str(file_path.relative_to(root)),
                            "line": line_idx,
                            "name": match.group(1),
                            "snippet": line.strip()[:100]
                        })
        except Exception:
            pass

    if args.format == "json":
        print(json.dumps(results, indent=2))
    else:
        for kind, findings in results.items():
            print(f"=== {kind.replace('_', ' ').title()} ({len(findings)}) ===")
            for f in findings:
                print(f"  {f['file']}:{f['line']} -> {f['name']}")
            print()

if __name__ == "__main__":
    main()
