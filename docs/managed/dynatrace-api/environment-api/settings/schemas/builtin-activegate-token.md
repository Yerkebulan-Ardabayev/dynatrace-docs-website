---
title: Settings API - Network security schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-activegate-token
---

# Settings API - Network security schema table

# Settings API - Network security schema table

* Published Dec 05, 2023

### Network security (`builtin:activegate-token)`

Dynatrace assures out-of-the-box connection security between Dynatrace environment’s elements.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:activegate-token` | * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:activegate-token` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:activegate-token` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:activegate-token` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Manually enforce ActiveGate token authentication `authTokenEnforcementManuallyEnabled` | boolean | - | Required |
| Enable notifications about ActiveGate tokens expiration dates `expiringTokenNotificationsEnabled` | boolean | Note: ActiveGate tokens notifications are sent only when you deployed ActiveGate tokens with expiration dates in your environment and notifications are defined (see notification settings (`<your-dynatrace-url>//ui/settings/builtin:problem.notifications`)) | Required |