---
title: Settings API - Monitor name schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-synthetic-multiprotocol-name
scraped: 2026-05-12T11:48:12.997120
---

# Settings API - Monitor name schema table

# Settings API - Monitor name schema table

* Published Jul 31, 2024

### Monitor name (`builtin:synthetic.multiprotocol.name)`

Define the display name of your network availability monitor

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:synthetic.multiprotocol.name` | * `group:synthetic.multiprotocol` | `MULTIPROTOCOL_MONITOR` - Network availability monitor |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.name` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:synthetic.multiprotocol.name` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:synthetic.multiprotocol.name` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor name `name` | text | - | Required |