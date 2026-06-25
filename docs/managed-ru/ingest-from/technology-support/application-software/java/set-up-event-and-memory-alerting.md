---
title: События и оповещения о нехватке памяти (OOM) и потоков (OOT)
source: https://docs.dynatrace.com/managed/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting
scraped: 2026-05-12T12:04:28.243185
---

# События и оповещения о нехватке памяти (OOM) и потоков (OOT)

# События и оповещения о нехватке памяти (OOM) и потоков (OOT)

* Чтение: 2 мин
* Обновлено 10 января 2024 г.

Чтобы настроить события out-of-memory (OOM) и out-of-threads (OOT) для standalone/PaaS-сценариев и cloud-native Full-Stack внедрений, выполните приведённые ниже инструкции.

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Включите функцию OneAgent**](/managed/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#enable-feature "Настройте события и оповещения о нехватке памяти (OOM) и потоков (OOT) в Dynatrace.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Создайте метрические события**](/managed/ingest-from/technology-support/application-software/java/set-up-event-and-memory-alerting#create-metrics "Настройте события и оповещения о нехватке памяти (OOM) и потоков (OOT) в Dynatrace.")

## Шаг 1. Включите функцию OneAgent

Чтобы включить обнаружение out-of-memory (OOM) и out-of-threads (OOT)

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Найдите и включите **Enable Out-Of-Memory and Out-Of-Thread Detection for Kubernetes and PaaS installations**.
3. Нажмите **Save changes**.

## Шаг 2. Настройте оповещения о высокой активности GC

Если в вашем окружении уже настроены оповещения о [высокой активности GC](/managed/observe/infrastructure-observability/hosts/configuration/anomaly-detection#hosts "Настройка обнаружения аномалий хоста, включая пороги проблем и событий."), для standalone/PaaS-сценариев и cloud-native Full-Stack внедрений оповещения создаются автоматически.

Чтобы проверить настройку

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Hosts**.
2. Убедитесь, что **Detect high GC activity** включено.

   Если используется собственная настройка для [оповещений о длительных временах сборки мусора](/managed/dynatrace-intelligence/root-cause-analysis/event-analysis-and-correlation/event-categories/resource-events#long-garbage-collection-time "Подробнее о ресурсных событиях и логике их формирования."), обратите внимание, что для standalone/PaaS-сценариев и cloud-native Full-Stack внедрений данные, собираемые с интервалом наблюдения 10 секунд, приводятся к одноминутному интервалу наблюдения.

Также можно создавать оповещения только для конкретных метрических событий.

1. Перейдите в **Settings** > **Anomaly detection** и выберите **Metric events**.
2. Нажмите **Add metric event**.
3. Задайте два следующих события.

   | Метрическое событие | Ключ метрики | Порог | Нарушающие выборки | Скользящее окно | Выборки для снятия оповещения |
   | --- | --- | --- | --- | --- | --- |
   | High GC suspension time | `builtin:tech.jvm.memory.gc.suspensionTime` | 25 % | 3 | 5 | 4 |
   | High GC total collection time | `builtin:tech.jvm.memory.gc.collectionTime` | 24 s | 3 | 5 | 4 |
4. Нажмите **Save changes**.

## Связанные темы

* [Метрические события](/managed/dynatrace-intelligence/anomaly-detection/metric-events "Узнайте о метрических событиях в Dynatrace")
* [Статические пороги для мониторинга инфраструктуры](/managed/dynatrace-intelligence/anomaly-detection/static-thresholds-infrastructure "Узнайте о фиксированных порогах, используемых Dynatrace для определения, когда обнаруженное замедление или рост частоты ошибок оправдывает создание нового события проблемы.")