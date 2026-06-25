---
title: Settings API - Nginx schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-nginx
scraped: 2026-05-12T11:45:21.035241
---

# Settings API - Nginx schema table

# Settings API - Nginx schema table

* Published Dec 05, 2023

### Nginx (`builtin:monitored-technologies.nginx)`

By default, Nginx monitoring is enabled on all hosts. If you want to disable Nginx monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable Nginx monitoring only on selected hosts, disable global Nginx monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.nginx` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.nginx` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor Nginx `enabled` | boolean | - | Required |