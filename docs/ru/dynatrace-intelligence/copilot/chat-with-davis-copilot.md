---
title: Dynatrace Assist
source: https://www.dynatrace.com/docs/dynatrace-intelligence/copilot/chat-with-davis-copilot
scraped: 2026-03-06T21:33:52.070519
---

**Dynatrace Assist** -- чат с Dynatrace Intelligence для вопросов о данных среды и общих вопросов по Dynatrace.

## Разрешения

Для генеративного ИИ:
* `document:documents:write/read/delete` -- работа с диалогами
* `davis-copilot:conversations:execute` -- функция диалогов
* `hub:catalog:read` -- каталог приложений

Для агентного режима дополнительно:
* `davis-copilot:nl2dql:execute`, `davis-copilot:dql2nl:execute`
* `mcp-gateway:servers:invoke/read`
* `davis:analyzers:read`

См. [Агентные разрешения](copilot-getting-started.md#assist-agentic).

## Начало работы

1. Выберите **Dynatrace Assist** (значок под кнопкой **Поиск**).
2. Введите вопрос, нажмите **Run**.
3. Уточняющие вопросы доступны. Диалоги сохраняются автоматически.

Ответы генерируются на основе официальных источников: документация, Developer, Community, Hub, новости и веб-сайт Dynatrace.

### Агентные возможности

При включённом агентном ИИ -- анализ данных и безопасности среды. См. [Включение агентного ИИ](copilot-getting-started.md#assist-agentic).

### Обратная связь

Используйте кнопки оценки ответов. Обратная связь не используется для обучения моделей -- только для мониторинга качества командой продукта.

## Сценарии использования

* Общие вопросы о Dynatrace.
* Использование инструментов и возможностей MCP.
* Выполнение задач без переключения между приложениями.
* Комбинирование инструментов в одном запросе.

## Связанные темы

* Начало работы с агентным и генеративным ИИ
* Встроенные стартеры диалогов
* FAQ
* Dynatrace MCP server
