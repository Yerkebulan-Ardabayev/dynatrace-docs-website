---
title: Timeseries API v1 - POST точки данных
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/read-data-points/post-data-points
scraped: 2026-05-12T11:58:33.933040
---

# Timeseries API v1 - POST точки данных

# Timeseries API v1 - POST точки данных

* Справочник
* Опубликовано 07 ноября 2019 г.

Этот API устарел. В будущем он будет удалён. Используйте вместо него [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.").

Получает параметры и точки данных указанной метрики. По сравнению с GET-запросом, POST-запрос предоставляет меньше данных о самой метрике.

Чтобы получить точки данных, необходимо указать временной диапазон и тип агрегации, поддерживаемый запрашиваемой метрикой. Подробнее смотрите в разделе **Parameters**.

Запрос потребляет и возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| POST | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| POST | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Чтобы получить точки данных, необходимо указать временной диапазон и тип агрегации.

Существует два взаимоисключающих способа задать временной диапазон:

* Комбинация **startTimestamp** и **endTimestamp**.
* **relativeTime**

Максимально допустимый временной диапазон, 6 месяцев.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| timeseriesIdentifier | string | Чувствительный к регистру ID timeseries, из которой вы хотите прочитать параметры и точки данных. | path | Обязательный |
| body | [TimeseriesQueryMessage](#openapi-definition-TimeseriesQueryMessage) | JSON-тело запроса, содержащее параметры для идентификации требуемых точек данных. | body | Опциональный |

### Объекты тела запроса

#### Объект `TimeseriesQueryMessage`

Параметры фильтрации для запроса timeseries.

| Элемент | Тип | Описание | Обязательный |
| --- | --- | --- | --- |
| aggregationType | string | Тип агрегации для результирующих точек данных.  Если запрашиваемая метрика не поддерживает указанную агрегацию, запрос завершится ошибкой. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` | Опциональный |
| considerMaintenanceWindowsForAvailability | boolean | Исключить (`true`) или включить (`false`) точки данных из любого [maintenance window](https://dt-url.net/b2123rg0), определённого в вашей среде. | Опциональный |
| endTimestamp | integer | Начальная метка времени временного диапазона, в миллисекундах UTC.  Если она позже текущего времени, Dynatrace автоматически использует вместо неё текущее время.  Временной диапазон не должен превышать 6 месяцев. | Опциональный |
| entities | string[] | Фильтрует запрашиваемые точки данных по сущностям, которые должны их доставить. Можно указать несколько сущностей сразу.  Допустимые значения, это ID сущностей Dynatrace.  Если выбранная сущность не поддерживает запрашиваемую метрику, запрос завершится ошибкой. | Опциональный |
| filters | object | Фильтр, это объект, содержащий карту ключей фильтра и их значений. Допустимые ключи фильтра:  `processType`: фильтрует по типу процесса. Допустимые значения смотрите в разделе «Типы процессов». `osType`: фильтрует по операционной системе. Допустимые значения смотрите в разделе «Типы ОС». `serviceType`: фильтрует по типу сервиса. Допустимые значения смотрите в разделе «Типы сервисов». `technology`: фильтрует по типу технологии. Допустимые значения смотрите в разделе «Типы технологий». `webServiceName`: фильтрует по имени веб-сервиса. `webServiceNamespace`: фильтрует по пространству имён веб-сервиса. `host`: фильтрует по ID сущности хоста, например HOST-007. | Опциональный |
| includeParentIds | boolean | Указывает, должны ли результаты раскрывать сопоставления измерений между родительскими сущностями и их потомками.  Например: SERVICE-0000000000000001, SERVICE\_METHOD-0000000000000001 | Опциональный |
| percentile | integer | Указывает, какой процентиль выбранной метрики времени отклика должен быть доставлен.  Применимо только к типу агрегации `PERCENTILE`.  Допустимые значения процентиля, от 1 до 99.  Учтите, что экспорт процентиля возможен только для метрик на основе времени отклика, например времени отклика приложений и сервисов. | Опциональный |
| predict | boolean | Флаг для прогнозирования будущих точек данных. | Опциональный |
| queryMode | string | Определяет тип результата, который должен вернуть вызов. Допустимые режимы результата:  `series`: возвращает все точки данных метрики в указанном временном диапазоне. `total`: возвращает одно скалярное значение для указанного временного диапазона.  По умолчанию используется режим `series`. Элемент может принимать значения * `SERIES` * `TOTAL` | Опциональный |
| relativeTime | string | Относительный временной диапазон, отсчитываемый назад от текущего времени. Элемент может принимать значения * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | Опциональный |
| startTimestamp | integer | Начальная метка времени временного диапазона, в миллисекундах UTC. | Опциональный |
| tags | string[] | Фильтрует запрашиваемые точки данных по сущности, которая должна их доставить. Доставляются только данные сущностей с указанным тегом.  Можно указать несколько тегов в следующем формате: `tags=tag1&tags=tag2`. Сущность должна соответствовать *всем* указанным тегам.  В случае тегов «ключ-значение», например импортированных тегов AWS или CloudFoundry, используйте следующий формат: `[context]key:value`. | Опциональный |
| timeseriesId | string | Чувствительный к регистру ID метрики, из которой вы хотите прочитать точки данных.  Чтобы получить список доступных метрик, можно выполнить запрос GET timeseries. | Опциональный |

### JSON-модель тела запроса

Это модель тела запроса, показывающая возможные элементы. Её нужно скорректировать для использования в реальном запросе.

```
{



"aggregationType": "AVG",



"considerMaintenanceWindowsForAvailability": "false",



"endTimestamp": 1521542929000,



"entities": [



"HOST-0000000000000007"



],



"includeParentIds": "false",



"predict": true,



"queryMode": "SERIES",



"relativeTime": "HOUR",



"startTimestamp": 1521042929000,



"tags": [



"office-linz"



],



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle"



}
```

## Ответ

Результат, это JSON-объект, содержащий точки данных и параметры метрики.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TimeseriesQueryResultWrapper](#openapi-definition-TimeseriesQueryResultWrapper) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `TimeseriesQueryResultWrapper`

| Элемент | Тип | Описание |
| --- | --- | --- |
| result | [TimeseriesDataPointQueryResult](#openapi-definition-TimeseriesDataPointQueryResult) | Список точек данных метрики, а также их параметры. |

#### Объект `TimeseriesDataPointQueryResult`

Список точек данных метрики, а также их параметры.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregationType | string | Тип агрегации точек данных. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| dataPoints | object | Точки данных метрики.  JSON-объект, который сопоставляет ID сущности, доставившей точки данных, и массив, состоящий из массивов значений точек данных с плавающей точкой.  Может содержать более одного ID сущности на запись (например, хост и его сетевой интерфейс). В таких случаях ID сущностей разделяются запятыми.  Точка данных содержит значение и метку времени, в которую это значение было записано.  Dynatrace хранит данные во временных слотах. Объект **dataPoints** показывает *начальную* метку времени слота. Если **startTimestamp** или **endTimestamp** вашего запроса попадает внутрь временного слота данных, этот слот включается в ответ. Из-за того, что метка времени первой точки данных лежит за пределами указанного временного диапазона, в первой точке данных ответа вы увидите *более раннюю* метку времени, чем указанный **startTimestamp**.  Существует три версии точек данных:  * Числовая точка данных: содержит числовое значение. * Enum-точка данных: содержит enum-значение, в настоящее время только для timeseries доступности. * Точка данных прогноза: аналогична числовой точке данных, но содержит доверительный интервал, в пределах которого ожидаются будущие значения. |
| entities | object | Список сущностей, из которых происходят точки данных.  JSON-объект, который сопоставляет ID сущности в Dynatrace и фактическое имя сущности. |
| resolutionInMillisUTC | integer | Разрешение точек данных. |
| timeseriesId | string | ID метрики. |
| unit | string | Единица измерения точек данных. Элемент может принимать значения * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (µs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (‰)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |

#### Объект `ErrorEnvelope`

| Элемент | Тип | Описание |
| --- | --- | --- |
| error | [Error](#openapi-definition-Error) | - |

#### Объект `Error`

| Элемент | Тип | Описание |
| --- | --- | --- |
| code | integer | HTTP-код состояния |
| constraintViolations | [ConstraintViolation[]](#openapi-definition-ConstraintViolation) | Список нарушений ограничений |
| message | string | Сообщение об ошибке |

#### Объект `ConstraintViolation`

Список нарушений ограничений

| Элемент | Тип | Описание |
| --- | --- | --- |
| location | string | - |
| message | string | - |
| parameterLocation | string | -Элемент может принимать значения * `HEADER` * `PATH` * `PAYLOAD_BODY` * `QUERY` |
| path | string | - |

### JSON-модели тела ответа

```
{



"result": {



"aggregationType": "AVG",



"dataPoints": {



"HOST-0000000000000007": [



[



1522220334000,



89



]



]



},



"entities": {



"HOST-0000000000000007": "Laptop-8"



},



"resolutionInMillisUTC": 300000,



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle",



"unit": "Percent"



}



}
```

```
{



"error": {



"code": 1,



"constraintViolations": [



{



"location": "string",



"message": "string",



"parameterLocation": "HEADER",



"path": "string"



}



],



"message": "string"



}



}
```

## Замечание о временном интервале

Dynatrace хранит данные во временных слотах. Объект `dataPoints` показывает *начальную* метку времени слота. Если `startTimestamp` или `endTimestamp` вашего запроса попадает внутрь временного слота данных, этот слот будет включён в ответ. Из-за того, что метка времени первой точки данных лежит за пределами указанного временного диапазона, в первой точке данных ответа вы увидите *более раннюю* метку времени, чем указанный `startTimestamp`.

![Схема меток времени](https://dt-cdn.net/images/timestamp-scheme-541-8f324d62ae.png)

Схема меток времени

## Пример

В этом примере запрос возвращает значения метрики **Actions per session** (`com.dynatrace.builtin:app.actionspersession`) за последний час для приложений **APPLICATION-85A7CC** и **APPLICATION-8E41C8**. Результат возвращает среднее количество действий пользователя на приложение. Результат усечён до трёх точек данных на приложение.

#### Curl

```
curl -X POST \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries \



-H 'Authorization: abcdefjhij1234567890' \



-H 'Content-Type: application/json' \



-d '{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"relativeTime": "hour",



"aggregationType": "avg",



"entities": [



"APPLICATION-85A7CCAAC7345F0B",



"APPLICATION-8E41C8C247910758"



]



}'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries
```

#### Тело запроса

```
{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"relativeTime": "hour",



"aggregationType": "avg",



"entities": [



"APPLICATION-85A7CC",



"APPLICATION-8E41C8"



]



}
```

#### Содержимое ответа

```
{



"result": {



"dataPoints": {



"APPLICATION-85A7CC": [



[



1534920000000,



1.6666666666666667



],



[



1534920060000,



2.5



],



[



1534920120000,



2.888888888888889



]



],



"APPLICATION-8E41C8": [



[



1534920000000,



null



],



[



1534920060000,



3



],



[



1534920120000,



null



]



]



},



"unit": "PerMinute (count/min)",



"resolutionInMillisUTC": 60000,



"aggregationType": "AVG",



"entities": {



"APPLICATION-85A7CC": "Permanent Docker",



"APPLICATION-8E41C8": "easyTravel AMP"



},



"timeseriesId": "com.dynatrace.builtin:app.actionspersession"



}



}
```

#### Код ответа

200