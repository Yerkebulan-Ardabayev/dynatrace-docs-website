---
title: Страницы и группы страниц в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/pages-and-pagegroups
---

# Страницы и группы страниц в RUM Classic

# Страницы и группы страниц в RUM Classic

* Практическое руководство
* Чтение: 7 мин
* Обновлено 05 марта 2026 г.

Страницы и группы страниц для веб-приложений дают дополнительный уровень контекстной информации для [действий пользователя](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") и других сущностей RUM. Этот контекст помогает точнее находить, фильтровать и агрегировать данные об опыте конечных пользователей, производительности и данные, важные для устранения неполадок.

* **Страницы** используются для анализа действий пользователя на отдельной веб-странице во всех пользовательских сессиях.
* **Группы страниц** используются для автоматической группировки действий пользователя, ведущих на технически похожие или одинаковые страницы, без потери деталей отдельных экземпляров.

В версиях Dynatrace 1.213 и более ранних для получения похожего результата нужно было настраивать [правила именования действий пользователя](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.").

## Автоматическая группировка страниц и действий пользователя

Рассмотрим пример приложения EasyTravel, портала бронирования путешествий.

Приложение EasyTravel

![EasyTravel app home page](https://dt-cdn.net/images/easytravel-1920-09f68a0a2f.png)

Главная страница приложения EasyTravel

EasyTravel показывает ряд предложений по путешествиям.

* У каждого предложения есть своя страница с деталями.
* Страницы деталей технически идентичны, различается только содержимое. Пример страниц деталей: `/easytravel/journeys/123456` и `/easytravel/journeys/654321`. Эти страницы отличаются только идентификатором путешествия.

### Группы страниц

Оценим производительность этого приложения. Вместо того чтобы сравнивать отдельные путешествия, разумнее подняться на уровень выше и анализировать производительность групп технически идентичных страниц. Здесь и пригождаются группы страниц. Группы страниц строятся на основе путей и идентификаторов, которые Dynatrace определяет автоматически.

Вот как соотносятся страницы и группы страниц в этом примере:

![Pages and page groups](https://dt-cdn.net/images/pages-and-page-groups-info-458-010ff91ea0.png)

Страницы и группы страниц

В целом группировка страниц работает «из коробки». При использовании Angular или Vue.js Dynatrace автоматически инструментирует соответствующий фреймворк-роутер, который сразу же даёт понятные разработчику, интуитивные имена и группы. При использовании других фреймворков, например React, Dynatrace применяет интеллектуальную группировку на стороне кластера на основе уровней пути и автоматического определения идентификаторов в пути страницы для группировки страниц веб-приложения.

### Действия пользователя

Действие пользователя может:

* **Вызывать перезагрузку страницы**, например при выборе навигационной ссылки на странице с серверным рендерингом, что приводит к [действию загрузки](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application.").
* **Запускать [смену маршрута](#analyze-route-changes)**, например когда мягкая навигация запускается через [действие XHR](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#xhr-action "Learn what user actions are and how they help you understand what users do with your application.") в одностраничном приложении.
* **Происходить без перезагрузки страницы или смены маршрута**, например при выборе кнопки, которая запускает действие XHR, получающее новые данные и обновляющее диаграмму, при этом пользователь остаётся на той же странице.

## Действия загрузки и страницы и группы страниц

### Действия загрузки

Чтобы сгруппировать несколько [действий загрузки](/managed/observe/digital-experience/rum-classic/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application."), которые представляют загрузки похожих или технически одинаковых страниц, создаётся [заполнитель](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions#add-and-use-placeholders "Customize automatically generated user action names for your web applications."). Обычно все идентификаторы или специфичные для сессии детали заменяются единой строкой URL. Затем заполнитель включается в [правило именования действий пользователя](/managed/observe/digital-experience/rum-classic/web-applications/initial-setup/create-custom-names-for-user-actions#create-action-names "Customize automatically generated user action names for your web applications.") и применяется ко всем связанным действиям пользователя. В итоге отдельные действия пользователя, такие как `Loading of page /journeys/62511135` и `Loading of page /journeys/61303030`, сопоставляются с общей строкой URL: `Loading of page /journeys/id`.

Это позволяет смотреть на агрегированные данные производительности для отдельной страницы (например, страниц деталей путешествия EasyTravel), но при этом теряются детали отдельных страниц (например, детали каждого конкретного путешествия).

### Страницы и группы страниц

Со страницами и группами страниц сохраняются все отдельные детали, поэтому можно смотреть и анализировать данные о производительности и информацию для устранения неполадок как на уровне страницы, так и на уровне группы страниц. Атрибут **имя страницы** сохраняет отдельные детали, а атрибут **группа страниц** можно использовать для просмотра агрегатов.

Однако с точки зрения анализа производительности страницы не заменяют действия загрузки, они их дополняют, поскольку исходные данные о производительности по-прежнему берутся из соответствующих действий загрузки.

## Определение собственной группировки страниц

Если автоматическая группировка не покрывает все случаи использования приложения, можно задать собственные имена страниц и групп страниц с помощью [RUM JavaScript API](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring Classic using the JavaScript API.").

1. В файле `index.js` вызвать [`dtrum.enableManualPageDetection()`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablemanualpagedetection), что сообщает RUM JavaScript о необходимости прекратить автоматическое определение и автоматическую группировку [событий смены страницы](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#page-change "Learn about user and error events and the types of user and error events captured by Dynatrace.").
2. Использовать команду [`dtrum.setPage(newPage: APIPage)`﻿](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#setpage), чтобы задать нужное имя страницы и группы:

   ```
   dtrum.setPage ({



   name: "My page",



   group: "My page group"



   });
   ```

## Доступ к страницам и группам страниц

Чтобы просмотреть данные мониторинга по страницам и группам страниц, начните со [страницы обзора приложения](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page."). Для перехода откройте **Web** и выберите приложение.

![Application overview page](https://dt-cdn.net/images/application-overview-page-1623-e66c333a82.jpg)

Страница обзора приложения

### Вкладки Page groups и Pages

На странице обзора приложения отображается раздел **Top 3 pages**, включающий вкладки **Page groups** и **Pages**. Выберите вкладку с нужной степенью детализации.

Page groups

Pages

Вкладка **Page groups** показывает три главные группы страниц по числу просмотров страниц в минуту.

![Page groups tab](https://dt-cdn.net/images/page-groups-tab-801-a4455b8f45.png)

Вкладка Page groups

* Выберите группу, чтобы перейти на её страницу обзора.
* Выберите **View all page groups**, чтобы отобразить **Multidimensional Analysis** для всех групп страниц.

Вкладка **Pages** показывает три главные страницы по числу просмотров страниц в минуту.

![Pages tab](https://dt-cdn.net/images/pages-tab-802-7f9edba68c.png)

Вкладка Pages

* Выберите страницу, чтобы перейти сразу на её страницу обзора.
* Выберите **View all pages**, чтобы отобразить **Multidimensional Analysis** для всех страниц.

### Страница многомерного анализа

Страница **Multidimensional analysis** предоставляет особенно полезный обзор всех страниц или групп страниц.

![Multidimensional analysis for page groups](https://dt-cdn.net/images/multidimensional-analysis-page-groups-1641-b480b47934.jpeg)

Многомерный анализ для групп страниц

Эта страница помогает найти ответы на следующие вопросы:

* Какие группы страниц или страницы просматриваются чаще всего?
* Какие посещаются чаще всего?
* Какие группы страниц или страницы наиболее загружены, где происходит много действий?
* На каких больше всего ошибок?
* Какие медленно выполняют первоначальную загрузку страницы?
* Какие медленно выполняют смену маршрута?

**Sessions** отображают обнаруженные смены страниц как дополнительный тип события [**Page change**](/managed/observe/digital-experience/rum-classic/rum-concepts/user-and-error-events#page-change "Learn about user and error events and the types of user and error events captured by Dynatrace."), включая смены страниц на основе полной загрузки страницы и смены маршрута. [Язык запросов пользовательских сессий Dynatrace (USQL)](/managed/observe/digital-experience/rum-classic/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") позволяет запрашивать и подсчитывать события **Page change**.

### Страница обзора группы страниц или страницы

На странице **Multidimensional analysis** выбери страницу или группу страниц, чтобы перейти на её страницу обзора. На скриншоте ниже показана страница обзора для группы страниц **journeys/:id/book**.

Page group overview page

![Page group overview page](https://dt-cdn.net/images/page-group-overview-page-1632-abdd7db86f.png)

Page group overview page

## Построение графика производительности страницы и группы страниц

Чтобы построить график производительности страницы или группы страниц, создай [вычисляемую метрику](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") для страницы или группы страниц в существующем многомерном анализе. Затем можно использовать [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для построения графика метрики на дашборде по выбору.

Чтобы создать вычисляемую метрику для страницы или группы страниц

1. Перейди в **Web**.
2. Выбери приложение, чтобы отобразить его страницу обзора.
3. В разделе **Impact of user actions on performance** выбери **Analyze performance**.
4. В разделе **Detail analysis for selected timeframe** выбери метрику производительности, а затем задай фильтр по имени страницы или группе страниц.
5. Выбери **Create metric**.

   ![Create a metric for a page group](https://dt-cdn.net/images/create-metric-for-page-group-1891-5710294840.jpeg)

   Create a metric for a page group

Подробнее о создании и построении графиков вычисляемых метрик см. в [Create calculated metrics for web applications in RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.").

## Анализ смены маршрутов

В одностраничных приложениях (SPA) и прогрессивных веб-приложениях (PWA) конечные пользователи не обязательно вызывают полную перезагрузку страницы при переходе с одной страницы на другую.

Такие веб-приложения используют компонент маршрутизации, который асинхронно загружает только те ресурсы, которые нужны для построения новой страницы. Поэтому мягкие переходы (иными словами, переходы «внутри страницы») также называются «сменой маршрута» (route changes) и повторно используют уже загруженные и отрисованные HTML-структуры. Dynatrace обнаруживает такие мягкие переходы и помечает их как **route changes**.

**Route change** в Dynatrace технически не является новым типом пользовательского действия, а представляет собой особый вид XHR-действия. Это навигация в одностраничном приложении без загрузки новых документов, однако она может выглядеть и восприниматься как переход на новую страницу.

Чтобы проанализировать смену маршрутов

1. Перейди в **Web**.
2. Выбери приложение, чтобы отобразить его страницу обзора.
3. В разделе **Top 3 pages** выбери **View all page groups** или **View all pages**.
4. В выпадающем списке **Action type** выбери **Route changes**, чтобы сфокусироваться на сменах маршрута для отдельных групп страниц или страниц.
5. Выбери группу страниц или страницу, которую нужно проанализировать.
6. В разделе **Performance** выбери **Route changes** из выпадающего списка, чтобы получить подробную информацию о производительности.
7. Выбери **Perform waterfall analysis**, чтобы проанализировать базовые действия смены маршрута для этой страницы. Здесь можно рассмотреть подробную информацию о производительности и ошибках в контексте.