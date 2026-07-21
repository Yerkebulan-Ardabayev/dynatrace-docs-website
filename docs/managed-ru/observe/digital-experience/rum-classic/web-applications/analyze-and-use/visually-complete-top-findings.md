---
title: Визуальное завершение: ключевые находки в RUM Classic
source: https://docs.dynatrace.com/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/visually-complete-top-findings
---

# Визуальное завершение: ключевые находки в RUM Classic

# Визуальное завершение: ключевые находки в RUM Classic

* Обзор
* Чтение за 2 минуты
* Опубликовано 05 июля 2019 г.

Dynatrace упрощает доступ к находкам по метрике Visually complete для каждой загрузки страницы, зафиксированной с помощью Dynatrace Real User Monitoring Classic, для тебя и твоих инженеров по оптимизации веб-производительности. Измерения Visually complete легко понять: они показывают, сколько времени требуется, чтобы видимая часть веб-приложения полностью отрисовалась на экране устройства конечного пользователя. Анализ метрики пользовательского опыта Visually complete помогает понять, что можно сделать для улучшения опыта конечных пользователей в верхней части экрана (above the fold) приложения. Однако оптимизация приложения по метрике Visually complete требует глубокого понимания поведения загрузки веб-страницы. Именно здесь незаменим Dynatrace [анализ waterfall](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/waterfall-analysis "Узнай, как анализировать все данные мониторинга действий пользователя с помощью анализа waterfall.").

## Находки по Visually complete

Плитка ключевых находок **Visually complete** помогает сфокусировать анализ waterfall на тех ресурсах страницы, которые влияют на пользовательский опыт в верхней части экрана. Она также быстро показывает, были ли нарушены какие-либо пороги производительности. Сверху отображается последний DOM-элемент (и идентификатор DOM-элемента), влияющий на время Visually complete для waterfall, зафиксированного на конкретном реальном устройстве и при конкретном размере экрана. Как видно на изображении ниже, CSS-файлы и JavaScript-файлы не выделяются как влияющие ресурсы, поскольку это невозможно определить с уверенностью. При оптимизации области above the fold нужно обращать внимание и на эти ресурсы, так как они могут визуально изменять DOM-элементы, не привязанные к запросу ресурса. В примере ниже финальным триггером для Visually complete становится простой тег SPAN, а не ресурс.

Как видно в примере ниже, ключевые находки могут также включать предупреждения. В этом примере отображаются два предупреждения. Пояснения к этим двум типам находок приведены под изображением.

![Анализ waterfall](https://dt-cdn.net/images/waterfall-with-visually-complete-top-finding-1968-796ce96ee6.png)

Анализ waterfall

## Находка №1: Visually complete (нарушение Apdex и ключевой метрики производительности)

Первое предупреждение определяется порогом, заданным для [ключевой метрики производительности](/managed/observe/digital-experience/rum-classic/rum-concepts/user-action-metrics#kpm "Узнай, какие метрики Dynatrace рассчитывает для действий пользователя, и выясни, что означает каждая метрика.") и [Apdex](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings "Узнай, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") приложения. [Этот параметр можно изменить](/managed/observe/digital-experience/rum-classic/rum-concepts/scores-and-ratings/apdex-ratings#key-user-actions "Узнай, как Dynatrace использует Apdex для измерения удовлетворённости пользователей производительностью приложения.") в настройках этого отслеживаемого приложения (см. пример ниже). Изменение порога напрямую влияет не только на ключевые находки, но и на расчёт показателя Apdex для приложения во всех представлениях Dynatrace, включая [карту мира](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/world-map-view "Узнай, как представление карты мира даёт сведения об оценках Apdex, действиях пользователя, длительности действий и ошибках JavaScript."), [обзор приложения](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/introduction-to-application-overview "Ознакомься с обзором вариантов анализа, доступных на странице обзора приложения.") и другие.

![Анализ waterfall](https://dt-cdn.net/images/application-apdex-settings-2019-e830c18ed8.png)

Анализ waterfall

## Находка №2: Speed index превышает процент от времени Visually complete

Второй порог связан с метриками [Speed index и Visually complete](/managed/observe/digital-experience/rum-classic/web-applications/analyze-and-use/how-to-use-visually-complete-and-speed-index-metrics "Узнай, как использовать метрики 'Visually complete' и 'Speed index'.") и с тем, как они соотносятся друг с другом. Visually complete показывает, когда область above the fold полностью отрисована, а Speed index помогает понять, насколько быстро загружаются самые большие области экрана. Чем больше разница между временем Speed index и Visually complete, тем лучше. Чтобы дать простой индикатор, Dynatrace предупреждает, если Speed index составляет 50% или более от Visually complete. Этот порог можно менять по мере улучшения производительности, когда потребуются более строгие ограничения.