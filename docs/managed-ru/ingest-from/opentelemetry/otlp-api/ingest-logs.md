---
title: Приём OTLP-логов
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/otlp-api/ingest-logs
---

# Приём OTLP-логов

# Приём OTLP-логов

* Справочник
* 3 мин. чтения
* Обновлено 15 июл. 2026

OpenTelemetry поддерживает атрибуты на разных уровнях запроса журнала OpenTelemetry: на уровне ресурса (resource), области видимости (scope) и записи (record).

Log ingestion API собирает данные логов и выполняет их автоматическую трансформацию.

## Трансформация данных

Каждая запись лога из принятого батча преобразуется в одну запись лога Dynatrace, которая содержит три специальных атрибута: `timestamp`, `loglevel`, `content`, а также набор прочих атрибутов «ключ-значение». Эти свойства задаются на основе ключей, присутствующих во входном объекте, по следующим правилам.

### Timestamp

* Задаётся на основе поля **Timestamp** входной записи лога.

* Если `timestamp` не удаётся задать на основе поля **Timestamp**, значение определяется по одному из следующих источников, проверяемых в указанном порядке:

  1. Содержимое body (если body является картой).
  2. Атрибуты записи OTLP-лога.
* Если метка времени берётся из body или записи OTLP-лога, значение определяется по первому найденному ключу из следующего списка (порядок важен, регистр не учитывается): `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.

* Поддерживаемые форматы: Unix epoch time в UTC, `RFC3339` и `RFC3164`.
  Unix epoch time может быть указан в секундах, миллисекундах и (начиная с Dynatrace версии 1.339+) дробных секундах.
* Если метка времени отсутствует, используются текущее время и часовой пояс UTC по умолчанию.
* Записи логов старше лимита **Log Age** отбрасываются. Метки времени, опережающие текущее время более чем на 10 минут, заменяются текущим временем. Подробности в разделе [Лимиты приёма](#ingestion-limits).

### Log level

* Задаётся на основе поля **SeverityText** (приоритет 1) или поля **SeverityNumber** (приоритет 2) входной записи лога.

* Если `loglevel` не удаётся задать на основе полей **SeverityText** или **SeverityNumber**, значение определяется по одному из следующих источников, проверяемых в указанном порядке:

  1. Содержимое body (если body является картой).
  2. Атрибуты записи OTLP-лога.
* Если `loglevel` берётся из body или записи OTLP-лога, значение определяется по первому найденному ключу из следующего списка (порядок важен, регистр не учитывается): `loglevel`, `status`, `severity`, `level`, `syslog.severity`.

* Значение по умолчанию: `NONE`.

### Content

* Content задаётся на основе поля **Body** входной записи лога.

* Если поле **Body** имеет тип **kvlist\_value** (список пар «ключ-значение»), `content` задаётся по значению первого найденного в **Body** ключа из следующего списка (порядок важен): `content`, `message`, `payload`, `body`, `log`.
* Если ни один из поддерживаемых ключей content не найден, `content` устанавливается в пустую строку.

* Если поле **Body** не является строковым типом, значение преобразуется в строку. Для составных типов применяется преобразование в строку формата JSON.

### Attributes

* Содержит все остальные атрибуты входной записи из разделов **Resource**, **InstrumentationScope** и **Attributes**.
* Атрибуты `TraceID` и `SpanID` отображаются в поля `trace_id` и `span_id`, а их значения преобразуются в шестнадцатеричный формат (например, `0xCAFEBABE`).
* Автоматический атрибут. Атрибут `dt.auth.origin` автоматически добавляется к каждой записи лога, принятой через API. Значение атрибута, это публичная часть ключа API, которым источник логов авторизуется для подключения к универсальному Log ingest API.

Все атрибуты рекомендуется сопоставлять с **semantic attributes**, чтобы Dynatrace корректно их интерпретировал. Подробности в [Semantic attributes (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "Supported semantic attributes that are indexed in Log Monitoring Classic.").

## Типы данных

Dynatrace поддерживает типы данных OpenTelemetry, описанные в разделах ниже.

### Scalar value

Все ключи атрибутов приводятся к нижнему регистру, значения атрибутов преобразуются в строки. Пользовательские и семантические атрибуты, как правило, доступны в запросах.

### Byte array

Массивы байтов преобразуются в строки base64. Например, массив

```
[0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]
```

преобразуется и принимается как `aGVsbG8gd29yZA==`.

### Array

Значения атрибутов-массивов преобразуются в массивы единообразного типа. Целевой тип выбирается по следующим правилам:

* Составные значения, такие как массивы или объекты, отображаются в строки JSON.
* Если хотя бы одно значение в массиве является строкой или должно быть преобразовано в строку (например, объект или массив), целевой тип всего массива, строка.
* Если все значения исходного массива числовые, целевой тип массива, числовой.
* Значения null считаются совместимыми с любым типом.

### Map

Карты принимаются путём рекурсивного извлечения ключей: значения сохраняются как отдельные атрибуты с именами, отражающими их положение в иерархии карты и содержащими в качестве префикса имя карты. Подробности в разделе [Обработка Log ingestion API](#otlp-structured-logs).

## Лимиты приёма

Лимиты для принимаемых запросов логов, их атрибутов и значений атрибутов описаны в [Log Monitoring default limits (Logs Classic)](/managed/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.").

Рекомендации по размеру ActiveGate для приёма OTLP-логов:

* [Linux ActiveGate sizing guide](/managed/ingest-from/dynatrace-activegate/installation/linux/linux-activegate-hardware-and-system-requirements#sizing-guide "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Linux for routing and monitoring purposes.")
* [Windows ActiveGate sizing guide](/managed/ingest-from/dynatrace-activegate/installation/windows/windows-activegate-hardware-and-system-requirements#sizing-guide "Learn what hardware and operating system requirements need to be taken into account before installing ActiveGate on Windows for routing and monitoring.")
* [Kubernetes ActiveGate sizing guide](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/resource-management/ag-resource-limits "Find CPU and memory resource recommendations for Dynatrace ActiveGates deployed in Kubernetes, sized by cluster scale and workload type.")

## Обработка Log ingestion API

Содержимое структурированных логов трансформируется, как описано ниже. Все примеры применимы к endpoints Log ingestion API, доступным на Environment ActiveGate.

#### Карты и массивы в атрибутах

В этом случае значения атрибутов-карт выравниваются, то есть ключи объединяются через точку (.) до достижения простого значения в иерархии, а значения атрибутов-массивов преобразуются в пользовательскую строку.

| Входные данные | Вывод endpoint Log ingestion API |
| --- | --- |
| ```  body: "Hello world!"  Resource:  - "any-attr-type-3": {"3" = "c"}  Scope:  - "any-attr-type-2" : {"2" = "b"}  Attributes:  - "any-attr-type-1" : {"1" = "a"}  - "any-attr-type-4" :  [ "val1", 10, -123.456, false, 0x01020304 ] ``` | ```  "content": "Hello world!"  "any-attr-type-1.1": "a"  "any-attr-type-2.2": "b"  "any-attr-type-3.3": "c"  "any-attr-type-4":  ["val1", 10, -123.456, false, "AQIDBA=="] ``` |

Выравнивание выполняется до максимального уровня вложенности, заданного лимитом **Nested objects**. Структуры с вложенностью сверх этого предела заменяются строковым значением `<truncated due to nesting limit>`. Подробности в разделе [Лимиты приёма](#ingestion-limits).

#### Карта в body

Если поле **Body** имеет тип **kvlist\_value** (список пар «ключ-значение»), структура обрабатывается так же, как атрибуты записи лога, включая выравнивание и разрешение конфликтов.

Атрибуты из **Body** также могут использоваться для задания атрибутов `timestamp`, `loglevel` и `content` записи лога, как описано ниже.

| Входные данные | Вывод endpoint Log ingestion API |
| --- | --- |
| ```  Body:  {  "content" = "Hello World!",  "my-body-attr-1": "abc",  "my-body-nested-1": {  "subkey": "val"  },  "@timestamp": "2025-06-01 13:01:02.123",  "loglevel": "INFO"  }  Attributes:  - "any-attr-type-1" : "my-attr" ``` | ```  "content": "Hello world!"  "timestamp": "2025-06-01 13:01:02.123"  "loglevel": "INFO"    "any-attr-type-1": "my-attr"  "my-body-attr-1": "abc"  "my-body-nested-1.subkey": "val" ``` |

#### Body как массив

В этом случае массив в body преобразуется в строку.

| Входные данные | Вывод endpoint Log ingestion API |
| --- | --- |
| ```  Body:  [ "string-val", true, 12, 12.34, 0x6279746573 ] ``` | ```  "content": "[\"string-val\",true,12,12.34,\"Ynl0ZXM=\"]"  ... ``` |

#### Конфликты имён

Когда атрибуты сохраняются в выровненном виде на стороне Dynatrace, возможны коллизии имён, если атрибуты на разных уровнях имеют одно и то же имя. Dynatrace разрешает это путём добавления префикса `overwritten[COUNTER].` к дублирующимся атрибутам. Значение счётчика указывает, сколько раз имя атрибута уже встречалось как дубликат.

Например, если на уровнях resource, scope и log есть три атрибута с именем `my.attribute`:

* атрибут resource принимается как `my.attribute`
* атрибут scope принимается как `overwritten1.my.attribute`
* атрибут log принимается как `overwritten2.my.attribute`

## Обработка дополнительных attributers

Log ingestion API дополнительно принимает атрибуты логов через:

* Параметры запроса
* Специальный заголовок: `X-Dynatrace-Attr`

Эти атрибуты объединяются с атрибутами из запроса логов OpenTelemetry согласно правилам, описанным ниже.

### Атрибуты параметров запроса

* Все параметры запроса, переданные в endpoint Log ingestion API, добавляются к атрибутам записи лога.
* Если ключ параметра встречается несколько раз, все значения фиксируются как атрибут-массив.
* Ключи и значения следуют тем же правилам разбора атрибутов, что и атрибуты запроса лога.
* Некоторые параметры обрабатываются API во внутренних целях и никогда не попадают в атрибуты записи лога, даже если переданы явно (например, используемые в заголовке **X‑Dynatrace‑Options**). Полный список зарезервированных имён параметров и описание их обработки см. в [документации API](/managed/dynatrace-api/environment-api/opentelemetry/post-logs#parameters "Send OpenTelemetry logs to Dynatrace via API.").

#### Пример

| URL запроса | Результат |
| --- | --- |
| ```  otlphttp:  logs_endpoint: /api/v2/otlp/v1/logs?env=prod&env=blue&team=payments ```  ```  Body: "Hello World!" ``` | ```  {  "content": "Hello World!",  "env": ["prod", "blue"],  "team": "payments"  } ``` |

### Атрибуты через заголовок (X-Dynatrace-Attr)

API поддерживает специальный заголовок для передачи дополнительных атрибутов:

```
otlphttp:



