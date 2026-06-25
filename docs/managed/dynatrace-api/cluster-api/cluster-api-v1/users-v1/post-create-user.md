---
title: Create user
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-user
scraped: 2026-05-12T12:13:01.851525
---

# Create user

# Create user

* Published Sep 13, 2021

This API call creates a cluster user account.

## Authentication

The `ServiceProviderAPI` (Service Provider API) Api-Token scope is required to get the default realm password policy configuration using the Dynatrace API. With this API method, you can preset user's password by passing `passwordClearText` value. This is allowed only if a specific Feature Flag is enabled. To do this, Please contact a Dynatrace product expert via live chat within your environment..

## Endpoint

`/api/v1.0/onpremise/users`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [UserConfig](#openapi-definition-UserConfig) | The JSON body of the request, containing parameters of the user. | body | Optional |

### Request body objects

#### The `UserConfig` object

The configuration of the user.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| email | string | User's email address | Required |
| firstName | string | User's first name | Required |
| groups | string[] | List of user's user group IDs. | Optional |
| id | string | User ID | Required |
| lastName | string | User's last name | Required |
| passwordClearText | string | User's password in a clear text; used only to set initial password | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserConfig](#openapi-definition-UserConfig) | Successfully created |
| **400** | - | Operation failed. The input is invalid. Possible reasons:  * all required values (ID, email, first name, last name) must be set * invalid user data * user ID already exists * user email address already assigned * user group ID does not exist |
| **403** | - | Operation forbidden - users and groups are fully managed via LDAP or SSO |
| **406** | - | Unacceptable request |
| **522** | - | Couldn't create user |
| **523** | - | User already exists |
| **524** | - | Email address already registered |

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

In this example, you add `john.wicked` user and assign `admins` group. As a response, you will receive back persisted state of the entity.

#### Curl

```
curl -X PUT "https://myManaged.cluster.com/api/v1.0/onpremise/users" -H  "accept: application/json" -H  "Content-Type: application/json" -d "{\"id\":\"john.wicked\",\"email\":\"john.wicked@company.com\",\"firstName\":\"John\",\"lastName\":\"Wicked\",\"passwordClearText\":null,\"groups\":[\"admin\"]}"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/users
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