---
title: "Get all cluster access requests"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-all-cluster-access-requests
updated: 2026-02-09
---

# Get all cluster access requests

# Get all cluster access requests

* Published Apr 02, 2020

This API call gets a list of all current cluster access requests, including user, access role, access duration, and state of the request.

## Authentication

To execute this request, you need one of the following API-Token scopes:

* **Cluster token management** (`ClusterTokenManagement`)
* **Service Provider API** (`ServiceProviderAPI` )
* Nodekeeper access for node management (`Nodekeeper`)  
  To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/remoteaccess/requests`

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AccessRequestData[]](#openapi-definition-AccessRequestData) | Successful |
| **403** | - | Approving remote access request is disabled |

### Response body objects

#### The `ResponseBody` object

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
[



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



]
```

## Example

In this example you request a cluster (`myManaged.cluster.com`) to return a list of all current remote access requests.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests"



-H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests
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

`200`
