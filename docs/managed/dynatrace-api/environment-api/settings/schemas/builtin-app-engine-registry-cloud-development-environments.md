---
title: Settings API - Cloud Development Environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-app-engine-registry-cloud-development-environments
---

# Settings API - Cloud Development Environments schema table

# Settings API - Cloud Development Environments schema table

* Published Nov 04, 2024

### Cloud Development Environments (`builtin:app-engine-registry.cloud-development-environments)`

In order to enable Cloud Development Environment (CDE) for application development, the respective domains need to be configured here.

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:app-engine-registry.cloud-development-environments` | * `group:dt-apps-development` * `group:preferences` | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:app-engine-registry.cloud-development-environments` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Cloud Development Environments `cloudDevelopmentEnvironments` | set | The URL to allow app development from. E.g. `https://*.my-company.my-cde-provider.com`. | Required |