---
title: Synthetic monitors API - GET all monitors
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-all-monitors
scraped: 2026-05-12T11:59:43.388358
---

# Synthetic monitors API - GET all monitors

# Synthetic monitors API - GET all monitors

* Reference
* Published Jul 25, 2019

Lists all synthetic monitors in your environment. The list contains only the names and IDs of monitors. To retrieve details, use the [**GET a monitor**](/managed/dynatrace-api/environment-api/synthetic/synthetic-monitors/get-a-monitor "View a synthetic monitor via the Synthetic v1 API.") call.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/synthetic/monitors` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/synthetic/monitors` |

## Authentication

To execute this request, you need an access token with one of the following scopes:

* `ExternalSyntheticIntegration`
* `DataExport`
* `ReadSyntheticData`

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| managementZone | integer | Filters the resulting set of monitors to those which are part of the specified management zone.  Specify the ID of the management zone here. | query | Optional |
| tag | string[] | Filters the resulting set of monitors by specified tags.  You can specify several tags in the following format: `tag=tag1&tag=tag2`. The monitor has to match **all** the specified tags.  In case of key-value tags, such as imported AWS or CloudFoundry tags use following format: `[context]key:value`. | query | Optional |
| location | string | Filters the resulting set of monitors to those assigned to a specified Synthetic location.  Specify the ID of the location here. | query | Optional |
| assignedApps | string[] | Filters the resulting set of monitors to those assigned to the specified applications.  You can specify several applications in the following format: `assignedApps=app1&assignedApps=app2`. The monitor has to have **all** the specified applications assigned.  Specify Dynatrace entity IDs of applications here. | query | Optional |
| type | string | Filters the resulting set of monitors to those of the specified type: `BROWSER` or `HTTP`. | query | Optional |
| enabled | boolean | Filters the resulting set of monitors to those which are enabled (`true`) or disabled (`false`). | query | Optional |
| credentialId | string | Filters the resulting set of monitors to those using the specified credential set.  Specify the ID of the credentials set here. | query | Optional |
| credentialOwner | string | Filters the resulting set of monitors to those using a credential owned by the specified user. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [Monitors](#openapi-definition-Monitors) | Success |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Client side error. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Server side error. |

### Response body objects

#### The `Monitors` object

A list of synthetic monitors

| Element | Type | Description |
| --- | --- | --- |
| monitors | [MonitorCollectionElement[]](#openapi-definition-MonitorCollectionElement) | The list of synthetic monitors. |

#### The `MonitorCollectionElement` object

The short representation of a synthetic monitor.

| Element | Type | Description |
| --- | --- | --- |
| enabled | boolean | The state of a synthetic monitor. |
| entityId | string | The ID of a synthetic object. |
| name | string | The name of a synthetic object. |
| type | string | The type of a synthetic monitor. The element can hold these values * `BROWSER` * `HTTP` |

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



"monitors": [



{



"enabled": true,



"entityId": "string",



"name": "string",



"type": "BROWSER"



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

In this example, the request lists all available monitors of the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to the first three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/v1/synthetic/monitors
```

#### Response body

```
{



"monitors": [



{



"name": "easyTravel Angular",



"entityId": "SYNTHETIC_TEST-000000000000C69F"



},



{



"name": "dynatrace.com",



"entityId": "SYNTHETIC_TEST-0000000000025434"



},



{



"name": "easytravel special offers",



"entityId": "SYNTHETIC_TEST-000000000000987A"



}



]



}
```

#### Response code

200

## Related topics

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")