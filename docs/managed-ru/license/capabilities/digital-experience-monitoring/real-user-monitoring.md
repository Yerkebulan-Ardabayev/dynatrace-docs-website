---
title: Расчёт потребления Real User Monitoring (RUM) (DPS)
source: https://docs.dynatrace.com/managed/license/capabilities/digital-experience-monitoring/real-user-monitoring
scraped: 2026-05-12T12:11:42.815615
---

# Расчёт потребления Real User Monitoring (RUM) (DPS)

# Расчёт потребления Real User Monitoring (RUM) (DPS)

* Explanation
* 5-min read
* Published Aug 12, 2025

На этой странице описано, как потребляется и тарифицируется DPS-возможность Real User Monitoring.
Обзор возможности и основных функций см. в [Real User Monitoring](/managed/license/capabilities/digital-experience-monitoring#rum "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.").

## Расчёт потребления: сессии на приложение в час

Единица измерения для расчёта потребления RUM (веб и мобильный) в вашей организации — сессии на приложение в час, без учёта захвата Session Replay.

Пользовательское действие — это клик мышью, касание пальцем или запуск приложения, инициирующий веб-запрос (например, загрузку страницы или навигационный переход).
Пользователь, взаимодействующий с несколькими веб-приложениями или приложениями в рамках одной сессии, потребляет по одной сессии в час для каждого приложения.
Для сессий продолжительностью более одного часа засчитывается одна сессия в час.

Полные сведения о начале и окончании пользовательских сессий RUM см. в [User session timings](/managed/observe/digital-experience/rum-concepts/user-session#user-session-timings "Learn how a user session is defined, when a user session starts or ends, how user session duration is calculated, and more.").
Потребление сессий RUM не ограничено.

Сессии, включающие только одно пользовательское действие, считаются «отскочившими» и не учитываются.
Пользователь, одновременно взаимодействующий с несколькими приложениями, потребляет по одной сессии для каждого из них.

Взаимодействия с гибридными мобильными приложениями, которые по техническим причинам включают веб-приложение и мобильное приложение, считаются единой сессией.

## Отслеживание потребления

В этом разделе описаны различные инструменты Dynatrace для отслеживания потребления и затрат.

### Отслеживание потребления с помощью метрик

Dynatrace предоставляет встроенные метрики использования для анализа потребления Real User Monitoring в вашей организации.

Подробнее о соответствующих метриках потребления мониторинга см. в [Built-in Real User Monitoring metrics](/managed/analyze-explore-automate/metrics-classic/built-in-metrics#real-user-monitoring "Explore the complete list of built-in Dynatrace metrics.").

### Отслеживание потребления и затрат в Account Management

Просмотреть использование можно также в Account Management.
Перейдите в [**Account Management**](https://myaccount.dynatrace.com/) > **Subscription** > **Overview** > **Cost and usage details** > **Usage summary** и выберите возможность **Third-Party Synthetic API Ingestion**.

### Отслеживание потребления и затрат через API

Запросить метрики можно через [Environment API — Metrics API v2](/managed/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Связанные темы

* [Обзор Digital Experience Monitoring (DEM) (DPS)](/managed/license/capabilities/digital-experience-monitoring "Learn how Dynatrace Digital Experience Monitoring (DEM) consumption is calculated using the Dynatrace Platform Subscription model.")
* [Real User Monitoring](/managed/observe/digital-experience/rum-concepts/rum-overview "Learn about Real User Monitoring, key performance metrics, mobile app monitoring, and more.")
* [Лицензирование Dynatrace](/managed/license "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.")
* [Ценообразование Dynatrace](https://www.dynatrace.com/pricing/)