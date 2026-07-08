---
title: Settings API - User experience score schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-user-experience-score
---

# Settings API - User experience score schema table

# Settings API - User experience score schema table

* Published Dec 05, 2023

### User experience score (`builtin:rum.user-experience-score)`

A [user experience score﻿](https://dt-url.net/39034wt) is calculated for each user session. Scores reflect the overall performance, usability, and detected errors of each session. Experiences are classified as either Satisfying, Tolerable, or Frustrating.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.user-experience-score` | * `group:web-and-mobile-monitoring` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.user-experience-score` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.user-experience-score` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.user-experience-score` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| If last user action in a session is classified as Frustrating, classify the entire session as Frustrating `considerLastAction` | boolean | - | Required |
| Consider rage clicks / rage taps in score calculation `considerRageClick` | boolean | - | Required |
| Threshold for Frustrating user experience `maxFrustratedUserActionsThreshold` | integer | User experience is considered Frustrating when the selected percentage or more of the user actions in a session are rated as Frustrating. | Required |
| Threshold for Satisfying user experience `minSatisfiedUserActionsThreshold` | integer | User experience is considered Satisfying when at least the selected percentage of the user actions in a session are rated as Satisfying. | Required |