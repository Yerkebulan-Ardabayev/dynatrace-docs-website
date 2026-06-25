---
title: Timeseries API v1 - GET список метрик
source: https://docs.dynatrace.com/managed/dynatrace-api/environment-api/metric-v1/metric-definitions/get-list
scraped: 2026-05-12T11:58:38.274891
---

# Timeseries API v1 - GET список метрик

# Timeseries API v1 - GET список метрик

* Справочник
* Опубликовано 06 ноября 2019 г.

Этот API устарел. В будущем он будет удалён. Используйте вместо него [Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Получение информации о метриках через Metrics v2 API.").

Перечисляет все определения метрик вместе с параметрами каждой метрики, доступной в вашей среде.

Полный список может быть длинным, но его можно сузить, указав параметры фильтрации, например источник метрики. Подробнее смотрите в разворачиваемом разделе **Parameters**.

Запрос возвращает payload `application/json`.

|  |  |  |
| --- | --- | --- |
| GET | ManagedDynatrace for Government | `https://{your-domain}/e/{your-environment-id}/api/v1/timeseries` |
| GET | Environment ActiveGate | `https://{your-activegate-domain}/e/{your-environment-id}/api/v1/timeseries` |

## Аутентификация

Для выполнения запроса нужен access-токен со scope `DataExport`.

О том, как получить и использовать токен, смотрите [Tokens and authentication](/managed/discover-dynatrace/references/dynatrace-api/basics/dynatrace-api-authentication).

## Параметры

| Параметр | Тип | Описание | В | Обязательный |
| --- | --- | --- | --- | --- |
| source | string | Тип метрики, например BUILTIN или CUSTOM. Элемент может принимать значения * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` | query | Опциональный |
| detailedSource | string | Функциональность, из которой происходят метрики, например Synthetic или RUM. | query | Опциональный |

### Возможные значения для элемента `detailedSource`:

Допустимые значения для элемента `detailedSource` можно найти в подзаголовках разделов **Built-in metrics** и **Plugin metrics** на страницах доступных метрик для [SaaS](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Изучите полный список встроенных метрик Dynatrace.") и [Managed](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Изучите полный список встроенных метрик Dynatrace."). Используйте их точно как в заголовках, пробелы включительно.

## Ответ

Результат, это JSON, содержащий массив объектов, где каждый объект представляет метрику.

### Коды ответа

| Код | Тип | Описание |
| --- | --- | --- |
| **200** | [TimeseriesDefinition[]](#openapi-definition-TimeseriesDefinition) | Успех |
| **4XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне клиента. |
| **5XX** | [ErrorEnvelope](#openapi-definition-ErrorEnvelope) | Ошибка на стороне сервера. |

### Объекты тела ответа

#### Объект `ResponseBody`

#### Объект `TimeseriesDefinition`

Конфигурация метрики со всеми её параметрами.

| Элемент | Тип | Описание |
| --- | --- | --- |
| aggregationTypes | string[] | Список допустимых агрегаций для этой метрики. Элемент может принимать значения * `AVG` * `COUNT` * `MAX` * `MEDIAN` * `MIN` * `PERCENTILE` * `SUM` |
| detailedSource | string | Функциональность, из которой происходит метрика. |
| dimensions | string[] | Детальное деление метрики, например группа процессов и ID процесса для некоторых метрик, связанных с процессами. |
| displayName | string | Имя метрики в интерфейсе пользователя. |
| filter | string | Функциональность, из которой происходит метрика. Элемент может принимать значения * `ALL` * `BUILTIN` * `CUSTOM` * `PLUGIN` * `REMOTE_PLUGIN` |
| pluginId | string | ID плагина, из которого происходит метрика. |
| timeseriesId | string | ID метрики. |
| types | string[] | Определение типа технологии. Используется для группировки метрик под логическим именем технологии. |
| unit | string | Единица измерения метрики. Элемент может принимать значения * `Ampere (A)` * `Billion (Gcount)` * `Bit (bit)` * `BitPerHour (bit/h)` * `BitPerMinute (bit/min)` * `BitPerSecond (bit/s)` * `Byte (B)` * `BytePerHour (B/h)` * `BytePerMinute (B/min)` * `BytePerSecond (B/s)` * `Cores` * `Count (count)` * `Day (ds)` * `DecibelMilliWatt (dBm)` * `G` * `GibiByte (GiB)` * `GibiBytePerHour (GiB/h)` * `GibiBytePerMinute (GiB/min)` * `GibiBytePerSecond (GiB/s)` * `GigaByte (GB)` * `GigaBytePerHour (GB/h)` * `GigaBytePerMinute (GB/min)` * `GigaBytePerSecond (GB/s)` * `Hertz (Hz)` * `Hour (hs)` * `KibiByte (KiB)` * `KibiBytePerHour (KiB/h)` * `KibiBytePerMinute (KiB/min)` * `KibiBytePerSecond (KiB/s)` * `KiloByte (kB)` * `KiloBytePerHour (kB/h)` * `KiloBytePerMinute (kB/min)` * `KiloBytePerSecond (kB/s)` * `M` * `MSU` * `MebiByte (MiB)` * `MebiBytePerHour (MiB/h)` * `MebiBytePerMinute (MiB/min)` * `MebiBytePerSecond (MiB/s)` * `MegaByte (MB)` * `MegaBytePerHour (MB/h)` * `MegaBytePerMinute (MB/min)` * `MegaBytePerSecond (MB/s)` * `MicroSecond (µs)` * `MilliSecond (ms)` * `MilliSecondPerMinute (ms/min)` * `Million (Mcount)` * `Minute (mins)` * `Month (mos)` * `N/A` * `NanoSecond (ns)` * `NanoSecondPerMinute (ns/min)` * `PerHour (count/h)` * `PerMinute (count/min)` * `PerSecond (count/s)` * `Percent (%)` * `Pixel (px)` * `Promille (‰)` * `Ratio` * `Second (s)` * `State` * `Trillion (Tcount)` * `Unspecified` * `Volt (V)` * `Watt (W)` * `Week (ws)` * `Year (ys)` * `k` * `km/h` * `m/h` * `m/s` * `mCores` |
| warnings | string[] | Предупреждения, возникшие при создании метрики. |

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
[



{



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"detailedSource": "Infrastructure",



"dimensions": [



"HOST"



],



"displayName": "CPU idle",



"filter": "BUILTIN",



"timeseriesId": "com.dynatrace.builting:host.cpu.idle",



"types": [



"Test"



],



"unit": "Percent",



"warnings": []



}



]
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

В этом примере запрос перечисляет метрики типа **PLUGIN**, где детальный источник, это **PHP-FPM**.

API-токен передаётся в заголовке **Authorization**.

Результат усечён до двух записей.

#### Curl

```
curl -X GET \



'https://mySampleEnv.live.dynatrace.com/api/v1/timeseries?source=plugin&detailedsource=PHP-FPM' \



-H 'Authorization: Api-Token dt0c01.abc123.abcdefjhij1234567890'
```

#### URL запроса

```
https://mySampleEnv.live.dynatrace.com/api/v1/timeseries?api-token&source=plugin&detailedsource=PHP-FPM
```

#### Содержимое ответа

```
[



{



"timeseriesId": "beta.python.phpfpm.dev:accepted conn",



"displayName": "accepted conn",



"dimensions": [



"PROCESS_GROUP_INSTANCE",



"pool"



],



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"unit": "Count (count)",



"filter": "PLUGIN",



"detailedSource": "PHP-FPM",



"pluginId": "beta.python.phpfpm.dev",



"types": []



},



{



"timeseriesId": "beta.python.phpfpm.dev:active processes",



"displayName": "active processes",



"dimensions": [



"PROCESS_GROUP_INSTANCE",



"pool"



],



"aggregationTypes": [



"AVG",



"SUM",



"MIN",



"MAX"



],



"unit": "Count (count)",



"filter": "PLUGIN",



"detailedSource": "PHP-FPM",



"pluginId": "beta.python.phpfpm.dev",



"types": []



}



]
```

#### Код ответа

200

## Типы процессов

Список известных типов процессов, которые мы мониторим с помощью Dynatrace, постоянно растёт. Если вы не видите нужный тип процесса в списке ниже, обратитесь к странице процессов Dynatrace, чтобы проверить, включён ли процесс там.

Нажмите, чтобы посмотреть список типов процессов

|  |  |  |  |
| --- | --- | --- | --- |
| * apachehttp * apmng * awsrds * cassandra * couchdb * db2 * dockerdaemon * dotnet * erlang * glassfish | * haproxy * iis * iisapppool * java * jboss * linuxsystem * memcached * mongodb * mongodbrouter | * mssql * mysql * nginx * nodejs * oracledb * perl * php * postgres * python | * redis * ruby * tomcat * unknown * varnishcache * weblogic * websphere * windowsservice * windowssystem |

## Типы ОС

Список известных операционных систем, которые мы мониторим с помощью Dynatrace, постоянно растёт. Если вы не видите нужный тип ОС в списке ниже, обратитесь к странице хостов Dynatrace, чтобы проверить, включён ли тип ОС там.

Нажмите, чтобы посмотреть список ОС

|  |  |
| --- | --- |
| * aix * darwin * hpux * linux | * solaris * unknown * windows * zos |

## Типы сервисов

Нажмите, чтобы посмотреть список сервисов

|  |  |
| --- | --- |
| * database * messaging * method * mobile * process | * rmi * unknown * webrequest * webservice * website |

## Типы технологий

Нажмите, чтобы посмотреть список технологий

|  |  |
| --- | --- |
| * apache * dotnet * iis * java * loganalytics * net * nginx * nodejs | * os * php * ruby * sdk * unknown * varnish * wsmb * z |

## Типы агрегации

Нажмите, чтобы посмотреть список типов агрегации

|  |  |
| --- | --- |
| * max * min * sum * count | * avg * median * percentile |

## Связанные темы

* [Extend metric observability](/managed/ingest-from/extend-dynatrace/extend-metrics "Узнайте, как расширить наблюдаемость метрик в Dynatrace.")