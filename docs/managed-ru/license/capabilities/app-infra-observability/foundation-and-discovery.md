---
title: Расчёт потребления Foundation & Discovery (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/foundation-and-discovery
scraped: 2026-05-12T11:13:49.082029
---

# Расчёт потребления Foundation & Discovery (DPS)

# Расчёт потребления Foundation & Discovery (DPS)

* Explanation
* 1-min read
* Updated on Dec 10, 2025

Dynatrace OneAgent можно настроить в режиме Foundation & Discovery, который обеспечивает базовый мониторинг хостов (например, работоспособность хоста, состояние диска и статус служб ОС).
В отличие от других инструментов базового мониторинга, Foundation & Discovery использует основные возможности OneAgent: обнаружение и топологию.

Режим Foundation & Discovery обнаруживает взаимодействие процессов и соответствующим образом заполняет [топологию Smartscape](/managed/analyze-explore-automate/smartscape-classic "Learn how Smartscape visualizes all the entities and dependencies in your environment.").
Это предоставляет важные подсказки для AIOps, включённого в OneAgent. Подробнее см. [Davis AI — автоматический анализ первопричин](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.").

Широкое развёртывание режима Foundation & Discovery позволяет выбрать оптимальный режим мониторинга для каждого хоста.
Критичность хоста можно определить на основе процессов, технологий, внешнедоступных сервисов и топологических связей.

OneAgent во всех режимах также включает автоматический [приём логов](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed."), который потребляет [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Your selection is unavailable in Dynatrace Managed.").

### Хост-часы

Единица измерения для расчёта потребления мониторинга хостов в режиме Foundation & Discovery — хост-час.
Каждый экземпляр Dynatrace OneAgent, установленный и запущенный на экземпляре операционной системы (на физической или виртуальной машине) с включённым режимом Foundation & Discovery, потребляет хост-часы.
Чем дольше мониторируется хост, тем больше хост-часов потребляется.
Потребление не зависит от объёма памяти хоста.

Стоимость хост-часа в Foundation & Discovery

Хотя Foundation & Discovery и Infrastructure Monitoring используют хост-часы в качестве единицы измерения, Foundation & Discovery имеет более низкую стоимость за хост-час, что отражает её ограниченные возможности.
Подробнее о [ценообразовании Dynatrace](https://www.dynatrace.com/pricing/) см. в вашей тарифной карте или обратитесь к менеджеру аккаунта Dynatrace.

#### Детализация тарификации потребления хост-часов

Dynatrace создан для эластичных облачных сред, где хосты и сервисы быстро запускаются и уничтожаются.
Поэтому детализация тарификации потребления хост-часов основана на 15-минутных интервалах.
Если хост отслеживается менее 15 минут в интервале, потребление хост-часов округляется до 15 минут перед расчётом.

На рисунке ниже показан расчёт потребления хост-часов на хост в 15-минутных интервалах.

![Foundation & Discovery consumption calculation](https://dt-cdn.net/images/discovery-consumption-1974-85ac28a179.webp)

Расчёт потребления Foundation & Discovery

### Метрики

Foundation & Discovery включает базовые встроенные метрики.
В отличие от Full-Stack и Infrastructure Monitoring, Foundation & Discovery не предлагает включённых пользовательских метрик.
Дополнительные сведения см. в [Режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Find out more about the available monitoring modes when using OneAgent.").

## Детали потребления: Foundation & Discovery

Dynatrace предоставляет встроенные метрики использования, помогающие понять и анализировать потребление Foundation & Discovery в вашей организации.
Чтобы использовать эти метрики, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и на портале **Account Management** (**Usage summary** > **Foundation & Discovery** > **Actions** > **View details**).

(DPS) Foundation & Discovery billing usage
:   Ключ: `builtin:billing.foundation_and_discovery.usage`

    Измерение: count

    Разрешение: 15 мин

    Описание: Общее число хост-часов в режиме Foundation & Discovery, подсчитанных в 15-минутных интервалах.

(DPS) Foundation & Discovery billing usage per host
:   Ключ: `builtin:billing.foundation_and_discovery.usage_per_host`

    Измерение: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Хост-часы на хост в режиме Foundation & Discovery, подсчитанные в 15-минутных интервалах.

(DPS) Ingested metric data points for Foundation & Discovery
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested`

    Измерение: count

    Разрешение: 15 мин

    Описание: Число точек данных метрик, агрегированных по всем хостам с мониторингом Foundation & Discovery.

(DPS) Ingested metric data points for Foundation & Discovery per host
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`

    Измерение: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Число точек данных метрик с разбивкой по хостам с мониторингом Foundation & Discovery.

## Связанные темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Learn about the different Application & Infrastructure Observability options that are available with a Dynatrace Platform Subscription (DPS) license.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)