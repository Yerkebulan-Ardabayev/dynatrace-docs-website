---
title: Mobile Symbolication API - GET storage info
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-storage-info
---

# Mobile Symbolication API - GET storage info

# Mobile Symbolication API - GET storage info

* Reference
* Published Sep 03, 2019

Gets the symbol file storage information.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/info` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/info` |

## Authentication

To execute this request, you need an access token with `DssFileManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SymbolFileStorageInfo](#openapi-definition-SymbolFileStorageInfo) | Success |

### Response body objects

#### The `SymbolFileStorageInfo` object

| Element | Type | Description |
| --- | --- | --- |
| availableStorage | integer | The available storage space for symbol files, in KB. Has the value of `-1` for an unlimited quota. |
| fileCount | integer | - |
| storageQuota | integer | The total storage quota for symbol files, in KB. Has the value of `-1` for an unlimited quota. |
| usedStorage | integer | The size of the used storage by symbol files, in KB. |

### Response body JSON models

```
{



"availableStorage": 1,



"fileCount": 1,



"storageQuota": 1,



"usedStorage": 1



}
```

## Related topics

* [Upload and manage symbol files for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")