---
title: Notifications API - POST filter notifications
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/post-notifications
---

# Notifications API - POST filter notifications

# Notifications API - POST filter notifications

* Reference
* Updated on Apr 14, 2026

This API returns all account‑level notification types, including budget, cost, and forecast.

|  |  |
| --- | --- |
| POST | `https://api.dynatrace.com/v1/accounts/{accountUuid}/notifications` |

## Authentication

To execute this request, you need the **Allow read access for usage and consumption resources** (`account-uac-read`) scope assigned to your token.

To learn how to obtain and use it, see [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Manage authentication and user permissions using OAuth clients.").

## Parameters

| Parameter | Type | Description | In | Required |
| --- | --- | --- | --- | --- |
| accountUuid | string | The ID of the required account.  You can find the UUID on the **Account Management** > **Identity & access management** > **OAuth clients** page, during creation of an OAuth client. | path | Required |
| body | [NotificationQueryParamsDto](#openapi-definition-NotificationQueryParamsDto) | - | body | Required |

### Request body objects

#### The `NotificationQueryParamsDto` object

| Element | Type | Description | Required |
| --- | --- | --- | --- |
| startDateTime | string | Start date and time to filter notifications. | Optional |
| endDateTime | string | End date and time to filter notifications. | Optional |
| types | string[] | Notification types to filter notifications. The element can hold these values * `FORECAST` * `BUDGET` * `COST` * `BYOK_REVOKED` * `BYOK_ACTIVATED` | Optional |
| severities | string[] | Notification severities to filter notifications. The element can hold these values * `SEVERE` * `WARN` * `INFO` | Optional |
| capabilities | array[] | Capabilities to filter notifications. | Optional |
| environments | array[] | Environments to filter notifications. | Optional |
| page | number | The page number. | Optional |
| pageSize | number | The maximum number of notifications to return, max 100. | Optional |
| sorts | string[] | The property to sort by. Prefix with "-" to invert sort order. The element can hold these values * `type` * `-type` * `date` * `-date` | Optional |

### Request body JSON model

This is a model of the request body, showing the possible elements. It has to be adjusted for usage in an actual request.

```
{



"startDateTime": "2023-01-01T00:00:00Z",



"endDateTime": "2023-12-31T23:59:59Z",



"types": [



"FORECAST"



],



"severities": [



"SEVERE"



],



"capabilities": [



"LOG_MANAGEMENT_ANALYZE"



],



"environments": [



"abc12345"



],



"page": 1,



"pageSize": 20,



"sorts": [



"-date"



]



}
```

## Response

### Response codes

| Code | Type | Description |
| --- | --- | --- |
| **200** | [NotificationListDto](#openapi-definition-NotificationListDto) | Success. The response contains a list of notifications based on the given query. |
| **400** | - | Failed. The request was unacceptable, often due to missing a required parameter |
| **401** | - | Failed. The bearer token is incorrect/expired or the requested account information does not match the bearer token |
| **403** | - | Access denied |
| **404** | - | Failed. The requested resource was not found |
| **500** | - | Failed. Something went wrong in Account Management API |

### Response body objects

#### The `NotificationListDto` object

| Element | Type | Description |
| --- | --- | --- |
| records | [NotificationDto](#openapi-definition-NotificationDto)[] | A list of notifications of the account. |
| totalRecordCount | number | The total number of notifications matching the filter. |
| hasNextPage | boolean | If there are more notifications. |

#### The `NotificationDto` object

| Element | Type | Description |
| --- | --- | --- |
| key | string | - |
| accountUuid | string | - |
| message | string | - |
| severity | string | - |
| type | string | - |
| details | [SubscriptionRelatedEventDataDto](#openapi-definition-SubscriptionRelatedEventDataDto) | [ByokEventDto](#openapi-definition-ByokEventDto) | - |
| date | string | - |

#### The `SubscriptionRelatedEventDataDto` object

| Element | Type | Description |
| --- | --- | --- |
| environments | string[] | - |
| capabilities | string[] | - |
| allEnvironments | boolean | - |
| allCapabilities | boolean | - |

#### The `ByokEventDto` object

| Element | Type | Description |
| --- | --- | --- |
| environmentUuid | string | - |
| keyName | string | - |

### Response body JSON models

```
{



"records": [



{



"key": "budget-key-example",



"accountUuid": "00000000-0000-0000-0000-000000000000",



"message": "Message for budget 0 0",



"severity": "WARN",



"type": "budget",



"details": {



"environments": [



{



"uuid": "env-uuid",



"clusterUuid": "cluster-uuid"



}



],



"capabilities": [



"cap1"



],



"allEnvironments": false,



"allCapabilities": true



},



"date": "2025-12-14T10:02:09.297Z"



},



{



"key": "byok-key-example",



"accountUuid": "00000000-0000-0000-0000-000000000000",



"message": "BYOK event message",



"severity": "WARN",



"type": "byok-revoked",



"details": {



"environmentUuid": "env-uuid",



"keyName": "key-name"



},



"date": "2025-12-14T10:02:09.297Z"



}



],



"totalRecordCount": 300,



"hasNextPage": true



}
```