---
title: Settings API - Enablement and cost control schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-enablement
---

# Settings API - Enablement and cost control schema table

# Settings API - Enablement and cost control schema table

* Published Dec 05, 2023

### Enablement and cost control (`builtin:rum.web.enablement)`

Turn on Real User Monitoring and Session Replay. Configure cost and traffic control settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.enablement` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:rum-settings` | `APPLICATION` - Web application  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.enablement` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.enablement` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.enablement` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Real User Monitoring `rum` | [rum](#rum) | Capture and analyze all user actions within your application. Enable [Real User Monitoring (RUM)﻿](https://dt-url.net/1n2b0prq) to monitor and improve your application's performance, identify errors, and gain insight into your user's behavior and experience. | Required |
| Session Replay `sessionReplay` | [sessionReplay](#sessionReplay) | [Session Replay﻿](https://dt-url.net/session-replay) captures all user interactions within your application and replays them in a movie-like experience while providing [best-in-class security and data protection﻿](https://dt-url.net/b303zxj). | Required |
| User Interactions `experienceAnalytics` | [experienceAnalytics](#experienceAnalytics) | - | Optional |

##### The `rum` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Real User Monitoring Classic `enabled` | boolean | - | Required |
| Enable New Real User Monitoring Experience `enabledOnGrail` | boolean | - | Optional |
| Cost and traffic control `costAndTrafficControl` | integer | Percentage of user sessions captured and analyzed | Required |

##### The `sessionReplay` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable Session Replay Classic `enabled` | boolean | Before enabling, Dynatrace checks your system against the prerequisites for [Session Replay Classic﻿](https://dt-url.net/ma3m0psf). | Required |
| Enable New Session Replay Experience `enabledOnGrail` | boolean | - | Optional |
| Cost and traffic control `costAndTrafficControl` | integer | [Percentage of user sessions recorded with Session Replay Classic﻿](https://dt-url.net/sr-cost-traffic-control). For example, if you have 50% for RUM and 50% for Session Replay Classic, it results in 25% of sessions recorded with Session Replay Classic. | Required |

##### The `experienceAnalytics` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable User Interactions `enabled` | boolean | Capture user interactions within your frontend, including all clicks and taps. During the Early Access period, there’s no cost associated with this feature. | Required |