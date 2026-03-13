---
title: RUM metrics migration
source: https://www.dynatrace.com/docs/analyze-explore-automate/metrics/upgrade/rum-metric-migration
scraped: 2026-03-05T21:37:58.010413
---

# Миграция метрик RUM

# Миграция метрик RUM

* Latest Dynatrace
* Reference
* 5-min read
* Updated on Jan 23, 2026

Ищете документацию по метрикам нового RUM Experience?

Вы можете получить доступ к полному списку доступных метрик и их описаний непосредственно в последней версии Dynatrace. Нажмите **CTRL**/**CMD**+**K**, введите `dt.frontend` и выберите **Show more**.

[Новый RUM Experience](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance."), который переносит RUM в Grail, вводит многочисленные встроенные метрики с префиксом `dt.frontend`. Поскольку используется другая модель данных, в отличие от RUM Classic, прямых эквивалентов [метрикам RUM Classic](/docs/analyze-explore-automate/metrics-classic/built-in-metrics#applications "Explore the complete list of built-in Dynatrace metrics.") с префиксом `builtin:apps` не существует. Тем не менее многие метрики имеют замены, выполняющие аналогичную функцию, как показано в таблице ниже. Обратите внимание, что метрики с префиксом `builtin:apps`, отсутствующие в таблице, замен не имеют.

Различия в значениях метрик между метриками `builtin:apps` и их заменами ожидаемы и обусловлены изменениями в базовой модели данных.

## Связанные темы

* [Новый опыт Real User Monitoring](/docs/observe/digital-experience/new-rum-experience "Discover the New RUM Experience for unmatched visibility into user behavior and frontend performance.")
