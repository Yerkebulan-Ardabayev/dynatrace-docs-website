---
title: Settings API - Apdex configuration schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-key-performance-metrics
---

# Settings API - Apdex configuration schema table

# Settings API - Apdex configuration schema table

* Published Dec 05, 2023

### Apdex configuration (`builtin:rum.mobile.key-performance-metrics)`

[Set the user-satisfaction performance thresholds﻿](https://dt-url.net/4l023z2) (**Satisfactory**, **Tolerable**, and **Frustrating**) for the **User action duration** metric to refine the Apdex calculations for this app.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.key-performance-metrics` | * `group:rum-general` | `DEVICE_APPLICATION_METHOD` - Mobile app key user action  `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.key-performance-metrics` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `thresholds` | [Thresholds](#Thresholds) | - | Required |
| Consider reported errors / web request errors in Apdex calculations `frustratingIfReportedOrWebRequestError` | boolean | Treat user actions with reported errors or web request errors as erroneous and rate their performance as Frustrating. Turn off this setting if errors should not affect the Apdex rate. | Required |

##### The `Thresholds` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Tolerable performance [sec] `tolerableThresholdSeconds` | float | If the action duration is below this value, the Apdex is considered to be **Satisfactory**. | Required |
| Frustrating performance [sec] `frustratingThresholdSeconds` | float | If the action duration is above this value, the Apdex is considered to be **Frustrating**. | Required |