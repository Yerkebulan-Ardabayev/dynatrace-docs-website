---
title: Расчёт потребления Real User Monitoring with Session Replay (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring-session-replay
scraped: 2026-05-12T12:11:40.975616
---

# Расчёт потребления Real User Monitoring with Session Replay (DPS)

# Расчёт потребления Real User Monitoring with Session Replay (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Real User Monitoring with Session Replay.
Обзор возможности и основных функций см. в [Real User Monitoring with Session Replay](/managed/license/capabilities/digital-experience-monitoring#rum-sr "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: сессии на приложение в час

Когда Session Replay активирован для конкретной сессии RUM, единица измерения — одна сессия на приложение (веб и мобильный) в час с активированным Session Replay (также называемая «Session Replay Capture» в прайс-листе).

В зависимости от сессии тарифицируется либо сессия RUM, либо сессия RUM с Session Replay — но не обе одновременно.
Если сессия длится более одного часа, она засчитывается несколько раз (по одному разу в час).

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Real User Monitoring with Session Replay в вашей организации.

Подробнее о соответствующих метриках потребления мониторинга см. в [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

### Отслеживание потребления и затрат в Account Management

Просмотреть использование можно также в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Real User Monitoring with Session Replay**.

### Просмотр потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Session Replay](/managed/observe/digital-experience/session-replay "Learn how you can use Session Replay to better understand and troubleshoot errors experienced by your customers.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)