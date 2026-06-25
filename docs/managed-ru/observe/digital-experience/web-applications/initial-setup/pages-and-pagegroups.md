---
title: Страницы и группы страниц
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/initial-setup/pages-and-pagegroups
scraped: 2026-05-12T11:35:12.224624
---

# Страницы и группы страниц

# Страницы и группы страниц

* How-to guide
* 7-min read
* Updated on Mar 05, 2026

Страницы и группы страниц для веб-приложений предоставляют дополнительный уровень контекстной информации для ваших [пользовательских действий](/managed/observe/digital-experience/rum-concepts/user-actions "Learn what user actions are and how they help you understand what users do with your application.") и других RUM-сущностей. Этот дополнительный контекст можно использовать для улучшения поиска, фильтрации и агрегирования данных о пользовательском опыте, производительности и отладке.

* Используйте **страницы** для анализа пользовательских действий на одной веб-странице в рамках всех пользовательских сессий.
* Используйте **группы страниц** для автоматической группировки пользовательских действий, ведущих к технически схожим или идентичным страницам, не теряя деталей отдельных экземпляров.

В версиях Dynatrace 1.213 и более ранних для получения аналогичного результата требовалась настройка [правил именования пользовательских действий](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions "Customize automatically generated user action names for your web applications.").

## Автоматическая группировка страниц и пользовательских действий

Рассмотрим пример приложения EasyTravel — портала бронирования путешествий.

EasyTravel app

