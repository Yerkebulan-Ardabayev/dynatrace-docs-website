---
title: Smartscape
source: https://www.dynatrace.com/docs/analyze-explore-automate/smartscape
scraped: 2026-03-01T21:20:36.536218
---

## Разрешения

| Разрешение | Назначение |
| --- | --- |
| storage:smartscape:read | Чтение данных Smartscape из Grail |
| storage:buckets:read | Чтение проблем из dt.davis.problems |
| storage:events:read | Запрос проблем |
| storage:filter-segments:read | Чтение сегментов фильтров |
| storage:metrics:read | Отображение метрик сущностей |
| storage:spans:read, storage:logs:read, storage:security.events:read, storage:bizevents:read, storage:entities:read | Чтение переменных сегментов |

## Начало работы

**Smartscape** -- интерактивная карта цифровой экосистемы на основе **Smartscape on Grail**. Визуализирует топологию и взаимосвязи между сущностями в реальном времени.

## Концепции

1. [Концепции Smartscape](smartscape/smartscape-concepts.md) -- основы UI и возможностей.
2. [Модальные окна Smartscape](smartscape/smartscape-modals.md) -- визуализация среды в любом приложении Dynatrace.
3. [Представления Smartscape](smartscape/smartscape-views.md) -- настраиваемые представления для анализа зависимостей.

## Сценарии использования

* **Smartscape on Grail** -- исследование всей экосистемы с унифицированной моделью.
* **Обзор облаков** -- топология AWS EC2 для анализа безопасности и оптимизации затрат.
* **Kubernetes** -- видимость кластеров, пространств имен, обнаружение ошибок конфигурации.
* **Граф проблем** -- определение первопричины и зоны поражения.
* **Граф зависимостей сервисов** -- отслеживание потоков вызовов, изоляция узких мест.
* **Инфраструктура** -- карта хостов, VM и сетевых взаимосвязей.
