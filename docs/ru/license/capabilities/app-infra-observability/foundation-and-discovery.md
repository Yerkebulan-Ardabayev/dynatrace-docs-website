---
title: Расчет потребления Foundation & Discovery (DPS)
source: https://www.dynatrace.com/docs/license/capabilities/app-infra-observability/foundation-and-discovery
scraped: 2026-03-06T21:17:13.819056
---

# Расчёт потребления Foundation & Discovery (DPS)


* Пояснение

Dynatrace OneAgent можно настроить в режиме Foundation & Discovery, который обеспечивает базовый мониторинг ваших хостов (например, состояние хоста, состояние дисков и статус служб ОС).
В отличие от других инструментов базового мониторинга, Foundation & Discovery использует ключевые возможности OneAgent: обнаружение и топологию.

Режим Foundation & Discovery определяет межпроцессное взаимодействие и заполняет топологию Smartscape соответствующим образом.
Это предоставляет важные данные для AIOps, который входит в состав OneAgent. Подробнее см. Автоматический анализ первопричин Dynatrace Intelligence AI.

Широкое развёртывание режима Foundation & Discovery позволяет выбрать подходящий режим мониторинга для каждого хоста.
Критичность хоста может быть определена на основе процессов, технологий, внешне доступных сервисов и топологических связей.

OneAgent во всех режимах также включает автоматизированный приём логов, который потребляет Log Management and Analytics.

### Хост-часы

Единицей измерения для расчёта потребления мониторинга хостов в режиме Foundation & Discovery является хост-час.
Каждый экземпляр Dynatrace OneAgent, установленный и работающий на экземпляре операционной системы (развёрнутом на физической или виртуальной машине) с включённым режимом Foundation & Discovery, потребляет хост-часы.
Чем дольше хост находится под наблюдением, тем больше хост-часов потребляется.
Потребление не зависит от объёма памяти хоста.

Стоимость хост-часа Foundation & Discovery

Хотя Foundation & Discovery и Infrastructure Monitoring используют хост-часы в качестве единицы измерения потребления мониторинга, Foundation & Discovery имеет более низкую стоимость за хост-час, что отражает его ограниченные возможности.
Подробнее о [ценах Dynatrace](https://www.dynatrace.com/pricing/) см. вашу тарифную карту или обратитесь к менеджеру по работе с клиентами Dynatrace.

#### Гранулярность выставления счетов за потребление хост-часов

Dynatrace создан для эластичных облачных сред, где хосты и сервисы быстро создаются и уничтожаются.
Поэтому гранулярность выставления счетов за потребление хост-часов основана на 15-минутных интервалах.
Когда хост мониторится менее 15 минут в интервале, потребление хост-часов округляется до 15 минут перед расчётом.

На изображении ниже показано, как потребление хост-часов на хост рассчитывается с 15-минутными интервалами.

![Расчёт потребления Foundation & Discovery](https://dt-cdn.net/images/discovery-consumption-1974-85ac28a179.webp)

### Метрики

Foundation & Discovery включает базовые встроенные метрики.
В отличие от Full-Stack и Infrastructure Monitoring, Foundation & Discovery не предлагает пользовательские метрики.
Для получения дополнительной информации см. [Режимы мониторинга OneAgent](../../../platform/oneagent/monitoring-modes/monitoring-modes.md#discovery "Узнайте больше о доступных режимах мониторинга при использовании OneAgent.").

## Детали потребления: Foundation & Discovery

Dynatrace предоставляет встроенные метрики использования, которые помогают понять и проанализировать потребление Foundation & Discovery вашей организацией.
Чтобы использовать эти метрики, в ![Data Explorer](https://dt-cdn.net/images/data-explorer-512-743267b1fc.png "Data Explorer") **Data Explorer** введите `DPS` в поле **Search**.
Эти метрики также доступны через Environment API и на портале **Account Management** (**Usage summary** > **Foundation & Discovery** > **Actions** > **View details**).

(DPS) Foundation & Discovery billing usage
:   Ключ: `builtin:billing.foundation_and_discovery.usage`

    Размерность: count

    Разрешение: 15 мин

    Описание: Общее количество хост-часов в режиме Foundation & Discovery, подсчитанное с 15-минутными интервалами.

(DPS) Foundation & Discovery billing usage per host
:   Ключ: `builtin:billing.foundation_and_discovery.usage_per_host`

    Размерность: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Хост-часы на хост в режиме Foundation & Discovery, подсчитанные с 15-минутными интервалами.

(DPS) Ingested metric data points for Foundation & Discovery
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested`

    Размерность: count

    Разрешение: 15 мин

    Описание: Количество точек данных метрик, агрегированных по всем хостам, контролируемым Foundation & Discovery.

(DPS) Ingested metric data points for Foundation & Discovery per host
:   Ключ: `builtin:billing.foundation_and_discovery.metric_data_points.ingested_by_host`

    Размерность: `dt.entity.host`

    Разрешение: 15 мин

    Описание: Количество точек данных метрик в разбивке по хостам, контролируемым Foundation & Discovery.

## Связанные темы

* Dynatrace OneAgent
* Обзор Application & Infrastructure Observability (DPS).")
* [Цены Dynatrace](https://www.dynatrace.com/pricing/)
