---
title: Synthetic nodes API - GET all nodes
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all
---

# Synthetic nodes API - GET all nodes

# Synthetic nodes API - GET all nodes

* Reference
* Published Jul 26, 2019

We have a new version of this API—[Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."). Check it out!

Lists all synthetic nodes (and their parameters) available for your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/nodes` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/nodes` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

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
| nodes | [NodeCollectionElement](#openapi-definition-NodeCollectionElement)[] | A list of synthetic nodes |

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

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/nodes
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



"version": "1.164.0.20190205-184318",



"browserMonitorsEnabled": false



},



{



"entityId": "1267320067",



"hostname": "244.94.30.253",



"ips": [



"244.94.30.253"



],



"version": "1.161.0.20181210-173639",



"browserMonitorsEnabled": false



},



{



"entityId": "353074222",



"hostname": "GDN-007",



"ips": [



"132.46.87.141"



],



"version": "1.166.0.20190311-110828",



"browserMonitorsEnabled": true



}



]



}
```

#### Response code

200