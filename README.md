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

### DevOps & Infrastructure

MCP servers for managing infrastructure, containers, and DevOps workflows.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | github | Manage GitHub repositories and perform Git operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 2 | docker | Integrate with Docker to manage containers, images, and networks | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 3 | kubernetes | Orchestrate and manage containerized applications with Kubernetes | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 4 | gitlab | Interact with GitLab repositories and CI/CD pipelines | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gitlab.md) |
| 5 | circleci | Manage CI/CD pipelines and workflows in CircleCI | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/circleci.md) |
| 6 | **AWS Comprehensive** | Complete AWS service integration suite (20+ services) | TBD | [AWS Labs](https://github.com/awslabs/mcp) |
| 7 | **Terraform** | Infrastructure as Code management | **22.3K+** | [Docker Hub](https://hub.docker.com/r/hashicorp/terraform-mcp-server) |
| 8 | pulumi | Infrastructure as code platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/pulumi.md) |
| 9 | heroku | Cloud platform as a service (PaaS) | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/heroku.md) |
| 10 | jetbrains | Integrate with JetBrains IDEs and tools | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/jetbrains.md) |
| 11 | **TrendRadar** | ⭐AI-driven public opinion & trend monitor with multi-platform aggregation, RSS, and smart alerts.🎯 告别信息过载，你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 +  RSS 订阅，支持关键词精准筛选。AI 智能筛选新闻 + AI 翻译 +  AI 分析简报直推手机，也支持接入 MCP 架构，赋能 AI 自然语言对话分析、情感洞察与趋势预测等。支持 Docker ，数据本地/云端自持。集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送。 | TBD | [GitHub](https://github.com/sansan0/TrendRadar) |
| 12 | **github-mcp-server** | GitHub's official MCP Server | TBD | [GitHub](https://github.com/github/github-mcp-server) |
| 13 | **nginx-ui** | Yet another WebUI for Nginx | TBD | [GitHub](https://github.com/0xJacky/nginx-ui) |
| 14 | **hexstrike-ai** | HexStrike AI MCP Agents is an advanced MCP server that lets AI agents (Claude, GPT, Copilot, etc.) autonomously run 150+ cybersecurity tools for automated pentesting, vulnerability discovery, bug bounty automation, and security research. Seamlessly bridge LLMs with real-world offensive security capabilities. | TBD | [GitHub](https://github.com/0x4m4/hexstrike-ai) |
| 15 | **firecrawl-mcp-server** | 🔥 Official Firecrawl MCP Server - Adds powerful web scraping and search to Cursor, Claude and any other LLM clients. | TBD | [GitHub](https://github.com/firecrawl/firecrawl-mcp-server) |
| 16 | **kubefwd** | Bulk port forwarding Kubernetes services for local development. | TBD | [GitHub](https://github.com/txn2/kubefwd) |
| 17 | **archestra** | Enterprise AI Platform with guardrails, MCP registry, gateway & orchestrator | TBD | [GitHub](https://github.com/archestra-ai/archestra) |
| 18 | **py-xiaozhi** | A Python-based Xiaozhi AI for users who want the full Xiaozhi experience without owning specialized hardware. | TBD | [GitHub](https://github.com/huangjunsen0406/py-xiaozhi) |
| 19 | **bifrost** | Fastest enterprise AI gateway (50x faster than LiteLLM) with adaptive load balancer, cluster mode, guardrails, 1000+ models support & <100 µs overhead at 5k RPS. | TBD | [GitHub](https://github.com/maximhq/bifrost) |
| 20 | **mcp-context-forge** | An AI Gateway, registry, and proxy that sits in front of any MCP, A2A, or REST/gRPC APIs, exposing a unified endpoint with centralized discovery, guardrails and management. Optimizes Agent & Tool calling, and supports plugins. | TBD | [GitHub](https://github.com/IBM/mcp-context-forge) |
| 21 | **metamcp** | MCP Aggregator, Orchestrator, Middleware, Gateway in one docker | TBD | [GitHub](https://github.com/metatool-ai/metamcp) |
| 22 | **toolhive** | ToolHive is an enterprise-grade platform for running and managing Model Context Protocol (MCP) servers. | TBD | [GitHub](https://github.com/stacklok/toolhive) |
| 23 | **Unity-MCP** | AI Skills, MCP Tools, and CLI for Unity Engine. Full AI develop and test loop. Use cli for quick setup. Efficient token usage, advanced tools. Any C# method may be turned into a tool by a single line. Works with Claude Code, Gemini, Copilot, Cursor and any other absolutely for free. | TBD | [GitHub](https://github.com/IvanMurzak/Unity-MCP) |
| 24 | **minima** | On-premises conversational RAG with configurable containers | TBD | [GitHub](https://github.com/dmayboroda/minima) |
| 25 | **MCPJungle** | Self-hosted MCP Gateway for AI agents | TBD | [GitHub](https://github.com/mcpjungle/MCPJungle) |
| 26 | **scira-mcp-chat** | A minimalistic MCP client with a good feature set. | TBD | [GitHub](https://github.com/zaidmukaddam/scira-mcp-chat) |
| 27 | **context-space** | Ultimate Context Engineering Infrastructure, starting from MCPs and Integrations | TBD | [GitHub](https://github.com/context-space/context-space) |
| 28 | **vllora** | Debug your AI agents | TBD | [GitHub](https://github.com/vllora/vllora) |
| 29 | **drift** | Codebase intelligence for AI. Detects patterns & conventions + remembers decisions across sessions. MCP server for any IDE. Offline CLI. | TBD | [GitHub](https://github.com/dadbodgeoff/drift) |
| 30 | **notion-mcp-server** | Official Notion MCP Server | TBD | [GitHub](https://github.com/makenotion/notion-mcp-server) |
| 31 | **mcp-server** | An MCP server for interacting with the Financial Datasets stock market API. | TBD | [GitHub](https://github.com/financial-datasets/mcp-server) |
| 32 | **mcp-server-kubernetes** | MCP Server for kubernetes management commands | TBD | [GitHub](https://github.com/Flux159/mcp-server-kubernetes) |
| 33 | **kubernetes-mcp-server** | Model Context Protocol (MCP) server for Kubernetes and OpenShift | TBD | [GitHub](https://github.com/containers/kubernetes-mcp-server) |
| 34 | **mcp-server-qdrant** | An official Qdrant Model Context Protocol (MCP) server implementation | TBD | [GitHub](https://github.com/qdrant/mcp-server-qdrant) |
| 35 | **terraform-mcp-server** | The Terraform MCP Server provides seamless integration with Terraform ecosystem, enabling advanced automation and interaction capabilities for Infrastructure as Code (IaC) development. | TBD | [GitHub](https://github.com/hashicorp/terraform-mcp-server) |
| 36 | **awesome-devops-mcp-servers** | A curated list of awesome MCP servers focused on DevOps tools and capabilities. | TBD | [GitHub](https://github.com/rohitg00/awesome-devops-mcp-servers) |
| 37 | **apify-mcp-server** | The Apify MCP server enables your AI agents to extract data from social media, search engines, maps, e-commerce sites, or any other website using thousands of ready-made scrapers, crawlers, and automation tools available on the Apify Store. | TBD | [GitHub](https://github.com/apify/apify-mcp-server) |
| 38 | **kubectl-mcp-server** | A Model Context Protocol (MCP) server for Kubernetes. Install: npx kubectl-mcp-server or pip install kubectl-mcp-server | TBD | [GitHub](https://github.com/rohitg00/kubectl-mcp-server) |

### Database & Storage

MCP servers for accessing and managing databases and storage solutions.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | postgres | Interact with PostgreSQL databases | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgres.md) |
| 2 | **MongoDB** | MongoDB database integration | **4.2K+** | [Docker Hub](https://hub.docker.com/r/mongodb/mongodb-mcp-server) |
| 3 | redis | Interact with Redis in-memory data structure store | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis.md) |
| 4 | elasticsearch | Search, analyze, and visualize data with Elasticsearch | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elasticsearch.md) |
| 5 | chroma | Interact with Chroma vector database for embeddings and retrieval | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/chroma.md) |
| 6 | neo4j-server | Graph database server management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-server.md) |
| 7 | astra-db | Interact with DataStax Astra DB, a cloud-native Cassandra database | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/astra-db.md) |
| 8 | neon | Serverless PostgreSQL database service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neon.md) |
| 9 | **Supabase** | Open source Firebase alternative | TBD | [GitHub](https://github.com/supabase/mcp-server-supabase) |
| 10 | tembo | Enhanced PostgreSQL database platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tembo.md) |
| 11 | **mcp-database-connector-lite** | Free, open-source SQLite MCP server with query execution, schema inspection, and data manipulation | TBD | [GitHub](https://github.com/tiranmoskovitch-dev/mcp-database-connector-lite) |
| 12 | **XHS-Downloader** | 小红书（XiaoHongShu、RedNote）链接提取/作品采集工具：提取账号发布、收藏、点赞、专辑作品链接；提取搜索结果作品、用户链接；采集小红书作品信息；提取小红书作品下载地址；下载小红书作品文件 | TBD | [GitHub](https://github.com/JoeanAmier/XHS-Downloader) |
| 13 | **lamda** |  The most powerful Android RPA agent framework, next generation of mobile automation robots. | TBD | [GitHub](https://github.com/firerpa/lamda) |
| 14 | **httprunner** | HttpRunner 是一款开源的 API/UI 测试框架，简单易用，功能强大，具有丰富的插件化机制和高度的可扩展能力。 | TBD | [GitHub](https://github.com/httprunner/httprunner) |
| 15 | **mcp-memory-service** | Open-source persistent memory for AI agent pipelines (LangGraph, CrewAI, AutoGen) and Claude. REST API + knowledge graph + autonomous consolidation. | TBD | [GitHub](https://github.com/doobidoo/mcp-memory-service) |
| 16 | **mysql_mcp_server** | A Model Context Protocol (MCP) server that enables secure interaction with MySQL databases | TBD | [GitHub](https://github.com/designcomputer/mysql_mcp_server) |
| 17 | **codebase-memory-mcp** | High-performance code intelligence MCP server. Indexes codebases into a persistent knowledge graph — average repo in milliseconds. 64 languages, sub-ms queries, 99% fewer tokens. Single static binary, zero dependencies. | TBD | [GitHub](https://github.com/DeusData/codebase-memory-mcp) |
| 18 | **awesome-openclaw** | A curated list of OpenClaw resources, tools, skills, tutorials & articles. OpenClaw (formerly Moltbot / Clawdbot) — open-source self-hosted AI agent for WhatsApp, Telegram, Discord & 50+ integrations. | TBD | [GitHub](https://github.com/SamurAIGPT/awesome-openclaw) |
| 19 | **mcp-server-mysql** | A Model Context Protocol server that provides read-only access to MySQL databases. This server enables LLMs to inspect database schemas and execute read-only queries. | TBD | [GitHub](https://github.com/benborla/mcp-server-mysql) |
| 20 | **mongodb-mcp-server** | A Model Context Protocol server to connect to MongoDB databases and MongoDB Atlas Clusters. | TBD | [GitHub](https://github.com/mongodb-js/mongodb-mcp-server) |
| 21 | **android-mcp-server** | An MCP server that provides control over Android devices via adb | TBD | [GitHub](https://github.com/minhalvp/android-mcp-server) |

### Web & Content

MCP servers for web search, content access, and web automation.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | brave | Perform web searches using Brave's privacy-focused search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/brave.md) |
| 2 | notion | Create and manage content in Notion workspaces | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/notion.md) |
| 3 | puppeteer | Automate browser interactions and scrape web content | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/puppeteer.md) |
| 4 | duckduckgo | Privacy-focused web search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/duckduckgo.md) |
| 5 | firecrawl | Web crawling and content extraction tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/firecrawl.md) |
| 6 | **Scrapling** | 🕷️ An adaptive Web Scraping framework that handles everything from a single request to a full-scale crawl! | TBD | [GitHub](https://github.com/D4Vinci/Scrapling) |
| 7 | **chrome-devtools-mcp** | Chrome DevTools for coding agents | TBD | [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp) |
| 8 | **UI-TARS-desktop** | The Open-Source Multimodal AI Agent Stack: Connecting Cutting-Edge AI Models and Agent Infra | TBD | [GitHub](https://github.com/bytedance/UI-TARS-desktop) |
| 9 | **gpt-researcher** | An autonomous agent that conducts deep research on any data using any LLM providers | TBD | [GitHub](https://github.com/assafelovic/gpt-researcher) |
| 10 | **Skill_Seekers** | Convert documentation websites, GitHub repositories, and PDFs into Claude AI skills with automatic conflict detection | TBD | [GitHub](https://github.com/yusufkaraaslan/Skill_Seekers) |
| 11 | **browser-tools-mcp** | Monitor browser logs directly from Cursor and other MCP compatible IDEs. | TBD | [GitHub](https://github.com/AgentDeskAI/browser-tools-mcp) |
| 12 | **mcp** | Browser MCP is a Model Context Provider (MCP) server that allows AI applications to control your browser | TBD | [GitHub](https://github.com/BrowserMCP/mcp) |
| 13 | **deep-research** | Use any LLMs (Large Language Models) for Deep Research. Support SSE API and MCP server. | TBD | [GitHub](https://github.com/u14app/deep-research) |
| 14 | **mcpo** | A simple, secure MCP-to-OpenAPI proxy server | TBD | [GitHub](https://github.com/open-webui/mcpo) |
| 15 | **exa-mcp-server** | Exa MCP for web search and web crawling! | TBD | [GitHub](https://github.com/exa-labs/exa-mcp-server) |
| 16 | **Auto-claude-code-research-in-sleep** | ARIS ⚔️ (Auto-Research-In-Sleep) — Lightweight Markdown-only skills for autonomous ML research: cross-model review loops, idea discovery, and experiment automation. No framework, no lock-in — works with Claude Code, Codex, OpenClaw, or any LLM agent. | TBD | [GitHub](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) |
| 17 | **google_workspace_mcp** | Control Gmail, Google Calendar, Docs, Sheets, Slides, Chat, Forms, Tasks, Search & Drive with AI - Comprehensive Google Workspace / G Suite MCP Server & CLI Tool | TBD | [GitHub](https://github.com/taylorwilsdon/google_workspace_mcp) |
| 18 | **grafbase** | The Grafbase GraphQL Federation Gateway | TBD | [GitHub](https://github.com/grafbase/grafbase) |
| 19 | **apple-docs-mcp** | MCP server for Apple Developer Documentation - Search iOS/macOS/SwiftUI/UIKit docs, WWDC videos, Swift/Objective-C APIs & code examples in Claude, Cursor & AI assistants | TBD | [GitHub](https://github.com/kimsungwhee/apple-docs-mcp) |
| 20 | **octocode-mcp** | MCP server for semantic code research and context generation on real-time using LLM patterns &#124; Search naturally across public & private repos based on your permissions &#124; Transform any accessible codebase/s into AI-optimized knowledge on simple and complex flows &#124; Find real implementations and live docs from anywhere | TBD | [GitHub](https://github.com/bgauryy/octocode-mcp) |
| 21 | **mcp-server-browserbase** | Allow LLMs to control a browser with Browserbase and Stagehand | TBD | [GitHub](https://github.com/browserbase/mcp-server-browserbase) |
| 22 | **shadcn-ui-mcp-server** | A mcp server to allow LLMS gain context about shadcn ui component structure,usage and installation,compaitable with react,svelte 5,vue & React Native | TBD | [GitHub](https://github.com/Jpisnice/shadcn-ui-mcp-server) |
| 23 | **arxiv-mcp-server** | A Model Context Protocol server for searching and analyzing arXiv papers | TBD | [GitHub](https://github.com/blazickjp/arxiv-mcp-server) |
| 24 | **linkedin-mcp-server** | This MCP server allows Claude and other AI assistants to access your LinkedIn. Scrape LinkedIn profiles, companies and jobs, and perform job searches. | TBD | [GitHub](https://github.com/stickerdaniel/linkedin-mcp-server) |
| 25 | **duckduckgo-mcp-server** | A Model Context Protocol (MCP) server that provides web search capabilities through DuckDuckGo, with additional features for content fetching and parsing. | TBD | [GitHub](https://github.com/nickclyde/duckduckgo-mcp-server) |
| 26 | **browser-use-mcp-server** | Browse the web, directly from Cursor etc. | TBD | [GitHub](https://github.com/kontext-dev/browser-use-mcp-server) |

### Integrations & APIs

MCP servers for accessing external services and APIs.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | stripe | Process payments and manage financial transactions | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/stripe.md) |
| 2 | shopify | Manage Shopify e-commerce stores and products | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/shopify.md) |
| 3 | **shopsavvy** | Complete product and pricing data solution - search products, compare prices, track history | TBD | [GitHub](https://github.com/shopsavvy/shopsavvy-mcp-server) |
| 4 | atlassian | Integrate with Atlassian products like Jira and Confluence | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlassian.md) |
| 5 | azure | Interact with Microsoft Azure cloud services and resources | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/azure.md) |
| 6 | google-maps | Geographic information and location services | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/google-maps.md) |
| 7 | slack | Send and receive messages in Slack workspaces | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/slack.md) |
| 8 | gdrive | Access and manage files in Google Drive | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gdrive.md) |
| 9 | box | Manage files and folders in Box cloud storage | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/box.md) |
| 10 | razorpay | Payment gateway and financial services platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/razorpay.md) |
| 11 | resend | Email delivery and management service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/resend.md) |
| 12 | **x402engine-mcp** | 51 pay-per-call APIs for AI agents — LLMs, image/video generation, code execution, TTS, transcription, crypto data, wallet analytics, web scraping, and IPFS via HTTP 402 micropayments | TBD | [GitHub](https://github.com/agentc22/x402engine-mcp) |
| 13 | **mcp-api-bridge-lite** | Free REST API to MCP bridge — connect any REST API to AI assistants with simple YAML configuration, supporting GET, POST, PUT, DELETE with authentication | TBD | [GitHub](https://github.com/tiranmoskovitch-dev/mcp-api-bridge-lite) |
| 14 | **lightning-wallet-mcp** | Give AI agents a Bitcoin wallet with Lightning Network payments and L402 support | TBD | [GitHub](https://github.com/lightningfaucet/lightning-wallet-mcp) |
| 15 | **WritBase** | MCP-native task management for AI agent fleets | TBD | [GitHub](https://github.com/Writbase/writbase) |
| 16 | **short-video-maker** | Creates short videos for TikTok, Instagram Reels, and YouTube Shorts using the Model Context Protocol (MCP) and a REST API. | TBD | [GitHub](https://github.com/gyoridavid/short-video-maker) |
| 17 | **n8n-mcp-server** | MCP server that provides tools and resources for interacting with n8n API | TBD | [GitHub](https://github.com/leonardsellem/n8n-mcp-server) |

### AI & Machine Learning

MCP servers for AI and machine learning capabilities.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | tavily | AI-powered web search and research assistant | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tavily.md) |
| 2 | perplexity-ask | AI-powered question answering system | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/perplexity-ask.md) |
| 3 | elevenlabs | AI voice generation and text-to-speech | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elevenlabs.md) |
| 4 | wolfram-alpha | Computational knowledge engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wolfram-alpha.md) |
| 5 | everart | AI art generation and manipulation | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/everart.md) |
| 6 | **OpenAI Compatible** | Any OpenAI SDK compatible API | TBD | [GitHub](https://github.com/imbactbulletz/any-chat-completions-mcp) |
| 7 | **Amazon Bedrock** | AWS AI services integration | TBD | [AWS Labs](https://github.com/awslabs/mcp) |
| 8 | **Amazon Nova Canvas** | AI image generation platform | TBD | [AWS Labs](https://github.com/awslabs/mcp) |
| 9 | **Roundtable** | Multi-model AI debate platform — GPT-4o, Claude, Gemini & 200+ models discuss, then synthesize insight | TBD | [GitHub](https://github.com/deadpixel/roundtable-dashboard) |
| 10 | **n8n** | Fair-code workflow automation platform with native AI capabilities. Combine visual building with custom code, self-host or cloud, 400+ integrations. | TBD | [GitHub](https://github.com/n8n-io/n8n) |
| 11 | **gemini-cli** | An open-source AI agent that brings the power of Gemini directly into your terminal. | TBD | [GitHub](https://github.com/google-gemini/gemini-cli) |
| 12 | **context7** | Context7 Platform -- Up-to-date code documentation for LLMs and AI code editors | TBD | [GitHub](https://github.com/upstash/context7) |
| 13 | **ruflo** | 🌊 The leading agent orchestration platform for Claude. Deploy intelligent multi-agent swarms, coordinate autonomous workflows, and build conversational AI systems. Features    enterprise-grade architecture, distributed swarm intelligence, RAG integration, and native Claude Code / Codex Integration | TBD | [GitHub](https://github.com/ruvnet/ruflo) |
| 14 | **serena** | A powerful coding agent toolkit providing semantic retrieval and editing capabilities (MCP server & other integrations) | TBD | [GitHub](https://github.com/oraios/serena) |
| 15 | **activepieces** | AI Agents & MCPs & AI Workflow Automation • (~400 MCP servers for AI agents) • AI Automation / AI Agent with MCPs • AI Workflows & AI Agents • MCPs for AI Agents | TBD | [GitHub](https://github.com/activepieces/activepieces) |
| 16 | **MaxKB** | 🔥 MaxKB is an open-source platform for building enterprise-grade agents.  强大易用的开源企业级智能体平台。 | TBD | [GitHub](https://github.com/1Panel-dev/MaxKB) |
| 17 | **trigger.dev** | Trigger.dev – build and deploy fully‑managed AI agents and workflows | TBD | [GitHub](https://github.com/triggerdotdev/trigger.dev) |
| 18 | **mcp-use** | The fullstack MCP framework to develop MCP Apps for ChatGPT / Claude & MCP Servers for AI Agents. | TBD | [GitHub](https://github.com/mcp-use/mcp-use) |
| 19 | **OpenMetadata** | OpenMetadata is a unified metadata platform for data discovery, data observability, and data governance powered by a central metadata repository, in-depth column level lineage, and seamless team collaboration. | TBD | [GitHub](https://github.com/open-metadata/OpenMetadata) |
| 20 | **xiaozhi-esp32-server** | 本项目为xiaozhi-esp32提供后端服务，帮助您快速搭建ESP32设备控制服务器。Backend service for xiaozhi-esp32, helps you quickly build an ESP32 device control server. | TBD | [GitHub](https://github.com/xinnan-tech/xiaozhi-esp32-server) |
| 21 | **ida-pro-mcp** | AI-powered reverse engineering assistant that bridges IDA Pro with language models through MCP. | TBD | [GitHub](https://github.com/mrexodia/ida-pro-mcp) |
| 22 | **Viper** | Adversary simulation and Red teaming platform with AI | TBD | [GitHub](https://github.com/FunnyWolf/Viper) |
| 23 | **mcp-server-chart** | 🤖 A visualization mcp & skills contains 25+ visual charts using @antvis. Using for chart generation and data analysis. | TBD | [GitHub](https://github.com/antvis/mcp-server-chart) |
| 24 | **excel-mcp-server** | A Model Context Protocol server for Excel file manipulation | TBD | [GitHub](https://github.com/haris-musa/excel-mcp-server) |
| 25 | **MCP-Chinese-Getting-Started-Guide** | Model Context Protocol(MCP) 编程极速入门 | TBD | [GitHub](https://github.com/liaokongVFX/MCP-Chinese-Getting-Started-Guide) |
| 26 | **fastmcp** | 🚀 The fast, Pythonic way to build MCP servers and clients. | TBD | [GitHub](https://github.com/PrefectHQ/fastmcp) |
| 27 | **Upsonic** | Agent Framework For Fintech and Banks | TBD | [GitHub](https://github.com/Upsonic/Upsonic) |
| 28 | **unity-mcp** | Unity MCP acts as a bridge, allowing AI assistants (like Claude, Cursor) to interact directly with your Unity Editor via a local MCP (Model Context Protocol) Client. Give your LLM tools to manage assets, control scenes, edit scripts, and automate tasks within Unity. | TBD | [GitHub](https://github.com/CoplayDev/unity-mcp) |
| 29 | **cursor-talk-to-figma-mcp** | TalkToFigma: MCP integration between AI Agent (Cursor, Claude Code) and Figma, allowing Agentic AI to communicate with Figma for reading designs and modifying them programmatically. | TBD | [GitHub](https://github.com/grab/cursor-talk-to-figma-mcp) |
| 30 | **awesome-mcp-servers** | Awesome MCP Servers - A curated list of Model Context Protocol servers | TBD | [GitHub](https://github.com/appcypher/awesome-mcp-servers) |
| 31 | **5ire** | 5ire is a cross-platform desktop AI assistant, MCP client. It compatible with major service providers,  supports local knowledge base and  tools via model context protocol servers . | TBD | [GitHub](https://github.com/nanbingxyz/5ire) |
| 32 | **casibase** | ⚡️AI Cloud OS: Open-source enterprise-level AI knowledge base and MCP (model-context-protocol)/A2A (agent-to-agent) management platform with admin UI, user management and Single-Sign-On⚡️, supports ChatGPT, Claude, Llama, Ollama, HuggingFace, etc., chat bot demo: https://ai.casibase.com, admin UI demo: https://ai-admin.casibase.com | TBD | [GitHub](https://github.com/casibase/casibase) |
| 33 | **markdownify-mcp** | A Model Context Protocol server for converting almost anything to Markdown | TBD | [GitHub](https://github.com/zcaceres/markdownify-mcp) |
| 34 | **generative-ai** | Comprehensive resources on Generative AI, including a detailed roadmap, projects, use cases, interview preparation, and coding preparation. | TBD | [GitHub](https://github.com/genieincodebottle/generative-ai) |
| 35 | **gemini-mcp-tool** | MCP server that enables AI assistants to interact with Google Gemini CLI, leveraging Gemini's massive token window for large file analysis and codebase understanding | TBD | [GitHub](https://github.com/jamubc/gemini-mcp-tool) |
| 36 | **mcphub.nvim** | An MCP client for Neovim that seamlessly integrates MCP servers into your editing workflow with an intuitive interface for managing, testing, and using MCP servers with your favorite chat plugins. | TBD | [GitHub](https://github.com/ravitemer/mcphub.nvim) |
| 37 | **pilot-shell** | The professional development environment for Claude Code: From requirement to production-grade code. Planned, tested, verified. | TBD | [GitHub](https://github.com/maxritter/pilot-shell) |
| 38 | **jadx-ai-mcp** | Plugin for JADX to integrate MCP server | TBD | [GitHub](https://github.com/zinja-coder/jadx-ai-mcp) |
| 39 | **mcp-language-server** | mcp-language-server gives MCP enabled clients access semantic tools like get definition, references, rename, and diagnostics. | TBD | [GitHub](https://github.com/isaacphi/mcp-language-server) |
| 40 | **mcp-unity** | Model Context Protocol (MCP) plugin to connect with Unity Editor — designed for Cursor, Claude Code, Codex, Windsurf and other IDEs | TBD | [GitHub](https://github.com/CoderGamester/mcp-unity) |
| 41 | **code-mode** | 🔌 Plug-and-play library to enable agents to call MCP and UTCP tools via code execution.  | TBD | [GitHub](https://github.com/universal-tool-calling-protocol/code-mode) |
| 42 | **nerve** | The Simple Agent Development Kit. | TBD | [GitHub](https://github.com/evilsocket/nerve) |
| 43 | **tuui** | A desktop MCP client designed as a tool unitary utility integration, accelerating AI adoption through the Model Context Protocol (MCP) and enabling cross-vendor LLM API orchestration. | TBD | [GitHub](https://github.com/AI-QL/tuui) |
| 44 | **MCP-Bridge** | A middleware to provide an openAI compatible endpoint that can call MCP tools | TBD | [GitHub](https://github.com/SecretiveShell/MCP-Bridge) |
| 45 | **MassGen** | 🚀 MassGen is an open-source multi-agent scaling system that runs in your terminal, autonomously orchestrating frontier models and agents to collaborate, reason, and produce high-quality results. &#124; Join us on Discord: discord.massgen.ai | TBD | [GitHub](https://github.com/massgen/MassGen) |
| 46 | **arcade-mcp** | The best way to create, deploy, and share MCP Servers | TBD | [GitHub](https://github.com/ArcadeAI/arcade-mcp) |
| 47 | **mcp-client-cli** | A simple CLI to run LLM prompt and implement MCP client. | TBD | [GitHub](https://github.com/adhikasp/mcp-client-cli) |
| 48 | **awesome-mcp-servers** | A collection of MCP servers. | TBD | [GitHub](https://github.com/punkpeye/awesome-mcp-servers) |
| 49 | **pal-mcp-server** | The power of Claude Code / GeminiCLI / CodexCLI + [Gemini / OpenAI / OpenRouter / Azure / Grok / Ollama / Custom Model / All Of The Above] working as one. | TBD | [GitHub](https://github.com/BeehiveInnovations/pal-mcp-server) |
| 50 | **Office-Word-MCP-Server** | A Model Context Protocol (MCP) server for creating, reading, and manipulating Microsoft Word documents. This server enables AI assistants to work with Word documents through a standardized interface, providing rich document editing capabilities. | TBD | [GitHub](https://github.com/GongRzhe/Office-Word-MCP-Server) |
| 51 | **slack-mcp-server** | The most powerful MCP Slack Server with no permission requirements, Apps support, GovSlack, DMs, Group DMs and smart history fetch logic. | TBD | [GitHub](https://github.com/korotovsky/slack-mcp-server) |
| 52 | **docs-mcp-server** | Grounded Docs MCP Server: Open-Source Alternative to Context7, Nia, and Ref.Tools | TBD | [GitHub](https://github.com/arabold/docs-mcp-server) |
| 53 | **ros-mcp-server** | Connect AI models like Claude & GPT with robots using MCP and ROS. | TBD | [GitHub](https://github.com/robotmcp/ros-mcp-server) |
| 54 | **Awesome-MCP-Servers** | A curated list of Model Context Protocol (MCP) servers  | TBD | [GitHub](https://github.com/YuzeHao2023/Awesome-MCP-Servers) |
| 55 | **jupyter-mcp-server** | 🪐 🔧 Model Context Protocol (MCP) Server for Jupyter. | TBD | [GitHub](https://github.com/datalayer/jupyter-mcp-server) |
| 56 | **openapi-mcp-server** | Allow AI to wade through complex OpenAPIs using Simple Language | TBD | [GitHub](https://github.com/janwilmake/openapi-mcp-server) |
| 57 | **douyin-mcp-server** | 提取抖音无水印视频链接，视频文案，douyin-mcp-server，mcp，claude skill，支持龙虾 | TBD | [GitHub](https://github.com/yzfly/douyin-mcp-server) |

## MCP Clients

### Desktop Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | **Claude Desktop** | Official Claude client with native MCP support | Windows, macOS |
| 2 | **Cursor AI** | AI-powered code editor with MCP support | Windows, macOS, Linux |
| 3 | **Windsurf** | AI browser with MCP integration | macOS |
| 4 | **Cline** | Terminal-based chat client with MCP support | Windows, macOS, Linux |
| 5 | **MetaMCP** | Unified middleware MCP client | Windows, macOS, Linux |
| 6 | **Continue.dev** | AI coding assistant for IDEs | VS Code, JetBrains |


### Mobile Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | Claude Mobile | Mobile Claude client with MCP support | iOS, Android |
| 2 | AI Assistant | Multi-model mobile client with MCP | iOS |

### IDE Extensions

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | VS Code AI Assistant | VS Code extension with MCP support | VS Code |
| 2 | JetBrains AI Assistant | JetBrains IDE extension with MCP | JetBrains IDEs |
| 3 | GitHub Copilot Chat | GitHub's AI assistant with MCP capabilities | VS Code, Visual Studio, JetBrains |

### Command Line Tools

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | Claude CLI | Command-line interface for Claude with MCP | Windows, macOS, Linux |
| 2 | MCP CLI | General MCP client for command line | Windows, macOS, Linux |
| 3 | mark3labs/mcphost | CLI host for MCP interactions | Windows, macOS, Linux |

### Web Applications

| # | Client Name | Description | Platforms |
|---|-------------|-------------|-----------|
| 1 | Claude Web | Web interface for Claude with MCP support | Web |
| 2 | Glama AI | Web-based multi-model client with MCP | Web |
| 3 | Phind | Developer-focused search with MCP | Web |

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
| 1 | lastmile-ai/mcp-agent | TypeScript | Build agents with MCP servers |
| 2 | mcpdotdirect/template-mcp-server | TypeScript | CLI tool for new MCP servers |
| 3 | stephencme/create-mcp-ts | TypeScript | MCP server creator with templates |
| 4 | Upsonic/gpt-computer-assistant | Python | Framework for AI agents |
| 5 | p-funk/FEGIS | Python | Interactive agent framework |


## Agent Development Frameworks

| # | Framework Name | Language | Description | Link |
|---|----------------|----------|-------------|------|
| 1 | mcp-agent | TypeScript | Build effective agents with MCP servers using simple, composable patterns | [GitHub](https://github.com/lastmile-ai/mcp-agent) |
| 2 | gpt-computer-assistant | Python | Framework to build vertical AI agent with MCP integration | [GitHub](https://github.com/Upsonic/gpt-computer-assistant) |
| 3 | FEGIS | Python | A semantic programming framework for LLMs with MCP support | [GitHub](https://github.com/p-funk/FEGIS) |
| 4 | langchain-mcp | Python | LangChain integration for MCP | [GitHub](https://github.com/langchain-ai/langchain-mcp) |
| 5 | solana-agent-kit | TypeScript | Solana MCP SDK for blockchain agent development | [GitHub](https://github.com/sendaifun/solana-agent-kit) |

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
| 1 | modelcontextprotocol/inspector | TypeScript | Official UI for testing MCP servers |
| 2 | wong2/mcp-cli | Multiple | Command line inspector for testing |
| 3 | mclenhard/mcp-evals | Multiple | Package for running evaluations |
| 4 | Typewise/mcp-chaos-rig | TypeScript | Fault injection server for testing MCP clients against auth failures, disappearing tools, flaky responses, and token expiry |

### Utilities

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | hamidra/yamcp | TypeScript | MCP workspace manager |
| 2 | punkpeye/mcp-proxy | TypeScript | SSE proxy for MCP servers |
| 3 | multi-mcp | Python | Multi-MCP Proxy Server |
| 4 | f/MCPTools | Go | CLI tool for MCP server interactions |
| 5 | portel-dev/ncp | TypeScript | MCP orchestrator with intelligent discovery, 98.2% accuracy, and 94.8% token savings. Transforms 100+ tools into 2 unified interfaces |
| 6 | strowk/mcp-autotest | Go | YAML-based autotest tool |
| 7 | khalidsaidi/ragmap | TypeScript | RAG-focused MCP subregistry + discovery server: semantic/keyword search, filters (transport, hasRemote, reachable), MCP tools for finding retrieval-capable servers. [GitHub](https://github.com/khalidsaidi/ragmap) · [API](https://ragmap-api.web.app) |

### Hosting Solutions

| # | Tool Name | Description |
|---|-----------|-------------|
| 1 | Glama | Platform for hosting open-source MCP servers |
| 2 | Smithery | Cloud hosting for MCP servers via containers |

### Templates

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | fastmcp-boilerplate | TypeScript | MCP server built with FastMCP |
| 2 | dart-mcp-server-template | Dart | Template for Dart MCP servers |
| 3 | rails-mcp-startup-boilerplate | Ruby | Rails template for paid MCP servers |

## Docker MCP Toolkit

Docker provides a comprehensive MCP Toolkit with over 100 pre-built MCP servers that are ready to use with Claude and other MCP clients.

There are currently 109 MCP servers available:

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | github | Manage GitHub repositories and perform Git operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 2 | docker | Integrate with Docker to manage containers, images, and networks | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 3 | kubernetes | Orchestrate and manage containerized applications with Kubernetes | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 4 | puppeteer | Automate browser interactions and scrape web content | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/puppeteer.md) |
| 5 | stripe | Process payments and manage financial transactions | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/stripe.md) |
| 6 | slack | Send and receive messages in Slack workspaces | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/slack.md) |
| 7 | postgres | Interact with PostgreSQL databases | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgres.md) |
| 8 | redis | Interact with Redis in-memory data structure store | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis.md) |
| 9 | brave | Perform web searches using Brave's privacy-focused search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/brave.md) |
| 10 | notion | Create and manage content in Notion workspaces | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/notion.md) |
| 11 | elasticsearch | Search, analyze, and visualize data with Elasticsearch | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elasticsearch.md) |
| 12 | gitlab | Interact with GitLab repositories and CI/CD pipelines | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gitlab.md) |
| 13 | azure | Interact with Microsoft Azure cloud services and resources | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/azure.md) |
| 14 | gdrive | Access and manage files in Google Drive | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gdrive.md) |
| 15 | grafana | Create and manage Grafana dashboards and visualizations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/grafana.md) |
| 16 | obsidian | Work with Obsidian notes and knowledge management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/obsidian.md) |
| 17 | atlassian | Integrate with Atlassian products like Jira and Confluence | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlassian.md) |
| 18 | tavily | AI-powered web search and research assistant | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tavily.md) |
| 19 | shopify | Manage Shopify e-commerce stores and products | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/shopify.md) |
| 20 | sentry | Monitor application errors and performance | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/sentry.md) |
| 21 | 302_sandbox | A sandbox environment for testing HTTP redirects and status codes | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/302_sandbox.md) |
| 22 | 3d-printer | Control and monitor 3D printers with slice file management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/3d-printer.md) |
| 23 | armor-crypto | Secure encryption and decryption tools for sensitive data | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/armor-crypto.md) |
| 24 | astra-db | Interact with DataStax Astra DB, a cloud-native Cassandra database | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/astra-db.md) |
| 25 | atlas-docs | Access MongoDB Atlas documentation and best practices | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlas-docs.md) |
| 26 | audiense-insights | Access audience analytics and marketing insights data | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/audiense-insights.md) |
| 27 | aws-kb-retrieval-server | Retrieve information from AWS Knowledge Bases | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/aws-kb-retrieval-server.md) |
| 28 | barryyip0625-mcp-discord | Communicate with Discord servers and channels | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/barryyip0625-mcp-discord.md) |
| 29 | basic-memory | Simple memory persistence for AI conversations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/basic-memory.md) |
| 30 | bitrefill | Purchase gift cards and mobile refills with cryptocurrency | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/bitrefill.md) |
| 31 | box | Manage files and folders in Box cloud storage | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/box.md) |
| 32 | chroma | Interact with Chroma vector database for embeddings and retrieval | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/chroma.md) |
| 33 | circleci | Manage CI/CD pipelines and workflows in CircleCI | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/circleci.md) |
| 34 | context7 | Provide contextual information for enhanced AI conversations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/context7.md) |
| 35 | cyreslab-ai-shodan | Search for internet-connected devices using Shodan | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/cyreslab-ai-shodan.md) |
| 36 | dappier | Access real-time data from trusted sources across multiple domains | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/dappier.md) |
| 37 | dart | Manage projects and tasks in Dart project management tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/dart.md) |
| 38 | databutton | Build and deploy data apps with Python and Streamlit | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/databutton.md) |
| 39 | descope | Implement secure user authentication and authorization | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/descope.md) |
| 40 | desktop-commander | Control desktop applications and perform system operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/desktop-commander.md) |
| 41 | devhub-cms | Manage content with DevHub CMS | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/devhub-cms.md) |
| 42 | doit | Task management and productivity tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/doit.md) |
| 43 | duckduckgo | Privacy-focused web search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/duckduckgo.md) |
| 44 | e2b | Cloud-based development environment | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/e2b.md) |
| 45 | edubase | Education management platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/edubase.md) |
| 46 | elevenlabs | AI voice generation and text-to-speech | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/elevenlabs.md) |
| 47 | everart | AI art generation and manipulation | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/everart.md) |
| 48 | exa | Advanced replacement for the traditional ls command | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/exa.md) |
| 49 | fetch | Web content retrieval tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fetch.md) |
| 50 | fibery | Connected work platform for knowledge management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fibery.md) |
| 51 | filesystem | Interact with file system and perform file operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/filesystem.md) |
| 52 | firecrawl | Web crawling and content extraction tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/firecrawl.md) |
| 53 | flexprice | Dynamic pricing solution for businesses | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/flexprice.md) |
| 54 | github-chat | GitHub discussions and collaboration integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github-chat.md) |
| 55 | github-official | Official GitHub API integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github-official.md) |
| 56 | glif | Blockchain and crypto management platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/glif.md) |
| 57 | google-maps | Geographic information and location services | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/google-maps.md) |
| 58 | gyazo | Screenshot capturing and sharing service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gyazo.md) |
| 59 | hackle | Feature flag and experiment management platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hackle.md) |
| 60 | handwriting-ocr | Optical character recognition for handwritten text | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/handwriting-ocr.md) |
| 61 | heroku | Cloud platform as a service (PaaS) | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/heroku.md) |
| 62 | husqvarna-automower | Control and monitor Husqvarna robotic lawn mowers | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/husqvarna-automower.md) |
| 63 | hyperbrowser | Advanced web browsing and automation tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hyperbrowser.md) |
| 64 | hyperspell | AI-powered grammar and spelling checking | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/hyperspell.md) |
| 65 | iaptic | Subscription and payment management tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/iaptic.md) |
| 66 | jetbrains | Integrate with JetBrains IDEs and tools | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/jetbrains.md) |
| 67 | kagisearch | Neural search engine for web content | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kagisearch.md) |
| 68 | kong | API gateway and service mesh platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kong.md) |
| 69 | lara | AI-powered content research and writing assistant | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/lara.md) |
| 70 | line | Messaging application and platform integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/line.md) |
| 71 | mcp-discord | Discord messaging and community management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-discord.md) |
| 72 | mcp-notion-server | Notion workspace integration and management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-notion-server.md) |
| 73 | multiversx-mx | Blockchain infrastructure and smart contract platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/multiversx-mx.md) |
| 74 | neo4j-cloud-aura-api | Managed graph database cloud service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-cloud-aura-api.md) |
| 75 | neo4j-cypher | Graph database query language and integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-cypher.md) |
| 76 | neo4j-memory | In-memory storage for Neo4j operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-memory.md) |
| 77 | neo4j-server | Graph database server management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neo4j-server.md) |
| 78 | neon | Serverless PostgreSQL database service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neon.md) |
| 79 | neondatabase-labs | Experimental features for Neon database | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/neondatabase-labs.md) |
| 80 | octomind | Automated testing and quality assurance platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/octomind.md) |
| 81 | openapi-schema | API definition and documentation standard | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/openapi-schema.md) |
| 82 | opik | Advanced image processing and generation | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/opik.md) |
| 83 | osp_marketing_tools | Online marketing and promotion tools | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/osp_marketing_tools.md) |
| 84 | oxylabs | Web scraping and data extraction tools | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/oxylabs.md) |
| 85 | perplexity-ask | AI-powered question answering system | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/perplexity-ask.md) |
| 86 | playwright | Browser automation and testing framework | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/playwright.md) |
| 87 | postgresql | Object-relational database system | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgresql.md) |
| 88 | pulumi | Infrastructure as code platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/pulumi.md) |
| 89 | razorpay | Payment gateway and financial services platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/razorpay.md) |
| 90 | redis-cloud | Managed Redis database service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/redis-cloud.md) |
| 91 | resend | Email delivery and management service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/resend.md) |
| 92 | risken | Security risk management platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/risken.md) |
| 93 | scrapegraph | Web scraping and data visualization | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/scrapegraph.md) |
| 94 | scrapezy | Automated web scraping and data extraction | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/scrapezy.md) |
| 95 | smithery-cli | Command-line interface for Smithery platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/smithery-cli.md) |
| 96 | tembo | Enhanced PostgreSQL database platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tembo.md) |
| 97 | time | Time management and tracking utilities | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/time.md) |
| 98 | triplewhale | E-commerce analytics and marketing platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/triplewhale.md) |
| 99 | tweetbinder | Twitter/X analytics and social media insights | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tweetbinder.md) |
| 100 | v-3-discordmcp | Discord messaging and community management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/v-3-discordmcp.md) |
| 101 | veyrax | Web application security and testing platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/veyrax.md) |
| 102 | webflow | Visual website design and content management system | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/webflow.md) |
| 103 | wikipedia-mcp | Wikipedia knowledge retrieval | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wikipedia-mcp.md) |
| 104 | wolfram-alpha | Computational knowledge engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/wolfram-alpha.md) |
| 105 | youtube_transcript | YouTube video transcript extraction | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/youtube_transcript.md) |
| 106 | docker | Manage Docker containers, images, and Docker Hub | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/docker.md) |
| 107 | github | Manage GitHub repositories and perform Git operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/github.md) |
| 108 | kubernetes | Orchestrate and manage containerized applications | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/kubernetes.md) |
| 109 | postgresql | Interact with PostgreSQL databases | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/postgresql.md) |

