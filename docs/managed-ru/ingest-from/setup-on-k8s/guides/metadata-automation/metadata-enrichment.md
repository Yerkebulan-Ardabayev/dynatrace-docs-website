---
title: Настройка каталога обогащения
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
scraped: 2026-05-12T11:24:18.092975
---

# Настройка каталога обогащения

# Настройка каталога обогащения

* Чтение: 2 мин
* Опубликовано 28 июля 2023 г.

Обогащение метаданными является необязательной функцией, которая улучшает сигналы мониторинга, добавляя дополнительные метаданные.

## Что вы узнаете

В этом руководстве описано, как настроить и включить обогащение метаданными в Dynatrace Operator. Следуя этому руководству, вы сможете:

* Проверить правильность применения обогащённых метаданных для различных сценариев использования.
* Связать логи и метрики с конкретными сущностями, такими как поды, процессы и т. д.

## Предварительные требования

* Dynatrace Operator установлен и запущен в вашем кластере Kubernetes.
* К вашему кластеру применён корректный DynaKube.

## Шаги

1. Включите обогащение метаданными

Чтобы включить обогащение метаданными, измените YAML вашего DynaKube:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true
```

Если используются дополнительные функции, такие как ActiveGate или OneAgent, ваша конфигурация может включать:

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true



oneAgent:



cloudNativeFullStack: (or other mode)



...



activeGate:



capabilities:



- routing



...
```

2. Используйте селектор пространств имён

Необязательно

Чтобы ограничить обогащение метаданными определёнными пространствами имён, добавьте поле `namespaceSelector` в вашу конфигурацию:

```
metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



team: finance
```

Эта конфигурация применяет обогащение метаданными только к пространствам имён с меткой `team=finance`.

3. Проверьте каталог обогащения

Убедитесь, что каталог обогащения во внедрённых подах отражает настроенные вами атрибуты метаданных.

Файлы обогащения хранятся в следующем каталоге: `/var/lib/dynatrace/enrichment`

В этом каталоге находятся файлы обогащения `dt_metadata.json` и `dt_metadata.properties`

Файлы выглядят так:

1. dt\_metadata.properties

```
dt.entity.kubernetes_cluster=<kubernetes-cluster-id>



dt.kubernetes.cluster.id=<cluster-id>



dt.kubernetes.workload.kind=<workload-kind>



dt.kubernetes.workload.name=<workload-name>



k8s.cluster.name=<cluster-name>



k8s.cluster.uid=<cluster-uid>



k8s.container.name=<container-name>



k8s.namespace.name=<namespace-name>



k8s.node.name=<node-name>



k8s.pod.name=<pod-name>



k8s.pod.uid=<pod-uid>



k8s.workload.kind=<workload-kind>



k8s.workload.name=<workload-name>
```

2. dt\_metadata.json

```
{



"dt.entity.kubernetes_cluster": "<kubernetes-cluster-id>",



"dt.kubernetes.cluster.id": "<cluster-id>",



"dt.kubernetes.workload.kind": "<workload-kind>",



"dt.kubernetes.workload.name": "<workload-name>",



"k8s.cluster.name": "<cluster-name>",



"k8s.cluster.uid": "<cluster-uid>",



"k8s.container.name": "<container-name>",



"k8s.namespace.name": "<namespace-name>",



"k8s.node.name": "<node-name>",



"k8s.pod.name": "<pod-name>",



"k8s.pod.uid": "<pod-uid>",



"k8s.workload.kind": "<workload-kind>",



"k8s.workload.name": "<workload-name>"



}
```

**Обратите внимание:** файлы обогащения будут использоваться для различных видов обогащения автоматически, если включён OneAgent. Если OneAgent не включён, файлы обогащения и их содержимое необходимо использовать вручную.

Подробнее см. [Обогащение принимаемых данных измерениями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

## Узнать больше

* [Документация Dynatrace: файлы обогащения метаданными](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")

Выполнив эти шаги, вы сможете в полной мере использовать обогащение метаданными для улучшения мониторинга Kubernetes и получения более глубокой аналитики.