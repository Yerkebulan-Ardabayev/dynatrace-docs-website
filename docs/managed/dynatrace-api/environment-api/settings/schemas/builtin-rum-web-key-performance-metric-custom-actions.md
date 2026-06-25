---
title: Settings API - Apdex configuration for custom actions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-key-performance-metric-custom-actions
scraped: 2026-05-12T11:43:16.876223
---

# Settings API - Apdex configuration for custom actions schema table

# Settings API - Apdex configuration for custom actions schema table

* Published Dec 05, 2023

### Apdex configuration for custom actions (`builtin:rum.web.key-performance-metric-custom-actions)`

Set the Tolerating and Frustrated performance thresholds to [refine the Apdex calculationsï»¿](https://dt-url.net/apdex-thresholds) for this application.

The key performance metric for custom actions is always **User action duration**.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.key-performance-metric-custom-actions` | * `group:rum-kpm-settings` * `group:rum-settings` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-custom-actions` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| User action duration thresholds `thresholds` | [Thresholds](#Thresholds) | - | Required |

##### The `Thresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Tolerating threshold [sec] `toleratedThresholdSeconds` | float | If **User action duration** is below this value, the action is assigned to the Satisfied performance zone. | Required |
| Frustrated threshold [sec] `frustratingThresholdSeconds` | float | If **User action duration** is above this value, the action is assigned to the Frustrated performance zone. | Required |