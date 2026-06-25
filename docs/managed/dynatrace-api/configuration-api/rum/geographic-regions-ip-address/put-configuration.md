---
title: IP address mapping rules - PUT configuration
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/rum/geographic-regions-ip-address/put-configuration
scraped: 2026-05-12T11:17:57.727711
---

# IP address mapping rules - PUT configuration

# IP address mapping rules - PUT configuration

* Reference
* Published Sep 24, 2020

Updates the configuration of mapping between IP addresses and geographic regions.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [IpAddressMappings](#openapi-definition-IpAddressMappings) | The JSON body of the request. Contains the configuration of the IP address mapping. | body | Optional |

### Request body objects

#### The `IpAddressMappings` object

Configuration of the IP address mappings to geographic locations.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ipAddressMappingRules | [IpAddressMappingRule[]](#openapi-definition-IpAddressMappingRule) | A list of IP address mapping rules.  Rules are evaluated from top to bottom; the first matching rule applies. | Optional |

#### The `IpAddressMappingRule` object

Configuration of the IP address mapping to the geographic location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| ipAddressMappingLocation | [IpAddressMappingLocation](#openapi-definition-IpAddressMappingLocation) | The location for an IP address mapping. | Required |
| ipAddressRange | [IpAddressRange](#openapi-definition-IpAddressRange) | The IP address or the IP address range to be mapped to the location. | Required |

#### The `IpAddressMappingLocation` object

The location for an IP address mapping.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| city | string | The city name of the location. | Optional |
| countryCode | string | The country code of the location.  To fetch the list of available country codes, use the [GET all countriesï»¿](https://dt-url.net/37030go) request. | Required |
| latitude | number | The latitude of the location in `DDD.dddd` format. | Optional |
| longitude | number | The longitude of the location in `DDD.dddd` format. | Optional |
| regionCode | string | The region code of the location.  To fetch the list of available region codes, use the [GET regions of the countryï»¿](https://dt-url.net/az230x0) request. | Optional |

#### The `IpAddressRange` object

The IP address or the IP address range to be mapped to the location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| address | string | The IP address to be mapped.  For an IP address range, this is the **from** address. | Required |
| addressTo | string | The **to** address of the IP address range. | Optional |
| subnetMask | integer | The subnet mask of the IP address range. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

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

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The configuration has been updated. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/geographicRegions/ipAddressMappings/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The submitted configuration is valid. Response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid |

#### Response body objects

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

#### Response body JSON models

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

* [Map internal IP addresses to locations for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/map-internal-ip-addresses-to-locations-web "Configure Dynatrace to use local addresses to understand where the users of your web applications are.")
* [Map internal IP addresses to locations for mobile applications](/managed/observe/digital-experience/mobile-applications/additional-configuration/map-internal-ip-addresses-to-locations-mobile "Configure Dynatrace to use local addresses to understand where the users of your mobile applications are.")
* [Map internal IP addresses to locations for custom applications](/managed/observe/digital-experience/custom-applications/additional-configuration/map-internal-ip-addresses-to-locations-custom "Configure Dynatrace to use local addresses to understand where the users of your custom applications are.")