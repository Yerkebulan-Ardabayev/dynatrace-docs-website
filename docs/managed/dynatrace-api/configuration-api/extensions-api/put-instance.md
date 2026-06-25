---
title: Extensions API - PUT an extension's instance
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/extensions-api/put-instance
scraped: 2026-05-12T11:20:06.469478
---

# Extensions API - PUT an extension's instance

# Extensions API - PUT an extension's instance

* Reference
* Published Mar 06, 2020

Updates properties of the specified instance of the extension.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/extensions/{id}/instances/{configurationId}` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the extension where you want to update the configuration.  If you set the extension ID in the body as well, it must match this ID. | path | Required |
| configurationId | string | The ID of the configuration to be updated. | path | Required |
| body | [ExtensionConfigurationDto](#openapi-definition-ExtensionConfigurationDto) | The JSON body of the request. Contains updated parameters of the extension configuration. | body | Optional |

### Request body objects

#### The `ExtensionConfigurationDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| activeGate | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | The short representation of a Dynatrace entity. | Optional |
| enabled | boolean | The extension is enabled (`true`) or disabled (`false`). | Required |
| endpointId | string | The ID of the endpoint. | Optional |
| endpointName | string | The name of the endpoint, displayed in Dynatrace. | Optional |
| extensionId | string | The ID of the extension. | Optional |
| hostId | string | The ID of the host on which the extension runs. | Optional |
| properties | object | The list of extension parameters.  Each parameter is a key-value pair. | Optional |
| useGlobal | boolean | Allows to skip current configuration and use global one. | Required |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| description | string | A short description of the Dynatrace entity. | Optional |
| id | string | The ID of the Dynatrace entity. | Required |
| name | string | The name of the Dynatrace entity. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"activeGate": {



"id": "7835970235169136995",



"name": "ActiveGate Host Name"



},



"enabled": true,



"hostId": "HOST-01A7DEFA5340A86D",



"id": "custom.remote.python.demo",



"properties": {



"dropdownProperty": "three",



"password": "",



"serverIp": "127.0.0.1",



"username": "dynatrace"



},



"useGlobal": false



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

### Response body objects

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