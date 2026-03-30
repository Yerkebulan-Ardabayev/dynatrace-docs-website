---
title: Включение OpenTelemetry Span Sensor для OneAgent
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration
scraped: 2026-03-06T21:30:54.102654
---

* Latest Dynatrace

Помимо конфигурации на стороне приложения, несколько специфичных для Dynatrace настроек позволяют управлять тем, как данные OpenTelemetry используются в Dynatrace.

Чтобы узнать, как отправлять данные OpenTelemetry в Dynatrace OneAgent, см. Использование OneAgent с данными OpenTelemetry.

## Предварительные требования

Java

Go

Node.js

PHP

.NET и .NET Core

.NET Framework

Python

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracing](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Поддерживается в AWS Lambda.

Для включения OpenTelemetry Java

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (Java)**.

Существующие трейсеры заменяются и перестанут работать после включения OpenTelemetry Java.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.41 |

Opt-in

Для включения OpenTelemetry Go

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (Go) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для Go.

OneAgent версии 1.217 и ранее: OpenTelemetry Go Sensor распространяет контекст Dynatrace между процессами только если включена опция **Send W3C Trace Context HTTP headers**:

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
2. Включите **Send W3C trace context HTTP headers**.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://www.npmjs.com/package/@opentelemetry/api) | 1[1](#fn-monitoring-framework-1-def) |

1

Поддерживается в AWS Lambda

Opt-in

Для включения OpenTelemetry Node.js:

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

1. Найдите и включите **OpenTelemetry (Node.js) [Opt-In]**.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

Opt-in

Для включения OpenTelemetry PHP:

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (PHP) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для PHP.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

Для включения OpenTelemetry .NET и .NET Core:

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (.NET) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для .NET.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

Для включения OpenTelemetry .NET Framework:

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (.NET) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для .NET.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-python) | 1.1+ |

Opt-in

Для включения OpenTelemetry Python:

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Найдите и включите **OpenTelemetry (Python) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для Python.

## Редактирование атрибутов

OpenTelemetry Span Sensor модуля кода OneAgent автоматически захватывает все атрибуты OpenTelemetry.
Если вы хотите предотвратить случайное сохранение персональных данных, вы можете исключить определённые ключи атрибутов, значения которых не должны сохраняться.
Исключив атрибуты, содержащие персональные данные, вы можете выполнить требования вашей организации по конфиденциальности и контролировать область хранимых данных мониторинга.

Для настройки хранения и маскирования атрибутов вашей среды

1. Перейдите на соответствующую страницу настроек:

   * В Latest Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **OneAgent features**.
   * В Dynatrace Classic перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**

2. Выберите **Server-side service monitoring** > **Attribute capturing**.
3. (необязательно) Чтобы изменить стандартное поведение хранения атрибутов OpenTelemetry, перейдите в **Preferences**.

   * Чтобы хранить все атрибуты, кроме указанных в списке **Blocked attributes**, выберите **Allow all attributes**
   * Чтобы блокировать все атрибуты, кроме указанных в списке **Allowed attributes**, выберите **Block all attributes**

   Возможен только один вариант настройки.
4. Добавьте имя атрибута в список атрибутов.

   1. На странице **Attribute capturing** выберите **Blocked attributes** или **Allowed attributes**.

      Список разрешённых атрибутов: Dynatrace рекомендует включать несколько базовых атрибутов, таких как `service.name` или `service.version`. Для удобства Dynatrace поставляется с конфигурацией по умолчанию, которую можно изменить.
   2. Выберите **Add item**, чтобы добавить новый ключ в список атрибутов, и введите ключ.
   3. Выберите **Save changes**.
5. Выполните следующие действия для маскирования хранимого значения атрибута.

   1. На странице **Attribute capturing** выберите **Attribute data masking**.
   2. Выберите **Add item**, чтобы добавить новый ключ в список маскируемых атрибутов.
   3. Введите ключ хранимого значения и выберите вариант из выпадающего списка **Masking**. Подробнее о вариантах маскирования см. в разделе Трассировки OpenTelemetry.
   4. Выберите **Save changes**.

