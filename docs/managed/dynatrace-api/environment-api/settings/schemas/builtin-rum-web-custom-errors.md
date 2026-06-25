---
title: Settings API - Custom errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-errors
scraped: 2026-05-12T11:47:19.603264
---

# Settings API - Custom errors schema table

# Settings API - Custom errors schema table

* Published Dec 05, 2023

### Custom errors (`builtin:rum.web.custom-errors)`

Create rules to capture custom errors and include them in your Apdex calculations or Davis AI problem detection and analysis.
For more details, see [Configure custom errorsï»¿](https://dt-url.net/sh220gh).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-errors` | * `group:rum-errors` | `APPLICATION` - Web application  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-errors` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Ignore custom errors in Apdex calculations `ignoreCustomErrorsInApdexCalculation` | boolean | This setting overrides Apdex settings for individual rules listed below | Required |
| `errorRules` | [CustomErrorRule](#CustomErrorRule)[] | - | Required |

##### The `CustomErrorRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Match key `keyMatcher` | enum | The element has these enums * `ALL` * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Required |
| Key pattern `keyPattern` | text | A case-insensitive key pattern | Required |
| Match value `valueMatcher` | enum | The element has these enums * `ALL` * `BEGINS_WITH` * `ENDS_WITH` * `CONTAINS` * `EQUALS` | Required |
| Value pattern `valuePattern` | text | A case-insensitive value pattern | Required |
| Capture settings `captureSettings` | [CaptureSettings](#CaptureSettings) | - | Required |

##### The `CaptureSettings` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Capture this error `capture` | boolean | - | Required |
| Include error in Apdex calculations `impactApdex` | boolean | - | Required |
| Include error in Davis AI problem detection and analysis `considerForAi` | boolean | [View more detailsï»¿](https://dt-url.net/hd580p2k) | Required |