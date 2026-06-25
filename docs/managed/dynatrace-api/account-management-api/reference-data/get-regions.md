---
title: Reference data API - GET geographical regions
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/reference-data/get-regions
scraped: 2026-05-12T11:24:42.135733
---

# Reference data API - GET geographical regions

# Reference data API - GET geographical regions

* Reference
* Published Jul 25, 2022

Lists all geographical regions that your account uses.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/ref/v1/regions` |

## Authentication

To execute this request, you need the **Allow read access for environment resources** (`account-env-read`) scope assigned to your token. To learn how to obtain and use it.

## Parameters

The request doesn't provide any configurable parameters.

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [RegionDto[]](#openapi-definition-RegionDto) | Success. The response contains the list of regions. |

### Response body objects

#### The `ResponseBody` object

#### The `RegionDto` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the region. |

### Response body JSON models

```
[



{



"name": "string"



}



]
```

## Example

In this example, the request lists all regions of the account with the UUID of **9ad20784-76c6-4167-bfba-9b0d8d72a71d**. The result is truncated to two entries.

#### Curl

```
curl --request GET \



--url https://api.dynatrace.com/ref/v1/regions \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/ref/v1/regions
```

#### Response body

```
[



{



"name": "US East Virginia"



},



{



"name": "US West Oregon"



}



]
```

#### Response code

200