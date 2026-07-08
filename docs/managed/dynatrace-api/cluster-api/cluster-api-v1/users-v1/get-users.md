---
title: Get users
source: https://docs.dynatrace.com/managed/dynatrace-api/cluster-api/cluster-api-v1/users-v1/get-users
---

# Get users

# Get users

* Published Sep 13, 2021

This API call retrieves a list of cluster users that currently exist in cluster.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Tokens and authentication](/managed/dynatrace-api/cluster-api/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/v1.0/onpremise/users`

## Parameter

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [UserConfig](#openapi-definition-UserConfig)[] | Success |

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

In this example, you retrieve all users that currently exist in your Dynatrace Managed cluster. For each user, you get a detailed information and groups membership.

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/v1.0/onpremise/users" -H  "accept: application/json"
```

#### Request URL

```
https://myManaged.cluster.com/api/v1.0/onpremise/users
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