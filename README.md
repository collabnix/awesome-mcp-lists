# A Curated List of containerised MCP Servers, Clients and Toolkits

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![GitHub stars](https://img.shields.io/github/stars/collabnix/awesome-mcp-lists.svg)](https://github.com/collabnix/awesome-mcp-lists/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/collabnix/awesome-mcp-lists.svg)](https://github.com/collabnix/awesome-mcp-lists/network)
[![GitHub issues](https://img.shields.io/github/issues/collabnix/awesome-mcp-lists.svg)](https://github.com/collabnix/awesome-mcp-lists/issues)
[![GitHub license](https://img.shields.io/github/license/collabnix/awesome-mcp-lists.svg)](https://github.com/collabnix/awesome-mcp-lists/blob/main/LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/collabnix/awesome-mcp-lists/pulls)
[![Docker MCP](https://img.shields.io/badge/Docker-MCP-blue)](https://www.docker.com/)

A comprehensive curated list of containerised MCP Servers, Clients and toolkits.

## Table of Contents
- [MCP Servers](#mcp-servers)
  - [DevOps & Infrastructure](#devops--infrastructure)
  - [Database & Storage](#database--storage)
  - [Web & Content](#web--content)
  - [Integrations & APIs](#integrations--apis)
  - [AI & Machine Learning](#ai--machine-learning)
  - [Security & Authentication](#security--authentication)
  - [Development Tools](#development-tools)
  - [Communication](#communication)
  - [Knowledge Management](#knowledge-management)
  - [Multimedia & Design](#multimedia--design)
- [MCP Clients](#mcp-clients)
  - [Desktop Applications](#desktop-applications)
  - [Mobile Applications](#mobile-applications)
  - [IDE Extensions](#ide-extensions)
  - [Command Line Tools](#command-line-tools)
  - [Web Applications](#web-applications)
- [MCP Toolkits](#mcp-toolkits)
  - [SDKs & Libraries](#sdks--libraries)
  - [Frameworks](#frameworks)
  - [Testing Tools](#testing-tools)
  - [Utilities](#utilities)
  - [Hosting Solutions](#hosting-solutions)
  - [Templates](#templates)

## Containerised MCP Servers
- [Helium MCP](https://github.com/connerlambden/helium-mcp) — Real-time news with 37-dimension bias scoring, ML options pricing, and live market data. [Interactive demo](https://connerlambden.github.io/helium-news-explorer/) · [REST API](https://heliumtrades.com/mcp-page/)

### DevOps & Infrastructure

MCP servers for managing infrastructure, containers, and DevOps workflows.

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | github | Manage GitHub repositories and perform Git operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 2 | docker | Integrate with Docker to manage containers, images, and networks | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 3 | kubernetes | Orchestrate and manage containerized applications with Kubernetes | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 4 | gitlab | Interact with GitLab repositories and CI/CD pipelines | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gitlab.md) |
| 5 | circleci | Manage CI/CD pipelines and workflows in CircleCI | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/circleci.md) |
| 6 | **AWS Comprehensive** | Complete AWS service integration suite (20+ services) | [AWS Labs](https://github.com/awslabs/mcp) |
| 7 | **Terraform** | Infrastructure as Code management | [Docker Hub](https://hub.docker.com/r/hashicorp/terraform-mcp-server) |
| 8 | pulumi | Infrastructure as code platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/pulumi.md) |
| 9 | heroku | Cloud platform as a service (PaaS) | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/heroku.md) |
| 10 | jetbrains | Integrate with JetBrains IDEs and tools | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/jetbrains.md) |
| 11 | **github-mcp-server** | GitHub's official MCP server for repository and workflow management | [GitHub](https://github.com/github/github-mcp-server) |
| 12 | **mcp-context-forge** | AI Gateway, registry, and proxy for MCP, A2A, and REST/gRPC APIs with unified endpoint and centralized discovery | [GitHub](https://github.com/IBM/mcp-context-forge) |
| 13 | **toolhive** | Enterprise-grade platform for running and managing MCP servers | [GitHub](https://github.com/stacklok/toolhive) |
| 14 | **MCPJungle** | Self-hosted MCP Gateway for AI agents | [GitHub](https://github.com/mcpjungle/MCPJungle) |
| 15 | **mcp-server-kubernetes** | MCP Server for Kubernetes management commands | [GitHub](https://github.com/Flux159/mcp-server-kubernetes) |
| 16 | **kubectl-mcp-server** | MCP server for Kubernetes via kubectl — install with npx or pip | [GitHub](https://github.com/rohitg00/kubectl-mcp-server) |
| 17 | **apify-mcp-server** | Extract data from social media, search engines, maps, and any website using Apify scrapers via MCP | [GitHub](https://github.com/apify/apify-mcp-server) |
| 18 | **TrendRadar** | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。 | [GitHub](https://github.com/sansan0/TrendRadar) |
| 19 | **nginx-ui** | Yet another WebUI for Nginx | [GitHub](https://github.com/0xJacky/nginx-ui) |
| 20 | **Dark-Moon** | Open source (GPL-3.0) autonomous AI penetration testing platform and MCP host that orchestrates offensive tools across web, API, Active Directory and Kubernetes, with proof of exploitation and a local Privacy Gateway. | [GitHub](https://github.com/ASCIT31/Dark-Moon) |
| 21 | **hexstrike-ai** | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities. | [GitHub](https://github.com/0x4m4/hexstrike-ai) |
| 22 | **firecrawl-mcp-server** | 🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients. | [GitHub](https://github.com/firecrawl/firecrawl-mcp-server) |
| 23 | **csharp-sdk** | The official C# SDK for Model Context Protocol servers and clients. Maintained in collaboration with Microsoft. | [GitHub](https://github.com/modelcontextprotocol/csharp-sdk) |
| 24 | **kubefwd** | Bulk port forwarding Kubernetes services for local development. | [GitHub](https://github.com/txn2/kubefwd) |
| 25 | **bifrost** | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS. | [GitHub](https://github.com/maximhq/bifrost) |
| 26 | **metamcp** | MCP Aggregator, Orchestrator, Middleware, Gateway in one docker | [GitHub](https://github.com/metatool-ai/metamcp) |
| 27 | **Unity-MCP** | AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free. | [GitHub](https://github.com/IvanMurzak/Unity-MCP) |
| 28 | **holaOS** | The agent environment for long-horizon work, continuity, and self-evolution. | [GitHub](https://github.com/holaboss-ai/holaOS) |
| 29 | **minima** | On-premises conversational RAG with configurable containers | [GitHub](https://github.com/dmayboroda/minima) |
| 30 | **scira-mcp-chat** | A minimalistic MCP client with a good feature set. | [GitHub](https://github.com/zaidmukaddam/scira-mcp-chat) |
| 31 | **context-space** | Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations | [GitHub](https://github.com/context-space/context-space) |
| 32 | **notion-mcp-server** | Official Notion MCP Server | [GitHub](https://github.com/makenotion/notion-mcp-server) |
| 33 | **mcp-server** | An MCP server for interacting with the Financial Datasets stock market API. | [GitHub](https://github.com/financial-datasets/mcp-server) |
| 34 | **kubernetes-mcp-server** | Model Context Protocol (MCP) server for Kubernetes and OpenShift | [GitHub](https://github.com/containers/kubernetes-mcp-server) |
| 35 | **terraform-mcp-server** | The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development. | [GitHub](https://github.com/hashicorp/terraform-mcp-server) |
| 36 | **awesome-devops-mcp-servers** | A curated list of awesome MCP servers focused on DevOps tools and capabilities. | [GitHub](https://github.com/rohitg00/awesome-devops-mcp-servers) |
| 37 | **KiCAD-MCP-Server** | KiCAD MCP is a Model Context Protocol (MCP) implementation that enables Large Language Models (LLMs) like Claude to directly interact with KiCAD for printed circuit board design. | [GitHub](https://github.com/mixelpixx/KiCAD-MCP-Server) |
| 38 | **Find MCP** | Search 17,000+ MCP servers from the official MCP registry - remote Streamable HTTP (catalog.agentage.io/mcp, no auth for search) or stdio (npx @agentage/find-mcp) | [GitHub](https://github.com/agentage/find-mcp) |
| 39 | **SandBase Harness** | Local-first MCP bridge and agent runtime for governed sessions, approvals, credentials, audit/replay, and sandboxed execution through local, Docker, Kubernetes, or self-hosted worker backends | [GitHub](https://github.com/sandbaseai/sandbase-harness) |
| 40 | **worldmonitor** | Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface | [GitHub](https://github.com/koala73/worldmonitor) |
| 41 | **python-sdk** | The official Python SDK for Model Context Protocol servers and clients | [GitHub](https://github.com/modelcontextprotocol/python-sdk) |
| 42 | **typescript-sdk** | The official TypeScript SDK for Model Context Protocol servers and clients | [GitHub](https://github.com/modelcontextprotocol/typescript-sdk) |
| 43 | **openstatus** | 🫖 Status page with uptime monitoring & API monitoring as code   🫖 | [GitHub](https://github.com/openstatusHQ/openstatus) |
| 44 | **ha-mcp** | The Unofficial and Awesome Home Assistant MCP Server | [GitHub](https://github.com/homeassistant-ai/ha-mcp) |
| 45 | **ghidra-mcp** | Ghidra MCP Server — 200+ MCP tools for AI-powered reverse engineering. GUI plugin + headless server, lazy tool loading, convention enforcement, batch operations, Ghidra Server integration, and Docker deployment. | [GitHub](https://github.com/bethington/ghidra-mcp) |
| 46 | **radar** | The missing open-source Kubernetes UI with a built-in MCP server for AI agents. See what's broken, why, and what changed. Issues, Topology, event timeline, Helm, GitOps, live service traffic, and cluster audits - all in one Go binary. | [GitHub](https://github.com/skyhook-io/radar) |
| 47 | **jcodemunch-mcp** | Cut AI token costs 95%+ on code exploration. The leading MCP server for precise, symbol-level GitHub code retrieval via tree-sitter AST. Works with Claude Code, Cursor & any MCP client. 313B+ tokens saved. | [GitHub](https://github.com/jgravelle/jcodemunch-mcp) |
| 48 | **AssetOpsBench** | AssetOpsBench - Industry 4.0: A unified benchmark and framework for building, orchestrating, and evaluating domain-specific AI agents for Industry 4.0 asset operations and maintenance, with 460+ scenarios, 5 specialist agents (IoT, FMSR, TSFM, Work Order,...), and multi-agent orchestration blueprints (MetaAgent, AgentHive) over MCP. | [GitHub](https://github.com/IBM/AssetOpsBench) |
| 49 | **arc-kit** | The Enterprise Architecture Governance Harness — strategy, architecture, delivery, and assurance using AI coding assistants | [GitHub](https://github.com/tractorjuice/arc-kit) |
| 50 | **matlab-mcp-server** | Run MATLAB® using AI applications with the official MATLAB MCP Server from MathWorks®. This MCP server for MATLAB supports a wide range of coding agents like Claude Code® and Visual Studio® Code. | [GitHub](https://github.com/matlab/matlab-mcp-server) |
| 51 | **cve-mcp-server** | Production-grade MCP server giving Claude 27 security intelligence tools across 21 APIs — CVE lookup, EPSS scoring, CISA KEV, MITRE ATT&CK, Shodan, VirusTotal, and more. | [GitHub](https://github.com/mukul975/cve-mcp-server) |
| 52 | **docker-android** | Android in docker solution with noVNC supported, video recording and mcp server | TBD | [GitHub](https://github.com/budtmo/docker-android) |
| 53 | **drawio-skill** | From text & real sources to maintainable .drawio architecture models: Diagram IR with source-kind profiles, incremental sync preserving manual layout, multi-view projection, architecture-as-test with a CI action, query/review, what-if, accessible Story Mode, and a built-in MCP server | TBD | [GitHub](https://github.com/Agents365-ai/drawio-skill) |
| 54 | **wsl2-distro-manager** | GUI for the Windows Subsystem for Linux — and native Linux/macOS VMs on Mac. Install, back up, move and configure distros without CLI flags; AI assistant with tools, MCP server for agents, remote WSL over SSH. | TBD | [GitHub](https://github.com/bostrot/wsl2-distro-manager) |

### Database & Storage

MCP servers for accessing and managing databases and storage solutions.

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | postgres | Interact with PostgreSQL databases | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgres.md) |
| 2 | **MongoDB** | MongoDB database integration | [Docker Hub](https://hub.docker.com/r/mongodb/mongodb-mcp-server) |
| 3 | redis | Interact with Redis in-memory data structure store | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis.md) |
| 4 | elasticsearch | Search, analyze, and visualize data with Elasticsearch | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elasticsearch.md) |
| 5 | chroma | Interact with Chroma vector database for embeddings and retrieval | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/chroma.md) |
| 6 | neo4j-server | Graph database server management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-server.md) |
| 7 | astra-db | Interact with DataStax Astra DB, a cloud-native Cassandra database | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/astra-db.md) |
| 8 | neon | Serverless PostgreSQL database service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neon.md) |
| 9 | **Supabase** | Open source Firebase alternative | [GitHub](https://github.com/supabase/mcp-server-supabase) |
| 10 | tembo | Enhanced PostgreSQL database platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tembo.md) |
| 11 | **mcp-database-connector-lite** | Free, open-source SQLite MCP server with query execution, schema inspection, and data manipulation | [GitHub](https://github.com/tiranmoskovitch-dev/mcp-database-connector-lite) |
| 12 | **mysql_mcp_server** | MCP server that enables secure interaction with MySQL databases | [GitHub](https://github.com/designcomputer/mysql_mcp_server) |
| 13 | **mcp-server-mysql** | Read-only MCP server for MySQL — inspect schemas and execute read-only queries | [GitHub](https://github.com/benborla/mcp-server-mysql) |
| 14 | **mcp-server-qdrant** | Official Qdrant MCP server implementation for vector database integration | [GitHub](https://github.com/qdrant/mcp-server-qdrant) |
| 15 | **mcp-memory-service** | Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude | [GitHub](https://github.com/doobidoo/mcp-memory-service) |
| 16 | **XHS-Downloader** | 小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件 | [GitHub](https://github.com/JoeanAmier/XHS-Downloader) |
| 17 | **lamda** |  The most powerful Android RPA agent framework, next generation mobile automation. | [GitHub](https://github.com/firerpa/lamda) |
| 18 | **context-mode** | Context window optimization for AI coding agents. Sandboxes tool output, 98% reduction. 12 platforms | [GitHub](https://github.com/mksglu/context-mode) |
| 19 | **httprunner** | HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。 | [GitHub](https://github.com/httprunner/httprunner) |
| 20 | **codebase-memory-mcp** | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 66 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. | [GitHub](https://github.com/DeusData/codebase-memory-mcp) |
| 21 | **awesome-openclaw** | A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations. | [GitHub](https://github.com/SamurAIGPT/awesome-openclaw) |
| 22 | **mongodb-mcp-server** | A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters. | [GitHub](https://github.com/mongodb-js/mongodb-mcp-server) |
| 23 | **whodb** | Where data access meets operational intelligence | [GitHub](https://github.com/clidey/whodb) |
| 24 | **prest** | PostgreSQL ➕ REST, low-code, simplify and accelerate development, ⚡ instant, realtime, high-performance on any Postgres application, existing or new, MCP server | [GitHub](https://github.com/prest/prest) |
| 25 | **GoNavi** | High-performance multi-data-source database client — ~30MB, AI & MCP ready, zero Electron bloat. &#124; 高性能多数据源数据库客户端：约 30MB，AI 与 MCP 就绪，告别 Electron 膨胀。 | [GitHub](https://github.com/Syngnat/GoNavi) |
| 26 | **x64dbg-mcp-server** | x64dbg-MCP Server is a native MCP (Model Context Protocol) plugin for x64dbg that exposes the debugger's full functionality over HTTP. Connect any MCP-compatible AI assistant and control x64dbg programmatically: set breakpoints, step through code, read memory, dump registers, and more.  Built with Zig — zero dependencies, single-binary output, cros | [GitHub](https://github.com/duty1g/x64dbg-mcp-server) |

### Web & Content

MCP servers for web search, content access, and web automation.

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | brave | Perform web searches using Brave's privacy-focused search engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/brave.md) |
| 2 | notion | Create and manage content in Notion workspaces | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/notion.md) |
| 3 | puppeteer | Automate browser interactions and scrape web content | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/puppeteer.md) |
| 4 | duckduckgo | Privacy-focused web search engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/duckduckgo.md) |
| 5 | firecrawl | Web crawling and content extraction tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/firecrawl.md) |
| 6 | **ContextWire** | Free search API for AI agents with multi-engine support, multiple search profiles, and a remote MCP server (streamable-http). 1,000 free queries/month | [GitHub](https://github.com/keptlive/contextwire-mcp) |
| 7 | **exa-mcp-server** | Official Exa MCP server for web search and web crawling | [GitHub](https://github.com/exa-labs/exa-mcp-server) |
| 8 | **browser-tools-mcp** | Monitor browser logs and console directly from Cursor and other MCP-compatible IDEs | [GitHub](https://github.com/AgentDeskAI/browser-tools-mcp) |
| 9 | **apple-docs-mcp** | MCP server for Apple Developer Documentation — search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, and code examples | [GitHub](https://github.com/kimsungwhee/apple-docs-mcp) |
| 10 | **arxiv-mcp-server** | MCP server for searching and analyzing arXiv papers | [GitHub](https://github.com/blazickjp/arxiv-mcp-server) |
| 11 | **linkedin-mcp-server** | MCP server for accessing LinkedIn profiles, companies, jobs, and performing job searches | [GitHub](https://github.com/stickerdaniel/linkedin-mcp-server) |
| 12 | **browser-use-mcp-server** | MCP server for browser automation — browse the web directly from Cursor and other AI assistants | [GitHub](https://github.com/kontext-dev/browser-use-mcp-server) |
| 13 | **chrome-devtools-mcp** | Chrome DevTools MCP server for coding agents — inspect pages, capture logs, and debug | [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| 14 | **google_workspace_mcp** | Control Gmail, Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, and Drive with AI via MCP | [GitHub](https://github.com/taylorwilsdon/google_workspace_mcp) |
| 15 | **Scrapling** | 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! | [GitHub](https://github.com/D4Vinci/Scrapling) |
| 16 | **UI-TARS-desktop** | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra | [GitHub](https://github.com/bytedance/UI-TARS-desktop) |
| 17 | **gpt-researcher** | An autonomous agent that conducts deep research on any data using any LLM providers | [GitHub](https://github.com/assafelovic/gpt-researcher) |
| 18 | **Skill_Seekers** | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection | [GitHub](https://github.com/yusufkaraaslan/Skill_Seekers) |
| 19 | **Auto-claude-code-research-in-sleep** | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent. | [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) |
| 20 | **mcp** | Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser | [GitHub](https://github.com/BrowserMCP/mcp) |
| 21 | **deep-research** | Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server. | [GitHub](https://github.com/u14app/deep-research) |
| 22 | **mcpo** | A simple, secure MCP-to-OpenAPI proxy server | [GitHub](https://github.com/open-webui/mcpo) |
| 23 | **grafbase** | The Grafbase GraphQL Federation Gateway | [GitHub](https://github.com/grafbase/grafbase) |
| 24 | **mcp-server-browserbase** | Allow LLMs to control a browser with Browserbase and Stagehand | [GitHub](https://github.com/browserbase/mcp-server-browserbase) |
| 25 | **shadcn-ui-mcp-server** | A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native | [GitHub](https://github.com/Jpisnice/shadcn-ui-mcp-server) |
| 26 | **duckduckgo-mcp-server** | A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing. | [GitHub](https://github.com/nickclyde/duckduckgo-mcp-server) |
| 27 | **browser-use-mcp-server** | Browse the web, directly from Cursor etc. | [GitHub](https://github.com/kontext-security/browser-use-mcp-server) |
| 28 | **openagent** | ⚡️next-generation personal AI assistant powered by LLM, RAG and agent loops, supporting computer-use, browser-use and coding agent, demo: https://demo.openagentai.org | [GitHub](https://github.com/the-open-agent/openagent) |
| 29 | **Xquik MCP Server** | X/Twitter data extraction, account monitoring, webhooks, and API exploration via MCP | [GitHub](https://github.com/Xquik-dev/x-twitter-scraper) |
| 30 | **kaitoInfra/twitterapi-io-mcp-server** | Twitter/X data API for AI agents via MCP — tweet search with full operators, profiles, threads, real-time WebSocket streaming, trending topics. Hosted endpoint mcp.twitterapi.io/mcp ([twitterapi.io](https://twitterapi.io)) | [GitHub](https://github.com/kaitoInfra/twitterapi-io-mcp-server) |
| 31 | **QuantDinger** | AI quantitative trading platform for crypto, stocks, and forex with backtesting, live trading, market data, and multi-agent research.vibe-trading ,trading-agents,ai-trader,ai-trading | [GitHub](https://github.com/OpenByteInc/QuantDinger) |
| 32 | **semble** | Fast and Accurate Code Search for Agents. Uses 99% fewer tokens than grep+read | [GitHub](https://github.com/MinishLab/semble) |
| 33 | **nanobot** | Ultra-lightweight, open-source, self-hosted personal AI agent framework in Python with WebUI, tools, memory, MCP, multi-agent workflows, automation, and chat apps | [GitHub](https://github.com/HKUDS/nanobot) |
| 34 | **magic-mcp** | It's like v0, but in your Cursor / Claude Code / Windsurf: search 10,000+ React/Tailwind components, generate new UI with AI, and publish your own — right from your editor. Magic MCP is now the 21st MCP; this package keeps old configs working. Setup: 21st.dev/mcp | [GitHub](https://github.com/21st-dev/magic-mcp) |
| 35 | **wigolo** | The go-to web for your AI coding agent — local-first search, fetch, crawl & research over MCP. No API keys, no cloud, $0/query. Public beta. | [GitHub](https://github.com/KnockOutEZ/wigolo) |
| 36 | **stealth-browser-mcp** | The only browser automation that bypasses anti-bot systems. AI writes network hooks, clones UIs pixel-perfect via simple chat. | [GitHub](https://github.com/vibheksoni/stealth-browser-mcp) |
| 37 | **video-search-and-summarization** | NVIDIA AI Blueprint for video search and summarization (VSS) is a GPU-accelerated reference architecture for building video analytics agents with real-time verified alerts, visual Q&A, and automated reporting. The VSS Blueprint uses vision language models (VLMs) such as NVIDIA Cosmos, LLMs such as NVIDIA Nemotron, RAG, and NVIDIA NIMs. | [GitHub](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization) |
| 38 | **anysearch-mcp-server** | Unified real-time search MCP server supporting general web search, vertical domain search, parallel batch search, and full-page URL content extraction. | [GitHub](https://github.com/anysearch-ai/anysearch-mcp-server) |
| 39 | **vexa** | Open-source meeting transcription API for Google Meet, Microsoft Teams & Zoom. Auto-join bots, real-time WebSocket transcripts, MCP server for AI agents. Self-host or use hosted SaaS. | TBD | [GitHub](https://github.com/Vexa-ai/vexa) |

### Integrations & APIs

MCP servers for accessing external services and APIs.

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | stripe | Process payments and manage financial transactions | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/stripe.md) |
| 2 | shopify | Manage Shopify e-commerce stores and products | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/shopify.md) |
| 3 | **Packrift MCP** | Remote MCP server for packaging supplies: product search, live pricing, inventory, package-fit recommendations, shipping estimates, and cart URLs | [GitHub](https://github.com/Packrift/packrift-mcp) |
| 4 | **shopsavvy** | Complete product and pricing data solution - search products, compare prices, track history | [GitHub](https://github.com/shopsavvy/shopsavvy-mcp-server) |
| 5 | **agent-signal** | Collective intelligence for AI shopping agents - 23 tools for buyer intelligence, seller analytics, price alerts, and trend tracking | [GitHub](https://github.com/dan24ou-cpu/agent-signal) |
| 6 | **buywhere-mcp** | Real-time product search and price comparison across Singapore and SEA merchants (Lazada, Shopee, FairPrice, etc.) | [GitHub](https://github.com/BuyWhere/buywhere-mcp?utm_source=awesome-mcp-lists&utm_medium=referral&utm_campaign=june30_25k&utm_content=awesome-mcp-lists) |
| 7 | atlassian | Integrate with Atlassian products like Jira and Confluence | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlassian.md) |
| 8 | azure | Interact with Microsoft Azure cloud services and resources | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/azure.md) |
| 9 | google-maps | Geographic information and location services | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/google-maps.md) |
| 10 | slack | Send and receive messages in Slack workspaces | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/slack.md) |
| 11 | gdrive | Access and manage files in Google Drive | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gdrive.md) |
| 12 | box | Manage files and folders in Box cloud storage | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/box.md) |
| 13 | razorpay | Payment gateway and financial services platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/razorpay.md) |
| 14 | resend | Email delivery and management service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/resend.md) |
| 15 | **x402engine-mcp** | Connects agents to 108 x402 pay-per-call APIs: 72 LLMs plus image/video, web, code, crypto, audio, travel, and IPFS; supports Base, Solana, and MegaETH | [GitHub](https://github.com/agentc22/x402engine-mcp) |
| 16 | **mcp-api-bridge-lite** | Free REST API to MCP bridge — connect any REST API to AI assistants with simple YAML configuration, supporting GET, POST, PUT, DELETE with authentication | [GitHub](https://github.com/tiranmoskovitch-dev/mcp-api-bridge-lite) |
| 17 | **lightning-wallet-mcp** | Give AI agents a Bitcoin wallet with Lightning Network payments and L402 support | [GitHub](https://github.com/lightningfaucet/lightning-wallet-mcp) |
| 18 | **WritBase** | MCP-native task management for AI agent fleets | [GitHub](https://github.com/Writbase/writbase) |
| 19 | **agent-signal** | Collective intelligence for AI shopping agents — buyer intelligence, seller analytics, price alerts, and session logging | [GitHub](https://github.com/dan24ou-cpu/agent-signal) |
| 20 | **dexpaprika-mcp** | Real-time DEX data across multiple blockchains with pool, token, OHLCV, and trade data. Free, no API key | [GitHub](https://github.com/coinpaprika/dexpaprika-mcp) |
| 21 | **coinpaprika-mcp** | Crypto market data for thousands of coins and exchanges — tickers, OHLCV, historical prices. Free, no API key | [GitHub](https://github.com/coinpaprika/coinpaprika-mcp) |
| 22 | **TWZRD Agent Intel** | Solana-native trust scoring and x402 payment receipt MCP server for AI agents — free preflight, paid signed V5 trust receipt. Streamable-HTTP transport | [GitHub](https://intel.twzrd.xyz) |
| 23 | **nutrient-dws-mcp-server** | MCP server for Nutrient Document Web Services API — convert, merge, redact, sign, OCR, watermark, and extract documents | [GitHub](https://github.com/PSPDFKit/nutrient-dws-mcp-server) |
| 24 | **n8n-mcp-server** | MCP server for interacting with the n8n workflow automation API | [GitHub](https://github.com/leonardsellem/n8n-mcp-server) |
| 25 | **Gmail-MCP-Server** | MCP server for Gmail integration — read, search, send, and manage emails in Claude Desktop | [GitHub](https://github.com/jasonsum/Gmail-MCP-Server) |
| 26 | **short-video-maker** | Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API. | [GitHub](https://github.com/gyoridavid/short-video-maker) |
| 27 | **Sanka MCP Server** | Hosted remote MCP server for Sanka API, connecting AI agents to CRM and back-office workflows. | [GitHub](https://github.com/sankaHQ/sanka-mcp) |
| 28 | **mcp-notion-server** | A Model Context Protocol server for connecting Notion to MCP-compatible clients | [GitHub](https://github.com/suekou/mcp-notion-server) |
| 29 | **dpx-mcp** | Settlement protocol MCP server for institutional cross-border USDC transactions on Base mainnet. 14 tools: Stability Oracle (macro, FX, ESG, climate, supply chain, earth systems), ESG scoring, FX quotes, Verification of Payee, and settlement execution. x402 pay-per-call. MiCA-aligned. | [GitHub](https://github.com/untitledfinancial/dpx-mcp) |
| 30 | **apistatuscheck-mcp-server** | Live and historical availability for 285 public APIs and developer platforms across 29 categories — tell a third-party outage apart from a bug in your own code. 8 tools: status, uptime history, incident history, reliability ranking. Hosted Streamable HTTP, no API key. | [GitHub](https://github.com/shibley/apistatuscheck-mcp-server) |
| 31 | **ParlayAPI** | Sports odds and player props with your own API key and account allowances; build from the repository Dockerfile | [GitHub](https://github.com/JacobiusMakes/parlay-api-mcp) |

### AI & Machine Learning

MCP servers for AI and machine learning capabilities.

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | tavily | AI-powered web search and research assistant | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tavily.md) |
| 2 | perplexity-ask | AI-powered question answering system | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/perplexity-ask.md) |
| 3 | elevenlabs | AI voice generation and text-to-speech | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elevenlabs.md) |
| 4 | wolfram-alpha | Computational knowledge engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wolfram-alpha.md) |
| 5 | everart | AI art generation and manipulation | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/everart.md) |
| 6 | **OpenAI Compatible** | Any OpenAI SDK compatible API | [GitHub](https://github.com/imbactbulletz/any-chat-completions-mcp) |
| 7 | **Amazon Bedrock** | AWS AI services integration | [AWS Labs](https://github.com/awslabs/mcp) |
| 8 | **Amazon Nova Canvas** | AI image generation platform | [AWS Labs](https://github.com/awslabs/mcp) |
| 9 | **Roundtable** | Multi-model AI debate platform — GPT-4o, Claude, Gemini & 200+ models discuss, then synthesize insight | [GitHub](https://github.com/deadpixel/roundtable-dashboard) |
| 10 | **excel-mcp-server** | MCP server for reading and writing Microsoft Excel data | [GitHub](https://github.com/haris-musa/excel-mcp-server) |
| 11 | **jupyter-mcp-server** | MCP server for Jupyter notebooks — run code, manage kernels, and inspect outputs | [GitHub](https://github.com/dsp-ant/jupyter-mcp-server) |
| 12 | **mcp-server-chart** | Visualization MCP server with 25+ chart types using Ant Design Charts | [GitHub](https://github.com/antvis/mcp-server-chart) |
| 13 | **gemini-mcp-tool** | MCP server that lets AI assistants interact with Google Gemini CLI for additional AI capabilities | [GitHub](https://github.com/jamubc/gemini-mcp-tool) |
| 14 | **ida-pro-mcp** | AI-powered reverse engineering assistant that bridges IDA Pro with language models | [GitHub](https://github.com/mrexodia/ida-pro-mcp) |
| 15 | **n8n** | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. | [GitHub](https://github.com/n8n-io/n8n) |
| 16 | **gemini-cli** | An open-source AI agent that brings the power of Gemini directly into your terminal. | [GitHub](https://github.com/google-gemini/gemini-cli) |
| 17 | **context7** | Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors | [GitHub](https://github.com/upstash/context7) |
| 18 | **ruflo** | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration | [GitHub](https://github.com/ruvnet/ruflo) |
| 19 | **serena** | A powerful MCP toolkit for coding, providing semantic retrieval and editing capabilities  - the IDE for your agent | [GitHub](https://github.com/oraios/serena) |
| 20 | **activepieces** | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents | [GitHub](https://github.com/activepieces/activepieces) |
| 21 | **MaxKB** | 🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。 | [GitHub](https://github.com/1Panel-dev/MaxKB) |
| 22 | **nuclear** | Streaming music player that finds free music for you | [GitHub](https://github.com/nukeop/nuclear) |
| 23 | **trigger.dev** | Trigger.dev – build and deploy fully‑managed AI agents and workflows | [GitHub](https://github.com/triggerdotdev/trigger.dev) |
| 24 | **OpenMetadata** | OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. | [GitHub](https://github.com/open-metadata/OpenMetadata) |
| 25 | **mcp-use** | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents. | [GitHub](https://github.com/mcp-use/mcp-use) |
| 26 | **xiaozhi-esp32-server** | 本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server. | [GitHub](https://github.com/xinnan-tech/xiaozhi-esp32-server) |
| 27 | **Viper** | Adversary simulation and Red teaming platform with AI | [GitHub](https://github.com/FunnyWolf/Viper) |
| 28 | **fastmcp** | 🚀 The fast, Pythonic way to build MCP servers and clients. | [GitHub](https://github.com/PrefectHQ/fastmcp) |
| 29 | **unity-mcp** | Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. | [GitHub](https://github.com/CoplayDev/unity-mcp) |
| 30 | **Upsonic** | Agent Framework For Fintech and Banks | [GitHub](https://github.com/Upsonic/Upsonic) |
| 31 | **cursor-talk-to-figma-mcp** | TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically. | [GitHub](https://github.com/grab/cursor-talk-to-figma-mcp) |
| 32 | **awesome-mcp-servers** | Awesome MCP Servers - A curated list of Model Context Protocol servers | [GitHub](https://github.com/appcypher/awesome-mcp-servers) |
| 33 | **5ire** | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers . | [GitHub](https://github.com/nanbingxyz/5ire) |
| 34 | **casibase** | ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com | [GitHub](https://github.com/casibase/casibase) |
| 35 | **markdownify-mcp** | A Model Context Protocol server for converting almost anything to Markdown | [GitHub](https://github.com/zcaceres/markdownify-mcp) |
| 36 | **generative-ai** | Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation. | [GitHub](https://github.com/genieincodebottle/generative-ai) |
| 37 | **mcphub.nvim** | An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins. | [GitHub](https://github.com/ravitemer/mcphub.nvim) |
| 38 | **jadx-ai-mcp** | Plugin for JADX to integrate MCP server | [GitHub](https://github.com/zinja-coder/jadx-ai-mcp) |
| 39 | **pilot-shell** | Make Claude Code production-ready — spec-driven plans, enforced quality gates, persistent knowledge | [GitHub](https://github.com/maxritter/pilot-shell) |
| 40 | **mcp-unity** | Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs | [GitHub](https://github.com/CoderGamester/mcp-unity) |
| 41 | **code-mode** | 🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution.  | [GitHub](https://github.com/universal-tool-calling-protocol/code-mode) |
| 42 | **korean-law-mcp** | 국가법령정보MCP &#124; 법제처 41개 API → 14개 MCP 도구. 법령·판례·조례·조약을 AI로 검색·조회·분석 &#124; 41 Korean legal APIs → 14 MCP tools | [GitHub](https://github.com/chrisryugj/korean-law-mcp) |
| 43 | **nerve** | The Simple Agent Development Kit. | [GitHub](https://github.com/evilsocket/nerve) |
| 44 | **tuui** | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration. | [GitHub](https://github.com/AI-QL/tuui) |
| 45 | **MassGen** | 🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. &#124; Join us on Discord: discord.massgen.ai | [GitHub](https://github.com/massgen/MassGen) |
| 46 | **MCP-Bridge** | A middleware to provide an openAI compatible endpoint that can call MCP tools | [GitHub](https://github.com/SecretiveShell/MCP-Bridge) |
| 47 | **arcade-mcp** | The best way to create, deploy, and share MCP Servers | [GitHub](https://github.com/ArcadeAI/arcade-mcp) |
| 48 | **awesome-mcp-servers** | A collection of MCP servers. | [GitHub](https://github.com/punkpeye/awesome-mcp-servers) |
| 49 | **pal-mcp-server** | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. | [GitHub](https://github.com/BeehiveInnovations/pal-mcp-server) |
| 50 | **slack-mcp-server** | The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic. | [GitHub](https://github.com/korotovsky/slack-mcp-server) |
| 51 | **docs-mcp-server** | Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools | [GitHub](https://github.com/arabold/docs-mcp-server) |
| 52 | **ros-mcp-server** | Connect AI models like Claude & GPT with robots using MCP and ROS. | [GitHub](https://github.com/robotmcp/ros-mcp-server) |
| 53 | **Awesome-MCP-Servers** | A curated list of Model Context Protocol (MCP) servers  | [GitHub](https://github.com/YuzeHao2023/Awesome-MCP-Servers) |
| 54 | **jupyter-mcp-server** | 🪐 🔧 Model Context Protocol (MCP) Server for Jupyter. | [GitHub](https://github.com/datalayer/jupyter-mcp-server) |
| 55 | **douyin-mcp-server** | 提取抖音无水印视频链接，视频文案，douyin-mcp-server，mcp，claude skill，支持龙虾 | [GitHub](https://github.com/yzfly/douyin-mcp-server) |
| 56 | **openapi-mcp-server** | Allow AI to wade through complex OpenAPIs using Simple Language | [GitHub](https://github.com/janwilmake/openapi-mcp-server) |
| 57 | **mcp-language-server** | mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics. | [GitHub](https://github.com/isaacphi/mcp-language-server) |
| 58 | **Office-Word-MCP-Server** | A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities. | [GitHub](https://github.com/GongRzhe/Office-Word-MCP-Server) |
| 59 | **MODULAR-RAG-MCP-SERVER** | A modular RAG (Retrieval-Augmented Generation) system with MCP Server architecture. Using Skill to make AI follow each step of the spec and complete the code 100% by AI. | [GitHub](https://github.com/jerry-ai-dev/MODULAR-RAG-MCP-SERVER) |
| 60 | **lemonade** | Lemonade helps users discover and run local AI apps by serving optimized LLMs right from their own GPUs and NPUs. Join our discord: https://discord.gg/5xXzkMu8Zk | [GitHub](https://github.com/lemonade-sdk/lemonade) |
| 61 | **MeiGen-AI-Design-MCP** | Supports GPT Image 2, Nanobanana & ComfyUI, with a 1,400+ prompt library, carefully crafted hooks and a multi-task orchestration system | [GitHub](https://github.com/jau123/MeiGen-AI-Design-MCP) |
| 62 | **google-meta-ads-ga4-mcp** | MCP server for Google Ads, Meta Ads & GA4 — works with ChatGPT, Claude, Cursor, n8n, Windsurf & more. 250+ tools for campaign management, analytics & optimization. | [GitHub](https://github.com/irinabuht12-oss/google-meta-ads-ga4-mcp) |
| 63 | **cocos-mcp-server** | 一款全面的、便捷的cocos creator AI MCP服务插件，适用于3.8.0以上cocos版本，一键安装，一键启动。A comprehensive and convenient cocos creator AI MCP service plug-in, suitable for cocos versions above 3.8.0, one-click installation and one-click start. | [GitHub](https://github.com/DaxianLee/cocos-mcp-server) |
| 64 | **RunAPI** | MCP server for model discovery and AI image, video, music/audio, text-to-speech, and LLM jobs via RunAPI | [GitHub](https://github.com/runapi-ai/mcp) |
| 65 | **NotFair** | Open-source Claude Code skills for SEO, GEO, Google Ads, and Meta Ads — connects to live data via Google Ads MCP, Meta Ads MCP, Google Search Console MCP, and Google Analytics (GA4) MCP | [GitHub](https://github.com/nowork-studio/NotFair) |
| 66 | **reactive-resume** | A one-of-a-kind resume builder that keeps your privacy in mind. Completely secure, customizable, portable, open-source and free forever. Try it out today! | [GitHub](https://github.com/amruthpillai/reactive-resume) |
| 67 | **FunASR** | Open-source speech recognition toolkit for training, inference, streaming ASR, VAD, punctuation, speaker diarization pipelines, and OpenAI-compatible/MCP serving. | [GitHub](https://github.com/modelscope/FunASR) |
| 68 | **unstract** | LLM-Driven Extraction of Unstructured Data — Built for API Deployments & ETL Pipeline Workflows | [GitHub](https://github.com/Zipstack/unstract) |
| 69 | **blender-mcp** | Community plugin to control Blender 3D with any LLM of your choice | [GitHub](https://github.com/ahujasid/blender-mcp) |
| 70 | **awesome-agentic-ai-zh** | A trilingual (繁中 / English / 简中) learning roadmap for agentic AI: from LLM basics to multi-agent systems, with 240+ curated resources and hands-on examples. 中文 AI agent 學習地圖。 | [GitHub](https://github.com/WenyuChiou/awesome-agentic-ai-zh) |
| 71 | **ableton-mcp** | 🎵 Control Ableton Live with Claude AI — create tracks, arrange clips & compose music via MCP | [GitHub](https://github.com/ahujasid/ableton-mcp) |
| 72 | **nitrostack** | The full-stack TypeScript framework to build, test, and deploy production-ready MCP servers and AI-native apps. | [GitHub](https://github.com/nitrocloudofficial/nitrostack) |
| 73 | **open-codex-computer-use** | 👾 Open Computer Use – Open-Source Alternative to Codex Computer Use | [GitHub](https://github.com/iFurySt/open-codex-computer-use) |

## MCP Clients

### Desktop Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | **[Claude Desktop](https://www.anthropic.com/claude)** | Official Claude client with native MCP support | Windows, macOS |
| 2 | **[Cursor AI](https://www.cursor.com/)** | AI-powered code editor with MCP support | Windows, macOS, Linux |
| 3 | **[Windsurf](https://codeium.com/windsurf)** | AI browser with MCP integration | macOS |
| 4 | **[Cline](https://github.com/cline/cline)** | Terminal-based chat client with MCP support | Windows, macOS, Linux |
| 5 | **[MetaMCP](https://github.com/metatool-ai/metatool-app)** | Unified middleware MCP client | Windows, macOS, Linux |
| 6 | **[Continue.dev](https://github.com/continuedev/continue)** | AI coding assistant for IDEs | VS Code, JetBrains |
| 7 | **[MCPlato](https://mcplato.com/)** | Local-first desktop AI workspace with workspace-scoped MCP configuration and permission-aware tool use | Windows, macOS |
| 8 | **[KyttoMCP](https://kytto.jakubhecht.sk/)** | Local control panel that manages MCP server configuration across Claude Desktop, Claude
  Code, Cursor, VS Code and Codex from one matrix | Windows, macOS |

### Mobile Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | Claude Mobile | Mobile Claude client with MCP support | iOS, Android |
| 2 | [AI Assistant](https://apps.apple.com/app/ai-assistant-chat-with-ai/id6737047893) | Multi-model mobile client with MCP | iOS |

### IDE Extensions

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | [VS Code AI Assistant](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot-chat) | VS Code extension with MCP support | VS Code |
| 2 | [JetBrains AI Assistant](https://www.jetbrains.com/ai/) | JetBrains IDE extension with MCP | JetBrains IDEs |
| 3 | [GitHub Copilot Chat](https://github.com/features/copilot) | GitHub's AI assistant with MCP capabilities | VS Code, Visual Studio, JetBrains |

### Command Line Tools

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | [Claude CLI](https://docs.anthropic.com/en/docs/claude-code/overview) | Command-line interface for Claude with MCP | Windows, macOS, Linux |
| 2 | [MCP CLI](https://github.com/wong2/mcp-cli) | General MCP client for command line | Windows, macOS, Linux |
| 3 | [mark3labs/mcphost](https://github.com/mark3labs/mcphost) | CLI host for MCP interactions | Windows, macOS, Linux |

### Web Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | [Claude Web](https://claude.ai) | Web interface for Claude with MCP support | Web |
| 2 | [Glama AI](https://glama.ai) | Web-based multi-model client with MCP | Web |
| 3 | [Phind](https://www.phind.com) | Developer-focused search with MCP | Web |
| 4 | [Ontheia](https://ontheia.ai) | Self-hosted, open-source AI agent platform with native MCP support. Multi-provider, GDPR by design. | Web, Linux, MacOS, Windows |
| 5 | [FLUJO](https://github.com/mario-andreschak/FLUJO) | Local-first visual AI agent builder and MCP client with server management, tool inspection, multi-model chat, and Docker deployment | Web, Windows, macOS, Linux |

## MCP Toolkits

### SDKs & Libraries

| # | Tool Name | Language | Description | GitHub Stars | GitHub |
|---|-----------|----------|-------------|-------------|-------------|
| 1 | FastMCP | TypeScript | High-level framework for building MCP servers in TypeScript | 1000+ | [GitHub](https://github.com/fastrepl/fastmcp) |
| 2 | FastMCP (Python) | Python | High-level framework for building MCP servers in Python | 800+ | [GitHub](https://github.com/fastrepl/fastmcp-python) |
| 3 | LiteMCP | TypeScript | A lightweight TypeScript framework for building MCP servers | 600+ | [GitHub](https://github.com/wong2/LiteMCP) |
| 4 | mcp-framework | TypeScript | Fast and elegant TypeScript framework for building MCP servers | 400+ | [GitHub](https://github.com/QuantGeekDev/mcp-framework) |
| 5 | mcp-use | Python | Open source Python library to easily connect any LLM to any MCP server | 350+ | [GitHub](https://github.com/astelmach01/mcp-use) |
| 6 | MCP Fusion | TypeScript | Zero-config framework for building production-ready MCP servers with auto tool discovery, multi-transport (stdio/SSE/HTTP) and Zod validation | [GitHub](https://github.com/vinkius-labs/mcp-fusion) |

### Frameworks

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | [lastmile-ai/mcp-agent](https://github.com/lastmile-ai/mcp-agent) | TypeScript | Build agents with MCP servers |
| 2 | [mcpdotdirect/template-mcp-server](https://github.com/mcpdotdirect/template-mcp-server) | TypeScript | CLI tool for new MCP servers |
| 3 | [stephencme/create-mcp-ts](https://github.com/stephencme/create-mcp-ts) | TypeScript | MCP server creator with templates |
| 4 | [Upsonic/gpt-computer-assistant](https://github.com/Upsonic/gpt-computer-assistant) | Python | Framework for AI agents |
| 5 | [p-funk/FEGIS](https://github.com/p-funk/FEGIS) | Python | Interactive agent framework |


## Agent Development Frameworks

| # | Framework Name | Language | Description | Link |
|---|----------------|----------|-------------|------|
| 1 | mcp-agent | TypeScript | Build effective agents with MCP servers using simple, composable patterns | [GitHub](https://github.com/lastmile-ai/mcp-agent) |
| 2 | gpt-computer-assistant | Python | Framework to build vertical AI agent with MCP integration | [GitHub](https://github.com/Upsonic/gpt-computer-assistant) |
| 3 | FEGIS | Python | A semantic programming framework for LLMs with MCP support | [GitHub](https://github.com/p-funk/FEGIS) |
| 4 | langchain-mcp | Python | LangChain integration for MCP | [GitHub](https://github.com/langchain-ai/langchain-mcp) |
| 5 | solana-agent-kit | TypeScript | Solana MCP SDK for blockchain agent development | [GitHub](https://github.com/sendaifun/solana-agent-kit) |
| 6 | EGC | TypeScript | Persistent cross-session memory MCP server for 13+ AI coding tools. SQLite-backed state survives context resets. | [GitHub](https://github.com/Fmarzochi/EGC) |

## Language-Specific SDKs

| # | SDK Name | Language | Description | Link |
|---|----------|----------|-------------|------|
| 1 | spring-ai-mcp | Java | Java SDK and Spring Framework integration for building MCP servers | [GitHub](https://github.com/spring-projects-experimental/spring-ai-mcp) |
| 2 | mark3labs/mcp-go | Go | Golang SDK for building MCP Servers and Clients | [GitHub](https://github.com/mark3labs/mcp-go) |
| 3 | foxy-contexts | Go | Golang library to write MCP Servers declaratively with testing included | [GitHub](https://github.com/strowk/foxy-contexts) |
| 4 | mcp-rs-template | Rust | MCP CLI server template for Rust | [GitHub](https://github.com/linux-china/mcp-rs-template) |
| 5 | ModelContextProtocol.NET | C# | A C# SDK for building MCP servers on .NET | [GitHub](https://github.com/salty-flower/ModelContextProtocol.NET) |
| 6 | http4k MCP SDK | Kotlin | Functional, testable Kotlin SDK for MCP | [GitHub](https://github.com/http4k/http4k) |
| 7 | mcpc | C | Modern C SDK for building MCP servers/clients | [GitHub](https://github.com/micl2e2/mcpc) |

### Testing Tools

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | [modelcontextprotocol/inspector](https://github.com/modelcontextprotocol/inspector) | TypeScript | Official UI for testing MCP servers |
| 2 | [wong2/mcp-cli](https://github.com/wong2/mcp-cli) | Multiple | Command line inspector for testing |
| 3 | [mclenhard/mcp-evals](https://github.com/mclenhard/mcp-evals) | Multiple | Package for running evaluations |
| 4 | [Typewise/mcp-chaos-rig](https://github.com/Typewise/mcp-chaos-rig) | TypeScript | Fault injection server for testing MCP clients against auth failures, disappearing tools, flaky responses, and token expiry |
| 5 | [MCP Config Doctor fixtures](https://github.com/supoju/mcp-config-doctor-fixtures) | Config fixtures | Redaction-safe Codex, Gemini CLI, and VS Code MCP client fixtures for validator tests and bug reports |
| 6 | [Agent QA](https://github.com/vostride/agent-qa) | TypeScript | Local stdio MCP server for natural-language web and mobile regression tests with retained execution evidence |

### Utilities

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | hamidra/yamcp | TypeScript | MCP workspace manager |
| 2 | punkpeye/mcp-proxy | TypeScript | SSE proxy for MCP servers |
| 3 | multi-mcp | Python | Multi-MCP Proxy Server |
| 4 | f/MCPTools | Go | CLI tool for MCP server interactions |
| 5 | portel-dev/ncp | TypeScript | MCP orchestrator with intelligent discovery, 98.2% accuracy, and 94.8% token savings. Transforms 100+ tools into 2 unified interfaces. [GitHub](https://github.com/portel-dev/ncp) |
| 6 | strowk/mcp-autotest | Go | YAML-based autotest tool |
| 7 | [MCP Lens](https://github.com/labmimors/dsh-mcp-lens) | TypeScript | DeepSeek Harness plugin that exposes configured MCP catalogs through two model-facing interfaces with allow/deny policy gates and lazy connections |

### Hosting Solutions

| # | Tool Name | Description |
|---|-----------|-------------|
| 1 | Glama | Platform for hosting open-source MCP servers |
| 2 | Smithery | Cloud hosting for MCP servers via containers |
| 3 | [ToolRouter](https://toolrouter.com) | Give your AI agent superpowers with access to 150+ tools on demand with just one account. Competitor research, video production, web search, image generation, security scanning, and more. One API key replaces managing dozens of provider accounts. `npx -y toolrouter-mcp` |

### Templates

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | fastmcp-boilerplate | TypeScript | MCP server built with FastMCP |
| 2 | dart-mcp-server-template | Dart | Template for Dart MCP servers |
| 3 | rails-mcp-startup-boilerplate | Ruby | Rails template for paid MCP servers |

## Docker MCP Toolkit

Docker provides a comprehensive MCP Toolkit with over 100 pre-built MCP servers that are ready to use with Claude and other MCP clients.

There are currently 110 MCP servers available:

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | github | Manage GitHub repositories and perform Git operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 2 | docker | Integrate with Docker to manage containers, images, and networks | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 3 | kubernetes | Orchestrate and manage containerized applications with Kubernetes | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 4 | puppeteer | Automate browser interactions and scrape web content | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/puppeteer.md) |
| 5 | stripe | Process payments and manage financial transactions | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/stripe.md) |
| 6 | slack | Send and receive messages in Slack workspaces | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/slack.md) |
| 7 | postgres | Interact with PostgreSQL databases | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgres.md) |
| 8 | redis | Interact with Redis in-memory data structure store | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis.md) |
| 9 | brave | Perform web searches using Brave's privacy-focused search engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/brave.md) |
| 10 | notion | Create and manage content in Notion workspaces | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/notion.md) |
| 11 | elasticsearch | Search, analyze, and visualize data with Elasticsearch | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elasticsearch.md) |
| 12 | gitlab | Interact with GitLab repositories and CI/CD pipelines | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gitlab.md) |
| 13 | azure | Interact with Microsoft Azure cloud services and resources | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/azure.md) |
| 14 | gdrive | Access and manage files in Google Drive | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gdrive.md) |
| 15 | grafana | Create and manage Grafana dashboards and visualizations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/grafana.md) |
| 16 | obsidian | Work with Obsidian notes and knowledge management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/obsidian.md) |
| 17 | atlassian | Integrate with Atlassian products like Jira and Confluence | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlassian.md) |
| 18 | tavily | AI-powered web search and research assistant | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tavily.md) |
| 19 | shopify | Manage Shopify e-commerce stores and products | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/shopify.md) |
| 20 | sentry | Monitor application errors and performance | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/sentry.md) |
| 21 | 302_sandbox | A sandbox environment for testing HTTP redirects and status codes | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/302_sandbox.md) |
| 22 | 3d-printer | Control and monitor 3D printers with slice file management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/3d-printer.md) |
| 23 | armor-crypto | Secure encryption and decryption tools for sensitive data | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/armor-crypto.md) |
| 24 | astra-db | Interact with DataStax Astra DB, a cloud-native Cassandra database | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/astra-db.md) |
| 25 | atlas-docs | Access MongoDB Atlas documentation and best practices | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlas-docs.md) |
| 26 | audiense-insights | Access audience analytics and marketing insights data | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/audiense-insights.md) |
| 27 | aws-kb-retrieval-server | Retrieve information from AWS Knowledge Bases | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/aws-kb-retrieval-server.md) |
| 28 | barryyip0625-mcp-discord | Communicate with Discord servers and channels | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/barryyip0625-mcp-discord.md) |
| 29 | basic-memory | Simple memory persistence for AI conversations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/basic-memory.md) |
| 30 | bitrefill | Purchase gift cards and mobile refills with cryptocurrency | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/bitrefill.md) |
| 31 | box | Manage files and folders in Box cloud storage | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/box.md) |
| 32 | chroma | Interact with Chroma vector database for embeddings and retrieval | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/chroma.md) |
| 33 | circleci | Manage CI/CD pipelines and workflows in CircleCI | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/circleci.md) |
| 34 | context7 | Provide contextual information for enhanced AI conversations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/context7.md) |
| 35 | cyreslab-ai-shodan | Search for internet-connected devices using Shodan | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/cyreslab-ai-shodan.md) |
| 36 | dappier | Access real-time data from trusted sources across multiple domains | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/dappier.md) |
| 37 | dart | Manage projects and tasks in Dart project management tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/dart.md) |
| 38 | databutton | Build and deploy data apps with Python and Streamlit | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/databutton.md) |
| 39 | descope | Implement secure user authentication and authorization | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/descope.md) |
| 40 | desktop-commander | Control desktop applications and perform system operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/desktop-commander.md) |
| 41 | devhub-cms | Manage content with DevHub CMS | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/devhub-cms.md) |
| 42 | doit | Task management and productivity tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/doit.md) |
| 43 | duckduckgo | Privacy-focused web search engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/duckduckgo.md) |
| 44 | e2b | Cloud-based development environment | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/e2b.md) |
| 45 | edubase | Education management platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/edubase.md) |
| 46 | elevenlabs | AI voice generation and text-to-speech | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elevenlabs.md) |
| 47 | everart | AI art generation and manipulation | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/everart.md) |
| 48 | exa | Advanced replacement for the traditional ls command | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/exa.md) |
| 49 | fetch | Web content retrieval tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fetch.md) |
| 50 | fibery | Connected work platform for knowledge management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fibery.md) |
| 51 | filesystem | Interact with file system and perform file operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/filesystem.md) |
| 52 | firecrawl | Web crawling and content extraction tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/firecrawl.md) |
| 53 | flexprice | Dynamic pricing solution for businesses | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/flexprice.md) |
| 54 | github-chat | GitHub discussions and collaboration integration | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github-chat.md) |
| 55 | github-official | Official GitHub API integration | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github-official.md) |
| 56 | glif | Blockchain and crypto management platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/glif.md) |
| 57 | google-maps | Geographic information and location services | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/google-maps.md) |
| 58 | gyazo | Screenshot capturing and sharing service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gyazo.md) |
| 59 | hackle | Feature flag and experiment management platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hackle.md) |
| 60 | handwriting-ocr | Optical character recognition for handwritten text | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/handwriting-ocr.md) |
| 61 | heroku | Cloud platform as a service (PaaS) | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/heroku.md) |
| 62 | husqvarna-automower | Control and monitor Husqvarna robotic lawn mowers | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/husqvarna-automower.md) |
| 63 | hyperbrowser | Advanced web browsing and automation tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hyperbrowser.md) |
| 64 | hyperspell | AI-powered grammar and spelling checking | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hyperspell.md) |
| 65 | iaptic | Subscription and payment management tool | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/iaptic.md) |
| 66 | jetbrains | Integrate with JetBrains IDEs and tools | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/jetbrains.md) |
| 67 | kagisearch | Neural search engine for web content | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kagisearch.md) |
| 68 | kong | API gateway and service mesh platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kong.md) |
| 69 | lara | AI-powered content research and writing assistant | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/lara.md) |
| 70 | line | Messaging application and platform integration | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/line.md) |
| 71 | mcp-discord | Discord messaging and community management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-discord.md) |
| 72 | mcp-notion-server | Notion workspace integration and management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-notion-server.md) |
| 73 | multiversx-mx | Blockchain infrastructure and smart contract platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/multiversx-mx.md) |
| 74 | neo4j-cloud-aura-api | Managed graph database cloud service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-cloud-aura-api.md) |
| 75 | neo4j-cypher | Graph database query language and integration | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-cypher.md) |
| 76 | neo4j-memory | In-memory storage for Neo4j operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-memory.md) |
| 77 | neo4j-server | Graph database server management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-server.md) |
| 78 | neon | Serverless PostgreSQL database service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neon.md) |
| 79 | neondatabase-labs | Experimental features for Neon database | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neondatabase-labs.md) |
| 80 | octomind | Automated testing and quality assurance platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/octomind.md) |
| 81 | openapi-schema | API definition and documentation standard | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/openapi-schema.md) |
| 82 | opik | Advanced image processing and generation | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/opik.md) |
| 83 | osp_marketing_tools | Online marketing and promotion tools | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/osp_marketing_tools.md) |
| 84 | oxylabs | Web scraping and data extraction tools | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/oxylabs.md) |
| 85 | perplexity-ask | AI-powered question answering system | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/perplexity-ask.md) |
| 86 | playwright | Browser automation and testing framework | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/playwright.md) |
| 87 | postgresql | Object-relational database system | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgresql.md) |
| 88 | pulumi | Infrastructure as code platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/pulumi.md) |
| 89 | razorpay | Payment gateway and financial services platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/razorpay.md) |
| 90 | redis-cloud | Managed Redis database service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis-cloud.md) |
| 91 | resend | Email delivery and management service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/resend.md) |
| 92 | risken | Security risk management platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/risken.md) |
| 93 | scrapegraph | Web scraping and data visualization | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/scrapegraph.md) |
| 94 | scrapezy | Automated web scraping and data extraction | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/scrapezy.md) |
| 95 | smithery-cli | Command-line interface for Smithery platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/smithery-cli.md) |
| 96 | tembo | Enhanced PostgreSQL database platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tembo.md) |
| 97 | time | Time management and tracking utilities | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/time.md) |
| 98 | triplewhale | E-commerce analytics and marketing platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/triplewhale.md) |
| 99 | tweetbinder | Twitter/X analytics and social media insights | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tweetbinder.md) |
| 100 | v-3-discordmcp | Discord messaging and community management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/v-3-discordmcp.md) |
| 101 | veyrax | Web application security and testing platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/veyrax.md) |
| 102 | webflow | Visual website design and content management system | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/webflow.md) |
| 103 | wikipedia-mcp | Wikipedia knowledge retrieval | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wikipedia-mcp.md) |
| 104 | wolfram-alpha | Computational knowledge engine | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wolfram-alpha.md) |
| 105 | youtube_transcript | YouTube video transcript extraction | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/youtube_transcript.md) |
| 106 | docker | Manage Docker containers, images, and Docker Hub | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 107 | github | Manage GitHub repositories and perform Git operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 108 | kubernetes | Orchestrate and manage containerized applications | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 109 | postgresql | Interact with PostgreSQL databases | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgresql.md) |

### Security & Authentication

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | sentry | Monitor application errors and performance | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/sentry.md) |
| 2 | cyreslab-ai-shodan | Search for internet-connected devices using Shodan | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/cyreslab-ai-shodan.md) |
| 3 | descope | Implement secure user authentication and authorization | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/descope.md) |
| 4 | armor-crypto | Secure encryption and decryption tools for sensitive data | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/armor-crypto.md) |
| 5 | **VirusTotal** | File and URL security analysis | [GitHub](https://github.com/skydeckai/virustotal-mcp-server) |
| 6 | risken | Security risk management platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/risken.md) |
| 7 | **Agent Module** | EU AI Act compliance logic for autonomous agents — risk classification, prohibited practices, transparency obligations, GDPR data protection. Free 24hr trial, self-provisioned via MCP | [GitHub](https://github.com/AgentModule/mcp) |
| 8 | **damn-vulnerable-MCP-server** | Intentionally vulnerable MCP server for security research, training, and CTF exercises | [GitHub](https://github.com/harishsg993010/damn-vulnerable-MCP-server) |
| 9 | **operant-mcp** | Open-source MCP server with 51 security testing tools for pentesting, vulnerability scanning, and security auditing | [GitHub](https://github.com/operantlabs/operant-mcp) |
| 10 | **mcp-for-beginners** | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. | [GitHub](https://github.com/microsoft/mcp-for-beginners) |
| 11 | **fastapi_mcp** | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! | [GitHub](https://github.com/tadata-org/fastapi_mcp) |
| 12 | **klavis** | Klavis AI:  MCP integration platforms that let AI agents use tools reliably at any scale | [GitHub](https://github.com/Klavis-AI/klavis) |
| 13 | **osaurus** | Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source. | [GitHub](https://github.com/osaurus-ai/osaurus) |
| 14 | **ENScan_GO** | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入 | [GitHub](https://github.com/wgpsec/ENScan_GO) |
| 15 | **Gmail-MCP-Server** | A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions. | [GitHub](https://github.com/GongRzhe/Gmail-MCP-Server) |
| 16 | **open-connector** | Open-source auth gateway connecting 1000+ SaaS providers to AI agents through SDK, CLI, MCP, HTTP, and OpenAPI. | [GitHub](https://github.com/oomol-lab/open-connector) |
| 17 | **tradingview-mcp** | TradingView MCP server — real-time market data, technical analysis, screeners & backtesting for Claude, ChatGPT, Cursor & any MCP client. Stocks, crypto, forex & futures across global exchanges. Hosted or self-host. | [GitHub](https://github.com/atilaahmettaner/tradingview-mcp) |
| 18 | **codex-with-chatgpt** | ChatGPT thinks. Codex works. Use ChatGPT as the planning brain while keeping the Codex harness. | TBD | [GitHub](https://github.com/XiaoDuoYa/codex-with-chatgpt) |

### Development Tools

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | filesystem | Interact with file system and perform file operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/filesystem.md) |
| 2 | e2b | Cloud-based development environment | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/e2b.md) |
| 3 | octomind | Automated testing and quality assurance platform | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/octomind.md) |
| 4 | openapi-schema | API definition and documentation standard | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/openapi-schema.md) |
| 5 | desktop-commander | Control desktop applications and perform system operations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/desktop-commander.md) |
| 6 | **Roundtable** | **Zero-configuration MCP server that unifies multiple AI coding assistants (Claude Code, Cursor, GPT-4) for enhanced development workflows** | [GitHub](https://github.com/askbudi/roundtable) |
| 7 | **Asynkor** | Coordination layer for AI agent teams — file leasing, shared memory, cross-machine sync. One MCP server for Claude Code, Cursor, Windsurf | [GitHub](https://github.com/asynkor/asynkor) |
| 8 | **n8n-mcp** | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you  | [GitHub](https://github.com/czlonkowski/n8n-mcp) |
| 9 | **xiaohongshu-mcp** | MCP for xiaohongshu.com | [GitHub](https://github.com/xpzouying/xiaohongshu-mcp) |
| 10 | **Awesome-MCP-ZH** | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients | [GitHub](https://github.com/yzfly/Awesome-MCP-ZH) |
| 11 | **XcodeBuildMCP** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | [GitHub](https://github.com/getsentry/XcodeBuildMCP) |
| 12 | **fast-agent** | Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP Support | [GitHub](https://github.com/evalstate/fast-agent) |
| 13 | **memory-bank-mcp** | A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank. | [GitHub](https://github.com/alioshr/memory-bank-mcp) |
| 14 | **awesome-mcp-servers** | A curated list of Model Context Protocol (MCP) servers | [GitHub](https://github.com/wong2/awesome-mcp-servers) |
| 15 | **Office-PowerPoint-MCP-Server** | A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol. | [GitHub](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) |
| 16 | **mcp-server-guide** | A guide on how to use the Figma MCP server | [GitHub](https://github.com/figma/mcp-server-guide) |
| 17 | **drawio-mcp-server** | Draw.io Model Context Protocol (MCP) Server | [GitHub](https://github.com/lgazo/drawio-mcp-server) |
| 18 | **awesome-remote-mcp-servers** | Remote MCP Servers | [GitHub](https://github.com/jaw9c/awesome-remote-mcp-servers) |
| 19 | **excel-mcp-server** | A Model Context Protocol (MCP) server that reads and writes MS Excel data | [GitHub](https://github.com/negokaz/excel-mcp-server) |
| 20 | **server** | Core PHP implementation for the Model Context Protocol (MCP) server | [GitHub](https://github.com/php-mcp/server) |
| 21 | **gadgethumans-api-hub-mcp** | 334 free developer tools: QR codes, passwords, UUIDs, hashes, Base64, JSON, color converter, email verification, IP geolocation, timestamps, plus 300+ calculators, text analysis, color tools, readability, domain, code and financial tools. MCP server at `uvx gadgethumans-api-hub-mcp`. Free, no API key required. | [GitHub](https://github.com/scotia1973-bot/gadgethumans-api-hub-mcp) |
| 22 | **mcp-server** | MCP Server for Burp | [GitHub](https://github.com/PortSwigger/mcp-server) |
| 23 | **crosspaste-desktop** | Cross-device clipboard sync for macOS, Windows & Linux — end-to-end encrypted, LAN-only, no cloud. OCR, CLI and MCP server built in. | TBD | [GitHub](https://github.com/CrossPaste/crosspaste-desktop) |

### Communication

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | mcp-discord | Discord messaging and community management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-discord.md) |
| 2 | line | Messaging application and platform integration | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/line.md) |
| 3 | tweetbinder | Twitter/X analytics and social media insights | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tweetbinder.md) |
| 4 | **supabase-mcp-server** | Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more. | [GitHub](https://github.com/alexander-zuev/supabase-mcp-server) |
| 5 | **mcp-server-chatsum** | Query and Summarize your chat messages. | [GitHub](https://github.com/chatmcp/mcp-server-chatsum) |
| 6 | **BulkPublish** | Create, adapt, schedule, publish, and analyze social media content across connected channels through a hosted Streamable HTTP MCP server or local npm package. | [Docs](https://app.bulkpublish.com/docs) |

### Knowledge Management

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | obsidian | Work with Obsidian notes and knowledge management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/obsidian.md) |
| 2 | fibery | Connected work platform for knowledge management | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fibery.md) |
| 3 | context7 | Provide contextual information for enhanced AI conversations | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/context7.md) |
| 4 | atlas-docs | Access MongoDB Atlas documentation and best practices | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlas-docs.md) |
| 5 | **knowledge-rag** | Local RAG system via MCP — hybrid search (semantic + BM25 + RRF), cross-encoder reranking, markdown-aware chunking, 12 MCP tools. Zero external servers | [GitHub](https://github.com/lyonzin/knowledge-rag) |
| 6 | **screenpipe** | 24/7 local screen and mic recording; MCP server indexes OCR, accessibility, and audio transcripts so agents can search what you've seen, said, or heard. Works with Ollama. | [GitHub](https://github.com/screenpipe/screenpipe) |
| 7 | **Hexis** | Git-backed platform for skills, tools, and context for AI agents, with review workflows, role-based access, encrypted secrets, and remote MCP access. | [GitHub](https://github.com/Bevel-Software/Hexis) |

### Multimedia & Design

| # | MCP Server | Description | Link |
|---|------------|-------------|------|
| 1 | gyazo | Screenshot capturing and sharing service | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gyazo.md) |
| 2 | handwriting-ocr | Optical character recognition for handwritten text | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/handwriting-ocr.md) |
| 3 | webflow | Visual website design and content management system | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/webflow.md) |
| 4 | youtube_transcript | YouTube video transcript extraction | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/youtube_transcript.md) |
| 5 | speech-ai | Speech AI with pronunciation assessment, text-to-speech, and speech-to-text | [GitHub](https://github.com/fasuizu-br/speech-ai-examples) |
| 6 | **Prompt to Asset** | MCP server that generates production-ready visual assets (app icons, favicons, OG images) across 30+ image generation models | [GitHub](https://github.com/MohamedAbdallah-14/prompt-to-asset) |
| 7 | **OrkasVideoStudio** | Local-first MCP toolkit for agent-driven video composition, editing, generation, and automatic assembly | [GitHub](https://github.com/Orkas-AI/Orkas-VideoStudio) |
| 8 | **AI Applyd** | ATS resume scoring, job-description analysis, interview prep, cover letters, resume building and auto-apply that submits on the employer's own hiring system | [GitHub](https://github.com/whateverneveranywhere/aiapplyd-mcp) |
| 9 | **YouTube Transcript MCP** | MCP server for YouTube transcripts, video and channel search, channel browsing, and playlist extraction, returned as clean JSON or markdown for Claude, ChatGPT and other MCP clients | [GitHub](https://github.com/ZeroPointRepo/youtube-mcp) |
| 10 | **Magic Hour** | Hosted MCP server for generating and editing video, images, and audio through 44 Magic Hour API tools | [GitHub](https://github.com/magichourhq/magic-hour-mcp) |



### Installation Steps

1. Open Docker Desktop
2. Go to Extensions Marketplace
3. Search for "Docker MCP Toolkit"
4. Click Install
5. Once installed, open the extension from the left sidebar
6. Browse the catalog and start using MCP tools with your AI assistant

For a complete list of Docker MCP Servers (109+ implementations), visit the [Docker MCP Toolkit GitHub repository](https://github.com/docker/labs-ai-tools-for-devs/tree/main/prompts/mcp).

## Contributing

We welcome contributions to this awesome list! Please read our [contribution guidelines](CONTRIBUTING.md) before submitting your suggestions.

## License

[![CC0](https://mirrors.creativecommons.org/presskit/buttons/88x31/svg/cc-zero.svg)](https://creativecommons.org/publicdomain/zero/1.0/)

To the extent possible under law, the contributors have waived all copyright and related or neighboring rights to this work.
