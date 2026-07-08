---
title: Settings API - Custom configuration properties schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-web-custom-configuration-properties
---

# Settings API - Custom configuration properties schema table

# Settings API - Custom configuration properties schema table

* Published Apr 03, 2024

### Custom configuration properties (`builtin:rum.web.custom-configuration-properties)`

Here you can set additional JavaScript tag properties that are specific to your application. To do this, type key-value pairs defined using (=).

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.web.custom-configuration-properties` | * `group:capturing` * `group:web-and-mobile-monitoring` * `group:web-and-mobile-monitoring.capturing` | `APPLICATION` - Web application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.web.custom-configuration-properties` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Custom configuration property `customProperty` | text | - | Required |