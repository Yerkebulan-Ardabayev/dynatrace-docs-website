---
title: Settings API - Extension Execution Controller schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eec-local
---

# Settings API - Extension Execution Controller schema table

# Settings API - Extension Execution Controller schema table

* Published Dec 05, 2023

### Extension Execution Controller (`builtin:eec.local)`

Extension Execution Controller configuration for OneAgent deployment

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eec.local` | * `group:preferences` | `HOST` - Host  `HOST_GROUP` - Host Group  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.local` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eec.local` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.local` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Extension Execution Controller `enabled` | boolean | - | Required |
| Enable local HTTP Metric, Log and Event Ingest API `ingestActive` | boolean | - | Required |
| Enable Dynatrace StatsD `statsdActive` | boolean | This is applicable only to non-containerized Linux and Windows hosts | Required |
| Performance profile `performanceProfile` | enum | Select performance profile for Extension Execution Controller [Documentation﻿](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles") The element has these enums * `DEFAULT` * `HIGH` | Required |