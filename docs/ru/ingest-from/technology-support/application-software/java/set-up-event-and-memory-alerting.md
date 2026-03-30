---
title: События и оповещения о нехватке памяти (OOM) и нехватке потоков (OOT)
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-03-06T21:29:46.503655
---

Чтобы настроить события нехватки памяти (OOM) и нехватки потоков (OOT) для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций, следуйте приведённым ниже инструкциям.

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Включить функцию OneAgent**](set-up-event-and-memory-alerting.md#enable-feature "Настройка событий и оповещений о нехватке памяти (OOM) и нехватке потоков (OOT) в Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Создать метрические события**](set-up-event-and-memory-alerting.md#create-metrics "Настройка событий и оповещений о нехватке памяти (OOM) и нехватке потоков (OOT) в Dynatrace.")

## Шаг 1: Включение функции OneAgent

Чтобы включить обнаружение событий нехватки памяти (OOM) и нехватки потоков (OOT):

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Найдите и включите **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Нажмите **Save changes**.

## Шаг 2: Настройка оповещений о высокой активности GC

Если вы уже настроили оповещения о высокой активности GC в вашей среде, оповещения автоматически создаются для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций.

Чтобы проверить настройку:

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Hosts**.
2. Убедитесь, что **Detect high GC activity** включено.

   Если вы используете настраиваемую конфигурацию для оповещений о длительном времени сборки мусора, обратите внимание, что для автономных/PaaS-сценариев и cloud-native Full-Stack инъекций данные, собранные с 10-секундными интервалами наблюдения, приводятся к одноминутным интервалам наблюдения.

Кроме того, можно создать оповещения только для конкретных метрических событий.

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Metric events**.
2. Нажмите **Add metric event**.
3. Определите следующие два события.
4. Нажмите **Save changes**.

## Связанные темы

* Метрические события
* Статические пороговые значения для мониторинга инфраструктуры
