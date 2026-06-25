---
title: Extensions 2.0 API - GET active
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/environment-configurations/get-environment-configuration
scraped: 2026-05-12T11:56:07.142652
---

# Extensions 2.0 API - GET active

# Extensions 2.0 API - GET active

* Reference
* Published Jan 22, 2021

Gets the active environment configuration version of the specified Extensions 2.0 extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/environmentConfiguration` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `extensionEnvironment.read`
* `extensions.read`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | The name of the requested extension 2.0. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionEnvironmentConfigurationVersion](#openapi-definition-ExtensionEnvironmentConfigurationVersion) | Success |
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