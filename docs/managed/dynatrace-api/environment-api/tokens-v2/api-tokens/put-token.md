---
title: Access tokens API - PUT a token
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/put-token
---

# Access tokens API - PUT a token

# Access tokens API - PUT a token

* Reference
* Published Mar 15, 2021

Updates the specified API token. You can:

* Change the token name and scope.
* Revoke the token. A revoked token still exists in the environment, but it can't be used.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens/{id}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens/{id}` |

## Authentication

To execute this request, you need an access token with `apiTokens.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the token to be updated.  You can't disable the token you're using for authentication of the request. | path | Required |
| body | [ApiTokenUpdate](#openapi-definition-ApiTokenUpdate) | The JSON body of the request. Contains updated parameters of the API token. | body | Required |

### Request body objects

#### The `ApiTokenUpdate` object

The update of the API token.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| enabled | boolean | The token is enabled (`true`) or disabled (`false`) | Optional |
| name | string | The name of the token. | Optional |
| scopes | string[] | The list of scopes assigned to the token.  Apart from the new scopes, you need to submit the existing scopes you want to keep, too. Any existing scope, missing in the payload, is removed.  * `InstallerDownload`: PaaS integration - Installer download. * `DataExport`: Access problem and event feed, metrics, and topology. * `PluginUpload`: Upload Extension. * `SupportAlert`: PaaS integration - Support alert. * `AdvancedSyntheticIntegration`: Dynatrace module integration - Synthetic Classic. * `ExternalSyntheticIntegration`: Create and read synthetic monitors, locations, and nodes. * `RumBrowserExtension`: RUM Browser Extension. * `LogExport`: Read logs. * `ReadConfig`: Read configuration. * `WriteConfig`: Write configuration. * `DTAQLAccess`: User sessions. * `UserSessionAnonymization`: Anonymize user session data for data privacy reasons. * `DataPrivacy`: Change data privacy settings. * `CaptureRequestData`: Capture request data. * `Davis`: Dynatrace module integration - Davis. * `DssFileManagement`: Mobile symbolication file management. * `RumJavaScriptTagManagement`: Real user monitoring JavaScript tag management. * `TenantTokenManagement`: Token management. * `ActiveGateCertManagement`: ActiveGate certificate management. * `RestRequestForwarding`: Fetch data from a remote environment. * `ReadSyntheticData`: Read synthetic monitors, locations, and nodes. * `DataImport`: Data ingest, e.g.: metrics and events. * `syntheticExecutions.write`: Write synthetic monitor executions. * `syntheticExecutions.read`: Read synthetic monitor execution results. * `auditLogs.read`: Read audit logs. * `metrics.read`: Read metrics. * `metrics.write`: Write metrics. * `entities.read`: Read entities. * `entities.write`: Write entities. * `problems.read`: Read problems. * `problems.write`: Write problems. * `events.read`: Read events. * `events.ingest`: Ingest events. * `openpipeline.events`: OpenPipeline - Ingest Events (Built-in). * `openpipeline.events.custom`: OpenPipeline - Ingest Events (Custom). * `openpipeline.events_security`: OpenPipeline - Ingest Security Events (Built-in). * `openpipeline.events_security.custom`: OpenPipeline - Ingest Security Events (Custom). * `openpipeline.events_sdlc`: OpenPipeline - Ingest Software Development Lifecycle Events (Built-in). * `openpipeline.events_sdlc.custom`: OpenPipeline - Ingest Software Development Lifecycle Events (Custom). * `openpipeline.events_smartscape`: OpenPipeline - Ingest Smartscape Events (Built-in). * `bizevents.ingest`: Ingest bizevents. * `networkZones.read`: Read network zones. * `networkZones.write`: Write network zones. * `activeGates.read`: Read ActiveGates. * `activeGates.write`: Write ActiveGates. * `activeGateTokenManagement.read`: Read ActiveGate tokens. * `activeGateTokenManagement.create`: Create ActiveGate tokens. * `activeGateTokenManagement.write`: Write ActiveGate tokens. * `agentTokenManagement.read`: Read Agent tokens. * `credentialVault.read`: Read credential vault entries. * `credentialVault.write`: Write credential vault entries. * `extensions.read`: Read extensions. * `extensions.write`: Write extensions. * `extensionConfigurations.read`: Read extension monitoring configurations. * `extensionConfigurations.write`: Write extension monitoring configurations. * `extensionEnvironment.read`: Read extension environment configurations. * `extensionEnvironment.write`: Write extension environment configurations. * `metrics.ingest`: Ingest metrics. * `attacks.read`: Read attacks. * `attacks.write`: Write Application Protection settings. * `securityProblems.read`: Read security problems. * `securityProblems.write`: Write security problems. * `syntheticLocations.read`: Read synthetic locations. * `syntheticLocations.write`: Write synthetic locations. * `settings.read`: Read settings. * `settings.write`: Write settings. * `tenantTokenRotation.write`: Tenant token rotation. * `slo.read`: Read SLO. * `slo.write`: Write SLO. * `releases.read`: Read releases. * `apiTokens.read`: Read API tokens. * `apiTokens.write`: Write API tokens. * `openTelemetryTrace.ingest`: Ingest OpenTelemetry traces. * `logs.read`: Read logs. * `logs.ingest`: Ingest logs. * `geographicRegions.read`: Read Geographic regions. * `oneAgents.read`: Read OneAgents. * `oneAgents.write`: Write OneAgents. * `traces.lookup`: Look up a single trace. * `unifiedAnalysis.read`: Read Unified Analysis page. * `hub.read`: Read Hub related data. * `hub.write`: Manage metadata of Hub items. * `hub.install`: Install and update Hub items. * `javaScriptMappingFiles.read`: Read JavaScript mapping files. * `javaScriptMappingFiles.write`: Write JavaScript mapping files. * `extensionConfigurationActions.write`: Actions for extension monitoring configurations. * `rumCookieNames.read`: Read RUM cookie names. * `adaptiveTrafficManagement.read`: Read sampling configuration for Adaptive Traffic Management. * `rumManualInsertionTags.read`: Read RUM manual insertion tags. * `extensionDiscoveryJmx.read`: Read discovered JMX metrics via extensions. * `extensionDiscoveryPmi.read`: Read discovered PMI metrics via extensions. The element can hold these values * `InstallerDownload` * `DataExport` * `PluginUpload` * `SupportAlert` * `AdvancedSyntheticIntegration` * `ExternalSyntheticIntegration` * `RumBrowserExtension` * `LogExport` * `ReadConfig` * `WriteConfig` * `DTAQLAccess` * `UserSessionAnonymization` * `DataPrivacy` * `CaptureRequestData` * `Davis` * `DssFileManagement` * `RumJavaScriptTagManagement` * `TenantTokenManagement` * `ActiveGateCertManagement` * `RestRequestForwarding` * `ReadSyntheticData` * `DataImport` * `syntheticExecutions.write` * `syntheticExecutions.read` * `auditLogs.read` * `metrics.read` * `metrics.write` * `entities.read` * `entities.write` * `problems.read` * `problems.write` * `events.read` * `events.ingest` * `openpipeline.events` * `openpipeline.events.custom` * `openpipeline.events_security` * `openpipeline.events_security.custom` * `openpipeline.events_sdlc` * `openpipeline.events_sdlc.custom` * `openpipeline.events_smartscape` * `bizevents.ingest` * `networkZones.read` * `networkZones.write` * `activeGates.read` * `activeGates.write` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `agentTokenManagement.read` * `credentialVault.read` * `credentialVault.write` * `extensions.read` * `extensions.write` * `extensionConfigurations.read` * `extensionConfigurations.write` * `extensionEnvironment.read` * `extensionEnvironment.write` * `metrics.ingest` * `attacks.read` * `attacks.write` * `securityProblems.read` * `securityProblems.write` * `syntheticLocations.read` * `syntheticLocations.write` * `settings.read` * `settings.write` * `tenantTokenRotation.write` * `slo.read` * `slo.write` * `releases.read` * `apiTokens.read` * `apiTokens.write` * `openTelemetryTrace.ingest` * `logs.read` * `logs.ingest` * `geographicRegions.read` * `oneAgents.read` * `oneAgents.write` * `traces.lookup` * `unifiedAnalysis.read` * `hub.read` * `hub.write` * `hub.install` * `javaScriptMappingFiles.read` * `javaScriptMappingFiles.write` * `extensionConfigurationActions.write` * `rumCookieNames.read` * `adaptiveTrafficManagement.read` * `rumManualInsertionTags.read` * `extensionDiscoveryJmx.read` * `extensionDiscoveryPmi.read` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"enabled": true,



"name": "myToken",



"scopes": [



"InstallerDownload"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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