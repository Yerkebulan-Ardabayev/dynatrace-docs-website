---
title: Анализ производительности
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/performance-analysis
scraped: 2026-05-12T11:14:27.836825
---

# Анализ производительности

# Анализ производительности

* How-to guide
* 6-min read
* Published Jul 19, 2017

Раздел **Performance analysis** отображает ряд метрик производительности приложения. Просто разверните раздел **Performance analysis** инфографики на [странице обзора приложения](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.") для просмотра параметров анализа производительности.

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

Performance analysis

## Работа с инфографикой

Каждая область инфографики в верхней части является кликабельной и предоставляет доступ к более подробным сведениям по каждой метрике. При выборе части инфографики левая часть под ней отображает различные данные, отражающие выбранную часть.

Левая часть инфографики анализа производительности показывает разбивку трафика приложения по типу браузера, типу пользователя и географическому региону. В центре находятся различные типы действий, рейтинг Apdex и раздел ошибок, а справа — разделы ресурсов и сервисов. По умолчанию в каждом разделе отображается топ-результат по каждому измерению. Разделы инфографики кратко описаны ниже.

Топ браузеров

При выборе раздела **Top browser** инфографики под инфографикой отображается **Browser breakdown**. Здесь показан трафик по типам браузеров — десктопным, мобильным, [синтетическим](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") и другим.

Выбрав **Analyze performance** в нижнем правом углу раздела **Browser breakdown**, можно перейти на [страницу многомерного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.") и выполнить многомерный анализ с точки зрения **Browsers**.

![Browsers](https://dt-cdn.net/images/browsers-2278-df044b9e0a.png)

Browsers

Топ типов пользователей

При выборе **Top user type** в разделе **User type** под инфографикой отображается количество действий в минуту, действия Load и XHR, а также ошибки JavaScript для **Real users** в сравнении с **Robots** (например, Googlebot) и [**Synthetic**](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."). Полоса в верхней части раздела **User type** является визуальным представлением этой разбивки.

Выбрав **Analyze performance** в нижнем правом углу раздела **Browser breakdown**, можно перейти на [страницу многомерного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.") и выполнить многомерный анализ с точки зрения **User type**.

![User types](https://dt-cdn.net/images/user-types-2289-a96765e8cd.png)

User types

Разбивка по геолокации

Выбрав **Geolocation breakdown**, можно просмотреть географические расположения с наибольшим трафиком. Дополнительные сведения можно посмотреть на [карте мира](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), перейдя по ссылке **View full world map**.

Выбрав **Analyze performance** в нижнем правом углу этого раздела, можно перейти на [страницу многомерного анализа](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.") и выполнить многомерный анализ с точки зрения **Geolocations**.

![Geolocations](https://dt-cdn.net/images/geolocations-2335-e51f88186e.png)

Geolocations

Действия загрузки, XHR и пользовательские действия

[Пользовательские действия](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") делятся на **Load** actions и **XHR** actions (или пользовательские действия, если они доступны).

При выборе части пользовательских действий инфографики отображается раздел **Impact of user actions on performance**. Отображаемые графики показывают, в том числе, метрику [Visually complete](/managed/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") для действий загрузки и метрику [Response end](/managed/observe/digital-experience/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") для XHR-действий.

Также можно использовать селектор метрик для отображения **Slowest 10%**, **Median** или **Fastest 10%** пользовательских действий.

Выбрав **Analyze performance** в нижнем правом углу этого раздела, можно [анализировать производительность приложения и пользовательские действия по нескольким измерениям](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Performance analysis](https://dt-cdn.net/images/performance-analysis-marked-2346-a63d69b1ca.png)

Performance analysis

Рейтинг Apdex

Dynatrace использует [рейтинги Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для оценки удовлетворённости пользователей конкретными приложениями. Выбрав **Apdex rating**, можно просмотреть удовлетворённость пользователей в указанном временном диапазоне.

![Apdex](https://dt-cdn.net/images/apdex-2275-4f37729a71.png)

Apdex

Ресурсы

Выберите **Resources** в инфографике для просмотра сведений о ресурсах, на которые опирается приложение. Dynatrace использует имена хостов-провайдеров загруженных ресурсов для категоризации контентных ресурсов как **3rd party resources**, **CDN resources** или **1st party resources**. Можно изучить продолжительность действий по типу ресурса и сравнить с предыдущим временным диапазоном.

На вкладке **1st party resources** также можно искать тенденции во внутренних ресурсах — **Scripts**, **Images** и **CSS** отслеживаются и отображаются отдельно.

Из этого раздела также можно перейти к [настройкам определения провайдеров](/managed/observe/digital-experience/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications.") для добавления провайдера вручную.

![Resources](https://dt-cdn.net/images/resources-2279-8542dfb13e.png)

Resources

Сервисы

Выберите раздел **Services** инфографики для просмотра сервисов, поддерживающих приложение, в разделе **Called services**. Выбрав **View service flow** в нижнем правом углу этого раздела, можно [просмотреть последовательность вызовов сервисов, инициируемых каждым сервисом](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment."). Dynatrace позволяет [получить доступ к потоку сервисов для приложения и для пользовательского действия](/managed/observe/digital-experience/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Learn how to access service flows for applications and user actions.").

![Services](https://dt-cdn.net/images/services-2255-23e1ba2133.png)

Services

### Доступность приложения

Если настроен один или несколько [синтетических мониторов](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.") для проверки доступности приложения, доступность можно видеть прямо на странице обзора приложения в разделе **Availability**. График доступности показывает сводное представление всех синтетических мониторов выбранного приложения. Выберите **View full details** для просмотра деталей об отключениях и перехода непосредственно к деталям синтетического монитора (настройки [временного диапазона анализа](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") сохранятся) для дальнейшего анализа.

![Availability](https://dt-cdn.net/images/availability-2274-52399f442d.png)

Availability

## Составные метрики по времени отклика

Этот раздел помогает с высокоуровневой точки зрения определить направление работы по производительности. Например, можно выяснить, является ли проблемой для приложения продолжительность до времени первого байта или следует сосредоточиться на воспринимаемой пользователем производительности загрузки, определяемой Speed index и Visually complete.

Выбрав **Analyze performance** в нижнем правом углу этого раздела, можно [анализировать производительность приложения и пользовательские действия по нескольким измерениям](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Composite metrics](https://dt-cdn.net/images/metrics-2309-defde297c9.png)

Composite metrics

## Топ-3 включённых доменов

Можно сразу видеть **Top 3 included domains** — домены с наибольшим количеством действий, автоматически обнаруженных [OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") в среде. Выберите **View full details** для просмотра подробностей о трафике из этих доменов и [определения новых приложений](/managed/observe/digital-experience/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

![Domains](https://dt-cdn.net/images/domains-2296-117bbe4967.png)

Domains

## Проблемы

Раздел [Problems](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.") отображает проблемы, автоматически обнаруженные Davis — движком ИИ Dynatrace. Выберите проблему для просмотра подробностей.

![Problems](https://dt-cdn.net/images/problems-2300-47780cd400.png)

Problems

## Топ ошибок

Список **Top errors** отображает наиболее часто встречающиеся [ошибки](/managed/observe/digital-experience/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") по типу: **JavaScript**, **Request** или **Custom**. Можно [настраивать ошибки](/managed/observe/digital-experience/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.") по типу или индивидуально.

Чтобы просмотреть **Top errors**:

1. Перейдите в **Web**.
2. Выберите приложение для анализа и прокрутите страницу вниз до раздела **Top errors**.

![Top errors infographic](https://dt-cdn.net/images/top-errors-921-5efd41aa51.png)

Top errors infographic

## Топ-3 пользовательских действий

Список **Top 3 user actions** показывает три самых медленных пользовательских действия. Действия сортируются по **приоритету** (действия с высоким приоритетом идут первыми) и **общему затраченному времени** (продолжительность умножается на количество действий). Метрика **total time consumed** ценна тем, что учитывает частоту вызова действия. Например, медленное действие, вызываемое часто, оказывает большее влияние на производительность, чем медленное действие, вызываемое редко.

При выборе пользовательского действия открывается [страница обзора пользовательского действия](/managed/observe/digital-experience/web-applications/analyze-and-use/analyze-individual-user-actions "Understand how you can access user action detail pages and analyze user actions.") для дальнейшего анализа.

Выбрав **View full details** в нижнем правом углу раздела, можно [анализировать производительность приложения и пользовательские действия по нескольким измерениям](/managed/observe/digital-experience/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![User actions](https://dt-cdn.net/images/user-actions-2260-8e1d88bb09.png)

User actions

## События

События представляют системные инциденты, которые могут представлять интерес. К таким событиям относятся ошибки, развёртывания новых версий приложения, изменения конфигурации и другие. События, показанные на изображении ниже, были сгенерированы из-за [превышения максимального количества пользовательских действий в минуту](https://dt-url.net/h92389d).

![Events](https://dt-cdn.net/images/image-2240-9cc2b49e51.png)

Events