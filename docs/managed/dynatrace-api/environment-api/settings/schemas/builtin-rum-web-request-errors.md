---
title: Settings API - Request errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-request-errors
scraped: 2026-05-12T11:42:18.893365
---

# Settings API - Request errors schema table

# Settings API - Request errors schema table

* Published Dec 05, 2023

### Request errors (`builtin:rum.web.request-errors)`

Create capture and detection rules to include request errors in your Apdex calculations or Davis AI problem detection and analysis.
For more details, see [Configure request errorsï»¿](https://dt-url.net/13020hh).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.request-errors` | * `group:rum-errors` | `APPLICATION` - Web application  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.request-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.request-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.request-errors` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ignore request errors in Apdex calculations `ignoreRequestErrorsInApdexCalculation` | boolean | This setting overrides Apdex settings for individual rules listed below | Required |
| `errorRules` | [RequestErrorRule](#RequestErrorRule)[] | - | Required |

##### The `RequestErrorRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Match by error code `errorCodes` | text | - | Optional |
| Match by errors that have failed image requests `considerFailedImages` | boolean | - | Required |
| Match by errors that have CSP violations `considerCspViolations` | boolean | - | Required |
| Filter settings `filterSettings` | [FilterSettings](#FilterSettings) | - | Required |
| Capture settings `captureSettings` | [CaptureSettings](#CaptureSettings) | - | Required |

##### The `FilterSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Filter by URL `filter` | enum | The element has these enums * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Optional |
| URL `url` | text | - | Required |

##### The `CaptureSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Capture this error `capture` | boolean | - | Required |
| Include error in Apdex calculations `impactApdex` | boolean | - | Required |
| Include error in Davis AI problem detection and analysis `considerForAi` | boolean | [View more detailsï»¿](https://dt-url.net/hd580p2k) | Required |