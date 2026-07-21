---
title: Анализ поведения пользователей в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/user-behavior-analysis
---

# Анализ поведения пользователей в RUM Classic

# Анализ поведения пользователей в RUM Classic

* Практическое руководство
* 5 минут на чтение
* Опубликовано 11 июля 2019 г.

Раздел **User behavior analysis** отображает ряд ключевых показателей поведения пользователей, таких как отказы, самые популярные посадочные и выходные страницы, конверсии и многое другое. Достаточно развернуть раздел **User behavior analysis** инфографики на [странице обзора приложения](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page."), чтобы увидеть варианты анализа поведения пользователей.

![User behavior](https://dt-cdn.net/images/user-behaviour-2360-e98d95092b.png)

User behavior

## Инфографика

Каждая область инфографики, расположенной вверху, кликабельна и открывает доступ к более подробным данным по каждому показателю. При выборе части инфографики раздел слева, сразу под инфографикой, отображает данные, соответствующие выбранной части. Отдельные части инфографики кратко описаны ниже.

Top users

Если выбрать плитку **Top users** на инфографике, слева под инфографикой откроется раздел **Users**, где можно сравнить новых пользователей с вернувшимися. Чтобы сосредоточиться на одной группе, выбери **Set as filter**.

Вернувшийся посетитель определяется с помощью cookie, который сохраняется в браузере конечного пользователя. Cookie действителен 2 года. Если пользователь вернётся в веб-приложение спустя 2 года, он будет считаться новым пользователем. Это позволяет понимать и выстраивать стратегию кэширования для веб-приложения. Чем больше вернувшихся пользователей, тем эффективнее может быть стратегия кэширования. Если на графике нет вернувшихся пользователей, стоит проверить [настройки конфиденциальности данных](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-real-user-monitoring-according-to-gdpr "Learn about the privacy settings that Dynatrace provides to ensure that your web applications comply with the data-privacy regulations of your region.") приложения. Нужно убедиться, что переключатель, разрешающий размещение этого cookie, включён.

![Top users](https://dt-cdn.net/images/top-users-2268-5a624f0fbf.png)

Top users

Top user types

В разделе **Top user types** можно посмотреть, какой тип пользователей, **Real users**, [**Synthetic**](/managed/observe/digital-experience/synthetic-monitoring "Learn about Synthetic Monitoring and how to create a single-URL browser monitor, a browser clickpath, or an HTTP monitor.") или **Robots** (например, Googlebot), генерирует больше всего трафика. Выбери **Set as filter**, чтобы отфильтровать все данные по конкретному типу пользователей.

![User types](https://dt-cdn.net/images/user-types-2-2272-dc6ea2050d.png)

User types

Geolocation breakdown

Выбрав **Geolocation breakdown**, можно анализировать региональные различия пользователей по различным показателям, таким как активные сессии, отказы или продолжительность сессии. С помощью выпадающего списка выбирается показатель, можно углубиться в конкретный регион и сфокусироваться на нём с помощью **Set as filter**. [Карту мира](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors.") также можно увеличить.

![Geolocations](https://dt-cdn.net/images/geo-2362-31f66a4bee.png)

Geolocations

Sessions

При выборе раздела **Sessions** в середине инфографики слева, под инфографикой, открывается раздел **Active sessions**. В нём показано, в какое время происходит больше всего сессий и когда пользователи используют приложение. В нижней части раздела отображаются 3 интервала с наибольшим числом активных сессий (**Top 3 active-session intervals**), а также 3 интервала с наибольшим числом начатых сессий (**Top 3 session-start intervals**).

![Active sessions](https://dt-cdn.net/images/active-sessions-new-2560-9864b6202e.png)

Active sessions

Entry actions

Выбрав **Entry actions**, можно проанализировать **Entry actions' duration**. Важно следить за трендом первой загрузки страницы или XHR-действия сессии, поскольку это часто посадочные страницы приложения. Также можно проверить [Apdex rating](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") по входным действиям, поскольку пользователи ожидают хорошего опыта работы с приложением с самого начала.

![Entry actions](https://dt-cdn.net/images/entry-actions-new-2560-b574d97923.png)

Entry actions

Exit actions

Выбрав **Exit actions**, можно проанализировать **Exit actions' duration**. Стоит следить за продолжительностью последней загрузки страницы или XHR-действия пользователей, чтобы понять, не покидают ли пользователи приложение из-за проблем с производительностью. Также можно проверить [Apdex rating](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") по выходным действиям, чтобы понять, не приводит ли негативный опыт к уходу пользователей.

![Exit actions](https://dt-cdn.net/images/exit-actions-2268-48f685dc0f.png)

Exit actions

Other actions

Выбрав **Other actions**, можно проанализировать **Other actions' duration**, продолжительность всех действий, которые не являются первым или последним действием сессии пользователя. Также можно проверить [Apdex rating](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") этих действий.

![Other actions](https://dt-cdn.net/images/other-actions-2289-7781712a70.png)

Other actions

Bounce rate

Выбери часть инфографики **Bounce rate**, чтобы посмотреть **Bounce rate analysis**. В этом анализе можно проверить, влияют ли долгие входные действия на показатель отказов, а также изучить влияние ошибок JavaScript на показатель отказов.

![Bounce rate](https://dt-cdn.net/images/bounce-rate-2277-c7c0752671.png)

Bounce rate

Overall conversion

Выбери раздел **Overall conversion** инфографики, чтобы увидеть общий показатель успеха относительно [целей конверсии](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones."). Каждая сконвертированная сессия достигла хотя бы одной из целей конверсии.

![Conversion analysis](https://dt-cdn.net/images/conversion-trend-2262-f8c4859038.png)

Conversion analysis

## Problems

Раздел [Problems](/managed/dynatrace-intelligence "Learn how Davis® AI detects performance anomalies, identifies root causes, and uses AI models for adaptive thresholds across your environment.") показывает проблемы, автоматически обнаруженные Davis, движком анализа первопричин на базе ИИ Dynatrace. Выбери проблему, чтобы узнать подробности.

![Problems](https://dt-cdn.net/images/problems-users-2300-90269cf429.png)

Problems

### Top conversion goals

Раздел **Top conversion goals** показывает показатель конверсии для [заданных целей](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/define-conversion-goals "Learn how to analyze conversion goals for specific user actions to understand how successfully you're meeting your conversion milestones."). Выбери **View full details** в правом нижнем углу этого раздела, чтобы посмотреть общие показатели, связанные с целями конверсии, или проанализировать прогресс по конкретным целям. Также можно перейти на страницу анализа конверсии, выбрав конкретную цель конверсии.

![Conversion goals](https://dt-cdn.net/images/conversion-goals-2288-b870fb76eb.png)

Conversion goals

## Top 3 bounces

В разделе **Top 3 bounces** видно, у каких действий пользователей больше всего отказов, и можно сравнить продолжительность действий с отказом с продолжительностью тех же действий в сессиях, где отказа не произошло.

Выбери **View full details**, чтобы увидеть полный список и связанные показатели по каждому отказу. Здесь можно сравнить продолжительность и ошибки JavaScript для действий с отказом с теми же действиями в других сессиях, где отказа не было.

![Bounces](https://dt-cdn.net/images/bounces-2231-3f8c2873cd.png)

Bounces

## Top entry and exit actions

Когда-нибудь возникал вопрос, какие входные и выходные действия приложения самые медленные или самые популярные? Не обязательно специально настроенные посадочные страницы, а те страницы, которые пользователи действительно используют для входа в приложение и выхода из него.

Внизу страницы обзора приложения находится раздел **Top entry and exit actions**. Выбери конкретное действие или **View full details**. Здесь можно найти исторические тренды по всем входным и выходным действиям.

![Entry and exit actions](https://dt-cdn.net/images/entry-and-exit-actions-2234-2b9112ea3e.png)

Entry and exit actions

## Events

События представляют собой системные инциденты, которые могут представлять интерес. К таким событиям относятся, например, ошибки, развёртывание новых версий приложения, изменения конфигурации и многое другое.

![Events](https://dt-cdn.net/images/events-2297-ae4e392191.png)

Events