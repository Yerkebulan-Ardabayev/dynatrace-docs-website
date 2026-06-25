---
title: Dynatrace Platform Subscription API - GET all subscriptions
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-all
scraped: 2026-05-12T11:24:31.454641
---

# Dynatrace Platform Subscription API - GET all subscriptions

# Dynatrace Platform Subscription API - GET all subscriptions

* Reference
* Published Mar 30, 2023

Возвращает все Dynatrace Platform Subscriptions аккаунта.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`). О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** при создании OAuth-клиента. | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SubscriptionListDto](#openapi-definition-SubscriptionListDto) | Успех. Тело ответа содержит список подписок аккаунта. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `SubscriptionListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| data | [SubscriptionSummaryDto[]](#openapi-definition-SubscriptionSummaryDto) | Список подписок аккаунта. |

#### Объект `SubscriptionSummaryDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | UUID Dynatrace Platform Subscription. |
| type | string | Тип Dynatrace Platform Subscription. |
| subType | string | Подтип Dynatrace Platform Subscription. |
| name | string | Отображаемое имя Dynatrace Platform Subscription. |
| status | string | Статус Dynatrace Platform Subscription. |
| startTime | string | Дата начала подписки в формате `2021-05-01`. |
| endTime | string | Дата окончания подписки в формате `2021-05-01`. |

### JSON-модели тела ответа

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