---
title: Synthetic Monitoring
source: https://docs.dynatrace.com/managed/observe/digital-experience/synthetic-monitoring
scraped: 2026-05-12T11:07:21.296221
---

# Synthetic Monitoring

# Synthetic Monitoring

* Overview
* 1-min read
* Published Sep 25, 2018

То, что ваше веб-приложение доступно из офиса и отлично работает на вашем ноутбуке, не означает, что пользователи по всему миру получают такой же опыт. Поэтому критически важно постоянно обеспечивать доступность и производительность приложения с точки зрения пользователей.

Dynatrace Synthetic Monitoring позволяет с лёгкостью отслеживать доступность и производительность ваших приложений в том виде, в каком их видят пользователи со всего мира в любое время суток. Доступность — это доля успешных запросов в определённый момент или период времени, показывающая, полностью ли функционирует и доступно ли приложение. Производительность показывает, не замедляется ли ваша веб-страница или записанное взаимодействие по сравнению с пороговым значением.

Доступность и производительность внутренних ресурсов не менее важны. Возможность запуска мониторов из частных расположений позволяет применять тестовые возможности публичных расположений непосредственно в вашей инфраструктуре.

Dynatrace предлагает следующие типы синтетических мониторов: браузерные мониторы по одному URL, браузерные clickpath-ы, HTTP-мониторы и NAM-мониторы. Подробнее см. по ссылкам ниже. Лицензирование основано на [потреблении синтетических действий и запросов](/managed/license "О Dynatrace Platform Subscription (DPS), лицензионной модели для всех возможностей Dynatrace.").

### Общая информация

* [Типы синтетических мониторов](/managed/observe/digital-experience/synthetic-monitoring/general-information/types-of-synthetic-monitors "Узнайте о типах синтетических мониторов Dynatrace.")
* [Расчёты Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-calculations "Поймите расчёты метрик Synthetic Monitoring.")
* [Поддерживаемые методы аутентификации в Synthetic Monitoring](/managed/observe/digital-experience/synthetic-monitoring/general-information/synthetic-authentication "Узнайте, как настраивать методы аутентификации для мониторинга веб-приложений и API-эндпоинтов в Synthetic Monitoring.")
* [Выполнение синтетических мониторов по требованию для CI/CD](/managed/observe/digital-experience/synthetic-monitoring/general-information/on-demand-executions "Выполняйте синтетические мониторы по требованию из публичных или частных расположений.")
* [Интеграция с внешними хранилищами](/managed/observe/digital-experience/synthetic-monitoring/general-information/external-vault-integration "Синхронизируйте учётные данные Synthetic Monitoring с внешними хранилищами.")
* [Публичные расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/public-synthetic-locations "Узнайте обо всех доступных публичных расположениях Synthetic Monitoring.")
* [Архитектура и коммуникации Synthetic](/managed/observe/digital-experience/synthetic-monitoring/general-information/architecture-communication "Подробное описание архитектуры и коммуникационной инфраструктуры для приложения Synthetic.")

### HTTP-мониторы

* [Создание HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/create-an-http-monitor-classic "Узнайте, как настроить HTTP-монитор для проверки производительности и доступности сайта.")
* [Настройка HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/configure-http-monitors-classic "Узнайте о настройке HTTP-мониторов.")
* [Режим скрипта для конфигурации HTTP-монитора](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/script-mode-for-http-monitor-configuration-classic "Создавайте и редактируйте HTTP-мониторы в формате JSON.")
* [Скрипты до и после выполнения для HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/pre-and-post-scripting-for-http-monitors-classic "Узнайте, как применять предварительные и последующие скрипты к запросам.")
* [Метрики HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/http-monitors-classic/http-monitor-metrics-classic "Узнайте о метриках производительности, собираемых для HTTP-мониторов.")

### Анализ и оповещения

* [Обзор оповещений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-alerting-overview "Узнайте о концепциях и рабочем процессе оповещений Synthetic.")
* [Сведения Synthetic для браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-browser-monitors "Анализируйте результаты браузерных мониторов и clickpath-ов на странице Synthetic details.")
* [Многомерный анализ для браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/multidimensional-analysis-for-browser-monitors "Узнайте, как анализировать точки данных браузерных мониторов.")
* [Графики водопада](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/waterfall-graphs "Как анализировать загрузку ресурсов страницы для браузерных мониторов.")
* [Результаты отчётности HTTP-мониторов](/managed/observe/digital-experience/synthetic-monitoring/analysis-and-alerting/synthetic-details-for-http-monitors-classic "Узнайте о странице Synthetic details для HTTP-мониторов.")

### Браузерные мониторы

* [Создание браузерного монитора по одному URL](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/create-a-single-url-browser-monitor "Узнайте, как настроить браузерный монитор по одному URL для проверки доступности сайта.")
* [Запись браузерного clickpath-а](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/record-a-browser-clickpath "Узнайте, как записать браузерный clickpath для мониторинга доступности и производительности приложения.")
* [Настройка браузерных мониторов](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/configure-browser-monitors "Узнайте о настройке браузерных мониторов и clickpath-ов.")
* [События браузерного clickpath-а](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/browser-clickpath-events "Узнайте о типах событий, создаваемых при записи браузерного clickpath-а.")
* [Режим скрипта для конфигурации браузерного монитора](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/script-mode-for-browser-monitor-configuration "Создавайте и редактируйте браузерные мониторы в формате JSON.")
* [Количество действий, потребляемых браузерными clickpath-ами](/managed/observe/digital-experience/synthetic-monitoring/browser-monitors/number-of-actions-consumed-by-browser-clickpaths "Узнайте, сколько действий потребляет браузерный clickpath и чем они отличаются от событий.")

### Частные расположения Synthetic

* [Создание частного расположения Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/create-a-private-synthetic-location "Узнайте, как создать частное расположение для синтетического мониторинга.")
* [Требования для частных расположений Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/system-and-hardware-requirements-for-private-synthetic "Поддерживаемые операционные системы, версии Chromium и требования к оборудованию для запуска синтетических мониторов из частных расположений.")
* [Настройка прокси для частного синтетического мониторинга](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/setting-up-proxy-for-private-synthetic "Узнайте, как настроить свойства ActiveGate для использования прокси в частном синтетическом мониторинге.")
* [Контейнеризированные, автомасштабируемые частные расположения Synthetic в Kubernetes](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/containerized-locations "Разверните и управляйте контейнеризированными, автомасштабируемыми частными расположениями Synthetic на Kubernetes/RedHat OpenShift.")
* [Управление частными расположениями Synthetic](/managed/observe/digital-experience/synthetic-monitoring/private-synthetic-locations/manage-private-synthetic-locations "Анализируйте и управляйте использованием ресурсов в частных расположениях Synthetic.")

### API

* [Synthetic API v1](/managed/dynatrace-api/environment-api/synthetic "Узнайте о возможностях Dynatrace Synthetic v1 API.")
* [Synthetic API v2](/managed/dynatrace-api/environment-api/synthetic-v2 "Узнайте о возможностях Dynatrace Synthetic v2 API.")
* [API хранилища учётных данных](/managed/dynatrace-api/configuration-api/credential-vault "Узнайте о возможностях Dynatrace configuration API для учётных данных.")
* [API вычисляемых метрик — Synthetic](/managed/dynatrace-api/configuration-api/calculated-metrics/synthetic-metrics "Управляйте вычисляемыми синтетическими метриками через Dynatrace configuration API.")

## Связанные темы

* [Synthetic Monitoring](https://www.dynatrace.com/platform/synthetic-monitoring/)