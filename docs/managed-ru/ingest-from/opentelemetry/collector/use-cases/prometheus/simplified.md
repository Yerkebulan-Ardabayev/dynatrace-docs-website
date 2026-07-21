---
title: Сбор метрик Prometheus с помощью OTel Collector (упрощённый вариант)
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified
---

# Сбор метрик Prometheus с помощью OTel Collector (упрощённый вариант)

# Сбор метрик Prometheus с помощью OTel Collector (упрощённый вариант)

* Практическое руководство
* 4 минуты на чтение
* Обновлено 19 июня 2026 г.

На этой странице описано, как настроить OpenTelemetry Collector для сбора метрик с эндпоинтов Prometheus и пересылки полученных метрик в Dynatrace.
Раздел посвящён упрощённой настройке для случаев, когда набор эндпоинтов статичен или прост и не требуется автомасштабирование или резервирование.

## Когда использовать этот подход

Использовать единый Collector, если применим один или несколько из следующих сценариев.

* Сбор данных с небольшого или умеренного числа эндпоинтов (до нескольких десятков).
* Список целей в основном статичен или формируется простым service discovery (`static_configs`, одно пространство имён Kubernetes, обнаружение на основе файлов).
* Одного экземпляра Collector достаточно по ресурсам CPU и памяти для ожидаемой нагрузки.

Рано или поздно ресурсов одного Collector перестаёт хватать.
Если стандартная архитектура пока не нужна, можно запустить несколько независимых упрощённых Collector'ов, каждый из которых собирает данные со своего набора целей (например, по одному на пространство имён или команду).
При этом цели нужно распределять самостоятельно, и общего автомасштабирования не будет.

## Когда переходить на стандартное развёртывание

