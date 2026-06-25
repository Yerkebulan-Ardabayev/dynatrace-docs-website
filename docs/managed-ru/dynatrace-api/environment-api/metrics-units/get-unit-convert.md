---
title: Metric units API - GET конвертация единиц
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metrics-units/get-unit-convert
scraped: 2026-05-12T11:12:19.497120
---

# Metric units API - GET конвертация единиц

# Metric units API - GET конвертация единиц

* Справочник
* Опубликовано 25 марта 2022 г.

Преобразует исходную единицу в целевую.

Если целевая единица не задана, запрос автоматически подбирает подходящую целевую единицу с учётом предпочтительного формата чисел (если он указан).

Запрос возвращает payload в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v2/units/{unitId}/convert` |
| GET | Environment and Cluster ActiveGate (default port 9999) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}/convert` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `metrics.read`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| unitId | string | ID исходной единицы. | path | Обязательный |
| value | number | Значение для преобразования. | query | Обязательный |
| targetUnit | string | ID целевой единицы.  Если не задан, запрос автоматически подбирает подходящую целевую единицу на основе указанного формата чисел. | query | Необязательный |
| numberFormat | string | Предпочтительный формат чисел для целевого значения. Можно указать следующие форматы:  * `binary` * `decimal`  `Используется только если целевая единица не задана. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UnitConversionResult](#openapi-definition-UnitConversionResult) | Успех |
| **404** | - | Не найдено. Запрашиваемый ресурс не найден или запрос некорректен. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `UnitConversionResult`

Результат преобразования единиц.

| Элемент | Тип | Описание |
| --- | --- | --- |
| resultValue | number | Результат преобразования единиц. |
| unitId | string | ID единицы для этого результата преобразования. |

### JSON-модели тела ответа

```
{



"resultValue": 1,



"unitId": "string"



}
```