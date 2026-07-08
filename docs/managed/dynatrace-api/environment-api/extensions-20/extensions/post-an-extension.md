---
title: Extensions 2.0 API - POST an extension file
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/extensions-20/extensions/post-an-extension
---

# Extensions 2.0 API - POST an extension file

# Extensions 2.0 API - POST an extension file

* Reference
* Published Jan 22, 2021

Uploads an Extensions 2.0 extension file to your Dynatrace environment.

The request consumes an `application/octet-stream` payload and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/extensions` |
| POST | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/extensions` |

## Authentication

To execute this request, you need an access token with `extensions.write` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| validateOnly | boolean | Validate and store (`false`) or just validate (`true`) the uploaded extension file.  If not set, `false` is used. | query | Optional |

### Request body

Extension 2.0 package file (`*.zip`) to be uploaded.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ExtensionUploadResponseDto](#openapi-definition-ExtensionUploadResponseDto) | The extension is valid |
| **201** | [ExtensionUploadResponseDto](#openapi-definition-ExtensionUploadResponseDto) | Success. The extension 2.0 has been uploaded. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input file is invalid. |
| **409** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Upload not possible yet, please try again in a few seconds. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ExtensionUploadResponseDto` object

| Element | Type | Description |
| --- | --- | --- |
| assetsInfo | [AssetInfo](#openapi-definition-AssetInfo)[] | Information about extension assets included |
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

#### The `AssetInfo` object

Assets types and its count

| Element | Type | Description |
| --- | --- | --- |
| assetType | string | - |
| count | integer | - |

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
| metrics | [MetricDto](#openapi-definition-MetricDto)[] | Feature set metrics |

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



"assetsInfo": [



{



"assetType": "string",



"count": 1



}



],



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