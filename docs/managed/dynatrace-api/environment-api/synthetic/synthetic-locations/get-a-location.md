---
title: Synthetic locations API - GET a location
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-a-location
scraped: 2026-05-12T11:56:51.982082
---

# Synthetic locations API - GET a location

# Synthetic locations API - GET a location

* Reference
* Published Jul 26, 2019

We have a new version of this APIâ[Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."). Check it out!

Gets parameters of the specified location.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| locationId | string | The Dynatrace entity ID of the required location. | path | Required |

## Response

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Learn the variations of models in the Synthetic locations v1 API.").

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticLocation](#openapi-definition-SyntheticLocation) | Success. The response contains parameters of the synthetic location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticLocation` object

Configuration of a synthetic location.

**countryCode**, **regionCode**, **city** parameters are optional as they can be retrieved based on **latitude** and **longitude** of location.

The actual set of fields depends on the type of the location. Find the list of actual objects in the description of the **type** field or see [Synthetic locations API v2 - JSON modelsï»¿](https://dt-url.net/3n43szj).

| Element | Type | Description |
| --- | --- | --- |
| city | string | The city of the location. |
| countryCode | string | The country code of the location.  To fetch the list of available country codes, use the [GET all countriesï»¿](https://dt-url.net/37030go) request. |
| countryName | string | The country name of the location. |
| entityId | string | The Dynatrace entity ID of the location. |
| latitude | number | The latitude of the location in `DDD.dddd` format. |
| longitude | number | The longitude of the location in `DDD.dddd` format. |
| name | string | The name of the location. |
| regionCode | string | The region code of the location.  To fetch the list of available region codes, use the [GET regions of the countryï»¿](https://dt-url.net/az230x0) request. |
| regionName | string | The region name of the location. |
| status | string | The status of the location:  * `ENABLED`: The location is displayed as active in the UI. You can assign monitors to the location. * `DISABLED`: The location is displayed as inactive in the UI. You can't assign monitors to the location. Monitors already assigned to the location will stay there and will be executed from the location. * `HIDDEN`: The location is not displayed in the UI. You can't assign monitors to the location. You can only set location as `HIDDEN` when no monitor is assigned to it. The element can hold these values * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `PUBLIC` -> PublicSyntheticLocation * `PRIVATE` -> PrivateSyntheticLocation * `CLUSTER` -> PrivateSyntheticLocation The element can hold these values * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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



"city": "string",



"countryCode": "string",



"countryName": "string",



"entityId": "string",



"latitude": 1,



"longitude": 1,



"name": "string",



"regionCode": "string",



"regionName": "string",



"status": "DISABLED",



"type": "CLUSTER"



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

## Example - public location

In this example, the request gets the details of the **Amazon US East (N. Virginia)** public location, which has the ID of **GEOLOCATION-95196F3C9A4F4215**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/GEOLOCATION-95196F3C9A4F4215 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/GEOLOCATION-95196F3C9A4F4215
```

#### Response body

```
{



"entityId": "GEOLOCATION-95196F3C9A4F4215",



"type": "PUBLIC",



"name": "Amazon US East (N. Virginia)",



"countryCode": "US",



"regionCode": "VA",



"city": "Amazon US East (N. Virginia)",



"latitude": 39.0436,



"longitude": -77.4875,



"cloudPlatform": "AMAZON_EC2",



"ips": [



"134.189.153.97",



"134.189.153.98",



"134.189.153.99"



]



}
```

#### Response code

200

## Example - private location

In this example, the request gets the details of the **Gdansk HTTP** private location, which has the ID of **SYNTHETIC\_LOCATION-95196F3C9A4F4215**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-95196F3C9A4F4215 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-95196F3C9A4F4215
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-9C75B59442498323",



"type": "PRIVATE",



"name": "Gdansk HTTP",



"countryCode": "PL",



"regionCode": "82",



"city": "GdaÅsk",



"latitude": 54.3449,



"longitude": 18.6283,



"nodes": [



"2015649819",



"3086117876"



]



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")