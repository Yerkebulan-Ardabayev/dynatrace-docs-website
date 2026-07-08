---
title: Environment management API - GET all environments of an account
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/environment-management-api/environment-management-api
---

# Environment management API - GET all environments of an account

# Environment management API - GET all environments of an account

* Reference
* Published Jul 25, 2022

Lists all environments and [management zones](/managed/manage/identity-access-management/permission-management/management-zones "Learn about management zones concepts, how to define management zones, and how to make the most of them.") of an account.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/env/v1/accounts/{accountUuid}/environments` |

## Authentication

To execute this request, you need the **Allow read access for environment resources** (`account-env-read`) scope assigned to your token. To learn how to obtain and use it.

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EnvironmentResourceDto](#openapi-definition-EnvironmentResourceDto) | Success. The response contains a list of the account's environments. |

### Response body objects

#### The `EnvironmentResourceDto` object

| Element | Type | Description |
| --- | --- | --- |
| tenantResources | [TenantResourceDto](#openapi-definition-TenantResourceDto)[] | A list of environments in the account. |
| managementZoneResources | [ManagementZoneResourceDto](#openapi-definition-ManagementZoneResourceDto)[] | A list of management zones in the account. |

#### The `TenantResourceDto` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the environment. |
| id | string | The ID of the environment. |

#### The `ManagementZoneResourceDto` object

| Element | Type | Description |
| --- | --- | --- |
| parent | string | The ID of the environment to which the management zone belongs. |
| name | string | The name of the management zone. |
| id | string | The ID of the management zone. |

### Response body JSON models

```
{



"tenantResources": [



{



"name": "string",



"id": "string"



}



],



"managementZoneResources": [



{



"parent": "string",



"name": "string",



"id": "string"



}



]



}
```

## Example

In this example, the request lists all environments and management zones of the account with the UUID of **9ad20784-76c6-4167-bfba-9b0d8d72a71d**.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/env/v1/accounts/9ad20784-76c6-4167-bfba-9b0d8d72a71d/environments' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/env/v1/accounts/9ad20784-76c6-4167-bfba-9b0d8d72a71d/environments
```

#### Response body

```
{



"tenantResources": [



{



"name": "Sample environment",



"id": "mySampleEnv"



},



{



"name": "Sample environment - staging",



"id": "mySampleEnvStaging"



}



],



"managementZoneResources": [



{



"name": "mobile app only",



"id": "154240256445017454",



"parent": "mySampleEnv"



},



{



"name": "load tests only",



"id": "144245256741917454",



"parent": "mySampleEnvStaging"



}



]



}
```

#### Response code

200