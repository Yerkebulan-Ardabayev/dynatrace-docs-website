---
title: Synthetic locations API - GET all locations
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/get-all-locations
---

# Synthetic locations API - GET all locations

# Synthetic locations API - GET all locations

* Reference
* Published Jul 25, 2019

We have a new version of this API—[Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."). Check it out!

Lists all locations, public and private, and their parameters available for your environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `DataExport`
* `ExternalSyntheticIntegration`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Filters the resulting set of locations to those which are hosted on a specific cloud platform. The element can hold these values * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Optional |
| type | string | Filters the resulting set of locations by a specific type. The element can hold these values * `PUBLIC` * `PRIVATE` | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SyntheticLocations](#openapi-definition-SyntheticLocations) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticLocations` object

A list of synthetic locations.

| Element | Type | Description |
| --- | --- | --- |
| locations | [LocationCollectionElement](#openapi-definition-LocationCollectionElement)[] | A list of synthetic locations. |

#### The `LocationCollectionElement` object

A synthetic location.

| Element | Type | Description |
| --- | --- | --- |
| capabilities | string[] | The list of location's capabilities. |
| cloudPlatform | string | The cloud provider where the location is hosted.  Only applicable to `PUBLIC` locations. The element can hold these values * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| entityId | string | The Dynatrace entity ID of the location. |
| ips | string[] | The list of IP addresses assigned to the location.  Only applicable to `PUBLIC` locations. |
| name | string | The name of the location. |
| stage | string | The release stage of the location. The element can hold these values * `BETA` * `COMING_SOON` * `DELETED` * `GA` |
| status | string | The status of the location. The element can hold these values * `DISABLED` * `ENABLED` * `HIDDEN` |
| type | string | The type of the location. The element can hold these values * `CLUSTER` * `PRIVATE` * `PUBLIC` |

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



"locations": [



{



"capabilities": [



"BROWSER",



"HTTP"



],



"cloudPlatform": "AMAZON_EC2",



"entityId": "GEOLOCATION-B8D793BCA914E0AF",



"ips": [



"134.189.153.97",



"134.189.153.98"



],



"name": "Gdansk",



"stage": "GA",



"status": "ENABLED",



"type": "PUBLIC"



},



{



"entityId": "SYNTHETIC_LOCATION-53F47ECB33907667",



"name": "My private location",



"status": "ENABLED",



"type": "PRIVATE"



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

## Example

In this example, the request lists all synthetic locations available for the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations
```

#### Response body

```
{



"locations": [



{



"name": "Amazon US East (N. Virginia)",



"entityId": "GEOLOCATION-95196F3C9A4F4215",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"134.189.153.97",



"134.189.153.98",



"134.189.153.99"



]



},



{



"name": "AWS Europe (London)",



"entityId": "GEOLOCATION-A9022AAFA0763F56",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"243.22.221.174",



"104.179.71.29"



]



},



{



"name": "Gdansk HTTP",



"entityId": "SYNTHETIC_LOCATION-9C75B59442498323",



"type": "PRIVATE"



}



]



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")