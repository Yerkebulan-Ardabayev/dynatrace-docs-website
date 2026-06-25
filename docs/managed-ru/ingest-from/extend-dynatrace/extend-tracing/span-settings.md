---
title: Настройки spans
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-tracing/span-settings
scraped: 2026-05-12T11:37:59.140301
---

# Настройки spans

# Настройки spans

* 4-min read
* Updated on Mar 16, 2023

Dynatrace предоставляет гибкие настройки для управления захватом атрибутов spans и самих spans.

Все настройки находятся в **Settings > Server-side service monitoring**.

## Захват атрибутов (attribute capturing)

### Разрешение атрибутов

Настройте список атрибутов spans, которые Dynatrace будет сохранять:

1. Перейдите в **Settings > Server-side service monitoring > Span attribute capturing**.
2. Добавьте правила разрешения или блокировки атрибутов.

### Блокировка атрибутов

Атрибуты из блокировочного списка не будут захватываться, что позволяет защитить конфиденциальные данные.

### Маскировка атрибутов

Значения атрибутов можно маскировать для защиты персональных данных.

## Захват spans (span capturing rules)

Настройте правила, определяющие какие spans следует захватывать:

1. Перейдите в **Settings > Server-side service monitoring > Span capturing rules**.
2. Добавьте правила на основе имён spans, атрибутов или типов операций.

## Точки входа span (span entry points)

Точки входа определяют начало новой распределённой трассировки. Настройка позволяет управлять созданием новых PurePath.

## Контекстное распространение span (span context propagation)

Настройте форматы контекстного распространения:
* W3C TraceContext (рекомендуется)
* B3 (Zipkin)
* Dynatrace (DT)

## Связанные темы

* [Интеграция с OpenTracing](/managed/ingest-from/extend-dynatrace/extend-tracing/opentracing "Узнайте, как интегрировать OpenTracing с Dynatrace.")
* [OneAgent SDK](/managed/ingest-from/extend-dynatrace/extend-tracing/oneagent-sdk "OneAgent SDK для ручного инструментирования.")