# MCP Portal (website)

The browsable, searchable web front-end for [Awesome MCP Lists](https://github.com/collabnix/awesome-mcp-lists),
served via GitHub Pages from the `docs/` folder.

👉 **Live site:** https://collabnix.github.io/awesome-mcp-lists/

## How it works — single source of truth

The directory is **generated from the repository's [`README.md`](../README.md)**, so the
website and the list never drift apart. You do **not** edit server cards by hand.

```
README.md  ──(scripts/build_site_data.py)──▶  docs/data/servers.json  ──(index.html fetch)──▶  rendered cards
```

- `docs/index.html` — self-contained page (inline CSS + JS). On load it fetches
  `data/servers.json` and renders cards grouped by category, with live search,
  per-group tabs, and category filters.
- `docs/data/servers.json` — generated data file. **Do not edit by hand.**
- `learn.html` / `learn-*.js` / `learn-*.css` — the "Learn MCP" tutorial section.

## Adding or updating an entry

Add it to the main [`README.md`](../README.md) — see
[CONTRIBUTING.md](../CONTRIBUTING.md). The site data is regenerated automatically:

- On every push to `main` that touches `README.md`, the **Sync stats & site data**
  GitHub Action re-runs `scripts/build_site_data.py` and commits the updated
  `docs/data/servers.json`.

To regenerate locally:

```bash
python3 scripts/build_site_data.py        # rewrites docs/data/servers.json
cd docs && python3 -m http.server 8000    # preview at http://localhost:8000
```

> The page uses `fetch()`, so preview it over `http://` (the command above),
> not by opening the file directly with `file://`.

## Deployment

GitHub Pages is configured to serve from the `docs/` folder on `main`. Any merged
change to `README.md` flows to the live site automatically once the sync Action runs.

## License

Part of the awesome-mcp-lists project — [CC0 1.0](../LICENSE).
