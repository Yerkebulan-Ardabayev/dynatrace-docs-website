---
title: Dynatrace Platform Subscription API - GET forecast
source: https://docs.dynatrace.com/managed/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-monitors/get-forecast
scraped: 2026-05-12T11:24:38.413735
---

# Dynatrace Platform Subscription API - GET forecast

# Dynatrace Platform Subscription API - GET forecast

* Reference
* Published Aug 30, 2023

Возвращает прогноз использования Dynatrace Platform Subscription к концу годового периода обязательств.

Запрос возвращает payload `application/json`.

|  |  |
| --- | --- |
| GET | `https://api.dynatrace.com/sub/v2/accounts/{accountUuid}/subscriptions/forecast` |

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
| **200** | [Forecast](#openapi-definition-Forecast) | Успех. Тело ответа содержит прогноз использования подписки. |
| **400** | - | Ошибка. Запрос неприемлем, чаще всего из-за отсутствия обязательного параметра. |
| **401** | - | Ошибка. Bearer-токен некорректен или просрочен, либо запрашиваемая информация об аккаунте не соответствует bearer-токену. |
| **403** | - | Доступ запрещён. |
| **404** | - | Ошибка. Запрашиваемый ресурс не найден. |
| **500** | - | Ошибка. Что-то пошло не так в Account Management API. |

### Объекты тела ответа

#### Объект `Forecast`

| Элемент | Тип | Описание |
| --- | --- | --- |
| forecastMedian | number | Медианное прогнозируемое потребление. |
| forecastLower | number | Нижняя граница прогноза потребления. |
| forecastUpper | number | Верхняя граница прогноза потребления. |
| budget | number | Бюджетная квота, используемая в прогнозе. |
| forecastBudgetPct | number | Прогнозируемое потребление бюджета в процентах. |
| forecastBudgetDate | string | Дата, когда прогноз использует всю бюджетную квоту. |
| forecastCreatedAt | string | Дата создания прогноза. |

### JSON-модели тела ответа

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