---
title: Включение OpenTelemetry Span Sensor для OneAgent
source: https://docs.dynatrace.com/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration
scraped: 2026-05-12T11:22:08.544944
---

# Включение OpenTelemetry Span Sensor для OneAgent

# Включение OpenTelemetry Span Sensor для OneAgent

* How-to guide
* 5-min read
* Updated on Feb 09, 2026

В дополнение к конфигурации на стороне приложения ряд специфичных для Dynatrace настроек позволяет контролировать использование данных OpenTelemetry в Dynatrace.

Чтобы узнать, как отправлять данные OpenTelemetry в Dynatrace OneAgent, смотрите [Использование OneAgent с данными OpenTelemetry](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.").

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
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3, 1.4 - 1.54, 1.55 - 1.60 |
| [OpenTracing](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

Поддерживается в [AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности AWS Lambda и варианты интеграции").

Чтобы включить OpenTelemetry Java:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (Java)**.

Существующие трейсеры будут заменены и перестанут работать после включения OpenTelemetry Java.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-go/) | 1.0 - 1.7, 1.8 - 1.11.0, 1.11.1 - 1.27, 1.28 - 1.43 |

Opt-in

Чтобы включить OpenTelemetry Go:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (Go) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для Go.

OneAgent версии 1.217 и более ранних: OpenTelemetry Go Sensor распространяет контекст Dynatrace между процессами только при включённой опции **Send W3C Trace Context HTTP headers**:

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Включите **Send W3C trace context HTTP headers**.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://www.npmjs.com/package/@opentelemetry/api) | 1 |

Opt-in

Чтобы включить OpenTelemetry Node.js:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

1. Найдите и включите **OpenTelemetry (Node.js) [Opt-In]**.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-php) | 1.0.0 |

Opt-in

Чтобы включить OpenTelemetry PHP:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (PHP) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для PHP.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

Чтобы включить OpenTelemetry .NET и .NET Core:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (.NET) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для .NET.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet) | 1.0.1+, 1.1+ |

Opt-in

Чтобы включить OpenTelemetry .NET Framework:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (.NET) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для .NET.

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-python) | 1.1+ |

Opt-in

Чтобы включить OpenTelemetry Python:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Найдите и включите **OpenTelemetry (Python) [Opt-In]**.

Существующие трейсеры не затрагиваются поддержкой OneAgent OpenTelemetry для Python.

## Редакция атрибутов

OpenTelemetry Span Sensor кодового модуля OneAgent автоматически захватывает все атрибуты OpenTelemetry. Чтобы предотвратить случайное сохранение персональных данных, можно исключить определённые ключи атрибутов, значения которых не должны сохраняться. Исключая атрибуты, содержащие персональные данные, вы можете выполнять требования конфиденциальности вашей организации и контролировать область хранимых данных мониторинга.

Чтобы настроить параметры хранения и маскировки атрибутов для вашего окружения:

1. Перейдите в **Settings** > **Preferences** > **OneAgent network modules & integrations**.

2. Выберите **Server-side service monitoring** > **Attribute capturing**.
3. Необязательно: чтобы изменить параметры сохранения атрибутов OpenTelemetry по умолчанию, перейдите в **Preferences**.

   * Чтобы хранить все атрибуты, кроме перечисленных в списке **Blocked attributes**, выберите **Allow all attributes**.
   * Чтобы блокировать все атрибуты, кроме перечисленных в списке **Allowed attributes**, выберите **Block all attributes**.

   Можно выбрать только один параметр.
4. Добавьте имя атрибута в список атрибутов.

   1. На странице **Attribute capturing** выберите **Blocked attributes** или **Allowed attributes**.

      Список разрешённых атрибутов: Dynatrace рекомендует включить несколько основных атрибутов, таких как `service.name` или `service.version`. Для удобства использования Dynatrace поставляется с конфигурацией по умолчанию, которую можно настроить.
   2. Выберите **Add item** для добавления нового ключа в список атрибутов и введите ключ.
   3. Выберите **Save changes**.
