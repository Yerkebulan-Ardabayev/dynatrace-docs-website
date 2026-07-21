---
title: Понимание и управление потреблением Infrastructure Monitoring (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/infrastructure-monitoring
---

# Понимание и управление потреблением Infrastructure Monitoring (DPS)

# Понимание и управление потреблением Infrastructure Monitoring (DPS)

* Пояснение
* Чтение за 1 минуту
* Обновлено 01 июня 2026 г.

Dynatrace Infrastructure Monitoring, это OneAgent режим мониторинга, обеспечивающий полную наблюдаемость на уровне хостов для физических и виртуальных машин. На этой странице описано, как рассчитывается потребление Infrastructure Monitoring, как отслеживать и анализировать своё использование и как оптимизировать расходы.

Помимо всех возможностей [Foundation & Discovery](/managed/license/capabilities/app-infra-observability/foundation-and-discovery "Узнайте, как выставляется счёт и рассчитывается плата за потребление возможности Dynatrace Foundation & Discovery DPS."), Infrastructure Monitoring также включает детализированные метрики производительности процессов, метрики производительности диска, анализ сетевого взаимодействия между процессами и анализ использования памяти по процессам.
Dynatrace Extensions можно включить на хостах с режимом Infrastructure Monitoring, при этом они могут потреблять [точки данных пользовательских метрик](/managed/license/capabilities/app-infra-observability/infrastructure-monitoring#infra-metrics "Узнайте, как рассчитывается потребление Infrastructure Monitoring, как отслеживать и анализировать своё использование и как оптимизировать расходы.").

## Как рассчитывается потребление

Потребление Infrastructure Monitoring измеряется в **часах хоста** с использованием позиции тарифного плана **Infrastructure Monitoring**.

### Ключевые термины

Хост
:   Экземпляр операционной системы (физическая или виртуальная машина), на котором установлен и работает Dynatrace OneAgent.

Точка данных метрики
:   Отдельное значение измерения, хранящееся в Dynatrace, относящееся к метрике, определяемой ключом метрики, и имеющее временную метку.

### Правила подсчёта и исключения

Час хоста представляет собой один час активного мониторинга для одного хоста.

Потребление не зависит от объёма памяти хоста. Каждый отслеживаемый хост даёт один час хоста за час независимо от того, сколько у него ОЗУ.

### Гранулярность биллинга

Dynatrace создан для динамичных облачных сред, где хосты и сервисы быстро создаются и уничтожаются.
Поэтому гранулярность биллинга для потребления часов хоста рассчитывается с интервалом 15 минут.
Если хост отслеживался менее 15 минут в интервале, потребление часов хоста округляется до 15 минут перед расчётом потребления.

На рисунке ниже показано, как рассчитывается потребление часов хоста для каждого хоста с интервалом в 15 минут.

![Пример потребления Infrastructure Monitoring](https://dt-cdn.net/images/infrastructure-monitoring-consumption-light-mode-3840-23a7d10898.png)

Пример потребления Infrastructure Monitoring

### Включённая функциональность

В этом разделе предполагается, что использовались рекомендованные Dynatrace варианты развёртывания.
При использовании собственного развёртывания начисление платы за включённые метрики может по-прежнему работать так, как описано, но это не гарантируется Dynatrace.

Использование метрик Infrastructure Monitoring и [других встроенных метрик](/managed/analyze-explore-automate/metrics-classic/built-in-metrics "Ознакомьтесь с полным списком встроенных метрик Dynatrace.") включено без дополнительной платы на хостах с включённым Infrastructure Monitoring.

Каждый хост также включает 1500 точек данных пользовательских метрик за каждый 15-минутный интервал. Неиспользованные точки данных пользовательских метрик не переносятся на следующие интервалы.

Включённые точки данных метрик применяются автоматически к метрикам, поступающим с хостов, которые отслеживаются OneAgent в режиме Infrastructure Monitoring. Это относится к пользовательским метрикам, как описано в таблице ниже.

Точки данных пользовательских метрик, превышающие включённый объём точек данных метрик, тарифицируются как [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Узнайте, как выставляется счёт и рассчитывается плата за потребление возможности Dynatrace Custom Metrics Classic DPS.").

| Источник | Примеры (включая, но не ограничиваясь) |
| --- | --- |
| Хост, отслеживаемый Infrastructure Monitoring, и отправленные через [API метрик OneAgent](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Используйте API метрик Dynatrace для получения метрик отслеживаемых сущностей.") | * Метрики OpenTelemetry * Spring Micrometer * StatsD * JMX * Extensions, запущенные локально на хосте через OneAgent * локальный на хосте Telegraf |
| Узел Kubernetes, отслеживаемый Infrastructure Monitoring | * Метрики OpenTelemetry * Spring Micrometer * JMX * [Метрики Prometheus через ActiveGate](/managed/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics "Приём метрик из эндпоинтов Prometheus в Kubernetes, оповещения по метрикам и потребление мониторинга.")  * Сюда не входят метрики, отправленные через Dynatrace Collector или OpenTelemetry Collector. |

#### Пример расчёта включённых точек данных пользовательских метрик

* Первый 15-минутный интервал: `1 (отслеживаемых хостов) × 1500 (точек данных метрик) = 1500 включённых точек данных пользовательских метрик`
* Второй 15-минутный интервал: `2 (отслеживаемых хостов) × 1500 (точек данных метрик) = 3000 включённых точек данных пользовательских метрик`
* Третий 15-минутный интервал: `1 (отслеживаемых хостов) × 1500 (точек данных метрик) = 1500 включённых точек данных пользовательских метрик`
* Четвёртый 15-минутный интервал: `1 (отслеживаемых хостов) × 1500 (точек данных метрик) = 1500 включённых точек данных пользовательских метрик`

Потребление точек данных пользовательских метрик принимает разные формы.
Одинаковое количество точек данных пользовательских метрик может расходоваться:

* Небольшим числом метрик высокого разрешения или множеством метрик низкого разрешения.
* Равномерно в течение нескольких 15-минутных интервалов или всё сразу в течение одной минуты.
* Всеми хостами с Infrastructure Monitoring, подмножеством всех таких хостов или одним отдельным хостом с Infrastructure Monitoring.

## Отслеживание потребления

Dynatrace предоставляет различные возможности, которые помогают понять и проанализировать потребление Infrastructure Monitoring вашей организацией.

### Данные через Account Management

Менеджеры лицензий могут просматривать использование и затраты в [**Account Management**﻿](https://myaccount.dynatrace.com/).

![Сведения о стоимости и использовании Infrastructure Monitoring](https://dt-cdn.net/images/screenshot-2026-06-11-at-15-48-1822-293540e773.png)

Сведения о стоимости и использовании Infrastructure Monitoring

1. Перейти в [**Account Management**﻿](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary**.
2. Выбрать возможность **Infrastructure Monitoring**.
3. На этом экране также можно детализировать данные об использовании на уровне возможности и среды.

   * Уровень возможности: выбрать **View Details** рядом с нужной возможностью.
   * Уровень Environment: в таблице **Environments** выбрать **…** > **Open details with Notebooks**.

Дополнительная информация: [Overview (Dynatrace Platform Subscription)](/managed/manage/account-management/license-subscription/subscription-overview-dps "Просмотр сводки бюджета и анализа затрат по Dynatrace Platform Subscription (DPS).").

## Оптимизация потребления

### Рекомендации по конфигурации

* Отслеживать бюджет включённых пользовательских метрик. Каждый хост включает 1500 точек данных пользовательских метрик за 15-минутный интервал. Если расширения или пользовательская инструментация регулярно генерируют больше, стоит проверить, действительно ли нужны все метрики, и рассмотреть удаление малополезных метрик.
* Регулярно проверять инвентарь хостов. Искать выведенные из эксплуатации хосты, дублирующиеся экземпляры OneAgent или хосты, уменьшенные автомасштабированием и более не активные. Удаление неактивных хостов немедленно останавливает потребление.

### Постоянная оптимизация

* Использовать метрику `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host` для выявления хостов с высоким потреблением и сопоставления с их ценностью для бизнеса.
* Отключать OneAgent на простаивающих непроизводственных хостах (например, на staging-средах вне рабочего времени), чтобы не платить за неиспользуемый мониторинг.
* Проверять Dynatrace Extensions, работающие на хостах с Infrastructure Monitoring. Каждое расширение может генерировать точки данных пользовательских метрик. Отключать расширения, которые больше не приносят пользы.

### Автоматизация

Dynatrace можно использовать для автоматизации части работы по оптимизации:

* Оповещения об аномалиях: получать уведомления о неожиданных скачках потребления часов хоста Infrastructure Monitoring. Для этого настроить [Cost Monitors](/managed/manage-your-costs/control/cost-monitors "Узнайте, как использовать функцию Cost Monitors для прогнозов и событий затрат.") в [**Account Management**﻿](https://myaccount.dynatrace.com/).
* Отчёты по расписанию: регулярно доставлять автоматические отчёты о потреблении заинтересованным сторонам. Для этого использовать ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и ![Workflows](https://dt-cdn.net/images/workflows-1024-b5708f3cf9.webp "Workflows") **Workflows**.
* Рабочие процессы устранения: автоматически реагировать на события превышения порога затрат, например отключать некритичные хосты при достижении лимита бюджета. Для этого использовать [AutomationEngine](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

## Частые вопросы

### Влияет ли объём памяти хоста на потребление Infrastructure Monitoring?

Нет. Потребление часов хоста не зависит от объёма памяти хоста. Каждый отслеживаемый хост даёт один час хоста за каждый час мониторинга независимо от того, сколько у него ОЗУ. Это отличается от Full-Stack Monitoring, потребление которого масштабируется в зависимости от памяти.

### Как Infrastructure Monitoring соотносится с Foundation & Discovery?

Оба варианта используют часы хостов в качестве единицы измерения, но Infrastructure Monitoring обеспечивает значительно более глубокую наблюдаемость:

* Foundation & Discovery: базовое состояние хоста, статус служб ОС, обнаружение топологии и процессов. Без пользовательских метрик. Более низкая стоимость за час хоста.
* Infrastructure Monitoring: всё, что есть в Foundation & Discovery, плюс подробные метрики производительности процессов, производительность диска, анализ сетевого трафика, анализ памяти по процессам, а также 1 500 включённых точек данных пользовательских метрик на хост за 15 минут.

### Что происходит, если количество точек данных пользовательских метрик превышает включённую квоту?

Точки данных сверх 1 500 на хост за 15-минутный интервал тарифицируются как [Custom Metrics Classic](/managed/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

* Используй `builtin:billing.infrastructure_monitoring.metric_data_points.included` и `builtin:billing.infrastructure_monitoring.metric_data_points.ingested`, чтобы оставаться в рамках бюджета.
* Используй `builtin:billing.infrastructure_monitoring.metric_data_points.ingested_by_host`, чтобы определить, какие хосты являются источником превышения.

### Как работает детализация тарификации?

Потребление рассчитывается 15-минутными интервалами. Если хост мониторится менее 15 минут в течение заданного интервала, его потребление округляется до 15 минут. Это обеспечивает точную тарификацию для короткоживущих облачных инстансов.

### Включает ли Infrastructure Monitoring приём логов?

OneAgent автоматически принимает логи во всех режимах мониторинга, включая Infrastructure Monitoring. Однако приём логов не расходует часы хостов Infrastructure Monitoring, он тарифицируется отдельно как [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

### Можно ли использовать Dynatrace Extensions вместе с Infrastructure Monitoring?

Да. Dynatrace Extensions можно включить на хостах Infrastructure Monitoring. Extensions может генерировать точки данных пользовательских метрик, которые засчитываются в квоту 1 500 включённых точек данных на хост за 15-минутный интервал. Любое превышение тарифицируется отдельно.

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Цены Dynatrace﻿](https://www.dynatrace.com/pricing/)