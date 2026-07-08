---
title: Reports API - POST a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/post-report
---

# Reports API - POST a report

# Reports API - POST a report

* Reference
* Published Jan 16, 2020

Creates a new report.

The request consumes and produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports` |

## Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| body | [DashboardReport](#openapi-definition-DashboardReport) | The JSON body of the request. Contains parameters of the new report. | body | Optional |

### Request body objects

#### The `DashboardReport` object

Configuration of a dashboard report.

The dashboard report provides a public link to the associated dashboard with a custom reporting period: last week for weekly subscribers or last month for monthly subscribers.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| dashboardId | string | The ID of the associated dashboard. | Required |
| enabled | boolean | The email notifications for the dashboard report are enabled (`true`) or disabled (`false`). | Optional |
| id | string | The ID of the report. | Optional |
| subscriptions | [DashboardReportSubscription](#openapi-definition-DashboardReportSubscription) | A list of the report subscribers. | Required |
| type | string | -The element can hold these values * `DASHBOARD` | Required |

#### The `DashboardReportSubscription` object

A list of the report subscribers.

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| MONTH | string[] | A list of monthly subscribers.  Monthly subscribers receive the report on the first Monday of the month at midnight.  You can specify email addresses or Dynatrace user IDs here. | Optional |
| WEEK | string[] | A list of weekly subscribers.  Weekly subscribers receive the report every Monday at midnight.  You can specify email addresses or Dynatrace user IDs here. | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"dashboardId": "8dd67562-8bf5-4a09-830d-4e0ca992abd6",



"enabled": "true",



"id": "337d883e-98c3-4dac-b8f2-1a9cdbd05969",



"subscriptions": {



"MONTH": [



"demo@email.com",



"demo2@email.com"



],



"WEEK": [



"demo@email.com"



]



},



"type": "DASHBOARD"



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [EntityShortRepresentation](#openapi-definition-EntityShortRepresentation) | Success. The new report has been created. The response contains the ID of the new report. |
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

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **204** indicates a valid payload.

The request consumes an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/validator` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/validator` |

### Authentication

To execute this request, you need an access token with `WriteConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

### Response

#### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Validated. The submitted report is valid. The response doesn't have a body. |
| **400** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Failed. The input is invalid. |

#### Response body objects

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

#### Response body JSON models

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

In this example, the request creates a new report for the dashboard with the ID of **2768e6ca-e199-4433-9e0d-2922aec2099b**.

The report is sent weekly to Dynatrace user **john.smith** and monthly to Dynatrace user **jane.brown**.

The API token is passed in the **Authorization** header.

You can download or copy the example request body to try it out on your own. Be sure to use the dashboard ID and user that are available in your environment.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports \



-H 'Accept: application/json' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"type": "DASHBOARD",



"dashboardId": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"enabled": "true",



"subscriptions": {



"WEEK": [



"john.smith"



],



"MONTH": [



"jane.brown"



]



}



}



'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports
```

#### Request body

```
{



"type": "DASHBOARD",



"dashboardId": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"enabled": "true",



"subscriptions": {



"WEEK": ["john.smith"],



"MONTH": ["jane.brown"]



}



}
```

#### Response body

```
{



"id": "f78f78f5-00bd-4cc1-9e8b-ecfd1e379a73"



}
```

#### Response code

204

## Related topics

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.")