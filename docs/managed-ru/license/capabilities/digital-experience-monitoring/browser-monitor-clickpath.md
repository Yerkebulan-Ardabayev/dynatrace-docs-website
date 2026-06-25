---
title: Расчёт потребления Browser Monitor or Clickpath (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/browser-monitor-clickpath
scraped: 2026-05-12T12:11:44.694339
---

# Расчёт потребления Browser Monitor or Clickpath (DPS)

# Расчёт потребления Browser Monitor or Clickpath (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Browser Monitor or Clickpath.
Обзор возможности и основных функций см. в [Browser Monitor or Clickpath](/managed/license/capabilities/digital-experience-monitoring#browser-monitor "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: синтетическое действие

Единица измерения для браузерных мониторов — синтетическое действие.
Синтетическое действие — это взаимодействие с синтетическим браузером, инициирующее веб-запрос: загрузку страницы, навигационное событие или действие, вызывающее XHR- или Fetch-запрос, выполняемое при частных и публичных запусках Synthetic Browser Monitors.

Следующие взаимодействия не считаются действиями:

* Прокрутка, нажатия клавиш или клики, не инициирующие веб-запросы.
* XHR- или Fetch-запросы, выполняемые синтетическим браузером в результате пользовательского действия (например, загрузки страницы), не инициированного напрямую пользовательским вводом.

Синтетическое действие тарифицируется сразу после его совершения — независимо от того, успешно ли оно выполнено или завершилось ошибкой.
Если действие завершается ошибкой и последующие действия не выполняются, они не тарифицируются.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

Пример: оценка возможного потребления

Следующий расчёт даёт оценку максимально возможного потребления при условии выполнения всех синтетических действий.
Фактическое потребление может отличаться в зависимости от того, завершились ли некоторые действия ошибкой и были ли пропущены последующие.

`# синтетических действий на монитор = (# синтетических действий в мониторе) × (# запусков в час) × (# локаций) × # часов`

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Browser Monitor and Clickpath в вашей организации.

Подробнее о соответствующих метриках потребления мониторинга см. в [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#synthetic "Explore the complete list of built-in Dynatrace metrics.").

### Отслеживание потребления и затрат в Account Management

Отслеживать использование можно также в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Browser Monitor and Clickpath**.

### Отслеживание потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.")
* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)