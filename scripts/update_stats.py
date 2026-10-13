#!/usr/bin/env python3
"""Recompute the headline stats line in README.md between the
`<!-- STATS:START -->` / `<!-- STATS:END -->` markers.

Counts numbered table rows (listed projects) and catalog categories, floors
them to friendly round numbers, and rewrites the banner. Idempotent: prints
whether anything changed (CI uses `git diff` to decide whether to commit).
"""
import re
import sys

README = sys.argv[1] if len(sys.argv) > 1 else "README.md"

with open(README, encoding="utf-8") as f:
    text = f.read()

# Listed projects: every numbered table row like `| 12 | ... |`.
projects = len(re.findall(r"(?m)^\|\s*\d+\s*\|", text))

# Categories: every `### ` heading that is a catalog section, plus the two
# standalone `## ` catalogs. Exclude non-catalog headings.
non_catalog = {"Installation Steps"}
sub = [h for h in re.findall(r"(?m)^###\s+(.*?)\s*$", text) if h not in non_catalog]
top_catalogs = {"Agent Development Frameworks", "Language-Specific SDKs"}
tops = [h for h in re.findall(r"(?m)^##\s+(.*?)\s*$", text) if h in top_catalogs]
categories = len(sub) + len(tops)


def floor_to(n, step):
    return (n // step) * step


proj_round = floor_to(projects, 10)
cat_round = floor_to(categories, 5)

banner = (
    f"**\U0001F4E6 {proj_round}+ listed projects** &nbsp;·&nbsp; "
    f"**\U0001F5C2️ {cat_round}+ categories** &nbsp;·&nbsp; "
    f"**\U0001F433 100+ Docker MCP Toolkit servers** &nbsp;·&nbsp; "
    f"**\U0001F91D community-curated**"
)

new_block = f"<!-- STATS:START -->\n{banner}\n<!-- STATS:END -->"
new_text, n = re.subn(
    r"<!-- STATS:START -->.*?<!-- STATS:END -->",
    new_block,
    text,
    flags=re.DOTALL,
)

if n == 0:
    print("No STATS markers found in README.md — nothing to update.", file=sys.stderr)
    sys.exit(1)

if new_text != text:
    with open(README, "w", encoding="utf-8") as f:
        f.write(new_text)
    print(f"Updated stats: {proj_round}+ projects, {cat_round}+ categories "
          f"(raw: {projects} projects, {categories} categories).")
else:
    print(f"Stats already current: {proj_round}+ projects, {cat_round}+ categories.")
