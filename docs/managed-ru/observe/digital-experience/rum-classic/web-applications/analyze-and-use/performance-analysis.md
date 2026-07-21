---
title: Анализ производительности в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/performance-analysis
---

# Анализ производительности в RUM Classic

# Анализ производительности в RUM Classic

* Практическое руководство
* Чтение 6 мин.
* Опубликовано 19 июля 2017 г.

Раздел **Performance analysis** отображает ряд метрик производительности приложения. Чтобы увидеть варианты анализа производительности, нужно развернуть раздел **Performance analysis** на инфографике на [странице обзора приложения](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.").

![Performance analysis](https://dt-cdn.net/images/performance-analysis-2346-018950fbc4.png)

Performance analysis

## Работа с инфографикой

Каждая область инфографики, расположенная сверху, кликабельна и открывает доступ к более подробным данным по каждой метрике. При выборе части инфографики левая секция сразу под инфографикой показывает данные, отражающие выбранную часть.

Левая часть инфографики анализа производительности показывает разбивку трафика приложения по измерениям: тип браузера, тип пользователя и географический регион. В середине отображаются разные типы действий, рейтинг Apdex и раздел ошибок, а справа расположены разделы ресурсов и сервисов. По умолчанию в каждом разделе отображается ведущий показатель по данному измерению. Ниже кратко описаны отдельные секции инфографики.

Top browsers

При выборе секции **Top browser** на инфографике под ней слева отображается **Browser breakdown**. Здесь показан трафик по десктопным браузерам, мобильным браузерам, [синтетическому мониторингу](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") и другим источникам.

При выборе **Analyze performance** в нижнем правом углу раздела **Browser breakdown** происходит переход на [страницу многомерного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions."), где можно выполнить многомерный анализ с точки зрения **Browsers**.

![Browsers](https://dt-cdn.net/images/browsers-2278-df044b9e0a.png)

Browsers

Top user type

При выборе **Top user type** в разделе **User type** под инфографикой можно увидеть число действий в минуту, действия Load и XHR, а также ошибки JavaScript для **Real users** в сравнении с **Robots** (например, Googlebot) и [**Synthetic**](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor."). Полоса, отображаемая в верхней части раздела **User type**, служит визуальным представлением этой разбивки.

При выборе **Analyze performance** в нижнем правом углу раздела **Browser breakdown** происходит переход на [страницу многомерного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions."), где можно выполнить многомерный анализ с точки зрения **User type**.

![User types](https://dt-cdn.net/images/user-types-2289-a96765e8cd.png)

User types

Geolocation breakdown

При выборе **Geolocation breakdown** можно увидеть географические регионы с наибольшим трафиком. Более подробные данные доступны на [карте мира](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), которую можно открыть, выбрав **View full world map**.

При выборе **Analyze performance** в нижнем правом углу этого раздела происходит переход на [страницу многомерного анализа](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions."), где можно выполнить многомерный анализ с точки зрения **Geolocations**.

![Geolocations](https://dt-cdn.net/images/geolocations-2335-e51f88186e.png)

Geolocations

Load, XHR, and custom user actions

[User actions](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") делятся на действия **Load** и действия **XHR** (либо на пользовательские действия, если они доступны).

При выборе части инфографики с действиями пользователей можно увидеть **влияние действий пользователей на производительность**. Отображаемые графики показывают, среди прочего, метрику [Visually complete](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") для действий Load и [Response end](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") для действий XHR.

Также можно использовать переключатель метрик, чтобы отобразить **Slowest 10%**, **Median** или **Fastest 10%** действий пользователей.

При выборе **Analyze performance** в нижнем правом углу этого раздела можно [проанализировать производительность приложения и действия пользователей по нескольким измерениям](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Performance analysis](https://dt-cdn.net/images/performance-analysis-marked-2346-a63d69b1ca.png)

Performance analysis

Apdex rating

Dynatrace полагается на [рейтинги Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для расчёта удовлетворённости пользователей конкретными приложениями. При выборе **Apdex rating** можно увидеть удовлетворённость пользователей в пределах заданного периода времени.

![Apdex](https://dt-cdn.net/images/apdex-2275-4f37729a71.png)

Apdex

Resources

Выбор **Resources** на инфографике открывает подробные данные о ресурсах, от которых зависит приложение. Dynatrace использует имена хостов провайдеров загружаемых ресурсов, чтобы разделить ресурсы контента на категории **3rd party resources**, **CDN resources** или **1st party resources**. Можно изучить длительность действий по типу ресурса, а также сравнить её с предыдущим периодом времени.

На вкладке **1st party resources** также можно отслеживать тенденции по внутренним ресурсам: **Scripts**, **Images** и **CSS**-ресурсы отслеживаются и отображаются отдельно.

Из этого раздела также можно перейти к [настройкам определения провайдеров](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-third-party-and-cdn-content-detection-web "Manually define third-party and CDN providers along with auto-detected providers for your web applications."), где можно вручную добавить провайдера.

![Resources](https://dt-cdn.net/images/resources-2279-8542dfb13e.png)

Resources

Services

Выбор части инфографики **Services** открывает сервисы, поддерживающие приложение, в разделе **Called services**. При выборе **View service flow** в нижнем правом углу этого раздела можно [просмотреть последовательность вызовов сервисов, инициируемых каждым сервисом](/managed/observe/application-observability/services-classic/service-flow "Find out how Dynatrace can help you trace the sequence of service calls that are triggered by each service request in your environment."). Dynatrace позволяет [получить доступ к потоку сервисов как для приложения, так и для отдельного действия пользователя](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/service-flows-for-applications-and-user-actions "Learn how to access service flows for applications and user actions.").

![Services](https://dt-cdn.net/images/services-2255-23e1ba2133.png)

Services

### Доступность приложения

Если настроен один или несколько [синтетических мониторов](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.") для проверки доступности приложения, доступность приложения видна прямо на странице обзора приложения в разделе **Availability**. График доступности показывает агрегированное представление всех синтетических мониторов выбранного приложения. Можно выбрать **View full details**, чтобы просмотреть подробности о простоях и перейти непосредственно к деталям синтетического монитора (настройки [периода анализа](/managed/analyze-explore-automate/dashboards-classic/dashboards/dashboard-timeframe "Learn about Dynatrace dashboard timeframe and management zone settings.") при этом сохранятся) для дальнейшего анализа.

![Availability](https://dt-cdn.net/images/availability-2274-52399f442d.png)

Availability

## Композитные метрики по времени отклика

Этот раздел помогает на верхнем уровне определить, где стоит сфокусировать внимание с точки зрения производительности. Например, можно понять, есть ли проблема с продолжительностью до получения первого байта (time to first byte) или нужно сосредоточиться на воспринимаемой пользователем скорости загрузки, отражаемой Speed index и Visually complete.

При выборе **Analyze performance** в правом нижнем углу этого раздела можно [проанализировать производительность приложения и действия пользователей по множеству измерений](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![Composite metrics](https://dt-cdn.net/images/metrics-2309-defde297c9.png)

Composite metrics

## Топ-3 включённых домена

Здесь можно сразу увидеть **Топ-3 включённых домена**, то есть домены, содержащие наибольшее число действий, автоматически обнаруженных [OneAgent](/managed/ingest-from/dynatrace-oneagent "Understand the important concepts related to OneAgent and find out how to install and operate OneAgent on different platforms.") в среде. Можно выбрать **View full details**, чтобы посмотреть подробности о трафике с этих доменов и [определить новые приложения](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/define-your-applications-via-the-my-web-application-placeholder "Learn how to define your applications following the suggested, manual, or application detection rules approach.").

![Domains](https://dt-cdn.net/images/domains-2296-117bbe4967.png)

Domains

## Problems

Раздел [Problems](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.") показывает проблемы, автоматически обнаруженные Davis, AI-движком Dynatrace. Достаточно выбрать проблему, чтобы узнать подробности.

![Problems](https://dt-cdn.net/images/problems-2300-47780cd400.png)

Problems

## Top errors

Список **Top errors** отображает наиболее часто встречающиеся [ошибки](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#error "Learn about user and error events and the types of user and error events captured by Dynatrace.") по типу ошибки: **JavaScript**, **Request** или **Custom**. Ошибки можно [настроить](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-errors "Configure your application to capture or ignore request, custom, and JavaScript errors.") как по типу, так и по отдельности.

Чтобы просмотреть **Top errors**

1. Перейти в **Web**.
2. Выбрать приложение, которое нужно проанализировать, и прокрутить вниз до **Top errors**.

![Top errors infographic](https://dt-cdn.net/images/top-errors-921-5efd41aa51.png)

Top errors infographic

## Топ-3 действия пользователя

Список **Топ-3 действия пользователя** показывает три самых медленных действия пользователя. Действия сортируются по **приоритету** (действия с высоким приоритетом отображаются первыми) и по **суммарно затраченному времени** (длительность, умноженная на количество действий). Показатель **суммарно затраченного времени** ценен тем, что учитывает частоту вызова действия. Например, медленное действие, которое вызывается часто, оказывает более существенное влияние на производительность, чем медленное действие, которое вызывается редко.

При выборе действия пользователя откроется [страница обзора действия пользователя](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/analyze-individual-user-actions "Understand how you can access user action detail pages and analyze user actions."), где можно более подробно проанализировать конкретное действие пользователя.

При выборе **View full details** в правом нижнем углу раздела можно [проанализировать производительность приложения и действия пользователей по множеству измерений](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/multi-dimensional-analysis "Find out how Dynatrace Real User Monitoring Classic enables you to dig deep into your user actions and perform analysis across numerous dimensions.").

![User actions](https://dt-cdn.net/images/user-actions-2260-8e1d88bb09.png)

User actions

## Events

События представляют собой системные инциденты, которые могут быть интересны пользователю. К таким событиям относятся ошибки, развёртывания новых версий приложения, изменения конфигурации и другое. События, показанные на изображении ниже, были сгенерированы из-за того, что было [превышено максимальное количество действий пользователя в минуту﻿](https://dt-url.net/h92389d).

![Events](https://dt-cdn.net/images/image-2240-9cc2b49e51.png)

Events