---
title: "Get cluster access request"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/remote-access/get-cluster-access-request
updated: 2026-02-09
---

# Get cluster access request

# Get cluster access request

* Published Apr 02, 2020

This API call gets cluster access request information for a specific request access ID. The request produces an `application/json` payload.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [AccessRequestData](#openapi-definition-AccessRequestData) | Successful |
| **400** | - | Bad request |
| **403** | - | Approving remote access request is disabled |
| **404** | - | Not found |

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

In this example, you request to list remote access permission for a specific request access ID (`7a397770-86b7-473b-b23e-4a07d79f2eff`). In return, you receive a JSON response that indicates that the request ID `7a397770-86b7-473b-b23e-4a07d79f2eff` is for user `john.smith@dynatrace.com` that has remote access permission with admin role for `7` days and the reason is to verify cluster state after upgrade.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff"



-H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/remoteaccess/requests/7a397770-86b7-473b-b23e-4a07d79f2eff
```

#### Response body

```
{



"requestId": "7a397770-86b7-473b-b23e-4a07d79f2eff",



"userId": "john.smith@dynatrace.com",



"reason": "SUP-123456 Verifying cluster state after upgrade",



"requestedDays": 7,



"role": "devops-admin",



"createdTimestamp": 1586452866661,



"expirationTimestamp": 1587081600000,



"state": "ACCEPTED",



"stateModifiedByUser": "katie.novak"



}
```

#### Response code

`200`
