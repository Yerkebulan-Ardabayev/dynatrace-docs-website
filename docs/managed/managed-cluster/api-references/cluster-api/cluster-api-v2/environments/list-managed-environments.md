---
title: "List all existing environments"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/environments/list-managed-environments
updated: 2026-02-09
---

# List all existing environments

# List all existing environments

* Published Mar 09, 2021

This API call lists all existing environments.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/environments`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| nextPageKey | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response.  The first page is always returned if you don't specify the **nextPageKey** query parameter.  When the **nextPageKey** is set to obtain subsequent pages, you must omit all other query parameters. | query | Optional |
| pageSize | integer | The amount of environments in a single response payload.  The maximal allowed page size is 1000.  If not set, 100 is used. | query | Optional |
| sort | string | The sort order. Possible sorts orders are:  * 'name' (without quotes): Sort by name ascending. * '-name' (without quotes): Sort by name descending. * 'creationDate' (without quotes): Sort by creation date ascending. * '-creationDate' (without quotes): Sort by name descending. | query | Optional |
| filter | string | Specifies the filter of the query.  You can set one or several of the following criteria:  * Name: `name(string)`. The name can be either a substring or the full name of an environment. Case-insensitive. * Trial: `trial(true)` or `trial(false)`. Only includes trial environments if true is specified or only non-trial environments if false is specified. * State: `state(ENABLED)` or `state(DISABLED)`. * Tag: `tag(string)`. To filter by multiple tags by applying OR logic use `tag(string1,string2)`. To filter by multiple tags by applying AND logic use `tag(string1),tag(string2)`.   To set several criteria, separate them with a comma (`,`). Only results, matching **all** criteria, are included into response. | query | Optional |
| includeConsumptionInfo | boolean | If true, consumption information (limits, usage) is returned for each environment.  Returned usage is typically up to 1 hour old. To obtain fresher data, you can use **includeUncachedConsumptionInfo** parameter instead.  This option is not available for the DPS licensing model. | query | Optional |
| includeStorageInfo | boolean | If true, storage information (limits, usage) is returned for each environment. | query | Optional |
| includeUncachedConsumptionInfo | boolean | If true, uncached consumption information (limits, usage) is returned for each environment.  Up to date consumption will be calculated. Calculation may be time consuming, so it's recommended to use **includeConsumptionInfo** parameter instead.  If both this parameter and **includeConsumptionInfo** are set, **includeUncachedConsumptionInfo** will take priority.  This option is not available for the DPS licensing model. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EnvironmentList](#openapi-definition-EnvironmentList) | Successful operation. |
| **422** | - | Consumption information is not available for the DPS licensing model. |

### Response body objects

#### The `EnvironmentList` object

A list of environments.

| Element | Type | Description |
| --- | --- | --- |
| environments | [Environment[]](#openapi-definition-Environment) | The list of environments. |
| nextPageKey | string | The cursor for the next page of results. Has the value of `null` on the last page.  Use it in the **nextPageKey** query parameter to obtain subsequent pages of the result. |
| pageSize | integer | The number of entries per page. |
| totalCount | integer | The total number of entries in the result. |

#### The `Environment` object

Basic configuration for an environment.

| Element | Type | Description |
| --- | --- | --- |
| creationDate | string | The creation date of the environment in ISO 8601 format (yyyy-MM-dd'T'HH:mm:ss.SSS'Z') |
| id | string | The ID of the environment. Has to match [a-zA-Z0-9\_-]{1,70} |
| name | string | The display name of the environment. |
| quotas | [EnvironmentQuotas](#openapi-definition-EnvironmentQuotas) | Environment level consumption and quotas information. Only returned if includeConsumptionInfo or includeUncachedConsumptionInfo param is true. Not available for the DPS licensing model. If skipped when editing via PUT method then already set quotas will remain. |
| state | string | Indicates whether the environment is enabled or disabled. The default value is ENABLED. The element can hold these values * `DISABLED` * `ENABLED` |
| storage | [EnvironmentStorage](#openapi-definition-EnvironmentStorage) | Environment level storage usage and limit information. Not returned if includeStorageInfo param is not true. If skipped when editing via PUT method then already set limits will remain. |
| tags | string[] | A set of tags that are assigned to this environment. Every tag can have a maximum length of 100 characters. |
| trial | boolean | Specifies whether the environment is a trial environment or a non-trial environment. Creating a trial environment is only possible if your license allows that. The default value is false (non-trial). |

#### The `EnvironmentQuotas` object

Environment level consumption and quotas information. Only returned if includeConsumptionInfo or includeUncachedConsumptionInfo param is true. Not available for the DPS licensing model. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| customMetrics | [CustomMetricsQuota](#openapi-definition-CustomMetricsQuota) | Custom metrics consumption and quota information on environment level. Not set (and not editable) if Custom metrics is not enabled. Not set (and not editable) if Davis data units is enabled. If skipped when editing via PUT method then already set quota will remain. |
| davisDataUnits | [DavisDataUnitsQuota](#openapi-definition-DavisDataUnitsQuota) | Davis data units consumption and quota information on environment level. Not set (and not editable) if Davis data units is not enabled. If skipped when editing via PUT method then already set quotas will remain. |
| demUnits | [DemUnitsQuota](#openapi-definition-DemUnitsQuota) | DEM units consumption and quota information on environment level. Not set (and not editable) if DEM units is not enabled. If skipped when editing via PUT method then already set quotas will remain. |
| hostUnits | [HostUnitQuota](#openapi-definition-HostUnitQuota) | Host units consumption and quota information on environment level. If skipped when editing via PUT method then already set quota will remain. |
| logMonitoring | [LogMonitoringQuota](#openapi-definition-LogMonitoringQuota) | Log monitoring consumption and quota information on environment level. Not set (and not editable) if Log monitoring is not enabled. Not set (and not editable) if Log monitoring is migrated to Davis data on license level. If skipped when editing via PUT method then already set quotas will remain. |
| sessionProperties | [SessionPropertiesQuota](#openapi-definition-SessionPropertiesQuota) | User session properties consumption information on environment level. |
| syntheticMonitors | [SyntheticQuota](#openapi-definition-SyntheticQuota) | Synthetic monitors consumption and quota information on environment level. Not set (and not editable) if neither Synthetic nor DEM units is enabled. If skipped when editing via PUT method then already set quotas will remain. |
| userSessions | [UserSessionsQuota](#openapi-definition-UserSessionsQuota) | User sessions consumption and quota information on environment level. If skipped when editing via PUT method then already set quotas will remain. |

#### The `CustomMetricsQuota` object

Custom metrics consumption and quota information on environment level. Not set (and not editable) if Custom metrics is not enabled. Not set (and not editable) if Davis data units is enabled. If skipped when editing via PUT method then already set quota will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentUsage | number | Current environment usage. |
| maxLimit | integer | Concurrent environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `DavisDataUnitsQuota` object

Davis data units consumption and quota information on environment level. Not set (and not editable) if Davis data units is not enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `DemUnitsQuota` object

DEM units consumption and quota information on environment level. Not set (and not editable) if DEM units is not enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `HostUnitQuota` object

Host units consumption and quota information on environment level. If skipped when editing via PUT method then already set quota will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentUsage | number | Current environment usage. |
| maxLimit | integer | Concurrent environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `LogMonitoringQuota` object

Log monitoring consumption and quota information on environment level. Not set (and not editable) if Log monitoring is not enabled. Not set (and not editable) if Log monitoring is migrated to Davis data on license level. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `SessionPropertiesQuota` object

User session properties consumption information on environment level.

| Element | Type | Description |
| --- | --- | --- |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. |

#### The `SyntheticQuota` object

Synthetic monitors consumption and quota information on environment level. Not set (and not editable) if neither Synthetic nor DEM units is enabled. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| annualLimit | integer | Annual environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |
| consumedThisMonth | number | Monthly environment consumption. Resets each calendar month. |
| consumedThisYear | number | Yearly environment consumption. Resets each year on license creation date anniversary. |
| monthlyLimit | integer | Monthly environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `UserSessionsQuota` object

User sessions consumption and quota information on environment level. If skipped when editing via PUT method then already set quotas will remain.

| Element | Type | Description |
| --- | --- | --- |
| consumedMobileSessionsThisMonth | number | Monthly Mobile user sessions environment consumption. Resets each calendar month. |
| consumedMobileSessionsThisYear | number | Yearly Mobile user sessions environment consumption. Resets each year on license creation date anniversary. |
| consumedUserSessionsWithMobileSessionReplayThisMonth | number | Monthly Mobile user sessions with replay environment consumption. Resets each calendar month. |
| consumedUserSessionsWithMobileSessionReplayThisYear | number | Yearly Mobile user sessions with replay environment consumption. Resets each year on license creation date anniversary. |
| consumedUserSessionsWithWebSessionReplayThisMonth | number | Monthly Web user sessions with replay environment consumption. Resets each calendar month. |
| consumedUserSessionsWithWebSessionReplayThisYear | number | Yearly Web user sessions with replay environment consumption. Resets each year on license creation date anniversary. |
| totalAnnualLimit | integer | Annual total User sessions environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |
| totalConsumedThisMonth | number | Monthly total User sessions environment consumption. Resets each calendar month. |
| totalConsumedThisYear | number | Yearly total User sessions environment consumption. Resets each year on license creation date anniversary. |
| totalMonthlyLimit | integer | Monthly total User sessions environment quota. Not set if unlimited. When updating via PUT method, skipping this field will set quota unlimited. |

#### The `EnvironmentStorage` object

Environment level storage usage and limit information. Not returned if includeStorageInfo param is not true. If skipped when editing via PUT method then already set limits will remain.

| Element | Type | Description |
| --- | --- | --- |
| realUserMonitoringRetention | [RealUserMonitoringRetention](#openapi-definition-RealUserMonitoringRetention) | Real user monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. |
| rumNonAggregatedDataRetention | [RumNonAggregatedDataRetention](#openapi-definition-RumNonAggregatedDataRetention) | Non-aggregated RUM data retention settings on environment level. Can be set to any value from 1 to 365 days. If skipped when editing via PUT method then already set limit will remain. |
| serviceCodeLevelRetention | [ServiceCodeLevelRetention](#openapi-definition-ServiceCodeLevelRetention) | Service code level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain. |
| serviceRequestLevelRetention | [ServiceRequestLevelRetention](#openapi-definition-ServiceRequestLevelRetention) | Service request level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain. |
| sessionReplayRetention | [SessionReplayRetention](#openapi-definition-SessionReplayRetention) | Session replay retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. |
| sessionReplayStorage | [SessionReplayStorage](#openapi-definition-SessionReplayStorage) | Session replay storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. |
| symbolFilesFromMobileApps | [SymbolFilesFromMobileApps](#openapi-definition-SymbolFilesFromMobileApps) | Symbol files from mobile apps storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. |
| syntheticMonitoringRetention | [SyntheticMonitoringRetention](#openapi-definition-SyntheticMonitoringRetention) | Synthetic monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain. |
| transactionStorage | [TransactionStorage](#openapi-definition-TransactionStorage) | Transaction storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain. |
| transactionTrafficQuota | [TransactionTrafficQuota](#openapi-definition-TransactionTrafficQuota) | Maximum number of newly monitored entry point PurePaths captured per process/minute on environment level. Can be set to any value from 100 to 100000. If skipped when editing via PUT method then already set limit will remain. |
| userActionsPerMinute | [UserActionsPerMinute](#openapi-definition-UserActionsPerMinute) | Maximum number of user actions generated per minute on environment level. Can be set to any value from 1 to 2147483646 or left unlimited. If skipped when editing via PUT method then already set limit will remain. |

#### The `RealUserMonitoringRetention` object

Real user monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `RumNonAggregatedDataRetention` object

Non-aggregated RUM data retention settings on environment level. Can be set to any value from 1 to 365 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `ServiceCodeLevelRetention` object

Service code level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `ServiceRequestLevelRetention` object

Service request level retention settings on environment level. Service code level retention time can't be greater than service request level retention time and both can't exceed one year.If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `SessionReplayRetention` object

Session replay retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `SessionReplayStorage` object

Session replay storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] |
| maxLimit | integer | Maximum storage limit [bytes] |
| retentionReductionPercentage | string | Percentage of truncation for new data. |
| retentionReductionReason | string | Reason of truncation. |

#### The `SymbolFilesFromMobileApps` object

Symbol files from mobile apps storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] |
| maxLimit | integer | Maximum storage limit [bytes] |

#### The `SyntheticMonitoringRetention` object

Synthetic monitoring retention settings on environment level. Can be set to any value from 1 to 35 days. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsedInDays | integer | Current data age [days] |
| currentlyUsedInMillis | integer | Current data age [milliseconds] |
| maxLimitInDays | integer | Maximum retention limit [days] |

#### The `TransactionStorage` object

Transaction storage usage and limit information on environment level. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| currentlyUsed | integer | Currently used storage [bytes] |
| maxLimit | integer | Maximum storage limit [bytes] |
| retentionReductionPercentage | string | Percentage of truncation for new data. |
| retentionReductionReason | string | Reason of truncation. |

#### The `TransactionTrafficQuota` object

Maximum number of newly monitored entry point PurePaths captured per process/minute on environment level. Can be set to any value from 100 to 100000. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| maxLimit | integer | Maximum traffic [units per minute] |

#### The `UserActionsPerMinute` object

Maximum number of user actions generated per minute on environment level. Can be set to any value from 1 to 2147483646 or left unlimited. If skipped when editing via PUT method then already set limit will remain.

| Element | Type | Description |
| --- | --- | --- |
| maxLimit | integer | Maximum traffic [units per minute] |

### Response body JSON models

```
{



"environments": [



{



"name": "example environment",



"state": "ENABLED",



"tags": [



"tag1",



"tag2"



],



"trial": false



}



],



"nextPageKey": "AQAAABQBAAAABQ==",



"pageSize": 1,



"totalCount": 1



}
```

## Example

Lists the two newest enabled environments with their license consumption, sorted by name.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/environments?pageSize=2&sort=-creationDate&filter=state%28ENABLED%29&includeConsumptionInfo=true" -H "accept: application/json; charset=utf-8" -H "Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/environments?pageSize=2&sort=-creationDate&filter=state%28ENABLED%29&includeConsumptionInfo=true
```

