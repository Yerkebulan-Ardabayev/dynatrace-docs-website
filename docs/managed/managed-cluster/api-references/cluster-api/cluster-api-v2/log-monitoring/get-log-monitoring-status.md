---
title: "Get Log Monitoring status"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/get-log-monitoring-status
updated: 2026-02-09
---

# Get Log Monitoring status

# Get Log Monitoring status

* Published Oct 18, 2021

This API call retrieves the Log Monitoring status for the specified environment.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/logMonitoring/{environmentId}/status`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| environmentId | string | The ID of the environment. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LogMonitoringStatus](#openapi-definition-LogMonitoringStatus) | Successful operation. |
| **404** | - | Failed. The requested resource doesn't exist. |

### Response body objects

#### The `LogMonitoringStatus` object

Log Monitoring status

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | Specifies whether Log Monitoring is enabled |

### Response body JSON models

```
{



"enabled": "true"



}
```

## Example

In this example, you retrieve Log Monitoring configuration status for the environment: `19a963a7-b19f-4382-964a-4df674c8eb8e`. In return, you receive a JSON response that indicating that the latest version of Dynatrace Log Monitoring is enabled in this environment.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/logMonitoring/19a963a7-b19f-4382-964a-4df674c8eb8e/status"



-H  "accept: application/json; charset=utf-8"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/logMonitoring/19a963a7-b19f-4382-964a-4df674c8eb8e/status
```

#### Response body

```
{



"enabled": "true"



}
```

#### Response code

`200`
