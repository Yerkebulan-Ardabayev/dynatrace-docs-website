---
title: Extensions 2.0 API - PUT a monitoring configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/monitoring-configurations/put-monitoring-configuration
scraped: 2026-05-12T11:56:21.020617
---

# Extensions 2.0 API - PUT a monitoring configuration

# Extensions 2.0 API - PUT a monitoring configuration

* Reference
* Published Apr 07, 2021

Updates the specified monitoring configuration of an Extensions 2.0 extension.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/monitoringConfigurations/{configurationId}` |

## Authentication

To execute this request, you need an access token with `extensionConfigurations.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | The name of the requested extension 2.0. | path | Required |
| configurationId | string | The ID of the requested monitoring configuration. | path | Required |
| body | [MonitoringConfigurationUpdateDto](#openapi-definition-MonitoringConfigurationUpdateDto) | JSON body of the request, containing monitoring configuration parameters. | body | Required |

### Request body objects

#### The `MonitoringConfigurationUpdateDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| value | [JsonNode](#openapi-definition-JsonNode) | The monitoring configuration | Optional |

#### The `JsonNode` object

The monitoring configuration

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"value": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [MonitoringConfigurationResponse](#openapi-definition-MonitoringConfigurationResponse) | Success |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `MonitoringConfigurationResponse` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP Status code |
| objectId | string | The identifier of the new configuration |

#### The `ErrorEnvelope` object

| Element | Type | Description |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### The `Error` object

| Element | Type | Description |
| --- | --- | --- |
| code | integer | The HTTP status code |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | A list of constraint violations |
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



"code": 1,



"objectId": "331e416f-9ab7-4694-8408-816026820645"



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

## Related topics

* [Develop your own Extensions](/managed/ingest-from/extensions/develop-your-extensions "Develop your own Extensions in Dynatrace.")