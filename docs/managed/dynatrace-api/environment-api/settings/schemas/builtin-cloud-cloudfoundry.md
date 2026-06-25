---
title: Settings API - Cloud Foundry schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-cloud-cloudfoundry
scraped: 2026-05-12T11:45:38.821268
---

# Settings API - Cloud Foundry schema table

# Settings API - Cloud Foundry schema table

* Published Dec 05, 2023

### Cloud Foundry (`builtin:cloud.cloudfoundry)`

Use this page to connect your Cloud Foundry foundation to Dynatrace for monitoring. Please have your Cloud Foundry API target URL, your authentication endpoint and your Cloud Foundry username and password ready.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:cloud.cloudfoundry` | * `group:cloud-and-virtualization` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:cloud.cloudfoundry` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Enabled `enabled` | boolean | - | Required |
| Name this connection `label` | text | - | Required |
| Cloud Foundry API Target `apiUrl` | text | - | Required |
| Cloud Foundry Authentication Endpoint `loginUrl` | text | - | Required |
| Cloud Foundry Username `username` | text | - | Required |
| Cloud Foundry Password `password` | secret | - | Required |
| ActiveGate group `activeGateGroup` | text | - | Optional |