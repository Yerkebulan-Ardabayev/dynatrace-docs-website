---
title: "Synthetic locations API v2 - PUT a location (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/put-a-location
updated: 2026-02-09
---

# Synthetic locations API v2 - PUT a location (Dynatrace Managed)

# Synthetic locations API v2 - PUT a location (Dynatrace Managed)

* Published Jul 26, 2019

This API call:

* Private locations Updates an existing location.
* Public locations Changes the status of an existing location.

The request consumes an `application/json` payload.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| locationId | string | The Dynatrace entity ID of the synthetic location to be updated. | path | Required |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | The JSON body of the request. Contains updated parameters of the location. | body | Required |

### Request body objects

#### The `SyntheticLocationUpdate` object

The synthetic location update. This is a base object, the exact type depends on the value of the `type` field.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> SyntheticPrivateLocationUpdate The element can hold these values * `PRIVATE` * `PUBLIC` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"type": "PRIVATE"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Success. The location has been updated. Response doesn't have a body. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

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

## Example - private location

In this example, the request updates the **private** synthetic location from the [POST request example](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/post-a-location#example "Create a private synthetic location via the Synthetic v2 API."). It changes the name of the location to **Linz** and adds the synthetic node with the ID of **353074222**.

The API token is passed in the **Authorization** header.

The response code of **204** indicates that the update was successful.

You can download or copy the example request body to try it out on your own. Be sure to replace the list of nodes with nodes available in your environment. You can fetch the list of available nodes with the [GET all nodes](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all "List all synthetic nodes via the Synthetic v1 API.") request.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"regionCode": "04",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"290433380",



"353074222"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-493122BFA29674DC
```

#### Request body

```
{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["290433380", "353074222"],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}
```

#### Response code

204

## Example - public location

In this example, the request disables the public location with the ID of **SYNTHETIC\_LOCATION-0000000000000273**.

The API token is passed in the **Authorization** header.

The response code of **204** indicates that the update was successful.

#### Curl

```
curl -L -X PUT 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000273' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"type": "PUBLIC",



"status": "DISABLED"



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations/SYNTHETIC_LOCATION-0000000000000273
```

#### Request body

```
{



"type": "PUBLIC",



"status": "DISABLED"



}
```

#### Response code

204

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
