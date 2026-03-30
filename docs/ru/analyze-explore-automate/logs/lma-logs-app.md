---
title: Приложение журналов
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-logs-app
scraped: 2026-03-06T21:09:41.161992
---

# Приложение Logs

### Разрешения

| Разрешение | Описание |
| --- | --- |
| storage:logs:read | Чтение логов (обязательно) |
| storage:buckets:read | Чтение логов (обязательно) |
| storage:files:read | Join с таблицами подстановок |
| storage:user.events:read | Чтение пользовательских событий |
| storage:spans:read | Чтение спанов (необязательно) |
| storage:bizevents:read | Бизнес-события (необязательно) |
| storage:metrics:read | Метрики (необязательно) |
| storage:events:read | События (необязательно) |
| storage:security.events:read | События безопасности (необязательно) |
| storage:user.sessions:read | Пользовательские сессии (необязательно) |

### Установка

Убедитесь, что приложение [установлено в вашей среде](../../manage/hub.md#install).

## Разделы

1. [Запросы и фильтрация логов](lma-logs-app/query-and-filter.md)
2. [Диаграмма распределения логов](lma-logs-app/log-distribution-chart.md)
3. [Окружающие логи](lma-logs-app/surrounding-logs.md)
4. [Фильтрация фасетами](lma-logs-app/facets.md)
5. [Настройка сообщения лога](lma-logs-app/message.md)
6. [Ограничения](lma-logs-app/limits.md)

## О приложении

**Logs** -- отправная точка для поиска записей логов без написания запросов:

* **Фильтрация** без DQL для поиска нужных записей.
* **Проактивное расследование** через диаграмму распределения логов.
* **Контекст первопричин** -- окружающие логи на основе трейсов и источника.
* **Расширение анализа** -- переход к связанным хостам, кластерам K8s, трейсам.
* **Обмен результатами** -- продолжение работы в Notebooks, Dashboards, Investigations, Workflows.

## FAQ

**Редактирование DQL-запроса:** выберите **Edit DQL query** в меню рядом с **Run query**.

**Лицензирование:** запросы тарифицируются по объему запрошенных данных. Бесплатно: фасеты, подсказки, диаграмма распределения, поиск по результатам. Лицензия расходуется при **Run query** и **Surrounding logs**.

**Доступ:** требуется доступ к Dynatrace Platform и логам в Grail ([политики доступа](../../platform/upgrade.md#built-in-policies)).
