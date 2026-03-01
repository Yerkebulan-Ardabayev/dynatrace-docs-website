---
title: Policy management API - POST a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary
scraped: 2026-03-01T21:21:06.342864
---

# Policy management API - POST a policy boundary

# Policy management API - POST a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Creates a new policy boundary within a level. You can't create a global-level boundary, as these are managed by Dynatrace.

The request consumes and produces an `application/json` payload.

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains new policy boundary | body | Required |

### Request body objects

#### The `PolicyBoundaryDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy boundary. | Required |
| boundaryQuery | string | The boundary query of the policy boundary. | Required |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. | Required |

#### The `Map` object

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Successful response - policy boundary created |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The request is invalid |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **200** indicates a valid payload.

The request consumes an `application/json` payload.

### Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains new policy boundary | body | Required |

### Request body objects

#### The `PolicyBoundaryDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy boundary. | Required |
| boundaryQuery | string | The boundary query of the policy boundary. | Required |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. | Required |

#### The `Map` object

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Example

In this example, the request creates a new policy boundary within a level. It a new policy boundary for the `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request POST \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries \



--header 'accept: application/json' \



--header 'Authorization: Bearer abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "name_string",



"boundaryQuery": "boundaryQuery",



"metadata": {}



}'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries
```

#### Request body

```
{



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"metadata": {}



}
```

#### Response body

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-AA"



]



}



],



"metadata": {}



}
```

#### Response code

201 - Successful response - policy boundary created.