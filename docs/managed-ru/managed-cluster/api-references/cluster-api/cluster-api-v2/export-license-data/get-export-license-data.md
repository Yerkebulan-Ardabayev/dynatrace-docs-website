---
title: "Export license data"
source: https://docs.dynatrace.com/managed/managed-cluster/api-references/cluster-api/cluster-api-v2/export-license-data/get-export-license-data
updated: 2026-02-09
---

Этот API-вызов экспортирует агрегированное почасовое использование лицензии всех ваших окружений как ZIP-файл.

Этот API совместим только с классическим лицензированием Dynatrace и не содержит данных оплаченного потребления.

## Аутентификация

Для выполнения этого запроса API-токену нужно разрешение **Service Provider API** (`ServiceProviderAPI`). Создайте API-токен через Cluster Management Console (CMC). Как его получить и использовать, смотрите Cluster API - Authentication.

Запрос возвращает payload `application/octet-stream`.

## Endpoint

`/api/cluster/v2/license/consumption`

## Формат ответа

Запрос возвращает payload `application/octet-stream`.

## Ответ

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | string | OK: экспорт данных потребления лицензии начнётся |
| **400** | - | Bad request. Указан некорректный диапазон времени. |
| **422** | - | Несовместимая лицензионная модель. |
| **429** | - | Данные потребления лицензии уже экспортируются. Дождитесь окончания первого запроса перед запросом нового экспорта. |
| **500** | - | Операция не выполнена |

### Объекты тела ответа

#### Объект `ResponseBody`

## Пример

В этом примере запрашиваются данные лицензии Dynatrace Managed в диапазоне с 19 марта 2020, 6:00 (1584594000000) до 9 июня 2020, 17:00 (1591714800000).

#### Curl

```
curl -X GET "https://myManaged.cluster.com/api/cluster/v2/license/consumption?startTs=1584594000000&endTs=1591714800000"


-H  "accept: application/octet-stream"
```

#### URL запроса

```
https://myManaged.cluster.com/api/cluster/v2/license/consumption?startTs=1584594000000&endTs=1591714800000
```

#### Тело ответа

ZIP-файл с файлами данных лицензии в формате JSON. Детали JSON-формата смотрите в Export license data.

#### Код ответа

`200`
