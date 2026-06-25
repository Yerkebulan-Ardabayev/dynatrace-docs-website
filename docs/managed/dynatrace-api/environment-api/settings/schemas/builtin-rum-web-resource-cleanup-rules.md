---
title: Settings API - Resource URL cleanup rules schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-resource-cleanup-rules
scraped: 2026-05-12T11:48:05.682344
---

# Settings API - Resource URL cleanup rules schema table

# Settings API - Resource URL cleanup rules schema table

* Published Dec 05, 2023

### Resource URL cleanup rules (`builtin:rum.web.resource-cleanup-rules)`

Resource URL cleanup rules are used to aggregate resource URLs that are otherwise identical except for dynamic elements such as IDs (for example, from REST APIs), query strings (for example, random arguments that disable caching), and other session data. Once such session-specific detail is stripped away, URLs are displayed in aggregate within waterfall analysis view. Note that resource URL cleanup rules are executed in the order specified below. For complete details about cleanup rules, visit [Define URL cleanup rulesï»¿](https://dt-url.net/resource-cleanup-rules-response-codes).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.resource-cleanup-rules` | * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.content-resources` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.resource-cleanup-rules` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | For example: *Mask journeyId* | Required |
| Regular expression `regularExpression` | text | For example: `(.*)(journeyId=)-?\d+(.*)` | Required |
| Replace with `replaceWith` | text | For example: `$1$2\*$3` | Required |