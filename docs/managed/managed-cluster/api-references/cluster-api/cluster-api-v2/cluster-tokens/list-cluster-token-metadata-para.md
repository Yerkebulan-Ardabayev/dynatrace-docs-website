---
title: "List Cluster token metadata with id"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-para
updated: 2026-02-09
---

# List Cluster token metadata with id

# List Cluster token metadata with id

* Published Feb 12, 2020

This API call lists the metadata of a Dynatrace Cluster token by the ID of the token.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required token. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Success |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested token has not been found. |

### Response body objects

#### The `TokenMetadata` object

Metadata of a token.

| Element | Type | Description |
| --- | --- | --- |
| created | integer | The creation time as a unix timestamp in milliseconds. |
| expires | integer | The expiration time as a unix timestamp in milliseconds. |
| id | string | The ID of the token. |
| lastUse | integer | The unix timestamp in milliseconds when the token was last used. |
| name | string | The name of the token. |
| personalAccessToken | boolean | The token is a [personal access tokenï»¿](https://dt-url.net/wm03sop) (`true`) or an API token (`false`). |
| revoked | boolean | Revocation status of the token. Revoked tokens are disabled. |
| scopes | string[] | A list of scopes assigned to the token. The element can hold these values * `ClusterTokenManagement` * `ControlManagement` * `DiagnosticExport` * `EnvironmentTokenManagement` * `ExternalSyntheticIntegration` * `Nodekeeper` * `ReadSyntheticData` * `ServiceProviderAPI` * `UnattendedInstall` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `apiTokens.read` * `apiTokens.write` * `settings.read` * `settings.write` |
| userId | string | The owner of the token. |

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



"created": 1554076800000,



"expires": 1585976400000,



"id": "acbed0c4-4ef1-4303-991f-102510a69322",



"lastUse": 1554354000000,



"name": "myToken",



"personalAccessToken": true,



"revoked": true,



"scopes": [



"DataExport",



"ReadConfig",



"WriteConfig"



],



"userId": "john.smith"



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

In this example, the request queries the metadata of the token, which has the ID of `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"



-H  "accept: application/json; charset=utf-8"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Response body

```
{



"id": "4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4",



"name": "myToken",



"userId": "john.smith",



"revoked": true,



"created": 1554076800000,



"expires": 1585976400000,



"lastUse": 1554354000000,



"scopes": [



"DataExport",



"ReadConfig",



"WriteConfig"



]



}
```

#### Response code

`204`
