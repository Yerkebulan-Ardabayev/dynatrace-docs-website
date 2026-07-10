---
title: Geographic regions API - GET regions of a country
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/geographic-regions/get-regions-country
---

# Geographic regions API - GET regions of a country

# Geographic regions API - GET regions of a country

* Reference
* Updated on May 02, 2022

Lists regions of a country.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/regions/{countryCode}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/regions/{countryCode}` |

## Authentication

To execute this request, you need an access token with `geographicRegions.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| countryCode | string | The ISO code of the required country.  To fetch the list of available country codes, use the [GET all countries﻿](https://dt-url.net/37030go?dt=m) request. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CountryWithRegions](#openapi-definition-CountryWithRegions) | Success. The response contains the list of country's regions. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CountryWithRegions` object

Information about a country.

| Element | Type | Description |
| --- | --- | --- |
| countryCode | string | The ISO code of the country. |
| countryName | string | The name of the country. |
| regionCount | integer | The number of regions in the country. |
| regions | [Region](#openapi-definition-Region)[] | The list of regions in the country. |

#### The `Region` object

Information about a country's region.

| Element | Type | Description |
| --- | --- | --- |
| code | string | The code of the region. |
| name | string | The name of the region. |

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



"countryCode": "FR",



"countyName": "France",



"regionCount": 2,



"regions": [



{



"code": "ARA",



"name": "Auvergne-Rhone-Alpes"



},



{



"code": "BFC",



"name": "Bourgogne-Franche-Comte"



}



]



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

* [Real User Monitoring Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/rum-overview "Learn about Real User Monitoring Classic, key performance metrics, mobile app monitoring, and more.")
* [Detection of IP addresses, geolocations, and user agents in RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/detection-of-ip-addresses-locations-and-user-agents "Dynatrace detects IP addresses and geolocations like a city, region, and country as well as browsers, devices, and operating systems.")