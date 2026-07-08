---
title: Dynatrace Managed MCP server
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/managed-mcp-server
---

# Dynatrace Managed MCP server

# Dynatrace Managed MCP server

* Explanation
* 2-min read
* Updated on Jun 16, 2026

The Dynatrace Managed MCP server is an open-source server that implements the Model Context Protocol (MCP). It enables AI assistants to query observability data from self-hosted Dynatrace Managed environments. Instead of navigating the Dynatrace web UI manually, you can investigate problems, query metrics, and analyze security findings. You can do this directly from an AI assistant such as Claude Desktop or Visual Studio Code with GitHub Copilot.

The server is a community-supported project released under the MIT License. A separate MCP server exists for Dynatrace SaaS environments.

## Use cases

The MCP server is most useful when you need observability context without switching tools. Typical applications include:

* Investigating incidents by asking your AI assistant to retrieve problem details and related entity data
* Querying performance metrics and logs in natural language without constructing API calls manually
* Comparing production and staging environments to confirm whether a new version improves performance, load, or error rates
* Analyzing security vulnerabilities and compliance findings across your Managed environment
* Understanding monitored entity relationships through their dependency graphs
* Running multi-phase incident investigations that combine problems, logs, and metrics in a single conversation

### Multi-environment support

A single MCP server instance connects to multiple Managed environments simultaneously. Each environment has a short name that you reference in your prompts. This is useful for organizations that run separate Managed Clusters per region, team, or lifecycle stage.

You can also run the Managed MCP server alongside the Dynatrace SaaS MCP server. This supports hybrid migration scenarios where historical observability data remains on a Managed Cluster while live data is on Dynatrace SaaS.

## Available tools

The MCP server exposes the following observability data from each connected Managed environment:

* **Problems**: Active problems and their details
* **Entities**: Monitored entities and their relationships
* **Metrics**: Performance metrics via the V2 Metrics API
* **Logs**: Log content with content-based and time-based filtering
* **Events**: System events
* **Service level objectives**: Details, evaluations, and error budgets
* **Security**: Vulnerabilities and security problems

## Get started

Setup instructions, configuration options, and AI client integration examples are available in the [Dynatrace Managed MCP server repository﻿](https://github.com/dynatrace-oss/dynatrace-managed-mcp).