![EasyTravel app home page](https://dt-cdn.net/images/easytravel-1920-09f68a0a2f.png)

EasyTravel app home page

EasyTravel предлагает ряд туристических предложений.

* У каждого предложения есть своя страница с подробностями.
* Страницы с подробностями технически идентичны; отличается только содержимое. Например: `/easytravel/journeys/123456` и `/easytravel/journeys/654321`. Эти страницы отличаются только идентификатором путешествия.

### Группы страниц

Проанализируем производительность этого приложения. Вместо сравнения отдельных путешествий имеет смысл начать на уровень выше и анализировать производительность групп технически идентичных страниц. Именно здесь и нужны группы страниц. Группы страниц основаны на путях и идентификаторах, которые Dynatrace определяет автоматически.

Ниже показана взаимосвязь страниц и групп страниц в данном примере:

![Pages and page groups](https://dt-cdn.net/images/pages-and-page-groups-info-458-010ff91ea0.png)

Pages and page groups

В целом группировка страниц работает автоматически. При использовании Angular или Vue.js Dynatrace автоматически инструментирует маршрутизатор соответствующего фреймворка, что сразу же предоставляет понятные разработчику имена и группы. Для других фреймворков, например React, Dynatrace использует интеллектуальную кластерную группировку на основе уровней пути и автоматического определения идентификаторов в пути страницы.

### Пользовательские действия

Пользовательское действие может:

* **Вызвать перезагрузку страницы** — например, при выборе навигационной ссылки на странице с серверным рендерингом, что приводит к [действию загрузки](/managed/observe/digital-experience/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application.").
* **Инициировать [смену маршрута](#analyze-route-changes)** — например, при мягкой навигации через [XHR-действие](/managed/observe/digital-experience/rum-concepts/user-actions#xhr-action "Learn what user actions are and how they help you understand what users do with your application.") в одностраничном приложении.
* **Происходить без перезагрузки страницы или смены маршрута** — например, при нажатии кнопки, запускающей XHR-действие, которое загружает новые данные и обновляет диаграмму, но пользователь остаётся на той же странице.

## Действия загрузки, страницы и группы страниц

### Действия загрузки

Для группировки нескольких [действий загрузки](/managed/observe/digital-experience/rum-concepts/user-actions#load-action "Learn what user actions are and how they help you understand what users do with your application."), представляющих загрузки схожих или технически идентичных страниц, создаётся [заполнитель](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions#add-and-use-placeholders "Customize automatically generated user action names for your web applications."). Как правило, все идентификаторы или зависящие от сессии детали заменяются единой строкой URL. Заполнитель включается в [правило именования пользовательских действий](/managed/observe/digital-experience/web-applications/initial-setup/create-custom-names-for-user-actions#create-action-names "Customize automatically generated user action names for your web applications.") и применяется ко всем связанным пользовательским действиям. В итоге отдельные пользовательские действия, такие как `Loading of page /journeys/62511135` и `Loading of page /journeys/61303030`, отображаются под общей строкой URL: `Loading of page /journeys/id`.

Хотя это позволяет просматривать агрегированные данные о производительности для одной страницы (например, для страниц с подробностями путешествий EasyTravel), теряются детали отдельных страниц (например, подробности каждого конкретного путешествия).

### Страницы и группы страниц

При использовании страниц и групп страниц сохраняются все индивидуальные детали, что позволяет просматривать и анализировать данные о производительности и отладке на уровне страницы и на уровне группы страниц. Атрибут **page name** сохраняет индивидуальные детали, а атрибут **page group** используется для агрегатного анализа.

Однако с точки зрения анализа производительности страницы не заменяют действия загрузки, а дополняют их, поскольку лежащие в основе данные о производительности по-прежнему берутся из действий загрузки.

## Определение собственной группировки страниц

Если автоматическая группировка не покрывает все сценарии вашего приложения, используйте [JavaScript API RUM](/managed/observe/digital-experience/web-applications/additional-configuration/customize-rum "Find out how to customize Real User Monitoring using the JavaScript API.") для задания собственных имён страниц и групп страниц.

1. В файле `index.js` вызовите [`dtrum.enableManualPageDetection()`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#enablemanualpagedetection), чтобы сообщить RUM JavaScript о необходимости прекратить автоматическое определение и группировку [событий смены страниц](/managed/observe/digital-experience/rum-concepts/user-and-error-events#page-change "Learn about user and error events and the types of user and error events captured by Dynatrace.").
2. Используйте команду [`dtrum.setPage(newPage: APIPage)`](https://docs.dynatrace.com/javascriptapi/doc/types/dtrum.html#setpage) для задания желаемого имени страницы и группы:

   ```
   dtrum.setPage ({



   name: "My page",



   group: "My page group"



   });
   ```

## Доступ к страницам и группам страниц

Для просмотра данных мониторинга страниц и групп страниц начните со [страницы обзора приложения](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page."). Перейдите в **Web** и выберите приложение.

![Application overview page](https://dt-cdn.net/images/application-overview-page-1623-e66c333a82.jpg)

Application overview page

### Вкладки Page groups и Pages

На странице обзора приложения отображается раздел **Top 3 pages**, содержащий вкладки **Page groups** и **Pages**. Выберите вкладку с нужным уровнем детализации.

Page groups

Pages

Вкладка **Page groups** отображает три ведущие группы страниц по количеству просмотров страниц в минуту.

![Page groups tab](https://dt-cdn.net/images/page-groups-tab-801-a4455b8f45.png)

Page groups tab

* Выберите группу для перехода на её страницу обзора.
* Выберите **View all page groups** для отображения **Multidimensional Analysis** по всем группам страниц.

Вкладка **Pages** отображает три ведущие страницы по количеству просмотров страниц в минуту.

![Pages tab](https://dt-cdn.net/images/pages-tab-802-7f9edba68c.png)

Pages tab

* Выберите страницу для перехода непосредственно на её страницу обзора.
* Выберите **View all pages** для отображения **Multidimensional Analysis** по всем страницам.

### Страница многомерного анализа

Страница **Multidimensional analysis** предоставляет удобный обзор всех страниц или групп страниц.

![Multidimensional analysis for page groups](https://dt-cdn.net/images/multidimensional-analysis-page-groups-1641-b480b47934.jpeg)

Multidimensional analysis for page groups

Эта страница помогает найти ответы на следующие вопросы:

* Какие группы страниц или страницы наиболее просматриваемые?
* Какие посещаются чаще всего?
* На каких группах страниц или страницах происходит больше всего действий?
* Где больше всего ошибок?
* На каких медленная начальная загрузка?
* На каких медленная смена маршрута?

**Sessions** отображает обнаруженные смены страниц как дополнительный тип события [**Page change**](/managed/observe/digital-experience/rum-concepts/user-and-error-events#page-change "Learn about user and error events and the types of user and error events captured by Dynatrace."), включая смены страниц при полной загрузке и смены маршрута. [Dynatrace User Sessions Query Language (USQL)](/managed/observe/digital-experience/session-segmentation/custom-queries-segmentation-and-aggregation-of-session-data "Learn how you can access and query user session data based on keywords, syntax, functions, and more.") позволяет запрашивать и подсчитывать события **Page change**.

### Страница обзора группы страниц или страницы

На странице **Multidimensional analysis** выберите страницу или группу страниц для перехода на её страницу обзора. На скриншоте ниже показана страница обзора для группы страниц **journeys/:id/book**.

Page group overview page

![Page group overview page](https://dt-cdn.net/images/page-group-overview-page-1632-abdd7db86f.png)

Page group overview page

## Построение графиков производительности страниц и групп страниц

Для построения графика производительности страницы или группы страниц создайте [вычисляемую метрику](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.") для страницы или группы страниц в существующем многомерном анализе. Затем используйте [Data Explorer](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") для отображения метрики на нужной панели мониторинга.

Чтобы создать вычисляемую метрику для страницы или группы страниц:

1. Перейдите в **Web**.
2. Выберите приложение для отображения его страницы обзора.
3. В разделе **Impact of user actions on performance** выберите **Analyze performance**.
4. В разделе **Detail analysis for selected timeframe** выберите метрику производительности, затем задайте фильтр по имени страницы или группе страниц.
5. Выберите **Create metric**.

   ![Create a metric for a page group](https://dt-cdn.net/images/create-metric-for-page-group-1891-5710294840.jpeg)

   Create a metric for a page group

Подробнее о создании и отображении вычисляемых метрик см. в разделе [Create calculated metrics for web applications](/managed/observe/digital-experience/web-applications/additional-configuration/rum-calculated-metrics-web "Create calculated metrics as well as custom charts based on calculated metrics for your web applications.").

## Анализ смен маршрутов

В одностраничных приложениях (SPA) и прогрессивных веб-приложениях (PWA) конечные пользователи не всегда вызывают полную перезагрузку страницы при навигации с одной страницы на другую.

Такие веб-приложения используют компонент маршрутизатора, который асинхронно загружает только ресурсы, необходимые для построения новой страницы. Мягкие навигации (иными словами, «навигации внутри страницы») поэтому также называют «сменами маршрутов» и они повторно используют уже загруженные и отрендеренные HTML-структуры. Dynatrace обнаруживает эти мягкие навигации и помечает их как **route changes**.

**Route change** в Dynatrace технически не является новым типом пользовательских действий, а представляет собой особый вид XHR-действия. Это навигация в одностраничном приложении без загрузки новых документов, хотя внешне она может выглядеть как переход на новую страницу.

Для анализа смен маршрутов:

1. Перейдите в **Web**.
2. Выберите приложение для отображения его страницы обзора.
3. В разделе **Top 3 pages** выберите **View all page groups** или **View all pages**.
4. В раскрывающемся списке **Action type** выберите **Route changes** для фокусировки на сменах маршрутов для отдельных групп страниц или страниц.
5. Выберите группу страниц или страницу для анализа.
6. В разделе **Performance** выберите **Route changes** из раскрывающегося списка для получения подробных сведений о производительности.
7. Выберите **Perform waterfall analysis** для анализа базовых действий смены маршрута для этой страницы. Здесь можно сопоставить подробные данные о производительности и ошибках.