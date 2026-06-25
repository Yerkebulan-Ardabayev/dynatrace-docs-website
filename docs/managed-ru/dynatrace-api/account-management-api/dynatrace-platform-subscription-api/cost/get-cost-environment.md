---
title: Dynatrace Platform Subscription API - GET cost per environment
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost/get-cost-environment
scraped: 2026-05-12T11:24:35.549083
---

# Dynatrace Platform Subscription API - GET cost per environment

# Dynatrace Platform Subscription API - GET cost per environment

* Reference
* Published Mar 30, 2023

Возвращает данные о стоимости Dynatrace Platform Subscription в разбивке по окружениям мониторинга.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v3/accounts/{accountUuid}/subscriptions/{subscriptionUuid}/environments/cost` |

## Аутентификация

Для выполнения этого запроса токену нужен scope **Allow read access for usage and consumption resources** (`account-uac-read`). О том, как его получить и использовать, смотрите [OAuth clients](/managed/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и правами пользователей через OAuth-клиенты.").

## Параметры

| Параметр | Тип | Описание | Где | Обязательный |
| --- | --- | --- | --- | --- |
| accountUuid | string | ID нужного аккаунта.  UUID можно найти на странице **Account Management** > **Identity & access management** > **OAuth clients** при создании OAuth-клиента. | path | Required |
| subscriptionUuid | string | UUID запрашиваемой подписки.  Список подписок можно получить через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). | path | Required |
| startTime | string | Время начала запроса в формате `2021-05-01T15:11:00Z`. Границы временного диапазона (startTime, endTime) обе обязательны, если не передан «page-key». | query | Optional |
| endTime | string | Время окончания запроса в формате `2021-05-01T15:11:00Z`. Границы временного диапазона (startTime, endTime) обе обязательны, если не передан «page-key». | query | Optional |
| environmentIds | string[] | Список окружений, для которых читаются данные использования. Несколько окружений разделяются запятой (`,`). | query | Optional |
| capabilityKeys | string[] | Список capabilities, для которых читаются данные использования. Несколько capabilities разделяются запятой (`,`).  Чтобы получить ключи capabilities, используйте вызов [GET subscriptions](https://dt-url.net/qd43uld) и посмотрите поле **capabilities** в ответе. | query | Optional |
| clusterIds | string[] | Список Managed-кластеров, для которых читаются данные использования.  Неприменимо к SaaS-окружениям. | query | Optional |
| page-key | string | Курсор для следующей страницы результатов. Находится в поле **nextPageKey** предыдущего ответа. | query | Optional |
| page-size | number | Запрашиваемое число записей для следующей страницы. | query | Optional |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [SubscriptionEnvironmentCostListV3Dto](#openapi-definition-SubscriptionEnvironmentCostListV3Dto) | Успех. Тело ответа содержит стоимость подписки в разбивке по окружениям. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `SubscriptionEnvironmentCostListV3Dto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| data | [SubscriptionEnvironmentCostV3Dto[]](#openapi-definition-SubscriptionEnvironmentCostV3Dto) | Данные о стоимости подписки. |
| lastModifiedTime | string | Время последней модификации данных подписки в формате `2021-05-01T15:11:00Z`. |
| nextPageKey | string | Ключ следующей страницы для пагинации, если такая страница существует. |

#### Объект `SubscriptionEnvironmentCostV3Dto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| clusterId | string | UUID Managed-кластера. |
| environmentId | string | UUID окружения. |
| cost | [SubscriptionCapabilityCostReceivedDto[]](#openapi-definition-SubscriptionCapabilityCostReceivedDto) | Стоимость подписки для окружения. |

#### Объект `SubscriptionCapabilityCostReceivedDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| startTime | string | Время начала для стоимости capability в формате `2021-05-01T15:11:00Z`. |
| endTime | string | Время окончания для стоимости capability в формате `2021-05-01T15:11:00Z`. |
| value | number | Общая стоимость по всем capabilities. |
| currencyCode | string | Валюта стоимости. |
| capabilityKey | string | Ключ capability подписки. |
| capabilityName | string | Отображаемое имя capability подписки. |
| bookingDate | string | Дата проводки capability подписки в формате `2021-05-01T15:11:00Z`. |

### JSON-модели тела ответа

```
{



"data": [



{



"clusterId": "string",



"environmentId": "string",



"cost": [



{



"startTime": "string",



"endTime": "string",



"value": 1,



"currencyCode": "string",



"capabilityKey": "string",



"capabilityName": "string",



"bookingDate": "string"



}



]



}



],



"lastModifiedTime": "string",



"nextPageKey": "string"



}
```