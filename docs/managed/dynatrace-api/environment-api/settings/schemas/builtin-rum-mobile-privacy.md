---
title: Settings API - Privacy settings schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-rum-mobile-privacy
scraped: 2026-05-12T11:48:59.353844
---

# Settings API - Privacy settings schema table

# Settings API - Privacy settings schema table

* Published Dec 05, 2023

### Privacy settings (`builtin:rum.mobile.privacy)`

Enable user opt-in mode to allow your users to decide what types of data they are willing to share. For details, see [Opt-in modeï»¿](https://dt-url.net/9602z8z)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:rum.mobile.privacy` | * `group:rum-general` * `group:privacy-settings` | `MOBILE_APPLICATION` - Mobile App |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.privacy` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:rum.mobile.privacy` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:rum.mobile.privacy` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enable user opt-in mode `optInModeEnabled` | boolean | - | Required |