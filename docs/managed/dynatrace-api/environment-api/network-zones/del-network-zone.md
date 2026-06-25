---
title: Network zones API - DELETE a network zone
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/network-zones/del-network-zone
scraped: 2026-05-12T11:52:08.425170
---

# Network zones API - DELETE a network zone

# Network zones API - DELETE a network zone

* Reference
* Published Apr 08, 2020

Deletes the specified network zone. Deletion cannot be undone!

You can only delete an empty network zone (a zone that no ActiveGate or OneAgent is using). If the network zone is used as an alternative zone for any OneAgent, it will be automatically removed from the list of possible alternatives.

|  |  |
| --- | --- |
| DELETE | * Managed - Environment https://{your-environment-id}.live.dynatrace.com/api/v2/networkZones/{id} * Managed - Cluster Use the `DELETE /networkZones/{id}` endpoint of the [Cluster API](/managed/dynatrace-api/cluster-api/cluster-api-v2 "Find out about managing environments, network zones, Synthetic locations, nodes, and tokens in Dynatrace Managed using the Cluster API v2."). |

## Authentication

To execute this request, you need the **Write network zones** (`networkZones.write`) permission assigned to your API token. To learn how to obtain and use it, see [Authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the network zone to be deleted. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Deleted. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. See error message in the response body for details. |
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

* [Network zones](/managed/manage/network-zones "Find out how network zones work in Dynatrace.")