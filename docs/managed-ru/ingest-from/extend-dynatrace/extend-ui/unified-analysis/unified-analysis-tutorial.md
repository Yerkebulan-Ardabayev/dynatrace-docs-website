---
title: Обучающий пример: страницы унифицированного анализа
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial
scraped: 2026-05-12T11:37:59.140301
---

# Обучающий пример: страницы унифицированного анализа

# Обучающий пример: страницы унифицированного анализа

* 10-min read
* Updated on Mar 16, 2023

Пошаговое руководство по созданию страниц унифицированного анализа для пользовательских типов сущностей.

## Предварительные условия

* Установленное и настроенное расширение Dynatrace 2.0.
* Настроенная пользовательская топология с типом сущности.
* Права администратора в окружении Dynatrace.

## Симулятор Easy Taxis Fleet

В качестве примера используется симулятор парка такси Easy Taxis Fleet, который генерирует метрики для транспортных средств такси.

## Шаги

### 1. Создание и загрузка расширения с топологией

Создайте файл `extension.yaml` с определением топологии:

```yaml
name: custom:easy-taxis
version: 1.0.0
minDynatraceVersion: "1.240"
author:
  name: Easy Taxis

topology:
  types:
    - name: easy_taxis:taxi
      displayName: Taxi Vehicle
      rules:
        - idPattern: "taxi-{taxi.id}"
          sources:
            - sourceType: Metrics
              condition: "$prefix(easy_taxis)"
          attributes:
            - pattern: "{taxi.id}"
              key: taxi.id
              displayName: Taxi ID
```

### 2. Проверка прогресса

После загрузки расширения убедитесь, что сущности такси появились в интерфейсе Dynatrace.

### 3. Настройка страниц унифицированного анализа

Добавьте секцию `screens` в файл `extension.yaml`:

```yaml
screens:
  - entityType: easy_taxis:taxi
    detailsSettings:
      staticContent:
        breadcrumb:
          - entityType: easy_taxis:taxi
        showGlobalFilter: false
      layout:
        autoGenerate: false
        cards:
          - key: taxi_metrics
            type: CHART_GROUP

    detailsCharts:
      - key: taxi_metrics
        displayName: Taxi Metrics
        numberOfVisibleCharts: 2
        charts:
          - displayName: Trip Count
            series:
              - key: easy_taxis.trip.count
                displayName: Trips
                aggregation: SUM
                type: AUTO
```

Загрузите обновлённое расширение и проверьте отображение страниц.

## Связанные темы

* [Справочник по унифицированному анализу](/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-reference "Полный справочник конфигурации.")
* [Пользовательская топология](/managed/ingest-from/extend-dynatrace/extend-topology/custom-topology "Создание пользовательских типов сущностей.")