---
title: Учебное руководство WMI: единый анализ
source: https://docs.dynatrace.com/managed/ingest-from/extensions/develop-your-extensions/data-sources/wmi-extensions/wmi-tutorial/wmi-tutorial-05
scraped: 2026-05-12T11:54:17.898448
---

# WMI tutorial - унифицированный анализ

# WMI tutorial - унифицированный анализ

* Практическое руководство
* Чтение: 4 мин
* Опубликовано 30 марта 2022 г.

Страницы унифицированного анализа предоставляют возможности анализа производительности и устранения неполадок для новой отслеживаемой технологии.

Они позволяют отказаться от создания отдельных дашбордов и разовых графиков. Раздел `screens` определяет содержимое страницы каждой сущности: графики и списки связанных сущностей для быстрого перехода к деталям.

## Страница детального анализа

Страница сведений состоит из раздела `staticContent` и макета `layout` для динамического содержимого, включающего карточки `cards` (графики и списки).

`staticContent`

* `showProblems`: показывает панель проблем данной сущности
* `showProperties`: показывает раздел **Properties and tags**
* `showTags`: показывает теги, применённые к данной сущности
* `showGlobalFilter`: показывает глобальную панель фильтрации
* `showAddTag`: показывает кнопку **Add tag**

Макет `layout` состоит из карточек, определяемых в подразделах `chartsCards` и `entitiesListCards`.

## Карточка графиков

Карточка графиков: раздел экрана, отображающий графики. В карточке определяются все возможные графики; часть из них отображается одновременно, остальные доступны в раскрывающемся списке над графиком.

Карточки графиков используют [селекторы метрик](/managed/dynatrace-api/environment-api/metric-v2/metric-selector "Настройте селектор метрик для API метрик v2.") для корректного отображения метрик.

Простой пример карточки графиков:

```
chartsCards:



- key: "host-cpu-metrics"



displayName: "Host CPU"



numberOfVisibleCharts: 2



charts:



- displayName: "Idle CPU"



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- displayName: "User CPU"



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"
```

## Список сущностей

Список сущностей содержит объекты, связанные с текущей сущностью. Для каждой возвращаемой сущности можно строить дополнительные графики, которые отображаются как единое значение в представлении списка.

Списки сущностей используют [селекторы сущностей](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Настройте селектор сущностей для эндпоинтов Environment API.") для корректного отображения связанных объектов.

Простой пример списка сущностей:

```
entitiesListCards:



- key: "nic-list"



displayName: "Network Interfaces"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Interface)"



displayCharts: false



displayIcons: true



enableDetailsExpandability: true
```

`$(entityConditions)`: функция, которая автоматически сопоставляется с текущей сущностью. Её использование обязательно для селекторов сущностей в расширении.

## Карточка свойств

Карточку свойств `propertiesCard` сущности можно изменить: добавить дополнительные свойства или скрыть ненужные. Свойства извлекаются из атрибутов сущности (если тип `ATTRIBUTE`) или через селектор сущности (если тип `RELATION`).

## Определение страниц унифицированного анализа для расширения

1. Добавьте раздел `screens` в файл `extension.yaml` по приведённому шаблону.
2. Настройте параметры страницы сведений для типов сущностей Generic Host и Generic Network Device.
3. Используйте карточки графиков для отображения всех метрик каждой сущности.
4. Добавьте карточки списков сущностей, чтобы Generic Host отображал все работающие на нём сетевые адаптеры и интерфейсы.
5. Добавьте свойство на основе связи, чтобы Generic Network Device отображал хост, на котором работает.
6. Соберите и загрузите новую версию пакета расширения.
7. Проверьте, что страницы отображаются корректно.

```
screens:



- entityType: wmi:generic_host



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



- type: "CHART_GROUP"



key: "wmi_host-chart-metrics"



- type: "ENTITIES_LIST"



key: "wmi_host-list-network_interfaces"



- type: "ENTITIES_LIST"



key: "wmi_host-list-network_adapters"



chartsCards:



- key: "wmi_host-chart-metrics"



displayName: "Generic Host Metrics"



numberOfVisibleCharts: 2



charts:



- displayName: "CPU Usage Breakdown"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"



- metricSelector: "custom.demo.host-observability.host.cpu.time.processor:SplitBy()"



- displayName: "CPU User"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.user:SplitBy()"



- displayName: "CPU Idle"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.idle:SplitBy()"



- displayName: "CPU Used"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.host.cpu.time.processor:SplitBy()"



entitiesListCards:



- key: "wmi_host-list-network_interfaces"



displayName: "Network Interfaces"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Interface)"



pageSize: 5



displayCharts: false



displayIcons: true



enableDetailsExpandability: true



numberOfVisibleCharts: 1



charts:



- displayName: "Traffic"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- key: "wmi_host-list-network_adapters"



displayName: "Network Adapters"



entitySelectorTemplate: "type(wmi:generic_network_device),fromRelationships.runsOn($(entityConditions)),wmi_network_type(Adapter)"



pageSize: 5



displayCharts: false



displayIcons: true



enableDetailsExpandability: true



numberOfVisibleCharts: 1



charts:



- displayName: "Traffic"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- entityType: wmi:generic_network_device



propertiesCard:



properties:



- type: ATTRIBUTE



attribute:



key: wmi_network_name



displayName: Name



- type: ATTRIBUTE



attribute:



key: wmi_network_type



displayName: Type



- type: RELATION



relation:



entitySelectorTemplate: type(wmi:generic_host),toRelationships.runsOn($(entityConditions))



displayName: Host



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



- type: "CHART_GROUP"



key: "wmi_network_device-chart-traffic"



chartsCards:



- key: "wmi_network_device-chart-traffic"



displayName: "Traffic"



numberOfVisibleCharts: 2



charts:



- displayName: "Traffic breakdown"



visualization:



themeColor: BLUE



seriesType: AREA



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- metricSelector: "custom.demo.host-observability.network.bytes.received.persec:SplitBy()"



- displayName: "Bytes sent"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- displayName: "Bytes received"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"



- displayName: "Bytes"



visualization:



themeColor: BLUE



seriesType: LINE



metrics:



- metricSelector: "custom.demo.host-observability.network.bytes.sent.persec:SplitBy()"
```

## Результаты

Настроенные страницы унифицированного анализа отображаются и заполняются данными в соответствии с ожиданиями.

![result](https://dt-cdn.net/images/wmi-tutorial-ua-details-1626-532b22a38b.png)

result