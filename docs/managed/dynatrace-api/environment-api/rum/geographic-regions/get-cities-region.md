---
title: Geographic regions API - GET cities of a region
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/rum/geographic-regions/get-cities-region
---

# Geographic regions API - GET cities of a region

# Geographic regions API - GET cities of a region

* Reference
* Updated on May 02, 2022

Lists cities of a region.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/rum/cities/{countryCode}/{regionCode}` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/rum/cities/{countryCode}/{regionCode}` |

## Authentication

To execute this request, you need an access token with `geographicRegions.read` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| countryCode | string | The ISO code of the required country.  To fetch the list of available country codes, use the [GET all countries﻿](https://dt-url.net/37030go?dt=m) request. | path | Required |
| regionCode | string | The code of the required region.  To fetch the list of available region codes, use the [GET regions of the country﻿](https://dt-url.net/az230x0?dt=m) request. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [CountryWithRegionsWithCities](#openapi-definition-CountryWithRegionsWithCities) | Success. The response contains the list of region's cities. |
| **404** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The requested resource doesn't exist. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `CountryWithRegionsWithCities` object

Information about a country.

| Element | Type | Description |
| --- | --- | --- |
| countryCode | string | The ISO code of the country. |
| countryName | string | The name of the country. |
| regionCount | integer | The number of regions in the country. |
| regions | [RegionWithCities](#openapi-definition-RegionWithCities)[] | The list of regions in the country. |

#### The `RegionWithCities` object

Information about a country's region and its cities.

| Element | Type | Description |
| --- | --- | --- |
| cities | [City](#openapi-definition-City)[] | The list of cities in the region. |
| cityCount | integer | The number of cities in a region of a country. |
| code | string | The code of the region. |
| name | string | The name of the region. |

#### The `City` object

Information about a city.

| Element | Type | Description |
| --- | --- | --- |
| latitude | number | The latitude of the city. |
| longitude | number | The longitude of the city. |
| name | string | The name of the city. |

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



"countryName": "France",



"regionCount": 13,



"regions": [



{



"cities": [



{



"latitude": 46.2806,



"longitude": 6.7217,



"name": "Abondance"



},



{



"latitude": 46.1008,



"longitude": 3.4463,



"name": "Abrest"



}



],



"cityCount": 4,



"code": "ARA",



"name": "Auvergne-Rhone-Alpes"



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