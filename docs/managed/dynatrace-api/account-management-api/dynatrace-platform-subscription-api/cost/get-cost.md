---
title: Dynatrace Platform Subscription API - GET cost
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost
---

# Dynatrace Platform Subscription API - GET cost

# Dynatrace Platform Subscription API - GET cost

* Reference
* Published Mar 30, 2023

Gets the aggregated costs data for a Dynatrace Platform Subscription.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/cost` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| subscriptionUuid | string | The UUID of the requested subscription.  Fetch the list of subscriptions via the [GET all subscriptions﻿](https://dt-url.net/jq03jvq) request. | path | Required |
| environmentIds | string[] | A list of environments for which you want to read the usage data. To specify several environments, separate them with a comma (`,`). | query | Optional |
| capabilityKeys | string[] | A list of capabilities for which you want to read the usage data. To specify several capabilities, separate them with a comma (`,`).  To obtain capability keys, use the [GET subscriptions﻿](https://dt-url.net/qd43uld) call and look for the **capabilities** field of the response. | query | Optional |
| clusterIds | string[] | A list of Managed clusters for which you want to read the usage data.  Not applicable to SaaS environments. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SubscriptionCostListDto](#openapi-definition-SubscriptionCostListDto) | Success. The response contains the costs of the subscription, split by date. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `SubscriptionCostListDto` object

| Element | Type | Description |
| --- | --- | --- |
| data | [SubscriptionCostBookingDto](#openapi-definition-SubscriptionCostBookingDto)[] | Cost data of the subscription. |
| lastModifiedTime | string | The time the subscription data was last modified in `2021-05-01T15:11:00Z` format. |

#### The `SubscriptionCostBookingDto` object

| Element | Type | Description |
| --- | --- | --- |
| startTime | string | The start time for the capability cost in `2021-05-01T15:11:00Z` format. |
| endTime | string | The end time for the capability cost in `2021-05-01T15:11:00Z` format. |
| value | number | The total cost for all the capabilities. |
| currencyCode | string | The currency of the cost. |
| lastBookingDate | string | The last booking date for the capability cost |

### Response body JSON models

```
{



"data": [



{



"startTime": "string",



"endTime": "string",



"value": 1,



"currencyCode": "string",



"lastBookingDate": "string"



}



],



"lastModifiedTime": "string"



}
```