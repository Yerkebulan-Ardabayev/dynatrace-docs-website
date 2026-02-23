---
title: Policy management API - GET a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-boundary
scraped: 2026-02-23T21:34:13.687045
---

# Policy management API - GET a policy boundary

# Policy management API - GET a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Gets a policy boundary within a level.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | The ID of the required boundary. | path | Required |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Successful response - policy boundary |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `PolicyBoundaryOverview` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | The display name of the policy boundary. |
| boundaryQuery | string | The boundary query of the policy boundary. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. |

#### The `Condition` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the condition.  It indicates which part of the **services** is checked by the condition. |
| operator | string | The operator of the condition. |
| values | string[] | A list of reference values of the condition. |

#### The `Map` object

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"uuid": "string",



"levelType": "string",



"levelId": "string",



"name": "string",



"boundaryQuery": "string",



"boundaryConditions": [



{



"name": "string",



"operator": "string",



"values": [



"string"



]



}



],



"metadata": {}



}
```

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Example

In this example, the request retrieves the details of the policy boundary with the UUID of **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** for the account with the `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Response body

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bndry_teamA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AB\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-A"



]



}



],



"metadata": {}



}
```

#### Response code

200 - Successful response - policy boundary.