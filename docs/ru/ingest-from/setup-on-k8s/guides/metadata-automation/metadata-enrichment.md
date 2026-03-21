---
title: Настройка директории обогащения
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
scraped: 2026-03-06T21:23:38.378350
---

* Latest Dynatrace
* 2-min read

Обогащение метаданными — это необязательная функция, которая улучшает сигналы мониторинга за счёт добавления дополнительных метаданных.

## Что вы узнаете

В этом руководстве объясняется, как настроить и включить обогащение метаданными в Dynatrace Operator. Следуя этому руководству, вы сможете:

* Проверить корректность применения обогащённых метаданных для различных вариантов использования.
* Связать журналы и метрики с конкретными объектами, такими как поды, процессы и т.д.

## Предварительные требования

* Dynatrace Operator установлен и работает в вашем кластере Kubernetes.
* К вашему кластеру применён действующий DynaKube.

## Шаги

1. Включение обогащения метаданными

Для включения обогащения метаданными измените YAML-файл вашего DynaKube:

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

При использовании дополнительных функций, таких как ActiveGate или OneAgent, ваша конфигурация может включать:

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

2. Использование селектора пространств имён

Необязательно

Чтобы ограничить обогащение метаданными конкретными пространствами имён, добавьте поле `namespaceSelector` в вашу конфигурацию:

```
metadataEnrichment:


enabled: true


namespaceSelector:


matchLabels:


team: finance
```

Эта конфигурация применяет обогащение метаданными только к пространствам имён с меткой `team=finance`.

3. Проверка директории обогащения

Убедитесь, что директория обогащения в инжектированных подах отражает настроенные вами атрибуты метаданных.

Файлы обогащения хранятся в следующей директории: `/var/lib/dynatrace/enrichment`

В этой директории находятся файлы обогащения `dt_metadata.json` и `dt_metadata.properties`

Файлы выглядят следующим образом:

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

**Обратите внимание:** Файлы обогащения будут использоваться для различных обогащений автоматически, если включён OneAgent. Если OneAgent не включён, файлы обогащения и их содержимое необходимо использовать вручную.

Подробнее см. в разделе [Обогащение принятых данных Dynatrace-специфичными измерениями](../../../extend-dynatrace/extend-data.md#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии Dynatrace-специфичными полями.").

## Дополнительные материалы

* [Документация Dynatrace: файлы обогащения метаданными](../../../extend-dynatrace/extend-data.md#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии Dynatrace-специфичными полями.")

Следуя этим шагам, вы сможете в полной мере использовать возможности обогащения метаданными для улучшения мониторинга Kubernetes и получения более глубоких аналитических данных.
