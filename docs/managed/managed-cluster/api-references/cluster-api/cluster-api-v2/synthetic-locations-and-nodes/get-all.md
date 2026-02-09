---
title: "Synthetic nodes API v2 - GET all nodes (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all
updated: 2026-02-09
---

# Synthetic nodes API v2 - GET all nodes (Dynatrace Managed)

# Synthetic nodes API v2 - GET all nodes (Dynatrace Managed)

* Published Oct 30, 2020

This API call lists all synthetic nodes (and their parameters) available for your environment. The request produces an `application/json` payload.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/nodes`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| assignedToLocation | string | Filters the resulting set of nodes to those which are assigned to a synthetic location or not. The element can hold these values * `TRUE` * `FALSE` | query | Optional |
| isContainerized | boolean | If set to true, returns only containerized nodes. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Nodes](#openapi-definition-Nodes) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Nodes` object

A list of synthetic nodes

| Element | Type | Description |
| --- | --- | --- |
| nodes | [NodeCollectionElement[]](#openapi-definition-NodeCollectionElement) | A list of synthetic nodes |

#### The `NodeCollectionElement` object

The short representation of a synthetic object. Only contains the ID and the display name.

| Element | Type | Description |
| --- | --- | --- |
| activeGateVersion | string | The version of the Active Gate. |
| autoUpdateEnabled | boolean | The Active Gate has the Auto update option enabled ('true') or not ('false') |
| browserMonitorsEnabled | boolean | Browser check capabilities enabled flag. |
| capabilities | string[] | The list of node's capabilities. |
| entityId | string | The ID of a node. |
| healthCheckStatus | string | The health check status of the synthetic node. |
| hostname | string | The hostname of a node. |
| ips | string[] | The IP of a node. |
| oneAgentRoutingEnabled | boolean | The Active Gate has the One Agent routing enabled ('true') or not ('false'). |
| operatingSystem | string | The Active Gate's host operating system. |
| playerVersion | string | The version of the synthetic player. |
| status | string | The status of the synthetic node. |
| version | string | The version of a node |

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



"nodes": [



{



"activeGateVersion": "1.172.2.20190607-040913",



"autoUpdateEnabled": true,



"browserMonitorsEnabled": true,



"capabilities": [



"HTTP_HIGH_RESOURCE",



"HTTP"



],



"entityId": "3086117876",



"healthCheckStatus": "Ok",



"hostname": "gdn.dyna.trace",



"ips": [



"238.245.160.14"



],



"oneAgentRoutingEnabled": true,



"operatingSystem": "Linux",



"playerVersion": "1.179.0.20190920-145430",



"status": "Running",



"version": "1.161.0.20181210-173639"



}



]



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

## Example

In this example, the request lists all synthetic nodes available in the `mySampleEnv` environment.

The API token is passed in the **Authorization** header.

The result is truncated to two entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/nodes
```

#### Response body

```
{



"nodes": [



{



"entityId": "3086117876",



"hostname": "gdn.dyna.trace",



"ips": [



"238.245.160.14"



],



"version": "1.207.0.20201029-141904",



"browserMonitorsEnabled": true,



"activeGateVersion": "1.207.0.20201029-180431",



"oneAgentRoutingEnabled": false,



"operatingSystem": "Platform: Linux, Version: 4.4.0-1092-aws, Architecture: amd64, Processors: 2",



"autoUpdateEnabled": true,



"status": "Running",



"playerVersion": "1.207.0.20201029-081128",



"healthCheckStatus": "Ok"



},



{



"entityId": "1267320067",



"hostname": "244.94.30.253",



"ips": [



"244.94.30.253"



],



"version": null,



"browserMonitorsEnabled": true,



"activeGateVersion": "1.207.0.20201029-180431",



"oneAgentRoutingEnabled": false,



"operatingSystem": "Platform: Linux, Version: 4.15.0-1057-azure, Architecture: amd64, Processors: 2",



"autoUpdateEnabled": true,



"status": null,



"playerVersion": null,



"healthCheckStatus": "Offline"



}



]



}
```

#### Response code

200
