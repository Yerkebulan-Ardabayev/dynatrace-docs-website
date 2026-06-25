---
title: Settings API - PHP schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-php
scraped: 2026-05-12T11:42:37.679277
---

# Settings API - PHP schema table

# Settings API - PHP schema table

* Published Dec 05, 2023

### PHP (`builtin:monitored-technologies.php)`

By default, PHP monitoring is enabled on all hosts. If you want to disable PHP monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable PHP monitoring only on selected hosts, disable global PHP monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.php` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.php` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.php` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.php` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor PHP `enabled` | boolean | - | Required |
| Enable FastCGI PHP processes launched by Apache HTTP Server `enabledFastCGI` | boolean | Requires PHP monitoring enabled and from Dynatrace OneAgent version 1.191 it's ignored and permanently enabled | Required |
| Monitor PHP CLI web server `enablePhpCliServerInstrumentation` | boolean | Requires enabled PHP monitoring and Dynatrace OneAgent version 1.261 or later | Required |