---
title: Create cluster user accounts
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/post-create-users
scraped: 2026-05-12T12:12:39.936973
---

# Create cluster user accounts

# Create cluster user accounts

* Published Sep 13, 2021

This API call creates multiple cluster user accounts.

## Authentication

The `ServiceProviderAPI` (Service Provider API) Api-Token scope is required to get the default realm password policy configuration using the Dynatrace API. With this API method, you can preset user's password by passing `passwordClearText` value. This is allowed only if a specific Feature Flag is enabled. To do this, Please contact a Dynatrace product expert via live chat within your environment..

## Endpoint

`/api/v1.0/onpremise/users/bulk`

## Parameter

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [UserConfig[]](#openapi-definition-UserConfig) | The JSON body of the request, containing parameters of the users. | body | Optional |

### Request body objects

#### The `RequestBody` object

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
[



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



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserConfig[]](#openapi-definition-UserConfig) | Success |
| **400** | - | Operation failed. The input is invalid. Possible reasons:  * no user information received for the create-users request * all required values (ID, email, first name, last name) must be set * invalid user data * input contains duplicated IDs * input contains duplicated email addresses * user ID already exists * user email address already assigned * user group ID does not exist |
| **403** | - | Operation forbidden - either LDAP or SSO with group assignment integration is turned on |
| **406** | [UserConfig[]](#openapi-definition-UserConfig) | Unacceptable or incomplete request. Some users added |

### Response body objects

#### The `ResponseBody` object

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
[



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



]
```

## Example

In this example, we add two users - `john.wicked` and `ann.brown` in a single request. This will set their data and assign individually group memberships. As a response, you will receive back persisted state of the entities.

#### Curl

```
curl -X POST "https://myManaged.cluster.com/api/v1.0/onpremise/users/bulk" -H  "accept: application/json" -H  "Content-Type: application/json" -d "[{\"id\":\"john.wicked\",\"email\":\"john.wicked@company.com\",\"firstName\":\"John\",\"lastName\":\"Wicked\",\"passwordClearText\":null,\"groups\":[\"owners\",\"users\"]},{\"id\":\"anne.brown\",\"email\":\"anne.brown@company.com\",\"firstName\":\"Anne\",\"lastName\":\"Brown\",\"passwordClearText\":null,\"groups\":[\"users\"]}]"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/users/bulk
```

#### Response body

```
[



{



"id": "john.wicked",



"email": "john.wicked@company.com",



"firstName": "John",



"lastName": "Wicked",



"passwordClearText": null,



"groups": [



"owners",



"users"



]



},



{



"id": "anne.brown",



"email": "anne.brown@company.com",



"firstName": "Anne",



"lastName": "Brown",



"passwordClearText": null,



"groups": ["users"]



}



]
```

#### Response code

`200`