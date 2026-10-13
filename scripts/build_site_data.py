#!/usr/bin/env python3
"""Parse README.md into docs/data/servers.json so the website renders from the
same source of truth as the list. Run after editing the README.

Output shape:
  { "generated": true,
    "counts": {"total": N, "servers": .., "clients": .., "toolkits": .., "docker": ..},
    "groups": {"servers": [ {name, description, url, category}, ... ], ... } }
"""
import json
import os
import re

README = "README.md"
OUT = os.path.join("docs", "data", "servers.json")

LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://[^)\s]+)\)")
BARE_URL_RE = re.compile(r"(https?://[^\s|]+)")

# Which top-level `## ` heading maps to which group.
GROUP_FOR_TOP = {
    "MCP Servers": "servers",
    "MCP Clients": "clients",
    "MCP Toolkits": "toolkits",
    "Agent Development Frameworks": "toolkits",
    "Language-Specific SDKs": "toolkits",
    "Docker MCP Toolkit": "docker",
}
SKIP_CATEGORIES = {"Installation Steps"}


def clean(text: str) -> str:
    """Strip markdown emphasis/links down to display text."""
    text = text.strip()
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)  # [t](u) -> t
    text = text.replace("**", "").replace("&#124;", "|").strip()
    return text


def split_cells(line: str):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]


def is_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", line)) and "-" in line


def extract_url(line: str):
    m = LINK_RE.search(line)
    if m:
        return m.group(2)
    m = BARE_URL_RE.search(line)
    return m.group(1) if m else None


def main():
    with open(README, encoding="utf-8") as f:
        lines = f.readlines()

    groups = {"servers": [], "clients": [], "toolkits": [], "docker": []}
    top = None
    category = None
    in_table = False
    header_cols = 0

    for raw in lines:
        line = raw.rstrip("\n")
        m2 = re.match(r"^##\s+(.*?)\s*$", line)
        m3 = re.match(r"^###\s+(.*?)\s*$", line)
        if m2:
            top = m2.group(1)
            category = top if top in ("Agent Development Frameworks", "Language-Specific SDKs") else None
            in_table = False
            continue
        if m3:
            category = m3.group(1)
            in_table = False
            continue

        stripped = line.strip()
        is_row = stripped.startswith("|") and stripped.endswith("|")
        if not is_row:
            in_table = False
            continue
        if is_separator(line):
            continue

        cells = split_cells(line)
        if not in_table:
            header_cols = len(cells)
            in_table = True
            continue  # skip header row

        group = GROUP_FOR_TOP.get(top or "")
        if not group or (category in SKIP_CATEGORIES):
            continue
        if len(cells) < 3:
            continue

        name = clean(cells[1]) if len(cells) > 1 else ""
        url = extract_url(line)
        # Description = longest non-link free-text cell after the name.
        candidates = cells[2:]
        desc = ""
        for c in candidates:
            cc = clean(c)
            # ignore cells that are essentially just a link label like "GitHub"/"Docs"
            if cc.lower() in ("github", "docs", "docker hub", "n/a", "tbd", ""):
                continue
            if len(cc) > len(desc):
                desc = cc
        if not name:
            continue

        groups[group].append({
            "name": name,
            "description": desc,
            "url": url or "",
            "category": category or (top or "Other"),
        })

    counts = {k: len(v) for k, v in groups.items()}
    counts["total"] = sum(counts.values())
    data = {"generated": True, "counts": counts, "groups": groups}

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Wrote {OUT}")
    print("Counts:", json.dumps(counts))


if __name__ == "__main__":
    main()
