---
title: Расширение встроенных страниц единого анализа
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages
---

# Расширение встроенных страниц единого анализа

# Расширение встроенных страниц единого анализа

* Reference
* 2-min read
* Published May 19, 2022

Если расширение поставляет дополнительные данные для сущности по умолчанию, у которой есть собственная страница единого анализа, можно расширить эту страницу с помощью card injections. Примеры встроенных страниц единого анализа: [страница обзора хоста](/managed/observe/infrastructure-observability/hosts/monitoring/host-monitoring "Monitor hosts with Dynatrace.") или любая страница единого анализа Kubernetes. Card injections доступны начиная с версии Dynatrace 1.233.

## Определение card injection

Конфигурация card injection аналогична конфигурации самого макета страницы, с одним существенным отличием: injected cards упорядочиваются по алфавиту в соответствии со своим ключом, который должен использовать чётко заданный префикс. Это гарантирует, что несвязанные данные от разных расширений не будут перемешаны на одной странице единого анализа. Injections добавляются в разделы `detailsInjections` и `listInjections` конфигурации страницы.

```
detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE
```

Для карточки, поставляемой расширением, доступны следующие параметры:

* `type`: тип карточки, который можно передать на страницу единого анализа. Поддерживаемые типы: `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS` и `MESSAGE`.
* `key`: уникальный ключ карточки, используемый для ссылки на нужную конфигурацию карточки. Нужно использовать чётко заданный префикс ключа, чтобы связанные карточки правильно размещались на странице. Карточки сортируются по алфавиту на основе ключа.
* `entitySelectorTemplate`: entity selector, используемый для ссылки на карточки другого отслеживаемого типа сущности. Подробнее: [Environment API v2 - Entity selector](/managed/dynatrace-api/environment-api/entity-v2/entity-selector "Configure the entity selector for Environment API endpoints.").

  Details

  Параметр может решать несколько задач: выбирать сущность, на которой будет отображаться диаграмма, фильтровать сущности по определённым правилам или связывать сущности между собой. Используется совместно с `entityType` для дополнительного уточнения того, какие сущности применимы к карточке. Например, если `entityType` равен `HOST`, с помощью `entitySelectorTemplate` можно отображать карточку только для хостов с определённой операционной системой.

  `$entityConditions` выступает динамическим плейсхолдером, адаптирующимся к контексту, в котором отображается карточка. Например, когда карточка отображается на странице, посвящённой конкретному хосту, `$entityConditions` автоматически подстраивается под условия, применимые к этому хосту.

  Например, когда карточка со следующей конфигурацией отображается на странице хоста.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))"
  ```

  Плейсхолдер `$(entityConditions)` автоматически заменится так, чтобы указывать на конкретную сущность хоста.

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))"
  ```
* `width`: определяет ширину карточки относительно ширины страницы. Поддерживаемые значения: `HALF_SIZE` и `FULL_SIZE`.
* `conditions`: список условий, которые должны выполняться для отображения карточки.

## Ссылка на card injection

На завершающем шаге нужно указать ссылку на карточку, которую необходимо внедрить на встроенную страницу единого анализа, с помощью пакета Extensions 2.0 и разместить её в файле `extension.yaml` в разделе `screens`. В этом примере расширяется встроенная страница обзора хоста (`entityType: HOST`).

```
name: custom:com.ua.example.extension



version: 1.0.0



minDynatraceVersion: 1.233.0



author:



name: StackEnterprise



# Here comes your usual extension YAML content: data source, declarative metrics, topology, etc.



screens:



- entityType: HOST



detailsInjections:



- type: CHART_GROUP



key: my-host-feature-windows-only-chart



conditions:



- entityAttribute|osType=WINDOWS



- type: CHART_GROUP



key: my-host-feature-chart1



- type: CHART_GROUP



key: my-host-feature-chart2



- type: CHART_GROUP



key: my-host-feature-process-chart



entitySelectorTemplate: type(PROCESS_GROUP_INSTANCE), fromRelationships.isProcessOf($(entityConditions))



width: HALF_SIZE



chartsCards:



- key: my-host-feature-windows-only-chart



...



- key: my-host-feature-chart1



...



- key: my-host-feature-chart2



...



- entityType: PROCESS_GROUP_INSTANCE



chartsCards:



- key: my-host-feature-process-chart



...
```