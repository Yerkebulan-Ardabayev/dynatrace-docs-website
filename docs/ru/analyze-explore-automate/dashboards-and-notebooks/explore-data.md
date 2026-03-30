---
title: Изучение данных
source: https://www.dynatrace.com/docs/analyze-explore-automate/dashboards-and-notebooks/explore-data
scraped: 2026-03-06T21:10:58.587097
---

# Исследование данных

**Dashboards** и **Notebooks** предлагают:

* [Dynatrace Intelligence (ИИ)](#copilot) -- естественный язык для доступа к данным Grail.
* Интерфейс Explore для [логов](#explore-logs), [метрик](#explore-metrics) и [бизнес-событий](#explore-business-events).
* [DQL-запросы](#create-a-dql-query) для полной мощности Grail.

## Начало работы

1. Меню **Add** > выберите тип данных (Logs, Metrics, Business Events, Events, Problems, Traces, User sessions, Security events, User events).
2. Настройте фильтры: поле, оператор, значение. Комбинация `=` с `*` создает фильтры "начинается с", "заканчивается на", "содержит".
3. Нажмите **Run**.

Для сложных сценариев создайте DQL-запрос: меню > **Create DQL tile/section**.

## Переход на поля Smartscape

Поля `dt.entity.*` устарели. Используйте `dt.smartscape.*`. Обновите запросы и проверьте дашборды/ноутбуки.

## Prompt (ИИ)

### В дашборде

1. Меню **Add** > **Prompt**.
2. Введите запрос на естественном языке (например, `average cpu usage percentage by host`).
3. **Run** -- ИИ создаст и выполнит DQL-запрос.
4. Для редактирования: раскройте **DQL** или создайте DQL-плитку через меню.

### В ноутбуке

Аналогично. Меню **Add** > **Prompt** > ввод запроса > **Run**. Опция **Generate DQL only** для предпросмотра запроса.

**Auto select** визуализации: включите в правом верхнем углу панели настроек.

## Логи

1. Меню **Add** > **Logs** -- первые 20 строк логов.
2. Добавляйте фильтры через поле фильтра.

### Фильтрация

* **log.source**: `log.source = *oneagent*` -- логи с источником, содержащим "oneagent".
* **content**: `content = *crash*` -- логи с содержимым "crash".
* **status**: `status in (ERROR, WARN)` -- фильтр по нескольким статусам.

### Команды

* **Summarize** -- агрегация результатов по полю.
* **Convert to time series** -- преобразование в временной ряд для графиков.
* **Bucketize** -- группировка данных в корзины для гистограмм.
* **Sort** -- сортировка по полю.
* **Limit** -- ограничение количества записей.

## Метрики

1. Меню **Add** > **Metrics** > выберите метрику.
2. **Run** -- линейный график среднего значения.

### Команды метрик

* **Filters** -- фильтрация по полям (например, host.name).
* **Split by** -- агрегация по измерению (например, dt.entity.host).
* **Compare to previous period** -- сравнение с предыдущим периодом.
* **Default value** -- замена null значений.
* **Rate** -- скорость изменения (Per Second/Minute/Hour/Day).
* **Reduce to single value** -- свертка для визуализаций Single value, Table.
* **Alias** -- переименование метрики для читаемости.
* **Bucketize** -- группировка для гистограмм.
* **Expressions** -- арифметические операции над метриками (например, `A+B`).
* **Sort**, **Limit**, **Interval** -- глобальные команды.

## Бизнес-события

Аналогично логам. Меню **Add** > **Business Events**. Фильтрация по event.provider, event.type. Те же команды: Summarize, Convert to time series, Sort, Limit.

## Другие области

Events, Problems, Traces, User sessions, Security events, User events -- интерфейс аналогичен.

## Запросы к Grail

* **DQL** -- раскройте для просмотра автоматически созданного запроса.
* **Create DQL section/tile** -- создание DQL-секции/плитки для дальнейшего редактирования.
