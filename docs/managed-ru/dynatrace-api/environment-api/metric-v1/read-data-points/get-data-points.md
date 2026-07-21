---
title: Timeseries API v1 - GET точки данных
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/read-data-points/get-data-points
scraped: 2026-05-12T11:58:42.494548
---

# Timeseries API v1 - GET точки данных

# Timeseries API v1 - GET точки данных

* Справочник
* Опубликовано 07 ноября 2019 г.

Этот API устарел. В будущем он будет удалён. Используйте вместо него [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.").

Получает параметры и точки данных указанной метрики.

Чтобы получить точки данных, установите параметр **includeData** в `true`. Также необходимо указать временной диапазон и тип агрегации, поддерживаемый запрашиваемой метрикой. Подробнее смотрите в разделе **Parameters**.

Можно получить либо точки данных, либо скалярный результат указанной метрики, в зависимости от **queryMode**.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries/{timeseriesIdentifier}` |

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
| includeData | boolean | Флаг для включения точек данных в ответ. Установите `true`, чтобы получить точки данных. Также необходимо указать временной диапазон и тип агрегации.  По умолчанию `false`, что означает, что точки данных не включаются. | query | Опциональный |
| aggregationType | string | Тип агрегации для результирующих точек данных.  Если запрашиваемая метрика не поддерживает указанную агрегацию, запрос завершится ошибкой. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` | query | Опциональный |
| startTimestamp | integer | Начальная метка времени запрашиваемого временного диапазона, в миллисекундах UTC. | query | Опциональный |
| endTimestamp | integer | Конечная метка времени запрашиваемого временного диапазона, в миллисекундах (UTC).  Если она позже текущего времени, Dynatrace автоматически использует вместо неё текущее время.  Временной диапазон не должен превышать 6 месяцев. | query | Опциональный |
| predict | boolean | Флаг для прогнозирования будущих точек данных. | query | Опциональный |
| relativeTime | string | Относительный временной диапазон, отсчитываемый назад от текущего времени. Элемент может принимать значения * `10mins` * `15mins` * `2hours` * `30mins` * `3days` * `5mins` * `6hours` * `day` * `hour` * `min` * `month` * `week` | query | Опциональный |
| queryMode | string | Тип результата, который должен вернуть вызов. Допустимые режимы результата:  `series`: возвращает все точки данных timeseries в указанном временном диапазоне. `total`: возвращает одно скалярное значение для указанного временного диапазона.  По умолчанию используется режим `series`. Элемент может принимать значения * `SERIES` * `TOTAL` | query | Опциональный |
| entity | string[] | Фильтрует запрашиваемые точки данных по сущности, которая должна их доставить. Допустимые значения, это ID сущностей Dynatrace.  Можно указать несколько сущностей в следующем формате: `entity=entity1&entity=entity2`. Сущность должна соответствовать хотя бы одному из указанных ID.  Если выбранная сущность не поддерживает запрашиваемую timeseries, запрос завершится ошибкой. | query | Опциональный |
| tag | string[] | Фильтрует запрашиваемые точки данных по сущности, которая должна их доставить. Доставляются только данные сущностей с указанным тегом.  Можно указать несколько тегов в следующем формате: `tag=tag1&tag=tag2`. Сущность должна соответствовать **всем** указанным тегам.  В случае тегов «ключ-значение», например импортированных тегов AWS или CloudFoundry, используйте формат `key:value`. Если есть также контекст, используйте формат `[context]key:value`. | query | Опциональный |
| percentile | integer | Указывает, какой процентиль выбранной метрики времени отклика должен быть доставлен.  Применимо только к типу агрегации `PERCENTILE`.  Допустимые значения процентиля, от 1 до 99.  Учтите, что экспорт процентиля возможен только для метрик на основе времени отклика, например времени отклика приложений и сервисов. | query | Опциональный |
| includeParentIds | boolean | Если установлено true, результат раскрывает сопоставления измерений между родительскими сущностями и их потомками.  Например: SERVICE-0000000000000001, SERVICE\_METHOD-0000000000000001 | query | Опциональный |
| considerMaintenanceWindowsForAvailability | boolean | Исключить (`true`) или включить (`false`) точки данных из любого [maintenance window](https://dt-url.net/b2123rg0?dt=m), определённого в вашей среде. | query | Опциональный |

## Ответ

Результат, это JSON-объект, содержащий точки данных и параметры метрики.

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

## Замечание о временном интервале

Dynatrace хранит данные во временных слотах. Объект `dataPoints` показывает *начальную* метку времени слота. Если `startTimestamp` или `endTimestamp` вашего запроса попадает внутрь временного слота данных, этот слот будет включён в ответ. Из-за того, что метка времени первой точки данных лежит за пределами указанного временного диапазона, в первой точке данных ответа вы увидите *более раннюю* метку времени, чем указанный `startTimestamp`.

![Схема меток времени](https://dt-cdn.net/images/timestamp-scheme-541-8f324d62ae.png)

Схема меток времени

## Пример

В этом примере запрос возвращает значения метрики **Actions per session** (`com.dynatrace.builtin:app.actionspersession`) за последний час для приложений **APPLICATION-85A7CC** и **APPLICATION-8E41C8**.

API-токен передаётся в заголовке **Authorization**.

Результат возвращает среднее количество действий пользователя на приложение, усечённое до трёх точек данных на приложение.

#### Curl

```
curl -X GET \



https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=true&relativeTime=hour&aggregationType=avg&entity=APPLICATION-85A7CC&entity=APPLICATION-8E41C8 \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries/com.dynatrace.builtin:app.actionspersession?includeData=true&relativeTime=hour&aggregationType=avg&entity=APPLICATION-85A7CC&entity=APPLICATION-8E41C8
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



"dataResult": {



"dataPoints": {



"APPLICATION-85A7CC": [



[



1534921560000,



1.75



],



[



1534921620000,



2



],



[



1534921680000,



2



]



],



"APPLICATION-8E41C8": [



[



1534921560000,



4



],



[



1534921620000,



7



],



[



1534921680000,



4



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



},



"aggregationTypes": [



"AVG"



],



"filter": "BUILTIN"



}
```

#### Код ответа

200