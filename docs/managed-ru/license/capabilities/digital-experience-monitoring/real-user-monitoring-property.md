---
title: Расчёт потребления Real User Monitoring Property (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring-property
scraped: 2026-05-12T12:11:46.536062
---

# Расчёт потребления Real User Monitoring Property (DPS)

# Расчёт потребления Real User Monitoring Property (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Real User Monitoring Property.
Обзор возможности и основных функций см. в [Real User Monitoring Property](/managed/license/capabilities/digital-experience-monitoring#rum-property "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: отдельные пользовательские сессии

Dynatrace измеряет потребление свойств RUM с использованием определённых свойств внутри отдельных пользовательских сессий. До 20 свойств на приложение включены в объём. За каждое дополнительное свойство сверх этого лимита взимается плата в соответствии с общим числом отдельных пользовательских сессий, использующих это свойство.

`((# тарифицируемых свойств) - (20 включённых свойств)) × (# отдельных пользовательских сессий) = Потребление`

Подробнее о соответствующих метриках потребления мониторинга см. в [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Real User Monitoring Property в вашей организации.
Для использования этих метрик в Data Explorer введите `DPS` в поле **Search**.

### Отслеживание потребления и затрат в Account Management

Просмотреть использование можно также в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Real User Monitoring Property**.

### Просмотр потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)