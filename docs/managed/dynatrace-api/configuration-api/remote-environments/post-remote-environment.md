---
title: Remote environments API - POST a remote environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/remote-environments/post-remote-environment
---

# Remote environments API - POST a remote environment configuration

# Remote environments API - POST a remote environment configuration

* Reference
* Published Nov 19, 2019

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") instead. Look for the **Remote environment** (`builtin:remote.environment`) schema.

Creates a new remote environment configuration.

Before creation, Dynatrace verifies the provided URI and token by trying to reach the environment using the token for authentication. If the attempt fails, no remote environment configuration is created.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The body must not provide an ID. An ID is assigned automatically by Dynatrace.

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [RemoteEnvironmentConfigDto](#openapi-definition-RemoteEnvironmentConfigDto) | The JSON body of the request. Contains parameters of the new remote environment configuration. | body | Optional |

### Request body objects

#### The `RemoteEnvironmentConfigDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| displayName | string | The display name of the remote environment. | Required |
| id | string | The ID of the configuration. | Optional |
| networkScope | string | The network scope of the remote environment:  * `EXTERNAL`: The remote environment is located in an another network. * `INTERNAL`: The remote environment is located in the same network. * `CLUSTER`: The remote environment is located in the same cluster.  Dynatrace SaaS can only use `EXTERNAL`.  If not set, `EXTERNAL` is used. The element can hold these values * `CLUSTER` * `EXTERNAL` * `INTERNAL` | Optional |
| token | string | The API token granting access to the remote environment.  The token must have the **Fetch data from a remote environment** (`RestRequestForwarding`) scope.  For security reasons, GET requests return this field as `null`. | Optional |
| uri | string | The URI of the remote environment. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"displayName": "string",



"id": "string",



"networkScope": "EXTERNAL",



"token": "string",



"uri": "string"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [RemoteEnvironmentConfigStub](#openapi-definition-RemoteEnvironmentConfigStub) | Success. A new remote environment configuration has been created. The response contains the ID of the new configuration. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `RemoteEnvironmentConfigStub` object

The short representation of a remote environment.

| Element | Type | Description |
| --- | --- | --- |
| id | string | - |
| name | string | - |
| networkScope | string | The network scope of the remote environment:  * `EXTERNAL`: The remote environment is located in an another network. * `INTERNAL`: The remote environment is located in the same network. * `CLUSTER`: The remote environment is located in the same cluster.  Dynatrace SaaS can only use `EXTERNAL`.  If not set, `EXTERNAL` is used. The element can hold these values * `CLUSTER` * `EXTERNAL` * `INTERNAL` |
| uri | string | The display name of the remote environment. |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### Response body JSON models

```
{



"id": "string",



"name": "string",



"networkScope": "CLUSTER",



"uri": "string"



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/remoteEnvironments/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted configuration is valid. Response doesn't have a body |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation](#openapi-definition-ConstraintViolation)[] | A list of constraint violations |
| message | string | The error message |

#### The `ConstraintViolation` object

A list of constraint violations

| Element | Type | Description |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -The element can hold these values * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

#### Response body JSON models

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Example

In this example, the request creates a new remote environment configuration, referring to the **Pre-Production** environment.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/ \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"displayName": "Pre-Production",



"uri": "https://preProd.live.dynatrace.com",



"token": "1234567890abcdefjhij",



"networkScope": "EXTERNAL"



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/remoteEnvironments/
```

#### Request body

```
{



"displayName": "Pre-Production",



"uri": "https://PreProd.live.dynatrace.com",



"token": "1234567890abcdefjhij",



"networkScope": "INTERNAL"



}
```

#### Response body

```
{



"id": "c89b9d9f-8c59-4c5b-b7ef-1a082d11e9ba",



"name": "Pre-Production",



"uri": "https://preProd.live.dynatrace.com",



"networkScope": "EXTERNAL"



}
```

#### Response code

201