---
title: Унифицированные сервисы
source: https://www.dynatrace.com/docs/observe/application-observability/services/service-detection/service-detection-v1/service-types/unified-service
scraped: 2026-03-05T21:34:37.084360
---

# Унифицированные сервисы

# Унифицированные сервисы

* Classic
* How-to guide
* 6-min read
* Updated on Oct 13, 2025

Dynatrace version 1.274

## Обзор

Тип **Unified service** представляет сервисы, обнаруженные с помощью правил Service Detection v2 (SDv2) на основе атрибутов ресурсов.
Эти сервисы впервые были представлены для OpenTelemetry и теперь внедряются для OneAgent в публичном предварительном просмотре (осень 2025 г.).

Сервисы, использующие обнаружение SDv2, отображают **Unified service** как тип сервиса в свойствах веб-интерфейса, что указывает на применение правил обнаружения SDv2.

Ключевые возможности:

* Метрики времени отклика, пропускной способности и процента ошибок
* Автоматическое обнаружение и мониторинг конечных точек

Термин «унифицированные сервисы» был введён ещё до появления SDv2. Правила обнаружения сервисов, конечных точек, сбоев и разделения были введены одновременно, однако изначально были жёстко запрограммированы. SDv2 делает эти правила настраиваемыми. Хотя в свойствах по-прежнему отображается **Unified service**, SDv2 ориентирован на правила обнаружения, а не на типы сервисов.

Метрики Grail `dt.service.request.response_time`, `dt.service.request.failure_count` и `dt.service.request.count` тарифицируются. Подробнее см. в разделе [Метрики на основе Grail (DPS)](../../../../../../license/capabilities/metrics.md "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

Сведения о текущих правилах обнаружения и параметрах настройки см. в разделе [Service Detection v2](../../service-detection-v2.md "Find out how to detect, name, and split services from OpenTelemetry and OneAgent spans.").

## Устаревший span:service

Устаревшие **span:services** были автоматически перенесены в SDv2 (**Unified service**) к 1 октября 2025 г.

Это касается только **span:services** (сервисов, принятых через OTLP API), но не **span (default) services**, обнаруженных OneAgent с датчиком OpenTelemetry, которые останутся без изменений.

Подробнее см. в записи [Обзор Service Detection V2 (SDv2)ï»¿](https://dt-url.net/b4030ff) в сообществе Dynatrace.
