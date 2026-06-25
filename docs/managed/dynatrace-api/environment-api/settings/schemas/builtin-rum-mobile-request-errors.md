---
title: Settings API - Request errors schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-request-errors
scraped: 2026-05-12T11:44:19.073340
---

# Settings API - Request errors schema table

# Settings API - Request errors schema table

* Published Dec 05, 2023

### Request errors (`builtin:rum.mobile.request-errors)`

Create exclusion rules to define which HTTP response codes should not be treated as errors. By default, Dynatrace considers all 4xx and 5xx response status codes to be web request errors.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.request-errors` | - | `MOBILE_APPLICATION` - Mobile App  `CUSTOM_APPLICATION` - Custom Application |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.request-errors` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| `errorRules` | Set<[RequestErrorRule](#RequestErrorRule)> | - | Required |

##### The `RequestErrorRule` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Exclude response codes `errorCodes` | text | - | Required |