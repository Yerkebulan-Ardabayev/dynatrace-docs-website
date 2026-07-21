---
title: Настройка обогащения метаданных
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment
---

# Настройка обогащения метаданных

# Настройка обогащения метаданных

* Практическое руководство
* 3 мин на чтение
* Обновлено 25 июня 2026 г.

Обогащение метаданных присоединяет Kubernetes метаданные (идентификаторы кластера, namespace, workload, pod и контейнера) к сигналам телеметрии. Механизм зависит от режима:

* **Внедрение OneAgent**: Dynatrace Operator записывает метаданные в каталог обогащения по пути `/var/lib/dynatrace/enrichment` и в аннотацию pod `metadata.dynatrace.com`.
* **Внедрение OTLP-экспортера**: Dynatrace Operator внедряет переменные окружения `OTEL_RESOURCE_ATTRIBUTES` и аннотацию pod `metadata.dynatrace.com`.
* **Отдельный `metadataEnrichment`**: Dynatrace Operator записывает метаданные в каталог обогащения по пути `/var/lib/dynatrace/enrichment` и в аннотацию pod `metadata.dynatrace.com`.

## Предварительные требования

* Dynatrace Operator установлен и работает в кластере Kubernetes.
* В кластере применён корректный DynaKube.

## Как включить

1. Включить внедрение OneAgent

Внедрение OneAgent автоматически включает обогащение метаданных. Настроить его можно в DynaKube:

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

Чтобы проверить, изучите любой pod с внедрением и найдите аннотацию `metadata.dynatrace.com`, содержащую объект JSON с обогащёнными метаданными Kubernetes:

```
kubectl get pod <pod-name> -n <namespace> -o yaml
```

2. Включить внедрение OTLP-экспортера

Внедрение OTLP-экспортера автоматически включает обогащение метаданных для сигналов OTLP. Dynatrace Operator добавляет метаданные Kubernetes к переменной окружения `OTEL_RESOURCE_ATTRIBUTES` у pod'ов с внедрением и записывает их в аннотацию pod `metadata.dynatrace.com`.

Настроить это можно в DynaKube:

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

Полные инструкции по настройке и шаги проверки см. в разделе [Включение автоматической настройки OpenTelemetry OTLP-экспортера](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматическая настройка OTLP-экспортера в приложениях, инструментированных с помощью SDKов OpenTelemetry, с использованием Dynatrace Operator.").

3. Включить отдельное обогащение метаданных

Dynatrace Operator записывает метаданные Kubernetes в файлы каталога обогащения по пути `/var/lib/dynatrace/enrichment` и в аннотацию pod `metadata.dynatrace.com`.

Используйте этот вариант при развёртывании с `classicFullStack`, отдельным `logMonitoring`, `telemetryIngest` или мониторингом ActiveGate для Kubernetes.

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

Чтобы ограничить обогащение метаданных конкретными namespace, добавьте `namespaceSelector`:

```
spec:



metadataEnrichment:



enabled: true



namespaceSelector:



matchLabels:



inject: metadata  # обогащение получают только namespace с этой меткой
```

Промаркируйте namespace, которые нужно включить:

```
kubectl label namespace <namespace> inject=metadata
```

Чтобы проверить, убедитесь, что файлы появились в pod'ах с внедрением:

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

Примеры кода для чтения этих файлов см. в разделе [Обогащение поступающих данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.").

## Задание атрибутов ресурса в DynaKube

Dynatrace Operator версии 1.10.0+

В DynaKube можно определить дополнительные атрибуты ресурса. Dynatrace Operator распространяет их на сигналы телеметрии без необходимости меток namespace или аннотаций pod.

Три поля определяют, куда внедряются атрибуты:

* `.spec.resourceAttributes`, применяется ко всем сигналам: внедрение OneAgent, внедрение OTLP-экспортера, отдельный мониторинг логов и ActiveGate.
* `.spec.oneAgent.<mode>.additionalResourceAttributes`, применяется только к сигналам OneAgent. Имеет приоритет над дублирующимися ключами в `.spec.resourceAttributes`.
* `.spec.otlpExporterConfiguration.additionalResourceAttributes`, применяется только к телеметрии OTLP. Имеет приоритет над дублирующимися ключами в `.spec.resourceAttributes`.

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

* **Внедрение OneAgent**: Dynatrace Operator записывает атрибуты в `dt_node_metadata.properties` для OneAgentов, а также в `dt_metadata.properties`, `dt_metadata.json` и аннотацию pod `metadata.dynatrace.com` для pod'ов с внедрением.
* **Внедрение OTLP-экспортера**: Dynatrace Operator добавляет атрибуты в `OTEL_RESOURCE_ATTRIBUTES` и аннотацию pod `metadata.dynatrace.com` для pod'ов с внедрением.
* **Отдельный мониторинг логов и ActiveGate**: Dynatrace Operator применяет `.spec.resourceAttributes` напрямую. `additionalResourceAttributes`, специфичные для режима, на эти компоненты не влияют.

Действует мягкое ограничение в 10 атрибутов суммарно по `.spec.resourceAttributes` и `additionalResourceAttributes` вместе, при превышении этого лимита Dynatrace Operator записывает предупреждение в журнал.

Конфликтующие ключи при одновременном внедрении OneAgent и OTLP

Когда на одном и том же pod'е одновременно активны внедрение OneAgent и внедрение OTLP-экспортера, оба записывают данные в общую аннотацию JSON `metadata.dynatrace.com`. Если один и тот же ключ определён в обеих секциях, поведение непредсказуемо. При одновременной активности на одном pod'е нужно использовать разные ключи в `additionalResourceAttributes` для OneAgent и OTLP, чтобы избежать непредсказуемого поведения.

### Санитизация ключей атрибутов

Для сценариев внедрения в pod (внедрение OneAgent и внедрение OTLP-экспортера) Dynatrace Operator распространяет атрибуты в виде аннотаций pod Kubernetes в формате `metadata.dynatrace.com/<key>`. Суффиксы ключей аннотаций Kubernetes должны состоять из допустимых символов DNS-метки, поэтому Dynatrace Operator санитизирует ключи атрибутов, заменяя недопустимые символы перед записью в аннотации.

Dynatrace Operator проверяет ключи атрибутов и сообщает следующее:

* **Предупреждение**: ключ содержит символы, которые Dynatrace Operator заменяет при санитизации, Dynatrace Operator переименовывает ключ, но всё равно записывает аннотацию.
* **Ошибка**: санитизированный ключ представляет собой пустую строку, Dynatrace Operator отбрасывает ключ.
* **Ошибка**: два ключа дают одинаковое санитизированное значение, результатом становится коллизия.
* **Ошибка**: санитизированный ключ превышает 63 символа, это нарушает ограничение Kubernetes на длину сегмента имени аннотации для `metadata.dynatrace.com/<key>`.

Полный справочник параметров см. в разделе [Справочник параметров DynaKube API](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.").

## Дополнительные материалы

* [Обогащение поступающих данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")