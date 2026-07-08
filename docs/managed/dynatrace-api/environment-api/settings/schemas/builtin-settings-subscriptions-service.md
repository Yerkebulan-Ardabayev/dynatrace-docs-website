---
title: Settings API - Key requests schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-settings-subscriptions-service
---

# Settings API - Key requests schema table

# Settings API - Key requests schema table

* Published Dec 05, 2023

### Key requests (`builtin:settings.subscriptions.service)`

Configuration for specifying Key requests for a particular Service. Each Service could have several Key requests.

* Key requests can be used to have long-term metric history and dedicated dashboard tiles for charting and direct access from your dashboard. Request naming rules can affect Key requests and vice versa.
* When you set up a Request naming rule that affects Key requests, to keep a renamed request as Key request you must provide the final name (after all Request naming rules are applied) here.

You can learn more about Key requests in our [help﻿](https://dt-url.net/ss03uui "Visit dynatrace.com").

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:settings.subscriptions.service` | - | `SERVICE` - Service |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.subscriptions.service` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:settings.subscriptions.service` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:settings.subscriptions.service` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Key request names `keyRequestNames` | set | - | Required |