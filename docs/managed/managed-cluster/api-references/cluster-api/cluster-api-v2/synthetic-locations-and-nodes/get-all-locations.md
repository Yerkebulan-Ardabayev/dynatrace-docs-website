---
title: "Synthetic locations API v2 - GET all locations (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/get-all-locations
updated: 2026-02-09
---

# Synthetic locations API v2 - GET all locations (Dynatrace Managed)

# Synthetic locations API v2 - GET all locations (Dynatrace Managed)

* Published Jul 25, 2019

This API call lists all locations, public and private, and their parameters available for your environment. The request produces an `application/json` payload.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| cloudPlatform | string | Filters the resulting set of locations to those which are hosted on a specific cloud platform. The element can hold these values * `AWS` * `AZURE` * `ALIBABA` * `GOOGLE_CLOUD` * `OTHER` | query | Optional |
| type | string | Filters the resulting set of locations to those of a specific type. The element can hold these values * `PUBLIC` * `PRIVATE` | query | Optional |
| capability | string | Filters the resulting set of locations to those which support specific capability. The element can hold these values * `BROWSER` * `HTTP` * `HTTP_HIGH_RESOURCE` * `ICMP` * `TCP` * `DNS` | query | Optional |

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
| locations | [LocationCollectionElement[]](#openapi-definition-LocationCollectionElement) | A list of synthetic locations. |

#### The `LocationCollectionElement` object

A synthetic location.

| Element | Type | Description |
| --- | --- | --- |
| capabilities | string[] | The list of location's capabilities. |
| cloudPlatform | string | The cloud provider where the location is hosted.  Only applicable to `PUBLIC` locations. The element can hold these values * `ALIBABA` * `AMAZON_EC2` * `AZURE` * `DYNATRACE_CLOUD` * `GOOGLE_CLOUD` * `INTEROUTE` * `OTHER` * `UNDEFINED` |
| deploymentType | string | Location's deployment type The element can hold these values * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` |
| entityId | string | The Dynatrace entity ID of the location. |
| geoCity | string | Location's city. |
| geoContinent | string | Location's continent. |
| geoCountry | string | Location's country. |
| geoLatitude | number | Location's latitude. |
| geoLocationId | string | The Dynatrace GeoLocation ID of the location. |
| geoLongitude | number | Location's longitude. |
| ips | string[] | The list of IP addresses assigned to the location.  Only applicable to `PUBLIC` locations. |
| lastModificationTimestamp | integer | The timestamp of the last modification of the location. |
| name | string | The name of the location. |
| nodes | string[] | A list of synthetic nodes belonging to the location.  You can retrieve the list of available nodes with the [GET all nodesï»¿](https://dt-url.net/miy3rpl) call. |
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



"locations": [



{



"capabilities": [



"BROWSER",



"HTTP"



],



"cloudPlatform": "AMAZON_EC2",



"entityId": "SYNTHETIC_LOCATION-53F47ECB33907667",



"geoCity": "Gdansk",



"geoContinent": "Europe",



"geoCountry": "Poland",



"geoLatitude": "54.399078369140625",



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215",



"geoLongitude": "18.576557159423828",



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



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215",



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



https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations
```

#### Response body

```
{



"locations": [



{



"name": "Amazon US East (N. Virginia)",



"entityId": "SYNTHETIC_LOCATION-0000000000000004",



"type": "PUBLIC",



"cloudPlatform": "AMAZON_EC2",



"ips": [



"79.50.224.74",



"96.124.117.100"



],



"stage": "GA",



"status": "ENABLED",



"capabilities": [



"BROWSER"



],



"geoLocationId": "GEOLOCATION-95196F3C9A4F4215"



},



{



"name": "GdaÅsk",



"entityId": "SYNTHETIC_LOCATION-0000000000000064",



"type": "PUBLIC",



"cloudPlatform": "OTHER",



"ips": [



"120.157.221.247",



"172.158.6.93",



"197.136.70.30",



"227.53.205.237",



"131.123.197.12"



],



"stage": "GA",



"status": "ENABLED",



"capabilities": [



"BROWSER",



"HTTP"



],



"geoLocationId": "GEOLOCATION-0A41430434C388A9"



},



{



"name": "Linz HTTP",



"entityId": "SYNTHETIC_LOCATION-BB5EE23C1D48AFF5",



"type": "PRIVATE",



"status": "ENABLED",



"geoLocationId": "GEOLOCATION-427705B3488A4C45"



}



]



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
