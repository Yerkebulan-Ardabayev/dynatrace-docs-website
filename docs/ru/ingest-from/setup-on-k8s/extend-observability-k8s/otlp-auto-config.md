---
title: Включение автоматической настройки экспортера OpenTelemetry OTLP
source: https://www.dynatrace.com/docs/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config
scraped: 2026-03-06T21:36:30.633862
---

# Включение автоматической конфигурации экспортёра OpenTelemetry OTLP

# Включение автоматической конфигурации экспортёра OpenTelemetry OTLP

* Latest Dynatrace
* Опубликовано 24 ноября 2025

Dynatrace Operator версии 1.8.0+

Dynatrace Operator может автоматически настраивать экспортёр OpenTelemetry OTLP для приложений, инструментированных с помощью [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/). Это выполняется путём внедрения переменных окружения в поды вашего приложения при запуске, что позволяет отправлять данные телеметрии напрямую в Dynatrace.

## Включение автоконфигурации OTLP

### Предоставление токена для загрузки данных

Вам необходимо предоставить [токен для загрузки данных](../deployment/tokens-permissions.md#dataIngestToken "Настройте токены и разрешения для мониторинга вашего кластера Kubernetes") для Dynatrace Operator. Этот токен передаётся вашему приложению как часть конфигурации экспортёра OTLP.

### Обновление ресурса DynaKube

Добавьте раздел `otlpExporterConfiguration` в ваш пользовательский ресурс DynaKube. Это включает автоконфигурацию для всех сигналов (метрики, трассировки, логи):

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



signals:



metrics: {}



traces: {}



logs: {}
```

Вы можете включить внедрение для каждого типа сигнала (метрики, трассировки, логи) отдельно.

**Примечание**: По умолчанию, если какая-либо переменная окружения `OTEL_EXPORTER_OTLP_*` уже присутствует в спецификации контейнера, Dynatrace Operator пропустит внедрение конфигурации конечной точки (т.е. `OTEL_EXPORTER_OTLP_*`) — даже если существующая конфигурация не пересекается с тем, что было бы добавлено автоматически. Чтобы разрешить Dynatrace Operator переопределять существующую конфигурацию, включите [режим переопределения](#override). Атрибуты ресурсов (`OTEL_RESOURCE_ATTRIBUTES`) не затрагиваются этой логикой и по-прежнему будут установлены или расширены.

### Проверка автоконфигурации

Если автоконфигурация OTLP была успешно внедрена, под вашего приложения получит следующую аннотацию:

```
otlp-exporter-configuration.dynatrace.com/injected: "true"
```

Если что-то пошло не так, под будет аннотирован причиной сбоя:

```
otlp-exporter-configuration.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/reason: <reason>
```

## Внедряемая конфигурация OTLP

### Переменные окружения

Следующие переменные окружения внедряются в контейнеры вашего приложения:

| Переменная | Значение |
| --- | --- |
| `DT_API_TOKEN` | `dataIngestToken, предоставленный пользователем` |
| `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/traces` |
| `OTEL_EXPORTER_OTLP_TRACES_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_TRACES_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/metrics` |
| `OTEL_EXPORTER_OTLP_METRICS_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_METRICS_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE` | `delta` |
| `OTEL_EXPORTER_OTLP_LOGS_ENDPOINT` | `https://<tenant-uid>.live.dynatrace.com/api/v2/otlp/v1/logs` |
| `OTEL_EXPORTER_OTLP_LOGS_PROTOCOL` | `http/protobuf` |
| `OTEL_EXPORTER_OTLP_LOGS_HEADERS` | `authorization=Api-Token $(DT_API_TOKEN)` |
| `OTEL_RESOURCE_ATTRIBUTES` | `k8s.cluster.name=dynakube,k8s.container.name=app ...` |

### Атрибуты ресурсов

Dynatrace Operator добавляет атрибуты ресурсов в `OTEL_RESOURCE_ATTRIBUTES` для обогащения данных OpenTelemetry, предоставляя топологию и дополнительный контекст для точек данных для полноценного взаимодействия с Dynatrace:

* `k8s.cluster.name`
* `k8s.container.name`
* `k8s.workload.name`
* `k8s.cluster.uid`
* `k8s.pod.name`
* `k8s.pod.uid`
* `k8s.node.name`
* `k8s.namespace.name`
* `k8s.workload.kind`
* `dt.kubernetes.cluster.id`
* `dt.entity.kubernetes_cluster`

Значения для этих атрибутов получаются из метаданных кластера и подов. Кроме того, применяются [правила обогащения метаданными](../guides/metadata-automation/k8s-metadata-telemetry-enrichment.md#enrichment-options "Руководства по обогащению телеметрии в Kubernetes"), определённые в вашем тенанте, для дополнительного улучшения атрибутов ресурсов. Также все метаданные, предоставленные в аннотациях `metadata.dynatrace.com/<key>: <value>` на пространстве имён или на внедрённом поде, добавляются как атрибуты ресурсов.

Любые атрибуты, которые вы уже установили в `OTEL_RESOURCE_ATTRIBUTES`, сохраняются, а вышеуказанные атрибуты добавляются к ним.

Атрибуты ресурсов всегда внедряются, когда автоконфигурация включена, независимо от существующих настроек экспортёра OTLP или того, включён ли режим переопределения.

## Ограничения

### Поды приложений, использующие `envFrom`

Когда вы заполняете переменные окружения с помощью `envFrom`, Dynatrace Operator не может обнаружить уже установленные переменные окружения. В этом случае внедрённая конфигурация экспортёра Dynatrace OTLP имеет приоритет над значениями из `envFrom`, даже без использования [режима переопределения](#override).

### Жёстко заданная конфигурация SDK

* В OTel SDK программная конфигурация имеет приоритет над переменными окружения. Убедитесь, что стандартные переменные окружения экспортёра поддерживаются вашим приложением.
* Dynatrace всегда использует протокол `http/protobuf`. Если ваше приложение ограничено gRPC, внедрённая переменная протокола не будет иметь эффекта и связь не будет установлена.

## Маршрутизация трафика OTLP через ActiveGate

Если ActiveGate развёрнут в кластере с тем же DynaKube, который используется для автоконфигурации OTLP, трафик маршрутизируется через этот ActiveGate. Без ActiveGate в кластере трафик отправляется напрямую в ваш тенант Dynatrace.

## Управление секретами

Следующие секреты создаются в каждом пространстве имён с внедрением:

* `dynatrace-otlp-exporter-certs` содержит сертификаты, необходимые для связи с настроенной конечной точкой, которой является одна из следующих:

  + TLS-сертификат для ActiveGate.
  + То, что установлено в `.spec.trustedCAs`, если API тенанта используется как конечная точка.
* `dynatrace-otlp-exporter-config` содержит копию токена для загрузки данных.

Секреты обновляются автоматически при изменении токена или сертификата, но только новые поды получат обновлённые значения. Перезапустите поды вашего приложения после изменения, чтобы избежать проблем с аутентификацией или связью.

**Примечание**: Если секреты не создаются достаточно быстро или временно недоступны по другим причинам, внедрение конфигурации экспортёра OTLP [будет пропущено](#verify-config).

## Управление внедрением

### Селектор пространств имён

Чтобы ограничить автоконфигурацию определёнными пространствами имён, вы можете использовать селектор пространств имён:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



namespaceSelector:



matchLabels:



my.app.com/otel: "true"



signals:



metrics: {}



traces: {}



logs: {}
```

### Аннотации подов и контейнеров

Для детального управления вы можете использовать аннотации для управления поведением внедрения непосредственно на подах:

* `feature.dynatrace.com/automatic-injection: false` (на DynaKube) отключает автоматическое внедрение модулей кода, обогащение метаданными и автоконфигурацию экспортёра OTLP по умолчанию.
* `dynatrace.com/inject: true/false` (на поде) включает/отключает внедрение для каждого пода.
* `otlp-exporter-configuration.dynatrace.com/inject: true/false` (на поде) включает/отключает внедрение для каждого пода.
* `container.inject.dynatrace.com/<container-name>: false` (на поде или DynaKube) отключает внедрение для определённых контейнеров.

| `feature.dynatrace.com/automatic-injection` | `dynatrace.com/inject` | `otlp-exporter-configuration.dynatrace.com/inject` | Внедрено |
| --- | --- | --- | --- |
| true (по умолчанию) | true/не задано | true | да |
| true (по умолчанию) | true/не задано | false | да |
| true (по умолчанию) | false | true | да |
| true (по умолчанию) | false | false | нет |
| false | true | true | да |
| false | true | false | да |
| false | false/не задано | true | да |
| false | false/не задано | false | нет |

## Включение переопределения переменных окружения

По умолчанию любая существующая конфигурация (например, уже установленные переменные окружения) не изменяется, не перезаписывается и не удаляется. Это включает все переменные окружения, соответствующие шаблону `OTEL_EXPORTER_OTLP_*`. Если любая из этих переменных окружения уже существует в спецификации контейнера, автоматическая конфигурация **вообще** не выполняется, даже если активированный сигнал не конфликтует напрямую с существующей конфигурацией.

Например, если в `.spec.otlpExporterConfiguration.signals` активированы только `traces`, а контейнер уже имеет `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` не будет сконфигурирован на вашем поде.

Чтобы включить это переопределение, вы можете активировать режим переопределения:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl: https://<environment-id>.live.dynatrace.com/api



otlpExporterConfiguration:



signals:



metrics: {}



overrideEnvVars: true
```

С `.spec.otlpExporterConfiguration.overrideEnvVars: true` Dynatrace Operator будет:

* Добавлять конфигурацию для сигналов, которых ещё нет (в данном примере `metrics`)
* Перезаписывать конфигурацию для уже существующих сигналов
* Сохранять существующие конфигурации, если они не конфликтуют с настроенными сигналами

Следующие примеры используют вышеуказанную конфигурацию DynaKube с включённым `metrics` и `overrideEnvVars`, установленным в `true`.

### Простое переопределение

**До**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: grpc



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token 123456
```

**После**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

### Простое добавление нового сигнала

**До**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_TRACES_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_TRACES_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_TRACES_HEADERS



value: authorization=Api-Token 123456
```

**После**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_TRACES_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_TRACES_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_TRACES_HEADERS



value: authorization=Api-Token 123456



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

### Общие переменные окружения конфигурации OTLP

Особый случай — использование `OTEL_EXPORTER_OTLP_ENDPOINT` и сопутствующих переменных окружения. Эти переменные предоставляют значения по умолчанию для всех сигналов одновременно. Если такая переменная уже установлена для контейнера, она не удаляется. Вместо этого добавляется конфигурация для конкретного сигнала, которая имеет приоритет.

В этом примере метрики теперь будут отправляться на конечную точку Dynatrace, в то время как трассировки и логи будут по-прежнему отправляться на ранее настроенную конечную точку.

**До**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_HEADERS



value: authorization=Api-Token 123456
```

**После**

```
spec:



containers:



- env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://my-private-endpoint/otlp/v1/traces



- name: OTEL_EXPORTER_OTLP_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_HEADERS



value: authorization=Api-Token 123456



- name: OTEL_EXPORTER_OTLP_METRICS_ENDPOINT



value: https://<environment-id>.live.dynatrace.com/api/v2/otlp/v1/metrics



- name: OTEL_EXPORTER_OTLP_METRICS_PROTOCOL



value: http/protobuf



- name: OTEL_EXPORTER_OTLP_METRICS_HEADERS



value: authorization=Api-Token $(DT_API_TOKEN)
```

## Поддержка `NO_PROXY`

Если у вас настроен ActiveGate и прокси-сервер на подах вашего приложения, сервис ActiveGate автоматически добавляется в переменную окружения `NO_PROXY`. Если переменная окружения ещё не существует, она будет создана.

Вы можете отказаться от этого, добавив следующую аннотацию к вашему DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/otlp-exporter-configuration-set-no-proxy: "false"
```

## Связанные темы

* [Параметры DynaKube для Dynatrace Operator](../reference/dynakube-parameters.md "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")