---
title: Settings API - Dynatrace mobile app schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-mobile-notifications
---

# Settings API - Dynatrace mobile app schema table

# Settings API - Dynatrace mobile app schema table

* Published Feb 26, 2024

### Dynatrace mobile app (`builtin:mobile.notifications)`

The Dynatrace mobile application for iOS and Android enables users to receive customized push notifications on their mobile devices. Refer to the instructions below to set up the Dynatrace mobile app's access within this environment.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:mobile.notifications` | * `group:integration` | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mobile.notifications` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:mobile.notifications` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:mobile.notifications` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | Enables mobile push notifications for Davis® problems. On Dynatrace Managed environments, additionally enables mobile QR code generation. | Required |