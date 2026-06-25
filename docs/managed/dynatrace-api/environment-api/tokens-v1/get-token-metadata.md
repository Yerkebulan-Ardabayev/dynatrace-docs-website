---
title: Tokens API v1 - GET token metadata
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v1/get-token-metadata
scraped: 2026-05-12T12:11:23.787138
---

# Tokens API v1 - GET token metadata

# Tokens API v1 - GET token metadata

* Reference
* Updated on May 17, 2022

This API is deprecated. Use the [Access tokens API](/managed/dynatrace-api/environment-api/tokens-v2/api-tokens "Manage Dynatrace API authentication tokens.") instead.

Lists metadata of a Dynatrace API authentication token by the ID of the token. The token itself is **not** exposed.

Alternatively, you can retrieve metadata by submitting the token itself with the [POST token metadata](/managed/dynatrace-api/environment-api/tokens-v1/post-token-metadata "Learn how to use the Dynatrace API to look up the metadata of a Dynatrace API authentication token.") call.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/tokens/{id}` |

## Authentication

To execute this request, you need an access token with `TenantTokenManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required token. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested token has not been found. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `TokenMetadata` object

Metadata of a token.

| Element | Type | Description |
| --- | --- | --- |
| created | integer | The creation time as a unix timestamp in milliseconds. |
| expires | integer | The expiration time as a unix timestamp in milliseconds. |
| id | string | The ID of the token. |
| lastUse | integer | The unix timestamp in milliseconds when the token was last used. |
| name | string | The name of the token. |
| personalAccessToken | boolean | The token is a [personal access tokenï»¿](https://dt-url.net/wm03sop) (`true`) or an API token (`false`). |
| revoked | boolean | Revocation status of the token. Revoked tokens are disabled. |
| scopes | string[] | A list of scopes assigned to the token. The element can hold these values * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |
| userId | string | The owner of the token. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"created": 1554076800000,



"expires": 1585976400000,



"id": "acbed0c4-4ef1-4303-991f-102510a69322",



"lastUse": 1554354000000,



"name": "myToken",



"personalAccessToken": true,



"revoked": true,



"scopes": [



"DataExport",



"ReadConfig",



"WriteConfig"



],



"userId": "john.smith"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

In this example, the request queries the metadata of the **admin** token, which has the ID of **d5836312-5790-4e80-afcf-09971954c3ea**.

The API token is passed in the **Authorization** header.

The token, as displayed in the Dynatrace interface, has the following settings:

![Dynatrace API authentication token](https://dt-cdn.net/images/token-permissions-1283-6453dccd8a.png)

Dynatrace API authentication token

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/tokens/d5836312-5790-4e80-afcf-09971954c3ea
```

#### Response body

```
{



"id": "d5836312-5790-4e80-afcf-09971954c3ea",



"name": "admin",



"userId": "admin@mysampleenv.com",



"created": "2019-03-13T09:45:40Z",



"lastUse": "2019-04-04T09:13:23Z",



"scopes": [



"ExternalSyntheticIntegration",



"DataPrivacy",



"WriteConfig",



"DssFileManagement",



"LogExport",



"DTAQLAccess",



"ReadConfig",



"CaptureRequestData",



"ReadSyntheticData",



"DataExport",



"UserSessionAnonymization",



"MaintenanceWindows",



"LogImport",



"TenantTokenManagement"



]



}
```

#### Response code

200