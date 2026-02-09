---
title: "Update Cluster token"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/update-cluster-token
updated: 2026-02-09
---

# Update Cluster token

# Update Cluster token

* Published Feb 12, 2020

This API call updates the specified Dynatrace Cluster token. You can:

* Change the token name.
* Revoke the token.  
  A revoked token still exists in the environment, but it can't be used.
* Change the scope of a token.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the token to be updated.  You can't update the token you're using for authentication of the request. | path | Required |
| body | [UpdateToken](#openapi-definition-UpdateToken) | The JSON body of the request. Contains updated parameters of the token. | body | Required |

### Request body objects

#### The `UpdateToken` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The name of the token. | Optional |
| revoked | boolean | The token is revoked (`true`) or active (`false`). | Optional |
| scopes | string[] | The list of permissions assigned to the token.  Apart from the new permissions, you need to submit the existing permissions you want to keep, too. Any existing permission, missing in the payload, is revoked.  * `DiagnosticExport`: DiagnosticExport. * `ControlManagement`: ControlManagement. * `UnattendedInstall`: UnattendedInstall. * `ServiceProviderAPI`: Service Provider API. * `ExternalSyntheticIntegration`: Create and read synthetic monitors, locations, and nodes. * `ClusterTokenManagement`: Cluster token management. * `ReadSyntheticData`: Read synthetic monitors, locations, and nodes. * `Nodekeeper`: Nodekeeper access for node management. * `EnvironmentTokenManagement`: "Token Management" Token creation for existing environments. * `activeGateTokenManagement.read`: Read ActiveGate tokens. * `activeGateTokenManagement.create`: Create ActiveGate tokens. * `activeGateTokenManagement.write`: Write ActiveGate tokens. * `settings.read`: Read settings. * `settings.write`: Write settings. * `apiTokens.read`: Read API tokens. * `apiTokens.write`: Write API tokens. The element can hold these values * `DiagnosticExport` * `ControlManagement` * `UnattendedInstall` * `ServiceProviderAPI` * `ExternalSyntheticIntegration` * `ClusterTokenManagement` * `ReadSyntheticData` * `Nodekeeper` * `EnvironmentTokenManagement` * `activeGateTokenManagement.read` * `activeGateTokenManagement.create` * `activeGateTokenManagement.write` * `settings.read` * `settings.write` * `apiTokens.read` * `apiTokens.write` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"revoked": true,



"scopes": [



"DiagnosticExport"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The token has been updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. You can't update the token you're using for authentication of the request. |
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

In this example, the request queries the metadata of the specific token, which has the ID of `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4`. It changes the token scope by updating the token metadata. The name and validity of the token remain intact. The response code of 204 indicates that the update was successful.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: application/json; charset=utf-8"



-d  "{  \"revoked\": \"true\",  \"name\": \"updated token\",  \"scopes\": [    \"UnattendedInstall\"  ]}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens/4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4
```

#### Request body

```
{



"revoked": "true",



"name": "updated token",



"scopes": ["UnattendedInstall"]



}
```

#### Response code

`204`
