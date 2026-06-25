---
title: Extensions 2.0 API - DELETE an extension version
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/del-version
scraped: 2026-05-12T11:56:32.722591
---

# Extensions 2.0 API - DELETE an extension version

# Extensions 2.0 API - DELETE an extension version

* Reference
* Published Jan 22, 2021

Deletes the specified version of an Extensions 2.0 extension.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| DELETE | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}` |
| DELETE | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions/{extensionName}/{extensionVersion}` |

## Authentication

To execute this request, you need an access token with `extensions.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| extensionName | string | The name of the requested extension 2.0. | path | Required |
| extensionVersion | string | The version of the requested extension 2.0 | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Extension](#openapi-definition-Extension) | Success. The extension 2.0 version has been deleted. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Extension` object

| Element | Type | Description |
| --- | --- | --- |
| author | [AuthorDto](#openapi-definition-AuthorDto) | Extension author |
| dataSources | string[] | Data sources that extension uses to gather data |
| extensionName | string | Extension name |
| featureSets | string[] | Available feature sets |
| featureSetsDetails | object | Details of feature sets |
| fileHash | string | SHA-256 hash of uploaded Extension file |
| minDynatraceVersion | string | Minimal Dynatrace version that works with the extension |
| minEECVersion | string | Minimal Extension Execution Controller version that works with the extension |
| variables | string[] | Custom variables used in extension configuration |
| version | string | Extension version |

#### The `AuthorDto` object

Extension author

| Element | Type | Description |
| --- | --- | --- |
| name | string | Author name |

#### The `FeatureSetDetails` object

Additional information about a Feature Set

| Element | Type | Description |
| --- | --- | --- |
| description | string | Optional description for the feature set |
| displayName | string | Optional display name of the feature set |
| isRecommended | boolean | Marks the feature set as recommended (selected by default during activation) |
| metrics | [MetricDto[]](#openapi-definition-MetricDto) | Feature set metrics |

#### The `MetricDto` object

Metric gathered by an extension

| Element | Type | Description |
| --- | --- | --- |
| key | string | Metric key |
| metadata | [MetricMetadataDto](#openapi-definition-MetricMetadataDto) | Metric metadata |

#### The `MetricMetadataDto` object

Metric metadata

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the metric |
| displayName | string | The name of the metric in the user interface |
| unit | string | The unit of the metric |

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



"author": {



"name": "string"



},



"dataSources": [



"string"



],



"extensionName": "string",



"featureSets": [



"string"



],



"featureSetsDetails": {},



"fileHash": "string",



"minDynatraceVersion": "string",



"minEECVersion": "string",



"variables": [



"string"



],



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