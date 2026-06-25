---
title: Synthetic locations API - POST a location
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/post-a-location
scraped: 2026-05-12T11:56:55.967195
---

# Synthetic locations API - POST a location

# Synthetic locations API - POST a location

* Reference
* Published Mar 13, 2019

We have a new version of this APIâ[Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Find out what the Dynatrace Synthetic v2 API offers."). Check it out!

Creates a new **private** Synthetic location. For more details about synthetic location creation, see [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.").

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/locations` |

## Authentication

To execute this request, you need an access token with `ExternalSyntheticIntegration` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameter

To find all model variations that depend on the type of the model, see [JSON models](/managed/dynatrace-api/environment-api/synthetic/synthetic-locations/json-models "Learn the variations of models in the Synthetic locations v1 API.").

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [SyntheticLocation](#openapi-definition-SyntheticLocation) | The JSON body of the request. Contains parameters of the new private synthetic location. | body | Optional |

### Request body objects

#### The `SyntheticLocation` object

Configuration of a synthetic location.

**countryCode**, **regionCode**, **city** parameters are optional as they can be retrieved based on **latitude** and **longitude** of location.

The actual set of fields depends on the type of the location. Find the list of actual objects in the description of the **type** field or see [Synthetic locations API v2 - JSON modelsï»¿](https://dt-url.net/3n43szj).

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| autoUpdateChromium | boolean | Non-containerized location property. Auto upgrade of Chromium is enabled (`true`) or disabled (`false`). | Optional |
| availabilityLocationOutage | boolean | Alerting for location outage is enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. | Optional |
| availabilityNodeOutage | boolean | Alerting for node outage is enabled (`true`) or disabled (`false`). \n\n If enabled, the outage of *any* node in the location triggers an alert. Supported only for private Synthetic locations. | Optional |
| availabilityNotificationsEnabled | boolean | Notifications for location and node outage are enabled (`true`) or disabled (`false`). Supported only for private Synthetic locations. | Optional |
| browserExecutionSupported | boolean | Containerized location property. Boolean value describes if browser monitors will be executed on this location:  * `false`: Browser monitor executions disabled. * `true`: Browser monitor executions enabled. | Optional |
| deploymentType | string | The deployment type of the location:  * `STANDARD`: The location is deployed on Windows or Linux. * `KUBERNETES`: The location is deployed on Kubernetes. The element can hold these values * `KUBERNETES` * `OPENSHIFT` * `STANDARD` * `UNKNOWN` | Optional |
| fipsMode | string | Containerized location property indicating whether FIPS mode is enabled on this location:  * `DISABLED`: FIPS is not enabled on the location. * `ENABLED`: FIPS is enabled on the location. * `ENABLED_WITH_CORPORATE_PROXY`: FIPS with corporate proxy is enabled on this location.   Default: DISABLED The element can hold these values * `DISABLED` * `ENABLED` * `ENABLED_WITH_CORPORATE_PROXY` | Optional |
| locationNodeOutageDelayInMinutes | integer | Alert if location or node outage lasts longer than *X* minutes. \n\n Only applicable when `availabilityLocationOutage` or `availabilityNodeOutage` is set to `true`. Supported only for private Synthetic locations. | Optional |
| maxActiveGateCount | integer | Containerized location property. The maximum number of ActiveGates deployed for the location (required for a Kubernetes location). | Optional |
| minActiveGateCount | integer | Containerized location property. The minimum number of ActiveGates deployed for the location (required for a Kubernetes location). | Optional |
| namExecutionSupported | boolean | Containerized location property. Boolean value describes if icmp monitors will be executed on this location:  * `false`: Icmp monitor executions disabled. * `true`: Icmp monitor executions enabled. | Optional |
| nodeSize | string | Containerized location property. The size of a containerized node deployed for the location (required for a Kubernetes location). Accepted values:  * `XS`: extra small * `S`: small * `M`: medium   The node size `L` is not supported in containerized locations. The element can hold these values * `M` * `S` * `UNSUPPORTED` * `XS` | Optional |
| nodes | string[] | A list of synthetic nodes belonging to the location.  You can retrieve the list of available nodes with the [GET all nodesï»¿](https://dt-url.net/miy3rpl) call. | Optional |
| useNewKubernetesVersion | boolean | Containerized location property. Boolean value describes which kubernetes version will be used:  * `false`: Version 1.23+ that is older than 1.26 * `true`: Version 1.26+. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"autoUpdateChromium": true,



"availabilityLocationOutage": true,



"availabilityNodeOutage": true,



"availabilityNotificationsEnabled": true,



"browserExecutionSupported": true,



"deploymentType": "KUBERNETES",



"fipsMode": "DISABLED",



"locationNodeOutageDelayInMinutes": 1,



"maxActiveGateCount": 1,



"minActiveGateCount": 1,



"namExecutionSupported": true,



"nodeSize": "M",



"nodes": [



"string"



],



"useNewKubernetesVersion": true



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [EntityIdDto](#openapi-definition-EntityIdDto) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `EntityIdDto` object

A DTO for entity ID.

| Element | Type | Description |
| --- | --- | --- |
| entityId | string | Entity ID to be transferred |

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



"entityId": "string"



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

In this example, the request creates a new private Synthetic location. This location lies in **Linz, Austria**. It uses the synthetic node with the ID of **93302281**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to replace the list of nodes with nodes available in your environment.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": [



"93302281"



]



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/locations
```

#### Request body

```
{



"type": "PRIVATE",



"name": "REST example - Linz",



"countryCode": "AT",



"regionCode": "AU04",



"city": "Linz",



"latitude": 48.306351,



"longitude": 14.287399,



"nodes": ["93302281"]



}
```

#### Response body

```
{



"entityId": "SYNTHETIC_LOCATION-8F419D1B53639A45"



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Create a private Synthetic location](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Learn how to create a private location for synthetic monitoring.")