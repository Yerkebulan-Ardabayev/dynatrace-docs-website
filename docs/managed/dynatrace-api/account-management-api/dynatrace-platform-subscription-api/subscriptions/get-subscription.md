---
title: Dynatrace Platform Subscription API - GET a subscription
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-subscription
---

# Dynatrace Platform Subscription API - GET a subscription

# Dynatrace Platform Subscription API - GET a subscription

* Reference
* Published Mar 30, 2023

Gets detailed information about a Dynatrace Platform Subscription.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| subscriptionUuid | string | The UUID of the requested subscription.  Fetch the list of subscriptions via the [GET all subscriptions﻿](https://dt-url.net/jq03jvq) request. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SubscriptionDto](#openapi-definition-SubscriptionDto) | Success. The response contains the details of the subscription. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `SubscriptionDto` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | The UUID of the Dynatrace Platform Subscription. |
| type | string | The type of the Dynatrace Platform Subscription. |
| subType | string | The sub-type of the Dynatrace Platform Subscription. |
| name | string | The display name of the Dynatrace Platform Subscription. |
| status | string | The status of the Dynatrace Platform Subscription. |
| startTime | string | The start date of the subscription in `2021-05-01` format. |
| endTime | string | The end date of the subscription in `2021-05-01` format. |
| account | [SubscriptionAccountDto](#openapi-definition-SubscriptionAccountDto) | The account associated with the subscription. |
| budget | [SubscriptionBudgetDto](#openapi-definition-SubscriptionBudgetDto) | The budget associated with the subscription. |
| currentPeriod | [SubscriptionCurrentPeriodDto](#openapi-definition-SubscriptionCurrentPeriodDto) | The current period associated with the subscription. |
| periods | [SubscriptionPeriodDto](#openapi-definition-SubscriptionPeriodDto)[] | A list of subscription periods. |
| capabilities | [SubscriptionCapabilityDto](#openapi-definition-SubscriptionCapabilityDto)[] | A list of subscription capabilities. |

#### The `SubscriptionAccountDto` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | The UUID of the account. |

#### The `SubscriptionBudgetDto` object

| Element | Type | Description |
| --- | --- | --- |
| total | number | The total budget of the subscription. |
| used | number | The used budget of the subscription. |
| currencyCode | string | The currency of the subscription. |

#### The `SubscriptionCurrentPeriodDto` object

| Element | Type | Description |
| --- | --- | --- |
| startTime | string | The current period start date in `2021-05-01` format. |
| endTime | string | The current period end date in `2021-05-01` format. |
| daysRemaining | number | Remaining days in the current period. |

#### The `SubscriptionPeriodDto` object

| Element | Type | Description |
| --- | --- | --- |
| startTime | string | The subscription period start time in `2021-05-01T15:11:00Z` format. |
| endTime | string | The subscription period end time in `2021-05-01T15:11:00Z` format. |

#### The `SubscriptionCapabilityDto` object

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of the subscription capability. |
| name | string | The display name of the subscription capability. |

### Response body JSON models

```
{



"uuid": "string",



"type": "string",



"subType": "string",



"name": "string",



"status": "string",



"startTime": "string",



"endTime": "string",



"account": {



"uuid": "string"



},



"budget": {



"total": 1,



"used": 1,



"currencyCode": "string"



},



"currentPeriod": {



"startTime": "string",



"endTime": "string",



"daysRemaining": 1



},



"periods": [



{



"startTime": "string",



"endTime": "string"



}



],



"capabilities": [



{



"key": "string",



"name": "string"



}



]



}
```