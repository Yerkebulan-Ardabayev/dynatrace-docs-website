---
title: Анализ поведения пользователей
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/user-behavior-analysis
scraped: 2026-05-12T11:34:31.304276
---

# Анализ поведения пользователей

# Анализ поведения пользователей

* How-to guide
* 5-min read
* Published Jul 11, 2019

Раздел **User behavior analysis** отображает ряд ключевых метрик производительности, связанных с поведением пользователей: отказы, топ целевых и выходных страниц, конверсии и многое другое. Просто разверните раздел **User behavior analysis** инфографики на [странице обзора приложения](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.") для просмотра параметров анализа поведения пользователей.

![User behavior](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

User behavior

## Инфографика

Каждая область инфографики в верхней части является кликабельной и предоставляет доступ к более подробным сведениям по каждой метрике. При выборе части инфографики левая часть под ней отображает различные данные, отражающие выбранную часть. Разделы инфографики кратко описаны ниже.

Топ пользователей

При выборе плитки **Top users** инфографики в левой части под инфографикой отображается раздел **Users**, где можно сравнить новых и возвращающихся пользователей. Для фокусировки на одной группе выберите **Set as filter**.

Возвращающийся посетитель определяется с помощью cookie, хранящегося в браузере конечного пользователя. Cookie действителен в течение 2 лет. Если пользователь вернётся в приложение через 2 года, он будет считаться новым. Это позволяет понять и сформировать стратегию кэширования для приложения. Чем больше возвращающихся пользователей, тем эффективнее может быть стратегия кэширования. Если на графике нет возвращающихся пользователей, проверьте [настройки конфиденциальности данных](/managed/observe/digital-experience/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") приложения и убедитесь, что разрешение на размещение этого cookie включено.

![Top users](https://dt-cdn.net/images/top-users-2268-5a624f0fbf.png)

Top users

Топ типов пользователей

В разделе **Top user types** можно посмотреть, какой тип пользователей — **Real users**, [**Synthetic**](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") или **Robots** (например, Googlebot) — генерирует наибольший трафик. Выберите **Set as filter** для фильтрации всех данных по конкретному типу пользователей.

![User types](https://dt-cdn.net/images/user-types-2-2272-dc6ea2050d.png)

User types

Разбивка по геолокации

Выбрав **Geolocation breakdown**, можно анализировать региональные различия пользователей по различным метрикам — активным сессиям, отказам или длительности сессий. Используйте раскрывающийся список для выбора метрики, детализации региона и фокусировки на конкретном регионе через **Set as filter**. Также можно увеличить [карту мира](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.").

![Geolocations](https://dt-cdn.net/images/geo-2362-31f66a4bee.png)

Geolocations

Сессии

При выборе раздела **Sessions** в центре инфографики в левой части под инфографикой отображается раздел **Active sessions**. Этот раздел показывает, в какое время происходит наибольшее количество сессий и когда пользователи используют приложение. В нижней части раздела отображаются 3 интервала с наибольшим количеством активных сессий (**Top 3 active-session intervals**) и 3 интервала с наибольшим количеством начал сессий (**Top 3 session-start intervals**).

![Active sessions](https://dt-cdn.net/images/active-sessions-new-2560-9864b6202e.png)

Active sessions

Входные действия

Выбрав **Entry actions**, можно анализировать продолжительность **Entry actions**. Важно следить за тенденцией первого действия загрузки страницы или XHR в сессии, поскольку это часто целевые страницы приложения. Также можно просматривать [рейтинг Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для входных действий, поскольку пользователи ожидают хорошего опыта с первых же моментов работы с приложением.

![Entry actions](https://dt-cdn.net/images/entry-actions-new-2560-b574d97923.png)

Entry actions

Выходные действия

Выбрав **Exit actions**, можно анализировать продолжительность **Exit actions**. Отслеживайте продолжительность последнего действия загрузки страницы или XHR пользователей, чтобы определить, не покидают ли они приложение из-за проблем с производительностью. Также можно просматривать [рейтинг Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") для выходных действий, чтобы увидеть, не приводит ли плохой опыт к выходу пользователей.

![Exit actions](https://dt-cdn.net/images/exit-actions-2268-48f685dc0f.png)

Exit actions

Прочие действия

Выбрав **Other actions**, можно анализировать продолжительность **Other actions** — всех действий, которые не являются первым или последним действием в сессии пользователя. Также можно просматривать [рейтинг Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") этих действий.

![Other actions](https://dt-cdn.net/images/other-actions-2289-7781712a70.png)

Other actions

Показатель отказов

Выберите раздел **Bounce rate** инфографики для просмотра **Bounce rate analysis**. В этом анализе можно проверить, влияют ли долгие входные действия на показатель отказов, а также изучить влияние ошибок JavaScript на показатель отказов.

![Bounce rate](https://dt-cdn.net/images/bounce-rate-2277-c7c0752671.png)

Bounce rate

Общая конверсия

Выберите раздел **Overall conversion** инфографики для просмотра общего показателя успеха в сравнении с [целями конверсии](/managed/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones."). Каждая конвертированная сессия достигла как минимум одной из целей конверсии.

![Conversion analysis](https://dt-cdn.net/images/conversion-trend-2262-f8c4859038.png)

Conversion analysis

## Проблемы

Раздел [Problems](/managed/dynatrace-intelligence "Get familiar with the capabilities of Davis AI.") отображает проблемы, автоматически обнаруженные Davis — движком Dynatrace на основе ИИ. Выберите проблему для просмотра подробностей.

![Problems](https://dt-cdn.net/images/problems-users-2300-90269cf429.png)

Problems

### Топ целей конверсии

В разделе **Top conversion goals** отображается показатель конверсии для [определённых целей](/managed/observe/digital-experience/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones."). Выберите **View full details** в нижнем правом углу этого раздела для просмотра общих метрик по целям конверсии или анализа прогресса в достижении конкретных целей. Кроме того, можно перейти на страницу анализа конверсии, выбрав конкретную цель конверсии.

![Conversion goals](https://dt-cdn.net/images/conversion-goals-2288-b870fb76eb.png)

Conversion goals

## Топ-3 отказов

В разделе **Top 3 bounces** можно видеть, для каких пользовательских действий наибольшее количество отказов, и сравнивать продолжительность действий с отказами с теми же действиями в сессиях без отказов.

Выберите **View full details** для просмотра полного списка и связанных метрик для каждого отказа. Здесь можно сравнить продолжительности и ошибки JavaScript действий с отказами с теми же действиями в других сессиях.

![Bounces](https://dt-cdn.net/images/bounces-2231-3f8c2873cd.png)

Bounces

## Топ входных и выходных действий

Интересно, какие входные и выходные действия приложения самые медленные или самые популярные? Не обязательно специальные целевые страницы, а страницы, которые пользователи фактически используют для входа и выхода из приложения?

В нижней части страницы обзора приложения находится раздел **Top entry and exit actions**. Выберите конкретное действие здесь или нажмите **View full details**. Здесь можно найти исторические тенденции для всех входных и выходных действий.

![Entry and exit actions](https://dt-cdn.net/images/entry-and-exit-actions-2234-2b9112ea3e.png)

Entry and exit actions

## События

События представляют системные инциденты, которые могут быть интересны. Например, ошибки, развёртывания новых версий приложения, изменения конфигурации и другие.

![Events](https://dt-cdn.net/images/events-2297-ae4e392191.png)

Events