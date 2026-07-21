---
title: Понимание и управление потреблением Foundation & Discovery (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/app-infra-observability/foundation-and-discovery
---

# Понимание и управление потреблением Foundation & Discovery (DPS)

# Понимание и управление потреблением Foundation & Discovery (DPS)

* Пояснение
* 1 минута на чтение
* Обновлено 09 июня 2026

Dynatrace OneAgent можно настроить в режиме Foundation & Discovery, который обеспечивает базовый мониторинг хостов (например, состояние хоста, статус диска и статус служб ОС).
В отличие от других инструментов, обеспечивающих базовый мониторинг, Foundation & Discovery использует ключевые функции OneAgent: обнаружение и топологию.

Режим Foundation & Discovery определяет коммуникацию между процессами и соответствующим образом заполняет [топологию Smartscape](/managed/analyze-explore-automate/smartscape-classic "Узнать, как Smartscape визуализирует все объекты и зависимости в среде."). 
Это даёт важные подсказки для AIOps, входящего в состав OneAgent. Подробнее см. [автоматический анализ первопричин Davis AI](/managed/dynatrace-intelligence "Узнать, как Davis® AI обнаруживает аномалии производительности, определяет первопричины и использует модели ИИ для адаптивных порогов во всей среде.").

Широкое развёртывание режима Foundation & Discovery позволяет выбрать подходящий режим мониторинга для каждого хоста.
Критичность хоста можно определить на основе того, какие процессы, технологии, внешне доступные службы и топологические соединения на нём присутствуют.

OneAgent во всех режимах также включает автоматизированный [приём логов](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed."), который потребляет [Log Management and Analytics](/managed/upgrade/unavailable-in-managed "Ваш выбор недоступен в Dynatrace Managed.").

### Часы хоста

Единица измерения для расчёта потребления мониторинга хостов в режиме Foundation & Discovery, это час хоста.
Каждый экземпляр Dynatrace OneAgent, установленный и запущенный на экземпляре операционной системы (развёрнутой на физической или виртуальной машине) с включённым режимом Foundation & Discovery, потребляет часы хоста.
Чем дольше хост находится под мониторингом, тем больше часов хоста потребляется.
Потребление не зависит от объёма памяти хоста.

Стоимость часа хоста для Foundation & Discovery

Хотя Foundation & Discovery и Infrastructure Monitoring используют часы хоста как единицу измерения для расчёта потребления мониторинга, у Foundation & Discovery более низкая стоимость за час хоста, что отражает его ограниченные возможности.
Подробности по [ценообразованию Dynatrace﻿](https://www.dynatrace.com/pricing/) можно найти в тарифном плане или уточнить у аккаунт-менеджера Dynatrace.

#### Гранулярность биллинга при потреблении часов хоста

Dynatrace создан для эластичных облачных сред, где хосты и службы быстро создаются и уничтожаются.
Поэтому гранулярность биллинга при потреблении часов хоста основана на 15-минутных интервалах.
Если хост находится под мониторингом менее 15 минут в течение интервала, потребление часов хоста округляется до 15 минут перед расчётом потребления.

На изображении ниже показано, как рассчитывается потребление часов хоста на хост, вычисляемое по 15-минутным интервалам.

![Расчёт потребления Foundation & Discovery](https://cdn.bfldr.com/B686QPH3/as/p9vgqhhs5p9qm636tfq4m/Foundation__Discovery_consumption_calculation-Light_Mode?auto=webp&format=png&position=1)

Расчёт потребления Foundation & Discovery

### Метрики

Foundation & Discovery включает базовые встроенные метрики.
В отличие от Full-Stack и Infrastructure Monitoring, Foundation & Discovery не предлагает включённые пользовательские метрики.
Подробнее см. [режимы мониторинга OneAgent](/managed/platform/oneagent/monitoring-modes/monitoring-modes#discovery "Узнать больше о доступных режимах мониторинга при использовании OneAgent.").

## Детали потребления: Foundation & Discovery

Dynatrace предоставляет встроенные метрики использования, которые помогают понять и проанализировать потребление Foundation & Discovery в организации.
Для использования этих метрик в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** нужно ввести `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и портал **Account Management** (**Usage summary** > **Foundation & Discovery** > **Actions** > **View details**).

(DPS) Foundation & Discovery billing usage
:   Ключ: `builtin:billing.foundation_and_discovery.usage`

    Измерение: count

    Разрешение: 15 мин

    Описание: Общее количество часов хоста в режиме Foundation & Discovery, подсчитанное с интервалом 15 мин.

(DPS) Foundation & Discovery billing usage per host
:   Ключ: `builtin:billing.foundation_and_discovery.usage_per_host`

    Измерение: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Часы хоста на хост в режиме Foundation & Discovery, подсчитанные с интервалом 15 мин.

(DPS) Ingested metric data points for Foundation & Discovery
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested`

    Измерение: count

    Разрешение: 15 мин

    Описание: Количество точек данных метрик, агрегированное по всем хостам, отслеживаемым в режиме Foundation & Discovery.

(DPS) Ingested metric data points for Foundation & Discovery per host
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`

    Измерение: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Количество точек данных метрик в разбивке по каждому хосту, отслеживаемому в режиме Foundation & Discovery.

## Похожие темы

* [Dynatrace OneAgent](/managed/ingest-from/dynatrace-oneagent "Понять важные концепции, связанные с OneAgent, и узнать, как устанавливать и эксплуатировать OneAgent на разных платформах.")
* [Обзор Application & Infrastructure Observability (DPS)](/managed/license/capabilities/app-infra-observability "Узнать о различных опциях Application & Infrastructure Observability, доступных с лицензией Dynatrace Platform Subscription (DPS).")
* [Ценообразование Dynatrace﻿](https://www.dynatrace.com/pricing/)