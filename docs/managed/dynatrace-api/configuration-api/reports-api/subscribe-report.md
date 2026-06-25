---
title: Reports API - POST subscribe to a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/subscribe-report
scraped: 2026-05-12T11:15:41.116040
---

# Reports API - POST subscribe to a report

# Reports API - POST subscribe to a report

* Reference
* Published Jan 16, 2020

Subscribes the specified users to the specified report. All existing subscriptions remain intact.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}/subscribe` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}/subscribe` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the report to subscribe to. | path | Required |
| body | [ReportSubscriptions](#openapi-definition-ReportSubscriptions) | The JSON body of the request. Contains a list of new subscribers. | body | Optional |

### Request body objects

#### The `ReportSubscriptions` object

Configuration of a report subscription.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| recipients | string[] | A list of the recipients.  You can specify email addresses or Dynatrace user IDs here. | Required |
| schedule | string | The schedule of the subscription.  * Weekly subscribers receive the report every Monday at midnight. * Monthly subscribers receive the report on the first Monday of the month at midnight. The element can hold these values * `MONTH` * `WEEK` | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"recipients": [



"demo@email.com",



"demo2@email.com"



],



"schedule": "WEEK"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new subscriptions have been created. The response body contains the report ID. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

### Response body objects

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

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



"description": "Dynatrace entity for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity"



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

In this example, the request updates the report from the [POST request example](/managed/dynatrace-api/configuration-api/reports-api/post-report#example "Create a report configuration via the Dynatrace API."). It adds the weekly subscriptions for the Dynatrace user **ryan.white**.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73/subscribe \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"schedule": "WEEK",



"recipients": [



"ryan.white"



]



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73/subscribe
```

#### Request body

```
{



"schedule": "WEEK",



"recipients": [



"ryan.white"



]



}
```

#### Response body

```
{



"id": "f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73"



}
```

#### Response code

201

## Related topics

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.")