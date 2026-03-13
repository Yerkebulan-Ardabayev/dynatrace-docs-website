---
title: OpenTracing
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing
scraped: 2026-03-06T21:16:20.837739
---

# OpenTracing

# OpenTracing

* Latest Dynatrace
* 2-min read
* Updated on Sep 23, 2022

Early Adopter

OpenTracing — это проект с открытым исходным кодом, предоставляющий API и инструментарий для распределённой трассировки. Хотя OpenTracing и OpenCensus объединились в 2019 году и образовали OpenTelemetry, инструментарий OpenTracing по-прежнему используется многими популярными фреймворками, библиотеками и проектами.

Dynatrace OneAgent для Java автоматически собирает данные спанов OpenTracing и интегрирует их в сквозные распределённые трассировки PurePath.
OpenTracing с OneAgent позволяет вам:

* Получать информацию о сторонних Java-библиотеках или фреймворках, которые не поддерживаются OneAgent нативно, но содержат предварительно встроенный инструментарий OpenTracing.
* Обогащать данные мониторинга дополнениями, специфичными для проекта (например, пользовательский инструментарий, добавляющий бизнес-данные, или сбор диагностических точек, специфичных для разработчиков).
* Связывать независимые, не связанные транзакции для расширения сквозных распределённых трассировок (например, добавляя вендоро-нейтральный пользовательский инструментарий для получения сквозных транзакционных данных, специфичных для бизнес-процессов или предметной области).

![Поддержка OpenTracing в OneAgent](https://dt-cdn.net/images/oneagent-opentracing-support-2596-85407ecec3.png)

Качество спанов OpenTracing, захваченных OneAgent, зависит от качества инструментария, предоставленного сторонней библиотекой.

## Предварительные требования

| Фреймворк мониторинга | Версии |
| --- | --- |
| [OpenTelemetry](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracing](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Поддерживается в [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "Возможности и варианты интеграции AWS Lambda").

## Включение интеграции OpenTracing

Чтобы включить поддержку захвата данных спанов

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Отфильтруйте по **OpenTracing**.
3. Вы можете настроить OneAgent для:

   * Автоматической регистрации Dynatrace в качестве `GlobalTracer`, тем самым переопределяя другие трассировщики, зарегистрированные в приложении. Выберите эту настройку, только если вы уверены, что хотите переопределить другие трассировщики (например, Jaeger) в вашей системе трассировки.
   * Автоматической регистрации Dynatrace в качестве `GlobalTracer`, когда в приложении не зарегистрирован другой трассировщик. Используйте это, если вы не хотите вмешиваться в работу других трассировщиков в вашей системе трассировки.
4. В коде вашего приложения используйте возвращаемое значение `GlobalTracer.get()` для создания спанов.
   Следующий пример показывает, как вручную создавать спаны с помощью OpenTracing:

   ```
   // Make sure to use the correct Tracer.



   Tracer tracer = GlobalTracer.get();



   SpanBuilder spanBuilder = tracer.buildSpan("hello");



   spanBuilder.withTag("foo", "bar");



   Span span = spanBuilder.start();



   // Make sure to close every created Scope.



   // It is recommended to use a try-with-resource statement for that.



   try (Scope scope = tracer.activateSpan(span)) {



   // Do actual operation.



   } finally {



   // Make sure to finish every started Span.



   span.finish();



   }
   ```

   Следующий пример показывает, как использовать существующую библиотеку инструментария для создания спанов с помощью OpenTracing:

   ```
   HazelcastInstance untraced = HazelcastClient.newHazelcastClient();



   // This operation will not be visible in Dynatrace.



   untraced.getMap("map").put("key", "value");



   // TracingHazelcastInstance implements the same interface (HazelcastInstance)



   // but automatially creates span for every operation.



   // It internally calls GlobalTracer.get().



   // Available as a separate instrumentation scope/library:



   // https://github.com/opentracing-contrib/java-hazelcast



   HazelcastInstance traced = new TracingHazelcastInstance(



   HazelcastClient.newHazelcastClient(),



   false // traceWithActiveSpanOnly



   );



   // This operation will be visible in Dynatrace.



   traced.getMap("map").put("key", "value");
   ```

См. [Настройки спанов](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Узнайте, как настраивать параметры спанов для OpenTelemetry и OpenTracing.") для всех параметров конфигурации.

## Ограничения

* [Сервис спанов по умолчанию](/docs/observe/application-observability/services/service-detection/service-detection-v1#span-service "Узнайте, как Dynatrace Service Detection v1 обнаруживает и именует различные типы сервисов.")
* Когда инструментарий OneAgent и OpenTracing присутствуют одновременно для одной и той же технологии (например, входящие веб-запросы через Servlet API), вы можете столкнуться со следующими ограничениями:

  + Дублирование узлов в распределённых трассировках PurePath
  + Дополнительные накладные расходы
  + Для JDBC такое двойное инструментирование может нарушить обнаружение сервисов
    Будьте особенно осторожны при включении поддержки OpenTracing Java в OneAgent для [поддерживаемых технологий](/docs/ingest-from/technology-support#java "Технические подробности поддержки Dynatrace для конкретных платформ и фреймворков разработки."), поддерживаемых OneAgent «из коробки».
* Интеграция трассировок из инструментария OpenTracing для Spring Framework в настоящее время не поддерживается.
* Java-сенсор OpenTracing не захватывает атрибуты типа `array`.

## Поддерживаемые технологии

Dynatrace интегрирует трассировки из любого инструментария OpenTracing. Мы успешно протестировали инструментирование следующих библиотек и фреймворков:

* Hazelcast для OpenTracing Java
* Couchbase начиная с [java-client версии 3.1.3](https://github.com/couchbase/couchbase-jvm-clients) для OpenTracing Java
