---
title: Расширение встроенных страниц унифицированного анализа
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-ui/extend-unified-analysis-pages
scraped: 2026-03-06T21:34:16.785131
---

# Расширение встроенных унифицированных страниц анализа


* Classic
* Reference
* 2-min read
* Published May 19, 2022

Если ваше расширение предоставляет дополнительные данные для сущности по умолчанию с собственной унифицированной страницей анализа, вы можете расширить страницу с помощью инъекций карточек. Примеры встроенных унифицированных страниц анализа: [страница обзора хоста](../../../observe/infrastructure-observability/hosts/monitoring/host-monitoring.md "Мониторинг хостов с помощью Dynatrace.") или любая унифицированная страница анализа Kubernetes. Инъекции карточек доступны начиная с версии Dynatrace 1.233.

## Определение инъекции карточки

Конфигурация инъекции карточки аналогична конфигурации самого макета страницы с одним существенным отличием: вставляемые карточки упорядочиваются в алфавитном порядке по ключу, который должен использовать чётко заданный префикс ключа. Это гарантирует, что несвязанные данные, предоставляемые разными расширениями, не будут смешаны на унифицированной странице анализа. Инъекции можно добавлять в разделы `detailsInjections` и `listInjections` конфигурации экрана.

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

Для карточки, предоставляемой вашим расширением, доступны следующие параметры:

* `type`: Тип карточки, доступный для размещения на унифицированной странице анализа. Поддерживаемые типы: `CHART_GROUP`, `ENTITIES_LIST`, `EVENTS`, `LOGS` и `MESSAGE`.
* `key`: Уникальный ключ карточки, используемый для ссылки на нужную конфигурацию карточки. Используйте чётко заданный префикс ключа, чтобы обеспечить правильное размещение связанных карточек на странице. Карточки сортируются в алфавитном порядке по ключу.
* `entitySelectorTemplate`: Селектор сущностей, используемый для ссылки на карточки из другого типа отслеживаемых сущностей. Подробнее см. в разделе [Environment API v2 — Селектор сущностей](../../../dynatrace-api/environment-api/entity-v2/entity-selector.md "Настройте селектор сущностей для конечных точек Environment API.").

  Подробнее

  Он может служить нескольким целям: выбор сущности, на которой будет отображаться график, фильтрация сущностей по определённым правилам или связывание сущностей. Он используется совместно с `entityType` для дополнительного уточнения того, какие сущности применимы к карточке. Например, если `entityType` равен `HOST`, можно использовать `entitySelectorTemplate` для отображения карточки только для хостов с определённой операционной системой.

  `$entityConditions` выступает динамическим заполнителем, адаптирующимся к контексту, в котором отображается карточка. Например, когда карточка отображается на странице, посвящённой конкретному хосту, `$entityConditions` автоматически подстраивается под условия, применимые к этому хосту.

  Например, когда карточка со следующей конфигурацией отображается на странице хоста:

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf($(entityConditions))"
  ```

  Заполнитель `$(entityConditions)` будет автоматически заменён для указания на конкретную сущность хоста:

  ```
  "entitySelectorTemplate": "type(NETWORK_INTERFACE) AND fromRelationships.isNetworkInterfaceOf(type(HOST) AND entityId(HOST-<id>))"
  ```
* `width`: Определяет ширину карточки относительно ширины страницы. Поддерживаемые значения: `HALF_SIZE` и `FULL_SIZE`.
* `conditions`: Список условий, которые должны быть выполнены для отображения карточки.

## Ссылка на инъекцию карточки

На заключительном шаге необходимо сослаться на карточку для инъекции на встроенную унифицированную страницу анализа с помощью пакета Extensions 2.0 и поместить её в файл `extension.yaml` в разделе `screens`. В этом примере мы расширяем встроенную страницу обзора хоста (`entityType: HOST`).

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
