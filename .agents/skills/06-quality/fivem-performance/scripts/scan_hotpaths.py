#!/usr/bin/env python3
"""
Scans a FiveM project for potential performance hotpaths.
Identifies Wait(0) loops, threads, state bag writes, and NUI messages.
"""
import argparse
import re
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Scan FiveM project for performance hotpaths")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    
    checks = {
        "wait_0_loops": re.compile(r"\b(?:Citizen\.)?Wait\s*\(\s*0\s*\)"),
        "threads": re.compile(r"\b(?:Citizen\.)?CreateThread\s*\("),
        "nui_messages": re.compile(r"\bSendNUIMessage\s*\("),
        "state_writes": re.compile(r"\.state(?::set|\s*\[|\s*\.)"),
        "tick_events": re.compile(r"\b(?:RegisterTick|AddEventHandler\s*\(\s*['\"]onTick['\"])\s*\(")
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
                print(f"  {f['file']}:{f['line']} -> {f['snippet']}")
            print()

if __name__ == "__main__":
    main()
