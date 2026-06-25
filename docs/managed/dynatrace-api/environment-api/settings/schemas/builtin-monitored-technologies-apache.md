---
title: Settings API - Apache HTTP Server schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-apache
scraped: 2026-05-12T11:41:36.393745
---

# Settings API - Apache HTTP Server schema table

# Settings API - Apache HTTP Server schema table

* Published Dec 05, 2023

### Apache HTTP Server (`builtin:monitored-technologies.apache)`

By default, Apache HTTP Server monitoring is enabled on all hosts. If you want to disable Apache HTTP Server monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable Apache HTTP Server monitoring only on selected hosts, disable global Apache HTTP Server monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.apache` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.apache` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.apache` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.apache` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor Apache HTTP Server `enabled` | boolean | - | Required |