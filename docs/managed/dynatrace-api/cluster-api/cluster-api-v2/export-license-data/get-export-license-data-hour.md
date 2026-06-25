---
title: Export license data for 1 hour
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v2/export-license-data/get-export-license-data-hour
scraped: 2026-05-12T12:07:14.913245
---

# Export license data for 1 hour

# Export license data for 1 hour

* Updated on Nov 25, 2025

This API call exports aggregated hourly license usage of all your environments as a ZIP file for an hour.

This API is only compatible with [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.") and does not contain billed usage.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/license/consumption/hour`

## Response format

The request produces an `application/json` payload.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LicenseConsumption](#openapi-definition-LicenseConsumption) | Success |
| **400** | - | Bad request. Provided timestamp is incorrect. |
| **422** | - | Incompatible licensing model. |
| **500** | - | Operation failed |

### Response body objects

#### The `LicenseConsumption` object

Describes an hour of license consumption for each environment in the cluster

| Element | Type | Description |
| --- | --- | --- |
| clusterUuid | string | Cluster identifier |
| environmentBillingEntries | [EnvironmentLicenseConsumption[]](#openapi-definition-EnvironmentLicenseConsumption) | Environments' consumptions |
| timeFrameEnd | string | Consumption data export timeframe end |
| timeFrameStart | string | Consumption data export timeframe start |

#### The `EnvironmentLicenseConsumption` object

Describes license consumption for the environment

| Element | Type | Description |
| --- | --- | --- |
| customMetrics | [CustomMetricDto[]](#openapi-definition-CustomMetricDto) | Custom metrics consumption |
| davisDataUnits | [DavisDataUnitsUsageDto[]](#openapi-definition-DavisDataUnitsUsageDto) | Davis Data Units consumption |
| downloads | [DownloadsDto[]](#openapi-definition-DownloadsDto) | Not used |
| environmentUuid | string | Environment identifier |
| highAvailabilityCluster | boolean | Indicates if cluster has redundancy by the high availability feature. |
| hostUsages | [HostConsumption[]](#openapi-definition-HostConsumption) | Monitored hosts' consumption |
| internalUse | boolean | Environment is intended for internal use (e.g. self-monitoring) |
| logStorageUsageBytes | integer | Count of Log monitoring storage usage in bytes |
| logUploadVolumeBytes | integer | Count of Log monitoring upload volume in bytes |
| mobileSessionReplays | integer | Count of consumed mobile user session replays |
| mobileSessions | integer | Count of consumed mobile user sessions |
| newProblems | integer | Not used |
| sessionReplays | integer | Count of consumed user session replays |
| syntheticBillingUsage | [SyntheticBillingUsageDto[]](#openapi-definition-SyntheticBillingUsageDto) | Synthetic monitoring consumption |
| syntheticUsages | [SyntheticUsageDto[]](#openapi-definition-SyntheticUsageDto) | Not used |
| totalRUMUserPropertiesUsed | integer | Count of defined user session properties |
| trial | boolean | Environment type flag |
| visits | integer | Count of consumed user sessions |

#### The `CustomMetricDto` object

Custom metrics consumption

| Element | Type | Description |
| --- | --- | --- |
| source | string | Custom metric definition source name |
| total | integer | Count of custom metrics |

#### The `DavisDataUnitsUsageDto` object

Davis Data Units consumption.

| Element | Type | Description |
| --- | --- | --- |
| pool | string | Davis Data Units pool name |
| total | number | Count of consumed Davis Data Units |

#### The `DownloadsDto` object

Not used

| Element | Type | Description |
| --- | --- | --- |
| downloadCount | integer | - |
| firstDownloadTime | string | - |
| type | string | - |
| version | string | - |

#### The `HostConsumption` object

Describes license consumption by the monitored host.

| Element | Type | Description |
| --- | --- | --- |
| agentUsages | [AgentConsumption[]](#openapi-definition-AgentConsumption) | Agent details |
| hasContainers | boolean | Host running containers |
| hostCategory | string | Host unit size symbol |
| hostMemoryBytes | integer | Host's RAM in bytes |
| hostName | string | Not used |
| infrastructureOnly | boolean | Infrastructure-only monitoring mode |
| osiId | integer | Host identifier |
| paas | boolean | Application-only monitoring mode |
| passMemoryLimit | integer | Container memory limit |
| premiumLogAnalytics | boolean | Premium Log monitoring |
| vendorTypeId | integer | Platform as a Service vendor identifier |

#### The `AgentConsumption` object

Describes license consumption by the OneAgent.

| Element | Type | Description |
| --- | --- | --- |
| agentId | integer | Agent unique identifier |
| agentTypeId | integer | Agent type ID; 1 for OS agent |
| agentUsageRecords | [AgentActivity[]](#openapi-definition-AgentActivity) | Agent activity periods within an hour |
| networkTraffic | integer | Not used |

#### The `AgentActivity` object

Describes a period of time when OneAgent was actively consuming a license.

| Element | Type | Description |
| --- | --- | --- |
| endTime | string | Agent running end time within an hour |
| startTime | string | Agent running start time within an hour |

#### The `SyntheticBillingUsageDto` object

Synthetic monitoring consumption

| Element | Type | Description |
| --- | --- | --- |
| monitorTypeId | integer | Synthetic monitor type ID; 1 for browser monitor, 2 for HTTP monitor |
| privateExecutions | integer | Count of executions from private locations |
| publicExecutions | integer | Count of executions from public locations |
| testId | integer | Unique Synthetic monitor identifier |

#### The `SyntheticUsageDto` object

Not used

| Element | Type | Description |
| --- | --- | --- |
| failureCount | integer | - |
| monitorDefinitionId | string | - |
| monitorDescription | string | - |
| monitorTypeId | integer | - |
| performedSyntheticActions | integer | - |
| successCount | integer | - |
| syntheticActionCount | integer | - |

### Response body JSON models

```
{



"clusterUuid": "string",



"environmentBillingEntries": [



{



"customMetrics": [



{



"source": "JMX, Dynatrace API",



"total": 1



}



],



"davisDataUnits": [



{



"pool": "Metrics, Serverless Functions, Log",



"total": 1



}



],



"downloads": [



{



"downloadCount": 1,



"firstDownloadTime": "string",



"type": "string",



"version": "string"



}



],



"environmentUuid": "string",



"highAvailabilityCluster": true,



"hostUsages": [



{



"agentUsages": [



{



"agentId": 1,



"agentTypeId": 1,



"agentUsageRecords": [



{



"endTime": "string",



"startTime": "string"



}



],



"networkTraffic": 1



}



],



"hasContainers": true,



"hostCategory": "string",



"hostMemoryBytes": 1,



"hostName": "string",



"infrastructureOnly": true,



"osiId": 1,



"paas": true,



"passMemoryLimit": 1,



"premiumLogAnalytics": true,



"vendorTypeId": 1



}



],



"internalUse": true,



"logStorageUsageBytes": 1,



"logUploadVolumeBytes": 1,



"mobileSessionReplays": 1,



"mobileSessions": 1,



"newProblems": 1,



"sessionReplays": 1,



"syntheticBillingUsage": [



{



"monitorTypeId": 1,



"privateExecutions": 1,



"publicExecutions": 1,



"testId": 1



}



],



"syntheticUsages": [



{



"failureCount": 1,



"monitorDefinitionId": "string",



"monitorDescription": "string",



"monitorTypeId": 1,



"performedSyntheticActions": 1,



"successCount": 1,



"syntheticActionCount": 1



}



],



"totalRUMUserPropertiesUsed": 1,



"trial": true,



"visits": 1



}



],



"timeFrameEnd": "string",



"timeFrameStart": "string"



}
```

## Example

In this example, you request an hour of license data on Monday, 10 January 2022 10:00:00 GMT (1641808800000)

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/license/consumption/hour?startTs=1641810541000"



-H "accept: application/json; charset=utf-8"



-H "Authorization: Api-Token abcdefjhij1234567890"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/license/consumption/hour?startTs=1641808800000
```

#### Response body

```
{



"clusterUuid": "02ed02ed-02ed-02ed-02ed-02ed02ed02ed",



"timeFrameStart": 1641808800000,



"timeFrameEnd": 1641812400000,



"environmentBillingEntries": [



{



"environmentUuid": "590939093-9093-9093-9093-909390903909",



"visits": 323,



"mobileSessions": 101,



"totalRUMUserPropertiesUsed": 10,



"newProblems": 0,



"hostUsages": [



{



"osiId": -5174977934749450000,



"hostName": null,



"hostCategory": "L",



"agentUsages": [



{



"networkTraffic": null,



"agentId": 2000000008,



"agentTypeId": 1,



"agentUsageRecords": [



{



"startTime": 1641808800000,



"endTime": 1641812400000



}



]



}



],



"infrastructureOnly": false,



"paas": false,



"passMemoryLimit": 0,



"vendorTypeId": null,



"hostMemoryBytes": 8538218496,



"premiumLogAnalytics": true,



"hasContainers": false



}



],



"downloads": [],



"syntheticUsages": [],



"syntheticBillingUsage": [],



"customMetrics": null,



"davisDataUnits": [



{



"pool": "Metrics",



"total": 31



},



{



"pool": "Log",



"total": 233



},



{



"pool": "Events",



"total": 123



},



{



"pool": "Traces",



"total": 15.46369



},



{



"pool": "Serverless",



"total": 4



}



],



"trial": false,



"internalUse": false,



"highAvailabilityCluster": false,



"logStorageUsageBytes": 0,



"logUploadVolumeBytes": 0,



"sessionReplays": 3123,



"mobileSessionReplays": 1232



}



]



}
```

#### Response code

`200`