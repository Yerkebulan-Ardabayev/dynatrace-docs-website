---
title: Settings API - Usability analytics schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-usability-analytics
---

# Settings API - Usability analytics schema table

# Settings API - Usability analytics schema table

* Published Dec 05, 2023

### Usability analytics (`builtin:usability-analytics)`

Analyze detected usability issues within your application.

User action types that commonly reflect user frustration include dead clicks, rage clicks, rage rotates, and page refreshes.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:usability-analytics` | * `group:web-and-mobile-monitoring` * `group:preferences` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:usability-analytics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:usability-analytics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:usability-analytics` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Detect rage clicks `detectRageClicks` | boolean | Three or more rapid clicks within the same area of a web page are considered to be rage clicks. Rage clicks commonly reflect slow-loading or failed page resources. Rage click counts are compiled for each session and considered in the [User Experience Score﻿](https://dt-url.net/39034wt) . With this setting enabled, a rage click count is compiled for each monitored user session. | Required |