---
title: Synthetic locations API - PUT a location
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/put-a-location
scraped: 2026-05-12T11:56:58.090740
---

# Synthetic locations API - PUT a location

# Synthetic locations API - PUT a location

* Reference
* Published Jul 26, 2019

We have a new version of this APIâ[Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."). Check it out!

Updates an existing **private** synthetic location.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| PUT | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |
| PUT | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations/{locationId}` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Learn the variations of models in the Synthetic locations v1 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| locationId | string | The Dynatrace entity ID of the synthetic location to be updated. | path | Required |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | The JSON body of the request. Contains updated parameters of the private synthetic location or the status of the location. | body | Optional |

### Request body objects

#### The `SyntheticLocationUpdate` object

The update of a synthetic location. The actual object depends on the **type** of the location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> PrivateSyntheticLocationUpdate The element can hold these values * `PRIVATE` * `PUBLIC` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"latitude": 48.306351,



"longitude": 14.287399,



"name": "Linz Location",



"nodes": [



"93302281"



],



"status": "ENABLED",



"type": "PRIVATE"



}
```

## Response

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| locationId | string | The Dynatrace entity ID of the synthetic location to be updated. | path | Required |
| body | [SyntheticLocationUpdate](#openapi-definition-SyntheticLocationUpdate) | The JSON body of the request. Contains updated parameters of the private synthetic location or the status of the location. | body | Optional |

### Request body objects

#### The `SyntheticLocationUpdate` object

The update of a synthetic location. The actual object depends on the **type** of the location.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| type | string | Defines the actual set of fields depending on the value. See one of the following objects:  * `PUBLIC` -> SyntheticPublicLocationUpdate * `PRIVATE` -> PrivateSyntheticLocationUpdate The element can hold these values * `PRIVATE` * `PUBLIC` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"latitude": 48.306351,



"longitude": 14.287399,



"name": "Linz Location",



"nodes": [



"93302281"



],



"status": "ENABLED",



"type": "PRIVATE"



}
```

## Example

In this example, the request updates the private Synthetic location from the [POST request example](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/post-a-location#example "Create a private synthetic location via the Synthetic v1 API."). It changes the name of the location to **Linz** and adds the Synthetic node with the ID of **353074222**.

The API token is passed in the **Authorization** header.

The response code of **204** indicates that the update was successful.

You can download or copy the example request body to try it out on your own. Be sure to replace the list of nodes with nodes available in your environment.

#### Curl

```
curl -X PUT \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-8F419D1B53639A45 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"93302281",



"353074222"



]



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations/SYNTHETIC_LOCATION-8F419D1B53639A45
```

#### Request body

```
{



"type": "PRIVATE",



"name": "Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["93302281", "353074222"]



}
```

#### Response code

204

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")