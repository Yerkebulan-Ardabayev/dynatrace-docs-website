---
title: Settings API - Amazon GuardDuty schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-amazon-guardduty-connections
---

# Settings API - Amazon GuardDuty schema table

# Settings API - Amazon GuardDuty schema table

* Published Sep 25, 2025

### Amazon GuardDuty (`app:dynatrace.amazon.guardduty:connections)`

Ingest Amazon GuardDuty security findings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.amazon.guardduty:connections` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.amazon.guardduty:connections` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Connection name `name` | text | Provide a unique display name for your connection. | Required |
| Ingest token ID `ingest_token_id` | text | ID of the Grail ingest token to be used in this connection | Optional |