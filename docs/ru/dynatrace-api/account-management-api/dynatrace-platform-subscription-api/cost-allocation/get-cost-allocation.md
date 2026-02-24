---
title: Dynatrace Platform Subscription API - GET cost allocation
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation
scraped: 2026-02-24T21:27:44.524600
---

# Dynatrace Platform Subscription API - GET cost allocation

# Dynatrace Platform Subscription API - GET cost allocation

* Latest Dynatrace
* Reference
* Published Oct 18, 2024

Списки данных об использовании Dynatrace Platform Subscription по полю распределения затрат.

Запрос производит полезную нагрузку `application/json`.

## Аутентификация

Чтобы выполнить этот запрос, вам необходимо назначить область `Allow read access for usage and consumption resources` (`account-uac-read`) вашему токену. Чтобы узнать, как получить и использовать его, см. [Клиенты OAuth](/docs/manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients "Управление аутентификацией и разрешениями пользователей с помощью клиентов OAuth.").

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| subscription-uuid | string | UUID запрошенной подписки. Получите список подписок через запрос [GET all subscriptions](https://dt-url.net/jq03jvq). (обязательный) | path | Обязательный |
| field | string | Поле, по которому должны быть разделены затраты и использование. Допустимые значения: `COSTCENTER`, `PRODUCT` (обязательный, если не указан page-key) | query | Обязательный |
| environment-id | string | Идентификатор среды. (обязательный, если не указан page-key) | query | Необязательный |
| from | string | Начало запрошенного временного интервала в формате `2021-05-01`. | query | Необязательный |
| to | string | Конец запрошенного временного интервала в формате `2021-05-01`. | query | Необязательный |
| page-size | number | Определяет количество записей, запрошенных для следующей страницы. | query | Необязательный |
| page-key | string | Закодированный в base64 ключ для получения конкретной страницы. Если этот параметр запроса задан, другие параметры запроса не могут быть заданы. | query | Необязательный |

## Ответ

### Код ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PaginatedEnvironmentBreakdownDto](#openapi-definition-PaginatedEnvironmentBreakdownDto) | Успех. Ответ содержит страницу запрошенного анализа распределения затрат. |
| **400** | - | Запрос был недопустимым, часто из-за отсутствия обязательного параметра |
| **401** | - | Не предоставлена действительная сессия |
| **403** | - | Доступ запрещен |
| **500** | - | Что-то пошло не так на стороне Account Management |

### Объекты тела ответа

#### Объект `PaginatedEnvironmentBreakdownDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | Идентификатор среды |
| field | string | Поле, использованное для генерации анализа. Может быть `COSTCENTER` или `PRODUCT` |
| records | string[] | Список отдельных записей анализа. |
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