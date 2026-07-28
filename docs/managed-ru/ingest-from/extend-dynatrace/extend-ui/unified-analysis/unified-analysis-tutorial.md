---
title: Обучающий курс по Unified analysis
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/unified-analysis/unified-analysis-tutorial
---

# Обучающий курс по Unified analysis

# Обучающий курс по Unified analysis

* 5 минут чтения
* Опубликовано 19 апреля 2023 г.

Пошаговый курс о том, как загрузить пользовательскую топологию в среду Dynatrace и создать расширение для определения типов топологии и связей между ними.

После этого можно настроить страницы unified analysis для анализа данных из нескольких источников, включая логи, метрики и трейсы, в едином представлении. Также можно подключать различные источники данных и измерения, применять фильтры и углубляться в конкретные детали.

## Предварительные требования

* Dynatrace CLI

  + Python 3.8 или 3.9
  + Доступ к установщику пакетов pip для Python
  + Установите dt-cli

    ```
    pip install dt-cli
    ```

    Подробнее см. [Sign extensions](/managed/ingest-from/extensions/develop-your-extensions/sign-extensions "Learn how to sign an extension, upload certificates and custom extensions, and configure certificate permissions using the Dynatrace Extensions Framework.").
* Токен со следующими разрешениями:

  + **Read credential vault entries** (`credentialVault.read`)
  + **Write credential vault entries** (`credentialVault.write`)
  + **Read entities** (`entities.read`)
  + **Write entities** (`entities.write`)
  + **Ingest events** (`events.ingest`)
  + **Ingest metrics** (`metrics.ingest`)
  + **Ingest logs** (`logs.ingest`)
  + **Read extensions** (`extensions.read`)
  + **Write extensions** (`extensions.write`)

## Загрузка тестовых данных наблюдаемости в среду

В этом примере используется **Easy Taxis Fleet Simulator**, интерактивное CLI-приложение, которое имитирует парк умных такси, отправляющих данные наблюдаемости в среду Dynatrace.

