---
title: Settings API - RUM overload prevention schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-overload-prevention
---

# Settings API - RUM overload prevention schema table

# Settings API - RUM overload prevention schema table

* Published Dec 05, 2023

### RUM overload prevention (`builtin:rum.overload-prevention)`

Adjust the limit below to control the overall cluster performance capacity and prevent unexpected high consumption of your license volume.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.overload-prevention` | * `group:web-and-mobile-monitoring.web-applications` * `group:web-and-mobile-monitoring` * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.overload-prevention` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.overload-prevention` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.overload-prevention` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Maximum user actions per minute `overloadPreventionLimit` | integer | Once this limit is reached, Dynatrace [throttles the number of captured user sessions﻿](https://dt-url.net/fm3v0p7g). | Required |