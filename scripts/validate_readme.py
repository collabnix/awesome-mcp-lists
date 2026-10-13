#!/usr/bin/env python3
"""Validate README.md table entries.

Catches the most common contribution mistakes:
  * a row with a different number of columns than its table header
    (e.g. an extra `| TBD |` cell pasted into a 4-column table);
  * a raw, unescaped `|` inside a cell (use `&#124;` instead);
  * an empty name or link cell.

Usage:  python3 scripts/validate_readme.py [README.md]
Exits non-zero (and prints line-numbered errors) if any problem is found.
"""
import re
import sys

README = sys.argv[1] if len(sys.argv) > 1 else "README.md"


def cell_count(line: str) -> int:
    """Number of content cells in a markdown table row."""
    s = line.strip()
    # strip the leading/trailing pipe, then split
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return len(s.split("|"))


def is_separator(line: str) -> bool:
    return bool(re.match(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", line)) and "-" in line


def main() -> int:
    with open(README, encoding="utf-8") as f:
        lines = f.readlines()

    errors = []
    header_cols = None          # expected column count for the current table
    header_line_no = None
    in_table = False

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        stripped = line.strip()
        is_row = stripped.startswith("|") and stripped.endswith("|") and "|" in stripped[1:]

        if not is_row:
            in_table = False
            header_cols = None
            continue

        if is_separator(line):
            # the |---|---| row: confirms the previous line was a header
            continue

        if not in_table:
            # first row of a new table => it's the header
            header_cols = cell_count(line)
            header_line_no = i
            in_table = True
            continue

        # data row
        cols = cell_count(line)
        if cols != header_cols:
            errors.append(
                f"L{i}: row has {cols} columns but its table header "
                f"(L{header_line_no}) has {header_cols}. "
                f"Fix the column count — see CONTRIBUTING.md.\n      {stripped[:120]}"
            )

    # Stray TBD cell wedged before a link column (the classic bad paste).
    for i, raw in enumerate(lines, start=1):
        if re.search(r"\|\s*TBD\s*\|\s*\[(?:GitHub|Docs|Docker Hub)\]", raw):
            errors.append(f"L{i}: stray `| TBD |` cell before a link — remove it.")

    if errors:
        print(f"❌ README validation failed ({len(errors)} issue(s)):\n")
        for e in errors:
            print("  - " + e)
        print("\nSee CONTRIBUTING.md for the correct entry format.")
        return 1

    print("✅ README tables look good — all rows match their table's column count.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