1. В зависимости от операционной системы скачайте нужный файл из списка [EasyTaxis executables﻿](https://dt-url.net/13434et) и запустите его.
2. Введите `help`, чтобы просмотреть все доступные команды.
3. Для запуска симуляции парка используйте команду ниже.

   ```
   start -e <your-environment-url> -t <your-api-token>
   ```

   Обязательно замените `<your-environment-url>` и `<your-api-token>` на реальные значения.

   Подробнее об аргументах и флагах см. команду `start help`.

Симуляция отправляет метрики, логи и события в среду Dynatrace.

## Сборка и загрузка расширения

1. Перейдите на страницу GitHub и скачайте [Observability Clinic Materials﻿](https://dt-url.net/sl034x0).
2. Откройте папку `extensions-project-starter` в предпочитаемой среде разработки.
3. Перейдите в папку `scripts` и откройте файл `config.yaml`. Нужно заполнить три обязательных поля: URL среды, токен и версию схемы.

   ```
   tenant_url: <your-environment-url>



   api_token: <your-api-token>



   schema_version: 1.265
   ```
4. Из директории `scripts` выполните следующую команду для генерации сертификатов.

   ```
   python initialize.py
   ```

   Сгенерированные сертификаты появятся в папке `certs`.
5. Выполните следующую команду для загрузки схем версии 1.265.

   ```
   python download_schemas.py
   ```
6. Перейдите в папку `extension` и создайте файл `extension.yaml`. Подробнее о scope расширения см. [Extension YAML file](/managed/ingest-from/extensions/develop-your-extensions/extension-yaml#start-extension-yaml-file "Learn how to create an extension YAML file using the Extensions framework.").
7. Используйте следующий пример расширения с определённой топологией. Подробнее о scope топологии см. [WMI tutorial - custom topology](/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-04 "Learn about WMI extensions in the Extensions framework.").

   ```
   name: custom:ua.example



   version: 1.0.0



   minDynatraceVersion: "1.238"



   author:



   name: Joe Doe



   topology:



   types:



   - enabled: true



   name: easytaxis:smart_fleet



   displayName: Smart Fleet



   rules:



   - idPattern: fleet_{fleet.id}



   instanceNamePattern: Smart Fleet ({fleet.id})



   iconPattern: cluster



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.fleet)



   attributes:



   - key: FleetID



   pattern: "{fleet.id}"



   - key: Location



   pattern: "{fleet.location}"



   role: default



   - idPattern: fleet_{fleet.id}



   instanceNamePattern: Smart Fleet ({fleet.id})



   iconPattern: cluster



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.taxi)



   - sourceType: Logs



   role: default



   - enabled: true



   name: easytaxis:smart_taxi



   displayName: Smart Taxi



   rules:



   - idPattern: taxi_{fleet.id}_{taxi.id}



   instanceNamePattern: Smart Taxi ({taxi.id})



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis.taxi)



   attributes:



   - key: TaxiID



   pattern: "{taxi.id}"



   - key: RegistrationNumber



   pattern: "{taxi.registration}"



   - key: Class



   pattern: "{taxi.class}"



   role: default



   relationships:



   - enabled: true



   sources:



   - sourceType: Metrics



   condition: $prefix(custom.easytaxis)



   fromType: easytaxis:smart_taxi



   typeOfRelation: CHILD_OF



   toType: easytaxis:smart_fleet
   ```
8. Выполните следующую команду для подписания расширения и его загрузки в среду.

   ```
   python build_and_upload.py
   ```

## Проверка прогресса

Если перейти в **Settings** > **Topology model** > **Generic types**, видно, что типы **Smart Fleet** и **Smart taxi** созданы. Определённую связь между ними можно увидеть в разделе **Generic relationships**.

* Список экземпляров Smart Fleet доступен по адресу `<your-environment>/ui/entity/list/easytaxis:smart_fleet`.

  ![Smart Fleet instance](https://dt-cdn.net/images/smart-fleet-1239-e7365be7f8.png)

  Smart Fleet instance
* Список экземпляров Smart Taxi доступен по адресу `<your-environment>/ui/entity/list/easytaxis:smart_taxi`.

  ![Smart Taxi instance](https://dt-cdn.net/images/smart-taxi-1231-2e3fcf1c19.png)

  Smart Taxi instance

## Настройка страниц unified analysis

Теперь можно настроить страницы сущностей, создав определение страницы в файле `extension.yaml`.

```
screens:



- entityType: easytaxis:smart_fleet



detailsSettings:



staticContent:



showProblems: true



showProperties: true



showTags: true



showGlobalFilter: true



showAddTag: true



layout:



autoGenerate: false



cards:



- type: ENTITIES_LIST



key: fleet-list-taxis



entitiesListCards:



- key: fleet-list-taxis



displayName: Taxis part of this fleet



pageSize: 5



entitiesLimit: 500



displayCharts: false



enableDetailsExpandability: true



numberOfVisibleCharts: 2



displayIcons: true



entitySelectorTemplate: type(easytaxis:smart_taxi),fromRelationships.isChildOf($(entityConditions))



columns:



- type: ATTRIBUTE



attribute:



key: Class



displayName: Class



- type: ATTRIBUTE



attribute:



key: RegistrationNumber



displayName: Registration



charts:



- displayName: Engine Temperature



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.temperature



visualizationType: GRAPH_CHART



- displayName: Speed



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.speed



visualizationType: GRAPH_CHART



- entityType: easytaxis:smart_taxi



propertiesCard:



properties:



- type: RELATION



relation:



entitySelectorTemplate: type(easytaxis:smart_fleet),toRelationships.isChildOf($(entityConditions))



displayName: Mother Fleet



detailsSettings:



staticContent:



showTags: true



showProperties: true



showProblems: true



showAddTag: true



showGlobalFilter: true



layout:



autoGenerate: false



cards:



- type: CHART_GROUP



key: taxi-metrics



chartsCards:



- key: taxi-metrics



displayName: Smart Taxi Metrics



numberOfVisibleCharts: 3



charts:



- displayName: Engine Temperature



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.temperature



visualizationType: GRAPH_CHART



- displayName: Speed



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.speed



visualizationType: GRAPH_CHART



- displayName: Days to revision



graphChartConfig:



visualization:



themeColor: DEFAULT



seriesType: LINE



metrics:



- metricSelector: custom.easytaxis.taxi.engine.daystorevision



visualizationType: GRAPH_CHART



listSettings:



staticContent:



showGlobalFilter: true



layout:



autoGenerate: true
```

* Для сущности Smart Taxi это определение включает три графика с данными о скорости, температуре двигателя и количестве дней до ревизии.

  Страница сущности Smart Taxi

  ![UA page example](https://dt-cdn.net/images/screenshot-2023-04-19-at-6-32-21-pm-1061-c102f4ffd1.png)

  UA page example
* Для сущности Smart Fleet это определение включает список такси, входящих в данный парк. Каждую сущность такси можно раскрыть и увидеть два графика с данными о скорости и температуре двигателя.

  Страница сущности Smart Fleet

  ![Smart fleet example](https://dt-cdn.net/images/fleet-1-1455-ccb222479c.png)

  Smart fleet example

  ![Smart fleet expand](https://dt-cdn.net/images/fleet-2-1417-2b62cf52f0.png)

  Smart fleet expand

## Связанные темы

* [About Extensions](/managed/ingest-from/extensions/concepts "Learn more about the concept of Dynatrace Extensions.")