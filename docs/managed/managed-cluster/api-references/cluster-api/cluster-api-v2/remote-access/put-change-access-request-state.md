---
title: "Change state of access request"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/put-change-access-request-state
updated: 2026-02-09
---

# Change state of access request

# Change state of access request

* Published Feb 12, 2020

This API call changes state of access request for a specific request ID. You can set the state access request to `PENDING`, `ACCEPTED`, `REJECTED` or `EXPIRED`. The request consumes an `application/json` payload.

## Authentication

To execute this request, you need one of the following API-Token scopes:

* **Cluster token management** (`ClusterTokenManagement`)
* **Service Provider API** (`ServiceProviderAPI` )
* Nodekeeper access for node management (`Nodekeeper`)  
  To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/remoteaccess/requests`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| requestId | string | Request id param | path | Required |
| body | [AccessRequestStateData](#openapi-definition-AccessRequestStateData) | The JSON body of the request, containing new state of access request. | body | Optional |

### Request body objects

#### The `AccessRequestStateData` object

Access request data - format used to change a state of a request

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| state | string | Access request state The element can hold these values * `ACCEPTED` * `EXPIRED` * `PENDING` * `REJECTED` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"state": "ACCEPTED"



}
```

## Response code

### Response codes

| Code | Description |
| --- | --- |
| **200** | Success |
| **400** | Bad request |
| **403** | Approving remote access request is disabled |
| **404** | Access request not found |
| **409** | Access request was found, but it's already expired |
| **500** | Operation failed |

## Example

In this example you request to change the remote access permission to `rejected` for access request ID: `7a397770-86b7-473b-b23e-4a07d79f2eff`. The response code is `200` and the remote access permission state is changed.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff/state"



-H  "accept: */*"



-H  "Content-Type: */*"



-d "{\"state\":\"ACCEPTED\"}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff/state
```

#### Request body

```
{



"state": "REJECTED"



}
```

#### Response code

`200`
