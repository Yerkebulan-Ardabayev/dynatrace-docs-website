---
title: Access tokens API - GET all tokens
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/tokens-v2/api-tokens/get-all
scraped: 2026-05-12T12:01:08.958713
---

# Access tokens API - GET all tokens

# Access tokens API - GET all tokens

* Reference
* Published Mar 15, 2021

Lists all API tokens available in your environment.

You can limit the output by using the pagination:

1. Specify the number of results per page in the **pageSize** query parameter.
2. Then use the cursor from the **nextPageKey** field of the previous response in the **nextPageKey** query parameter to obtain subsequent pages.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/apiTokens` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/apiTokens` |

## Authentication

To execute this request, you need an access token with `apiTokens.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of API tokens in a single response payload.  The maximal allowed page size is 10000 and the minimal allowed page size is 100.  If not set, 200 is used. | query | Optional |
| apiTokenSelector | string | Filters the resulting sets of tokens. Only tokens matching the specified criteria are included into response.  You can set one or more of the following criteria:  * Owner: `owner("value")`. The user that owns the token. Case-sensitive. * Personal access token: `personalAccessToken(false)`. Set to `true` to include only personal access tokens or to `false` to include only API tokens. * Token scope: `scope("scope1","scope2")`. If several values are specified, the **OR** logic applies.  To set multiple criteria, separate them with commas (`,`). Only results matching **all** criteria are included into response. | query | Optional |
| fields | string | Specifies the fields to be included in the response.  The following fields are included by default:  * `id` * `name` * `enabled` * `owner` * `creationDate`  To remove fields from the response, specify them with the minus (`-`) operator as a comma-separated list (for example, `-creationDate,-owner`).  You can include additional fields:  * `personalAccessToken` * `expirationDate` * `lastUsedDate` * `lastUsedIpAddress` * `modifiedDate` * `scopes` * `additionalMetadata`  To add fields to the response, specify them with the plus (`+`) operator as a comma-separated list (for example, `+expirationDate,+scopes`). You can combine adding and removing of fields (for example, `+scopes,-creationDate`).  Alternatively, you can define the desired set of fields in the response. Specify the required fields as a comma-separated list, without operators (for example, `creationDate,expirationDate,owner`). The ID is always included in the response.  The **fields** string must be URL-encoded. | query | Optional |
| from | string | Filters tokens based on the last usage time. The start of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years | query | Optional |
| to | string | Filters tokens based on the last usage time. The end of the requested timeframe.  You can use one of the following formats:  * Timestamp in UTC milliseconds. * Human-readable format of `2021-01-25T05:57:01.123+01:00`. If no time zone is specified, UTC is used. You can use a space character instead of the `T`. Seconds and fractions of a second are optional. * Relative timeframe, back from now. The format is `now-NU/A`, where `N` is the amount of time, `U` is the unit of time, and `A` is an alignment. The alignment rounds all the smaller values to the nearest zero in the past. For example, `now-1y/w` is one year back, aligned by a week.   You can also specify relative timeframe without an alignment: `now-NU`.   Supported time units for the relative timeframe are: + `m`: minutes   + `h`: hours   + `d`: days   + `w`: weeks   + `M`: months   + `y`: years  If not set, the current timestamp is used. | query | Optional |
| sort | string | The sort order of the token list.  You can sort by the following properties with a sign prefix for the sort order:  * `name`: token name (`+` a...z or `-` z...a) * `lastUsedDate` last used (`+` never used tokens first `-` most recently used tokens first) * `creationDate` (`+` oldest tokens first `-` newest tokens first) * `expirationDate` (`+` tokens that expire soon first `-` unlimited tokens first) * `modifiedDate` last modified (`+` never modified tokens first `-` most recently modified tokens first)  If no prefix is set, + is used.  If not set, tokens are sorted by creation date with newest first. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ApiTokenList](#openapi-definition-ApiTokenList) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ApiTokenList` object

A list of API tokens.

| Element | Type | Description |
| --- | --- | --- |
| apiTokens | [ApiToken[]](#openapi-definition-ApiToken) | A list of API tokens. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

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



"apiTokens": {



"additionalMetadata": {



"dashboardId": "82402bab-7370-4359-924d-88ed13c8919a"



},



"creationDate": "2020-11-05T08:15:30.144Z",



"disabled": "false",



"expirationDate": "2020-11-12T08:15:30.144Z",



"id": "dt0c01.ST2EY72KQINMH574WMNVI7YN",



"lastUsedDate": "2020-11-12T08:15:30.144Z",



"lastUsedIpAddress": "34.197.2.44",



"name": "tokenName",



"owner": "john.smith",



"personalAccessToken": "true",



"scopes": [



"metrics.read"



]



},



"pageSize": "1",



"totalCount": "1"



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