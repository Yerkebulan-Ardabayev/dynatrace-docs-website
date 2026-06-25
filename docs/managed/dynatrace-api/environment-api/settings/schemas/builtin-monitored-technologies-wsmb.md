---
title: Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-monitored-technologies-wsmb
scraped: 2026-05-12T11:46:19.086330
---

# Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table

# Settings API - IBM Integration Bus | IBM App Connect Enterprise schema table

* Published Dec 05, 2023

### IBM Integration Bus | IBM App Connect Enterprise (`builtin:monitored-technologies.wsmb)`

By default, IBM Integration Bus | IBM App Connect Enterprise monitoring is enabled on all hosts. If you want to disable IBM Integration Bus | IBM App Connect Enterprise monitoring on selected hosts, disable it on these hosts via their settings.

If you want to enable IBM Integration Bus | IBM App Connect Enterprise monitoring only on selected hosts, disable global IBM Integration Bus | IBM App Connect Enterprise monitoring and enable it on these hosts via their settings.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:monitored-technologies.wsmb` | - | `HOST` - Host  `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:monitored-technologies.wsmb` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Monitor IBM Integration Bus | IBM App Connect Enterprise `enabled` | boolean | - | Required |