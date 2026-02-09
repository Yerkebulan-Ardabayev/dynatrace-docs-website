---
title: "List available Cluster tokens"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/cluster-tokens/list-cluster-tokens
updated: 2026-02-09
---

# List available Cluster tokens

# List available Cluster tokens

* Published Feb 12, 2020

This API call lists available tokens in your environment.

You can narrow down the output by adding parameters. The token has to match all the specified parameters.

You can also specify the limit of returned tokens.

This list may contain tokens which were created automatically (for example, InstallerDownload, Mobile, â¦) and are not visible on the Settings page. Deleting these might have unintended side-effects as they may still be in use.

## Authentication

To execute this request, you need the **Cluster token management** (`ClusterTokenManagement`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/tokens`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| limit | integer | Limits the maximum number of returned tokens.  If not set the value of `1000` is used.  Maximum value is 1000000. | query | Optional |
| user | string | Filters the resulting set of tokens by user, who owns the token. | query | Optional |
| permissions | string[] | Filters the resulting set of tokens by scopes assigned to the token.  You can specify several permissions in the following format: `permissions=scope1&permissions=scope2`. The token must have *all* the specified scopes. The element can hold these values * `ClusterTokenManagement` * `ControlManagement` * `DiagnosticExport` * `EnvironmentTokenManagement` * `ExternalSyntheticIntegration` * `Nodekeeper` * `ReadSyntheticData` * `ServiceProviderAPI` * `UnattendedInstall` * `activeGateTokenManagement.create` * `activeGateTokenManagement.read` * `activeGateTokenManagement.write` * `apiTokens.read` * `apiTokens.write` * `settings.read` * `settings.write` | query | Optional |
| from | integer | Last used after this timestamp (UTC milliseconds). | query | Optional |
| to | integer | Last used before this timestamp (UTC milliseconds). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Success |

### Response body objects

#### The `StubList` object

An ordered list of short representations of Dynatrace entities.

| Element | Type | Description |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | An ordered list of short representations of Dynatrace entities. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Example

In this example, the request lists API tokens in the `myManaged.cluster.com` environment for user `Pete` with cluster token management permissions.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/tokens?limit=1000&user=Pete&permissions=ClusterTokenManagement"



-H  "accept: application/json; charset=utf-8"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/tokens?limit=1000
```

#### Response body

```
{



"values": [



{



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1",



"description": "Dynatrace entity 1 for the REST API example"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

#### Response code

`200`