После этого ключ атрибута можно найти на странице **Distributed traces** на [вкладке **Summary**](../../../observe/application-observability/distributed-traces/use-cases/segment-request.md#summary-tab "Улучшите производительность распределённой системы, сегментируя запросы с медленным временем ответа через Service flow и анализируя их распределённые трассировки.").

## Ограничения поиска трассировок

### Атрибуты ресурсов

Поиск по атрибуту ресурса ограничен именем сервиса: фильтрация по `Service name` на странице **Distributed traces**.

### Атрибуты спанов

Поиск по атрибуту спана ограничен именем спана: фильтрация по `Request` на странице **Distributed traces**.

## Как работает Span Sensor

Подробнее о OpenTelemetry Span Sensor модуля кода OneAgent см. [Обнаружение спанов OpenTelemetry с помощью OpenTelemetry Span Sensor модуля кода OneAgent](oneagent-otel.md#oneagent-otel-span-sensor "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.").

### Точки входа

Чтобы избежать возможных конфликтов с существующими распределёнными трассировками PurePath, OneAgent по умолчанию принимает только спаны с [видом спана](https://opentelemetry.io/docs/concepts/signals/traces/#span-kind) `Server` или `Consumer`. Обычно это не является проблемой, поскольку библиотеки инструментирования, как правило, настраивают соответствующий вид спана, однако это следует учитывать, если ваше приложение полностью использует ручное инструментирование.

Это поведение можно настроить с помощью [правила точки входа](../../extend-dynatrace/extend-tracing/span-settings.md#span-entry-points "Узнайте, как настроить параметры спанов для OpenTelemetry и OpenTracing."). Для этого в Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span entry points** и создайте новое правило с соответствующим действием и записью для сопоставления.

### Иерархия спанов

В зависимости от вашей конфигурации вы можете столкнуться с «плоским обогащением спанов». Это ситуация, когда спаны отображаются в Dynatrace в виде плоского списка, а не древовидной иерархии. Хотя в целом это поведение по умолчанию при приёме трассировок OpenTelemetry через OneAgent, иерархия всё ещё может отражать фактические связи между спанами, определённые инструментированием, в зависимости от задействованных модулей кода OneAgent и их поддержки инструментируемых технологий.

Листовые спаны

При объединении спанов OpenTelemetry с трассировками сенсоров OneAgent убедитесь, что спаны OpenTelemetry являются листовыми спанами и не находятся между спанами OneAgent.

### Захват атрибутов

Поскольку OneAgent принимает спаны уже [при их создании](#point-of-ingestion), не все конечные атрибуты могут присутствовать при первоначальном приёме. Любые атрибуты, добавленные позднее, отмечаются в Dynatrace пометкой `initial value not set` и не могут использоваться для правил захвата спанов, поскольку они ещё не были доступны при оценке правил.

### Распространение контекста

При автоматическом приёме трассировок OpenTelemetry с помощью OneAgent Span Sensor существует различие между распространением контекста трассировок OpenTelemetry и трассировок OneAgent.

Хотя распространение трассировок OpenTelemetry может уже корректно обрабатываться вашим приложением, важно также объединить их со специфичной для OneAgent трассировкой. Это можно осуществить с помощью [правила распространения контекста](../../extend-dynatrace/extend-tracing/span-settings.md#span-context-propagation "Узнайте, как настроить параметры спанов для OpenTelemetry и OpenTracing."). Для настройки в Dynatrace перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **OpenTelemetry** > **Span context propagation** и создайте правило распространения контекста с действием `Propagate` и записью для сопоставления нужного спана (например, по имени спана или библиотеке инструментирования).

Старайтесь избегать объединения трассировок для технологий, уже нативно покрытых сенсорами OneAgent. Объединение таких спанов OpenTelemetry с трассировкой OneAgent может привести к неопределённым состояниям.

## Экспорт в сторонние бэкенды при использовании OneAgent

В то время как трассировки OpenTelemetry всегда экспортируются в другие бэкенды без изменений, небольшая корректировка данных происходит, когда ваше приложение, инструментированное OneAgent, начинает новую трассировку OpenTelemetry. Это касается только новых трассировок, а не продолжения трассировки через распространение контекста.

В этом случае OneAgent может уже создать новый объект трассировки при инициализации OpenTelemetry. Если эти две трассировки (с разными идентификаторами) не согласованы, данные телеметрии могут быть дублированы или фрагментированы. Чтобы избежать этого и при этом сохранить согласованность трассировок Dynatrace PurePath, OneAgent использует следующий подход:

* Идентификатор трассировки OpenTelemetry имеет приоритет при экспорте в сторонние системы
* На бэкенде Dynatrace вместо него назначается идентификатор трассировки PurePath

Для обеспечения корреляции между этими двумя идентификаторами Dynatrace создаёт дополнительные [ссылки спанов](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans) для каждого спана, связывая их с трассировкой OpenTelemetry.

Перезапись идентификатора применяется только к вновь начатым трассировкам (не к распространению контекста) и к SDK OpenTelemetry для Go, Java, JavaScript, PHP и Python, но не для .NET.

## Ограничения

### Java

* OneAgent версии 1.294 и ранее: OneAgent заменяет установленные глобальные компоненты SDK OpenTelemetry `TracerProvider`, `Propagator` и `ContextManager`.
  Поэтому при включённом OpenTelemetry Java трассировки больше не видны этому SDK и не экспортируются в бэкенды, такие как Jaeger.
* OneAgent версии 1.259+: для избежания дубликатов OneAgent [игнорирует спаны некоторых библиотек автоматического инструментирования](#java-span-dropping).
* Когда сенсоры OneAgent и OpenTelemetry присутствуют одновременно для одной технологии, возможны дополнительные накладные расходы.

### Go

* OneAgent может инструментировать только реализацию Tracer из стандартного SDK OpenTelemetry.
* Когда сенсоры OneAgent и OpenTelemetry присутствуют одновременно для одной технологии, возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Дополнительные накладные расходы

### Node.js

* OneAgent версии 1.331+: для избежания дубликатов OneAgent [игнорирует спаны некоторых библиотек автоматического инструментирования](#nodejs-span-dropping).
* OneAgent версии 1.329 и ранее: когда OneAgent и OpenTelemetry инструментируют один и тот же модуль (например, HTTP или GRPC), возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Разрывы в распределённых трассировках
  + Дополнительные накладные расходы
* OneAgent версии 1.261 и ранее: OneAgent заменяет установленные глобальные компоненты SDK OpenTelemetry `TracerProvider`, `Propagator` и `ContextManager`.
  Поэтому при включённом OpenTelemetry Node.js трассировки больше не видны этому SDK и не экспортируются в бэкенды, такие как Jaeger.

### PHP

* OneAgent версии 1.313+: для избежания дубликатов OneAgent [игнорирует спаны некоторых библиотек автоматического инструментирования](#php-span-dropping).

### Python

* Когда сенсоры OneAgent и OpenTelemetry присутствуют одновременно для одной технологии, возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Разрывы в распределённых трассировках
  + Дополнительные накладные расходы

### Все языки

* OneAgent захватывает атрибуты ресурсов OpenTelemetry только если они предоставлены через переменные окружения `OTEL_SERVICE_NAME` и `OTEL_RESOURCE_ATTRIBUTES`. При использовании API приёма трассировок OpenTelemetry это ограничение не применяется.
* Невозможно создать атрибуты запросов (обычно используемые для поиска и фильтрации трассировок) на основе атрибутов ресурсов OpenTelemetry.
* OneAgent обрезает значения атрибутов, превышающие 4096 символов.

## Предотвращение дублирования спанов в Java

OneAgent версии 1.259+

Чтобы избежать возможного дублирования спанов для областей, охваченных как OpenTelemetry, так и OneAgent, OneAgent пропускает спаны из следующих библиотек автоматического инструментирования Java, если OneAgent настроен на инструментирование вашего Java-приложения и приём спанов OpenTelemetry.

Такие спаны пропускаются только OneAgent. Экспорт в сторонние системы (например, другие бэкенды или Collector) не затрагивается.

## Предотвращение дублирования спанов в Node.js

OneAgent версии 1.331+

Чтобы избежать возможного дублирования спанов для областей, охваченных как OpenTelemetry, так и OneAgent, OneAgent пропускает спаны из следующих библиотек автоматического инструментирования Node.js, если OneAgent настроен на инструментирование вашего Node.js-приложения и приём спанов OpenTelemetry.

Такие спаны пропускаются только OneAgent. Экспорт в сторонние системы (например, другие бэкенды или Collector) не затрагивается.

## Предотвращение дублирования спанов в PHP

OneAgent версии 1.313+

Чтобы избежать возможного дублирования спанов для областей, охваченных как OpenTelemetry, так и OneAgent, OneAgent пропускает спаны из следующих библиотек автоматического инструментирования PHP, если OneAgent настроен на инструментирование вашего PHP-приложения и приём спанов OpenTelemetry.

Такие спаны пропускаются только OneAgent. Экспорт в сторонние системы (например, другие бэкенды или Collector) не затрагивается.
