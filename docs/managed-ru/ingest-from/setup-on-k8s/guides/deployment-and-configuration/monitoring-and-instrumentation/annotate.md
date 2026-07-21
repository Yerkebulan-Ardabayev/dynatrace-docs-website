---
title: Настройка мониторинга для пространств имён и подов
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate
---

# Настройка мониторинга для пространств имён и подов

# Настройка мониторинга для пространств имён и подов

* Чтение: 5 мин
* Обновлено 25 июня 2026 г.

cloudNativeFullStack

applicationMonitoring

metadataEnrichment

При мониторинге кластера Kubernetes с использованием cloud-native full-stack или application monitoring, при применении обогащения метаданных или автоматической настройке экспортёров OTLP может понадобиться ограничить это определёнными пространствами имён и подами.

По умолчанию Dynatrace Operator внедряется во **все пространства имён**, кроме:

* Пространств имён с префиксом `kube-` или `openshift-`.
* Пространства имён, где установлен Dynatrace Operator.

Настоятельно рекомендуется использовать поля `namespaceSelector` (см. ниже), чтобы полностью контролировать, куда происходит внедрение.

## Мониторинг определённых пространств имён

Чтобы настроить Dynatrace Operator так, чтобы внедрение OneAgent, применение обогащения метаданных или автоматическая настройка экспортёров OTLP выполнялись только в определённых пространствах имён, задай параметр `namespaceSelector` в пользовательском ресурсе DynaKube.

`namespaceSelector` и аннотации, описанные здесь, влияют только на внедрение, выполняемое webhook-частью Dynatrace Operator. Они не влияют на возможности мониторинга Kubernetes API у ActiveGate или на мониторинг уровня хоста, выполняемый OneAgent.

