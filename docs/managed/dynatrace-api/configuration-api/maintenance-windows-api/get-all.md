---
title: Maintenance windows API - GET all maintenance windows
source: https://docs.dynatrace.com/managed/dynatrace-api/configuration-api/maintenance-windows-api/get-all
scraped: 2026-05-12T12:06:29.763567
---

# Maintenance windows API - GET all maintenance windows

# Maintenance windows API - GET all maintenance windows

* Reference
* Updated on Apr 28, 2020

This API is deprecated. Use the [Settings API](/managed/dynatrace-api/environment-api/settings "Find out what the Dynatrace Settings API offers.") with the **Maintenance windows** (`builtin:alerting.maintenance-window`) schema instead.

Lists all maintenance windows available in your Dynatrace environment.

The request produces an `application/json` payload.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/config/v1/maintenanceWindows` |

## Authentication

To execute this request, you need an access token with `ReadConfig` scope.

To learn how to obtain and use it, see [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [StubList](#openapi-definition-StubList) | Success |

### Response body objects

#### The `StubList` object

An ordered list of short representations of Dynatrace entities.

| Element | Type | Description |
| --- | --- | --- |
| values | [EntityShortRepresentation[]](#openapi-definition-EntityShortRepresentation) | An ordered list of short representations of Dynatrace entities. |

#### The `EntityShortRepresentation` object

The short representation of a Dynatrace entity.

| Element | Type | Description |
| --- | --- | --- |
| description | string | A short description of the Dynatrace entity. |
| id | string | The ID of the Dynatrace entity. |
| name | string | The name of the Dynatrace entity. |

### Response body JSON models

```
{



"values": [



{



"description": "Dynatrace entity 1 for the REST API example",



"id": "6a98d7bc-abb9-44f8-ae6a-73e68e71812a",



"name": "Dynatrace entity 1"



},



{



"id": "ee70f7d3-9a4e-4f5f-94d2-c9d6156f1618",



"name": "Dynatrace entity 2"



},



{



"id": "8cdabe77-9e1a-4be8-b3df-269dd6fa9d7f"



}



]



}
```

## Example

In this example, the request asks for a list of all the maintenance windows in the **mySampleEnv** environment.

The API token is passed in the **Authorization** header.

The result is truncated to three entries.

#### Curl

```
curl -X GET \



"https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows" \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### Request URL

```
https://mySampleEnv.live.dynatrace.com/api/config/v1/maintenanceWindows
```

#### Response body

```
{



"values": [



{



"id": "0cd96661-07d9-42da-b2cc-19f22bb9f297",



"name": "Planned server downtime",



"description": "We plan to upgrade the server."



},



{



"id": "b2c61cb1-547c-312f-b2ab-fda372516e8f",



"name": "Monthly maintenance",



"description": "Monthly maintenance of the hardware"



},



{



"id": "0c1882ed-8f20-4e04-8505-05bdfb086ae8",



"name": "New app version deployment",



"description": "Deploy new version of the main app"



}



]



}
```

#### Response code

200

## Related topics

* [Maintenance windows](/managed/analyze-explore-automate/notifications-and-alerting/maintenance-windows "Understand when to use a maintenance window. Read about the supported maintenance window types.")