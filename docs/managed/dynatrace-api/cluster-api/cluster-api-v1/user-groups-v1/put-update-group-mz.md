---
title: Update management zones for user group
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/put-update-group-mz
---

# Update management zones for user group

# Update management zones for user group

* Published Sep 13, 2021

This API call updates management zone permissions for a single user group.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups/managementZones`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [MzPermissionsForGroup](#openapi-definition-MzPermissionsForGroup) | - | body | Optional |

### Request body objects

#### The `MzPermissionsForGroup` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| groupId | string | Group ID | Optional |
| mzPermissionsPerEnvironment | [MzListForEnvironment](#openapi-definition-MzListForEnvironment)[] | List of management zone permissions per environment | Optional |

#### The `MzListForEnvironment` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| environmentUuid | string | Environment UUID | Optional |
| mzPermissions | [MzPermissionsList](#openapi-definition-MzPermissionsList)[] | List of management zone models with permissions | Optional |

#### The `MzPermissionsList` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| mzId | string | The ID of the required management zone | Optional |
| permissions | string[] | The list of permissions for the required management zone The element can hold these values * `DEMO_USER` * `LOG_VIEWER` * `MANAGE_SECURITY_PROBLEMS` * `MANAGE_SETTINGS` * `REPLAY_SESSION_DATA` * `REPLAY_SESSION_DATA_WITHOUT_MASKING` * `VIEWER` * `VIEW_SECURITY_PROBLEMS` * `VIEW_SENSITIVE_REQUEST_DATA` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"groupId": "string",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "string",



"mzPermissions": [



{



"mzId": "string",



"permissions": [



"DEMO_USER"



]



}



]



}



]



}
```

## Response

### Response codes

| Code | Description |
| --- | --- |
| **200** | Successfully updated |
| **400** | Provided model is incorrect or is missing required elements |
| **404** | A group, environment or management zone does not exist |
| **510** | Operation failed |

## Example

In this example, you update the `salesgroup` user group to assign permissions to `5c6cf54c-5fe3-47e8-af18-54439090370b` environment's
management zones.

#### Curl

```
curl -X 'PUT' \



'https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones' \



-H 'accept: */*' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP' \



-H 'Content-Type: application/json' \



-d '{



"groupId": "salesgroup",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "5c6cf54c-5fe3-47e8-af18-54439090370b",



"mzPermissions": [



{



"mzId": "-3223778520145835472",



"permissions": [



"REPLAY_SESSION_DATA",



"VIEWER",



"MANAGE_SECURITY_PROBLEMS",



"REPLAY_SESSION_DATA_WITHOUT_MASKING"



]



}



]



}



]



}'
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/groups/managementZones
```

#### Response body

No response body

#### Response code

`200`