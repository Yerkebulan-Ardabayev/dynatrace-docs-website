---
title: Access tokens API - POST a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/post-token
---

# Access tokens API - POST a token

# Access tokens API - POST a token

* Reference
* Published Mar 15, 2021

Creates a new API token.

The token will be owned by the user who owns the token used to authenticate the call.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Authentication

To execute this request, you need an access token with `apiTokens.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ApiTokenCreate](#openapi-definition-ApiTokenCreate) | The JSON body of the request. Contains parameters of the new API token. | body | Required |

### Request body objects

#### The `ApiTokenCreate` object

Parameters of a new API token.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| expirationDate | string | The expiration date of the token.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the token never expires. Ensure that the expiration date is not set in the past. | Optional |
| name | string | The name of the token. | Required |
| personalAccessToken | boolean | The token is a personal access token (`true`) or an API token (`false`).  Personal access tokens are tied to the permissions of their owner. | Optional |
| scopes | string[] | A list of the scopes to be assigned to the token.  * `InstallerDownload`: PaaS integration - Installer download. * `DataExport`: Access problem and event feed, metrics, and topology. * `PluginUpload`: Upload Extension. * `SupportAlert`: PaaS integration - Support alert. * `AdvancedSyntheticIntegration`: Dynatrace module integration - Synthetic Classic. * `ExternalSyntheticIntegration`: Create and read synthetic monitors, locations, and nodes. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: Read logs. * `ReadConfig`: Read configuration. * `WriteConfig`: Write configuration. * `DTAQLAccess`: User sessions. * `UserSessionAnonymization`: Anonymize user session data for data privacy reasons. * `DataPrivacy`: Change data privacy settings. * `CaptureRequestData`: Capture request data. * `Davis`: Dynatrace module integration - Davis. * `DssFileManagement`: Mobile symbolication file management. * `RumJavaScriptTagManagement`: Real user monitoring JavaScript tag management. * `TenantTokenManagement`: Token management. * `ActiveGateCertManagement`: ActiveGate certificate management. * `RestRequestForwarding`: Fetch data from a remote environment. * `ReadSyntheticData`: Read synthetic monitors, locations, and nodes. * `DataImport`: Data ingest, e.g.: metrics and events. * `syntheticExecutions.write`: Write synthetic monitor executions. * `syntheticExecutions.read`: Read synthetic monitor execution results. * `auditLogs.read`: Read audit logs. * `metrics.read`: Read metrics. * `metrics.write`: Write metrics. * `entities.read`: Read entities. * `entities.write`: Write entities. * `problems.read`: Read problems. * `problems.write`: Write problems. * `events.read`: Read events. * `events.ingest`: Ingest events. * `openpipeline.events`: OpenPipeline - Ingest Events (Built-in). * `openpipeline.events.custom`: OpenPipeline - Ingest Events (Custom). * `openpipeline.events_security`: OpenPipeline - Ingest Security Events (Built-in). * `openpipeline.events_security.custom`: OpenPipeline - Ingest Security Events (Custom). * `openpipeline.events_sdlc`: OpenPipeline - Ingest Software Development Lifecycle Events (Built-in). * `openpipeline.events_sdlc.custom`: OpenPipeline - Ingest Software Development Lifecycle Events (Custom). * `bizevents.ingest`: Ingest bizevents. * `networkZones.read`: Read network zones. * `networkZones.write`: Write network zones. * `activeGates.read`: Read ActiveGates. * `activeGates.write`: Write ActiveGates. * `activeGateTokenManagement.read`: Read ActiveGate tokens. * `activeGateTokenManagement.create`: Create ActiveGate tokens. * `activeGateTokenManagement.write`: Write ActiveGate tokens. * `agentTokenManagement.read`: Read Agent tokens. * `credentialVault.read`: Read credential vault entries. * `credentialVault.write`: Write credential vault entries. * `extensions.read`: Read extensions. * `extensions.write`: Write extensions. * `extensionConfigurations.read`: Read extension monitoring configurations. * `extensionConfigurations.write`: Write extension monitoring configurations. * `extensionEnvironment.read`: Read extension environment configurations. * `extensionEnvironment.write`: Write extension environment configurations. * `metrics.ingest`: Ingest metrics. * `attacks.read`: Read attacks. * `attacks.write`: Write Application Protection settings. * `securityProblems.read`: Read security problems. * `securityProblems.write`: Write security problems. * `syntheticLocations.read`: Read synthetic locations. * `syntheticLocations.write`: Write synthetic locations. * `settings.read`: Read settings. * `settings.write`: Write settings. * `tenantTokenRotation.write`: Tenant token rotation. * `slo.read`: Read SLO. * `slo.write`: Write SLO. * `releases.read`: Read releases. * `apiTokens.read`: Read API tokens. * `apiTokens.write`: Write API tokens. * `openTelemetryTrace.ingest`: Ingest OpenTelemetry traces. * `logs.read`: Read logs. * `logs.ingest`: Ingest logs. * `geographicRegions.read`: Read Geographic regions. * `oneAgents.read`: Read OneAgents. * `oneAgents.write`: Write OneAgents. * `traces.lookup`: Look up a single trace. * `unifiedAnalysis.read`: Read Unified Analysis page. * `hub.read`: Read Hub related data. * `hub.write`: Manage metadata of Hub items. * `hub.install`: Install and update Hub items. * `javaScriptMappingFiles.read`: Read JavaScript mapping files. * `javaScriptMappingFiles.write`: Write JavaScript mapping files. * `extensionConfigurationActions.write`: Actions for extension monitoring configurations. * `rumCookieNames.read`: Read RUM cookie names. * `adaptiveTrafficManagement.read`: Read sampling configuration for Adaptive Traffic Management. * `rumManualInsertionTags.read`: Read RUM manual insertion tags. * `extensionDiscoveryJmx.read`: Read discovered JMX metrics via extensions. * `extensionDiscoveryPmi.read`: Read discovered PMI metrics via extensions. The element can hold these values * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"expirationDate": "now+14d",



"name": "tokenName",



"personalAccessToken": false,



"scopes": [



"metrics.read"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [ApiTokenCreated](#openapi-definition-ApiTokenCreated) | Success. The token has been created. The body of the response contains the token secret. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ApiTokenCreated` object

The newly created token.

| Element | Type | Description |
| --- | --- | --- |
| expirationDate | string | The token expiration date in ISO 8601 format (`yyyy-MM-dd'T'HH:mm:ss.SSS'Z'`). |
| id | string | The ID of the token, consisting of prefix and public part of the token. |
| token | string | The secret of the token. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
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



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"token": "dt0c01.ST2EY72KQINMH574WMNVI7YN.G3DFPBEJYMODIDAEX454M7YWBUVEFOWKPRVMWFASS64NFH52PX6BNDVFFM572RZM"



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

## Related topics

* [Access tokens](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/access-tokens "Learn the concept of an access token and its scopes.")