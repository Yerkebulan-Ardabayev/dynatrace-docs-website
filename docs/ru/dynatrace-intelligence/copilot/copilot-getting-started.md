---
title: Начало работы с агентным и генеративным ИИ Dynatrace Intelligence
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/copilot-getting-started
scraped: 2026-03-06T21:13:25.807648
---

Агентный и генеративный ИИ включён на уровне учётной записи по умолчанию, но требует активации на уровне окружения.

## Включение генеративного ИИ

1. **Settings** > **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable generative AI**.

Если страница настроек не видна -- назначьте политики `Setting Reader` и `Setting Writer`.

### Разрешения пользователей

Привяжите группу к политике с разрешениями:
* `ALLOW davis-copilot:nl2dql:execute;` -- NL -> DQL
* `ALLOW davis-copilot:dql2nl:execute;` -- DQL -> NL
* `ALLOW davis-copilot:conversations:execute;` -- диалоговый рекомендатель

## Включение агентного ИИ для Dynatrace Assist

1. **Settings** > **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable generative AI** и **Enable agentic AI**.

Агентный Assist передаёт результаты вызовов инструментов корпоративным поставщикам LLM.

### Разрешения

Дополнительные разрешения для инструментов MCP -- см. [Инструменты MCP](../../../common/dynatrace-intelligence/dynatrace-intelligence-integrations/dynatrace-mcp.md#server).

### Маскирование PII

Агентный Assist не маскирует PII -- блокирует запросы с обнаруженными PII.

### Вызов инструментов

Максимум **10 внутренних инструментов MCP** за один ответ.

## Доступ к данным

ИИ учитывает разрешения пользователей -- разные пользователи получают разные ответы. Все вызовы выполняются в рамках пользовательских разрешений.

## Предложения документов

Рекомендация руководств по устранению неполадок из Notebooks/Dashboards на основе векторного сходства.

1. **Settings** > **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable document suggestions**.

Индексируются только документы, доступные всем пользователям. Индексация каждые 6 часов.

## Запросы с учётом окружения

Обогащение ИИ данными окружения для более точных запросов (сущности, события, метрики).

1. **Settings** > **Dynatrace Intelligence** > **Generative and agentic AI**.
2. Включите **Enable environment-aware queries**.

Построение индекса -- до 24 часов. Индекс хранится только на вашем тенанте.

### Настройка доступа к данным

**Configure data access** > **Add a new rule** > выберите тип и имя для исключения.

## Связанные темы

* FAQ
* Запросы на естественном языке
* Советы по промптам
