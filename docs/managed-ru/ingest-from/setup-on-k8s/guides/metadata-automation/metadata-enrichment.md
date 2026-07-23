---
title: Настройка обогащения метаданными
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
---

# Настройка обогащения метаданными

# Настройка обогащения метаданными

* Практическое руководство
* 3 минуты чтения
* Обновлено 25 июн. 2026

Обогащение метаданными прикрепляет метаданные Kubernetes (идентификаторы кластера, пространства имён, рабочей нагрузки, пода и контейнера) к сигналам телеметрии. Механизм различается в зависимости от режима:

* **OneAgent injection**: Dynatrace Operator записывает метаданные в директорию обогащения `/var/lib/dynatrace/enrichment` и в аннотацию пода `metadata.dynatrace.com`.
* **OTLP exporter injection**: Dynatrace Operator добавляет переменные окружения `OTEL_RESOURCE_ATTRIBUTES` и аннотацию пода `metadata.dynatrace.com`.
* **Standalone `metadataEnrichment`**: Dynatrace Operator записывает метаданные в директорию обогащения `/var/lib/dynatrace/enrichment` и в аннотацию пода `metadata.dynatrace.com`.

## Предварительные требования

* Dynatrace Operator установлен и работает в кластере Kubernetes.
* В кластере применён корректный DynaKube.

## Как включить

1. Включите OneAgent injection

OneAgent injection автоматически включает обогащение метаданными. Настройте его в DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



oneAgent:



cloudNativeFullStack: {}
```

Для проверки просмотрите любой инжектированный под и найдите аннотацию `metadata.dynatrace.com`, содержащую объект JSON с обогащёнными метаданными Kubernetes:

```
kubectl get pod <pod-name> -n <namespace> -o yaml
```

2. Включите OTLP exporter injection

OTLP exporter injection автоматически включает обогащение метаданными для сигналов OTLP. Dynatrace Operator добавляет метаданные Kubernetes в переменную окружения `OTEL_RESOURCE_ATTRIBUTES` инжектированных подов и записывает их в аннотацию пода `metadata.dynatrace.com`.

Настройте его в DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



otlpExporterConfiguration:



signals:



metrics: {}



traces: {}



logs: {}
```

Полные инструкции по настройке и шаги проверки описаны в разделе [Enable automatic OpenTelemetry OTLP exporter configuration](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Automatically configure the OTLP exporter in applications instrumented with OpenTelemetry SDKs using Dynatrace Operator.").

3. Включите автономное обогащение метаданными

Dynatrace Operator записывает метаданные Kubernetes в файлы директории обогащения `/var/lib/dynatrace/enrichment` и в аннотацию пода `metadata.dynatrace.com`.

Используется при развёртывании с `classicFullStack`, автономным `logMonitoring`, `telemetryIngest` или модулем мониторинга Kubernetes ActiveGate.

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: <dk-name>



namespace: <dk-namespace>



spec:



apiUrl: <dk-apiUrl>



metadataEnrichment:



enabled: true
```

Чтобы ограничить обогащение метаданными определёнными пространствами имён, добавьте `namespaceSelector`:

```
spec:



metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



inject: metadata  # only namespaces with this label receive enrichment
```

Пометьте нужные пространства имён:

```
kubectl label namespace <namespace> inject=metadata
```

Для проверки убедитесь, что файлы появляются в инжектированных подах:

1. dt\_metadata.properties

```
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

Примеры кода для чтения этих файлов приведены в разделе [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

## Задание атрибутов ресурсов в DynaKube

Dynatrace Operator version 1.10.0+

Можно задать дополнительные атрибуты ресурсов в DynaKube. Dynatrace Operator распространяет их на сигналы телеметрии без необходимости задавать метки пространств имён или аннотации подов.

Три поля определяют, куда будут добавлены атрибуты:

* `.spec.resourceAttributes`, применяется ко всем сигналам: OneAgent injection, OTLP exporter injection, автономному мониторингу логов и ActiveGate.
* `.spec.oneAgent.<mode>.additionalResourceAttributes`, применяется только к сигналам OneAgent. Имеет приоритет над дублирующимися ключами в `.spec.resourceAttributes`.
* `.spec.otlpExporterConfiguration.additionalResourceAttributes`, применяется только к OTLP-телеметрии. Имеет приоритет над дублирующимися ключами в `.spec.resourceAttributes`.

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



resourceAttributes:



aws.account.id: 123456789012



oneAgent:



cloudNativeFullStack:



additionalResourceAttributes:



my.team: platform



namespaceSelector:



matchLabels:



my.app.com/oneagent: "true"



otlpExporterConfiguration:



additionalResourceAttributes:



my.team: platform



namespaceSelector:



matchLabels:



example.com/source: otel



signals:



metrics: {}



traces: {}



logs: {}
```

Dynatrace Operator распространяет объединённые атрибуты следующим образом:

* **OneAgent injection**: Dynatrace Operator записывает атрибуты в `dt_node_metadata.properties` для OneAgents и в `dt_metadata.properties`, `dt_metadata.json`, а также в аннотацию пода `metadata.dynatrace.com` для инжектированных подов.
* **OTLP exporter injection**: Dynatrace Operator добавляет атрибуты в `OTEL_RESOURCE_ATTRIBUTES` и в аннотацию пода `metadata.dynatrace.com` для инжектированных подов.
* **Standalone log monitoring и ActiveGate**: Dynatrace Operator применяет `.spec.resourceAttributes` напрямую. `additionalResourceAttributes` для конкретного режима не влияет на эти компоненты.

На суммарное количество атрибутов в `.spec.resourceAttributes` и `additionalResourceAttributes` вместе действует мягкое ограничение в 10 записей, при его превышении Dynatrace Operator выводит предупреждение.

Конфликтующие ключи при одновременном OneAgent и OTLP injection

Если на одном поде активны и OneAgent injection, и OTLP exporter injection, оба компонента записывают данные в общую аннотацию JSON `metadata.dynatrace.com`. Одинаковые ключи в обоих разделах приводят к неопределённому поведению. Когда оба механизма активны на одном поде, необходимо использовать уникальные ключи в `additionalResourceAttributes` для OneAgent и OTLP, чтобы избежать непредсказуемого поведения.

### Санитизация ключей атрибутов

В сценариях инжекции в поды (OneAgent injection и OTLP exporter injection) Dynatrace Operator распространяет атрибуты в виде аннотаций подов Kubernetes в формате `metadata.dynatrace.com/<key>`. Суффиксы ключей аннотаций Kubernetes должны содержать только допустимые символы DNS-меток, поэтому Dynatrace Operator санитизирует ключи атрибутов, заменяя недопустимые символы перед записью в аннотации.

Dynatrace Operator проверяет ключи атрибутов и сообщает о следующем:

* **Warning**: ключ содержит символы, которые Dynatrace Operator заменяет при санитизации, при этом ключ переименовывается, но аннотация всё равно записывается.
* **Error**: санитизированный ключ оказался пустой строкой, Dynatrace Operator удаляет такой ключ.
* **Error**: два ключа дают одинаковое санитизированное значение, что приводит к коллизии.
* **Error**: санитизированный ключ превышает 63 символа, что нарушает ограничение Kubernetes на длину сегмента имени аннотации для `metadata.dynatrace.com/<key>`.

Полный справочник параметров приведён в разделе [DynaKube API reference](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

## Дополнительные материалы

* [Enrich ingested data with Dynatrace-specific dimensions](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")