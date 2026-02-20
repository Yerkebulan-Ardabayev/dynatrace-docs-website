---
title: Dynatrace Platform Subscription API - GET cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation
scraped: 2026-02-20T21:12:30.274144
---

# Dynatrace Platform Subscription API - GET cost allocation

# Dynatrace Platform Subscription API - GET cost allocation

* Latest Dynatrace
* Reference
* Published Oct 18, 2024

Отображает данные об использовании Dynatrace Platform Subscription, сгруппированные по полю распределения затрат.

Запрос возвращает полезную нагрузку в формате `application/json`.

GET

`https://api.dynatrace.com/v1/subscriptions/{subscription-uuid}/cost-allocation`

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо иметь область действия **Allow read access for usage and consumption resources** (`account-uac-read`), назначенную вашему токену. Чтобы узнать, как получить и использовать его, см. [OAuth-клиенты](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью OAuth-клиентов.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| subscription-uuid | string | UUID запрошенной подписки.  Получите список подписок через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). (обязательно) | path | Обязательно |
| field | string | Поле, по которому должны быть разделены затраты и использование. Допустимые значения: `COSTCENTER`, `PRODUCT` (обязательно, если не указан page-key) | query | Обязательно |
| environment-id | string | Идентификатор среды. (обязательно, если не указан page-key) | query | Необязательно |
| from | string | Начало запрошенного временного интервала в формате `2021-05-01`. | query | Необязательно |
| to | string | Конец запрошенного временного интервала в формате `2021-05-01`. | query | Необязательно |
| page-size | number | Определяет количество записей, запрошенных для следующей страницы. | query | Необязательно |
| page-key | string | Кодированный в base64 ключ для получения конкретной страницы. Если этот параметр запроса задан, другие параметры запроса не могут быть заданы. | query | Необязательно |

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PaginatedEnvironmentBreakdownDto](#openapi-definition-PaginatedEnvironmentBreakdownDto) | Успех. Ответ содержит страницу запрошенного расчета распределения затрат. |
| **400** | - | Запрос был неприемлемым, часто из-за отсутствия обязательного параметра |
| **401** | - | Не предоставлена действительная сессия |
| **403** | - | Доступ запрещен |
| **500** | - | Что-то пошло не так на стороне Account Management |

### Объекты тела ответа

#### Объект `PaginatedEnvironmentBreakdownDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | Идентификатор среды |
| field | string | Поле, использованное для генерации расчета. Может быть `COSTCENTER` или `PRODUCT` |
| records | string[] | Список отдельных записей расчета. |
| nextPageKey | string | Ключ для запроса следующей страницы. |

### Модели тела ответа JSON

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

## Связанные темы

* [Распределение затрат DPS](/docs/license/cost-allocation "Узнайте, как распределить затраты по центрам затрат и продуктам.")