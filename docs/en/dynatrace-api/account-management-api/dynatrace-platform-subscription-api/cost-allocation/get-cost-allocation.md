---
title: Dynatrace Platform Subscription API - GET cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation
scraped: 2026-02-17T05:06:25.244049
---

# Dynatrace Platform Subscription API - GET cost allocation

# Dynatrace Platform Subscription API - GET cost allocation

* Latest Dynatrace
* Reference
* Published Oct 18, 2024

Lists Dynatrace Platform Subscription usage data by cost allocation field.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com/v1/subscriptions/{subscription-uuid}/cost-allocation`

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| subscription-uuid | string | The UUID of the requested subscription.  Fetch the list of subscriptions via the [GET all subscriptionsï»¿](https://dt-url.net/jq03jvq) request. (required) | path | Required |
| field | string | Field by which costs and usage should be split. Allowed values: `COSTCENTER`, `PRODUCT` (required unless page-key is provided) | query | Required |
| environment-id | string | The identifier of an environment. (required unless page-key is provided) | query | Optional |
| from | string | The start of the requested timeframe in `2021-05-01` format. | query | Optional |
| to | string | The end of the requested timeframe in `2021-05-01` format. | query | Optional |
| page-size | number | Defines the requested number of entries for the next page. | query | Optional |
| page-key | string | A base64 encoded key to retrieve a specific page. If this query parameter is set, no other query parameters can be set. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PaginatedEnvironmentBreakdownDto](#openapi-definition-PaginatedEnvironmentBreakdownDto) | Success. The response contains a page of the requested chargeback breakdown. |
| **400** | - | The request was unacceptable, often due to missing a required parameter |
| **401** | - | No valid session provided |
| **403** | - | Access denied |
| **500** | - | Something went wrong on Account Management's end |

### Response body objects

#### The `PaginatedEnvironmentBreakdownDto` object

| Element | Type | Description |
| --- | --- | --- |
| environmentId | string | Identifier of the environment |
| field | string | Field used to generate the breakdown. Can be `COSTCENTER` or `PRODUCT` |
| records | string[] | List of individual breakdown entries. |
| nextPageKey | string | Key to request the next page. |

### Response body JSON models

```
{



"environmentId": "string",



"field": "string",



"records": [



"string"



],



"nextPageKey": "string"



}
```

## Related topics

* [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.")