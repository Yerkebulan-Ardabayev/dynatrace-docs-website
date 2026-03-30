---
title: Рабочие процессы
source: https://www.dynatrace.com/docs/analyze-explore-automate/workflows
scraped: 2026-03-06T21:15:26.954952
---

# Workflows

**Workflows** -- инструмент автоматического реагирования на данные мониторинга. Не предназначен для массового приема/экспорта данных (используйте OpenPipeline или Dynatrace Extensions).

### Разрешения

| Разрешение | Описание |
| --- | --- |
| automation:workflows:read | Чтение workflow |
| automation:workflows:admin | Администрирование workflow и выполнений |
| automation:rules:read/write | Правила планирования |
| automation:calendars:read/write | Бизнес-календари |
| app-engine:apps:run | Просмотр приложений |
| app-engine:functions:run | Запуск function-executor |
| hub:catalog:read | Чтение Hub |
| document:documents:read | Чтение шаблонов workflow |

Полный список разрешений: **Hub** > **Workflows** > **Technical information**.

### Установка

Убедитесь, что приложение [установлено](../manage/hub.md#install).

## Основные концепции

* **Workflow** -- повторяемый процесс из последовательности задач с переходами (последовательно, параллельно, условно). Редактируется в визуальном графе.
* **Простой workflow** -- одна задача, ограниченная функциональность, не потребляет часы workflow.
* **Задача** -- единица работы (например, Create Incident, Notify Ops in Slack) с условиями, повторами, тайм-аутами и входной конфигурацией.
* **Действие** -- универсальная функция, выполняемая задачами. Предоставляются Dynatrace и партнерами через Hub.
* **Выполнение** -- конкретный экземпляр прохождения workflow. Запускается по расписанию, по событиям или вручную.

## Просмотр выполнений

Выберите **Executions** в заголовке Workflows. Фильтры: Keyword, Workflow, Execution state, Trigger type, Timeframe.

## EdgeConnect

Позволяет проксировать HTTP-запросы через EdgeConnect к непубличным сервисам. Настройка: см. Настройка и развертывание EdgeConnect.

## Сценарии использования

* Агентные workflow
* Автоматическое реагирование на события Dynatrace Intelligence
* Планирование отчетов с учетом праздников
* Оркестрация ИТ-процессов
* Подключение к облачным и локальным сервисам
* Комбинирование интеграций с пользовательским кодом
* Мониторинг в реальном времени и аудиторский след

## Учебные модули

1. Краткое руководство по Workflows
2. Создание workflow
3. Создание простого workflow
4. Триггеры workflow
5. Запуск и мониторинг workflow
6. [Пользовательские разрешения](workflows/security.md)
7. [Действия Workflows](workflows/default-workflow-actions.md)
8. [Коннекторы Workflows](workflows/actions.md)
9. Управление workflow
10. Справочник по выражениям
11. [Сценарии использования](workflows/use-cases.md)
