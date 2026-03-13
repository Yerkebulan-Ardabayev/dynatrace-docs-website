---
title: Out-of-memory (OOM) and out-of-threads (OOT) events and alerting
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-03-06T21:29:46.503655
---

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

# Out-of-memory (OOM) and out-of-threads (OOT) events and alerting

* Latest Dynatrace
* 2-min read
* Updated on Jan 10, 2024

Чтобы настроить события нехватки памяти (OOM) и нехватки потоков (OOT) для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций, следуйте приведённым ниже инструкциям.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Включить функцию OneAgent**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#enable-feature "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создать метрические события**](/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#create-metrics "Set up out-of-memory (OOM) and out-of-threads (OOT) events and alerting in Dynatrace.")

## Шаг 1: Включение функции OneAgent

Чтобы включить обнаружение событий нехватки памяти (OOM) и нехватки потоков (OOT):

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Найдите и включите **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Нажмите **Save changes**.

## Шаг 2: Настройка оповещений о высокой активности GC

Если вы уже настроили оповещения о [высокой активности GC](/docs/observe/infrastructure-observability/hosts/configuration/anomaly-detection#hosts "Configure host anomaly detection, including problem and event thresholds.") в вашей среде, оповещения автоматически создаются для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций.

Чтобы проверить настройку:

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Hosts**.
2. Убедитесь, что **Detect high GC activity** включено.

   Если вы используете настраиваемую конфигурацию для [оповещений о длительном времени сборки мусора](/docs/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events#long-garbage-collection-time "Learn more about resource events and the logic behind raising them."), обратите внимание, что для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций данные, собранные с 10-секундными интервалами наблюдения, приводятся к одноминутным интервалам наблюдения.

Кроме того, можно создать оповещения только для конкретных метрических событий.

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Metric events**.
2. Нажмите **Add metric event**.
3. Определите следующие два события.
4. Нажмите **Save changes**.

## Связанные темы

* [Metric events](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace")
* [Static thresholds for infrastructure monitoring](/docs/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure "Learn about the fixed thresholds used by Dynatrace to determine when a detected slowdown or error-rate increase justifies the generation of a new problem event.")
