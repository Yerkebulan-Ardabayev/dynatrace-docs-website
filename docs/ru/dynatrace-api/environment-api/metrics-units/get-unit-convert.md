---
title: Metric units API - GET convert units
source: https://www.dynatrace.com/docs/dynatrace-api/environment-api/metrics-units/get-unit-convert
scraped: 2026-03-06T21:35:45.467583
---

# API единиц измерения метрик — GET конвертация единиц


Конвертирует исходную единицу измерения в целевую.

Если целевая единица не задана, запрос автоматически находит подходящую целевую единицу с учётом предпочтительного числового формата (если указан).

Запрос возвращает данные в формате `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | Managed | `https://{your-environment-id}.live.dynatrace.com/api/v2/units/{unitId}/convert` |
| GET | Environment ActiveGateCluster ActiveGate | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/units/{unitId}/convert` |

## Аутентификация

Для выполнения этого запроса требуется токен доступа с областью `metrics.read`.

Подробнее о получении и использовании токена см. в разделе Токены и аутентификация.

## Параметры

| Параметр | Тип | Описание | Расположение | Обязательный |
| --- | --- | --- | --- | --- |
| unitId | string | Идентификатор исходной единицы измерения. | path | Обязательный |
| value | number | Значение для конвертации. | query | Обязательный |
| targetUnit | string | Идентификатор целевой единицы измерения. Если не задан, запрос автоматически находит подходящую целевую единицу на основе указанного числового формата. | query | Необязательный |
| numberFormat | string | Предпочтительный числовой формат целевого значения. Можно указать следующие форматы:  * `binary` * `decimal`  `Используется только если целевая единица не задана. | query | Необязательный |

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [UnitConversionResult](#openapi-definition-UnitConversionResult) | Успешно |
| **404** | - | Не найдено. Запрошенный ресурс не найден или запрос некорректен. |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `UnitConversionResult`

Результат конвертации единиц измерения.

| Элемент | Тип | Описание |
| --- | --- | --- |
| resultValue | number | Результат конвертации единиц измерения. |
| unitId | string | Идентификатор единицы измерения этого результата конвертации. |

### JSON-модели тела ответа

```
{


"resultValue": 1,


"unitId": "string"


}
```
