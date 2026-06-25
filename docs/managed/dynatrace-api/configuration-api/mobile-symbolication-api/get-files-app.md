---
title: Mobile Symbolication API - GET files for an app
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-files-app
scraped: 2026-05-12T11:19:30.450675
---

# Mobile Symbolication API - GET files for an app

# Mobile Symbolication API - GET files for an app

* Reference
* Published Sep 03, 2019

Lists the metadata of all symbol files (Android mapping files and iOS/tvOS symbol extract files) for a mobile app from the symbol file storage.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/{applicationId}` |

## Authentication

To execute this request, you need an access token with `DssFileManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| applicationId | string | The UUID of the required mobile or custom application. It can be found in the Instrumentation Wizard of your app. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SymbolFileList](#openapi-definition-SymbolFileList) | Success |

### Response body objects

#### The `SymbolFileList` object

| Element | Type | Description |
| --- | --- | --- |
| symbolFiles | [SymbolFile[]](#openapi-definition-SymbolFile) | A list of symbol files. |

#### The `SymbolFile` object

| Element | Type | Description |
| --- | --- | --- |
| appId | [AppIdentifier](#openapi-definition-AppIdentifier) | The identification info of the application to which the file belongs to. |
| applicationName | string | The name of the application to which the file belongs to. |
| pinned | boolean | Whether the file pinned and therefore cannot be deleted. |
| size | integer | The size of the file, in KB. |
| uploadTimestamp | integer | The timestamp of the file upload, in UTC milliseconds |

#### The `AppIdentifier` object

The identification info of the application to which the file belongs to.

| Element | Type | Description |
| --- | --- | --- |
| id | string | The ID of the mobile app. |
| os | string | The operating system the file belongs to. The element can hold these values * `ANDROID` * `IOS` * `TVOS` |
| packageName | string | The bundleId (iOS) or package name (Android) the file belongs to. |
| versionCode | string | The version code (Android) / bundle version (iOS) the file belongs to. |
| versionName | string | The version name (Android) / bundle versions string (iOS) the file belongs to. |

### Response body JSON models

```
{



"symbolFiles": [



{



"appId": {



"id": "string",



"os": "ANDROID",



"packageName": "string",



"versionCode": "string",



"versionName": "string"



},



"applicationName": "string",



"pinned": true,



"size": 1,



"uploadTimestamp": 1



}



]



}
```

## Related topics

* [Upload and manage symbol files for mobile applications](/managed/observe/digital-experience/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")