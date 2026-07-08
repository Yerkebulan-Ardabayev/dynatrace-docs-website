---
title: Dynatrace Platform Subscription API - GET all subscriptions
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-all
---

# Dynatrace Platform Subscription API - GET all subscriptions

# Dynatrace Platform Subscription API - GET all subscriptions

* Reference
* Published Mar 30, 2023

Lists all Dynatrace Platform Subscriptions of an account.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SubscriptionListDto](#openapi-definition-SubscriptionListDto) | Success. The response contains a list of the account's subscriptions. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `SubscriptionListDto` object

| Element | Type | Description |
| --- | --- | --- |
| data | [SubscriptionSummaryDto](#openapi-definition-SubscriptionSummaryDto)[] | A list of subscriptions of the account. |

#### The `SubscriptionSummaryDto` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | The UUID of the Dynatrace Platform Subscription. |
| type | string | The type of the Dynatrace Platform Subscription. |
| subType | string | The sub-type of the Dynatrace Platform Subscription. |
| name | string | The display name of the Dynatrace Platform Subscription. |
| status | string | The status of the Dynatrace Platform Subscription. |
| startTime | string | The start date of the subscription in `2021-05-01` format. |
| endTime | string | The end date of the subscription in `2021-05-01` format. |

### Response body JSON models

```
{



"data": [



{



"uuid": "string",



"type": "string",



"subType": "string",



"name": "string",



"status": "string",



"startTime": "string",



"endTime": "string"



}



]



}
```