---
title: "List Cluster token metadata with request"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-token-metadata-req
updated: 2026-02-09
---

# List Cluster token metadata with request

# List Cluster token metadata with request

* Published Feb 12, 2020

This API call lists the metadata of a Dynatrace Cluster token by the token value. The request consumes and produces an `application/json` payload.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens/lookup`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [Token](#openapi-definition-Token) | The JSON body of the request. Contains the required token. | body | Required |

### Request body objects

#### The `Token` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| token | string | Dynatrace API authentication token. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"token": "abcdefjhij1234567890"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TokenMetadata](#openapi-definition-TokenMetadata) | Success |

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

## Example

In this example, the request queries the metadata of the `4e9f128e-04f9-4795-pj319-8b7c-3c14a5e885e4` token.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/tokens/lookup"



-H  "accept: application/json; charset=utf-8"



-H  "Content-Type: application/json; charset=utf-8"



-d  "{  \"token\": \"abcdefjhij1234567890\"}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens/lookup
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

`200`
