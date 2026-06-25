---
title: Расширение OpenTelemetry Host Monitoring
source: https://docs.dynatrace.com/managed/observe/infrastructure-observability/extensions/opentelemetry-host-monitoring
scraped: 2026-05-12T12:15:04.282793
---

# OpenTelemetry Host Monitoring extension

# Расширение OpenTelemetry Host Monitoring

* Extension
* Updated on Mar 02, 2026

Создавайте топологию и экраны для данных хостов OpenTelemetry для ускоренного отображения и упрощённого анализа.

## Начало работы

### Обзор

Отслеживайте хосты с помощью OpenTelemetry, используя интегрированные визуализации метрик, топологию и оповещения. Расширение автоматически создаёт сущности для хостов и их запущенных процессов, представляя телеметрические данные через интуитивно понятные интерфейсы для быстрого анализа. Корреляция метрик, журналов и трассировок с сущностями хостов и процессов обеспечивает полный контекст и комплексное представление вашей инфраструктуры.

### Варианты использования

* Отслеживание производительности, работоспособности и доступности инфраструктуры, контролируемой OpenTelemetry.
* Анализ трендов и базовых показателей для планирования ёмкости.
* Создание оповещений о насыщении ресурсов, сетевых ошибках и других проблемах инфраструктуры.
* Специализированное, предварительно настроенное представление для мониторинга инфраструктуры.

### Требования

Данное расширение зависит от телеметрических данных, передаваемых в Dynatrace из OpenTelemetry через [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.").

## Активация и настройка

1. Развёртывание OpenTelemetry Collector.

   1. Следуйте инструкциям раздела [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector/deployment "How to deploy the Dynatrace OpenTelemetry Collector.") для развёртывания Collector.
   2. Используйте [эталонную конфигурацию](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml).
   3. Убедитесь, что Collector работает и телеметрические данные корректно передаются в Dynatrace.
2. Активируйте расширение OpenTelemetry Host Monitoring.

## Подробности

[OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") собирает телеметрические данные с вашей инфраструктуры и передаёт метрики в Dynatrace через OTel API.

Расширение отображает телеметрические данные, собранные OpenTelemetry Collector, и обеспечивает быстрый анализ и чёткое понимание данных, добавляя специфичный для Dynatrace контекст ко всем сигналам (метрикам, журналам и трассировкам).

Сведения об использовании расширения в Dynatrace см. в разделе [Monitor hosts that send OpenTelemetry data to Dynatrace](/managed/ingest-from/opentelemetry/collector/use-cases/host-monitoring "How to monitor your hosts that use Collectors to send OpenTelemetry data to Dynatrace.").

### Лицензирование и стоимость

Все принятые данные OpenTelemetry (журналы, метрики и трассировки) тарифицируются в соответствии с вашим тарифным планом — см. разделы [License Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.") или [Dynatrace classic licensing](/managed/license/monitoring-consumption-classic "Understand how Dynatrace monitoring consumption is calculated for classic licensing.").

Использование самого расширения не влечёт дополнительных затрат.

На основе наших измерений с использованием [эталонной конфигурации](https://github.com/Dynatrace/dynatrace-otel-collector/blob/main/config_examples/host-metrics.yaml) прогнозируются следующие объёмы приёма метрик:

* Около 4400 точек данных метрик на хост в час.
* Около 400 точек данных на процесс в час.

Оба значения зависят от набора доступных метрик. Подробнее см. в разделе [Ограничения](#limitations).

### Ограничения

* Метрика `system.processes.created` в настоящее время доступна только в операционных системах Linux и BSD.
* Метрика `process.disk.io` требует запуска Collector с привилегированным доступом. При его отсутствии метрика не будет собираться.

## Наборы функций

Данное расширение не включает наборы функций. Пользователи самостоятельно управляют тем, какие данные будут отправляться в Dynatrace, на основе конфигурации Collector.

[![Hub](https://dt-cdn.net/images/hub-512-82db3c583e.png "Hub")

### Исследовать в Dynatrace Hub

Создавайте топологию и экраны для данных хостов OpenTelemetry для ускоренного отображения и упрощённого анализа.](https://www.dynatrace.com/hub/detail/opentelemetry-host-monitoring-extension/)