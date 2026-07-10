---
title: IP address mapping rules - GET configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/get-configuration
---

# IP address mapping rules - GET configuration

# IP address mapping rules - GET configuration

* Reference
* Published Sep 24, 2020

Gets the configuration of mapping between IP addresses and geographic regions.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [IpAddressMappings](#openapi-definition-IpAddressMappings) | Success |

### Response body objects

#### The `IpAddressMappings` object

Configuration of the IP address mappings to geographic locations.

| Element | Type | Description |
| --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule](#openapi-definition-IpAddressMappingRule)[] | A list of IP address mapping rules.  Rules are evaluated from top to bottom; the first matching rule applies. |

#### The `IpAddressMappingRule` object

Configuration of the IP address mapping to the geographic location.

| Element | Type | Description |
| --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | The location for an IP address mapping. |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | The IP address or the IP address range to be mapped to the location. |

#### The `IpAddressMappingLocation` object

The location for an IP address mapping.

| Element | Type | Description |
| --- | --- | --- |
| city | string | The city name of the location. |
| countryCode | string | The country code of the location.  To fetch the list of available country codes, use the [GET all countries﻿](https://dt-url.net/37030go?dt=m) request. |
| latitude | number | The latitude of the location in `DDD.dddd` format. |
| longitude | number | The longitude of the location in `DDD.dddd` format. |
| regionCode | string | The region code of the location.  To fetch the list of available region codes, use the [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m) request. |

#### The `IpAddressRange` object

The IP address or the IP address range to be mapped to the location.

| Element | Type | Description |
| --- | --- | --- |
| address | string | The IP address to be mapped.  For an IP address range, this is the **from** address. |
| addressTo | string | The **to** address of the IP address range. |
| subnetMask | integer | The subnet mask of the IP address range. |

### Response body JSON models

```
{



"ipAddressMappingRules": [



{



"ipAddressMappingLocation": {



"city": "string",



"countryCode": "string",



"latitude": 1,



"longitude": 1,



"regionCode": "string"



},



"ipAddressRange": {



"address": "string",



"addressTo": "string",



"subnetMask": 1



}



}



]



}
```

## Related topics

* [Map internal IP addresses to locations for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Map internal IP addresses to locations for mobile applications in RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Map internal IP addresses to locations for custom applications in RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")