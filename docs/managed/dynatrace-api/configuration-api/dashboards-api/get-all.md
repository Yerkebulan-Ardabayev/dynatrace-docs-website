---
title: Dashboards API - GET all dashboards
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/dashboards-api/get-all
---

# Dashboards API - GET all dashboards

# Dashboards API - GET all dashboards

* Reference
* Published Aug 30, 2019

Lists all dashboards of your Dynatrace environment, regardless of access rights in the UI.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/dashboards` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/dashboards` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| owner | string | The owner of the dashboard. | query | Optional |
| tags | string[] | A list of tags applied to the dashboard.  The dashboard must match **all** the specified tags. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [DashboardList](#openapi-definition-DashboardList) | Success |

### Response body objects

#### The `DashboardList` object

A list of short representations of dashboards.

| Element | Type | Description |
| --- | --- | --- |
| dashboards | [DashboardStub](#openapi-definition-DashboardStub)[] | A list of short representations of dashboards. |

#### The `DashboardStub` object

A short representation of a dashboard.

| Element | Type | Description |
| --- | --- | --- |
| created | integer | The timestamp of dashboard creation, in UTC milliseconds. |
| id | string | The ID of the dashboard. |
| lastModified | integer | The timestamp of the last dashboard modification, in UTC milliseconds. |
| lastViewed | integer | The timestamp of the last dashboard view, in UTC milliseconds. |
| name | string | The name of the dashboard. |
| owner | string | The owner of the dashboard. |
| popularity | integer | The popularity of the dashboard, from 0 (least popular) to 10 (most popular). |

### Response body JSON models

```
{



"dashboards": [



{



"created": 1776772474839,



"id": "d6740373-ff26-4681-b95f-fd5b858c97f7",



"lastModified": 1776858899692,



"lastViewed": 1776945274839,



"name": "Home dashboard",



"owner": "admin",



"popularity": 5



},



{



"created": 1776772474839,



"id": "54b34dbb-2ae7-4c27-9dbc-90a4f4c68b10",



"lastModified": 1776858899692,



"name": "Databases",



"owner": "viewer"



},



{



"id": "8525b0bf-e33c-4a92-a534-9dedc1391e10",



"name": "Business value",



"owner": "rocks"



}



]



}
```

## Example

In this example, the request lists all dashboards of the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/dashboards
```

#### Response body

```
{



"dashboards": [



{



"id": "891f3203-9953-4796-aacd-886c0f59dddf",



"name": "Home",



"owner": "admin.user"



},



{



"id": "2768e6ca-e199-4433-9e0d-2922aec2099b",



"name": "Sample dashboard",



"owner": "john.smith"



},



{



"id": "1d7d34c6-0eb1-4131-8d29-9022f8e7f530",



"name": "Kubernetes metrics",



"owner": "jane.brown"



}



]



}
```

#### Response code

200

## Related topics

* [Dashboards](/managed/analyze-explore-automate/dashboards-classic "Learn how to create, manage, and use Dynatrace Dashboards Classic.")