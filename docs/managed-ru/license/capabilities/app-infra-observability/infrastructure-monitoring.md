---
title: Расчёт потребления Infrastructure Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/infrastructure-monitoring
scraped: 2026-05-12T11:13:43.319125
---

# Расчёт потребления Infrastructure Monitoring (DPS)

# Расчёт потребления Infrastructure Monitoring (DPS)

* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace OneAgent можно настроить в режиме Infrastructure Monitoring, который обеспечивает комплексный мониторинг хостов для физических и виртуальных серверов.

В дополнение ко всем функциям [Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Learn how your consumption of the Dynatrace Foundation & Discovery DPS capability is billed and charged."), Infrastructure Monitoring также включает детальные метрики производительности процессов, метрики производительности дисков, анализ сети между процессами и анализ памяти по процессам.
На хостах в режиме Infrastructure Monitoring можно включать расширения Dynatrace Extensions, которые могут потреблять [точки данных пользовательских метрик](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring#infra-metrics "Learn how your consumption of the Dynatrace Infrastructure Monitoring DPS capability is billed and charged.").

### Хост-часы

Единица измерения для расчёта потребления мониторинга хостов в режиме Infrastructure Monitoring — хост-час.
Каждый экземпляр Dynatrace OneAgent, установленный и запущенный на экземпляре операционной системы (например, на физической или виртуальной машине) с включённым режимом Infrastructure Monitoring, потребляет хост-часы.
Чем дольше мониторируется хост, тем больше хост-часов потребляется.
Потребление не зависит от объёма памяти хоста.

### Детализация тарификации потребления хост-часов

Dynatrace создан для динамичных облачных сред, где хосты и сервисы быстро запускаются и уничтожаются.
Поэтому детализация тарификации потребления хост-часов рассчитывается в 15-минутных интервалах.
Если хост отслеживается менее 15 минут в интервале, потребление хост-часов округляется до 15 минут перед расчётом.

На рисунке ниже показан расчёт потребления хост-часов на хост в 15-минутных интервалах.

![Infrastructure Monitoring consumption](https://dt-cdn.net/images/infrastructure-monitoring-consumption-5843-2c70d0f91c.jpg)

Потребление Infrastructure Monitoring

### Метрики

Этот раздел предполагает, что вы следовали рекомендуемым Dynatrace вариантам развёртывания.
При реализации пользовательского развёртывания тарификация включённых метрик может работать так, как описано, — но это не гарантируется Dynatrace.

Dynatrace Infrastructure Monitoring включает метрики Infrastructure Monitoring и [другие встроенные метрики](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Explore the complete list of built-in Dynatrace metrics.").
Эти метрики включены и никогда не тарифицируются.

Infrastructure Monitoring также включает определённый объём точек данных пользовательских метрик.
Каждый хост добавляет 1 500 точек данных пользовательских метрик в каждом 15-минутном интервале.
Включённые точки данных метрик, не использованные в 15-минутном интервале предоставления, не переносятся на последующие интервалы.
Включённые точки данных метрик окружения автоматически применяются к метрикам, происходящим с хостов, мониторируемых OneAgent в режиме Infrastructure Monitoring.
Это применяется к пользовательским метрикам, как описано в таблице ниже.

Точки данных пользовательских метрик, превышающие включённый объём, тарифицируются как [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

| Источник | Примеры (включая, но не ограничиваясь) |
| --- | --- |
| Хост с Infrastructure Monitoring, отправляющий данные через [OneAgent metric API](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.") | * OpenTelemetry метрики * Spring Micrometer * StatsD * JMX * Расширения, запущенные локально на хосте OneAgent * локальный на хосте Telegraf |
| Узел Kubernetes с Infrastructure Monitoring | * OpenTelemetry метрики * Spring Micrometer * JMX * [Метрики Prometheus через ActiveGate](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Metric ingestion from Prometheus endpoints in Kubernetes, metrics alerts, and monitoring consumption.") * Не включает метрики, отправленные через Dynatrace Collector или OpenTelemetry Collector. |

На основе Рисунка 2 выше приведён включённый объём точек данных пользовательских метрик для четырёх 15-минутных интервалов.

### Пример расчёта включённых точек данных пользовательских метрик

* Первый 15-минутный интервал: `1 (мониторируемый хост) × 1 500 (точки данных) = 1 500 включённых точек данных`
* Второй 15-минутный интервал: `2 (мониторируемых хоста) × 1 500 (точки данных) = 3 000 включённых точек данных`
* Третий 15-минутный интервал: `1 (мониторируемый хост) × 1 500 (точки данных) = 1 500 включённых точек данных`
* Четвёртый 15-минутный интервал: `1 (мониторируемый хост) × 1 500 (точки данных) = 1 500 включённых точек данных`

### Как потребляются точки данных пользовательских метрик в режиме Infrastructure Monitoring

Потребление точек данных пользовательских метрик может принимать различные формы.
Одинаковое число точек данных может потребляться:

* Несколькими метриками с высоким разрешением или многочисленными метриками с низким разрешением.
* Равномерно в нескольких 15-минутных интервалах или всё сразу за одну минуту.
* Всеми хостами с Infrastructure Monitoring, частью хостов или одним хостом.

## Детали потребления: Infrastructure Monitoring

Dynatrace предоставляет встроенные метрики использования, помогающие понять и анализировать потребление Infrastructure Monitoring в вашей организации.
Чтобы использовать эти метрики, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и в Account Management (**Usage summary** > **Infrastructure Monitoring** > **Actions** > **View details**).

Ниже перечислены метрики для мониторинга деталей потребления Infrastructure Monitoring.

(DPS) Infrastructure Monitoring billing usage
:   Ключ: `builtin:billing.infrastructure_monitoring.usage`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Общее число хост-часов, потреблённых в режиме Infrastructure Monitoring.

(DPS) Infrastructure Monitoring billing usage per host
:   Ключ: `builtin:billing.infrastructure_monitoring.usage_per_host`

    Измерение: Хост (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Потреблённые хост-часы в режиме Infrastructure Monitoring на хост.

(DPS) Total metric data points reported by Infrastructure hosts
:   Ключ: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Число точек данных метрик, потреблённых всеми хостами с Infrastructure Monitoring.

(DPS) Metric data points reported and split by Infrastructure hosts
:   Ключ: `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host`

    Измерение: Хост (`dt.entity.host`)

    Разрешение: 15 мин

    Описание: Число точек данных метрик с разбивкой по хостам с Infrastructure Monitoring.

(DPS) Available included metric data points for Infrastructure-monitored hosts
:   Ключ: `builtin:billing.infrastructure_monitoring.metric_data_points.included`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Общее число включённых точек данных метрик, вычитаемых из точек данных, зафиксированных всеми хостами с Infrastructure Monitoring.

(DPS) Consumed included metric data points for Infrastructure hosts
:   Ключ: `builtin:billing.infrastructure_monitoring.metric_data_points.included_used`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Число использованных включённых точек данных метрик хостов с Infrastructure Monitoring.

(DPS) Total metric data points billed for Infrastructure hosts
:   Ключ: `builtin:billing.custom_metrics_classic.usage.infrastructure_hosts`

    Измерение: Count

    Разрешение: 15 мин

    Описание: Число тарифицируемых точек данных метрик для всех хостов с Infrastructure Monitoring.

### Мониторинг потребления хост-часов

Вы можете отслеживать суммарное потребление хост-часов для различных интервалов (15 мин, час, день или неделя) и любого выбранного временного диапазона, используя метрику «(DPS) Infrastructure Monitoring billing usage».
В примере ниже показано, что 5 хостов мониторировались, и общее потребление составило 5 хост-часов за каждый час.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image011-1099-50bac22dd0.png)

Infrastructure Monitoring (DPS)

Можно детализировать суммарное потребление хост-часов с помощью метрики «(DPS) Infrastructure Monitoring billing usage per host».
В примере ниже показан список всех хостов, зафиксировавших потребление.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image013-1099-cb1470f609.png)

Infrastructure Monitoring (DPS)

### Мониторинг потребления метрик для хостов с Infrastructure Monitoring

Используйте метрику «(DPS) Total metric data points billed for Infrastructure hosts» для мониторинга числа тарифицируемых точек данных метрик хостов с Infrastructure Monitoring, как показано в примере ниже.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image015-1101-5c4b7620a4.png)

Infrastructure Monitoring (DPS)

Для управления бюджетом метрик можно сравнивать число доступных включённых точек данных с общим числом потреблённых точек данных, используя метрики «(DPS) Available included metric data points for Infrastructure hosts» и «(DPS) Total metric data points reported by Infrastructure hosts».
В примере ниже показано, что было потреблено больше точек данных метрик, чем включено для этих хостов с Infrastructure Monitoring.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image017-1100-7b133be12d.png)

Infrastructure Monitoring (DPS)

Вы можете использовать метрику «(DPS) Metric data points reported and split by Infrastructure hosts» для отслеживания числа точек данных метрик, потреблённых каждым хостом с Infrastructure Monitoring.
Представление с разбивкой помогает выявить хосты с наибольшим потреблением точек данных метрик.
В примере ниже показано, что один из хостов с Infrastructure Monitoring зафиксировал значительно больше точек данных метрик, чем остальные.

![Infrastructure Monitoring (DPS)](https://dt-cdn.net/images/image019-1768-c4ed044b93.png)

Infrastructure Monitoring (DPS)

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)