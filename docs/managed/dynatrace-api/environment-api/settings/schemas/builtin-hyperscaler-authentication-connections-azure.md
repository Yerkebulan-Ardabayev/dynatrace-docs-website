---
title: Settings API - Connections to Azure environments schema table
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/settings/schemas/builtin-hyperscaler-authentication-connections-azure
scraped: 2026-05-12T11:41:34.393766
---

# Settings API - Connections to Azure environments schema table

# Settings API - Connections to Azure environments schema table

* Published Sep 25, 2025

### Connections to Azure environments (`builtin:hyperscaler-authentication.connections.azure)`

Connections to Azure for Dynatrace integrations

| Schema ID | Schema groups | Scope |
| --- | --- | --- |
| `builtin:hyperscaler-authentication.connections.azure` | - | `environment` |

Retrieve schema via Settings API

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/settings/schemas/builtin:hyperscaler-authentication.connections.azure` |

## Authentication

To execute this request, you need an access token with **Read settings** (`settings.read`) scope. To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Name `name` | text | The name of the connection | Required |
| Connection Type `type` | enum | Azure Authentication mechanism to be used by the connection The element has these enums * `clientSecret` * `federatedIdentityCredential` | Required |
| `clientSecret` | [ClientSecretConfig](#ClientSecretConfig) | - | Required |
| `federatedIdentityCredential` | [FederatedIdentityCredential](#FederatedIdentityCredential) | - | Required |

##### The `ClientSecretConfig` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Directory (tenant) ID `directoryId` | text | Directory (tenant) ID of Microsoft Entra ID | Required |
| Application (client) ID `applicationId` | text | Application (client) ID of your app registered in Microsoft Azure App registrations | Required |
| Client secret `clientSecret` | secret | Client secret of your app registered in Microsoft Azure App registrations | Required |
| Consumers `consumers` | [ConsumersOfClientSecret](#ConsumersOfClientSecret)[] | Dynatrace integrations that can use this connection The element has these enums * `DA` * `SVC:com.dynatrace.da` * `NONE` | Required |

##### The `FederatedIdentityCredential` object

| Property | Type | Description | Required |
| --- | --- | --- | --- |
| Directory (tenant) ID `directoryId` | text | Directory (tenant) ID of Microsoft Entra ID | Optional |
| Application (client) ID `applicationId` | text | Application (client) ID of your app registered in Microsoft Azure App registrations | Optional |
| Consumers `consumers` | [ConsumersOfFederatedIdentityCredential](#ConsumersOfFederatedIdentityCredential)[] | Consumers that can use the connection The element has these enums * `DA` * `SVC:com.dynatrace.da` * `APP:dynatrace.microsoft.azure.connector` * `SVC:com.dynatrace.openpipeline` * `SVC:com.dynatrace.grail` * `SVC:com.dynatrace.bo` * `NONE` | Required |