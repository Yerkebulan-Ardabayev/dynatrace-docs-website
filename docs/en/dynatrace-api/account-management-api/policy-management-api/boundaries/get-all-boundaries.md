---
title: Policy management API - GET all policy boundaries
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-all-boundaries
scraped: 2026-02-23T21:36:50.152763
---

# Policy management API - GET all policy boundaries

# Policy management API - GET all policy boundaries

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Gets a list of policy boundaries within a level.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Optional |
| page | integer | - | query | Optional |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |

## Response

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| size | integer | - | query | Optional |
| page | integer | - | query | Optional |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |

## Example

In this example, the request retrieves all the policy boundaries that apply to the account with the `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**. Only the first three entries are returned.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890' \



--header 'accept: application/json' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890
```

#### Response body

```
{



"pageSize": 100,



"pageNumber": 1,



"totalCount": 22,



"content": [



{



"uuid": "a13f7b92-4c8e-4d3a-a1f7-9e3b6c2d8f01",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "Bnd1",



"boundaryQuery": "storage:dt.security_context = '${bindParam:bucket-name-param}';",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"${bindParam:bucket-name-param}"



]



}



],



"metadata": {}



},



{



"uuid": "345a2b02-678e-45ff-92c1-4b4fd5er3b0f",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd101",



"boundaryQuery": "storage:gcp.project.id = \"123\";",



"boundaryConditions": [



{



"name": "storage:gcp.project.id",



"operator": "EQ",



"values": [



"123"



]



}



],



"metadata": {}



},



{



"uuid": "a567b345-2345-4ab5-b8d1-0e9a65ae678f",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd101_alpha",



"boundaryQuery": "storage:dt.security_context = 'alpha';\n//storage:bucket-name = 'alpha';",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"alpha"



]



}



],



"metadata": {}



},



]



}
```

#### Response code

Success (200) - Successful response - list of policy boundaries