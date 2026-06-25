---
title: Dynatrace Platform Subscription API - GET cost per environment
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost-environment
scraped: 2026-05-12T11:24:35.549083
---

# Dynatrace Platform Subscription API - GET cost per environment

# Dynatrace Platform Subscription API - GET cost per environment

* Reference
* Published Mar 30, 2023

Gets the cost data for a Dynatrace Platform Subscription split by monitoring environment.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v3/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/environments/cost` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| subscriptionUuid | string | The UUID of the requested subscription.  Fetch the list of subscriptions via the [GET all subscriptionsï»¿](https://dt-url.net/jq03jvq) request. | path | Required |
| startTime | string | The start time of the query in `2021-05-01T15:11:00Z` format. Timeframe limits (startTime, endTime) are both required, unless a "page-key" is provided instead. | query | Optional |
| endTime | string | The end time of the query in `2021-05-01T15:11:00Z` format. Timeframe limits (startTime, endTime) are both required, unless a "page-key" is provided instead. | query | Optional |
| environmentIds | string[] | A list of environments for which you want to read the usage data. To specify several environments, separate them with a comma (`,`). | query | Optional |
| capabilityKeys | string[] | A list of capabilities for which you want to read the usage data. To specify several capabilities, separate them with a comma (`,`).  To obtain capability keys, use the [GET subscriptionsï»¿](https://dt-url.net/qd43uld) call and look for the **capabilities** field of the response. | query | Optional |
| clusterIds | string[] | A list of Managed clusters for which you want to read the usage data.  Not applicable to SaaS environments. | query | Optional |
| page-key | string | The cursor for the next page of results. You can find it in the **nextPageKey** field of the previous response. | query | Optional |
| page-size | number | Defines the requested number of entries for the next page. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SubscriptionEnvironmentCostListV3Dto](#openapi-definition-SubscriptionEnvironmentCostListV3Dto) | Success. The response contains the costs of the subscription, split by environment. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `SubscriptionEnvironmentCostListV3Dto` object

| Element | Type | Description |
| --- | --- | --- |
| data | [SubscriptionEnvironmentCostV3Dto[]](#openapi-definition-SubscriptionEnvironmentCostV3Dto) | Subscription cost data |
| lastModifiedTime | string | The time the subscription data was last modified in `2021-05-01T15:11:00Z` format. |
| nextPageKey | string | The next page key for pagination if next page exists |

#### The `SubscriptionEnvironmentCostV3Dto` object

| Element | Type | Description |
| --- | --- | --- |
| clusterId | string | The UUID of the Managed cluster |
| environmentId | string | The UUID of the environment. |
| cost | [SubscriptionCapabilityCostReceivedDto[]](#openapi-definition-SubscriptionCapabilityCostReceivedDto) | Subscription costs for the environment. |

#### The `SubscriptionCapabilityCostReceivedDto` object

| Element | Type | Description |
| --- | --- | --- |
| startTime | string | The start time for the capability cost in `2021-05-01T15:11:00Z` format. |
| endTime | string | The end time for the capability cost in `2021-05-01T15:11:00Z` format. |
| value | number | The total cost for all the capabilities. |
| currencyCode | string | The currency of the cost. |
| capabilityKey | string | The key of the subscription capability. |
| capabilityName | string | The display name of the subscription capability. |
| bookingDate | string | The booking date of the subscription capability in `2021-05-01T15:11:00Z` format. |

### Response body JSON models

```
{



"data": [



{



"clusterId": "string",



"environmentId": "string",



"cost": [



{



"startTime": "string",



"endTime": "string",



"value": 1,



"currencyCode": "string",



"capabilityKey": "string",



"capabilityName": "string",



"bookingDate": "string"



}



]



}



],



"lastModifiedTime": "string",



"nextPageKey": "string"



}
```