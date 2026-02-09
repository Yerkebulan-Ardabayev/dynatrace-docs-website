---
title: "Delete user sessions of a given user"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/user-management/delete-cluster-user-session
updated: 2026-02-09
---

# Delete user sessions of a given user

# Delete user sessions of a given user

* Published Apr 02, 2020

This API call enables you to terminate all sessions of a specific user.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/userSessions`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| userId | string | User ID (mandatory) | query | Optional |

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Success |
| **400** | Bad request. User id must be filled in. |
| **404** | User sessions not found |
| **500** | Operation failed |
| **510** | Failed to invalidate sessions |

## Example

In this example, the request deletes all user sessions with user ID value `user.name`. The response code of `200` indicates that the deletion was successful.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name" -H  "accept: */*"
```

#### Request URL

```
https://myManaged.cluster.com/api/cluster/v2/userSessions?userId=user.name
```

#### Response code

`200`
