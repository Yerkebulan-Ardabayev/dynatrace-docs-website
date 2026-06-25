---
title: Settings API - Ingest routing configuration (logs) schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-openpipeline-logs-routing
scraped: 2026-05-12T11:46:30.352698
---

# Settings API - Ingest routing configuration (logs) schema table

# Settings API - Ingest routing configuration (logs) schema table

* Published Aug 25, 2025

### Ingest routing configuration (logs) (`builtin:openpipeline.logs.routing)`

Contains configuration of routing

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:openpipeline.logs.routing` | * `group:openpipeline.all.routing` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.logs.routing` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:openpipeline.logs.routing` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:openpipeline.logs.routing` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Routing for pipelines `routingEntries` | [RoutingEntry](#RoutingEntry)[] | - | Required |

##### The `RoutingEntry` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Pipeline Type `pipelineType` | enum | The element has these enums * `custom` * `builtin` | Required |
| Pipeline ID `pipelineId` | setting | - | Required |
| Builtin Pipeline ID `builtinPipelineId` | text | - | Required |
| Query which determines whether the record should be routed to the target pipeline of this rule. `matcher` | text | - | Required |
| Description `description` | text | - | Required |