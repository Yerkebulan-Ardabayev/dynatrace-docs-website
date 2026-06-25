---
title: Включение автоматической настройки экспортёра OpenTelemetry OTLP
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config
scraped: 2026-05-12T12:03:40.512966
---

# Включение автоматической настройки экспортёра OpenTelemetry OTLP

# Включение автоматической настройки экспортёра OpenTelemetry OTLP

* Опубликовано 24 ноября 2025 г.

Dynatrace Operator version 1.8.0+

Dynatrace Operator может автоматически настраивать экспортёр OpenTelemetry OTLP для приложений, инструментированных с помощью [OpenTelemetry SDK](https://opentelemetry.io/docs/languages/). Это делается путём внедрения переменных окружения в поды вашего приложения при запуске, что позволяет отправлять данные телеметрии напрямую в Dynatrace.

## Включение автонастройки OTLP

### Предоставьте токен приёма данных

Необходимо предоставить [токен приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes") в Dynatrace Operator. Этот токен передаётся вашему приложению как часть настройки экспортёра OTLP.

### Обновите ваш ресурс DynaKube

Добавьте раздел `otlpExporterConfiguration` в ваш пользовательский ресурс DynaKube. Это включает автонастройку для всех сигналов (метрик, трассировок, логов):

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

Внедрение можно включать для каждого типа сигнала (метрики, трассировки, логи) отдельно.

Следующие секреты создаются в каждом [пространстве имён с внедрением](#namespace-selector):

* `dynatrace-otlp-exporter-certs` содержит сертификаты, необходимые для взаимодействия с настроенной конечной точкой, которая является одной из следующих:

  + TLS-сертификат для ActiveGate.
  + Сертификаты, содержащиеся в `.spec.trustedCAs`, если они предоставлены и недоступен ActiveGate с TLS-сертификатами.
* `dynatrace-otlp-exporter-config` содержит копию [токена приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

Секреты обновляются автоматически при изменении токена или сертификата, но обновлённые значения получат только новые поды. Перезапустите поды вашего приложения после изменения, чтобы избежать проблем с аутентификацией или взаимодействием.

**Примечания**:

* Настройка экспортёра OTLP [пропускается](#verify-config), если не выполнены предварительные требования.
* По умолчанию, если в спецификации контейнера уже присутствует какая-либо переменная окружения `OTEL_EXPORTER_OTLP_*`, Dynatrace Operator пропустит внедрение настройки конечной точки (то есть `OTEL_EXPORTER_OTLP_*`), даже если существующая настройка не пересекается с тем, что было бы добавлено автоматически. Чтобы разрешить Dynatrace Operator переопределять существующую настройку, включите [режим переопределения](#override). На атрибуты ресурсов (`OTEL_RESOURCE_ATTRIBUTES`) эта логика не влияет, они по-прежнему будут заданы или дополнены.

### Проверьте автонастройку

Если автонастройка OTLP была успешно внедрена, под вашего приложения получает следующую аннотацию:

```
otlp-exporter-configuration.dynatrace.com/injected: "true"
```

Если что-то идёт не так, под аннотируется причиной сбоя:

```
otlp-exporter-configuration.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/reason: <reason>
```

## Внедрённая настройка OTLP

### Переменные окружения

В контейнеры вашего приложения внедряются следующие переменные окружения:

| Переменная | Значение |
| --- | --- |
| `DT_API_TOKEN` | `dataIngestToken provided by user` |
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

Dynatrace Operator добавляет атрибуты ресурсов в `OTEL_RESOURCE_ATTRIBUTES`, чтобы обогатить данные OpenTelemetry, предоставляя топологию и дополнительный контекст для точек данных ради насыщенного опыта работы с Dynatrace:

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

Значения этих атрибутов выводятся из метаданных кластера и пода. Кроме того, все метаданные, указанные в аннотациях `metadata.dynatrace.com/<key>: <value>` на пространстве имён или на поде с внедрением, добавляются как атрибуты ресурсов.

Все атрибуты, которые вы уже задали в `OTEL_RESOURCE_ATTRIBUTES`, сохраняются, а перечисленные выше атрибуты добавляются к ним.

Атрибуты ресурсов всегда внедряются при включённой автонастройке, независимо от существующих настроек экспортёра OTLP и от того, включён ли режим переопределения.

## Ограничения

### Поды приложений, использующие `envFrom`

Когда вы заполняете переменные окружения с помощью `envFrom`, Dynatrace Operator не может обнаружить уже заданные переменные окружения. В этом случае внедрённая настройка экспортёра Dynatrace OTLP имеет приоритет над значениями из `envFrom`, даже без использования [режима переопределения](#override).

### Жёстко заданная настройка SDK

* В OTel SDK программная настройка имеет приоритет над переменными окружения. Убедитесь, что стандартные переменные окружения экспортёра поддерживаются вашим приложением.
* Dynatrace всегда использует протокол `http/protobuf`. Если ваше приложение ограничено протоколом gRPC, внедрённая переменная протокола не будет иметь эффекта, и взаимодействие завершится сбоем.

## Маршрутизация трафика OTLP через ActiveGate

Если ActiveGate внутри кластера развёрнут с тем же DynaKube, который используется для автонастройки OTLP, трафик маршрутизируется через этот ActiveGate. Без ActiveGate внутри кластера трафик отправляется напрямую в ваш тенант Dynatrace.

## Управление внедрением

### Селектор пространств имён

Чтобы ограничить автонастройку определёнными пространствами имён, можно использовать селектор пространств имён:

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

Для более точного управления помимо [селектора пространств имён](#namespace-selector) можно использовать аннотации, чтобы управлять поведением внедрения непосредственно на подах:

По умолчанию автоматическое внедрение и, следовательно, автонастройка экспортёра OTLP включены для всех пространств имён (управляется через [флаг функции](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "Список feature flags для настройки Dynatrace Operator в Kubernetes.")).

Управлять автонастройкой экспортёра OTLP можно либо с помощью существующих аннотаций, которые управляют всеми внедрениями Dynatrace одновременно (см. [документацию](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#podexclusion "Настройка мониторинга для пространств имён и подов") для получения дополнительной информации), либо добавив `otlp-exporter-configuration.dynatrace.com/inject: true/false` к поду.

Известная несогласованность в Dynatrace Operator 1.8

Существует известная несогласованность в том, как эти флаги работают между внедрением настройки экспортёра OTLP и внедрением OneAgent. Значение `feature.dynatrace.com/inject` используется как значение по умолчанию для `dynatrace.com/inject`, а аннотация `otlp-exporter-configuration.dynatrace.com/inject` по умолчанию имеет значение `true`. Это будет исправлено в следующем выпуске Dynatrace Operator.

Комбинации флагов внедрения

| `dynatrace.com/inject` [1](#fn-1-1-def) | `otlp-exporter-configuration.dynatrace.com/inject` [2](#fn-1-2-def) | `feature.dynatrace.com/automatic-injection` [3](#fn-1-3-def) | Внедрено |
| --- | --- | --- | --- |
| `false` | <n/a> | <n/a> | Неприменимоне внедрено |
| `true` / unset [4](#fn-1-4-def) | `false` | <n/a> | Неприменимоне внедрено |
| `true` / unset [4](#fn-1-4-def) | `true` | <n/a> | Применимовнедрено |
| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `true` / unset [4](#fn-1-4-def) | Применимовнедрено |
| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `false` | Неприменимоне внедрено |

[1](#fn-1-1-def) задаётся на поде приложения

[2](#fn-1-2-def) задаётся на поде приложения

[3](#fn-1-3-def) задаётся на DynaKube

[4](#fn-1-4-def) по умолчанию `true`

[5](#fn-1-5-def) значение `feature.dynatrace.com/automatic-injection` используется по умолчанию

## Включение переопределений переменных окружения

По умолчанию любая существующая настройка (например, уже заданные переменные окружения) не изменяется, не перезаписывается и не удаляется. Это включает все переменные окружения, соответствующие шаблону `OTEL_EXPORTER_OTLP_*`. Если какая-либо из этих переменных окружения уже существует в спецификации контейнера, автоматическая настройка не выполняется **вообще**, даже если активированный сигнал напрямую не конфликтует с существующей настройкой.

Например, если в `.spec.otlpExporterConfiguration.signals` активированы только `traces`, а в контейнере уже задана `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, то `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` не будет настроена на вашем поде.

Чтобы включить это переопределение, можно включить режим переопределения:

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

При `.spec.otlpExporterConfiguration.overrideEnvVars: true` Dynatrace Operator будет:

* Добавлять настройку для сигналов, которые ещё отсутствуют (в этом примере `metrics`)
* Перезаписывать настройку для уже присутствующих сигналов
* Сохранять существующие настройки, если они не конфликтуют с настроенными сигналами

В следующих примерах используется приведённая выше конфигурация DynaKube с включёнными `metrics` и `overrideEnvVars`, установленным в `true`.

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

### Переменные окружения общей настройки OTLP

Особый случай, это использование `OTEL_EXPORTER_OTLP_ENDPOINT` и сопутствующих ему переменных окружения. Эти переменные задают значения по умолчанию сразу для всех сигналов. Если такая переменная уже задана для контейнера, она не удаляется. Вместо этого добавляется настройка для конкретного сигнала, и она имеет приоритет.

В этом примере метрики теперь будут отправляться в конечную точку Dynatrace, а трассировки и логи по-прежнему будут отправляться в ранее настроенную конечную точку.

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

Если вы решите настроить ActiveGate и прокси на подах вашего приложения, сервис ActiveGate автоматически добавляется в переменную окружения `NO_PROXY`. Если эта переменная окружения ещё не существует, она будет создана.

От этого можно отказаться, добавив следующую аннотацию в ваш DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/otlp-exporter-configuration-set-no-proxy: "false"
```

## Связанные темы

* [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")