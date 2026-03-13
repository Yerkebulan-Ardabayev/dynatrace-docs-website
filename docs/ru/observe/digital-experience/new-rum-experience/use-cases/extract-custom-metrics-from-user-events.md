---
title: Extract a metric from user events
source: https://www.dynatrace.com/docs/observe/digital-experience/new-rum-experience/use-cases/extract-custom-metrics-from-user-events
scraped: 2026-03-06T21:15:59.487993
---

# Извлечение метрики из пользовательских событий

# Извлечение метрики из пользовательских событий

* Последняя версия Dynatrace
* Руководство
* Опубликовано 19 декабря 2025 г.

OpenPipeline упрощает преобразование [пользовательских событий](/docs/observe/digital-experience/new-rum-experience/concepts/data-model#user-events "Ознакомьтесь с моделью данных в основе нового опыта RUM.") в пользовательские метрики, предоставляя вам возможность анализировать закономерности, влияющие на ваши цели, в [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Анализируйте, визуализируйте и делитесь информацией из данных наблюдаемости — всё в одном совместном, настраиваемом рабочем пространстве.") и [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Создавайте интерактивные, настраиваемые представления для визуализации, анализа и обмена данными наблюдаемости в режиме реального времени."), обеспечивая при этом пригодность данных для долгосрочного анализа. Возможность разбора данных из стандартных атрибутов пользовательских событий в выделенные поля упрощает извлечение метрик.

В качестве иллюстрации процесса в этом руководстве используется пример сайта бронирования путешествий — количество просмотров по каждому маршруту извлекается в пользовательскую метрику для выявления трендов.

## Пример сценария

В этом руководстве мы используем [демонстрационное приложение Dynatrace easyTravel](https://dt-url.net/rj034fg) в качестве примера. easyTravel отображает доступные маршруты, и когда пользователь выбирает маршрут, отображаются его детали.

Приложение инструментировано JavaScript-кодом для RUM, и собранные данные сопоставляются с [фронтендом](/docs/observe/digital-experience/new-rum-experience/concepts/frontends "Узнайте о концепции фронтенда в новом опыте RUM.") с именем `easytravel`. Каждый раз, когда пользователь переходит с одной страницы на другую — например, с главной страницы на конкретный маршрут — фиксируется [событие навигации](/docs/observe/digital-experience/new-rum-experience/web-frontends/concepts/pages-views-and-navigations#navigations "Узнайте, как определяются страницы, представления и навигации для веб-фронтендов в новом опыте RUM.").

События навигации предоставляют информацию, необходимую для анализа количества просмотров по маршрутам. Каждый маршрут имеет уникальный ID. При мягкой навигации к конкретному маршруту путь URL обновляется и включает ID маршрута — например, `/easytravel/journeys/24859438`. Это значение фиксируется в поле `view.url.path` события навигации.

Таким образом, вы можете проанализировать количество просмотров по маршрутам, выполнив следующий запрос DQL:

```
fetch user.events



| filter matchesPhrase(frontend.name, "easytravel") AND



characteristics.has_navigation == true AND



matchesPhrase(view.url.path, "/easytravel/journeys/*") AND



not matchesPhrase(view.url.path, "*book")



| parse view.url.path, "'/'LD'/'LD'/'LD:journey_id"



| summarize by: {journey_id}, count()



| sort `count()` desc
```

Хотя этот запрос хорошо подходит для краткосрочного анализа, он не идеален для отслеживания долгосрочных трендов. Для этой цели более подходящим подходом является создание пользовательской метрики на основе запроса с использованием OpenPipeline.

## Перед началом работы

Необходимые знания

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](/docs/platform/openpipeline/concepts/processing "Изучите основные концепции обработки данных в Dynatrace OpenPipeline.")

Предварительные условия

Убедитесь, что у вас есть разрешения, описанные в разделе [Разрешения нового опыта RUM](/docs/observe/digital-experience/new-rum-experience/permissions "Узнайте, какие разрешения необходимы для настройки нового опыта RUM.").

## Инструкция

1. Создание конвейера для разбора и извлечения метрик

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User events** > **Pipelines**.
2. Чтобы создать новый конвейер, выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Pipeline** и введите имя (например, `easyTravel`).
3. Для настройки разбора ID маршрута в отдельное поле перейдите в **Processing** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **DQL** и определите процессор, указав:

   * Описательное имя (например, `Add journey_id`).
   * Условие сопоставления. В нашем примере условие сопоставления:

     ```
     characteristics.has_navigation == true AND



     matchesPhrase(view.url.path, "/easytravel/journeys/*") AND



     not matchesPhrase(view.url.path, "*book")
     ```
   * Определение процессора. В нашем примере определение процессора:

     ```
     parse view.url.path, "'/'LD'/'LD'/'LD:journey_id"



     | fieldsAdd journey_id
     ```
4. Для настройки извлечения метрик перейдите в **Metric extraction** > ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Processor** > **Counter metric** и определите процессор, указав:

   * Описательное **Name** (например, `Viewed journeys`).
   * **Matching condition** (`isNotNull(journey_id)`).
   * **Metric key** (`easytravel.journey_view_count`).
   * Измерение метрики. В разделе **Dimensions**

     1. Выберите **Custom**.
     2. Введите **Field name on record** (`journey_id`).
     3. Введите **Dimension name** (`journey_id`).
5. Выберите **Add dimension**.
6. Выберите **Save**.

2. Маршрутизация данных в конвейер

1. Перейдите в ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Process and contextualize** > **OpenPipeline** > **User events** > **Dynamic routing**.
2. Чтобы создать новый маршрут, выберите ![Add](https://dt-cdn.net/images/dashboards-app-menu-plus-7e9b7c3547.svg "Add") **Dynamic route** и укажите:

   * Описательное **Name** (например, `easyTravel route`).
   * **Matching condition**. В нашем примере условие сопоставления:

     ```
     matchesValue(frontend.name, "easytravel")
     ```
   * **Pipeline**, содержащий инструкции обработки (`easyTravel`).
3. Выберите **Save**.

## Заключение

Вы успешно создали конвейер для разбора пользовательских событий и извлечения метрики. Теперь вы можете перейти в ![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks** и просмотреть её, например, с помощью следующего запроса:

```
timeseries count = sum(easytravel.journey_view_count), by: {journey_id}, interval: 3h



| sort arraysum(count) desc



| limit 5
```

![Пользовательская метрика, извлечённая из пользовательских событий, показывающая самые просматриваемые маршруты в easyTravel](https://dt-cdn.net/images/custom-metric-extraction-from-user-events-example-1292-7c0ae97470.png)

## Связанные темы

* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "Как использовать Dynatrace Query Language.")
* [Обработка в OpenPipeline](/docs/platform/openpipeline/concepts/processing "Изучите основные концепции обработки данных в Dynatrace OpenPipeline.")