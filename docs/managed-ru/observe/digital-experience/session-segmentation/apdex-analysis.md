---
title: Анализ Apdex в контексте
source: https://docs.dynatrace.com/managed/observe/digital-experience/session-segmentation/apdex-analysis
scraped: 2026-05-12T11:33:26.760447
---

# Анализ Apdex в контексте

# Анализ Apdex в контексте

* How-to guide
* 2-min read
* Published Jan 27, 2023

Dynatrace позволяет анализировать [Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") вашего приложения по различным измерениям. Вы можете проверить оценку Apdex для конкретного действия пользователя, местоположения и приложения, а также просмотреть оценку Apdex для каждого действия пользователя в рамках одной сессии.

## Анализ по местоположению

Используйте представление **World map**, доступное для [веб](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Узнайте, как представление World map предоставляет сведения об оценках Apdex, действиях пользователей, длительности действий и ошибках JavaScript."), [мобильных](/managed/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего мобильного приложения.") и [пользовательских приложений](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#geo-regions "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения."), чтобы просматривать цветовые оценки Apdex и другую информацию о производительности.

## Анализ по действиям пользователя

Для анализа удовлетворённости пользователей по конкретному действию:

1. Перейдите в **Web**, **Mobile** или **Custom Applications**.
2. Выберите приложение и прокрутите до раздела **Top 3 user actions** или **Top 3 actions**.
3. Выберите **View full details** или **Analyze performance**.
4. Найдите нужное действие пользователя и выберите его. Откроется страница сведений о действии пользователя. Оценка отображается на плитке **Apdex rating**.

## Анализ по приложению

Для просмотра динамики удовлетворённости пользователей во времени для конкретного приложения:

* **Веб-приложения**

  1. Перейдите в **Web**.
  2. Выберите плитку **Apdex rating** на инфографике. Вы также можете выбрать **Analyze Apdex** для получения более подробных сведений.

* **Мобильные приложения**

  [График **Apdex rating**](/managed/observe/digital-experience/mobile-applications/analyze-and-use/check-usage-metrics-mobile#apdex-rating "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего мобильного приложения.") доступен на странице обзора приложения.

* **Пользовательские приложения**

  Откройте [график **Apdex rating**](/managed/observe/digital-experience/custom-applications/analyze-and-use/check-usage-metrics-custom#apdex-rating "Узнайте, как использовать Dynatrace для проверки метрик пользовательского опыта вашего пользовательского приложения.") со страницы обзора приложения.

## Анализ пути пользователя между приложениями

Для анализа и понимания проблемных зон для каждого действия пользователя в пути пользователя:

1. На странице обзора приложения выберите **Analyze user sessions**, затем выберите сессию пользователя.

## Apdex для бизнес-отчётности

Вы можете выделить Apdex как ключевую метрику для коллег по бизнесу, добавив плитки с Apdex на дашборд Dynatrace.

## Связанные темы

* [Оценки Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Узнайте, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.")
* [Настройка Apdex для веб-приложений](/managed/observe/digital-experience/web-applications/additional-configuration/configure-apdex-web "Настройте пороговые значения удовлетворённости пользователей для вашего веб-приложения и его ключевых действий.")
* [Настройка Apdex для мобильных приложений](/managed/observe/digital-experience/mobile-applications/additional-configuration/configure-apdex-mobile "Настройте пороговые значения удовлетворённости пользователей для вашего мобильного приложения и его ключевых действий.")
* [Настройка Apdex для пользовательских приложений](/managed/observe/digital-experience/custom-applications/additional-configuration/configure-apdex-custom "Настройте пороговые значения удовлетворённости пользователей для вашего пользовательского приложения и его ключевых действий.")