### Security & Authentication

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | sentry | Monitor application errors and performance | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/sentry.md) |
| 2 | cyreslab-ai-shodan | Search for internet-connected devices using Shodan | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/cyreslab-ai-shodan.md) |
| 3 | descope | Implement secure user authentication and authorization | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/descope.md) |
| 4 | armor-crypto | Secure encryption and decryption tools for sensitive data | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/armor-crypto.md) |
| 5 | **VirusTotal** | File and URL security analysis | TBD | [GitHub](https://github.com/skydeckai/virustotal-mcp-server) |
| 6 | risken | Security risk management platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/risken.md) |
| 7 | **mcp-for-beginners** | This open-source curriculum introduces the fundamentals of Model Context Protocol (MCP) through real-world, cross-language examples in .NET, Java, TypeScript, JavaScript, Rust and Python. Designed for developers, it focuses on practical techniques for building modular, scalable, and secure AI workflows from session setup to service orchestration. | TBD | [GitHub](https://github.com/microsoft/mcp-for-beginners) |
| 8 | **fastapi_mcp** | Expose your FastAPI endpoints as Model Context Protocol (MCP) tools, with Auth! | TBD | [GitHub](https://github.com/tadata-org/fastapi_mcp) |
| 9 | **klavis** | Klavis AI:  MCP integration platforms that let AI agents use tools reliably at any scale | TBD | [GitHub](https://github.com/Klavis-AI/klavis) |
| 10 | **osaurus** | Own your AI. The native macOS harness for AI agents -- any model, persistent memory, autonomous execution, cryptographic identity. Built in Swift. Fully offline. Open source. | TBD | [GitHub](https://github.com/osaurus-ai/osaurus) |
| 11 | **ENScan_GO** | 一款基于各大企业信息API的工具，解决在遇到的各种针对国内企业信息收集难题。一键收集控股公司ICP备案、APP、小程序、微信公众号等信息聚合导出。支持MCP接入 | TBD | [GitHub](https://github.com/wgpsec/ENScan_GO) |
| 12 | **Gmail-MCP-Server** | A Model Context Protocol (MCP) server for Gmail integration in Claude Desktop with auto authentication support. This server enables AI assistants to manage Gmail through natural language interactions. | TBD | [GitHub](https://github.com/GongRzhe/Gmail-MCP-Server) |

### Development Tools

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | filesystem | Interact with file system and perform file operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/filesystem.md) |
| 2 | e2b | Cloud-based development environment | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/e2b.md) |
| 3 | octomind | Automated testing and quality assurance platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/octomind.md) |
| 4 | openapi-schema | API definition and documentation standard | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/openapi-schema.md) |
| 5 | desktop-commander | Control desktop applications and perform system operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/desktop-commander.md) |
| 6 | Roundtable | Zero-configuration MCP server that unifies multiple AI coding assistants (Claude Code, Cursor, GPT-4) for enhanced development workflows | Production Ready | [GitHub](https://github.com/askbudi/roundtable) |
| 7 | **n8n-mcp** | A MCP for Claude Desktop / Claude Code / Windsurf / Cursor to build n8n workflows for you  | TBD | [GitHub](https://github.com/czlonkowski/n8n-mcp) |
| 8 | **xiaohongshu-mcp** | MCP for xiaohongshu.com | TBD | [GitHub](https://github.com/xpzouying/xiaohongshu-mcp) |
| 9 | **Awesome-MCP-ZH** | MCP 资源精选， MCP指南，Claude MCP，MCP Servers, MCP Clients | TBD | [GitHub](https://github.com/yzfly/Awesome-MCP-ZH) |
| 10 | **XcodeBuildMCP** | A Model Context Protocol (MCP) server and CLI that provides tools for agent use when working on iOS and macOS projects. | TBD | [GitHub](https://github.com/getsentry/XcodeBuildMCP) |
| 11 | **fast-agent** | Code, Build and Evaluate agents - excellent Model and Skills/MCP/ACP Support | TBD | [GitHub](https://github.com/evalstate/fast-agent) |
| 12 | **memory-bank-mcp** | A Model Context Protocol (MCP) server implementation for remote memory bank management, inspired by Cline Memory Bank. | TBD | [GitHub](https://github.com/alioshr/memory-bank-mcp) |
| 13 | **awesome-mcp-servers** | A curated list of Model Context Protocol (MCP) servers | TBD | [GitHub](https://github.com/wong2/awesome-mcp-servers) |
| 14 | **Office-PowerPoint-MCP-Server** | A MCP (Model Context Protocol) server for PowerPoint manipulation using python-pptx. This server provides tools for creating, editing, and manipulating PowerPoint presentations through the MCP protocol. | TBD | [GitHub](https://github.com/GongRzhe/Office-PowerPoint-MCP-Server) |
| 15 | **damn-vulnerable-MCP-server** | Damn Vulnerable MCP Server | TBD | [GitHub](https://github.com/harishsg993010/damn-vulnerable-MCP-server) |
| 16 | **drawio-mcp-server** | Draw.io Model Context Protocol (MCP) Server | TBD | [GitHub](https://github.com/lgazo/drawio-mcp-server) |
| 17 | **awesome-remote-mcp-servers** | Remote MCP Servers | TBD | [GitHub](https://github.com/jaw9c/awesome-remote-mcp-servers) |
| 18 | **excel-mcp-server** | A Model Context Protocol (MCP) server that reads and writes MS Excel data | TBD | [GitHub](https://github.com/negokaz/excel-mcp-server) |
| 19 | **server** | Core PHP implementation for the Model Context Protocol (MCP) server | TBD | [GitHub](https://github.com/php-mcp/server) |

### Communication

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | mcp-discord | Discord messaging and community management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-discord.md) |
| 2 | line | Messaging application and platform integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/line.md) |
| 3 | tweetbinder | Twitter/X analytics and social media insights | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tweetbinder.md) |
| 4 | **supabase-mcp-server** | Query MCP enables end-to-end management of Supabase via chat interface: read & write query executions, management API support, automatic migration versioning, access to logs and much more. | TBD | [GitHub](https://github.com/alexander-zuev/supabase-mcp-server) |
| 5 | **mcp-server-chatsum** | Query and Summarize your chat messages. | TBD | [GitHub](https://github.com/chatmcp/mcp-server-chatsum) |

### Knowledge Management

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | obsidian | Work with Obsidian notes and knowledge management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/obsidian.md) |
| 2 | fibery | Connected work platform for knowledge management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/fibery.md) |
| 3 | context7 | Provide contextual information for enhanced AI conversations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/context7.md) |
| 4 | atlas-docs | Access MongoDB Atlas documentation and best practices | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/atlas-docs.md) |

### Multimedia & Design

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | gyazo | Screenshot capturing and sharing service | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/gyazo.md) |
| 2 | handwriting-ocr | Optical character recognition for handwritten text | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/handwriting-ocr.md) |
| 3 | webflow | Visual website design and content management system | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/webflow.md) |
| 4 | youtube_transcript | YouTube video transcript extraction | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/youtube_transcript.md) |
| 5 | speech-ai | Speech AI with pronunciation assessment, text-to-speech, and speech-to-text | TBD | [GitHub](https://github.com/fasuizu-br/speech-ai-examples) |



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
