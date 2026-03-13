---
title: Accelerate root cause analysis
source: https://www.dynatrace.com/docs/secure/investigations/accelerate-root-cause-analysis
scraped: 2026-03-04T21:36:21.144114
---

# Ускорение анализа первопричин

# Ускорение анализа первопричин

* Последняя версия Dynatrace
* Практическое руководство
* Опубликовано 27 августа 2025 г.

Это руководство знакомит с расширенными возможностями, предназначенными для улучшения анализа первопричин и оптимизации рабочих процессов расследования в ![Investigations](https://dt-cdn.net/images/security-investigator-256-93f6c187d9.png "Investigations") **Investigations** — будь то устранение инцидентов, анализ проблем с производительностью или расследование угроз.

В настоящее время доступны следующие функции (скоро появятся новые).

### Обогащение IP-адресов

Добавляйте внешние данные репутации к IP-адресам с помощью надёжных источников разведки угроз, таких как AbuseIPDB или VirusTotal. Обогащение можно применять вручную к отдельным IP-адресам или автоматически к записям в списке доказательств, что позволяет ускорить сортировку и провести более глубокий контекстный анализ.

* [Подробнее: Enrich IP addresses](/docs/secure/investigations/enhance-results#enrich "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Использование опорной временной метки

Сравнивайте и коррелируйте события в разных временных периодах с помощью опорной временной метки. Это помогает измерять временные смещения между событиями и ключевыми моментами инцидента. Виртуальный столбец отображает разницу во времени, которую можно использовать для более точной фильтрации и корреляции данных в дереве запросов.

* [Подробнее: Set the reference time](/docs/secure/investigations/define-timeframes#reference "Adjust time ranges for data analysis and event correlation in Investigations.")

### Сводные запросы (Pivot queries)

Быстро переходите к связанным данным, создавая сводные запросы из любой записи на основе доступных измерений. Это формирует новый узел запроса с охватом ±5 минут вокруг выбранного события, выявляя связи и закономерности без ручного составления запросов.

* [Подробнее: Pivot results](/docs/secure/investigations/enhance-results#pivot "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

### Корреляция с метриками производительности

Коррелируйте записи журналов с показателями производительности системы, такими как использование CPU, памяти или сети. Динамический график отображает данные метрик вокруг выбранной временной метки журнала, помогая аналитикам оценить влияние и точнее установить первопричины.

* [Подробнее: Correlate logs with performance metrics](/docs/secure/investigations/enhance-results#metrics "Organize and interpret query outputs across investigations --- from performance analysis to threat detection.")

## Связанные темы

* [Threat hunting and forensics](/docs/secure/use-cases/threat-hunting "Use case scenario for threat hunting and forensics with Investigations.")
* [DPL Architect](/docs/platform/grail/dynatrace-pattern-language/dpl-architect "Extract fields with Dynatrace Pattern Language Architect.")
* [Notebooks](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability data—all in one collaborative, customizable workspace.")
* [Dynatrace Query Language](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.")
* [Use DQL queries](/docs/platform/grail/dynatrace-query-language/dql-guide "Find out how DQL works and what are DQL key concepts.")
* [DQL commands](/docs/platform/grail/dynatrace-query-language/commands "A list of DQL commands.")
* [DQL functions](/docs/platform/grail/dynatrace-query-language/functions "A list of DQL functions.")
* [DQL operators](/docs/platform/grail/dynatrace-query-language/operators "A list of DQL Operators.")
* [DQL data types](/docs/platform/grail/dynatrace-query-language/data-types "A list of DQL data types.")
* [Conversion and casting functions](/docs/platform/grail/dynatrace-query-language/functions/conversion-and-casting-functions "A list of DQL conversion and casting functions.")
* [DQL selection and modification commands](/docs/platform/grail/dynatrace-query-language/commands/selection-and-modification-commands "DQL selection and modification commands")
