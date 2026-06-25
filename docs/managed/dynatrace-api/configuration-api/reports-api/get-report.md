---
title: Reports API - GET a report
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/get-report
scraped: 2026-05-12T11:15:46.763842
---

# Reports API - GET a report

# Reports API - GET a report

* Reference
* Published Jan 16, 2020

Gets the properties of the specified report.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports/{id}` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| id | string | The ID of the required report. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DashboardReport](#openapi-definition-DashboardReport) | Success. The response body contains parameters of the report. |

### Response body objects

#### The `DashboardReport` object

Configuration of a dashboard report.

The dashboard report provides a public link to the associated dashboard with a custom reporting period: last week for weekly subscribers or last month for monthly subscribers.

| Element | Type | Description |
| --- | --- | --- |
| dashboardId | string | The ID of the associated dashboard. |
| enabled | boolean | The email notifications for the dashboard report are enabled (`true`) or disabled (`false`). |
| id | string | The ID of the report. |
| subscriptions | [DashboardReportSubscription](#openapi-definition-DashboardReportSubscription) | A list of the report subscribers. |
| type | string | -The element can hold these values * `DASHBOARD` |

#### The `DashboardReportSubscription` object

A list of the report subscribers.

| Element | Type | Description |
| --- | --- | --- |
| MONTH | string[] | A list of monthly subscribers.  Monthly subscribers receive the report on the first Monday of the month at midnight.  You can specify email addresses or Dynatrace user IDs here. |
| WEEK | string[] | A list of weekly subscribers.  Weekly subscribers receive the report every Monday at midnight.  You can specify email addresses or Dynatrace user IDs here. |

### Response body JSON models

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

## Example

In this example, the request inquires about the properties of the report with the ID of **0b2e3121-4f8d-4b08-a879-3047e044ba4c**.

The report contains data from the dashboard with the ID of **b6570e01-1d49-4bcc-a3bb-2fab2906512c**. It is sent weekly to Dynatrace users **john.smith** and **ryan.white** and monthly to Dynatrace user **jane.brown** and also to the **marketing.office@organization.com** email address.

The API token is passed in the **Authorization** header.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/0b2e3121-4f8d-4b08-a879-3047e044ba4c \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/0b2e3121-4f8d-4b08-a879-3047e044ba4c
```

#### Response body

```
{



"id": "0b2e3121-4f8d-4b08-a879-3047e044ba4c",



"type": "DASHBOARD",



"dashboardId": "b6570e01-1d49-4bcc-a3bb-2fab2906512c",



"enabled": true,



"subscriptions": {



"WEEK": [



"john.smith",



"ryan.white"



],



"MONTH": [



"jane.brown",



"marketing.office@organization.com"



]



}



}
```

#### Response code

200

## Related topics

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.")