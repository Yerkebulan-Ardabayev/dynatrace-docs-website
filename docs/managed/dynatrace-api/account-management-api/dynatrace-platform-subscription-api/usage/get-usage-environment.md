---
title: Dynatrace Platform Subscription API - GET usage per environment
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage-environment
scraped: 2026-05-12T11:24:34.119885
---

# Dynatrace Platform Subscription API - GET usage per environment

# Dynatrace Platform Subscription API - GET usage per environment

* Reference
* Published Mar 30, 2023

Gets the usage data for a Dynatrace Platform Subscription split by monitoring environment.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/environments/usage` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required SaaS account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| subscriptionUuid | string | The UUID of the requested subscription.  Fetch the list of subscriptions via the [GET all subscriptionsï»¿](https://dt-url.net/jq03jvq) request. | path | Required |
| startTime | string | The start of the requested timeframe in `2021-05-01T15:11:00Z` format. | query | Required |
| endTime | string | The end of the requested timeframe in `2021-05-01T15:11:00Z` format. | query | Required |
| environmentIds | string[] | A list of environments for which you want to read the usage data. To specify several environments, separate them with a comma (`,`). | query | Optional |
| capabilityKeys | string[] | A list of capabilities for which you want to read the usage data. To specify several capabilities, separate them with a comma (`,`).  To obtain capability keys, use the [GET subscriptionsï»¿](https://dt-url.net/qd43uld) call and look for the **capabilities** field of the response. | query | Optional |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [SubscriptionEnvironmentUsageListV2Dto](#openapi-definition-SubscriptionEnvironmentUsageListV2Dto) | Success. The response contains the usage data of the subscription, split by environment. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `SubscriptionEnvironmentUsageListV2Dto` object

| Element | Type | Description |
| --- | --- | --- |
| data | [SubscriptionEnvironmentUsageV2Dto[]](#openapi-definition-SubscriptionEnvironmentUsageV2Dto) | Usage data of the subscription. |
| lastModifiedTime | string | The time the subscription data was last modified in `2021-05-01T15:11:00Z` format. |

#### The `SubscriptionEnvironmentUsageV2Dto` object

| Element | Type | Description |
| --- | --- | --- |
| environmentId | string | The UUID of the environment |
| usage | [SubscriptionUsageDto[]](#openapi-definition-SubscriptionUsageDto) | A list of subscription usage for the environment. |

#### The `SubscriptionUsageDto` object

| Element | Type | Description |
| --- | --- | --- |
| capabilityKey | string | The key of the subscription capability. |
| capabilityName | string | The display name of the subscription capability. |
| startTime | string | The start time of the capability usage in `2021-05-01T15:11:00Z` format. |
| endTime | string | The end time of the capability usage in `2021-05-01T15:11:00Z` format. |
| value | number | The subscription usage by the capability. |
| unitMeasure | string | The unit of the capability usage. |

### Response body JSON models

```
{



"data": [



{



"environmentId": "string",



"usage": [



{



"capabilityKey": "string",



"capabilityName": "string",



"startTime": "string",



"endTime": "string",



"value": 1,



"unitMeasure": "string"



}



]



}



],



"lastModifiedTime": "string"



}
```