---
title: Delete user
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/delete-user
scraped: 2026-05-12T12:12:34.930433
---

# Delete user

# Delete user

* Published Sep 13, 2021

This API call deletes a cluster user.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/users`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | User ID path parameter. Missing or empty values will return a 'Bad Request'. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserConfig](#openapi-definition-UserConfig) | Successfully deleted |
| **304** | - | Not modified |
| **400** | - | No ID information received for the delete-user request |
| **406** | - | Unacceptable request |

### Response body objects

#### The `UserConfig` object

The configuration of the user.

| Element | Type | Description |
| --- | --- | --- |
| email | string | User's email address |
| firstName | string | User's first name |
| groups | string[] | List of user's user group IDs. |
| id | string | User ID |
| lastName | string | User's last name |
| passwordClearText | string | User's password in a clear text; used only to set initial password |

### Response body JSON models

```
{



"email": "string",



"firstName": "string",



"groups": [



"string"



],



"id": "string",



"lastName": "string",



"passwordClearText": "string"



}
```

## Example

In this example, you will delete the `john.wicked` user account. If the user account is deleted, you will receive details of the deleted user. If the user was removed previously, you will receive an empty response payload with code `200`.

#### Curl

```
curl -X DELETE "https://myManaged.cluster.com/api/v1.0/onpremise/users/john.wicked" -H  "accept: application/json"
```

#### Request URL

```
https://mymanaged.cluster.com/api/v1.0/onpremise/users/john.wicked
```

#### Response body

```
{



"id": "john.wicked",



"email": "john.wicked@company.com",



"firstName": "John",



"lastName": "Wicked",



"passwordClearText": null,



"groups": [



"admin"



]



}
```

#### Response code

`200`