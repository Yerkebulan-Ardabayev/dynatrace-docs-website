---
title: Settings API - Muted requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-settings-mutedrequests
scraped: 2026-05-12T11:39:16.262269
---

# Settings API - Muted requests schema table

# Settings API - Muted requests schema table

* Published Dec 05, 2023

### Muted requests (`builtin:settings.mutedrequests)`

Configuration for specifying Muted requests for particular Service. Each Service could have several Muted requests.

Dynatrace enables you to mute automatic alerts for selected, unimportant service requests. This will also exclude them from the service chart so that you can focus on the performance of requests that affect your customers. You can learn more about Muted requests in our [helpï»¿](https://dt-url.net/ze62t5p "Visit dynatrace.com")

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:settings.mutedrequests` | - | `SERVICE` - Service |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.mutedrequests` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:settings.mutedrequests` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.mutedrequests` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Muted request names `mutedRequestNames` | set | - | Required |