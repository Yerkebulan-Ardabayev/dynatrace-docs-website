---
title: Settings API - Microsoft Defender for Cloud schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-microsoft-defender-cloud-connections
---

# Settings API - Microsoft Defender for Cloud schema table

# Settings API - Microsoft Defender for Cloud schema table

* Published Jun 30, 2025

### Microsoft Defender for Cloud (`app:dynatrace.microsoft.defender.cloud:connections)`

Ingest Microsoft Defender for Cloud vulnerability findings and scan events.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.microsoft.defender.cloud:connections` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.microsoft.defender.cloud:connections` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | Provide a unique display name for your connection. | Required |
| Use trused service? `use_trusted_service` | enum | Export as a trusted service? The element has these enums * `true` * `false` | Required |
| Ingest token ID `ingest_token_id` | text | ID of the Grail ingest token to be used in this connection | Optional |