---
title: Настройка автоматической конфигурации экспортера OpenTelemetry OTLP
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config
---

# Настройка автоматической конфигурации экспортера OpenTelemetry OTLP

# Настройка автоматической конфигурации экспортера OpenTelemetry OTLP

* Практическое руководство
* Опубликовано 24 ноя 2025

Dynatrace Operator может автоматически настраивать экспортер OpenTelemetry OTLP для приложений, инструментированных с помощью [OpenTelemetry SDK﻿](https://opentelemetry.io/docs/languages/). Это делается путём внедрения переменных окружения в поды приложений при запуске, что позволяет отправлять данные телеметрии напрямую в Dynatrace.

Dynatrace Operator версии 1.8.0+

## Включение автоконфигурации OTLP

### Предоставление токена приёма данных

Нужно предоставить [токен приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes") оператору Dynatrace Operator. Этот токен передаётся приложению как часть конфигурации экспортера OTLP.

### Обновление ресурса DynaKube

Нужно добавить раздел `otlpExporterConfiguration` в пользовательский ресурс DynaKube. Это включает автоконфигурацию для всех сигналов (метрики, трейсы, логи):

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

Включение внедрения можно настроить отдельно для каждого типа сигнала (метрики, трейсы, логи).

В каждом [пространстве имён с внедрением](#namespace-selector) создаются следующие секреты:

* `dynatrace-otlp-exporter-certs` содержит сертификаты, необходимые для взаимодействия с настроенной конечной точкой, которой является одно из следующего:

  + TLS-сертификат для ActiveGate.
  + Сертификаты, содержащиеся в `.spec.trustedCAs`, если они предоставлены и нет доступного ActiveGate с TLS-сертификатами.
* `dynatrace-otlp-exporter-config` содержит копию [токена приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions "Настройка токенов и разрешений для мониторинга кластера Kubernetes").

Секреты обновляются автоматически при изменении токена или сертификата, но обновлённые значения получат только новые поды. После изменения нужно перезапустить поды приложений, чтобы избежать проблем с аутентификацией или взаимодействием.

**Примечания**:

* Конфигурация экспортера OTLP [пропускается](#verify-config), если предварительные условия не выполнены.
* По умолчанию, если в спецификации контейнера уже присутствует какая-либо переменная окружения `OTEL_EXPORTER_OTLP_*`, Dynatrace Operator пропускает внедрение конфигурации конечной точки (то есть `OTEL_EXPORTER_OTLP_*`), даже если существующая конфигурация не пересекается с тем, что было бы добавлено автоматически. Чтобы разрешить Dynatrace Operator переопределять существующую конфигурацию, нужно включить [режим переопределения](#override). Атрибуты ресурса (`OTEL_RESOURCE_ATTRIBUTES`) этой логикой не затрагиваются и всё равно будут установлены или расширены.

### Проверка автоконфигурации

Если автоконфигурация OTLP была успешно внедрена, под приложения получает следующую аннотацию:

```
otlp-exporter-configuration.dynatrace.com/injected: "true"
```

Если что-то пошло не так, под аннотируется причиной сбоя:

```
otlp-exporter-configuration.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/reason: <reason>
```

## Внедрённая конфигурация OTLP

### Переменные Environment

В контейнеры приложений внедряются следующие переменные окружения:

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

### Атрибуты ресурса

Dynatrace Operator добавляет атрибуты ресурса в `OTEL_RESOURCE_ATTRIBUTES`, чтобы обогатить данные OpenTelemetry информацией о топологии и дополнительным контекстом для точек данных ради насыщенного опыта работы с Dynatrace:

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

Значения этих атрибутов выводятся из метаданных кластера и пода. Кроме того, все метаданные, указанные в аннотациях `metadata.dynatrace.com/<key>: <value>` на пространстве имён или на поде с внедрением, добавляются как атрибуты ресурса.

Любые атрибуты, уже установленные в `OTEL_RESOURCE_ATTRIBUTES`, сохраняются, а перечисленные выше атрибуты добавляются к ним.

Атрибуты ресурса всегда внедряются при включённой автоконфигурации, независимо от существующих настроек экспортера OTLP и от того, включён ли режим переопределения.

### Дополнительные атрибуты ресурса

Dynatrace Operator версии 1.10+

Можно определить дополнительные атрибуты ресурса в DynaKube, которые Dynatrace Operator добавит в `OTEL_RESOURCE_ATTRIBUTES` наряду с автоматически выведенными атрибутами. Полное описание полей, детали распространения и известные ограничения смотрите в разделе [Настройка атрибутов ресурса в DynaKube](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment#resource-attributes "Настройка обогащения метаданных в Dynatrace Operator для присоединения метаданных Kubernetes к сигналам телеметрии с помощью OneAgent, экспортера OTLP или автономного обогащения.").

## Ограничения

### Поды приложений, использующие `envFrom`

Если переменные окружения заполняются с помощью `envFrom`, Dynatrace Operator не может обнаружить уже установленные переменные окружения. В этом случае внедрённая конфигурация экспортера OTLP Dynatrace имеет приоритет над значениями из `envFrom`, даже без использования [режима переопределения](#override).

### Жёстко заданная конфигурация SDK

* В SDK OTel программная конфигурация имеет приоритет над переменными окружения. Нужно убедиться, что приложение поддерживает стандартные переменные окружения экспортера.
* Dynatrace всегда использует протокол `http/protobuf`. Если приложение ограничено gRPC, внедрённая переменная протокола не будет иметь эффекта, и взаимодействие завершится сбоем.

## Маршрутизация трафика OTLP через ActiveGate

Если внутрикластерный ActiveGate развёрнут с тем же DynaKube, который используется для автоконфигурации OTLP, трафик маршрутизируется через этот ActiveGate. Без внутрикластерного ActiveGate трафик отправляется напрямую в тенант Dynatrace.

## Управление внедрением

### Селектор пространства имён

Чтобы ограничить автоконфигурацию конкретными пространствами имён, можно использовать селектор пространства имён:

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



example.com/source: otel



signals:



metrics: {}



traces: {}



logs: {}
```

### Аннотации пода и контейнера

Для более точного управления, выходящего за рамки [селектора пространства имён](#namespace-selector), можно использовать аннотации для управления поведением внедрения непосредственно на подах:

По умолчанию автоматическое внедрение и, соответственно, автоконфигурация экспортера OTLP включены для всех пространств имён (управляется через [feature-flag](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "Список feature-флагов для настройки Dynatrace Operator на Kubernetes.")).

Управлять автоконфигурацией экспортера OTLP можно либо с помощью существующих аннотаций, которые управляют сразу всеми внедрениями Dynatrace (подробнее в [документации](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#podexclusion "Настройка мониторинга для пространств имён и подов")), либо добавив к поду аннотацию `otlp-exporter-configuration.dynatrace.com/inject: true/false`.

Известная несогласованность в Dynatrace Operator 1.8

Есть известная несогласованность в том, как эти флаги работают между внедрением конфигурации экспортера OTLP и внедрением OneAgent. Значение `feature.dynatrace.com/inject` используется как значение по умолчанию для `dynatrace.com/inject`, при этом аннотация `otlp-exporter-configuration.dynatrace.com/inject` по умолчанию равна `true`. Это будет исправлено в следующем релизе Dynatrace Operator.

Комбинации флагов внедрения

| `dynatrace.com/inject` [1](#fn-1-1-def) | `otlp-exporter-configuration.dynatrace.com/inject` [2](#fn-1-2-def) | `feature.dynatrace.com/automatic-injection` [3](#fn-1-3-def) | Внедрено |
| --- | --- | --- | --- |
| `false` | <n/a> | <n/a> | Неприменимоне внедрено |
| `true` / не задано [4](#fn-1-4-def) | `false` | <n/a> | Неприменимоне внедрено |
| `true` / не задано [4](#fn-1-4-def) | `true` | <n/a> | Применимовнедрено |
| `true` / не задано [4](#fn-1-4-def) | не задано [5](#fn-1-5-def) | `true` / не задано [4](#fn-1-4-def) | Применимовнедрено |
| `true` / не задано [4](#fn-1-4-def) | не задано [5](#fn-1-5-def) | `false` | Неприменимоне внедрено |

[1](#fn-1-1-def) задаётся на поде приложения

[2](#fn-1-2-def) задаётся на поде приложения

[3](#fn-1-3-def) задаётся на DynaKube

[4](#fn-1-4-def) по умолчанию `true`

[5](#fn-1-5-def) значение `feature.dynatrace.com/automatic-injection`, используемое по умолчанию

## Включение переопределения переменных окружения

По умолчанию любая существующая конфигурация (например, уже установленные переменные окружения) не изменяется, не перезаписывается и не удаляется. Это касается всех переменных окружения, соответствующих шаблону `OTEL_EXPORTER_OTLP_*`. Если какие-либо из этих переменных окружения уже существуют в спецификации контейнера, автоматическая настройка не производится **вообще**, даже если активированный сигнал напрямую не конфликтует с существующей конфигурацией.

Например, если в `.spec.otlpExporterConfiguration.signals` активирован только `traces`, а в контейнере уже установлена переменная `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT`, переменная `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` не будет настроена в поде.

Чтобы включить это переопределение, можно активировать режим переопределения:

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

* Добавлять конфигурацию для сигналов, которые ещё не заданы (в этом примере, `metrics`)
* Перезаписывать конфигурацию для сигналов, которые уже заданы
* Сохранять существующие конфигурации, если они не конфликтуют с настроенными сигналами

В следующих примерах используется указанная выше конфигурация DynaKube с включённым `metrics` и `overrideEnvVars`, установленным в `true`.

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

### Переменные окружения общей конфигурации OTLP

Особый случай, это использование `OTEL_EXPORTER_OTLP_ENDPOINT` и сопутствующих ей переменных окружения. Эти переменные задают значения по умолчанию сразу для всех сигналов. Если такая переменная уже установлена для контейнера, она не удаляется. Вместо этого добавляется конфигурация, специфичная для конкретного сигнала, и она получает приоритет.

В этом примере метрики теперь будут отправляться на Dynatrace endpoint, в то время как трассировки и логи по-прежнему будут передаваться на ранее настроенный endpoint.

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

Если на подах приложения настроены и ActiveGate, и прокси, служба ActiveGate автоматически добавляется в переменную окружения `NO_PROXY`. Если эта переменная окружения ещё не существует, она будет создана.

Можно отказаться от этого поведения, добавив следующую аннотацию в DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/otlp-exporter-configuration-set-no-proxy: "false"
```

## Похожие темы

* [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator на Kubernetes.")