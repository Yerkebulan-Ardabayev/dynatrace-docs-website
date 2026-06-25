---
title: Dynatrace Platform Subscription API - GET usage per environment
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage-environment
scraped: 2026-05-12T11:24:34.119885
---

# Dynatrace Platform Subscription API - GET usage per environment

# Dynatrace Platform Subscription API - GET usage per environment

* Reference
* Published Mar 30, 2023

Возвращает данные использования Dynatrace Platform Subscription в разбивке по окружениям мониторинга.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/environments/usage` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`). О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного SaaS-аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** при создании OAuth-клиента. | path | Required |
| subscriptionUuid | string | UUID запрашиваемой подписки.  Список подписок можно получить через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). | path | Required |
| startTime | string | Начало запрашиваемого временного диапазона в формате `2021-05-01T15:11:00Z`. | query | Required |
| endTime | string | Конец запрашиваемого временного диапазона в формате `2021-05-01T15:11:00Z`. | query | Required |
| environmentIds | string[] | Список окружений, для которых читаются данные использования. Несколько окружений разделяются запятой (`,`). | query | Optional |
| capabilityKeys | string[] | Список capabilities, для которых читаются данные использования. Несколько capabilities разделяются запятой (`,`).  Чтобы получить ключи capabilities, используйте вызов [GET subscriptions](https://dt-url.net/qd43uld) и посмотрите поле **capabilities** в ответе. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SubscriptionEnvironmentUsageListV2Dto](#openapi-definition-SubscriptionEnvironmentUsageListV2Dto) | Успех. Тело ответа содержит данные использования подписки в разбивке по окружениям. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `SubscriptionEnvironmentUsageListV2Dto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| data | [SubscriptionEnvironmentUsageV2Dto[]](#openapi-definition-SubscriptionEnvironmentUsageV2Dto) | Данные использования подписки. |
| lastModifiedTime | string | Время последней модификации данных подписки в формате `2021-05-01T15:11:00Z`. |

#### Объект `SubscriptionEnvironmentUsageV2Dto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | UUID окружения. |
| usage | [SubscriptionUsageDto[]](#openapi-definition-SubscriptionUsageDto) | Список использования подписки для окружения. |

#### Объект `SubscriptionUsageDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| capabilityKey | string | Ключ capability подписки. |
| capabilityName | string | Отображаемое имя capability подписки. |
| startTime | string | Время начала использования capability в формате `2021-05-01T15:11:00Z`. |
| endTime | string | Время окончания использования capability в формате `2021-05-01T15:11:00Z`. |
| value | number | Использование подписки этой capability. |
| unitMeasure | string | Единица измерения использования capability. |

### JSON-модели тела ответа

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