---
title: Настройка визуализации «Список лидеров» в Dynatrace
source: https://docs.dynatrace.com/managed/analyze-explore-automate/dashboards-classic/charts-and-tiles/visualization-top-list
scraped: 2026-05-12T11:12:59.701679
---

# Настройка визуализации «Список лидеров» в Dynatrace

# Настройка визуализации «Список лидеров» в Dynatrace

* Практическое руководство
* Чтение: 1 мин
* Опубликовано 13 декабря 2021 г.

[Dashboards Classic](/managed/analyze-explore-automate/dashboards-classic "Узнайте, как создавать дашборды Dynatrace Classic, управлять ими и использовать их.")

Чтобы визуализировать результаты запроса в виде списка лидеров, выберите `Top list` из списка над определением запроса в левом верхнем углу страницы.

Эта визуализация не отображает несколько метрик. Если в запросе настроено несколько метрик, выполняется только выбранная в редакторе метрика (по умолчанию — первая).

Чтобы выбрать одну метрику из запроса с несколькими метриками, выберите букву рядом с метрикой или нажмите значок глаза.

![Data Explorer: переключение метрики](https://dt-cdn.net/images/eye-toggle-metric-1238-d343b9cc0e.png)

Data Explorer: переключение метрики

#### Пример в Data Explorer

![Data Explorer: Список лидеров](https://dt-cdn.net/images/visualization-example-top-list-1596-f2a02801a3.png)

Data Explorer: Список лидеров

#### Пример, закреплённый на дашборде в виде плитки

![Пример списка лидеров](https://dt-cdn.net/images/example-tile-top-list-263-57605443d4.png)

Пример списка лидеров

## Смена визуализации

При переключении между визуализациями учтите, что некоторые параметры характерны для конкретной визуализации.

* При переключении часть настроек может быть проигнорирована. Значок информации предупредит об этом.

  ![Data Explorer: предупреждение о смене визуализации](https://dt-cdn.net/images/change-visualization-warning-1277-9438aaceea.png)

  Data Explorer: предупреждение о смене визуализации

## Изменение набора метрик

По умолчанию отображается первая метрика. Чтобы выбрать другую, используйте букву или значок глаза.

## Настройки

Раздел **Settings** — один из разворачиваемых разделов на правой панели Data Explorer.

![Data Explorer: раздел Settings](https://dt-cdn.net/images/data-explorer-settings-settings-322-7b365c52e5.png)

Data Explorer: раздел Settings

### Трансформация свёртки

* По умолчанию — `Auto`.
* Доступные варианты: `Last value`, `Average`, `Count`, `Maximum`, `Minimum`, `Sum`, `Median`, `Value`, `Percentile 10th`, `Percentile 75th`, `Percentile 90th`.

При `Auto` для `Table`, `Single value`, `Top list` или `Honeycomb` используется разрешение `Inf`. Чтобы проверить запрос — **Result** > **Copy request**.

## Настройки по метрике

### Переименование метрики

1. В разделе **Settings** выберите для метрики, которую хотите переименовать.
2. Отредактируйте имя и выберите галочку для сохранения.

### Единица измерения и формат

* **Unit**: `None`, `Auto`, или конкретная единица. В **Advanced mode** — `:setUnit(<unit>)`.
* **Format**: `None`, `Auto`, `0`, `0.0`, `0.00`, `0.000`.

| Обозначение | Множитель | Значение |
| --- | --- | --- |
| k | 10^3 | кило, тысяча |
| M | 10^6 | мега, миллион |
| G | 10^9 | гига, миллиард |
| T | 10^12 | тера, триллион |

### Добавление переопределения цвета

1. В разделе **Settings** нажмите **Add color override**
2. Выберите ряд из списка
3. Выберите цвет переопределения

## Пороговые значения

Раздел **Threshold** используется для улучшения визуализаций и плиток.

![Data Explorer: раздел Threshold](https://dt-cdn.net/images/data-explorer-settings-threshold-323-3ddaf51ec3.png)

Data Explorer: раздел Threshold

Устанавливайте значения порогов после выбора **Unit**.

### Установка порогов

1. В разделе **Thresholds** введите значения порогов

   ![Установка значений порогов](https://dt-cdn.net/images/threshold-definition-set-threshold-values-graph-249-e0895fe995.png)

   Установка значений порогов
2. Настройте цвета порогов Необязательно

   ![Настройка цветов порогов](https://dt-cdn.net/images/threshold-definition-adjust-threshold-color-269-2e5d1f3fb4.png)

   Настройка цветов порогов

### Скрытие и отображение цветов порогов

Чтобы скрыть или показать цвета порогов, в разделе **Thresholds** нажмите.

![Скрытие/отображение порогов](https://dt-cdn.net/images/threshold-definition-hide-or-show-graph-249-989dc64199.png)

Скрытие/отображение порогов