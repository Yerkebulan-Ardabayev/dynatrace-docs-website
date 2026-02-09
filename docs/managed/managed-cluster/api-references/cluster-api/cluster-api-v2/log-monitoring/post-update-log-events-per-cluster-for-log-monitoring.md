---
title: "Update log events per cluster for Log Monitoring"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/log-monitoring/post-update-log-events-per-cluster-for-log-monitoring
updated: 2026-02-09
---

# Update log events per cluster for Log Monitoring

# Update log events per cluster for Log Monitoring

* Published Oct 14, 2021

This API call updates the total log events per cluster limit based on the cluster resources size.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/logMonitoring/refreshLogEventsLimit`

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [LogEventsLimitDto](#openapi-definition-LogEventsLimitDto) | Successful operation. Returns new log events limit |
| **500** | - | Refreshing log events limit not possible due to lack of storage statistics |

### Response body objects

#### The `LogEventsLimitDto` object

| Element | Type | Description |
| --- | --- | --- |
| limit | integer | - |

### Response body JSON models

```
{



"limit": 1



}
```

## Example

In this example, you increase the log events ingest limit to `54236` log events per minute per cluster.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/logMonitoring/refreshLogEventsLimit"



-H "accept: application/json; charset=utf-8"



-H "Authorization: Api-Token abc"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/logMonitoring/refreshLogEventsLimit
```

#### Response body

```
{



"limit": 54236



}
```

#### Response code

`200`
