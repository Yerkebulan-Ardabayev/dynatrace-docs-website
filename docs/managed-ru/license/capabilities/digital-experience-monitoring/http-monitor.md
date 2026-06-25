---
title: Расчёт потребления HTTP Monitor (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/http-monitor
scraped: 2026-05-12T12:11:39.130999
---

# Расчёт потребления HTTP Monitor (DPS)

# Расчёт потребления HTTP Monitor (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность HTTP Monitor.
Обзор возможности и основных функций см. в [HTTP Monitor](/managed/license/capabilities/digital-experience-monitoring#http-monitor "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: синтетический запрос

HTTP-монитор состоит из одного или нескольких HTTP(S)-запросов (например, `GET`, `POST`, `HEAD`).

Единица измерения для HTTP-мониторов — синтетический запрос.
Каждый HTTP(S)-запрос потребляет один синтетический запрос.

Синтетический запрос тарифицируется сразу после его выполнения — независимо от того, успешен он или завершился ошибкой.
Если запрос завершается ошибкой и последующие запросы не выполняются, они не тарифицируются.

Пример: оценка потребления

Следующий расчёт даёт оценку максимально возможного потребления при условии выполнения всех синтетических запросов.
Фактическое потребление может отличаться в зависимости от того, завершились ли некоторые запросы ошибкой и были ли пропущены последующие.

`# синтетических запросов на монитор = (# синтетических запросов в мониторе) × (# запусков в час) × (# локаций) × # часов`

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Real User Monitoring в вашей организации.

Подробнее о соответствующих метриках потребления мониторинга см. в [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#synthetic "Explore the complete list of built-in Dynatrace metrics.").

### Отслеживание потребления и затрат в Account Management

Просмотреть использование можно также в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **HTTP Monitor**.

### Просмотр потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)