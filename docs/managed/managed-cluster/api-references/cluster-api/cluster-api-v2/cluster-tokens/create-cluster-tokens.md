---
title: "Create new Cluster token"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/create-cluster-tokens
updated: 2026-02-09
---

# Create new Cluster token

# Create new Cluster token

* Published Feb 12, 2020

This API call creates a new cluster token.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

Creates a new Dynatrace Cluster token. The response contains the newly created token.

The request consumes and produces an `application/json` payload.

## Endpoint

`/api/cluster/v2/tokens`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [CreateToken](#openapi-definition-CreateToken) | The JSON body of the request. Contains parameters of the new token. | body | Required |

### Request body objects

#### The `CreateToken` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| expiresIn | [Duration](#openapi-definition-Duration) | Defines a period of time. | Optional |
| name | string | The name of the token. | Required |
| scopes | string[] | The list of scopes to be assigned to the token.  * `DiagnosticExport`: DiagnosticExport. * `ControlManagement`: ControlManagement. * `UnattendedInstall`: UnattendedInstall. * `ServiceProviderAPI`: Service Provider API. * `ExternalSyntheticIntegration`: Create and read synthetic monitors, locations, and nodes. * `ClusterTokenManagement`: Cluster token management. * `ReadSyntheticData`: Read synthetic monitors, locations, and nodes. * `Nodekeeper`: Nodekeeper access for node management. * `EnvironmentTokenManagement`: "Token Management" Token creation for existing environments. * `activeGateTokenManagement.read`: Read ActiveGate tokens. * `activeGateTokenManagement.create`: Create ActiveGate tokens. * `activeGateTokenManagement.write`: Write ActiveGate tokens. * `settings.read`: Read settings. * `settings.write`: Write settings. * `apiTokens.read`: Read API tokens. * `apiTokens.write`: Write API tokens. The element can hold these values * `DiagnosticExport` * `ControlManagement` * `UnattendedInstall` * `ServiceProviderAPI` * `ExternalSyntheticIntegration` * `ClusterTokenManagement` * `ReadSyntheticData` * `Nodekeeper` * `EnvironmentTokenManagement` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `settings.read` * `settings.write` * `apiTokens.read` * `apiTokens.write` | Required |

#### The `Duration` object

Defines a period of time.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| unit | string | The unit of time.  If not set, millisecond is used. The element can hold these values * `DAYS` * `HOURS` * `MILLIS` * `MINUTES` * `SECONDS` | Optional |
| value | integer | The amount of time. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"expiresIn": {



"unit": "DAYS",



"value": 1



},



"name": "string",



"scopes": [



"DiagnosticExport"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [Token](#openapi-definition-Token) | Success. The token has been created. The response body contains the token itself. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. Response body provides details. |

### Response body objects

#### The `Token` object

| Element | Type | Description |
| --- | --- | --- |
| token | string | Dynatrace API authentication token. |

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



"token": "abcdefjhij1234567890"



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

In this example, the request creates a new token named `Mytoken` that is valid for 24 hours. With this token you will be able to perform a diagnostic export (`DiagnosticExport`) and unattended install (`UnattendedInstall`).

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/tokens"



-H "accept: application/json; charset=utf-8"



-H "Content-Type: application/json; charset=utf-8"



-d "{  \"name\": \"MyToken\",  \"scopes\": [    \"DiagnosticExport\",    \"UnattendedInstall\"  ],  \"expiresIn\": {    \"value\": 24,    \"unit\": \"HOURS\"  }}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens
```

#### Request body

```
{



"name": "MyToken",



"scopes": ["DiagnosticExport", "UnattendedInstall"],



"expiresIn": {



"value": 24,



"unit": "HOURS"



}



}
```

#### Response body

```
{



"token": "abcdefjhij1234567890"



}
```

#### Response code

`201`
