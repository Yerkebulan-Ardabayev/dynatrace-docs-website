---
title: Settings API - .NET schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-dotnet
scraped: 2026-05-12T11:42:10.958888
---

# Settings API - .NET schema table

# Settings API - .NET schema table

* Published Dec 05, 2023

### .NET (`builtin:monitored-technologies.dotnet)`

By default, .NET monitoring is enabled on all hosts. If you want to disable .NET monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable .NET monitoring only on selected hosts, disable global .NET monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.dotnet` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.dotnet` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor .NET `enabled` | boolean | - | Required |
| Enable .NET Core `enabledDotNetCore` | boolean | - | Required |