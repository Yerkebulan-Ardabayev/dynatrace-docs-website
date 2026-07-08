---
title: Settings API - Apdex configuration for load actions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-key-performance-metric-load-actions
---

# Settings API - Apdex configuration for load actions schema table

# Settings API - Apdex configuration for load actions schema table

* Published Dec 05, 2023

### Apdex configuration for load actions (`builtin:rum.web.key-performance-metric-load-actions)`

Select a key performance metric and set the Tolerating and Frustrated performance thresholds to [refine the Apdex calculations﻿](https://dt-url.net/apdex-thresholds) for this application.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.key-performance-metric-load-actions` | * `group:rum-kpm-settings` * `group:rum-settings` | `APPLICATION_METHOD` - User Action  `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.key-performance-metric-load-actions` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key performance metric `kpm` | enum | The element has these enums * `USER_ACTION_DURATION` * `VISUALLY_COMPLETE` * `SPEED_INDEX` * `DOM_INTERACTIVE` * `LOAD_EVENT_END` * `LOAD_EVENT_START` * `RESPONSE_END` * `RESPONSE_START` * `FIRST_INPUT_DELAY` * `LARGEST_CONTENTFUL_PAINT` * `CUMULATIVE_LAYOUT_SHIFT` | Required |
| Key performance metric thresholds `thresholds` | [Thresholds](#Thresholds) | Set the Tolerating and Frustrated performance thresholds for this action type. | Required |
| Fallback metric thresholds `fallbackThresholds` | [FallbackThresholds](#FallbackThresholds) | If the selected key performance metric is not detected, the **User action duration** metric is used instead. | Required |

##### The `Thresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Tolerating threshold `toleratedThresholdSeconds` | float | If the key performance metric is below this value, the action is assigned to the Satisfied performance zone. | Required |
| Frustrated threshold `frustratingThresholdSeconds` | float | If the key performance metric is above this value, the action is assigned to the Frustrated performance zone. | Required |

##### The `FallbackThresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Tolerating threshold [sec] `toleratedFallbackThresholdSeconds` | float | If **User action duration** is below this value, the action is assigned to the Satisfied performance zone. | Required |
| Frustrated threshold [sec] `frustratingFallbackThresholdSeconds` | float | If **User action duration** is above this value, the action is assigned to the Frustrated performance zone. | Required |