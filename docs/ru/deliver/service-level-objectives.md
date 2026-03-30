---
title: Цели уровня обслуживания
source: https://www.dynatrace.com/docs/deliver/service-level-objectives
scraped: 2026-03-06T21:30:36.060105
---

# Service-Level Objectives

## Предварительные требования

### Разрешения

| Scope | Описание |
| --- | --- |
| `slo:slos:read` | Чтение SLO |
| `slo:slos:write` | Запись SLO |
| `slo:objective-templates:read` | Чтение шаблонов |
| `storage:buckets:read` | Чтение данных из Grail |
| `storage:logs:read` | Чтение логов |
| `storage:metrics:read` | Чтение метрик |
| `storage:bizevents:read` | Чтение бизнес-событий |
| `storage:events:read` | Чтение событий |
| `storage:security.events:read` | Чтение событий безопасности |
| `storage:user.events:read` | Чтение пользовательских событий |

### Установка

Убедитесь, что приложение [установлено в вашей среде](../manage/hub.md#install).

## Что такое SLO?

**SLO (Service-Level Objective)** — цель, определяющая минимально допустимый уровень обслуживания за определённый период.

Компоненты SLO:

* **SLI (Service-Level Indicator)** — количественная мера (0-100%), вычисляемая DQL-запросом.
* **Целевое значение** — например, 99.99% запросов без ошибок.
* **Период оценки** — временной интервал для измерения.
* **Статус SLO** — агрегированное значение SLI за период.

### SLO в Dynatrace

Обзорная страница показывает: имя, целевое значение, предупреждение, период оценки, действия. Выберите SLO для просмотра статуса (график/таблица), критических сервисов, критериев и метаданных.

### Бюджет ошибок

Разница между статусом SLO и пороговым значением. Пример: SLO доступности 95%, текущий статус 96% — оставшийся бюджет 1%.

### Скорость сжигания бюджета ошибок

Формула: `burn rate = error rate / error budget over the look-back window size`

Высокая скорость указывает на аномальное потребление бюджета.

## Мониторинг скорости сжигания

### Расчёт через DQL

Добавьте строку к SLI:

```
| fieldsAdd sli = "YOUR SLI"
| fieldsAdd target= "YOUR SLO-target" in percentage
| fieldsAdd burnRate = ((100 - sli[]) / (100 - target))
| fieldsRemove sli
```

Для агрегированного значения:

```
| fieldsAdd burnRate = ((100 - sli[]) / (100 - target))
| summarize sloBurnRate = avg(burnRate[]), timeframe = takeFirst(timeframe), interval = takeFirst(interval)
```

### Оповещения через Anomaly Detection

1. Введите SLI как DQL-запрос в Anomaly Detection.
2. Добавьте расчёт скорости сжигания.
3. Рекомендуемый порог: 10-14 при окне -1ч.

Рекомендуемые свойства событий:
* `dt.source entity` — затронутые сущности
* `event.type` — `ERROR_EVENT`, `AVAILABILITY_EVENT` или `PERFORMANCE_EVENT`
* `slo.name` — имя SLO
* `dt.owner` — ID команды для маршрутизации оповещений

## Обучающие модули

1. [Создание SLO](service-level-objectives/create-slo.md)
2. [Добавление SLO на дашборд](service-level-objectives/service-level-objective-tile-add-to-dashboard.md)
3. [Редактирование плитки SLO](service-level-objectives/service-level-objective-tile-edit-in-dashboard.md)
4. [Просмотр деталей плитки SLO](service-level-objectives/service-level-objective-tile-view.md)
5. [Разрешения для плиток SLO](service-level-objectives/service-level-objective-permissions.md)
6. Шаблоны SLO
7. Примеры SLO
8. [Обновление классических SLO](service-level-objectives/service-level-objective-upgrade-classic.md)
