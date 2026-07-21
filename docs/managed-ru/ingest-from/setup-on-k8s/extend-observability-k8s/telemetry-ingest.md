---
title: Включение конечных точек приёма телеметрии Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest
---

# Включение конечных точек приёма телеметрии Dynatrace

# Включение конечных точек приёма телеметрии Dynatrace

* Обновлено 04 нояб. 2025 г.

Dynatrace Operator версии 1.6+

Включение конечных точек приёма телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.

* Приём данных через конечные точки [OTLP﻿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger﻿](https://www.jaegertracing.io/), [StatsD﻿](https://github.com/statsd/statsd) или [Zipkin﻿](https://zipkin.io/)
* Анализ насыщенных контекстом данных со встроенными приложениями, DQL, Notebooks и Dashboards

## Предварительные требования

* Для [токена приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes") нужны области действия токена `openTelemetryTrace.ingest`, `logs.ingest` и `metrics.ingest`, и он должен быть указан в поле `dataIngestToken` в том же [секрете](/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed#create-secret-helm "Развёртывание Dynatrace Operator для observability Kubernetes."), что и токен API.

## Настройка и использование

Ниже описано, как настроить и использовать конечные точки приёма телеметрии, в два шага.

Подключение приложения Kubernetes

Если DynaKube получен с [экрана подключения приложения Dynatrace Kubernetes](/managed/ingest-from/setup-on-k8s/quickstart "Развёртывание Dynatrace Operator в Kubernetes"), имя сервиса приёма телеметрии будет установлено в `telemetry-ingest.dynatrace`. Как изменить его, см. в разделе [Настройка имени сервиса приёма телеметрии](#customize-the-service-name).

1. Создание DynaKube

Чтобы включить конечные точки приёма телеметрии, нужно указать список желаемых протоколов в поле DynaKube `.spec.telemetryIngest.protocols`. Подробнее о точных значениях см. в документации [справочника DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#telemetry-ingest-v1beta5 "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

Маршрутизация данных

При запущенном ActiveGate в кластере Kubernetes [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии от OpenTelemetry.") будет настроен на маршрутизацию всех принимаемых данных через инстанс ActiveGate внутри кластера, вместо прямого подключения к публичному ActiveGate. Кроме того, возможности, необходимые для приёма телеметрии, будут включены автоматически.

Если ActiveGate внутри кластера не развёрнут (то есть `.spec.activeGate` не указан), OpenTelemetry Collector будет настроен на прямое взаимодействие с тенантом Dynatrace.

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl:  https://ENVIRONMENTID.live.dynatrace.com/api



activeGate:



capabilities:



- kubernetes-monitoring



replicas: 1



resources:



requests:



cpu: 500m



memory: 1.5Gi



limits:



cpu: 1000m



memory: 1.5Gi



telemetryIngest:



protocols:



- jaeger



- zipkin



- otlp



- statsd



templates:



otelCollector:



imageRef:



repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



tag: <tag>
```

Образ OTel collector

Образ OTel collector берётся из наших [поддерживаемых публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator на использование образов из публичного реестра для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение по окружению Dynatrace."), нужно убедиться, что используемый `tag` существует! Также можно использовать [приватный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование приватного реестра").

2. Настройка приложений

После применения DynaKube Dynatrace Operator развернёт Dynatrace OpenTelemetry Collector с образом по умолчанию ([настраивается через `.spec.templates.otelCollector.imageRef`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extensions-collector-image-ref "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")) и сервис Kubernetes с именем `<dynakube-name>-telemetry-ingest.dynatrace` ([настраивается через `.spec.telemetryIngest.serviceName`](#customize-the-service-name)) для приёма телеметрии. Используемый номер порта зависит от протокола, который поддерживает приложение. Соответствующие номера портов приведены в [справочнике](#port-list) ниже.

В следующем фрагменте показано, как настроить приложение с помощью переменной окружения, инструментированное SDK OpenTelemetry:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: http://<dynakube-name>-telemetry-ingest.dynatrace:4317
```

### Справочник портов

Для приёма данных телеметрии открыты следующие порты:

| Имя | Протокол | Порт |
| --- | --- | --- |
| OTLP GRPC | TCP | 4317 |
| OTLP HTTP | TCP | 4318 |
| Zipkin | TCP | 9411 |
| Jaeger GRPC | TCP | 14250 |
| Jaeger Thrift Binary | UDP | 6832 |
| Jaeger Thrift Compact | UDP | 6831 |
| Jaeger Thrift HTTP | TCP | 14268 |
| StatsD | UDP | 8125 |

## Дополнительные настройки

### Использование конечных точек HTTPS

По умолчанию конечные точки приёма работают в режиме HTTP. Чтобы зашифровать трафик телеметрии с помощью HTTPS, можно указать [TLS-секрет﻿](https://dt-url.net/yw03zsm) Kubernetes через [`.spec.telemetryIngest.tlsRefName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). После этого конечные точки приёма будут настроены на использование указанных сертификатов и прослушивание HTTPS.

Пример для приложения с инструментацией OpenTelemetry с использованием HTTPS

В следующем фрагменте показано, как настроить приложение, инструментированное SDK OpenTelemetry, через переменную окружения:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://<dynakube-name>-telemetry-ingest.dynatrace:4318
```

### Настройка имени сервиса приёма телеметрии

По умолчанию имя сервиса для приёма телеметрии, это `<dynakube-name>-telemetry-ingest.dynatrace`, но его можно настроить, задав [`.spec.telemetryIngest.serviceName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Указанное значение будет использовано как имя сервиса, но сами сервисы по-прежнему будут находиться в пространстве имён DynaKube, где также развёрнут Dynatrace OpenTelemetry Collector.

Стоит учитывать, что наличие нескольких DynaKube с одинаковым именем сервиса приведёт к коллизиям имён сервисов.

Например, если задать `.spec.telemetryIngest.serviceName` как `my-telemetry-ingest`, конечные точки будут доступны по адресу `http://my-telemetry-ingest.dynatrace:4318`.

Пример

```
apiVersion: dynatrace.com/v1beta5



kind: DynaKube



metadata:



name: dynakube



namespace: dynatrace



spec:



apiUrl:  https://ENVIRONMENTID.live.dynatrace.com/api



telemetryIngest:



serviceName: my-telemetry-ingest



protocols:



- jaeger



- zipkin



- otlp



- statsd



templates:



otelCollector:



imageRef:



repository: public.ecr.aws/dynatrace/dynatrace-otel-collector



tag: <tag>
```

Образ OTel collector

Образ OTel collector берётся из наших [поддерживаемых публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Настройка Dynatrace Operator на использование образов из публичного реестра для себя самого и управляемых им компонентов. Это можно сделать вручную или через автоматическое определение по окружению Dynatrace."), нужно убедиться, что используемый `tag` существует! Также можно использовать [приватный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование приватного реестра").

### Настройки прокси

Любой прокси, указанный в [`.spec.proxy`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."), будет передан в OpenTelemetry Collector через переменные окружения `HTTP_PROXY` и `HTTPS_PROXY`. Если используется ActiveGate внутри кластера, URL ActiveGate внутри кластера будет автоматически добавлен в переменную окружения `NO_PROXY`, чтобы избежать лишних циклов взаимодействия.

#### Доверенные ЦС

Если для взаимодействия с прокси нужны сертификаты, их можно указать в [`.spec.trustedCAs`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Системные ЦС из образа контейнера OpenTelemetry Collector загружаются вместе с ЦС из `trustedCAs`. Системные ЦС содержат сертификаты, необходимые для взаимодействия с публичными ActiveGate.

### Постоянное хранилище ActiveGate

Когда телеметрия принимается через in-cluster ActiveGate, полученные данные буферизуются на PersistentVolume на ActiveGate до тех пор, пока данные не будут успешно переданы. Для этого [к ActiveGate подключается PersistentVolumeClaim](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data."). Следующий пример показывает PVC по умолчанию, который оператор настраивает для ActiveGate, если не указан пользовательский PVC:

```
apiVersion: v1



kind: PersistentVolumeClaim



metadata:



name: <ActiveGate-name>



namespace: dynatrace



spec:



accessModes:



- ReadWriteOnce



resources:



requests:



storage: 1Gi
```

Класс хранилища по умолчанию

Нужно убедиться, что [задан класс хранилища по умолчанию﻿](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1). Иначе PersistentVolumeClaim для ActiveGate не может быть создан.

Пользовательский PersistentVolumeClaim можно настроить в [`.spec.activegate.volumeClaimTemplate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

#### Эфемерный том

Для тестовых целей PVC можно заменить локальным эфемерным хранилищем с помощью [`.spec.activeGate.useEphemeralVolume`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

Использование `.spec.activeGate.useEphemeralVolume` не рекомендуется для рабочих сред.

### Время завершения работы ActiveGate

Если ActiveGate останавливается (например, в сценариях scale-in), ему требуется некоторое время, чтобы сбросить свои буферы, отправив все буферизованные данные в Dynatrace.
В крупных средах это может занять некоторое время, и Kubernetes может завершить работу ActiveGate слишком рано. Чтобы увеличить так называемый период отсрочки завершения, можно увеличить длительность через ['.spec.activegate.terminationGracePeriodSeconds'](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."), чтобы дать поду ActiveGate больше времени на корректное завершение работы.

## Похожие темы

* [Параметры DynaKube для оператора Dynatrace](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.")