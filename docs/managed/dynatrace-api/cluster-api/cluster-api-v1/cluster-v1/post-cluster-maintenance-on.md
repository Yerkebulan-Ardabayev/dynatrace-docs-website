---
title: Turn on the maintenance of the cluster
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/cluster-v1/post-cluster-maintenance-on
scraped: 2026-05-12T12:12:23.359385
---

# Turn on the maintenance of the cluster

# Turn on the maintenance of the cluster

* Published Sep 29, 2025

This API request turns on the maintenance of the cluster.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/cluster/maintenance/on`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [IpMigrationMaintenanceRequestDto](#openapi-definition-IpMigrationMaintenanceRequestDto) | JSON body of the request. Contains basic details about the cluster maintenance | body | Required |

### Request body objects

#### The `IpMigrationMaintenanceRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| nodeId | integer | An ID of the node that the migration is performed on. | Required |
| reason | string | A reason for the maintenance. The element can hold these values * `IP_MIGRATION` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"nodeId": 1,



"reason": "IP_MIGRATION"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | - | Success. The maintenance is now enabled. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. Can't enable the maintenance state, because the previous hasn't finished. |

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

#### Request body

```
{



"nodeId": 1,



"reason": "IP_MIGRATION"



}
```

#### Response body

```
{



"error": {



"code": 0,



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

#### Response code

200