endpoint: /api/v2/otlp



headers:



X-Dynatrace-Attr: region=eu-central-1&team=core
```

Правила:

* Ключи и значения следуют тем же правилам разбора атрибутов, что и параметры запроса.
* Многозначное поведение также поддерживается для атрибутов заголовка.
* Те же ограничения на зарезервированные имена параметров сохраняются.

### Правила приоритета атрибутов

Когда атрибуты присутствуют в нескольких местах, Log ingestion API применяет приоритет атрибутов, при этом сохраняя значения body для возможности аудита. Атрибуты применяются в следующем порядке:

* Параметры запроса (наивысший приоритет)
* Заголовок X-Dynatrace-Attr
* Запрос лога OpenTelemetry (наименьший приоритет; существующий путь ingestion)

#### Поведение при переопределении

Когда атрибуты из параметров запроса или заголовка переопределяют атрибуты запроса лога:

* Итоговое значение атрибута устанавливается согласно правилам приоритета источника атрибутов.
* Значения, уже присутствующие в запросе лога, сохраняются и дублируются под ключом `overwrittenN.<attribute_key>`.
  Где N, это возрастающее целое число (1, 2, …) в зависимости от того, сколько значений из запроса лога потребовалось сохранить. Это обеспечивает уникальность даже при нескольких конфликтах.
* Под ключами `overwrittenN.*` сохраняются только значения, исходящие из запроса лога. Атрибуты, переопределённые источниками с более высоким приоритетом, не порождают сохранённых копий.

#### Пример

| Запрос | Результат |
| --- | --- |
| ```  otlphttp:  logs_endpoint: /api/v2/otlp/v1/logs?team=frontend ```  Запрос лога:  ```  Body: "Hello World!"  Attributes:  - "team": "backend" ``` | ```  {  "content": "Hello World!",  "team": "frontend",  "overwritten1.team": "backend"  } ``` |

### Поведение при биллинге

Атрибуты, переданные через параметры запроса или заголовки, учитываются в расчётах биллинга.

Для многозначных атрибутов ключ атрибута учитывается в биллинге только один раз, независимо от количества значений.

## Связанные темы

* [OpenTelemetry logs ingest API](/managed/dynatrace-api/environment-api/opentelemetry/post-logs "Send OpenTelemetry logs to Dynatrace via API.")