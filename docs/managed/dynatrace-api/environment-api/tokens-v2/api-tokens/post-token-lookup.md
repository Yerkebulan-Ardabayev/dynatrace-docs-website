---
title: Access tokens API - POST token lookup
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token-lookup
scraped: 2026-05-12T12:01:13.018046
---

# Access tokens API - POST token lookup

# Access tokens API - POST token lookup

* Reference
* Published Mar 15, 2021

Gets metadata of the API token by its secret.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/lookup` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/lookup` |

## Authentication

To execute this request, you need an access token with **any** scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ApiTokenSecret](#openapi-definition-ApiTokenSecret) | The JSON body of the request. Contains the required token. | body | Required |

### Request body objects

#### The `ApiTokenSecret` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| token | string | The API token. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"token": "dt0c01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApiToken](#openapi-definition-ApiToken) | Success |
| **404** | - | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ApiToken` object

Metadata of an API token.

| Element | Type | Description |
| --- | --- | --- |
| additionalMetadata | object | Contains additional properties for specific kinds of token. Examples:  * A `dashboardId` property for dashboard sharing tokens. * A `reportId` property for report sharing tokens |
| creationDate | string | Token creation date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| enabled | boolean | The token is enabled (`true`) or disabled (`false`). |
| expirationDate | string | Token expiration date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`).  If not set, the token never expires. |
| id | string | The ID of the token, consisting of prefix and public part of the token. |
| lastUsedDate | string | Token last used date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`) |
| lastUsedIpAddress | string | Token last used IP address. |
| modifiedDate | string | Token last modified date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). Updating scopes or name counts as modification, enabling or disabling a token does not. |
| name | string | The name of the token. |
| owner | string | The owner of the token. |
| personalAccessToken | boolean | The token is a [personal access tokenï»¿](https://dt-url.net/wm03sop) (`true`) or an API token (`false`). |
| scopes | string[] | A list of scopes assigned to the token. The element can hold these values * `ActiveGateCertManagement` * `AdvancedSyntheticIntegration` * `CaptureRequestData` * `DTAQLAccess` * `DataExport` * `DataImport` * `DataPrivacy` * `Davis` * `DiagnosticExport` * `DssFileManagement` * `ExternalSyntheticIntegration` * `InstallerDownload` * `LogExport` * `MemoryDump` * `Mobile` * `PluginUpload` * `ReadConfig` * `ReadSyntheticData` * `RestRequestForwarding` * `RumBrowserExtension` * `RumJavaScriptTagManagement` * `SupportAlert` * `TenantTokenManagement` * `UserSessionAnonymization` * `ViewDashboard` * `ViewReport` * `WriteConfig` * `WriteSyntheticData` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `activeGates.read` * `activeGates.write` * `adaptiveTrafficManagement.read` * `agentTokenManagement.read` * `apiTokens.read` * `apiTokens.write` * `attacks.read` * `attacks.write` * `auditLogs.read` * `bizevents.ingest` * `credentialVault.read` * `credentialVault.write` * `entities.read` * `entities.write` * `events.ingest` * `events.read` * `extensionConfigurationActions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionDiscoveryJmx.read` * `extensionEnvironment.read` * `extensionEnvironment.write` * `extensions.read` * `extensions.write` * `geographicRegions.read` * `hub.install` * `hub.read` * `hub.write` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `logs.ingest` * `logs.read` * `metrics.ingest` * `metrics.read` * `metrics.write` * `networkZones.read` * `networkZones.write` * `oneAgents.read` * `oneAgents.write` * `openTelemetryTrace.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `problems.read` * `problems.write` * `releases.read` * `rumCookieNames.read` * `rumManualInsertionTags.read` * `securityProblems.read` * `securityProblems.write` * `settings.read` * `settings.write` * `slo.read` * `slo.write` * `syntheticExecutions.read` * `syntheticExecutions.write` * `syntheticLocations.read` * `syntheticLocations.write` * `tenantTokenRotation.write` * `traces.lookup` * `unifiedAnalysis.read` |

### Response body JSON models

```
{



"additionalMetadata": {



"dashboardId": "82402bab-7370-4359-924d-88ed13c8919a"



},



"creationDate": "2020-11-05T08:15:30.144Z",



"enabled": true,



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"lastUsedDate": "2020-11-12T08:15:30.144Z",



"lastUsedIpAddress": "34.197.2.44",



"modifiedDate": "2020-11-12T08:15:30.144Z",



"name": "myToken",



"owner": "john.smith",



"personalAccessToken": true,



"scopes": [



"metrics.read"



]



}
```

## Related topics

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")