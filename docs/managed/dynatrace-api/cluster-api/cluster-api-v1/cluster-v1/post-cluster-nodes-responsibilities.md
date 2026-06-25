---
title: Configure cluster nodes responsibilities
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-nodes-responsibilities
scraped: 2026-05-12T12:09:04.775577
---

# Configure cluster nodes responsibilities

# Configure cluster nodes responsibilities

* Published Apr 30, 2021

This API request configures cluster nodes responsibilities.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/cluster/configuration`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [ClusterNodesConfigDtoNodeResponsibilitiesConfigDto](#openapi-definition-ClusterNodesConfigDtoNodeResponsibilitiesConfigDto) | List of nodes for which responsibilities should be changed | body | Required |

### Request body objects

#### The `ClusterNodesConfigDtoNodeResponsibilitiesConfigDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| clusterNodes | [NodeResponsibilitiesConfigDto[]](#openapi-definition-NodeResponsibilitiesConfigDto) | - | Optional |

#### The `NodeResponsibilitiesConfigDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| agent | boolean | - | Optional |
| id | integer | - | Optional |
| webUI | boolean | - | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"clusterNodes": [



{



"agent": true,



"id": 1,



"webUI": true



}



]



}
```

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Success |

## Example

In this example, we disable Web UI traffic at a node 1. You can check the status of the operation with the Get cluster nodes configuration current status API call.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration" -H  "accept: */*" -H  "Content-Type: application/json" -d "{\"clusterNodes\":[{\"id\":1,\"ipAddress\":\"10.10.4.2\",\"webUI\":false,\"agent\":true,\"datacenter\":\"datacenter-1\",\"kubernetesRole\":\"\"}]}"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/cluster/configuration
```

#### Request body

```
{



"clusterNodes": [



{



"id": 1,



"ipAddress": "10.10.4.2",



"webUI": false,



"agent": true,



"datacenter": "datacenter-1",



"kubernetesRole": ""



}



]



}
```

#### Response body

```
{



"lockAcquired": true,



"acquirationTime": 1619771074449,



"notAcquiredReason": null



}
```

#### Response code

`200`