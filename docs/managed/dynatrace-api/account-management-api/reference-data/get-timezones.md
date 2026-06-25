---
title: Reference data API - GET time zones
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/reference-data/get-timezones
scraped: 2026-05-12T11:24:40.979212
---

# Reference data API - GET time zones

# Reference data API - GET time zones

* Reference
* Published Jul 25, 2022

Lists all time zones that your account uses.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/ref/v1/time-zones` |

## Authentication

To execute this request, you need the **Allow read access for environment resources** (`account-env-read`) scope assigned to your token. To learn how to obtain and use it.

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [TimeZoneDto[]](#openapi-definition-TimeZoneDto) | Success. The response contains the list of time zones. |

### Response body objects

#### The `ResponseBody` object

#### The `TimeZoneDto` object

| Element | Type | Description |
| --- | --- | --- |
| displayName | string | The UTC-based name of the time zone. |
| name | string | The standard name of the time zone. |

### Response body JSON models

```
[



{



"displayName": "string",



"name": "string"



}



]
```

## Example

In this example, the request lists all time zones of the account with the UUID of **9ad20784-76c6-4167-bfba-9b0d8d72a71d**. The result is truncated to three entries.

#### Curl

```
curl --request GET \



--url https://api.dynatrace.com/ref/v1/time-zones \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/ref/v1/time-zones
```

#### Response body

```
[



{



"displayName": "UTC+00:00 Universal Time Coordinated",



"name": "UTC"



},



{



"displayName": "UTC-07:00 Arizona",



"name": "America/Arizona"



},



{



"displayName": "UTC+01:00 Central European Time",



"name": "Europe/Berlin"



}



]
```

#### Response code

200