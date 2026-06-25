---
title: Settings API - Extension Execution Controller schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-eec-remote
scraped: 2026-05-12T11:40:40.434650
---

# Settings API - Extension Execution Controller schema table

# Settings API - Extension Execution Controller schema table

* Published Dec 05, 2023

### Extension Execution Controller (`builtin:eec.remote)`

Extension Execution Controller configuration for ActiveGate deployment

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:eec.remote` | - | `ENVIRONMENT_ACTIVE_GATE` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.remote` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:eec.remote` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:eec.remote` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Performance profile `performanceProfile` | enum | Select performance profile for Extension Execution Controller [Documentationï»¿](https://www.dynatrace.com/support/help/shortlink/extensions-concepts#resource-consumption "More about performance profiles") The element has these enums * `DEFAULT` * `HIGH` * `DEDICATED` | Required |