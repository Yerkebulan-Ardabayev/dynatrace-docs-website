---
title: Интеграция с OpenTracing
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing
scraped: 2026-05-12T11:37:59.140301
---

# Интеграция с OpenTracing

# Интеграция с OpenTracing

* 4-min read
* Updated on Mar 16, 2023

OpenTracing позволяет инструментировать приложения для распределённой трассировки с использованием стандартного API.

## Предварительные условия

| Требование | Описание |
| --- | --- |
| OneAgent | Версия 1.158+ |
| Поддерживаемые языки | Java, .NET, Node.js |
| Конфигурация | Включение в **Settings > Server-side service monitoring** |

## Включение через настройки

Перейдите в **Settings > Server-side service monitoring > OpenTracing and OpenTelemetry** и включите поддержку OpenTracing.

## Создание spans в Java

```java
import io.opentracing.Tracer;
import io.opentracing.util.GlobalTracer;

Tracer tracer = GlobalTracer.get();

try (Scope scope = tracer.buildSpan("my-operation").startActive(true)) {
    // выполнение операции
}
```

## Ограничения

* Spans OpenTracing отображаются в трейсах Dynatrace как дополнительные узлы.
* Некоторые функции Dynatrace (например, Davis AI-анализ) могут работать с ограничениями для spans OpenTracing.

## Поддерживаемые технологии

* Hazelcast
* Couchbase

## Связанные темы

* [Настройки spans](/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings "Настройка захвата атрибутов и spans.")
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "OneAgent SDK для ручного инструментирования.")