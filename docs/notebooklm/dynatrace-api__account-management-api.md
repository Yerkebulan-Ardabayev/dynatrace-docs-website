# Dynatrace Documentation: dynatrace-api/account-management-api

Generated: 2026-02-16

Files combined: 11

---


## Source: account-limits-api.md


---
title: Account limits API
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/account-limits-api
scraped: 2026-02-16T09:27:31.393325
---

# Account limits API

# Account limits API

* Latest Dynatrace
* Reference
* Published Dec 04, 2025

[### List account limits

Get an overview of account limits assigned to your Dynatrace account.](/docs/dynatrace-api/account-management-api/account-limits-api/get-account-limits "Get a list of assigned account limits via the Dynatrace API.")


---


## Source: get-cost-allocation.md


---
title: Dynatrace Platform Subscription API - GET cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation
scraped: 2026-02-16T09:40:11.276692
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


---


## Source: manage-cost-allocation.md


---
title: Dynatrace Platform Subscription API - manage cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/manage-cost-allocation
scraped: 2026-02-16T09:37:46.364546
---

# Dynatrace Platform Subscription API - manage cost allocation

# Dynatrace Platform Subscription API - manage cost allocation

* Latest Dynatrace
* Reference
* Published Oct 18, 2024

The Dynatrace Cost Allocation feature incorporates two fields for cost centers and products. You can use either or both fields. These fields reflect your company's cost allocation structure, enabling you to develop two distinct perspectives: one based on your cost centers (for example, departments) and another based on your products or services (for example, Applicationname or ApplicationID). Of course, you can customize the use of these fields to fit your company's organizational framework.

Use Dynatrace Platform Subscription API to manage your products and cost centers at scale.

## GET cost centers

Lists all the defined cost centers.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/costcenters`

### Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| page | number | The number of the requested page. Can be increased as long as **hasNextPage** is true in the response. | query | Optional |
| page-size | number | Defines the requested number of entries for the next page. | query | Optional |

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PaginatedFieldValueDto](#openapi-definition-PaginatedFieldValueDto) | Success. The response contains a page of allowed cost-allocation values for the costcenter field. |
| **400** | - | The request was unacceptable, often due to missing a required parameter |
| **401** | - | No valid session provided |
| **403** | - | Access denied |
| **500** | - | Something went wrong on Account Management's end |

### Response body objects

#### The `PaginatedFieldValueDto` object

| Element | Type | Description |
| --- | --- | --- |
| records | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The records on the current page. |
| hasNextPage | boolean | Indicates if there is another page to load. |

#### The `FieldValueDto` object

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of this value. |

### Response body JSON models

```
{



"records": [



{



"key": "string"



}



],



"hasNextPage": true



}
```

## POST cost centers

Add the provided value to the cost center field.

The request produces an `application/json` payload.

POST

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/costcenters`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| body | [FieldValuesRequestDto](#openapi-definition-FieldValuesRequestDto) | - | body | Required |

### Request body objects

#### The `FieldValuesRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| values | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The requested values. | Required |

#### The `FieldValueDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | The key of this value. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"values": [



{



"key": "string"



}



]



}
```

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The response doesn't have a body. The values were added to the field. |
| **400** | The existing and provided values combined should not contain duplicate keys. |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## PUT cost centers

Replace the current values to the cost center field.

The request produces an `application/json` payload.

PUT

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/costcenters`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| body | [FieldValuesRequestDto](#openapi-definition-FieldValuesRequestDto) | - | body | Required |

### Request body objects

#### The `FieldValuesRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| values | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The requested values. | Required |

#### The `FieldValueDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | The key of this value. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"values": [



{



"key": "string"



}



]



}
```

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The response doesn't have a body. The values of the field were replaced. |
| **400** | The provided values should not contain duplicate keys. |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## DELETE cost centers

Delete a value by key on the cost center field.

The request produces an `application/json` payload.

DELETE

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/costcenters/{key}`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| key | string | The key for the field value. | path | Required |

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The given value on the costcenter field was deleted. |
| **400** | The request was unacceptable, often due to missing a required parameter |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## GET products

