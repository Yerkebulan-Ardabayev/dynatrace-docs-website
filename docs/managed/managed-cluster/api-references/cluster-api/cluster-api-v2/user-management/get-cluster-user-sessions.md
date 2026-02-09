---
title: "Get cluster user sessions"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/get-cluster-user-sessions
updated: 2026-02-09
---

# Get cluster user sessions

# Get cluster user sessions

* Published Apr 02, 2020

This API call gets users sessions based on a specific user ID. You can request a list of user sessions for a specific user ID in a specific environment.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/userSessions`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| userId | string | User ID (optional) | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserSession[]](#openapi-definition-UserSession) | Success |
| **500** | - | Operation failed |

### Response body objects

#### The `ResponseBody` object

#### The `UserSession` object

Managed user session instance

| Element | Type | Description |
| --- | --- | --- |
| creationTime | integer | User session creation timestamp |
| device | string | Device on which user has logged in |
| ip | string | IP from which has logged in |
| lastAccessedTimestamp | integer | Timestamp when session was recently accessed |
| loginType | string | The way user has logged in The element can hold these values * `LOCAL` * `LDAP` * `SSO_MANAGED` * `DEVOPSTOKEN` |
| nodeId | integer | Node on which user session exists |
| sessionId | string | User session id |
| tenantUuid | string | UUID of tenant to which user has logged in (or cluster UUID if user has logged in to CMC) |
| userId | string | User id |

### Response body JSON models

```
[



{



"creationTime": 1,



"device": "string",



"ip": "string",



"lastAccessedTimestamp": 1,



"loginType": "LOCAL",



"nodeId": 1,



"sessionId": "string",



"tenantUuid": "string",



"userId": "string"



}



]
```

## Example

In this example, the request lists user sessions in the `myManaged.cluster.com` cluster for user `user.name`.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name"



-H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name
```

#### Response body

```
[



{



"userId": "user.name",



"nodeId": 4,



"sessionId": "string",



"creationTime": 0,



"lastAccessedTimestamp": 0,



"tenantUuid": "string",



"loginType": "LOCAL",



"device": "string",



"ip": "string"



}



]
```

#### Response code

`200`
