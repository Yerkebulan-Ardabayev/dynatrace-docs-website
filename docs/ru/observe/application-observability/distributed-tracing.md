---
title: Distributed Tracing
source: https://www.dynatrace.com/docs/observe/application-observability/distributed-tracing
scraped: 2026-03-06T21:09:46.417540
---

## Предварительные требования

* Подписка Dynatrace Platform Subscription (DPS).

### Разрешения

| Разрешение | Описание |
|---|---|
| storage:buckets:read | Чтение бакетов |
| storage:spans:read | Чтение спанов |
| storage:entities:read | Чтение сущностей |
| storage:logs:read | Чтение логов |
| state:user-app-states:read/write/delete | Состояние пользователя |
| storage:fieldsets:read | Маскированные поля |
| storage:filter-segments:read | Сегменты фильтрации |
| storage:smartscape:read | Узлы и связи Smartscape |

Убедитесь, что приложение [установлено](../../manage/hub.md#install).

## Начало работы

Distributed Tracing на базе Grail обеспечивает приём и обработку петабайтов данных трассировки для отслеживания ошибок и проблем производительности в распределённых системах. Данные хранятся в Grail и доступны через приложение и DQL.

## Учебные модули

1. [Анализ исключений](distributed-tracing/exception-analysis.md)
2. [Приём трассировок](distributed-tracing/ingest-traces.md) — инструментация через OneAgent или OpenTelemetry.
3. [Настройка разрешений Grail](distributed-tracing/permissions.md)
4. [Хранение и удержание данных](distributed-tracing/storage.md)
5. [Распространение контекста спана и трассировки](distributed-tracing/tracking-transactions.md)
6. [Трассировки, DQL и логи для выявления закономерностей](distributed-tracing/use-traces-and-dql-to-spot-patterns.md)
7. [Приложение Distributed Tracing](distributed-tracing/distributed-tracing-app.md)
8. [Расширенная аналитика на Grail](distributed-tracing/advanced-tracing-analytics.md)

## Концепции

### Распределённая трассировка

Последовательность спанов с уникальным trace ID, отслеживающая путь запроса через сервисы и компоненты. Помогает выявлять узкие места, ошибки и проблемы задержки.

### Спан

Отдельная операция в трассировке. Атрибуты: имя, метка времени, события (исключения), идентификатор родителя, тип. Спан без родителя — корневой спан (начало трассировки).

Контекст распространяется через HTTP-заголовки (W3C trace context) или идентификаторы в системах обмена сообщениями. См. [Распространение контекста](distributed-tracing/tracking-transactions.md).

### Атрибут

Пары ключ-значение с деталями о спане/запросе/ресурсе (коды ответа, HTTP-методы, URL). Используются для группировки, запросов и анализа трассировок.

Dynatrace использует атрибуты для: обнаружения и именования сервисов, построения топологии Smartscape, связывания логов с трассировками, анализа таймингов спанов.

### Сервис

Сервисы определяются и именуются на основе атрибутов спанов. Экземпляры сервиса обрабатывают отдельные спаны.

### Сбор данных

Используйте OneAgent или OpenTelemetry (или оба) для сбора трассировок. Trace ID распространяется по приложениям и микросервисам.

## Сценарии использования

* Устранение неполадок: причины сбоев запросов.
* Оптимизация производительности: узкие места и задержки.
* Детальный анализ отдельных трассировок.
* Исследовательский анализ неизвестных проблем.
* Синтез трассировок с логами, событиями и метриками.

## FAQ

* **"The new tracing experience is coming soon"** — поэтапное развёртывание до марта 2025.
* **Классические представления?** Да, Distributed Traces Classic работает параллельно.
* **Лицензия?** DPS FullStack и/или Custom Traces Classic. Дополнительных расходов нет.
* **Сброс фасетов?** **Distributed Tracing** > **Show facets** > **Reset to default**.
* **Нулевые span.kind?** Обновите OneAgent.
* **Неполные трассировки?** Обновите OneAgent и включите **Forward Tag 4 trace context extension**.
* **Фильтр по источнику?** Фасет `span source`.
* **Межсредовая трассировка?** Пока не поддерживается.

## Связанные темы

* Dynatrace Query Language
* Dynatrace Grail
* Распространение контекста спана и трассировки