Переходить на [стандартное развёртывание](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.") со стандартной архитектурой с использованием Target Allocator, если наблюдается один или несколько следующих признаков.

* Потолок пропускной способности: Collector не справляется с объёмом собираемых данных даже после увеличения CPU и памяти.
* Длительность сбора приближается к интервалу сбора: сбор данных занимает почти столько же времени, сколько сам интервал, поэтому Collector не может гарантированно завершить один цикл до начала следующего.
* Срабатывает `memory_limiter` или под завершается по OOM: Collector регулярно упирается в лимит памяти и теряет данные или перезапускается.
* Число целей превышает возможности ручного распределения: целей больше, чем может обработать один Collector, а разделение их между несколькими независимыми Collector'ами превратилось в обременительную рутину.
* Требуется автомасштабирование или резервирование: единый Collector представляет собой единую точку отказа и не может масштабироваться горизонтально с ростом нагрузки.

Стандартное развёртывание добавляет автоматическое обнаружение целей через Prometheus Operator CRD, горизонтальное автомасштабирование и резервирование в пулах scraper и gateway.

При переходе нужно преобразовать статические `scrape_configs` в CRD `ServiceMonitor` или `PodMonitor`; см. [Миграция с единого Collector](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard#migrate "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.").

## Предварительные требования

Этот сценарий использования предполагает наличие следующего:

* Цель сбора Prometheus, открывающая порт `8888`.
* Один из следующих дистрибутивов Collector с [приёмником Prometheus﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/receiver/prometheusreceiver), [процессором metric start time﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/metricstarttimeprocessor) и [процессором cumulative-to-delta﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor):

  + [Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector#dt-collector-dist "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + OpenTelemetry [Contrib](/managed/ingest-from/opentelemetry/collector#collector-contrib "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
  + [Пользовательская версия Builder](/managed/ingest-from/opentelemetry/collector#collector-builder "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.")
* [URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), в который нужно экспортировать данные.
* [Токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") с соответствующей областью доступа (требуется только для SaaS и ActiveGate).

О том, как настроить Collector с приведённой ниже конфигурацией, см. в разделах [Развёртывание Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") и [Настройка Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Расчёт ресурсов

Для Collector'ов, развёрнутых как поды в Kubernetes, рекомендуются следующие лимиты ресурсов для приёма до 1 миллиона точек данных в минуту (DPM). Для приёма большего объёма данных стоит рассмотреть [стандартную модель развёртывания](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Deploy a tiered Target Allocator, Scraper, and Gateway architecture for production-grade Prometheus scraping with the OpenTelemetry Collector.").

* CPU: 2 ядра
* Память: 8 ГиБ

Эти значения предполагают, что Collector настроен согласно [демонстрационной конфигурации](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/simplified#demo-configuration "Configure a single OpenTelemetry Collector to scrape Prometheus endpoints for small and medium-scale workloads."), которая включает приёмник `prometheus`, процессоры `metric_start_time` и `cumulativetodelta`, а также экспортёр `otlp_http`.
Дополнительные процессоры увеличат эти требования.

## Демонстрационная конфигурация

Эта конфигурация требует Dynatrace Collector версии 0.41.0 или новее. В примере конвейера ниже используется [процессор `metric_start_time`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/metricstarttimeprocessor), который добавляет метрикам временные метки начала, и [процессор `cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor), который преобразует метрики в дельта-темпоральность.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: 'node-exporter'



scrape_interval: 60s



static_configs:



- targets: ['prometheus-prometheus-node-exporter:9100']



- job_name: opentelemetry-collector



scrape_interval: 60s



static_configs:



- targets:



- 127.0.0.1:8888



processors:



metric_start_time:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [prometheus]



processors: [metric_start_time, cumulativetodelta]



exporters: [otlp_http]
```

Проверка конфигурации

[Проверьте свои настройки](/managed/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector."), чтобы избежать проблем с конфигурацией.

Рекомендация по процессору cumulativetodelta

Рекомендуется устанавливать параметр `max_staleness` [процессора cumulativetodelta﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) на значение выше, чем частота получения метрик Collector'ом (например, как часто поступают метрики через OTLP или насколько велик интервал сбора Prometheus). Это гарантирует, что ссылки на заброшенные потоки метрик не будут со временем накапливаться в памяти.

## Компоненты

В нашей конфигурации настроены следующие компоненты.

### Receivers

В разделе `receivers` указан приёмник `prometheus` как активный компонент-приёмник для нашего экземпляра Collector. Приёмник настроен с двумя заданиями, `node-exporter` и `opentelemetry-collector`, в разделе `scrape_configs`, для получения данных с указанных хостов раз в минуту (`scrape_interval: 60s`).

Полный список параметров конфигурации см. в [документации Prometheus﻿](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

В разделе `processors` указан [процессор `cumulativetodelta`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/cumulativetodeltaprocessor) для преобразования метрик, поступающих от приёмника Prometheus, в [формат дельта-агрегации](/managed/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector.").

В Dynatrace Collector версии 0.41.0+ указан
[процессор
`metric_start_time`﻿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.156.0/processor/metricstarttimeprocessor)
для добавления меток времени начала к метрикам. Это необходимо для корректного преобразования метрик в дельта-темпоральность.

### Exporters

В разделе `exporters` указывается стандартный экспортер [`otlp_http`﻿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.156.0/exporter/otlphttpexporter), для которого настраивается URL Dynatrace API и необходимый токен аутентификации.

Для этого задаются две следующие переменные окружения, на которые делается ссылка в значениях конфигурации `endpoint` и `Authorization`.

* `DT_ENDPOINT` содержит [базовый URL эндпоинта Dynatrace API](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте больше об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") (например, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` содержит [токен API](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте больше об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.")

### Пайплайн службы

В разделе `service` объекты receiver, processor и exporter собираются в пайплайн метрик, который выполняет задания Prometheus, преобразует их метрики в дельта-значения и передаёт данные в Dynatrace.

## Ограничения

Метрики передаются с помощью протокола OpenTelemetry (OTLP) через [Dynatrace OTLP API](/managed/ingest-from/opentelemetry/otlp-api "Узнайте больше об эндпоинтах OTLP API, которые приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и подпадают под лимиты и ограничения API.
Подробнее см.:

* [Ограничения метрик OpenTelemetry](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения при этом действуют.")
* [Сопоставление метрик Dynatrace](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения при этом действуют.")

Чтобы избежать дублирования данных, нужно убедиться, что заданную цель (например, брокер Kafka или эндпоинт Prometheus) опрашивает только один OTel Collector.

При использовании нескольких реплик OTel Collector нужно настроить каждую из них на свою цель. Это предотвращает дублирование метрик и лишние затраты на приём данных.

[Target Allocator](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Разверните многоуровневую архитектуру Target Allocator, Scraper и Gateway для промышленного сбора метрик Prometheus с помощью OpenTelemetry Collector.") автоматически распределяет цели Prometheus между пулом OTel Collector.

## Похожие темы

* [Сбор метрик Prometheus с помощью OTel Collector (стандартный вариант)](/managed/ingest-from/opentelemetry/collector/use-cases/prometheus/standard "Разверните многоуровневую архитектуру Target Allocator, Scraper и Gateway для промышленного сбора метрик Prometheus с помощью OpenTelemetry Collector.")
* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.")
* [Обогащение запросов OTLP данными Kubernetes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes.")
* [Источник данных Prometheus](/managed/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Узнайте, как создать расширение Prometheus с помощью фреймворка Extensions.")