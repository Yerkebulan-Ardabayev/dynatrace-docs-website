---
title: "Synthetic locations API v2 - GET a location (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-a-location
updated: 2026-02-09
---

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

# Synthetic locations API v2 - GET a location (Dynatrace Managed)

* Published Jul 26, 2019

This API call gets the parameters of the specified location. The request produces an `application/json` payload.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| locationId | string | The Dynatrace entity ID of the required location. | path | Required |

## Response

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
| geoLocationId | string | The Dynatrace GeoLocation ID of the location. |
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



"geoLocationId": "string",



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

## Response format

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

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
| geoLocationId | string | The Dynatrace GeoLocation ID of the location. |
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



"geoLocationId": "string",



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

In this example, the request gets the details of the **Amazon US East (N. Virginia)** public location, which has the ID of **SYNTHETIC\_LOCATION-0000000000000064**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000064 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000064
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-0000000000000064",



"type": "PUBLIC",



"name": "GdaÅsk",



"countryCode": "PL",



"regionCode": "EU",



"city": "GdaÅsk",



"latitude": 54.399078,



"longitude": 18.576557,



"status": "ENABLED",



"cloudPlatform": "OTHER",



"ips": [



"120.157.221.247",



"172.158.6.93",



"197.136.70.30",



"227.53.205.237",



"131.123.197.12"



],



"stage": "GA",



"browserType": "Chrome",



"browserVersion": "83.0.4103.61",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-0A41430434C388A9"



}
```

#### Response code

200

## Example - private location

In this example, the request gets the details of the **Linz HTTP** private location, which has the ID of **SYNTHETIC\_LOCATION-BB5EE23C1D48AFF5**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-BB5EE23C1D48AFF5
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-BB5EE23C1D48AFF5",



"type": "PRIVATE",



"name": "Linz HTTP",



"countryCode": "AT",



"regionCode": "04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"status": "ENABLED",



"nodes": [



"137829320"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 3000,



"geoLocationId": "GEOLOCATION-427705B3488A4C45"



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
