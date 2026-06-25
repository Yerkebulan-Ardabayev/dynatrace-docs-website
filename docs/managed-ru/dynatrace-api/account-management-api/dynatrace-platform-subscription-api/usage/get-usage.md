---
title: Dynatrace Platform Subscription API - GET usage
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/usage/get-usage
scraped: 2026-05-12T11:24:39.732678
---

# Dynatrace Platform Subscription API - GET usage

# Dynatrace Platform Subscription API - GET usage

* Reference
* Published Mar 30, 2023

Возвращает агрегированные данные использования Dynatrace Platform Subscription.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/usage` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`). О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** при создании OAuth-клиента. | path | Required |
| subscriptionUuid | string | UUID запрашиваемой подписки.  Список подписок можно получить через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). | path | Required |
| environmentIds | string[] | Список окружений, для которых читаются данные использования. Несколько окружений разделяются запятой (`,`). | query | Optional |
| capabilityKeys | string[] | Список capabilities, для которых читаются данные использования. Несколько capabilities разделяются запятой (`,`).  Чтобы получить ключи capabilities, используйте вызов [GET subscriptions](https://dt-url.net/qd43uld) и посмотрите поле **capabilities** в ответе. | query | Optional |
| clusterIds | string[] | Список Managed-кластеров, для которых читаются данные использования.  Неприменимо к SaaS-окружениям. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SubscriptionUsageListDto](#openapi-definition-SubscriptionUsageListDto) | Успех. Тело ответа содержит данные использования подписки в разбивке по дате. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `SubscriptionUsageListDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| data | [SubscriptionUsageDto[]](#openapi-definition-SubscriptionUsageDto) | Данные использования подписки. |
| lastModifiedTime | string | Время последней модификации данных подписки в формате `2021-05-01T15:11:00Z`. |

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



"capabilityKey": "string",



"capabilityName": "string",



"startTime": "string",



"endTime": "string",



"value": 1,



"unitMeasure": "string"



}



],



"lastModifiedTime": "string"



}
```