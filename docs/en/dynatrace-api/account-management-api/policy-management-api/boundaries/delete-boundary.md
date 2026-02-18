---
title: Policy management API - DELETE a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/delete-boundary
scraped: 2026-02-18T05:43:52.935853
---

# Policy management API - DELETE a policy boundary

# Policy management API - DELETE a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Deletes a policy boundary by uuid within a level. You can't delete a global-level boundary, as these are managed by Dynatrace.

DELETE

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
| **204** | - | Successful response - policy boundary deleted |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The request is invalid |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Example

In this example, the request deletes a policy boundary with policy boundary `UUID` of **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** for the `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request DELETE \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345 \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Response code

204 - Successful response - policy boundary deleted.