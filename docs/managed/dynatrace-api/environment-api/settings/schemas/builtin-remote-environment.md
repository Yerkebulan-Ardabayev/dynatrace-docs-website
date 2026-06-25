---
title: Settings API - Remote environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-remote-environment
scraped: 2026-05-12T11:45:35.130966
---

# Settings API - Remote environments schema table

# Settings API - Remote environments schema table

* Published Dec 05, 2023

### Remote environments (`builtin:remote.environment)`

Configure connections to other Dynatrace environments for cross-environment capabilities (e.g. dashboards)

For help on remote environments, see [Remote environment API documentationï»¿](https://dt-url.net/lc5n0p4z)

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:remote.environment` | * `group:integration.external` * `group:integration` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:remote.environment` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:remote.environment` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:remote.environment` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | - | Required |
| Remote environment URI `uri` | text | Specify the full URI to the remote environment. Your local environment will have to be able to connect this URI on a network level. | Required |
| Network scope `networkScope` | enum | * External: The remote environment is located in an another network. * Internal: The remote environment is located in the same network. * Cluster: The remote environment is located in the same cluster.  Dynatrace SaaS can only use External. The element has these enums * `EXTERNAL` * `INTERNAL` * `CLUSTER` | Required |
| Token `token` | secret | Provide a valid token created on the remote environment. | Required |