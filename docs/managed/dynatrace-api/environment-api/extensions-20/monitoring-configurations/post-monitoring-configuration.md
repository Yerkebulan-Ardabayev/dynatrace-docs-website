---
title: Extensions 2.0 API - POST a monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/post-monitoring-configuration
---

# Extensions 2.0 API - POST a monitoring configuration

# Extensions 2.0 API - POST a monitoring configuration

* Reference
* Published Apr 07, 2021

Creates a new monitoring configuration for the specified Extensions 2.0 extension.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations` |

## Authentication

To execute this request, you need an access token with `extensionConfigurations.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | The name of the requested extension 2.0. | path | Required |
| body | [MonitoringConfigurationDto](#openapi-definition-MonitoringConfigurationDto)[] | JSON body of the request, containing monitoring configuration parameters. | body | Required |

### Request body objects

#### The `RequestBody` object

#### The `MonitoringConfigurationDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| scope | string | The scope this monitoring configuration will be defined for | Required |
| value | [JsonNode](#openapi-definition-JsonNode) | The monitoring configuration | Optional |

#### The `JsonNode` object

The monitoring configuration

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
[



{



"scope": "HOST-D3A3C5A146830A79",



"value": {}



}



]
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MonitoringConfigurationResponse](#openapi-definition-MonitoringConfigurationResponse)[] | Success |
| **207** | ([MonitoringConfigurationResponse](#openapi-definition-MonitoringConfigurationResponse) | [ErrorEnvelope](#openapi-definition-ErrorEnvelope))[] | Multi-Status, if not all requests resulted in the same status |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope)[] | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope)[] | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ResponseBody` object

#### The `MonitoringConfigurationResponse` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP Status code |
| objectId | string | The identifier of the new configuration |

#### The `ErrorResponseBody` object

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
[



{



"code": 1,



"objectId": "331e416f-9ab7-4694-8408-816026820645"



}



]
```

```
[



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



]
```

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")