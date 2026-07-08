---
title: Mobile Symbolication API - GET supported version
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/mobile-symbolication-api/get-supported-versions
---

# Mobile Symbolication API - GET supported version

# Mobile Symbolication API - GET supported version

* Reference
* Published Sep 03, 2019

Gets the supported file format version for iOS symbol files.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/symfiles/ios/supportedversion` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/symfiles/ios/supportedversion` |

## Authentication

To execute this request, you need an access token with `DssFileManagement` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SupportedVersion](#openapi-definition-SupportedVersion) | Success |

### Response body objects

#### The `SupportedVersion` object

| Element | Type | Description |
| --- | --- | --- |
| version | string | The supported iOS file format version. |

### Response body JSON models

```
{



"version": "string"



}
```

## Related topics

* [Upload and manage symbol files for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/upload-and-manage-symbol-files "Learn about deobfuscation (Android) and symbolication (iOS and tvOS) and your options for uploading and managing symbol files in Dynatrace.")