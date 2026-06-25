---
title: Reports API - GET all reports
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/reports-api/get-all
scraped: 2026-05-12T11:15:39.595465
---

# Reports API - GET all reports

# Reports API - GET all reports

* Reference
* Published Jan 16, 2020

Lists all available reports of the specified type.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/reports` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/reports` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| type | string | Type of a report. The element can hold these values * `DASHBOARD` | query | Optional |
| sourceId | string | Referencing source entity of a report (e.g. dashboard). | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [ReportStubList](#openapi-definition-ReportStubList) | Success |

### Response body objects

#### The `ReportStubList` object

A list of short representations of reports.

| Element | Type | Description |
| --- | --- | --- |
| values | [DashboardReportStub[]](#openapi-definition-DashboardReportStub) | A list of reports. |

#### The `DashboardReportStub` object

A short representations of the report.

| Element | Type | Description |
| --- | --- | --- |
| dashboardId | string | The ID of the associated dashboard. |
| id | string | The ID of the report. |
| type | string | The type of the report. The element can hold these values * `DASHBOARD` |

### Response body JSON models

```
{



"values": [



{



"dashboardId": "9eee7ed6-a125-4d9d-bfa7-afdb3404cb36",



"id": "337d883e-98c3-4dac-b8f2-1a9cdbd05969",



"type": "DASHBOARD"



},



{



"dashboardId": "26ccd360-828c-4d83-a65e-040ddc31e8f6",



"id": "b059e372-0b35-4d44-869b-95c326748848",



"type": "DASHBOARD"



}



]



}
```

## Example

In this example, the request asks for a list of all the report configurations in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/ \



-H 'Accept: application/json; charset=utf-8' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/reports/
```

#### Response body

```
{



"values": [



{



"id": "3ad7dece-98a4-4cc4-8805-34dcd19d4714",



"type": "DASHBOARD",



"dashboardId": "18d5b111-05ed-4efb-8cf1-e8dd0a9e5c47"



},



{



"id": "81c86de0-95d6-42d1-ad50-8578bb688b1c",



"type": "DASHBOARD",



"dashboardId": "bf0aad45-3785-444f-88d3-21e547eb78b1"



},



{



"id": "0b2e3121-4f8d-4b08-a879-3047e044ba4c",



"type": "DASHBOARD",



"dashboardId": "b6570e01-1d49-4bcc-a3bb-2fab2906512c"



}



]



}
```

#### Response code

200

## Related topics

* [Subscribe to Dynatrace dashboard reports](/managed/analyze-explore-automate/dashboards-classic/dashboards/subscribe-to-dashboard-reports "Learn how to subscribe to reports generated from Dynatrace dashboards.")