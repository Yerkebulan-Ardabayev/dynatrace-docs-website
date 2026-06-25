---
title: Settings API - Hub subscriptions schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hub-channel-subscriptions
scraped: 2026-05-12T11:42:28.130379
---

# Settings API - Hub subscriptions schema table

# Settings API - Hub subscriptions schema table

* Published Feb 26, 2024

### Hub subscriptions (`builtin:hub-channel.subscriptions)`

Here you can manage your subscriptions to extend the available apps or releases listed in [Dynatrace Hubï»¿](https://www.dynatrace.com/support/help/manage/hub). Add a new token to enroll your subscription.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hub-channel.subscriptions` | * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hub-channel.subscriptions` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Subscriptions `tokenSubscriptions` | [TokenSubscription](#TokenSubscription)[] | - | Required |

##### The `TokenSubscription` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name of subscription `name` | text | - | Required |
| Subscription token `token` | text | - | Required |
| Description `description` | text | - | Optional |