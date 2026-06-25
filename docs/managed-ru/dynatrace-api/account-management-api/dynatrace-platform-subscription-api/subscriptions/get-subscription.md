---
title: Dynatrace Platform Subscription API - GET a subscription
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/subscriptions/get-subscription
scraped: 2026-05-12T11:24:37.078632
---

# Dynatrace Platform Subscription API - GET a subscription

# Dynatrace Platform Subscription API - GET a subscription

* Reference
* Published Mar 30, 2023

Возвращает подробную информацию о Dynatrace Platform Subscription.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`). О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** при создании OAuth-клиента. | path | Required |
| subscriptionUuid | string | UUID запрашиваемой подписки.  Список подписок можно получить через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). | path | Required |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SubscriptionDto](#openapi-definition-SubscriptionDto) | Успех. Тело ответа содержит подробности подписки. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `SubscriptionDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | UUID Dynatrace Platform Subscription. |
| type | string | Тип Dynatrace Platform Subscription. |
| subType | string | Подтип Dynatrace Platform Subscription. |
| name | string | Отображаемое имя Dynatrace Platform Subscription. |
| status | string | Статус Dynatrace Platform Subscription. |
| startTime | string | Дата начала подписки в формате `2021-05-01`. |
| endTime | string | Дата окончания подписки в формате `2021-05-01`. |
| account | [SubscriptionAccountDto](#openapi-definition-SubscriptionAccountDto) | Аккаунт, связанный с подпиской. |
| budget | [SubscriptionBudgetDto](#openapi-definition-SubscriptionBudgetDto) | Бюджет, связанный с подпиской. |
| currentPeriod | [SubscriptionCurrentPeriodDto](#openapi-definition-SubscriptionCurrentPeriodDto) | Текущий период подписки. |
| periods | [SubscriptionPeriodDto[]](#openapi-definition-SubscriptionPeriodDto) | Список периодов подписки. |
| capabilities | [SubscriptionCapabilityDto[]](#openapi-definition-SubscriptionCapabilityDto) | Список capabilities подписки. |

#### Объект `SubscriptionAccountDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| uuid | string | UUID аккаунта. |

#### Объект `SubscriptionBudgetDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| total | number | Общий бюджет подписки. |
| used | number | Использованный бюджет подписки. |
| currencyCode | string | Валюта подписки. |

#### Объект `SubscriptionCurrentPeriodDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| startTime | string | Дата начала текущего периода в формате `2021-05-01`. |
| endTime | string | Дата окончания текущего периода в формате `2021-05-01`. |
| daysRemaining | number | Оставшиеся дни в текущем периоде. |

#### Объект `SubscriptionPeriodDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| startTime | string | Время начала периода подписки в формате `2021-05-01T15:11:00Z`. |
| endTime | string | Время окончания периода подписки в формате `2021-05-01T15:11:00Z`. |

#### Объект `SubscriptionCapabilityDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| key | string | Ключ capability подписки. |
| name | string | Отображаемое имя capability подписки. |

### JSON-модели тела ответа

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