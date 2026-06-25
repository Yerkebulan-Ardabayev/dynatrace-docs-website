---
title: Settings API - AbuseIPDB Connections schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/app-dynatrace-abuseipdb-connections
scraped: 2026-05-12T11:49:43.777147
---

# Settings API - AbuseIPDB Connections schema table

# Settings API - AbuseIPDB Connections schema table

* Published Aug 04, 2025

### AbuseIPDB Connections (`app:dynatrace.abuseipdb:connections)`

AbuseIPDB Connections

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `app:dynatrace.abuseipdb:connections` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/app:dynatrace.abuseipdb:connections` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Activate connection `enabled` | boolean | Enable or disable the connection | Required |
| Connection name `name` | text | Enter a unique display name. | Required |
| API key `api_key` | secret | Log into AbuseIPDB and create an API key. Paste the key in this field. | Required |