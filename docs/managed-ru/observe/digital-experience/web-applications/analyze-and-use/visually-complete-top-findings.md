---
title: Топ результатов Visually complete
source: https://docs.dynatrace.com/managed/observe/digital-experience/web-applications/analyze-and-use/visually-complete-top-findings
scraped: 2026-05-12T11:34:57.375404
---

# Топ результатов Visually complete

# Топ результатов Visually complete

* Overview
* 2-min read
* Published Jul 05, 2019

Dynatrace упрощает специалистам по оптимизации веб-производительности доступ к результатам метрики Visually complete для каждой загрузки страницы, захватываемой Dynatrace Real User Monitoring. Измерения Visually complete легко понять: они измеряют время, необходимое для полной отрисовки видимой части веб-приложения на экранах устройств конечных пользователей. Анализ метрики пользовательского опыта Visually complete помогает понять, что можно сделать для улучшения опыта пользователей с видимой без прокрутки частью приложения. Однако оптимизация приложения для Visually complete требует глубокого понимания поведения загрузки веб-страниц. Именно здесь незаменим [анализ водопада](/managed/observe/digital-experience/web-applications/analyze-and-use/waterfall-analysis "Learn how to analyze all user action monitoring data through waterfall analysis.") Dynatrace.

## Результаты Visually complete

Плитка топ результатов **Visually complete** помогает сфокусировать анализ водопада на тех ресурсах страницы, которые влияют на пользовательский опыт видимой без прокрутки части. Она также даёт быстрое указание на то, были ли превышены пороговые значения производительности. Вверху отображается последний DOM-элемент (и идентификатор DOM-элемента), влияющий на тайминг Visually complete для водопада, захваченного на реальном устройстве с реальным размером экрана. Как видно на изображении ниже, CSS и JavaScript файлы не выделяются как влияющие ресурсы, поскольку это нельзя определить наверняка. При оптимизации видимой без прокрутки области необходимо также рассматривать эти ресурсы, так как они могут видимым образом изменять DOM-элементы, не привязанные к ресурсному запросу. В примере ниже конечным триггером для Visually complete является простой тег SPAN, а не ресурс.

Как видно из примера ниже, топ результатов также может содержать предупреждения. В этом примере отображаются два предупреждения. Ниже изображения описаны оба типа результатов.

![Waterfall analysis](https://dt-cdn.net/images/waterfall-with-visually-complete-top-finding-1968-796ce96ee6.png)

Waterfall analysis

## Топ результат #1: Visually complete (нарушение Apdex и ключевой метрики производительности)

Первое предупреждение определяется пороговым значением, установленным для [ключевой метрики производительности](/managed/observe/digital-experience/rum-concepts/user-action-metrics#kpm "Learn what metrics Dynatrace calculates for user actions and find out what each metric indicates.") и [Apdex](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance.") приложения. Можно [изменить эту настройку](/managed/observe/digital-experience/rum-concepts/scores-and-ratings/apdex-ratings#key-user-actions "Learn how Dynatrace uses Apdex to measure user satisfaction with application performance."), перейдя в настройки отслеживаемого приложения (см. пример ниже). Изменение порогового значения напрямую влияет не только на топ результаты, но и на расчёт Apdex для приложения во всех представлениях Dynatrace, включая [карту мира](/managed/observe/digital-experience/web-applications/analyze-and-use/world-map-view "Learn how the World map view offers insights into Apdex ratings, user actions, action durations, and JavaScript errors."), [обзор приложения](/managed/observe/digital-experience/web-applications/analyze-and-use/introduction-to-application-overview "Read an overview of the analysis options offered on the application overview page.") и другие.

![Waterfall analysis](https://dt-cdn.net/images/application-apdex-settings-2019-e830c18ed8.png)

Waterfall analysis

## Топ результат #2: Speed index превышает определённый процент от тайминга Visually complete

Второй порог связан с [метриками Speed index и Visually complete](/managed/observe/digital-experience/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Learn how to use 'Visually complete' and 'Speed index' metrics.") и их соотношением. Visually complete указывает момент полной отрисовки видимой без прокрутки области, тогда как Speed index помогает понять, насколько быстро загружаются наибольшие части экрана. Чем больше разница между Speed index и таймингом Visually complete, тем лучше. Для удобства Dynatrace предупреждает, если Speed index составляет 50% или более от Visually complete. Этот порог можно изменить по мере улучшения производительности при необходимости более строгих ограничений.