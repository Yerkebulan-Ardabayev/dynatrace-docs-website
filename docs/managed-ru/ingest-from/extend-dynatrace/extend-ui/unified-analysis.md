---
title: Страницы унифицированного анализа
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis
---

# Страницы унифицированного анализа

# Страницы унифицированного анализа

* Overview
* 4-min read
* Published Mar 09, 2023

Dynatrace страницы унифицированного анализа объединяют все данные наблюдаемости и необходимые аналитические инструменты для эффективного анализа и устранения неполадок в едином контексте. При изучении метрик, событий, логов и метаданных проблемного объекта конкретного домена на одной странице доступны все сигналы наблюдаемости, связанные с этим объектом.

[Страница обзора хоста](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Мониторинг хостов с Dynatrace.") является примером страницы унифицированного анализа, доступной в большинстве сред.

## Типы страниц

Существует два типа страниц унифицированного анализа:

* **List page**  
  List page генерируется автоматически и позволяет просматривать все экземпляры объектов конкретного типа. Доступные настройки описаны в разделе [List settings](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-settings "Подробнее о синтаксисе unified analysis.").
* **Details page**  
  Details page объединяет в едином контексте все сигналы наблюдаемости, привязанные к объекту. Как и List page, Details page генерируется автоматически для каждого объекта в среде. Доступные настройки описаны в разделе [Details settings](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-settings "Подробнее о синтаксисе unified analysis.").

## Карточки

На странице объекта можно определить карточки различных типов.

### Chart group

Компонент chart group используется для группировки настроенных графиков в сетку. Подробности конфигурации см. в разделе [Chart group cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#chart-group-cards "Подробнее о синтаксисе unified analysis.").

### Тип графика

Доступны следующие типы графиков (задаются полем `visualizationType`).

* **Graph chart:**

  ![Пример chart group](https://dt-cdn.net/images/chart-group-1169-76d6ed5a9e.png)

  Пример chart group
* **Pie chart:**

  ![Pie chart](https://dt-cdn.net/images/pie-chart-519-7780ea60ce.png)

  Pie chart
* **Single value:**

  ![Single value](https://dt-cdn.net/images/single-value-550-35129a06f1.png)

  Single value

### Entity list

Карточка entity list используется для отображения объектов одного типа, их атрибутов и связанных объектов в одной таблице.

Подробности конфигурации см. в разделе [Entities list cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#entities-list-cards "Подробнее о синтаксисе unified analysis.").

![Пример entity list](https://dt-cdn.net/images/a84b28ad-48ba-40b6-b83e-c2962c2d2f86-1423-5c0e42d7a4.png)

Пример entity list

### Metric table

Карточка metric table используется для отображения нескольких метрик в одной таблице.

Подробности конфигурации см. в разделе [Metric table cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#metric-table-cards "Подробнее о синтаксисе unified analysis.").

![Metric table card](https://dt-cdn.net/images/7dc47e10-5c1f-494d-bb1c-865fec747246-1598-1442ff2964.png)

Metric table card

### Properties

Карточка properties используется для отображения атрибутов и тегов. По умолчанию отображаются все атрибуты из [Monitored entities API](/managed/dynatrace-api/environment-api/entity-v2 "Подробнее о Dynatrace Monitored entities API."). Дополнительную информацию см. в разделе [Notifications bar](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring#notifications-bar "Мониторинг хостов с Dynatrace.").

Подробности конфигурации см. в разделе [Properties cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#properties-cards "Подробнее о синтаксисе unified analysis.").

![Пример Properties card](https://dt-cdn.net/images/properties-528-184d1764f0-528-10fef21345.png)

Пример Properties card

### Logs

Карточка logs, функционально идентичная [Log viewer](/managed/analyze-explore-automate/log-monitoring/analyze-log-data/log-viewer "Как использовать Log viewer Dynatrace для анализа данных логов."), отображает столбчатую диаграмму с частотой появления логов за выбранный период и детальную таблицу, где каждый лог представлен записью с дополнительными свойствами: временной меткой, статусом и содержимым.

Подробности конфигурации см. в разделе [Logs cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#logs-cards "Подробнее о синтаксисе unified analysis.").

![logs-card](https://dt-cdn.net/images/screenshot-2023-03-14-at-10-16-08-624-bf7cf1200b.png)

logs-card

### Messages

Карточка message используется для отображения информации при выполнении определённого условия. Подробности конфигурации см. в разделе [Message cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#message-cards "Подробнее о синтаксисе unified analysis."). Существует два типа визуализации карточки message:

* **Message**, карточка, отображающая только текстовую информацию.
* **Card**, карточка с заголовком, описанием и доступными действиями.

Например, message card можно отображать, если OneAgent не развёрнут:

![Пример Message card](https://dt-cdn.net/images/screenshot-from-2022-02-02-11-45-21-2531-4541e56bf6.png)

Пример Message card

### Events

Карточка events используется для отображения событий, связанных с указанными объектами.

Подробности конфигурации см. в разделе [Events cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#events-cards "Подробнее о синтаксисе unified analysis.").

![Пример Events card](https://dt-cdn.net/images/screenshot-2023-03-14-at-14-12-35-571-7d4521137a.png)

Пример Events card

### Health

Карточка health используется для визуального отображения конкретных метрик. По умолчанию предоставляется быстрый обзор из до шести отдельных плиток, каждая из которых представляет уникальную метрику или точку данных.

Отдельная плитка реагирует на определённые события в подключённых метриках и может принимать разные цвета:

* зелёный: есть данные хотя бы по одной подключённой метрике
* красный: есть открытая проблема, связанная хотя бы с одной подключённой метрикой
* серый: есть закрытая проблема, связанная хотя бы с одной подключённой метрикой
* белый: данные для этой плитки в текущем временном диапазоне отсутствуют

Подробности конфигурации см. в разделе [Health cards](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#health-cards "Подробнее о синтаксисе unified analysis.").

![Health card](https://dt-cdn.net/images/dee80e89-6646-420a-810d-0e7e2566677b-1640-4b6291895b.png)

Health card

## Концепции

### Actions

Actions определяют, что происходит при выборе одного из доступных вариантов в меню **More** (**…**) в правом верхнем углу каждой карточки.

Подробности конфигурации см. в разделе [Actions](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#actions "Подробнее о синтаксисе unified analysis.").

### Filtering

Унифицированный анализ поддерживает фильтрацию объектов по индексированным атрибутам. Фильтрацию можно включить для list page и в контексте конкретных карточек. Фильтрация объектов настраивается на двух уровнях:

* На уровне страницы: фильтрация затрагивает все карточки на странице. Отдельные конфигурации предусмотрены для [details page](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#details-filters "Подробнее о синтаксисе unified analysis.") и [list page](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference#list-filters "Подробнее о синтаксисе unified analysis.").
* На уровне entity list: фильтрация затрагивает только один список.

### Injections

Если нужно отображать карточки на странице без изменения их макета, см. [Extend built-in unified analysis pages](/managed/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages "Расширьте встроенные страницы unified analysis дополнительными данными, собранными расширением.").

### Exploratory analysis

Exploratory analysis анализирует только метрики из graph chart, входящих в chart groups, entities lists и metric tables. Подробнее см. [Davis® causal correlation analysis](/managed/dynatrace-intelligence/ai-models/causal-correlation-analysis "Как Davis® causal correlation analysis находит связанные метрики в вашей среде.").

**Next step**: [Unified analysis tutorial](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial "Как загрузить тестовые данные в среду Dynatrace и создать простое расширение unified analysis.")