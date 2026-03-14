---
title: Dynatrace Платформа Подписка API - Получить распределение затрат
source: https://www.dynatrace.com/docs/dynatrace-api/account-management-api/dynatrace-platform-subscription-api/cost-allocation/get-cost-allocation
scraped: 2026-03-06T21:26:54.898889
---

# Dynatrace Platform Subscription API — GET cost allocation


* Последняя версия Dynatrace
* Reference
* Опубликовано 18 октября 2024 г.

Возвращает данные об использовании Dynatrace Platform Subscription с разбивкой по полю распределения затрат.

Запрос возвращает полезную нагрузку типа `application/json`.

## Аутентификация

Для выполнения этого запроса вашему токену должна быть назначена область `account-uac-read` (**Allow read access for usage and consumption resources**). Подробнее о получении и использовании токена см. в разделе [OAuth-клиенты](../../../../manage/identity-access-management/access-tokens-and-oauth-clients/oauth-clients.md "Manage authentication and user permissions using OAuth clients.").

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| subscription-uuid | string | UUID запрашиваемой подписки. Получить список подписок можно с помощью запроса [GET all subscriptions](https://dt-url.net/jq03jvq). (обязательный) | path | Необязательный |
| field | string | Поле, по которому следует разбивать затраты и использование. Допустимые значения: `COSTCENTER`, `PRODUCT` (обязательный, если не указан page-key) | query | Необязательный |
| environment-id | string | Идентификатор среды. (обязательный, если не указан page-key) | query | Необязательный |
| from | string | Начало запрашиваемого временного диапазона в формате `2021-05-01`. | query | Необязательный |
| to | string | Конец запрашиваемого временного диапазона в формате `2021-05-01`. | query | Необязательный |
| page-size | number | Определяет запрашиваемое количество записей на следующую страницу. | query | Необязательный |
| page-key | string | Ключ в кодировке base64 для получения конкретной страницы. Если этот параметр запроса установлен, другие параметры запроса не могут быть заданы. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [PaginatedEnvironmentBreakdownDto](#openapi-definition-PaginatedEnvironmentBreakdownDto) | Успешно. Ответ содержит страницу запрошенной разбивки возвратных платежей. |
| **400** | - | Запрос неприемлем, как правило, из-за отсутствия обязательного параметра |
| **401** | - | Не предоставлена действительная сессия |
| **403** | - | Доступ запрещён |
| **500** | - | Произошла ошибка на стороне Account Management |

### Объекты тела ответа

#### Объект `PaginatedEnvironmentBreakdownDto`

| Элемент | Тип | Описание |
| --- | --- | --- |
| environmentId | string | Идентификатор среды |
| field | string | Поле, использованное для формирования разбивки. Может принимать значение `COSTCENTER` или `PRODUCT` |
| records | string[] | Список отдельных записей разбивки. |
| nextPageKey | string | Ключ для запроса следующей страницы. |

### JSON-модели тела ответа

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

* [Распределение ваших DPS-затрат](../../../../license/cost-allocation.md "Learn how to allocate costs to cost centers and products.")