Lists all the defined products.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/products`

### Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| page | number | The number of the requested page. Can be increased as long as **hasNextPage** is true in the response. | query | Optional |
| page-size | number | Defines the requested number of entries for the next page. | query | Optional |

### Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PaginatedFieldValueDto](#openapi-definition-PaginatedFieldValueDto) | Success. The response contains a page of allowed cost-allocation values for the product field. |
| **400** | - | The request was unacceptable, often due to missing a required parameter |
| **401** | - | No valid session provided |
| **403** | - | Access denied |
| **500** | - | Something went wrong on Account Management's end |

### Response body objects

#### The `PaginatedFieldValueDto` object

| Element | Type | Description |
| --- | --- | --- |
| records | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The records on the current page. |
| hasNextPage | boolean | Indicates if there is another page to load. |

#### The `FieldValueDto` object

| Element | Type | Description |
| --- | --- | --- |
| key | string | The key of this value. |

### Response body JSON models

```
{



"records": [



{



"key": "string"



}



],



"hasNextPage": true



}
```

## POST products

Add the provided value to the product field.

The request produces an `application/json` payload.

POST

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/products`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| body | [FieldValuesRequestDto](#openapi-definition-FieldValuesRequestDto) | - | body | Required |

### Request body objects

#### The `FieldValuesRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| values | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The requested values. | Required |

#### The `FieldValueDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | The key of this value. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"values": [



{



"key": "string"



}



]



}
```

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The response doesn't have a body. The values were added to the field. |
| **400** | The existing and provided values combined should not contain duplicate keys. |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## PUT products

Replace the current values to the product field.

The request produces an `application/json` payload.

PUT

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/products`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| body | [FieldValuesRequestDto](#openapi-definition-FieldValuesRequestDto) | - | body | Required |

### Request body objects

#### The `FieldValuesRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| values | [FieldValueDto[]](#openapi-definition-FieldValueDto) | The requested values. | Required |

#### The `FieldValueDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| key | string | The key of this value. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"values": [



{



"key": "string"



}



]



}
```

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The response doesn't have a body. The values of the field were replaced. |
| **400** | The provided values should not contain duplicate keys. |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## DELETE products

Delete a value by key on the cost center field.

The request produces an `application/json` payload.

DELETE

`https://api.dynatrace.com//v1/accounts/{accountUuid}/settings/products/{key}`

## Authentication

