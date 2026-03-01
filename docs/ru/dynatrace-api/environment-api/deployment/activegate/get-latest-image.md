---
title: Deployment API - GET the latest available ActiveGate image version
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/deployment/activegate/get-latest-image
scraped: 2026-03-01T21:28:07.386603
---

# Deployment API - GET the latest available ActiveGate image version

# Deployment API - GET the latest available ActiveGate image version

* Reference
* Published Nov 22, 2023

Get the latest available ActiveGate image version.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v1/deployment/image/gateway/latest` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v1/deployment/image/gateway/latest` |

## Authentication

To execute this request, you need an access token with `InstallerDownload` scope.

To learn how to obtain and use it, see [Tokens and authentication](/docs/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ImageDto](#openapi-definition-ImageDto) | Success |
| **404** | - | No ActiveGate image found |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `ImageDto` object

| Element | Type | Description |
| --- | --- | --- |
| source | string | Image location |
| tag | string | Image tag |

### Response body JSON models

```
{



"source": "string",



"tag": "string"



}
```