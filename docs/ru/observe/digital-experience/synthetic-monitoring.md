---
title: Synthetic Monitoring
source: https://www.dynatrace.com/docs/observe/digital-experience/synthetic-monitoring
scraped: 2026-03-06T21:14:11.591598
---

* 1-min read

Тот факт, что ваше веб-приложение доступно из вашего офиса и отлично работает на вашем ноутбуке, не означает, что ваши клиенты по всему миру также имеют положительный опыт работы с ним. Поэтому крайне важно обеспечить постоянную доступность и производительность вашего приложения с точки зрения пользователей.

Dynatrace Synthetic Monitoring позволяет легко отслеживать доступность и производительность ваших приложений, как их воспринимают ваши клиенты по всему миру и круглосуточно. Доступность — это показатель успешности в заданный момент или период времени, указывающий, является ли ваше приложение полностью функциональным и доступным для пользователей. Производительность измеряет, испытывает ли ваша веб-страница или записанное взаимодействие значительные замедления по сравнению с пороговым значением.

Доступность и производительность ваших внутренних ресурсов не менее важны. Благодаря возможности выполнения мониторов из частных локаций вы можете перенести возможности тестирования, доступные в публичных локациях, непосредственно в вашу собственную инфраструктуру.

Dynatrace предлагает следующие типы синтетических мониторов: мониторы браузера с одним URL, браузерные цепочки кликов (clickpaths), HTTP-мониторы и NAM-мониторы. Ознакомьтесь с приведёнными ниже ссылками для получения дополнительной информации. Лицензирование основано на [потреблении синтетических действий и запросов](../../license.md "About Dynatrace Platform Subscription (DPS), the licensing model for all Dynatrace capabilities.").

### Общая информация

* [Типы синтетических мониторов](synthetic-monitoring/general-information/types-of-synthetic-monitors.md "Learn about Dynatrace synthetic monitor types.")
* [Вычисления Synthetic](synthetic-monitoring/general-information/synthetic-calculations.md "Understand Synthetic Monitoring metric calculations.")
* [Поддерживаемые методы аутентификации в Synthetic Monitoring](synthetic-monitoring/general-information/synthetic-authentication.md "Learn how to configure authentication methods for monitoring web applications and API endpoints in Synthetic Monitoring.")
* [Выполнение синтетических мониторов по запросу для CI/CD](synthetic-monitoring/general-information/on-demand-executions.md "Execute synthetic monitors on demand from public or private locations")
* [Интеграция с внешним хранилищем учётных данных](synthetic-monitoring/general-information/external-vault-integration.md "Synchronize Synthetic Monitoring credentials with external vaults.")
* [Публичные локации Synthetic](synthetic-monitoring/general-information/public-synthetic-locations.md "Learn about all currently available public Synthetic Monitoring locations.")
* [Архитектура и коммуникация Synthetic](synthetic-monitoring/general-information/architecture-communication.md "Detailed description of the architecture and communication infrastructure for Synthetic app")

### HTTP-мониторы

* [Создание HTTP-монитора](synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic.md "Learn how to set up an HTTP monitor to check the performance and availability of your site.")
* [Настройка HTTP-мониторов](synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic.md "Learn about configuring HTTP monitors.")
* [Режим скриптов для настройки HTTP-мониторов](synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic.md "Create or edit your HTTP monitors in JSON format.")
* [Скрипты пред- и пост-выполнения для HTTP-мониторов](synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic.md "Learn how to apply pre and post scripts to your requests")
* [Метрики HTTP-мониторов](synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic.md "Learn about the performance metrics collected for HTTP monitors.")

### Анализ и оповещения

* [Обзор оповещений Synthetic](synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview.md "Learn about synthetic alerting concepts and workflow.")
* [Детали Synthetic для браузерных мониторов](synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors.md "Analyze browser monitor and clickpath results on the Synthetic details page.")
* [Многомерный анализ для браузерных мониторов](synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors.md "Learn how to analyze browser-monitor data points.")
* [Каскадные графики](synthetic-monitoring/analysis-and-alerting/waterfall-graphs.md "How to analyze page resource downloads for browser monitors.")
* [Результаты отчётности HTTP-мониторов](synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic.md "Learn about the Synthetic details page for HTTP monitors.")

### Браузерные мониторы

* [Создание браузерного монитора с одним URL](synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor.md "Learn how to set up a single-URL browser monitor to check the availability of your site.")
* [Запись браузерной цепочки кликов](synthetic-monitoring/browser-monitors/record-a-browser-clickpath.md "Learn how to record a browser clickpath to monitor the availability and performance of your application.")
* [Настройка браузерных мониторов](synthetic-monitoring/browser-monitors/configure-browser-monitors.md "Learn about configuring browser monitors and clickpaths.")
* [События браузерной цепочки кликов](synthetic-monitoring/browser-monitors/browser-clickpath-events.md "Learn about the event types created when recording a browser clickpath.")
* [Режим скриптов для настройки браузерных мониторов](synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration.md "Create or edit your browser monitors in JSON format.")
* [Количество действий, потребляемых браузерными цепочками кликов](synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths.md "Find out how many actions are consumed by a browser clickpath and how they differ from events.")

### Частные локации Synthetic

* [Создание частной локации Synthetic](synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location.md "Learn how to create a private location for synthetic monitoring.")
* [Требования к частным локациям Synthetic](synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic.md "Supported operating systems, Chromium versions, and hardware requirements for running synthetic monitors from private locations")
* [Настройка прокси для частного синтетического мониторинга](synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic.md "Learn how to configure ActiveGate properties to set up a proxy for private synthetic monitoring.")
* [Контейнеризированные, автоматически масштабируемые частные локации Synthetic на Kubernetes](synthetic-monitoring/private-synthetic-locations/containerized-locations.md "Deploy and manage containerized, auto-scalable private Synthetic locations on Kubernetes/RedHat OpenShift.")
* [Управление частными локациями Synthetic](synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations.md "Analyze and manage capacity usage at your private Synthetic locations.")

### API

* [Synthetic API v1](../../dynatrace-api/environment-api/synthetic.md "Find out what the Dynatrace Synthetic v1 API offers.")
* [Synthetic API v2](../../dynatrace-api/environment-api/synthetic-v2.md "Find out what the Dynatrace Synthetic v2 API offers.")
* [API хранилища учётных данных](../../dynatrace-api/configuration-api/credential-vault.md "Learn what the Dynatrace configuration API for credentials offers.")
* [API вычисляемых метрик - Synthetic](../../dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics.md "Manage calculated synthetic metrics via the Dynatrace configuration API.")

## Связанные темы

* [Synthetic Monitoring](https://www.dynatrace.com/platform/synthetic-monitoring/)