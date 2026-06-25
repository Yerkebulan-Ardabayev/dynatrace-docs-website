---
title: Notifications API - POST filter notifications
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/post-notifications
scraped: 2026-05-12T11:35:20.918278
---

# Notifications API - POST filter notifications

# Notifications API - POST filter notifications

* Reference
* Updated on Apr 14, 2026

Этот API возвращает все типы уведомлений на уровне аккаунта, включая budget, cost и forecast.

|  |  |
| --- | --- |
| POST | `https://api.dynatrace.com/v1/accounts/{accountUuid}/notifications` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`).

О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth clients.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** во время создания OAuth client. | path | Required |
| body | [NotificationQueryParamsDto](#openapi-definition-NotificationQueryParamsDto) | - | body | Required |

### Объекты тела запроса

#### Объект `NotificationQueryParamsDto`

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| startDateTime | string | Начальная дата и время для фильтрации уведомлений. | Optional |
| endDateTime | string | Конечная дата и время для фильтрации уведомлений. | Optional |
| types | string[] | Типы уведомлений для фильтрации. Возможные значения: * `FORECAST` * `BUDGET` * `COST` * `BYOK_REVOKED` * `BYOK_ACTIVATED` | Optional |
| severities | string[] | Severity уведомлений для фильтрации. Возможные значения: * `SEVERE` * `WARN` * `INFO` | Optional |
| capabilities | array[] | Capabilities для фильтрации уведомлений. | Optional |
| environments | array[] | Окружения для фильтрации уведомлений. | Optional |
| page | number | Номер страницы. | Optional |
| pageSize | number | Максимальное число возвращаемых уведомлений, max 100. | Optional |
| sorts | string[] | Свойство для сортировки. Префикс "-" инвертирует порядок. Возможные значения: * `type` * `-type` * `date` * `-date` | Optional |

### JSON-модель тела запроса

Это модель тела запроса со всеми возможными элементами. При использовании в реальном запросе её нужно адаптировать.

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

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [NotificationListDto](#openapi-definition-NotificationListDto) | Успех. Ответ содержит список уведомлений по заданному запросу. |
| **400** | - | Сбой. Запрос невалиден, часто из-за отсутствующего обязательного параметра |
| **401** | - | Сбой. Bearer-токен некорректен/истёк или запрошенная информация об аккаунте не соответствует bearer-токену |
| **403** | - | Доступ запрещён |
| **404** | - | Сбой. Запрошенный ресурс не найден |
| **500** | - | Сбой. Что-то пошло не так в Account Management API |

### Объекты тела ответа

#### Объект `NotificationListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| records | [NotificationDto[]](#openapi-definition-NotificationDto) | Список уведомлений аккаунта. |
| totalRecordCount | number | Общее число уведомлений, удовлетворяющих фильтру. |
| hasNextPage | boolean | Есть ли ещё уведомления. |

#### Объект `NotificationDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | - |
| accountUuid | string | - |
| message | string | - |
| severity | string | - |
| type | string | - |
| details | [SubscriptionRelatedEventDataDto](#openapi-definition-SubscriptionRelatedEventDataDto) | - |
| date | string | - |

#### Объект `SubscriptionRelatedEventDataDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environments | string[] | - |
| capabilities | string[] | - |
| allEnvironments | boolean | - |
| allCapabilities | boolean | - |

### JSON-модели тела ответа

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