Подробнее см. [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.") (поля `.spec.metadataEnrichment`, `.spec.oneAgent.cloudNativeFullStack`, `.spec.oneAgent.applicationMonitoring` и `.spec.otlpExporterConfiguration`).

1. Присвой пространствам имён метки.

Kubernetes

OpenShift

```
kubectl label namespace <my_namespace> dt-monitoring=true
```

```
oc label namespace <my_namespace> dt-monitoring=true
```

2. Измени DynaKube, добавив `namespaceSelector` для указания метки мониторинга.

Обогащение метаданных

Cloud-native full-stack мониторинг

Application monitoring

Настройка экспортёра OTLP

```
spec:



metadataEnrichment:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



oneAgent:



cloudNativeFullStack:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



oneAgent:



applicationMonitoring:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

```
spec:



otlpExporterConfiguration:



namespaceSelector:



matchLabels:



dt-monitoring: "true"
```

Подробнее о настройке меток для выборочного мониторинга см. [Labels and selectors﻿](https://dt-url.net/vj038vk).

Чтобы добавить исключения для определённых подов внутри выбранных пространств имён, можно [аннотировать соответствующие поды](#podexclusion).

## Исключение определённых пространств имён

Чтобы исключить определённые пространства имён из мониторинга, измени пользовательский ресурс DynaKube следующим образом.

* `key` определяет ключ метки. Начиная с Kubernetes версии 1.22, к пространствам имён по умолчанию добавляется метка `kubernetes.io/metadata.name`.
* `values` определяет значение метки.

```
...



namespaceSelector:



matchExpressions:



- key: LabelKey



operator: NotIn



values:



- LabelValue
```

Пример со стандартной меткой Kubernetes

Если выполнить `kubectl describe namespace dynatrace`, отобразится:

```
metadata:



name: dynatrace



labels:



kubernetes.io/metadata.name=dynatrace
```

Пример корректного селектора для исключения `dynatrace`:

```
...



namespaceSelector:



matchExpressions:



- key: kubernetes.io/metadata.name



operator: NotIn



values:



- dynatrace
```

Webhook будет внедряться в каждое пространство имён, которое соответствует всем `namespaceselector`.

Подробнее см. [Resources that support set-based requirements﻿](https://dt-url.net/hi03yvm).

## Исключение определённых подов в отслеживаемых пространствах имён

Чтобы исключить определённые поды внутри отслеживаемых пространств имён, соответствующим образом аннотируй поды.

```
...



metadata:



annotations:



...



oneagent.dynatrace.com/inject: "false"
```

Доступные аннотации для точной настройки включают следующие.

* `dynatrace.com/inject`: отключает всё внедрение, если задано значение `false`. При этом установка значения `true` не даёт эффекта, аннотация может использоваться только для исключения подов из внедрения.
* `metadata-enrichment.dynatrace.com/inject`: предотвращает добавление [файла обогащения метрик](/managed/ingest-from/extend-dynatrace/extend-data "Узнай, как автоматически обогащать данные телеметрии специфичными для Dynatrace полями."), если задано значение `false`.
* `oneagent.dynatrace.com/inject`: отключает изменения OneAgent, если задано значение `false`.
* `otlp-exporter-configuration.dynatrace.com/inject`: отключает [автоматическую настройку экспортёра OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматическая настройка экспортёра OTLP в приложениях, инструментированных SDKами OpenTelemetry, с помощью Dynatrace Operator."), если задано значение `false`.

## Исключение определённых контейнеров в отслеживаемых подах

Dynatrace Operator версии 1.0.0+

Чтобы исключить определённые образы контейнеров внутри отслеживаемых пространств имён, соответствующим образом аннотируй поды или DynaKube (это может быть полезно, например, для исключения sidecar-контейнеров).

```
...



metadata:



annotations:



...



container.inject.dynatrace.com/<container-name>: "false"
```

Эту аннотацию можно применить на **уровне DynaKube (влияет на все поды)** или на **уровне отдельного пода (влияет только на указанный под)**.

Это исключает контейнер из всех типов внедрения (OneAgent/метаданные)

## Мониторинг только определённых подов

Dynatrace Operator версии 0.8.0+

Dynatrace Operator можно настроить так, чтобы отслеживать пространства имён без внедрения в какие-либо поды, что позволяет самостоятельно выбирать, какие поды отслеживать.

1. Отключи функцию автоматического внедрения для развёртывания DynaKube в кластере.

   ```
   apiVersion: dynatrace.com/v1beta5



   kind: DynaKube



   metadata:



   name: dynakube



   namespace: dynatrace



   annotations:



   feature.dynatrace.com/automatic-injection: "false"



   spec:



   oneAgent:



   cloudNativeFullStack:



   namespaceSelector:



   matchLabels:



   dt-monitoring: "true"



   ...
   ```
2. Используй селекторы меток или ручные аннотации для пространств имён, которые нужно отслеживать выборочно.

   ```
   kubectl label namespace <my_namespace> dt-monitoring=true
   ```
3. Аннотируй поды, которые нужно отслеживать.

   * Работает с аннотациями `oneagent.dynatrace.com/inject`, `metadata-enrichment.dynatrace.com/inject` и `otlp-exporter-configuration.dynatrace.com/inject`.

   ```
   ...



   metadata:



   annotations:



   ...



   oneagent.dynatrace.com/inject: "true"
   ```

## Точная настройка внедрения для `applicationMonitoring` без CSI driver

Этот раздел признан устаревшим начиная с Dynatrace Operator версии 1.5.0 и заменён на [загрузку образа узла через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, загрузку образа через CSI driver и ZIP-загрузку.").

* `oneagent.dynatrace.com/flavor`: задай значение `default` или `musl`, чтобы указать совместимость бинарных файлов. Это определяет, какие бинарные файлы загружать, `glibc` или `musl`, по умолчанию используется `glibc`. Для контейнеров на основе `musl` (например, Alpine) укажи эту аннотацию, чтобы обеспечить корректный мониторинг.

  + Игнорируется, если используется том CSI или [загрузка образа узла через эфемерный том](/managed/ingest-from/setup-on-k8s/reference/code-modules-delivery-modes#ephemeral-node-image-pull "Справка о том, как Dynatrace Operator доставляет модули кода OneAgent в поды приложений, включая эфемерные тома, загрузку образа через CSI driver и ZIP-загрузку.").
* `oneagent.dynatrace.com/technologies`: список технологий через запятую. Фильтрует загружаемые модули кода, по умолчанию `all`. Используй эту аннотацию, чтобы настроить OneAgent на мониторинг определённых технологий внутри приложения.

  + Игнорируется, если используется том CSI.
* `oneagent.dynatrace.com/install-path`: задаёт путь, по которому будет смонтирован каталог OneAgent. По умолчанию установлено значение `/opt/dynatrace/oneagent-paas`. Скорректируй этот путь в соответствии со своим окружением или требованиями.

Ниже приведён пример, показывающий, как применить эти аннотации в развёртывании.

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"



oneagent.dynatrace.com/flavor: "musl"



oneagent.dynatrace.com/install-path: "/dynatrace"
```