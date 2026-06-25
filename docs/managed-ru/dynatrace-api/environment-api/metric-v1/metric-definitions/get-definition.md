---
title: Timeseries API v1 - GET определение метрики
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-definition
scraped: 2026-05-12T11:58:36.185674
---

# Timeseries API v1 - GET определение метрики

# Timeseries API v1 - GET определение метрики

* Справочник
* Опубликовано 06 ноября 2019 г.

Этот API устарел. В будущем он будет удалён. Используйте вместо него [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.").

Возвращает определение указанной метрики.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

Чтобы получить определение метрики без её точек данных, установите параметр **includeData** в `false`.

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| timeseriesId | string | Чувствительный к регистру ID метрики, из которой вы хотите прочитать параметры.  Чтобы получить список доступных метрик, можно выполнить запрос [GET metric definitions](/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list "Просмотр определений всех метрик вашей среды мониторинга через Timeseries v1 API."). | path | Обязательный |
| includeData | boolean | Флаг для включения точек данных в ответ. Установите `false`, чтобы получить только определение метрики. | query | Опциональный |

## Ответ

Результат, это JSON-объект, содержащий параметры метрики. Объект **TimeseriesDataPointQueryResult** в этом случае не возвращается.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TimeseriesQueryResult](#openapi-definition-TimeseriesQueryResult) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `TimeseriesQueryResult`

Конфигурация метрики со всеми её параметрами и, опционально, точками данных.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregationTypes | string[] | Список допустимых агрегаций для этой метрики. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| dataResult | [TimeseriesDataPointQueryResult](#openapi-definition-TimeseriesDataPointQueryResult) | Список точек данных метрики, а также их параметры. |
| detailedSource | string | Функциональность, из которой происходит метрика. |
| dimensions | string[] | Детальное деление метрики, например группа процессов и ID процесса для некоторых метрик, связанных с процессами. |
| displayName | string | Имя метрики в интерфейсе пользователя. |
| filter | string | Функциональность, из которой происходит метрика. Элемент может принимать значения * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` |
| pluginId | string | ID плагина, из которого происходит метрика. |
| timeseriesId | string | ID метрики. |
| types | string[] | Определение типа технологии. Используется для группировки метрик под логическим именем технологии. |
| unit | string | Единица измерения метрики. Элемент может принимать значения * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (µs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (‰)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| warnings | string[] | Предупреждения, возникшие при создании метрики. |

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



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"dataResult": {



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



},



"detailedSource": "Infrastructure",



"dimensions": [



"HOST"



],



"displayName": "CPU idle",



"filter": "BUILTIN",



"timeseriesId": "com.dynatrace.builtin:host.cpu.idle",



"types": [],



"unit": "Percent"



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

## Пример

В этом примере запрос запрашивает определение метрики **Actions per session** (`com.dynatrace.builtin:app.actionspersession`).

API-токен передаётся в заголовке **Authorization**.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=false \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=false
```

#### Содержимое ответа

```
{



"timeseriesId": "com.dynatrace.builtin:app.actionspersession",



"displayName": "Actions per session",



"dimensions": [



"APPLICATION"



],



"unit": "PerMinute (count/min)",



"detailedSource": "Web application",



"types": [],



"aggregationTypes": [



"AVG"



],



"filter": "BUILTIN"



}
```

#### Код ответа

200

## Связанные темы

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")