---
title: Dynatrace Platform Subscription API - manage cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/manage-cost-allocation
scraped: 2026-02-18T21:31:40.222803
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