5. Для маскировки сохранённого значения атрибута выполните следующие действия.

   1. На странице **Attribute capturing** выберите **Attribute data masking**.
   2. Выберите **Add item** для добавления нового ключа в список маскируемых атрибутов.
   3. Введите ключ сохранённого значения и выберите параметр из раскрывающегося списка **Masking**. Подробнее о параметрах маскировки смотрите в разделе [Трассировки OpenTelemetry](/managed/manage/data-privacy-and-security/data-privacy/personal-data-captured-by-dynatrace#otel-traces "Узнайте, какие типы данных конечных пользователей могут быть захвачены во время мониторинга Dynatrace и какие методы доступны для маскировки персональных данных конечных пользователей.").
   4. Выберите **Save changes**.

Затем ключ атрибута можно найти на странице **Distributed traces** на [вкладке **Summary**](/managed/observe/application-observability/distributed-traces/use-cases/segment-request#summary-tab "Повысьте производительность распределённой системы, сегментируя запросы с медленным временем отклика через Service flow и анализируя их распределённые трассировки.").

## Ограничения поиска трассировок

### Атрибуты ресурсов

Поиск по атрибуту ресурса ограничен именем сервиса: фильтруйте по `Service name` на странице **Distributed traces**.

### Атрибуты span

Поиск по атрибуту span ограничен именем span: фильтруйте по `Request` на странице **Distributed traces**.

## Принцип работы Span Sensor

Дополнительные сведения об OpenTelemetry Span Sensor кодового модуля OneAgent смотрите в разделе [Обнаружение span OpenTelemetry с помощью OpenTelemetry Span Sensor кодового модуля OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor "Узнайте, как отправлять данные OpenTelemetry в Dynatrace OneAgent.").

### Точки входа

Во избежание возможных конфликтов с существующими распределёнными трассировками PurePath OneAgent по умолчанию принимает только span-ы с [типом span](https://opentelemetry.io/docs/concepts/signals/traces/#span-kind) `Server` или `Consumer`. Обычно это не является проблемой, поскольку библиотеки инструментирования, как правило, настраивают соответствующий тип span. Однако это следует учитывать, если ваше приложение полностью использует ручную инструментацию.

Это поведение можно настроить с помощью [правила точки входа](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-entry-points "Узнайте, как настраивать параметры span для OpenTelemetry и OpenTracing."). Для этого в Dynatrace перейдите в **Settings** > **Server-side service monitoring** > **Span entry points** и создайте новое правило с соответствующим действием и условием совпадения.

### Иерархия span

В зависимости от вашей конфигурации вы можете столкнуться с «плоским обогащением span». Это когда span-ы отображаются в Dynatrace в виде плоского списка вместо иерархии дерева. Хотя в целом это стандартное поведение при приёме OpenTelemetry трассировок OneAgent, иерархия всё же может отражать фактические связи между span-ами, как определено инструментацией, в зависимости от задействованных кодовых модулей OneAgent и их поддержки инструментированных технологий.

Листовые span-ы

При объединении span-ов OpenTelemetry с трассировками датчиков OneAgent убедитесь, что span-ы OpenTelemetry являются листовыми и не располагаются между span-ами OneAgent.

### Захват атрибутов

Поскольку OneAgent принимает span-ы уже в момент их создания, не все окончательные атрибуты могут быть присутствовать при первоначальном приёме. Атрибуты, добавленные позднее, выделяются в Dynatrace примечанием `initial value not set` и не могут использоваться для правил захвата span, поскольку они ещё не были доступны при оценке правил.

### Распространение контекста

При автоматическом приёме трассировок OpenTelemetry с помощью OneAgent Span Sensor существует разница в распространении контекста между трассировками OpenTelemetry и трассировками OneAgent.

Хотя распространение трассировок OpenTelemetry может быть уже корректно обработано вашим приложением, важно также согласовать их с трассировкой OneAgent. Это можно сделать с помощью [правила распространения контекста](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings#span-context-propagation "Узнайте, как настраивать параметры span для OpenTelemetry и OpenTracing."). Для настройки в Dynatrace перейдите в **Settings** > **Server-side service monitoring** > **Span context propagation** и создайте правило с действием `Propagate` и условием совпадения для нужного span (например, на основе имени span или библиотеки инструментирования).

Старайтесь избегать объединения трассировок для технологий, уже охваченных нативными датчиками OneAgent. Объединение таких span-ов OpenTelemetry с трассировкой OneAgent может привести к неопределённым состояниям.

## Экспорт в сторонние бэкенды при использовании OneAgent

Хотя трассировки OpenTelemetry всегда экспортируются в другие бэкенды как есть, при запуске инструментированным OneAgent приложением новой трассировки OpenTelemetry происходит небольшая корректировка данных. Это относится только к новым трассировкам, но не к случаям, когда трассировка продолжается через распространение контекста.

В этом случае OneAgent может уже создать новый объект трассировки при инициализации OpenTelemetry. Если эти две трассировки (с отдельными ID) не будут согласованы, телеметрические данные могут дублироваться или фрагментироваться. Для снижения этого риска при сохранении согласованности трассировок PurePath Dynatrace OneAgent использует следующий подход:

* ID трассировки OpenTelemetry имеет приоритет при экспорте в сторонние системы
* В бэкенде Dynatrace вместо него присваивается ID трассировки PurePath

Для обеспечения корреляции между этими двумя ID Dynatrace создаёт дополнительные [ссылки span](https://opentelemetry.io/docs/specs/otel/overview/#links-between-spans) для каждого span, ссылающиеся на трассировку OpenTelemetry.

Перезапись ID применяется только к новым трассировкам (не к распространению контекста) и к SDK OpenTelemetry для Go, Java, JavaScript, PHP и Python, но не для .NET.

## Ограничения

### Java

* OneAgent версии 1.294 и более ранних: OneAgent заменяет установленные глобальные компоненты OpenTelemetry SDK `TracerProvider`, `Propagator` и `ContextManager`. Поэтому при включённом OpenTelemetry Java трассировки больше не видны этим SDK и не экспортируются в бэкенды, такие как Jaeger.
* OneAgent версии 1.259+: во избежание дублирования OneAgent [игнорирует span-ы из некоторых библиотек автоматической инструментации](#java-span-dropping).
* При наличии датчиков OneAgent и OpenTelemetry для одной технологии возможны дополнительные накладные расходы.

### Go

* OneAgent может инструментировать только реализацию Tracer SDK OpenTelemetry по умолчанию.
* При наличии датчиков OneAgent и OpenTelemetry для одной технологии возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Дополнительные накладные расходы

### Node.js

* OneAgent версии 1.331+: во избежание дублирования OneAgent [игнорирует span-ы из некоторых библиотек автоматической инструментации](#nodejs-span-dropping).
* OneAgent версии 1.329 и более ранних: при инструментировании OneAgent и OpenTelemetry одного модуля (например, HTTP или GRPC) возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Разрыв распределённых трассировок
  + Дополнительные накладные расходы
* OneAgent версии 1.261 и более ранних: OneAgent заменяет установленные глобальные компоненты OpenTelemetry SDK `TracerProvider`, `Propagator` и `ContextManager`. Поэтому при включённом OpenTelemetry Node.js трассировки больше не видны этим SDK и не экспортируются в бэкенды, такие как Jaeger.

### PHP

* OneAgent версии 1.313+: во избежание дублирования OneAgent [игнорирует span-ы из некоторых библиотек автоматической инструментации](#php-span-dropping).

### Python

* При наличии датчиков OneAgent и OpenTelemetry для одной технологии возможны следующие ограничения:

  + Дублирование узлов в распределённых трассировках
  + Разрыв распределённых трассировок
  + Дополнительные накладные расходы

### Все языки

* OneAgent захватывает атрибуты ресурсов OpenTelemetry только при их передаче через переменные окружения `OTEL_SERVICE_NAME` и `OTEL_RESOURCE_ATTRIBUTES`. При использовании API приёма трассировок OpenTelemetry это ограничение не применяется.
* Нельзя создавать [атрибуты запросов](/managed/observe/application-observability/services/request-attributes "Узнайте, что такое атрибуты запросов, и научитесь использовать их на всех уровнях представлений анализа сервисов.") (обычно используемые для поиска и фильтрации трассировок) на основе атрибутов ресурсов OpenTelemetry.
* OneAgent усекает значения атрибутов, превышающие 4096 символов.

## Предотвращение дублирования span в Java

OneAgent версии 1.259+

Во избежание дублирования span для областей, охваченных OpenTelemetry и OneAgent, OneAgent пропускает span-ы из следующих библиотек автоматической инструментации Java, если OneAgent настроен на инструментирование вашего Java-приложения и приём span-ов OpenTelemetry.

Такие span-ы пропускаются только OneAgent. Экспорт в сторонние системы (например, другие бэкенды или Collector) не затрагивается.

> _Reference-таблица ниже на английском._

|  |  |  |
| --- | --- | --- |
| io.opentelemetry.akka-http-10.0 | io.opentelemetry.apache-dbcp-2.0 | io.opentelemetry.apache-httpasyncclient-4.1 |
| io.opentelemetry.apache-httpclient-2.0 | io.opentelemetry.apache-httpclient-4.0 | io.opentelemetry.apache-httpclient-4.3 |
| io.opentelemetry.apache-httpclient-5.0 | io.opentelemetry.async-http-client-1.9 | io.opentelemetry.async-http-client-2.0 |
| io.opentelemetry.c3p0-0.9 | io.opentelemetry.cassandra-3.0 | io.opentelemetry.cassandra-4.0 |
| io.opentelemetry.cassandra-4.4 | io.opentelemetry.cxf-jaxrs-3.2 | io.opentelemetry.google-http-client-1.19 |
| io.opentelemetry.grpc-1.6 | io.opentelemetry.http-url-connection | io.opentelemetry.java-http-client |
| io.opentelemetry.jaxrs-1.0 | io.opentelemetry.jaxrs-1.0-common | io.opentelemetry.jaxrs-2.0-annotations |
| io.opentelemetry.jaxrs-2.0-common | io.opentelemetry.jaxrs-2.0-cxf-3.2 | io.opentelemetry.jaxrs-2.0-jersey-2.0 |
| io.opentelemetry.jaxrs-2.0-resteasy-3.0 | io.opentelemetry.jaxrs-2.0-resteasy-3.1 | io.opentelemetry.jaxrs-3.0-annotations |
| io.opentelemetry.jaxrs-3.0-jersey-3.0 | io.opentelemetry.jaxrs-3.0-resteasy-6.0 | io.opentelemetry.jaxrs-annotations-2.0 |
| io.opentelemetry.jaxrs-annotations-3.0 | io.opentelemetry.jaxrs-client-1.1 | io.opentelemetry.jaxrs-client-2.0 |
| io.opentelemetry.jaxrs-client-2.0-resteasy-3.0 | io.opentelemetry.jaxws-2.0 | io.opentelemetry.jaxws-2.0-axis2-1.6 |
| io.opentelemetry.jaxws-2.0-cxf-3.0 | io.opentelemetry.jaxws-2.0-metro-2.2 | io.opentelemetry.jaxws-cxf-3.0 |
| io.opentelemetry.jaxws-common | io.opentelemetry.jaxws-jws-api-1.1 | io.opentelemetry.jdbc |
| io.opentelemetry.jedis-1.4 | io.opentelemetry.jedis-3.0 | io.opentelemetry.jedis-4.0 |
| io.opentelemetry.jersey-2.0 | io.opentelemetry.jetty-11.0 | io.opentelemetry.jetty-8.0 |
| io.opentelemetry.jetty-httpclient-9.2 | io.opentelemetry.jms-1.1 | io.opentelemetry.jms-3.0 |
| io.opentelemetry.jsp-2.3 | io.opentelemetry.kafka-clients | io.opentelemetry.kafka-clients-0.11 |
| io.opentelemetry.kafka-clients-2.6 | io.opentelemetry.kafka-streams-0.11 | io.opentelemetry.lettuce-5.1 |
| io.opentelemetry.liberty | io.opentelemetry.liberty-20.0 | io.opentelemetry.mongo-3.1 |
| io.opentelemetry.netty-3.8 | io.opentelemetry.netty-4.0 | io.opentelemetry.netty-4.1 |
| io.opentelemetry.okhttp-2.2 | io.opentelemetry.okhttp-3.0 | io.opentelemetry.orcale-ucp-11.2 |
| io.opentelemetry.rabbitmq-2.7 | io.opentelemetry.reactor-kafka-1.0 | io.opentelemetry.reactor-netty-1.0 |
| io.opentelemetry.resteasy-3.0 | io.opentelemetry.resteasy-3.1 | io.opentelemetry.resteasy-6.0 |
| io.opentelemetry.rmi | io.opentelemetry.servlet-2.2 | io.opentelemetry.servlet-3.0 |
| io.opentelemetry.servlet-5.0 | io.opentelemetry.servlet-javax-common | io.opentelemetry.spring-jms-2.0 |
| io.opentelemetry.spring-jms-6.0 | io.opentelemetry.spring-kafka-2.7 | io.opentelemetry.spring-rabbit-1.0 |
| io.opentelemetry.spring-rmi-4.0 | io.opentelemetry.spring-webflux-5.0 | io.opentelemetry.spring-webflux-5.3 |
| io.opentelemetry.spring-ws-2.0 | io.opentelemetry.tomcat-10.0 | io.opentelemetry.tomcat-7.0 |
| io.opentelemetry.tomcat-jdbc | io.opentelemetry.undertow-1.4 | io.opentelemetry.vibur-dbcp-11.0 |

## Предотвращение дублирования span в Node.js

OneAgent версии 1.331+

Во избежание дублирования span для областей, охваченных OpenTelemetry и OneAgent, OneAgent пропускает span-ы из следующих библиотек автоматической инструментации Node.js, если OneAgent настроен на инструментирование вашего Node.js-приложения и приём span-ов OpenTelemetry.

Такие span-ы пропускаются только OneAgent. Экспорт в сторонние системы не затрагивается.

|  |  |
| --- | --- |
| @opentelemetry/instrumentation-http | @opentelemetry/instrumentation-undici |
| @opentelemetry/instrumentation-aws-sdk | @opentelemetry/instrumentation-aws-lambda |
| @opentelemetry/instrumentation-connect | @opentelemetry/instrumentation-graphql |
| @opentelemetry/instrumentation-grpc | @opentelemetry/instrumentation-ioredis |
| @opentelemetry/instrumentation-redis | @opentelemetry/instrumentation-kafkajs |
| @opentelemetry/instrumentation-memcached | @opentelemetry/instrumentation-mongodb |
| @opentelemetry/instrumentation-tedious | @opentelemetry/instrumentation-mysql |
| @opentelemetry/instrumentation-mysql2 | @opentelemetry/instrumentation-oracledb |
| @opentelemetry/instrumentation-pg | @opentelemetry/instrumentation-amqplib |

## Предотвращение дублирования span в PHP

OneAgent версии 1.313+

Во избежание дублирования span для областей, охваченных OpenTelemetry и OneAgent, OneAgent пропускает span-ы из следующих библиотек автоматической инструментации PHP, если OneAgent настроен на инструментирование вашего PHP-приложения и приём span-ов OpenTelemetry.

Такие span-ы пропускаются только OneAgent. Экспорт в сторонние системы не затрагивается.

|  |  |
| --- | --- |
| io.opentelemetry.contrib.php.curl | io.opentelemetry.contrib.php.laravel |
| io.opentelemetry.contrib.php.mongodb | io.opentelemetry.contrib.php.mysqli |
| io.opentelemetry.contrib.php.pdo | io.opentelemetry.contrib.php.slim |
| io.opentelemetry.contrib.php.symfony | io.opentelemetry.contrib.php.wordpress |