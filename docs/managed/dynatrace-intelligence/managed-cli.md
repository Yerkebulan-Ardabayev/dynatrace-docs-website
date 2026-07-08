---
title: Dynatrace Managed CLI
source: https://docs.dynatrace.com/managed/dynatrace-intelligence/managed-cli
---

# Dynatrace Managed CLI

# Dynatrace Managed CLI

* Explanation
* 2-min read
* Updated on Jun 11, 2026

The Dynatrace Managed CLI (`dtmgd`) is an open-source, read-only command-line tool for querying observability data from Managed Clusters. It provides terminal access to the Managed classic API. You can use it to script access to problems, entities, metrics, logs, events, service level objectives (SLOs), and security data without using the Dynatrace web UI. The CLI follows the same model as `dtctl`, the equivalent tool for Dynatrace SaaS.

## Use cases

* **Scripting and automation**: Use table, wide, JSON, and YAML output formats to integrate CLI output into shell scripts, CI pipelines, and monitoring workflows. Automatic pagination handles large result sets without additional scripting.
* **Multi-environment queries**: Run a single command across multiple configured environments in parallel and merge the results. This is useful for organizations that run separate Managed Clusters per region or team and need a unified view across them.
* **Real-time monitoring**: Use watch mode to re-run a query at configurable intervals and get a live terminal view of changing data such as open problems or recent events.
* **AI assistant integration**: Use the CLI as a data source for AI assistants and large language model pipelines that consume structured observability data. The CLI detects AI assistant environments and wraps output in structured JSON envelopes.

## Available commands

The CLI organizes access to Managed data into four command categories:

* **get**: List resources with filtering and sorting options
* **describe**: Retrieve detailed output for individual resources
* **query**: Fetch time-range data with aggregation and custom resolution
* **config**: Manage environment contexts and stored credentials

The following resource types are accessible across all command categories:

* Problems
* Entities and entity types
* Events
* Metrics
* Logs
* Service level objectives
* Security vulnerabilities
* Audit logs
* Network zones

## Get started

Installation instructions, configuration, and the full command reference are available in the [Dynatrace Managed CLI repository﻿](https://github.com/dynatrace-oss/dtmgd).