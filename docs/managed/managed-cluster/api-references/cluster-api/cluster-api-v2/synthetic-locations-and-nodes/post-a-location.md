---
title: "Synthetic locations API v2 - POST a location (Dynatrace Managed)"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/synthetic-locations-and-nodes/post-a-location
updated: 2026-02-09
---

# Synthetic locations API v2 - POST a location (Dynatrace Managed)

# Synthetic locations API v2 - POST a location (Dynatrace Managed)

* Published Mar 13, 2019

This API call creates a new **private** synthetic location. For more details about synthetic location creation, see [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring."). The request consumes and produces an `application/json` payload.

## Authentication

To execute this request, you need the **Service Provider API** (`ServiceProviderAPI`) permission assigned to your API token. Generate your API token via Cluster Management Console (CMC). To learn how to obtain and use it, see [Cluster API - Authentication](/managed/managed-cluster/api-references/cluster-api/basics/cluster-api-authentication "How to get authenticated to use the Dynatrace Cluster API.").

## Endpoint

`/api/cluster/v2/synthetic/locations`

## Parameter

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic-v2/synthetic-locations-v2/json-models "Get synthetic nodes information via the Synthetic v2 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [PrivateSyntheticLocation](#openapi-definition-PrivateSyntheticLocation) | The JSON body of the request. Contains parameters of the new private synthetic location. | body | Required |

### Request body objects

#### The `PrivateSyntheticLocation` object

Configuration of a private synthetic location.

Some fields are inherited from the base *SyntheticLocation* object.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Non-containerized location property. Auto upgrade of Chromium is enabled (`true`) or disabled (`false`). | Optional |
| availabilityLocationOutage | boolean | Alerting for location outage is enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. | Optional |
| availabilityNodeOutage | boolean | Alerting for node outage is enabled (`true`) or disabled (`false`). \n\n If enabled, the outage of *any* node in the location triggers an alert. Supported only for private Synthetic locations. | Optional |
| availabilityNotificationsEnabled | boolean | Notifications for location and node outage are enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. | Optional |
| browserExecutionSupported | boolean | Containerized location property. Boolean value describes if browser monitors will be executed on this location:  * `false`: Browser monitor executions disabled. * `true`: Browser monitor executions enabled. | Optional |
| city | string | The city of the location. | Optional |
| countryCode | string | The country code of the location.  To fetch the list of available country codes, use the [GET all countriesï»¿](https://dt-url.net/37030go) request. | Optional |
| countryName | string | The country name of the location. | Optional |
| deploymentType | string | The deployment type of the location:  * `STANDARD`: The location is deployed on Windows or Linux. * `KUBERNETES`: The location is deployed on Kubernetes. The element can hold these values * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Optional |
| entityId | string | The Dynatrace entity ID of the location. | Optional |
| fipsMode | string | Containerized location property indicating whether FIPS mode is enabled on this location:  * `DISABLED`: FIPS is not enabled on the location. * `ENABLED`: FIPS is enabled on the location. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS with corporate proxy is enabled on this location.   Default: DISABLED The element can hold these values * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Optional |
| geoLocationId | string | The Dynatrace GeoLocation ID of the location. | Optional |
| latitude | number | The latitude of the location in `DDD.dddd` format. | Required |
| locationNodeOutageDelayInMinutes | integer | Alert if location or node outage lasts longer than *X* minutes. \n\n Only applicable when `availabilityLocationOutage` or `availabilityNodeOutage` is set to `true`. Supported only for private Synthetic locations. | Optional |
| longitude | number | The longitude of the location in `DDD.dddd` format. | Required |
| namExecutionSupported | boolean | Containerized location property. Boolean value describes if icmp monitors will be executed on this location:  * `false`: Icmp monitor executions disabled. * `true`: Icmp monitor executions enabled. | Optional |
| name | string | The name of the location. | Required |
| nodeNames | object | A mapping id to name of the nodes belonging to the location. | Optional |
| nodes | string[] | A list of synthetic nodes belonging to the location.  You can retrieve the list of available nodes with the [GET all nodesï»¿](https://dt-url.net/miy3rpl) call. | Required |
| regionCode | string | The region code of the location.  To fetch the list of available region codes, use the [GET regions of the countryï»¿](https://dt-url.net/az230x0) request. | Optional |
| regionName | string | The region name of the location. | Optional |
| status | string | The status of the location:  * `ENABLED`: The location is displayed as active in the UI. You can assign monitors to the location. * `DISABLED`: The location is displayed as inactive in the UI. You can't assign monitors to the location. Monitors already assigned to the location will stay there and will be executed from the location. * `HIDDEN`: The location is not displayed in the UI. You can't assign monitors to the location. You can only set location as `HIDDEN` when no monitor is assigned to it. The element can hold these values * `DISABLED` * `ENABLED` * `HIDDEN` | Optional |
| type | string | -The element can hold these values * `CLUSTER` * `PRIVATE` * `PUBLIC` | Required |
| useNewKubernetesVersion | boolean | Containerized location property. Boolean value describes which kubernetes version will be used:  * `false`: Version 1.23+ that is older than 1.26 * `true`: Version 1.26+. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"autoUpdateChromium": true,



"availabilityLocationNodeOutageDelayInMinutes": 5,



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"availabilityNotificationsEnabled": true,



"browserExecutionSupported": true,



"city": "Linz",



"countryCode": "AT",



"deploymentType": "STANDARD",



"fipsMode": "DISABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"maxActiveGateCount": 5,



"minActiveGateCount": 2,



"namExecutionSupported": false,



"name": "Linz Location",



"nodeNames": {



"93302281": "ActiveGate 1"



},



"nodeSize": "S",



"nodes": [



"93302281"



],



"regionCode": "04",



"status": "ENABLED",



"type": "PRIVATE",



"useNewKubernetesVersion": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [SyntheticLocationIdsDto](#openapi-definition-SyntheticLocationIdsDto) | Success. The private location has been created. The response contains the ID of the new location. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `SyntheticLocationIdsDto` object

A DTO for synthetic Location IDs.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Entity ID to be transferred |
| geoLocationId | string | GeoLocation ID to be transferred |

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



"entityId": "string",



"geoLocationId": "string"



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

In this example, the request creates a new private Synthetic location. This location lies in **Linz, Austria**. It uses the synthetic node with the ID of **290433380**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to replace the list of nodes with nodes available in your environment. You can fetch the list of available nodes with the [GET all nodes](/managed/dynatrace-api/environment-api/synthetic/synthetic-nodes/get-all "List all synthetic nodes via the Synthetic v1 API.") request.

#### Curl

```
curl -L -X POST 'https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



--data-raw '{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"290433380"



],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v2/synthetic/locations
```

#### Request body

```
{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"city": "Linz",



"status": "ENABLED",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["290433380"],



"availabilityLocationOutage": false,



"availabilityNodeOutage": false,



"locationNodeOutageDelayInMillis": 5000



}
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-493122BFA29674DC",



"geoLocationId": "GEOLOCATION-96B57899C9B5A3C7"



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")
