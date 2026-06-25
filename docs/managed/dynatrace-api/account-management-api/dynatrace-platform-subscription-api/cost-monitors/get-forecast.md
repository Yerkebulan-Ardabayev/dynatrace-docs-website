---
title: Dynatrace Platform Subscription API - GET forecast
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-monitors/get-forecast
scraped: 2026-05-12T11:24:38.413735
---

# Dynatrace Platform Subscription API - GET forecast

# Dynatrace Platform Subscription API - GET forecast

* Reference
* Published Aug 30, 2023

Gets a forecast of Dynatrace Platform Subscription usage by the end of the annual commitment period.

The request produces an `application/json` payload.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/forecast` |

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
| **200** | [Forecast](#openapi-definition-Forecast) | Success. The response contains the forecast of the subscription's usage. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `Forecast` object

| Element | Type | Description |
| --- | --- | --- |
| forecastMedian | number | The median forecasted usage. |
| forecastLower | number | The lower bound of forecasted usage. |
| forecastUpper | number | The upper bound of forecasted usage. |
| budget | number | The budget quota used in the forecast. |
| forecastBudgetPct | number | The forecasted usage of the budget, in percent. |
| forecastBudgetDate | string | The date when the forecasted usage consumes all the budget quota. |
| forecastCreatedAt | string | The date when the forecast was created. |

### Response body JSON models

```
{



"forecastMedian": 1,



"forecastLower": 1,



"forecastUpper": 1,



"budget": 1,



"forecastBudgetPct": 1,



"forecastBudgetDate": "string",



"forecastCreatedAt": "string"



}
```