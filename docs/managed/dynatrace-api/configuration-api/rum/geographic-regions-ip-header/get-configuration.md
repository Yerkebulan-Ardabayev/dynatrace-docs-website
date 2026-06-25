---
title: IP mapping header rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-header/get-configuration
scraped: 2026-05-12T11:20:16.674493
---

# IP mapping header rules - GET configuration

# IP mapping header rules - GET configuration

* Reference
* Published Sep 24, 2020

Gets the list of IP detection headers.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipDetectionHeaders` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipDetectionHeaders` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [IpDetectionHeaders](#openapi-definition-IpDetectionHeaders) | Success |

### Response body objects

#### The `IpDetectionHeaders` object

Configuration of the custom client IP headers.

| Element | Type | Description |
| --- | --- | --- |
| ipDetectionHeaders | string[] | A list of custom client IP headers.  Headers are evaluated from top to bottom; the first matching header applies. |

### Response body JSON models

```
{



"ipDetectionHeaders": [



"string"



]



}
```

## Related topics

* [Customize IP address detection for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/customize-ip-address-detection-web "Change the way Dynatrace determines client IP addresses for your web applications.")
* [Customize IP address detection for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/customize-ip-address-detection-mobile "Change the way Dynatrace determines client IP addresses for your mobile applications.")
* [Customize IP address detection for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/customize-ip-address-detectio-custom "Change the way Dynatrace determines client IP addresses for your custom applications.")