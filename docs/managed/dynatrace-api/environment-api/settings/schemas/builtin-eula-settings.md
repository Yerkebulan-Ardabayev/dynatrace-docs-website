---
title: Settings API - Terms of use schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eula-settings
---

# Settings API - Terms of use schema table

# Settings API - Terms of use schema table

* Published Dec 05, 2023

### Terms of use (`builtin:eula-settings)`

Display end user terms (recommended for customers that purchased via a reseller).

See our Third party licenses (`<your-dynatrace-url>//ui/third-party-licenses`).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eula-settings` | * `group:preferences` | `environment`  `environment-default` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eula-settings` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eula-settings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eula-settings` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Display end user terms to new users logging in to the environment `enableEula` | boolean | - | Required |