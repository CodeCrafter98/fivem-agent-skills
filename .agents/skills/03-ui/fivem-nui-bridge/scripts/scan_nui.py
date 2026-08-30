#!/usr/bin/env python3
"""
Scans a FiveM project for NUI related communications and definitions.
"""
import argparse
import re
import json
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Scan FiveM project for NUI interfaces")
    parser.add_argument("root", nargs="?", default=".", help="Project root directory")
    parser.add_argument("--format", choices=["json", "text"], default="text", help="Output format")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    
    checks = {
        "lua_nui_callbacks": re.compile(r"Register(?:Nui|NUI)Callback\s*\(\s*['\"]([^'\"]+)"),
        "lua_nui_messages": re.compile(r"SendNUIMessage\s*\("),
        "frontend_fetches": re.compile(r"fetch\s*\(\s*`?['\"]?https://\$\{[^}]+\}/([^`'\"$]+)"),
        "frontend_postmessages": re.compile(r"window\.postMessage\s*\(")
    }

    results = {key: [] for key in checks}
    allowed_extensions = {".lua", ".ts", ".tsx", ".js", ".jsx"}

    for file_path in root.rglob("*"):
        if not file_path.is_file(): continue
        if ".git" in file_path.parts or "node_modules" in file_path.parts: continue
        if file_path.suffix.lower() not in allowed_extensions: continue
        
        try:
            text = file_path.read_text(encoding="utf-8", errors="ignore")
            lines = text.splitlines()
            
            for line_idx, line in enumerate(lines, 1):
                for kind, pattern in checks.items():
                    match = pattern.search(line)
                    if match:
                        value = match.group(1) if match.groups() else "(anonymous/dynamic)"
                        results[kind].append({
                            "file": str(file_path.relative_to(root)),
                            "line": line_idx,
                            "value": value,
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
                print(f"  {f['file']}:{f['line']} -> {f['value']}")
            print()

if __name__ == "__main__":
    main()
