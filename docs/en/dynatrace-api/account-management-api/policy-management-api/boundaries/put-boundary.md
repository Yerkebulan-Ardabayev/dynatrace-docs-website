---
title: Policy management API - PUT a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/put-boundary
scraped: 2026-02-16T09:32:15.838619
---

# Policy management API - PUT a policy boundary

# Policy management API - PUT a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Updates or creates a policy boundary by uuid within a level. You can't edit a global-level boundary, as these are managed by Dynatrace.

If the specified boundary doesn't exist, a [new boundary is created](/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary "Create a new boundary via the Policy management API.") instead.

The request consumes and produces an `application/json` payload.

PUT

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | The ID of the required boundary. | path | Required |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains policy boundary | body | Required |

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
| **204** | - | Successful response - policy boundary updated |
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

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}/validation/{policyUuid}`

### Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyUuid | - | The ID of the policy to be validated. | path | Required |
| levelId | - | The ID of the policy level. Use one of the following values, depending on the level type:  * account: use the UUID of the account. * environment: use the ID of the environment. | path | Required |
| levelType | - | The type of the [policyï»¿](https://dt-url.net/eu03uap) level. The following values are available:  * `account`: An account policy applies to all environments of an account. * `environment`: An environment policy applies to a specific environment.  Each level inherits the policies of the higher level and extends them with its own policies. | path | Required |
| body | [CreateOrUpdateLevelPolicyRequestDto](#openapi-definition-CreateOrUpdateLevelPolicyRequestDto) | The JSON body of the request. Contains the configuration of a policy to be validated. | body | Required |

### Request body objects

#### The `CreateOrUpdateLevelPolicyRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy. | Required |
| description | string | A short description of the policy. | Required |
| tags | string[] | A list of tags. | Optional |
| statementQuery | string | The [statementï»¿](https://dt-url.net/ht03ucb) of the policy. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"description": "string",



"tags": [



"string"



],



"statementQuery": "string"



}
```

## Example

In this example, the request updates the `name` of the policy boundary with `UUID` of **3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68** for the account with the `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request PUT \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68 \



--header 'Authorization: Bearer abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "host name",



"description": "storage:host.name = \"myHost\"",



"metadata": {}



}'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68
```

#### Request body

```
{



"name": "host name",



"boundaryQuery": "storage:host.name = \"myHost\";",



"metadata": {}



}
```

#### Response code

204 - Successful response - policy boundary updated.