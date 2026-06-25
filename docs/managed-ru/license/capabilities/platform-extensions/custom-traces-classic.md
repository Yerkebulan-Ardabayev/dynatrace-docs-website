---
title: Custom Traces Classic (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/platform-extensions/custom-traces-classic
scraped: 2026-05-12T12:13:05.791226
---

# Custom Traces Classic (DPS)

# Custom Traces Classic (DPS)

* 16-min read
* Updated on Jan 12, 2026

На этой странице описано, как потребляется и тарифицируется DPS-возможность Custom Traces Classic.
Обзор возможности и основных функций см. в [Custom Traces Classic](/managed/license/capabilities/platform-extensions#traces "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: принятые спаны

Единица измерения для Custom Traces Classic — принятый спан.
Спан — это единичная операция в рамках распределённой трассировки.
Для расчёта общего потребления умножьте количество принятых спанов на [цену за спан](https://www.dynatrace.com/pricing/rate-card/).

Трассировки, включая спаны OpenTelemetry, захваченные кодовыми модулями OneAgent или отправленные через локальный Trace API OneAgent, включены в [Full-Stack Monitoring](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") и поэтому не потребляются как Custom Traces Classic.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Custom Traces Classic в вашей организации.
Для использования в Data Explorer введите DPS в поле **Search**.
Эти метрики также доступны через Environment API и связаны в Account Management (**Usage summary** > **Custom Traces Classic** > **Actions** > **View details**).
В таблице ниже перечислены метрики для мониторинга потребления Custom Traces Classic в вашей организации.

(DPS) Total Custom Traces Classic billing usage
:   Ключ: `builtin:billing.custom_traces_classic.usage`

    Измерение: count

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых спанов, агрегированных по всем мониторируемым сущностям.

(DPS) Custom Traces Classic billing usage by monitored entity
:   Ключ: `builtin:billing.custom_traces_classic.usage_by_entity`

    Измерение: `dt.entity.monitored_entity\[ME:MONITORED_ENTITY]`

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых спанов с разбивкой по мониторируемой сущности.

(DPS) Custom Traces Classic billing usage by span type
:   Ключ: `builtin:billing.custom_traces_classic.usage_by_span_type`

    Измерение: `span_type\[STRING]`

    Разрешение: 1 мин

    Описание: Количество тарифицируемых принятых спанов с разбивкой по типу спана.

Суммарное количество тарифицируемых пользовательских трассировок за различные интервалы в любом выбранном периоде можно отслеживать с помощью метрики «(DPS) Total Custom Traces Classic billing usage».
В примере ниже показано потребление, агрегированное в 1-часовых интервалах.
С 11:00 до 14:00 каждый час потреблялось около 58 000 пользовательских трассировок.

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image056-906-0fd3d122fa.png)

Custom Traces Classic (DPS)

Потребление точек данных метрик по любой отфильтрованной сущности можно отслеживать с помощью метрики «(DPS) Billed metric data points reported and split by other entities».
В примере ниже показано, что все тарифицируемые пользовательские трассировки с 13:00 до 14:00 поступали от сущности collector-trace-exporter.

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image058-908-ecba7294a8.png)

Custom Traces Classic (DPS)

Для просмотра разбивки по типу спана используйте метрику «(DPS) Custom Traces Classic billing usage by span type».

![Custom Traces Classic (DPS)](https://dt-cdn.net/images/image060-906-1a6b019225.png)

Custom Traces Classic (DPS)

## Связанные темы

* [Обзор расширений платформы (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)