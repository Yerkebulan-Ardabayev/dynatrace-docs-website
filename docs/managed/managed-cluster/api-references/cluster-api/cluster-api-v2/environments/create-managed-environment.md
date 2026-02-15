---
title: "Create a new environment"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/create-managed-environment
updated: 2026-02-09
---

# Create a new environment

# Create a new environment

* Published Mar 09, 2021

This API call creates a new environment.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| createToken | boolean | If true, a token management token with the scopes 'apiTokens.read' and 'apiTokens.write' (for usage with token API v2) and 'TenantTokenManagement' (for usage with token API v1) is created when creating a new environment. This token is then returned in the response body. It can be used within the newly created environment to create other tokens for configuring this environment. | query | Optional |
| body | [Environment](#openapi-definition-Environment) | The JSON body of the request. The body must not provide an ID as it will be automatically assigned by the Dynatrace server. | body | Required |

### Request body objects

#### The `Environment` object

Basic configuration for an environment.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| creationDate | string | The creation date of the environment in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z') | Optional |
| id | string | The ID of the environment. Has to match [a-zA-Z0-9\_-]{1,70} | Optional |
| name | string | The display name of the environment. | Required |
| quotas | [EnvironmentQuotas](#openapi-definition-EnvironmentQuotas) | Environment level consumption and quotas information. Only returned if includeConsumptionInfo or includeUncachedConsumptionInfo param is true. Not available for the DPS licensing model. If skipped when editing via PUT method then already set quotas will remain. | Optional |
| state | string | Indicates whether the environment is enabled or disabled. The default value is ENABLED. The element can hold these values * `DISABLED` * `ENABLED` | Optional |
| storage | [EnvironmentStorage](#openapi-definition-EnvironmentStorage) | Environment level storage usage and limit information. Not returned if includeStorageInfo param is not true. If skipped when editing via PUT method then already set limits will remain. | Optional |
| tags | string[] | A set of tags that are assigned to this environment. Every tag can have a maximum length of 100 characters. | Optional |
| trial | boolean | Specifies whether the environment is a trial environment or a non-trial environment. Creating a trial environment is only possible if your license allows that. The default value is false (non-trial). | Optional |

#### The `EnvironmentQuotas` object

Environment level consumption and quotas information. Only returned if includeConsumptionInfo or includeUncachedConsumptionInfo param is true. Not available for the DPS licensing model. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| customMetrics | [CustomMetricsQuota](#openapi-definition-CustomMetricsQuota) | Custom metrics consumption and quota information on environment level. Not set (and not editable) if Custom metrics is not enabled. Not set (and not editable) if Davis data units is enabled. If skipped when editing via PUT method then already set quota will remain. | Optional |
| davisDataUnits | [DavisDataUnitsQuota](#openapi-definition-DavisDataUnitsQuota) | Davis data units consumption and quota information on environment level. Not set (and not editable) if Davis data units is not enabled. If skipped when editing via PUT method then already set quotas will remain. | Optional |
| demUnits | [DemUnitsQuota](#openapi-definition-DemUnitsQuota) | DEM units consumption and quota information on environment level. Not set (and not editable) if DEM units is not enabled. If skipped when editing via PUT method then already set quotas will remain. | Optional |
| hostUnits | [HostUnitQuota](#openapi-definition-HostUnitQuota) | Host units consumption and quota information on environment level. If skipped when editing via PUT method then already set quota will remain. | Optional |
| logMonitoring | [LogMonitoringQuota](#openapi-definition-LogMonitoringQuota) | Log monitoring consumption and quota information on environment level. Not set (and not editable) if Log monitoring is not enabled. Not set (and not editable) if Log monitoring is migrated to Davis data on license level. If skipped when editing via PUT method then already set quotas will remain. | Optional |
| sessionProperties | [SessionPropertiesQuota](#openapi-definition-SessionPropertiesQuota) | User session properties consumption information on environment level. | Optional |
| syntheticMonitors | [SyntheticQuota](#openapi-definition-SyntheticQuota) | Synthetic monitors consumption and quota information on environment level. Not set (and not editable) if neither Synthetic nor DEM units is enabled. If skipped when editing via PUT method then already set quotas will remain. | Optional |
| userSessions | [UserSessionsQuota](#openapi-definition-UserSessionsQuota) | User sessions consumption and quota information on environment level. If skipped when editing via PUT method then already set quotas will remain. | Optional |

#### The `CustomMetricsQuota` object

Custom metrics consumption and quota information on environment level. Not set (and not editable) if Custom metrics is not enabled. Not set (and not editable) if Davis data units is enabled. If skipped when editing via PUT method then already set quota will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentUsage | number | Current environment usage. | Optional |
| maxLimit | integer | Concurrent environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `DavisDataUnitsQuota` object

Davis data units consumption and quota information on environment level. Not set (and not editable) if Davis data units is not enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. | Optional |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. | Optional |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `DemUnitsQuota` object

DEM units consumption and quota information on environment level. Not set (and not editable) if DEM units is not enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. | Optional |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. | Optional |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `HostUnitQuota` object

Host units consumption and quota information on environment level. If skipped when editing via PUT method then already set quota will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentUsage | number | Current environment usage. | Optional |
| maxLimit | integer | Concurrent environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `LogMonitoringQuota` object

Log monitoring consumption and quota information on environment level. Not set (and not editable) if Log monitoring is not enabled. Not set (and not editable) if Log monitoring is migrated to Davis data on license level. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. | Optional |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. | Optional |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `SessionPropertiesQuota` object

User session properties consumption information on environment level.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. | Optional |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. | Optional |

#### The `SyntheticQuota` object

Synthetic monitors consumption and quota information on environment level. Not set (and not editable) if neither Synthetic nor DEM units is enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. | Optional |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. | Optional |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `UserSessionsQuota` object

User sessions consumption and quota information on environment level. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| consumedMobileSessionsThisMonth | number | Monthly Mobile user sessions environment consumption. Resets each calendar month. | Optional |
| consumedMobileSessionsThisYear | number | Yearly Mobile user sessions environment consumption. Resets each year on license creation date anniversary. | Optional |
| consumedUserSessionsWithMobileSessionReplayThisMonth | number | Monthly Mobile user sessions with replay environment consumption. Resets each calendar month. | Optional |
| consumedUserSessionsWithMobileSessionReplayThisYear | number | Yearly Mobile user sessions with replay environment consumption. Resets each year on license creation date anniversary. | Optional |
| consumedUserSessionsWithWebSessionReplayThisMonth | number | Monthly Web user sessions with replay environment consumption. Resets each calendar month. | Optional |
| consumedUserSessionsWithWebSessionReplayThisYear | number | Yearly Web user sessions with replay environment consumption. Resets each year on license creation date anniversary. | Optional |
| totalAnnualLimit | integer | Annual total User sessions environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |
| totalConsumedThisMonth | number | Monthly total User sessions environment consumption. Resets each calendar month. | Optional |
| totalConsumedThisYear | number | Yearly total User sessions environment consumption. Resets each year on license creation date anniversary. | Optional |
| totalMonthlyLimit | integer | Monthly total User sessions environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. | Optional |

#### The `EnvironmentStorage` object

Environment level storage usage and limit information. Not returned if includeStorageInfo param is not true. If skipped when editing via PUT method then already set limits will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| realUserMonitoringRetention | [RealUserMonitoringRetention](#openapi-definition-RealUserMonitoringRetention) | Real user monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. | Optional |
| rumNonAggregatedDataRetention | [RumNonAggregatedDataRetention](#openapi-definition-RumNonAggregatedDataRetention) | Non-aggregated RUM data retention settings on environment level. Can be set to any value from 1 to 365 days. If skipped when editing via PUT method then already set limit will remain. | Optional |
| serviceCodeLevelRetention | [ServiceCodeLevelRetention](#openapi-definition-ServiceCodeLevelRetention) | Service code level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain. | Optional |
| serviceRequestLevelRetention | [ServiceRequestLevelRetention](#openapi-definition-ServiceRequestLevelRetention) | Service request level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain. | Optional |
| sessionReplayRetention | [SessionReplayRetention](#openapi-definition-SessionReplayRetention) | Session replay retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. | Optional |
| sessionReplayStorage | [SessionReplayStorage](#openapi-definition-SessionReplayStorage) | Session replay storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. | Optional |
| symbolFilesFromMobileApps | [SymbolFilesFromMobileApps](#openapi-definition-SymbolFilesFromMobileApps) | Symbol files from mobile apps storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. | Optional |
| syntheticMonitoringRetention | [SyntheticMonitoringRetention](#openapi-definition-SyntheticMonitoringRetention) | Synthetic monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. | Optional |
| transactionStorage | [TransactionStorage](#openapi-definition-TransactionStorage) | Transaction storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. | Optional |
| transactionTrafficQuota | [TransactionTrafficQuota](#openapi-definition-TransactionTrafficQuota) | Maximum number of newly monitored entry point PurePaths captured per process/minute on environment level. Can be set to any value from 100 to 100000. If skipped when editing via PUT method then already set limit will remain. | Optional |
| userActionsPerMinute | [UserActionsPerMinute](#openapi-definition-UserActionsPerMinute) | Maximum number of user actions generated per minute on environment level. Can be set to any value from 1 to 2147483646 or left unlimited. If skipped when editing via PUT method then already set limit will remain. | Optional |

#### The `RealUserMonitoringRetention` object

Real user monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `RumNonAggregatedDataRetention` object

Non-aggregated RUM data retention settings on environment level. Can be set to any value from 1 to 365 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `ServiceCodeLevelRetention` object

Service code level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `ServiceRequestLevelRetention` object

Service request level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `SessionReplayRetention` object

Session replay retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `SessionReplayStorage` object

Session replay storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] | Optional |
| maxLimit | integer | Maximum storage limit [bytes] | Optional |
| retentionReductionPercentage | string | Percentage of truncation for new data. | Optional |
| retentionReductionReason | string | Reason of truncation. | Optional |

#### The `SymbolFilesFromMobileApps` object

Symbol files from mobile apps storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] | Optional |
| maxLimit | integer | Maximum storage limit [bytes] | Optional |

#### The `SyntheticMonitoringRetention` object

Synthetic monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] | Optional |
| currentlyUsedInMillis | integer | Current data age [milliseconds] | Optional |
| maxLimitInDays | integer | Maximum retention limit [days] | Optional |

#### The `TransactionStorage` object

Transaction storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] | Optional |
| maxLimit | integer | Maximum storage limit [bytes] | Optional |
| retentionReductionPercentage | string | Percentage of truncation for new data. | Optional |
| retentionReductionReason | string | Reason of truncation. | Optional |

#### The `TransactionTrafficQuota` object

Maximum number of newly monitored entry point PurePaths captured per process/minute on environment level. Can be set to any value from 100 to 100000. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| maxLimit | integer | Maximum traffic [units per minute] | Optional |

#### The `UserActionsPerMinute` object

Maximum number of user actions generated per minute on environment level. Can be set to any value from 1 to 2147483646 or left unlimited. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| maxLimit | integer | Maximum traffic [units per minute] | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "example environment",



"state": "ENABLED",



"tags": [



"tag1",



"tag2"



],



"trial": false



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EnvironmentShortRepresentation](#openapi-definition-EnvironmentShortRepresentation) | Success. The environment has been created and started. The response body contains the generated ID of the environment and a token with the scopes 'apiTokens.read' and 'apiTokens.write' (for usage with token API v2) and 'TenantTokenManagement'. The location header contains the generated ID as well. |
| **400** | - | Failed. The input is invalid. |

### Response body objects

#### The `EnvironmentShortRepresentation` object

The short representation of an environment.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |
| tokenManagementToken | string | A token with the 'Token management' permission. Can be used to within the newly created environment to create other tokens for configuring this environment. This value is only set if an environment was created with the query parameter 'createToken=true'. |

### Response body JSON models

```
{



"description": "string",



"id": "string",



"name": "string",



"tokenManagementToken": "string"



}
```

## Example

Creates an environment called `MyNewTeam` specifying details on license quota, storage limits and data retention.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/environments?createToken=true" -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890" -H "Content-Type: application/json; charset=utf-8" -d



"{\"name\":\"MyNewTeam\",\"state\":\"ENABLED\",\"tags\":[\"owner:john.wicked@dynatrace.com\",\"department:finance\"],\"trial\":false}, \"quotas\":{\"hostUnits\":{\"maxLimit\":1},\"demUnits\":{\"monthlyLimit\":1,\"annualLimit\":1},\"userSessions\":{\"totalMonthlyLimit\":1,\"totalAnnualLimit\":2},\"syntheticMonitors\":{\"monthlyLimit\":1,\"annualLimit\":1},\"davisDataUnits\":{\"monthlyLimit\":1,\"annualLimit\":2}},\"storage\":{\"transactionStorage\":{\"maxLimit\":1024},\"sessionReplayStorage\":{\"maxLimit\":2048},\"symbolFilesFromMobileApps\":{\"maxLimit\":5050},\"serviceRequestLevelRetention\":{\"maxLimitInDays\":35},\"serviceCodeLevelRetention\":{\"maxLimitInDays\":10},\"realUserMonitoringRetention\":{\"maxLimitInDays\":35},\"syntheticMonitoringRetention\":{\"maxLimitInDays\":35},\"sessionReplayRetention\":{\"maxLimitInDays\":35},\"userActionsPerMinute\":{\"maxLimit\":3500},\"transactionTrafficQuota\":{\"maxLimit\":1000}}}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/environments?createToken=true
```

#### Request body

```
{



"name": "MyNewTeam",



"state": "ENABLED",



"tags": [



"owner:john.wicked@dynatrace.com",



"department:finance"



],



"trial": false,



"quotas": {



"hostUnits": {



"maxLimit": 1



},



"demUnits": {



"monthlyLimit": 1,



"annualLimit": 1



},



"userSessions": {



"totalMonthlyLimit": 1,



"totalAnnualLimit": 2



},



"syntheticMonitors": {



"monthlyLimit": 1,



"annualLimit": 1



},



"davisDataUnits": {



"monthlyLimit": 1,



"annualLimit": 2



}



},



"storage": {



"transactionStorage": {



"maxLimit": 1024



},



"sessionReplayStorage": {



"maxLimit": 2048



},



"symbolFilesFromMobileApps": {



"maxLimit": 5050



},



"serviceRequestLevelRetention": {



"maxLimitInDays": 35



},



"serviceCodeLevelRetention": {



"maxLimitInDays": 10



},



"realUserMonitoringRetention": {



"maxLimitInDays": 35



},



"syntheticMonitoringRetention": {



"maxLimitInDays": 35



},



"sessionReplayRetention": {



"maxLimitInDays": 35



},



"userActionsPerMinute": {



"maxLimit": 3500



},



"transactionTrafficQuota": {



"maxLimit": 1000



}



}



}
```

#### Response body

Success. The environment has been created and started. The response body contains the generated ID of the environment and a token with the `Token management` permission. The location header contains the generated ID as well.

```
{



"id": "11a113a1-a11b-1234-123a-4df674c8eb8e",



"name": "MyNewTeam",



"tokenManagementToken":



"<DYNATRACE_TOKEN_PLACEHOLDER>.<token-value>"



}
```

#### Response code

`201`
