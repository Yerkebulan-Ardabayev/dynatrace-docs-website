---
title: Контекстный анализ Apdex в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/session-segmentation/apdex-analysis
---

# Контекстный анализ Apdex в RUM Classic

# Контекстный анализ Apdex в RUM Classic

* Практическое руководство
* Чтение за 2 мин
* Опубликовано 27 января 2023 г.

Dynatrace упрощает анализ [Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") приложения по разным измерениям. Можно проверить рейтинг Apdex для конкретного действия пользователя, местоположения и приложения, а также посмотреть рейтинг Apdex для каждого действия пользователя в рамках одной пользовательской сессии.

## Анализ по местоположению

Используйте представление **World map**, доступное для [веб-приложений](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Узнайте, как представление World map даёт сведения о рейтингах Apdex, действиях пользователей, длительности действий и ошибках JavaScript."), [мобильных приложений](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта мобильного приложения.") и [пользовательских приложений](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта пользовательского приложения."), чтобы увидеть оценки Apdex, выделенные цветом, и другую информацию о производительности.

![Анализ по местоположению](https://dt-cdn.net/images/apdex-on-worldmap-1903-677a742e2e.png)

Анализ по местоположению

## Анализ по действиям пользователя

Чтобы проанализировать удовлетворённость пользователей для конкретного действия пользователя

1. Перейдите в **Web**, **Mobile** или **Custom Applications**.
2. Выберите приложение и прокрутите вниз до **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное действие пользователя и выберите его.
   Откроется страница сведений о действии пользователя. Оценка отображается на плитке **Apdex rating**.

![Анализ по действиям пользователя](https://dt-cdn.net/images/apdex-on-user-action-1902-f7e7545781.png)

Анализ по действиям пользователя

## Анализ по приложению

Чтобы увидеть, как удовлетворённость пользователей меняется со временем для конкретного приложения

* **Веб-приложения**

  1. Перейдите в **Web**.
  2. Выберите плитку **Apdex rating** на инфографике. Также можно выбрать **Analyze Apdex**, чтобы получить более подробные сведения.

     ![Анализ по приложению](https://dt-cdn.net/images/apdex-on-application-overview-1905-895ba0a0d2.png)

     Анализ по приложению
* **Мобильные приложения**

  [График **Apdex rating**](/managed/observe/digital-experience/rum-classic/mobile-applications/analyze-and-use/check-usage-metrics-mobile#apdex-rating "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта мобильного приложения.") доступен на странице обзора приложения.
* **Пользовательские приложения**

  Откройте [график **Apdex rating**](/managed/observe/digital-experience/rum-classic/custom-applications/analyze-and-use/check-usage-metrics-custom#apdex-rating "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта пользовательского приложения.") со страницы обзора приложения.

## Анализ пользовательского пути между приложениями

Чтобы проанализировать и понять проблемные места для каждого действия пользователя в рамках пользовательского пути

1. На странице обзора приложения выберите **Analyze user sessions**, затем выберите пользовательскую сессию.

![Анализ пользовательского пути](https://dt-cdn.net/images/apdex-on-user-journey-1903-429abf6255.png)

Анализ пользовательского пути

## Apdex для бизнес-отчётности

Можно выделить Apdex как ключевую метрику для коллег из бизнеса, добавив плитки, связанные с Apdex, в дашборд Dynatrace.

![Плитки Apdex на дашборде](https://dt-cdn.net/images/apdex-on-dashboards-1920-72e753ae39.png)

Плитки Apdex на дашборде

## Похожие темы

* [Рейтинги Apdex в RUM Classic](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.")
* [Настройка параметров Apdex для веб-приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/web-applications/additional-configuration/configure-apdex-web "Настройте пороговые значения производительности для удовлетворённости пользователей вашего веб-приложения и его ключевых действий пользователя.")
* [Настройка параметров Apdex для мобильных приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/mobile-applications/additional-configuration/configure-apdex-mobile "Настройте пороговые значения производительности для удовлетворённости пользователей вашего мобильного приложения и его ключевых действий пользователя.")
* [Настройка параметров Apdex для пользовательских приложений в RUM Classic](/managed/observe/digital-experience/rum-classic/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороговые значения производительности для удовлетворённости пользователей вашего пользовательского приложения и его ключевых действий пользователя.")