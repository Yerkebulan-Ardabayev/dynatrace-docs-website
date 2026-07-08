---
title: Synthetic configuration API v2 - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/put-configuration
---

# Synthetic configuration API v2 - PUT configuration

# Synthetic configuration API v2 - PUT configuration

* Reference
* Updated on Sep 28, 2022

Updates the configuration of Synthetic monitoring in your environment.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/synthetic/config` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/synthetic/config` |

## Authentication

To execute this request, you need an access token with `syntheticLocations.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SyntheticConfigDto](#openapi-definition-SyntheticConfigDto) | A DTO for synthetic configuration. | body | Required |

### Request body objects

#### The `SyntheticConfigDto` object

A DTO for synthetic configuration.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| bmMonitorTimeout | integer | bmMonitorTimeout - browser monitor execution timeout (ms) | Required |
| bmStepTimeout | integer | bmStepTimeout - browser monitor single step execution timeout (ms) | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"bmMonitorTimeout": 1,



"bmStepTimeout": 1



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | [SyntheticConfigDto](#openapi-definition-SyntheticConfigDto) | Success. The set of synthetic related parameters has been updated. Response doesn't have a body. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

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

In this example, the request updates the configuration of the Synthetic monitoring from the [GET request](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-configuration-v2/get-configuration#example "View the configuration of Synthetic monitoring via the Synthetic API v2.") example. It halves the timeouts for browser monitor and browser monitor steps—setting them to `300,000` and `30,000` respectively.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to create a backup copy of your current configuration with the **GET Synthetic configuration** call.

#### Curl

```
curl --request PUT \



--url https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/config \



--header 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"bmMonitorTimeout": 300000,



"bmStepTimeout": 30000



}'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/config
```

#### Request body

```
{



"bmMonitorTimeout": 300000,



"bmStepTimeout": 30000



}
```

#### Response code

204

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")