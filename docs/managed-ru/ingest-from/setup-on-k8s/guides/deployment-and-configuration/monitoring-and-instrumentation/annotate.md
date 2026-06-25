---
title: Настройка мониторинга для пространств имён и подов
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate
scraped: 2026-05-12T11:37:42.018570
---

# Настройка мониторинга для пространств имён и подов

# Настройка мониторинга для пространств имён и подов

* Чтение: 5 мин
* Обновлено 19 марта 2026 г.

cloudNativeFullStack

applicationMonitoring

metadataEnrichment

В рамках мониторинга кластера Kubernetes с помощью cloud-native full-stack или application monitoring, при применении обогащения метаданными или автоматической настройке экспортёров OTLP вам может понадобиться ограничить его определёнными пространствами имён и подами.

По умолчанию Dynatrace Operator выполняет внедрение во **все пространства имён**, за исключением:

* Пространства имён с префиксом `kube-` или `openshift-`.
* Пространство имён, в котором был установлен Dynatrace Operator.

Настоятельно рекомендуем использовать поля `namespaceSelector` (см. ниже), чтобы сохранять полный контроль над тем, что внедряется.

## Мониторинг определённых пространств имён

При настройке Dynatrace Operator для внедрения OneAgent, применения обогащения метаданными или автоматической настройки экспортёров OTLP только в определённых пространствах имён задайте параметр `namespaceSelector` в пользовательском ресурсе DynaKube.

Описанные здесь `namespaceSelector` и аннотации влияют только на внедрение, выполняемое вебхук-частью Dynatrace Operator. Они не влияют на возможности мониторинга Kubernetes API в ActiveGate или мониторинг на уровне хоста, выполняемый OneAgent.

Дополнительные сведения см. в разделе [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.") (поля `.spec.metadataEnrichment`, `.spec.oneAgent.cloudNativeFullStack`, `.spec.oneAgent.applicationMonitoring` и `.spec.otlpExporterConfiguration`).

1. Добавьте метки к пространствам имён.

Kubernetes

OpenShift

```
kubectl label namespace <my_namespace> dt-monitoring=true
```

```
oc label namespace <my_namespace> dt-monitoring=true
```

2. Измените DynaKube, добавив `namespaceSelector`, чтобы указать метку для мониторинга.

Metadata enrichment

Cloud-native full-stack monitoring

Application monitoring

OTLP exporter configuration

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

Подробнее о настройке меток для выборочного мониторинга см. [Метки и селекторы](https://dt-url.net/vj038vk).

Чтобы добавить исключения для определённых подов в выбранных пространствах имён, можно [добавить аннотации к соответствующим подам](#podexclusion).

## Исключение определённых пространств имён

Чтобы исключить определённые пространства имён из мониторинга, измените пользовательский ресурс DynaKube следующим образом.

* `key` определяет ключ метки. Начиная с Kubernetes версии 1.22, к пространствам имён добавляется метка по умолчанию `kubernetes.io/metadata.name`.
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

Пример с меткой Kubernetes по умолчанию

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

Вебхук выполнит внедрение в каждое пространство имён, которое соответствует всем `namespaceselector`.

Подробнее см. [Ресурсы, поддерживающие требования на основе множеств](https://dt-url.net/hi03yvm).

## Исключение определённых подов в отслеживаемых пространствах имён

Чтобы исключить определённые поды в отслеживаемых пространствах имён, добавьте к подам соответствующие аннотации.

```
...



metadata:



annotations:



...



oneagent.dynatrace.com/inject: "false"
```

Для точного управления доступны следующие аннотации.

* `dynatrace.com/inject`: отключает всё внедрение, если задано значение `false`. Однако установка значения `true` не даёт никакого эффекта; аннотацию можно использовать только для исключения подов из внедрения.
* `metadata-enrichment.dynatrace.com/inject`: предотвращает добавление [файла обогащения метрик](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") при значении `false`.
* `oneagent.dynatrace.com/inject`: отключает изменения OneAgent, если задано значение `false`.
* `otlp-exporter-configuration.dynatrace.com/inject`: отключает [автоматическую настройку экспортёра OTLP](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config "Автоматически настройте экспортёр OTLP в приложениях, инструментированных с помощью OpenTelemetry SDK, используя Dynatrace Operator.") при значении `false`.

## Исключение определённых контейнеров в отслеживаемых подах

Dynatrace Operator версии 1.0.0+

Чтобы исключить определённые образы контейнеров в отслеживаемых пространствах имён, добавьте соответствующие аннотации к подам или DynaKube (это может быть полезно, например, для исключения sidecar-контейнеров).

```
...



metadata:



annotations:



...



container.inject.dynatrace.com/<container-name>: "false"
```

Эту аннотацию можно применить на **уровне DynaKube (затрагивает все поды)** или на **уровне отдельного пода (затрагивает только указанный под)**.

Это исключает контейнер из всех видов внедрения (OneAgent/метаданные)

## Мониторинг только определённых подов

Dynatrace Operator версии 0.8.0+

Dynatrace Operator можно настроить на мониторинг пространств имён без внедрения в какие-либо поды, чтобы вы могли выбрать, какие поды отслеживать.

1. Отключите функцию автоматического внедрения для развёртывания DynaKube в вашем кластере.

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
2. Используйте селекторы меток или аннотации вручную для пространств имён, которые нужно отслеживать выборочно.

   ```
   kubectl label namespace <my_namespace> dt-monitoring=true
   ```
3. Добавьте аннотации к подам, которые вы собираетесь отслеживать.

   * Работает с аннотациями `oneagent.dynatrace.com/inject`, `metadata-enrichment.dynatrace.com/inject` и `otlp-exporter-configuration.dynatrace.com/inject`.

   ```
   ...



   metadata:



   annotations:



   ...



   oneagent.dynatrace.com/inject: "true"
   ```

## Тонкая настройка внедрения для `applicationMonitoring` без CSI driver

Этот раздел устарел с версии Dynatrace Operator 1.5.0 и был заменён новой функцией [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка node image pull").

* `oneagent.dynatrace.com/flavor`: задайте значение `default` или `musl`, чтобы указать двоичную совместимость. Это определяет, какие двоичные файлы следует загружать, `glibc` или `musl`, при этом `glibc` является настройкой по умолчанию. Для контейнеров на основе `musl` (например, Alpine) укажите эту аннотацию, чтобы обеспечить корректный мониторинг.

  + Игнорируется, если используется том CSI или функция [node image pull](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/node-image-pull "Настройка node image pull").
* `oneagent.dynatrace.com/technologies`: список технологий, разделённых запятыми. Это фильтрует загружаемые модули кода, при этом значением по умолчанию является `all`. Используйте это, чтобы настроить OneAgent на мониторинг определённых технологий в вашем приложении.

  + Игнорируется, если используется том CSI.
* `oneagent.dynatrace.com/install-path`: указывает путь, по которому будет смонтирован каталог OneAgent. По умолчанию задано значение `/opt/dynatrace/oneagent-paas`. Скорректируйте этот путь в соответствии с вашим окружением или требованиями.

Ниже приведён пример, показывающий, как применить эти аннотации в вашем развёртывании.

```
...



metadata:



annotations:



oneagent.dynatrace.com/technologies: "java,nginx"



oneagent.dynatrace.com/flavor: "musl"



oneagent.dynatrace.com/install-path: "/dynatrace"
```