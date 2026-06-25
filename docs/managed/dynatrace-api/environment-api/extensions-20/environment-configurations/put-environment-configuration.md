---
title: Extensions 2.0 API - PUT environment configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/environment-configurations/put-environment-configuration
scraped: 2026-05-12T11:56:28.995158
---

# Extensions 2.0 API - PUT environment configuration

# Extensions 2.0 API - PUT environment configuration

* Reference
* Published Jan 22, 2021

Activates the specified version of an Extensions 2.0 extension.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |
| PUT | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `extensionEnvironment.write`
* `extensions.write`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | The name of the requested extension 2.0. | path | Required |
| body | [ExtensionEnvironmentConfigurationVersion](#openapi-definition-ExtensionEnvironmentConfigurationVersion) | The version of the requested environment configuration. | body | Required |

### Request body objects

#### The `ExtensionEnvironmentConfigurationVersion` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| version | string | Extension version | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"version": "1.2.3"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionEnvironmentConfigurationVersion](#openapi-definition-ExtensionEnvironmentConfigurationVersion) | Success. Environment configuration updated. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ExtensionEnvironmentConfigurationVersion` object

| Element | Type | Description |
| --- | --- | --- |
| version | string | Extension version |

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



"version": "1.2.3"



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