#### Response body

```
{



"totalCount": 78,



"pageSize": 2,



"nextPageKey": "AAAAAQAAAAIBnldfkgldsjoeriKIDFL2AAABd3uuvIMBAA5zdGF0ZShFTkFCTEVEKQEADS1jcmVhdGlvbkRhdGU=",



"environments": [



{



"name": "AndroidApps",



"id": "be22c776-1414-00e0-a00a-00b0dcf56443321",



"trial": false,



"state": "ENABLED",



"tags": [],



"creationDate": "2021-02-09T11:03:17.732Z",



"quotas": {



"hostUnits": {



"maxLimit": 10,



"currentUsage": 0



},



"demUnits": {



"monthlyLimit": 50001,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"userSessions": {



"totalMonthlyLimit": null,



"totalAnnualLimit": null,



"totalConsumedThisMonth": 0,



"totalConsumedThisYear": 0,



"consumedMobileSessionsThisMonth": 0,



"consumedMobileSessionsThisYear": 0,



"consumedUserSessionsWithWebSessionReplayThisMonth": 0,



"consumedUserSessionsWithWebSessionReplayThisYear": 0,



"consumedUserSessionsWithMobileSessionReplayThisMonth": 0,



"consumedUserSessionsWithMobileSessionReplayThisYear": 0



},



"sessionProperties": {



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"syntheticMonitors": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"customMetrics": null,



"davisDataUnits": {



"monthlyLimit": 18162,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"logMonitoring": null



}



},



{



"name": "Service Team",



"id": "881c4134-0000-0a00-aa0a-5b03ab7a34ed",



"trial": false,



"state": "ENABLED",



"tags": [],



"creationDate": "2021-02-07T08:49:45.091Z",



"quotas": {



"hostUnits": {



"maxLimit": null,



"currentUsage": 0



},



"demUnits": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 62



},



"userSessions": {



"totalMonthlyLimit": null,



"totalAnnualLimit": null,



"totalConsumedThisMonth": 0,



"totalConsumedThisYear": 0,



"consumedMobileSessionsThisMonth": 0,



"consumedMobileSessionsThisYear": 0,



"consumedUserSessionsWithWebSessionReplayThisMonth": 0,



"consumedUserSessionsWithWebSessionReplayThisYear": 0,



"consumedUserSessionsWithMobileSessionReplayThisMonth": 0,



"consumedUserSessionsWithMobileSessionReplayThisYear": 0



},



"sessionProperties": {



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"syntheticMonitors": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 62



},



"customMetrics": null,



"davisDataUnits": {



"monthlyLimit": null,



"annualLimit": null,



"consumedThisMonth": 0,



"consumedThisYear": 0



},



"logMonitoring": null



}



}



]



}
```

#### Response code

`200`
