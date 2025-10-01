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

### Web & Content

MCP servers for web search, content access, and web automation.

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | brave | Perform web searches using Brave's privacy-focused search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/brave.md) |
| 2 | notion | Create and manage content in Notion workspaces | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/notion.md) |
| 3 | puppeteer | Automate browser interactions and scrape web content | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/puppeteer.md) |
| 4 | duckduckgo | Privacy-focused web search engine | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/duckduckgo.md) |
| 5 | firecrawl | Web crawling and content extraction tool | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/firecrawl.md) |

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

### Utilities

| # | Tool Name | Language | Description |
|---|-----------|----------|-------------|
| 1 | hamidra/yamcp | TypeScript | MCP workspace manager |
| 2 | punkpeye/mcp-proxy | TypeScript | SSE proxy for MCP servers |
| 3 | multi-mcp | Python | Multi-MCP Proxy Server |
| 4 | f/MCPTools | Go | CLI tool for MCP server interactions |
| 5 | strowk/mcp-autotest | Go | YAML-based autotest tool |

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

### Development Tools

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | filesystem | Interact with file system and perform file operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/filesystem.md) |
| 2 | e2b | Cloud-based development environment | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/e2b.md) |
| 3 | octomind | Automated testing and quality assurance platform | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/octomind.md) |
| 4 | openapi-schema | API definition and documentation standard | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/openapi-schema.md) |
| 5 | desktop-commander | Control desktop applications and perform system operations | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/desktop-commander.md) |
| 6 | **Roundtable** | **Zero-configuration MCP server that unifies multiple AI coding assistants (Claude Code, Cursor, GPT-4) for enhanced development workflows** | **Production Ready** | [GitHub](https://github.com/askbudi/roundtable) |

### Communication

| # | MCP Server | Description | Docker Hub Pulls | Link |
|---|------------|-------------|------------------|------|
| 1 | mcp-discord | Discord messaging and community management | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/mcp-discord.md) |
| 2 | line | Messaging application and platform integration | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/line.md) |
| 3 | tweetbinder | Twitter/X analytics and social media insights | TBD | [GitHub](https://github.com/docker/labs-ai-tools-for-devs/blob/main/prompts/mcp/tweetbinder.md) |

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
