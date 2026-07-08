---
title: Settings API - Enablement and cost control schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-custom-enablement
---

# Settings API - Enablement and cost control schema table

# Settings API - Enablement and cost control schema table

* Published Dec 05, 2023

### Enablement and cost control (`builtin:rum.custom.enablement)`

Turn on Real User Monitoring. Configure cost and traffic control settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.custom.enablement` | * `group:rum-general` * `group:web-and-mobile-monitoring` | `CUSTOM_APPLICATION` - Custom Application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.enablement` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.custom.enablement` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.custom.enablement` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Real User Monitoring `rum` | [rum](#rum) | Capture and analyze all user actions within your application. Enable [Real User Monitoring (RUM)﻿](https://dt-url.net/1n2b0prq) to monitor and improve your application's performance, identify errors, and gain insight into your user's behavior and experience. | Required |

##### The `rum` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Real User Monitoring `enabled` | boolean | - | Required |
| Cost and traffic control `costAndTrafficControl` | integer | Percentage of user sessions captured and analyzed  By default, Dynatrace captures all user actions and user sessions for analysis. This approach ensures complete insight into your application’s performance and customer experience. You can optionally reduce the granularity of user-action and user-session analysis by capturing a lower percentage of user sessions. While this approach can reduce monitoring costs, it also results in lower visibility into how your customers are using your applications. For example, a setting of 10% results in Dynatrace analyzing only every tenth user session. | Required |