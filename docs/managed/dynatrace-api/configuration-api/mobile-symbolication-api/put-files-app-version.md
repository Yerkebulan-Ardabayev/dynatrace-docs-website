---
title: Mobile Symbolication API - PUT upload file for an app version
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/put-files-app-version
scraped: 2026-05-12T11:19:31.742052
---

# Mobile Symbolication API - PUT upload file for an app version

# Mobile Symbolication API - PUT upload file for an app version

* Reference
* Updated on Nov 12, 2025

Uploads a symbol file (Android mapping file and iOS/tvOS symbol extract file) for the specified version of a mobile app.

* For iOS apps, you must preprocess the dSYM files via the DSSClient before transferring them to Dynatrace. For more details, see [Upload symbol files via REST API](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files#ios-api "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.").
* You can upload a symbol file in any supported format (compressed or uncompressed). Note the following limits:

  + Uploaded fileâmust not exceed 100 MiB.
  + Uncompressed fileâmust not exceed 500 MiB after decompression (if compressed).

  If your file is too large, try compressing it to stay within the 100 MiB upload limit.

The request consumes one of the following payload types:

* `application/x-compressed`
* `application/x-zip-compressed`
* `application/zip`
* `text/plain`

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}/{packageName}/{os}/{versionCode}/{versionName}` |

## Authentication

To execute this request, you need an access token with `DssFileManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |
| packageName | string | The CFBundleIdentifier (iOS) or the package name (Android) of the required mobile app. | path | Required |
| os | string | The operating system of the required app. The element can hold these values * `ANDROID` * `IOS` * `TVOS` | path | Required |
| versionCode | string | The version code (Android) / CFBundleVersion (iOS) of the required app. | path | Required |
| versionName | string | The version name (Android) / CFBundleShortVersionString (iOS) of the required app. | path | Required |
| content-type | string | - | header | Optional |
| body | string | The file to be uploaded: a proguard file (\*.txt) for Android or the zip file produced by the DTXDssClient provided with the OneAgent for iOS. | body | Required |

### Request body objects

#### The `RequestBody` object

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The file has been uploaded and stored. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |
| **413** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The symbol file storage quota is exhausted. |

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

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")