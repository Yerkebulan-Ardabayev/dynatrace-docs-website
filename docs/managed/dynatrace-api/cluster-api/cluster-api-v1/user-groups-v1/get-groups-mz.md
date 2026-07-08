---
title: Get management zones for user groups
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/user-groups-v1/get-groups-mz
---

# Get management zones for user groups

# Get management zones for user groups

* Published Sep 13, 2021

This API call retrieves information on a management zone permissions for all user groups.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/groups/managementZones`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| includeEmptyEntries | boolean | Should include empty entries in response | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MzPermissionsForGroup](#openapi-definition-MzPermissionsForGroup)[] | Success |

### Response body objects

#### The `ResponseBody` object

#### The `MzPermissionsForGroup` object

| Element | Type | Description |
| --- | --- | --- |
| groupId | string | Group ID |
| mzPermissionsPerEnvironment | [MzListForEnvironment](#openapi-definition-MzListForEnvironment)[] | List of management zone permissions per environment |

#### The `MzListForEnvironment` object

| Element | Type | Description |
| --- | --- | --- |
| environmentUuid | string | Environment UUID |
| mzPermissions | [MzPermissionsList](#openapi-definition-MzPermissionsList)[] | List of management zone models with permissions |

#### The `MzPermissionsList` object

| Element | Type | Description |
| --- | --- | --- |
| mzId | string | The ID of the required management zone |
| permissions | string[] | The list of permissions for the required management zone The element can hold these values * `DEMO_USER` * `LOG_VIEWER` * `MANAGE_SECURITY_PROBLEMS` * `MANAGE_SETTINGS` * `REPLAY_SESSION_DATA` * `REPLAY_SESSION_DATA_WITHOUT_MASKING` * `VIEWER` * `VIEW_SECURITY_PROBLEMS` * `VIEW_SENSITIVE_REQUEST_DATA` |

### Response body JSON models

```
[



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



]
```

## Example

In this example, you retrieve management zones for all user groups.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/groups/managementZones' \



-H 'accept: application/json' \



-H 'Authorization: Api-Token FG563.LKJHDFLKJHDFHLKJDGV.ABCDEFGHJKLMNOP'
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/onpremise/groups/managementZones
```

#### Response body

```
[



{



"groupId": "aaa",



"mzPermissionsPerEnvironment": [



{



"environmentUuid": "4667c7df-c41a-800a-2c81-3c789c24faac",



"mzPermissions": []



},



{



"environmentUuid": "702822e6-c4d5-98b6-68f0-2fa6e916d83a",



"mzPermissions": [



{



"mzId": "1082937102825552837",



"permissions": []



},



{



"mzId": "3256863855844402130",



"permissions": []



},



{



"mzId": "9010752233197751135",



"permissions": []



},



{



"mzId": "6704521539267660126",



"permissions": []



},



{



"mzId": "9988288124425157928",



"permissions": []



},



{



"mzId": "3762222045561554923",



"permissions": []



}



]



},



{



"environmentUuid": "ff484b4b-4391-109e-429f-ce16dac3325a",



"mzPermissions": []



},



{



"environmentUuid": "a3d7fa42-a74d-ebd6-8aee-003b6c2abd6f",



"mzPermissions": []



},



{



"environmentUuid": "75188d7f-4e59-d4d3-c1ab-cb6eb5a095b8",



"mzPermissions": [



{



"mzId": "3695265796834015735",



"permissions": []



}



]



},



{



"environmentUuid": "560db49c-c2f5-8d41-3811-1623e4c4dd17",



"mzPermissions": []



},



{



"environmentUuid": "96cfb5d9-94e9-e5a3-96e6-b4ecced9f0ec",



"mzPermissions": []



},



{



"environmentUuid": "7e6cb304-79c5-6b90-9168-60f16deb1b00",



"mzPermissions": [



{



"mzId": "6978718201709411367",



"permissions": []



},



{



"mzId": "1884001224662458062",



"permissions": []



}



]



}



]



}



]
```

#### Response code

`200`