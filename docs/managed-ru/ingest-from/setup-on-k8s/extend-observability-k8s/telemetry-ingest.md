---
title: Включение конечных точек приёма телеметрии Dynatrace
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest
scraped: 2026-05-12T12:03:43.598049
---

# Включение конечных точек приёма телеметрии Dynatrace

# Включение конечных точек приёма телеметрии Dynatrace

* Обновлено 04 ноября 2025 г.

Dynatrace Operator version 1.6+

Включение конечных точек телеметрии Dynatrace в Kubernetes для приёма данных внутри кластера.

* Приём данных через конечные точки [OTLP](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger](https://www.jaegertracing.io/), [StatsD](https://github.com/statsd/statsd) или [Zipkin](https://zipkin.io/)
* Анализ насыщенных контекстом данных с помощью встроенных приложений, DQL, Notebooks и Dashboards

## Предварительные требования

* [Токен приёма данных](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Настройка токенов и разрешений для мониторинга кластера Kubernetes") требует областей токена `openTelemetryTrace.ingest`, `logs.ingest` и `metrics.ingest` и должен быть предоставлен через поле `dataIngestToken` в том же [секрете](/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed#create-secret-helm "Разверните Dynatrace Operator для Kubernetes observability."), что и ваш API-токен.

## Настройка и использование

Следующие два шага описывают, как настроить и использовать конечные точки приёма телеметрии.

Подключение через Kubernetes App

Если вы получили ваш DynaKube с [экрана подключения приложения Dynatrace Kubernetes App](/managed/ingest-from/setup-on-k8s/quickstart "Развёртывание Dynatrace Operator на Kubernetes"), имя сервиса приёма телеметрии будет задано как `telemetry-ingest.dynatrace`. Чтобы изменить его, см. [Настройка имени сервиса приёма телеметрии](#customize-the-service-name).

1. Создайте DynaKube

Чтобы включить конечные точки приёма телеметрии, укажите список нужных протоколов в поле DynaKube `.spec.telemetryIngest.protocols`. Подробнее о точных значениях см. в нашей документации [справочника по DynaKube](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#telemetry-ingest-v1beta5 "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

Маршрутизация данных

При наличии ActiveGate, работающего в кластере Kubernetes, [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Узнайте, как использовать OpenTelemetry Collector, включая Dynatrace OTel Collector, для приёма телеметрии из OpenTelemetry.") будет настроен на маршрутизацию всех принимаемых данных через ActiveGate внутри кластера вместо прямого подключения к публичному ActiveGate. Кроме того, автоматически будут включены возможности, необходимые для приёма телеметрии.

Если ActiveGate внутри кластера не развёрнут (то есть `.spec.activeGate` не указан), OpenTelemetry Collector будет настроен на прямое взаимодействие с вашим тенантом Dynatrace.

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

Образ OTel collector берётся из наших [поддерживаемых публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра"), убедитесь, что используемый `tag` существует! В качестве альтернативы можно использовать ваш [частный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра").

2. Настройте приложения

После применения DynaKube Dynatrace Operator развернёт Dynatrace OpenTelemetry Collector с образом по умолчанию ([настраивается с помощью `.spec.templates.otelCollector.imageRef`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extensions-collector-image-ref "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")) и сервис Kubernetes с именем `<dynakube-name>-telemetry-ingest.dynatrace` ([настраивается с помощью `.spec.telemetryIngest.serviceName`](#customize-the-service-name)) для приёма телеметрии. Используемый номер порта зависит от протокола, который поддерживает ваше приложение. Чтобы найти соответствующие номера портов, см. [справочник](#port-list) ниже.

Следующий фрагмент показывает, как настроить приложение, инструментированное с помощью OpenTelemetry SDK, используя переменную окружения:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: http://<dynakube-name>-telemetry-ingest.dynatrace:4317
```

### Справочник по портам

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

По умолчанию конечные точки приёма работают в режиме HTTP. Если требуется шифровать трафик телеметрии с помощью HTTPS, можно сослаться на [секрет Kubernetes TLS](https://dt-url.net/yw03zsm) через [`.spec.telemetryIngest.tlsRefName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Тогда конечные точки приёма будут настроены на использование указанных сертификатов и прослушивание HTTPS.

Пример для инструментированного OpenTelemetry приложения с использованием HTTPS

Следующий фрагмент показывает, как настроить приложение, инструментированное с помощью OpenTelemetry SDK, через переменную окружения:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://<dynakube-name>-telemetry-ingest.dynatrace:4318
```

### Настройка имени сервиса приёма телеметрии

По умолчанию имя сервиса для приёма телеметрии, это `<dynakube-name>-telemetry-ingest.dynatrace`, но его можно настроить, задав [`.spec.telemetryIngest.serviceName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Указанное значение будет использовано как имя сервиса, но сервисы по-прежнему будут находиться в пространстве имён DynaKube, где также развёрнут Dynatrace OpenTelemetry Collector.

Учтите, что наличие нескольких DynaKube с одинаковым именем сервиса приведёт к конфликтам имён сервисов.

Например, если задать для `.spec.telemetryIngest.serviceName` значение `my-telemetry-ingest`, конечные точки будут доступны по адресу `http://my-telemetry-ingest.dynatrace:4318`.

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

Образ OTel collector берётся из наших [поддерживаемых публичных реестров](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Использование публичного реестра"), убедитесь, что используемый `tag` существует! В качестве альтернативы можно использовать ваш [частный реестр](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Использование частного реестра").

### Настройки прокси

Любой прокси, указанный в [`.spec.proxy`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."), будет передан в OpenTelemetry Collector через переменные окружения `HTTP_PROXY` и `HTTPS_PROXY`. Если используется ActiveGate внутри кластера, URL этого ActiveGate будет автоматически добавлен в переменную окружения `NO_PROXY`, чтобы избежать ненужных циклов взаимодействия.

#### Доверенные центры сертификации (CA)

Если для взаимодействия через прокси требуется использовать сертификаты, их можно указать в [`.spec.trustedCAs`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."). Системные CA из образа контейнера OpenTelemetry Collector загружаются вместе с CA из `trustedCAs`. Системные CA содержат сертификаты, необходимые для взаимодействия с публичными ActiveGate.

### Постоянное хранилище ActiveGate

Когда приём телеметрии используется с ActiveGate внутри кластера, принимаемые данные буферизуются на PersistentVolume на ActiveGate до тех пор, пока данные не будут успешно переданы. Для этого к ActiveGate монтируется [PersistentVolumeClaim](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Настройте постоянное хранилище для контейнеризированного ActiveGate, используемое как временное хранилище для принимаемых данных."). Следующий пример иллюстрирует PVC по умолчанию, настраиваемый для ActiveGate оператором, если пользовательский PVC не указан:

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

Убедитесь, что определён [класс хранилища по умолчанию](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1). В противном случае PersistentVolumeClaim для ActiveGate не может быть подготовлен.

Пользовательский PersistentVolumeClaim можно настроить в [`.spec.activegate.volumeClaimTemplate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

#### Эфемерный том

В тестовых целях PVC можно заменить локальным эфемерным хранилищем с помощью [`.spec.activeGate.useEphemeralVolume`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.").

Использование `.spec.activeGate.useEphemeralVolume` не рекомендуется для производственных окружений.

### Время на завершение работы ActiveGate

Если ActiveGate завершает работу (например, в сценариях масштабирования вниз), ему требуется некоторое время, чтобы сбросить свои буферы, отправив все буферизованные данные в Dynatrace.
В крупных окружениях это может занять некоторое время, и Kubernetes потенциально может завершить работу ActiveGate слишком рано. Чтобы расширить так называемый период ожидания завершения (termination grace period), можно увеличить длительность через ['.spec.activegate.terminationGracePeriodSeconds'](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes."), чтобы дать поду ActiveGate больше времени на корректное завершение работы.

## Связанные темы

* [Параметры DynaKube для Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "Список доступных параметров для настройки Dynatrace Operator в Kubernetes.")