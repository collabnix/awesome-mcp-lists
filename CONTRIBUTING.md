# Contributing to Awesome MCP Lists

First off — **thank you!** 🙌 This list stays useful because people like you add the
servers, clients, and toolkits they've found valuable. Contributions of every size
are welcome, and most PRs are merged quickly.

This guide keeps every entry consistent so the list stays easy to scan and search.

---

## 📌 Quick start

1. **Fork** this repository and create a branch (`git checkout -b add-my-mcp-server`).
2. **Find the right section** in [`README.md`](README.md) (see [Where does my entry go?](#-where-does-my-entry-go)).
3. **Add one row** to the end of that section's table using the [entry format](#-entry-format) below.
4. **Open a pull request** and fill in the checklist in the PR template.

That's it. One entry per row, one PR per change where possible.

---

## ✅ What belongs here

This is a curated list of **containerised** (or easily self-hostable / hosted) MCP
servers, clients, and toolkits. To be listed, a project should:

- **Be a real, working MCP project** — a server, client, SDK, framework, or tool that
  implements or supports the [Model Context Protocol](https://modelcontextprotocol.io).
- **Have a public link** — a GitHub repo, documentation site, or package page that works.
- **Have a clear, honest description** — what it does, in plain language.
- **Be runnable** — ideally via Docker, `npx`, `uvx`, `pip`, a hosted endpoint, or a
  documented install path.

### Please avoid

- ❌ Dead links, abandoned repos, or empty placeholder projects.
- ❌ Duplicate entries — search the README first (`Ctrl/Cmd+F`) before adding.
- ❌ Pure marketing copy, SEO spam, or keyword stuffing in the description.
- ❌ Closed-source "coming soon" projects with nothing to try yet.

Maintainers may edit descriptions for clarity or decline entries that don't fit.

---

## 🧭 Where does my entry go?

| If your project is a… | Add it under… |
|-----------------------|---------------|
| MCP **server** (what you run to expose tools/data) | `## MCP Servers` → the best-fit category (DevOps, Database, Web, AI & ML, Security, Communication, …) |
| MCP **client** (an app that connects to servers) | `## MCP Clients` → Desktop / Mobile / IDE / CLI / Web |
| **SDK, framework, template, or utility** for building MCP | `## MCP Toolkits` or `## Language-Specific SDKs` |

Pick the single most relevant category. If nothing fits, add it to the closest one
and mention your reasoning in the PR — a maintainer can re-file it.

---

## 🧱 Entry format

Add your project as the **last row** of the relevant table. Keep the numbering
sequential (continue from the last row).

### Servers (most common)

```markdown
| 42 | **Your Project** | A concise, specific description of what it does. | [GitHub](https://github.com/you/your-project) |
```

- **Number** — next sequential number in that table.
- **Name** — bold (`**Name**`). Link the name instead if there's no link column.
- **Description** — one sentence, specific, no trailing period required. Describe
  *capabilities*, not adjectives. Escape any literal `|` as `&#124;`.
- **Link** — `[GitHub](url)`, `[Docs](url)`, or `[Docker Hub](url)`. Use a working URL.

### Clients

```markdown
| 9 | **[Client Name](https://link)** | What it is and its MCP support. | Windows, macOS, Linux |
```

### Toolkits / SDKs

```markdown
| 8 | tool-name | Language | What it does | [GitHub](https://github.com/you/tool) |
```

> **Match the columns of the table you're editing.** Some tables have 4 columns, some 5.
> Don't add or drop columns — if a table has no "pull count" column, don't paste a `TBD`.

---

## 🔍 Before you open the PR

- [ ] I searched the README and my project isn't already listed.
- [ ] I added **one row** to the correct section.
- [ ] My row has the **same number of columns** as the rest of that table.
- [ ] The link works and points to the project (not a tracking/affiliate redirect).
- [ ] The description is accurate and free of marketing fluff.
- [ ] The Markdown table still renders (preview the diff on GitHub).

---

## 💬 Suggesting instead of editing

Not comfortable editing Markdown? No problem — open an
[issue using the "Suggest an MCP project" template](../../issues/new/choose) and a
maintainer will add it.

---

## 📄 License

By contributing, you agree that your contributions are released under the project's
[CC0 1.0](LICENSE) dedication — i.e. into the public domain.

Thanks again for helping make this the best MCP list on the internet. 🚀
