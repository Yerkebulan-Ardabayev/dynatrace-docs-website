---
title: "Grant remote access permission"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/post-remote-access-permission
updated: 2026-02-09
---

# Grant remote access permission

# Grant remote access permission

* Published Feb 12, 2020

This API call grants remote access permission to a specific user. You can specify the user role, duration, and reason for remote access request. The request consumes and produces an `application/json` payload.

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
| body | [CreateAccessRequestDto](#openapi-definition-CreateAccessRequestDto) | The JSON body of the request, containing parameters of access request. | body | Optional |

### Request body objects

#### The `CreateAccessRequestDto` object

Access request data - format used to create a request

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| reason | string | Request reason description | Optional |
| requestedDays | integer | For how many days access is requested | Optional |
| role | string | Requested role The element can hold these values * `devops-admin` * `devops-user` * `devops-viewer` | Optional |
| userId | string | User id | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"reason": "string",



"requestedDays": 1,



"role": "devops-admin",



"userId": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [AccessRequestData](#openapi-definition-AccessRequestData) | Successfully created |
| **400** | - | Invalid parameters |
| **403** | - | Approving remote access request is disabled |
| **500** | - | Operation failed |
| **513** | - | Mission Control is unavailable |

### Response body objects

#### The `AccessRequestData` object

Access Request data

| Element | Type | Description |
| --- | --- | --- |
| createdTimestamp | integer | Access request created at (timestamp) |
| expirationTimestamp | integer | Access expires at (timestamp) |
| reason | string | Request reason description |
| requestId | string | Request id |
| requestedDays | integer | For how many days access is requested |
| role | string | Requested role The element can hold these values * `devops-admin` * `devops-user` * `devops-viewer` |
| state | string | Access request state The element can hold these values * `ACCEPTED` * `EXPIRED` * `PENDING` * `REJECTED` |
| stateModifiedByUser | string | Access request state was modified by user |
| userId | string | User id |

### Response body JSON models

```
{



"createdTimestamp": 1,



"expirationTimestamp": 1,



"reason": "string",



"requestId": "string",



"requestedDays": 1,



"role": "devops-admin",



"state": "ACCEPTED",



"stateModifiedByUser": "string",



"userId": "string"



}
```

## Example

In this example, you grant the user `john.smith@dynatrace.com` a remote cluster permission with an admin role for `7` days.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests"



-H  "accept: application/json"



-H  "Content-Type: */*"



-d "{\"userId\":\"john.smith@dynatrace.com\",\"reason\":\"SUP-123456 Verifying cluster state after upgrade\",\"requestedDays\":7,\"role\":\"devops-admin\"}"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests
```

#### Request body

```
{



"userId": "john.smith@dynatrace.com",



"reason": "SUP-123456 Verifying cluster state after upgrade",



"requestedDays": 7,



"role": "devops-admin"



}
```

#### Response body

```
{



"requestId":"7a397770-86b7-473b-b23e-4a07d79f2eff",



"userId":"john.smith@dynatrace.com",



"reason":"SUP-123456 Verifying cluster state after upgrade",



"requestedDays":7,



"role":"devops-admin",



"createdTimestamp":1586452866661,



"expirationTimestamp":null,



"state":"PENDING",



"stateModifiedByUser":null



}
```

#### Response code

`201`
