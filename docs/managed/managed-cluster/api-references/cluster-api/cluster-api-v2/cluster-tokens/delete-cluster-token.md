---
title: "Delete Cluster token"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/delete-cluster-token
updated: 2026-02-09
---

# Delete Cluster token

# Delete Cluster token

* Published Feb 12, 2020

This API call deletes a cluster token. It can be used to delete any token, including tokens not owned by the user who owns the token used to authenticate the call.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the token to be deleted. Can either be the public identifier or the secret.  You can't delete the token you're using for authentication of the request. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. You can't delete the token you're using for authentication of the request. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested token has not been found. |

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

## Example

In this example, the request deletes the token with ID value `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`. The response code of `204` indicates that the deletion was successful.

The API token is passed in the Authorization header.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"



-H "accept: application/json; charset=utf-8"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Response code

`204`
