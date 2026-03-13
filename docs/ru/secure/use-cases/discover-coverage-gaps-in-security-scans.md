---
title: Discover coverage gaps in security findings
source: https://www.dynatrace.com/docs/secure/use-cases/discover-coverage-gaps-in-security-scans
scraped: 2026-03-06T21:15:11.474257
---

# Discover coverage gaps in security findings

# Обнаружение пробелов в покрытии проверками безопасности

* Latest Dynatrace
* Tutorial
* Updated on Sep 30, 2025

В процессе жизненного цикла разработки программного обеспечения (SDLC) различные инструменты сканируют артефакты по мере их прохождения через этапы разработки. Артефакт, например образ контейнера, достигает этапа развёртывания и в итоге представляет ваши работающие приложения. На этом этапе вы хотите быть уверены, что артефакты прошли надлежащие процедуры проверки безопасности и не пропустили никакую обязательную валидацию.

Получить полную видимость цикла валидации непросто, так как продукты сканирования, используемые разными командами, изолированы друг от друга.

В этом контексте вы можете:

* Агрегировать результаты проверок безопасности для развёрнутых и работающих артефактов.
* Получить полную видимость проверок безопасности, которые эти артефакты прошли перед достижением вашей производственной среды.
* Обнаруживать пробелы в ваших процедурах безопасности и устранять их до того, как они станут реальным риском.
* Визуализировать результаты проверок безопасности в разных продуктах и инструментах с помощью наших образцов дашбордов, которые также могут стать хорошей основой для дальнейшей визуальной настройки под требования вашей организации к анализу и отчётности по безопасности.

## Целевая аудитория

Архитекторы и менеджеры по безопасности, ответственные за соответствие процедур сканирования безопасности стандартам безопасности.

Ключевые варианты использования включают:

* Получение обзора выполненных оценок безопасности
* Выявление пробелов в покрытии
* Определение наиболее значимых продуктов и их ROI

## Предварительные требования

[Загрузите результаты проверок безопасности](/docs/secure/threat-observability/security-events-ingest "Ingest external security data into Grail.") из вашего стороннего продукта.

## Начало работы

1. Визуализация

1. Откройте [![Dashboards](https://dt-cdn.net/images/dashboards-512-b1f1e9690b.png "Dashboards") **Dashboards**](/docs/analyze-explore-automate/dashboards-and-notebooks/dashboards-new "Create interactive, customizable views to visualize, analyze, and share your observability data in real time.") и перейдите в раздел **Ready-made**.
2. Найдите и выберите **Security product coverage** для нужной интеграции.

Пример результата:

![dashboard sample result](https://dt-cdn.net/images/2025-05-07-13-27-38-1905-24ee0d41ed.png)

2. Анализ

Откройте [![Notebooks](https://dt-cdn.net/images/notebooks-768-046137830a.webp "Notebooks") **Notebooks**](/docs/analyze-explore-automate/dashboards-and-notebooks/notebooks "Analyze, visualize, and share insights from your observability data — all in one collaborative, customizable workspace.") для [выполнения запросов](/docs/platform/grail/dynatrace-query-language "How to use Dynatrace Query Language.") к результатам проверок безопасности, используя формат данных из [Semantic Dictionary](https://dt-url.net/3q03pb0).

Для лучшего понимания того, как строить запросы, см. раздел [Примеры DQL-запросов для принятых событий](/docs/secure/threat-observability/dql-examples#ingested "DQL examples for security data powered by Grail.").