To execute this request, you need the **Allow write access for usage and consumption resources** (`account-uac-write`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| key | string | The key for the field value. | path | Required |

### Response

### Response codes

| Code | Description |
| --- | --- |
| **204** | The given value on the product field was deleted. |
| **400** | The request was unacceptable, often due to missing a required parameter |
| **401** | No valid session provided |
| **403** | Access denied |
| **500** | Something went wrong on Account Management's end |

## Related topics

* [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.")


---


## Source: cost-allocation.md


---
title: Dynatrace Platform Subscription API - Cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation
scraped: 2026-02-16T09:31:35.419046
---

# Dynatrace Platform Subscription API - Cost allocation

# Dynatrace Platform Subscription API - Cost allocation

* Latest Dynatrace
* Reference
* Published Oct 18, 2024

[![cost-allocation](https://cdn.bfldr.com/B686QPH3/at/9vhmq6x4kh88sq7hq4qbwg9t/DT0634.svg?auto=webp&width=72&height=72 "cost-allocation")

### View cost allocation

See how Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation "See how Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.")[![cost-allocation](https://cdn.bfldr.com/B686QPH3/at/9vhmq6x4kh88sq7hq4qbwg9t/DT0634.svg?auto=webp&width=72&height=72 "cost-allocation")

### Manage cost allocation

Manage Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/manage-cost-allocation "Manage Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.")

## Related topics

* [Allocate your DPS costs](/docs/license/cost-allocation "Learn how to allocate costs to cost centers and products.")


---


## Source: dynatrace-platform-subscription-api.md


---
title: Dynatrace Platform Subscription API
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api
scraped: 2026-02-16T09:35:35.837929
---

# Dynatrace Platform Subscription API

# Dynatrace Platform Subscription API

* Latest Dynatrace
* Reference
* Published Mar 30, 2023

[### List subscriptions

Get an overview of your subscriptions.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-all "List all Dynatrace Platform Subscriptions via the Account Management API.")[### View subscription

Check the details of a subscription.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-subscription "View info about a Dynatrace Platform Subscription via the Account Management API.")

## Usage

[### View usage

Get an overview of how your Dynatrace Platform Subscription is used.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage "Check how your Dynatrace Platform Subscription is used via the Account Management API.")[### View usage per environment

See how every monitoring environment consumes your Dynatrace Platform Subscription.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage-environment "Check how every monitoring environment consumes your Dynatrace Platform Subscription via the Account Management API.")

## Cost

[### View cost

Get an overview of the costs of your Dynatrace Platform Subscription.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost "Check the cost of your Dynatrace Platform Subscription via the Account Management API.")[### View cost per environment

See how much every monitoring environment contributes to the cost of your Dynatrace Platform Subscription.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost-environment "Check the cost of your Dynatrace Platform Subscription per environment via the Account Management API.")

## Cost monitor

[### View cost forecast

Get a forecasted cost of your Dynatrace Platform Subscription.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-monitors/get-forecast "Automate the management of your Dynatrace Platform Subscription via our API.")[### View cost events

Get cost and forecast events detected by Account Management.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-monitors/get-events "Automate the management of your Dynatrace Platform Subscription via our API.")

## Cost allocation

[![cost-allocation](https://cdn.bfldr.com/B686QPH3/at/9vhmq6x4kh88sq7hq4qbwg9t/DT0634.svg?auto=webp&width=72&height=72 "cost-allocation")

### View cost allocation

See how Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation "See how Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.")[![cost-allocation](https://cdn.bfldr.com/B686QPH3/at/9vhmq6x4kh88sq7hq4qbwg9t/DT0634.svg?auto=webp&width=72&height=72 "cost-allocation")

### Manage cost allocation

Manage Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.](/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/manage-cost-allocation "Manage Dynatrace Platform Subscription cost and usage are allocated to product and cost centers.")


---


## Source: platform-tokens-api.md


---
title: Platform tokens API
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/platform-tokens-api
scraped: 2026-02-16T09:39:19.074075
---

# Platform tokens API

# Platform tokens API

* Latest Dynatrace
* Reference
* Published Dec 04, 2025

[### List all platform tokens

Get an overview of all platform tokens in your Dynatrace account.](/docs/dynatrace-api/account-management-api/platform-tokens-api/get-all-platform-tokens "Get an overview of platform tokens in your Dynatrace account via the Dynatrace API.")[### Delete a platform token

Delete a platform token.](/docs/dynatrace-api/account-management-api/platform-tokens-api/delete-platform-token "Delete a platform token from your Dynatrace account via the Dynatrace API.")[### Edit a platform token's expiration date

Edit the expiration date of a platform token.](/docs/dynatrace-api/account-management-api/platform-tokens-api/put-platform-token-exp-date "Edit a platform token in your Dynatrace account via the Dynatrace API.")[### Edit a platform token's status

Edit the status of a platform token.](/docs/dynatrace-api/account-management-api/platform-tokens-api/put-platform-token-status "Edit a platform token in your Dynatrace account via the Dynatrace API.")


---


## Source: delete-boundary.md


---
title: Policy management API - DELETE a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/delete-boundary
scraped: 2026-02-16T09:33:43.021931
---

# Policy management API - DELETE a policy boundary

# Policy management API - DELETE a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Deletes a policy boundary by uuid within a level. You can't delete a global-level boundary, as these are managed by Dynatrace.

DELETE

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | The ID of the required boundary. | path | Required |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **204** | - | Successful response - policy boundary deleted |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The request is invalid |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Example

In this example, the request deletes a policy boundary with policy boundary `UUID` of **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** for the `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request DELETE \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345 \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Response code

204 - Successful response - policy boundary deleted.


---


## Source: get-boundary.md


---
title: Policy management API - GET a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/get-boundary
scraped: 2026-02-16T09:38:23.952905
---

# Policy management API - GET a policy boundary

# Policy management API - GET a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Gets a policy boundary within a level.

The request produces an `application/json` payload.

GET

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | The ID of the required boundary. | path | Required |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Successful response - policy boundary |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `PolicyBoundaryOverview` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | The display name of the policy boundary. |
| boundaryQuery | string | The boundary query of the policy boundary. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. |

#### The `Condition` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the condition.  It indicates which part of the **services** is checked by the condition. |
| operator | string | The operator of the condition. |
| values | string[] | A list of reference values of the condition. |

#### The `Map` object

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"uuid": "string",



"levelType": "string",



"levelId": "string",



"name": "string",



"boundaryQuery": "string",



"boundaryConditions": [



{



"name": "string",



"operator": "string",



"values": [



"string"



]



}



],



"metadata": {}



}
```

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Example

In this example, the request retrieves the details of the policy boundary with the UUID of **9a7b6c54-3d2e-4f10-a8b2-7cde9012f345** for the account with the `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request GET \



--url 'https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345' \



--header 'Authorization: Bearer abcdefjhij1234567890'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/9a7b6c54-3d2e-4f10-a8b2-7cde9012f345
```

#### Response body

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bndry_teamA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AB\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-A"



]



}



],



"metadata": {}



}
```

#### Response code

200 - Successful response - policy boundary.


---


## Source: post-boundary.md


---
title: Policy management API - POST a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary
scraped: 2026-02-15T21:24:26.820977
---

# Policy management API - POST a policy boundary

# Policy management API - POST a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Creates a new policy boundary within a level. You can't create a global-level boundary, as these are managed by Dynatrace.

The request consumes and produces an `application/json` payload.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains new policy boundary | body | Required |

### Request body objects

#### The `PolicyBoundaryDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy boundary. | Required |
| boundaryQuery | string | The boundary query of the policy boundary. | Required |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. | Required |

#### The `Map` object

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Successful response - policy boundary created |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The request is invalid |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `PolicyBoundaryOverview` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | The display name of the policy boundary. |
| boundaryQuery | string | The boundary query of the policy boundary. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. |

#### The `Condition` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the condition.  It indicates which part of the **services** is checked by the condition. |
| operator | string | The operator of the condition. |
| values | string[] | A list of reference values of the condition. |

#### The `Map` object

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"uuid": "string",



"levelType": "string",



"levelId": "string",



"name": "string",



"boundaryQuery": "string",



"boundaryConditions": [



{



"name": "string",



"operator": "string",



"values": [



"string"



]



}



],



"metadata": {}



}
```

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **200** indicates a valid payload.

The request consumes an `application/json` payload.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/validation`

### Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains new policy boundary | body | Required |

### Request body objects

#### The `PolicyBoundaryDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy boundary. | Required |
| boundaryQuery | string | The boundary query of the policy boundary. | Required |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. | Required |

#### The `Map` object

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Example

In this example, the request creates a new policy boundary within a level. It a new policy boundary for the `accountID` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request POST \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries \



--header 'accept: application/json' \



--header 'Authorization: Bearer abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "name_string",



"boundaryQuery": "boundaryQuery",



"metadata": {}



}'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries
```

#### Request body

```
{



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"metadata": {}



}
```

#### Response body

```
{



"uuid": "9a7b6c54-3d2e-4f10-a8b2-7cde9012f345",



"levelType": "account",



"levelId": "f1a2b3c4-d5e6-7890-ab12-34cd56ef7890",



"name": "bnd_teamAA",



"boundaryQuery": "storage:dt.security_context = \"TEAM-AA\";",



"boundaryConditions": [



{



"name": "storage:dt.security_context",



"operator": "EQ",



"values": [



"TEAM-AA"



]



}



],



"metadata": {}



}
```

#### Response code

201 - Successful response - policy boundary created.


---


## Source: put-boundary.md


---
title: Policy management API - PUT a policy boundary
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/put-boundary
scraped: 2026-02-16T09:32:15.838619
---

# Policy management API - PUT a policy boundary

# Policy management API - PUT a policy boundary

* Latest Dynatrace
* Reference
* Published Nov 20, 2025

Updates or creates a policy boundary by uuid within a level. You can't edit a global-level boundary, as these are managed by Dynatrace.

If the specified boundary doesn't exist, a [new boundary is created](/docs/dynatrace-api/account-management-api/policy-management-api/boundaries/post-boundary "Create a new boundary via the Policy management API.") instead.

The request consumes and produces an `application/json` payload.

PUT

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}`

## Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyBoundaryUuid | - | The ID of the required boundary. | path | Required |
| accountId | - | The ID of the policy boundary level. Use the UUID of the account. | path | Required |
| body | [PolicyBoundaryDto](#openapi-definition-PolicyBoundaryDto) | The JSON body of the request. Contains policy boundary | body | Required |

### Request body objects

#### The `PolicyBoundaryDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy boundary. | Required |
| boundaryQuery | string | The boundary query of the policy boundary. | Required |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. | Required |

#### The `Map` object

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"boundaryQuery": "string",



"metadata": {}



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **201** | [PolicyBoundaryOverview](#openapi-definition-PolicyBoundaryOverview) | Successful response - policy boundary created |
| **204** | - | Successful response - policy boundary updated |
| **400** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The request is invalid |
| **404** | [ErrorDto](#openapi-definition-ErrorDto) | Failed. The specified resource is not found. |

### Response body objects

#### The `PolicyBoundaryOverview` object

| Element | Type | Description |
| --- | --- | --- |
| uuid | string | - |
| levelType | string | - |
| levelId | string | - |
| name | string | The display name of the policy boundary. |
| boundaryQuery | string | The boundary query of the policy boundary. |
| boundaryConditions | [Condition[]](#openapi-definition-Condition) | - |
| metadata | [Map](#openapi-definition-Map) | The metadata of the policy boundary. |

#### The `Condition` object

| Element | Type | Description |
| --- | --- | --- |
| name | string | The name of the condition.  It indicates which part of the **services** is checked by the condition. |
| operator | string | The operator of the condition. |
| values | string[] | A list of reference values of the condition. |

#### The `Map` object

#### The `ErrorDto` object

| Element | Type | Description |
| --- | --- | --- |
| code | number | The code of the error. |
| message | string | A short description of the error. |
| errorsMap | object | - |

### Response body JSON models

```
{



"uuid": "string",



"levelType": "string",



"levelId": "string",



"name": "string",



"boundaryQuery": "string",



"boundaryConditions": [



{



"name": "string",



"operator": "string",



"values": [



"string"



]



}



],



"metadata": {}



}
```

```
{



"code": 1,



"message": "string",



"errorsMap": {}



}
```

## Validate payload

We recommend that you validate the payload before submitting it with an actual request. A response code of **200** indicates a valid payload.

The request consumes an `application/json` payload.

POST

`https://api.dynatrace.com/iam/v1/repo/account/{accountId}/boundaries/{policyBoundaryUuid}/validation/{policyUuid}`

### Authentication

To execute this request, you need the **Allow IAM policy configuration for environments** (`iam-policies-management`) permission assigned to your token. To learn how to obtain and use it, see [OAuth clients](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

### Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| policyUuid | - | The ID of the policy to be validated. | path | Required |
| levelId | - | The ID of the policy level. Use one of the following values, depending on the level type:  * account: use the UUID of the account. * environment: use the ID of the environment. | path | Required |
| levelType | - | The type of the [policyï»¿](https://dt-url.net/eu03uap) level. The following values are available:  * `account`: An account policy applies to all environments of an account. * `environment`: An environment policy applies to a specific environment.  Each level inherits the policies of the higher level and extends them with its own policies. | path | Required |
| body | [CreateOrUpdateLevelPolicyRequestDto](#openapi-definition-CreateOrUpdateLevelPolicyRequestDto) | The JSON body of the request. Contains the configuration of a policy to be validated. | body | Required |

### Request body objects

#### The `CreateOrUpdateLevelPolicyRequestDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| name | string | The display name of the policy. | Required |
| description | string | A short description of the policy. | Required |
| tags | string[] | A list of tags. | Optional |
| statementQuery | string | The [statementï»¿](https://dt-url.net/ht03ucb) of the policy. | Required |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"name": "string",



"description": "string",



"tags": [



"string"



],



"statementQuery": "string"



}
```

## Example

In this example, the request updates the `name` of the policy boundary with `UUID` of **3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68** for the account with the `accountId` **f1a2b3c4-d5e6-7890-ab12-34cd56ef7890**.

#### Curl

```
curl --request PUT \



--url https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68 \



--header 'Authorization: Bearer abcdefjhij1234567890' \



--header 'Content-Type: application/json' \



--data '{



"name": "host name",



"description": "storage:host.name = \"myHost\"",



"metadata": {}



}'
```

#### Request URL

```
https://api.dynatrace.com/iam/v1/repo/account/f1a2b3c4-d5e6-7890-ab12-34cd56ef7890/boundaries/3c9f1a72-bd84-4e6c-9f03-7a1e2c4d5b68
```

#### Request body

```
{



"name": "host name",



"boundaryQuery": "storage:host.name = \"myHost\";",



"metadata": {}



}
```

#### Response code

204 - Successful response - policy boundary updated.


---


## Source: service-user-management-api.md


---
title: Service user management API
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/service-user-management-api
scraped: 2026-02-16T09:39:30.628250
---

# Service user management API

# Service user management API

* Latest Dynatrace
* Reference
* Published Dec 04, 2025

[### List all service users

Get an overview of all service users in your Dynatrace account.](/docs/dynatrace-api/account-management-api/service-user-management-api/get-all-service-users "Get an overview of service users in your Dynatrace account via the Dynatrace API.")[### Create a service user

Add a new service user to your Dynatrace account.](/docs/dynatrace-api/account-management-api/service-user-management-api/post-service-user "Create a service user in your Dynatrace account via the Dynatrace API.")[### View a service user

View details of a selected service user.](/docs/dynatrace-api/account-management-api/service-user-management-api/get-service-user "Get an overview of a service user in an account via the Dynatrace API.")[### Edit a service user

Edit details of a service user.](/docs/dynatrace-api/account-management-api/service-user-management-api/put-service-user "Edit a service user in your Dynatrace account via the Dynatrace API.")[### Delete a service user

Delete a service user.](/docs/dynatrace-api/account-management-api/service-user-management-api/delete-service-user "Delete a service user from your Dynatrace account via the Dynatrace API.")


---
