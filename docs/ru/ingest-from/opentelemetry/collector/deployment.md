---
title: Развертывание Dynatrace OTel Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/deployment
scraped: 2026-03-06T21:35:58.147239
---

# Развёртывание Dynatrace OTel Collector


* Latest Dynatrace

## Режимы развёртывания

Collector можно [развернуть](https://opentelemetry.io/docs/collector/quick-start/) как автономный агент или шлюз.

Для наглядности на иллюстрациях ниже показаны режимы в конфигурации Kubernetes, но те же режимы можно использовать и вне Kubernetes.

Агент

Шлюз

В качестве агента Collector развёртывается либо вместе с приложением, либо на том же хосте, что и приложение. Такой Collector может принимать данные телеметрии и обогащать их, например, тегами или информацией об инфраструктуре.

![OpenTelemetry collector as agent](https://dt-cdn.net/images/collector-agent-deployment-new-9322-7f44156cfc.jpg)

В качестве шлюза один или несколько экземпляров Collector могут быть развёрнуты как автономные сервисы. Такой Collector можно развёртывать дополнительно, например, на кластер, регион или центр обработки данных. Балансировщик нагрузки может помочь масштабировать независимо работающие экземпляры Collector.

![OpenTelemetry collector as gateway](https://dt-cdn.net/images/collector-gateway-deployment-new-2-9322-7087373547.jpg)

Также возможно комбинировать эти режимы развёртывания и выстраивать цепочки экземпляров Collector. Рассмотрите этот вариант при развёртывании Collector в крупных средах.

## Варианты развёртывания

Dynatrace Collector можно развернуть для следующих платформ:

* [Kubernetes](#kubernetes)
* [Docker](#docker)
* [Windows, macOS и Linux](#binary)
* [Установочные пакеты Linux](#linux-installer-packages)

### Kubernetes

Для Kubernetes Dynatrace Collector можно развернуть следующими способами:

* OpenTelemetry Kubernetes Operator
* Helm
* Необработанный манифест

#### Данные доступа Dynatrace

Перед развёртыванием Collector необходимо настроить необходимые секреты Kubernetes для данных доступа Dynatrace.

Используйте kubectl для создания секретов Kubernetes для параметров экспорта Dynatrace. Замените заполнители (обозначенные фигурными скобками) фактическими значениями для [URL экспорта и API-токена](../otlp-api.md "Узнайте о конечных точках OTLP API, используемых приложением для экспорта данных OpenTelemetry в Dynatrace.").

```
kubectl create secret generic dynatrace-otelcol-dt-api-credentials --from-literal=DT_ENDPOINT={ENDPOINT_URL_HERE} --from-literal=DT_API_TOKEN={API_TOKEN_HERE}
```

#### Варианты развёртывания в Kubernetes

Приведённые ниже примеры конфигураций применяют ограничение ресурсов в 512 мегабайт. Вам может потребоваться изменить это значение в `resources.limits.memory` для вашего конкретного варианта использования.

OpenTelemetry Operator

Helm

Необработанный манифест

#### Предварительные требования

Если вы ещё не установили OpenTelemetry Operator, сначала убедитесь, что [cert-manager](https://cert-manager.io/docs/installation/) установлен. После этого вы можете развернуть Operator следующей командой `kubectl`:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/download/v0.144.0/opentelemetry-operator.yaml
```

После установки разверните Dynatrace Collector либо в [режиме шлюза, либо в режиме агента](#deployment-modes), используя один из следующих примеров конфигурации. Сохраните его как `crd-dynatrace-collector.yaml` и разверните с помощью `kubectl apply`.

Custom Resource Definition

CRD Kubernetes для Operator можно найти на [GitHub](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.144.0/docs/api/opentelemetrycollectors.md).

Развёртывание как шлюз (Deployment)

```
apiVersion: opentelemetry.io/v1beta1


kind: OpenTelemetryCollector


metadata:


name: dynatrace-otel


spec:


envFrom:


- secretRef:


name: dynatrace-otelcol-dt-api-credentials


env:


- name: MY_POD_IP


valueFrom:


fieldRef:


fieldPath: status.podIP


mode: "deployment"


image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0"


resources:


limits:


memory: 512Mi


config:


receivers:


otlp:


protocols:


grpc:


endpoint: ${env:MY_POD_IP}:4317


http:


endpoint: ${env:MY_POD_IP}:4318


exporters:


otlp_http:


endpoint: "${env:DT_ENDPOINT}"


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


traces:


receivers: [otlp]


processors: []


exporters: [otlp_http]


metrics:


receivers: [otlp]


processors: []


exporters: [otlp_http]


logs:


receivers: [otlp]


processors: []


exporters: [otlp_http]
```

Развёртывание как агент (DaemonSet)

```
apiVersion: opentelemetry.io/v1beta1


kind: OpenTelemetryCollector


metadata:


name: dynatrace-otel


spec:


envFrom:


- secretRef:


name: dynatrace-otelcol-dt-api-credentials


env:


- name: MY_POD_IP


valueFrom:


fieldRef:


fieldPath: status.podIP


mode: "daemonset"


image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0"


resources:


limits:


memory: 512Mi


config:


receivers:


otlp:


protocols:


grpc:


endpoint: ${env:MY_POD_IP}:4317


http:


endpoint: ${env:MY_POD_IP}:4318


exporters:


otlp_http:


endpoint: "${env:DT_ENDPOINT}"


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


traces:


receivers: [otlp]


processors: []


exporters: [otlp_http]


metrics:


receivers: [otlp]


processors: []


exporters: [otlp_http]


logs:


receivers: [otlp]


processors: []


exporters: [otlp_http]
```

Выберите один из стандартных [режимов развёртывания](#deployment-modes) для Dynatrace Collector.

Helm-чарты ниже используют `alternateConfig` для предоставления конфигурации Collector. При использовании этой записи конфигурация Helm-чарта по умолчанию, а также возможный объект `config` будут проигнорированы.

Развёртывание как шлюз (Deployment)

1. Сохраните следующую YAML-конфигурацию как `values-deployment.yaml`

   ```
   mode: deployment


   image:


   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector


   tag: 0.44.0


   command:


   name: dynatrace-otel-collector


   extraEnvs:


   - name: DT_API_TOKEN


   valueFrom:


   secretKeyRef:


   name: dynatrace-otelcol-dt-api-credentials


   key: DT_API_TOKEN


   - name: DT_ENDPOINT


   valueFrom:


   secretKeyRef:


   name: dynatrace-otelcol-dt-api-credentials


   key: DT_ENDPOINT


   resources:


   limits:


   memory: 512Mi


   alternateConfig:


   extensions:


   health_check:


   endpoint: "${env:MY_POD_IP}:13133"


   receivers:


   otlp:


   protocols:


   grpc:


   endpoint: ${env:MY_POD_IP}:4317


   http:


   endpoint: ${env:MY_POD_IP}:4318


   filelog: null


   exporters:


   otlp_http:


   endpoint: "${env:DT_ENDPOINT}"


   headers:


   Authorization: "Api-Token ${env:DT_API_TOKEN}"


   service:


   extensions: [health_check]


   pipelines:


   traces:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]


   metrics:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]


   logs:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]
   ```
2. Выполните следующие команды для настройки и установки Helm-чартов

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts


   helm repo update


   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-deployment.yaml
   ```

Развёртывание как агент (DaemonSet)

1. Сохраните следующую YAML-конфигурацию как `values-daemonset.yaml`

   ```
   mode: daemonset


   image:


   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector


   tag: 0.44.0


   command:


   name: dynatrace-otel-collector


   extraEnvs:


   - name: DT_API_TOKEN


   valueFrom:


   secretKeyRef:


   name: dynatrace-otelcol-dt-api-credentials


   key: DT_API_TOKEN


   - name: DT_ENDPOINT


   valueFrom:


   secretKeyRef:


   name: dynatrace-otelcol-dt-api-credentials


   key: DT_ENDPOINT


   resources:


   limits:


   memory: 512Mi


   alternateConfig:


   extensions:


   health_check:


   endpoint: "${env:MY_POD_IP}:13133"


   receivers:


   otlp:


   protocols:


   grpc:


   endpoint: ${env:MY_POD_IP}:4317


   http:


   endpoint: ${env:MY_POD_IP}:4318


   exporters:


   otlp_http:


   endpoint: "${env:DT_ENDPOINT}"


   headers:


   Authorization: "Api-Token ${env:DT_API_TOKEN}"


   service:


   extensions: [health_check]


   pipelines:


   traces:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]


   metrics:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]


   logs:


   receivers: [otlp]


   processors: []


   exporters: [otlp_http]
   ```
2. Выполните следующие команды для настройки и установки Helm-чартов

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts


   helm repo update


   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-daemonset.yaml
   ```

Сетевые порты

Убедитесь, что вы настроили и перенаправили все необходимые сетевые порты, используя [значение конфигурации `ports`](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).

Service

Используйте `kubectl apply` со следующей конфигурацией для настройки определений сервисов и правильных портов.

```
apiVersion: v1


kind: Service


metadata:


name: dynatrace-otel-collector


spec:


internalTrafficPolicy: Cluster


ipFamilies:


- IPv4


ipFamilyPolicy: SingleStack


ports:


- name: jaeger-compact


port: 6831


protocol: UDP


targetPort: 6831


- name: jaeger-grpc


port: 14250


protocol: TCP


targetPort: 14250


- name: jaeger-thrift


port: 14268


protocol: TCP


targetPort: 14268


- appProtocol: grpc


name: otlp


port: 4317


protocol: TCP


targetPort: 4317


- name: otlp-http


port: 4318


protocol: TCP


targetPort: 4318


- name: zipkin


port: 9411


protocol: TCP


targetPort: 9411


selector:


app.kubernetes.io/instance: dynatrace-otel-collector


app.kubernetes.io/name: dynatrace-otel-collector


sessionAffinity: None


type: ClusterIP
```

ConfigMap

Создайте ConfigMap, применив следующую конфигурацию с помощью `kubectl apply` для настройки конфигурации Collector.

```
apiVersion: v1


kind: ConfigMap


metadata:


name: dynatrace-otel-collector-config


data:


otel-collector-config: |


receivers:


otlp:


protocols:


grpc:


endpoint: ${env:MY_POD_IP}:4317


http:


endpoint: ${env:MY_POD_IP}:4318


exporters:


otlp_http:


endpoint: "${env:DT_ENDPOINT}"


headers:


Authorization: "Api-Token ${env:DT_API_TOKEN}"


service:


pipelines:


traces:


receivers: [otlp]


processors: []


exporters: [otlp_http]


metrics:


receivers: [otlp]


processors: []


exporters: [otlp_http]


logs:


receivers: [otlp]


processors: []


exporters: [otlp_http]
```

Манифест

Примените следующую конфигурацию манифеста с помощью `kubectl apply` для создания Deployment Dynatrace Collector в [режиме шлюза](#deployment-modes).

```
apiVersion: apps/v1


kind: Deployment


metadata:


name: dynatrace-otel-collector


spec:


selector:


matchLabels:


app.kubernetes.io/name: dynatrace-otel-collector


replicas: 1


template:


metadata:


labels:


app.kubernetes.io/instance: dynatrace-otel-collector


app.kubernetes.io/name: dynatrace-otel-collector


spec:


#You may have to configure RBAC to grant proper permissions for enriching data


#serviceAccountName: dynatrace-otel-collector


containers:


- name: dynatrace-otel-collector


args: ["--config", "/conf/otel-collector-config.yaml"]


env:


- name: MY_POD_IP


valueFrom:


fieldRef:


apiVersion: v1


fieldPath: status.podIP


- name: DT_ENDPOINT


valueFrom:


secretKeyRef:


name: dynatrace-otelcol-dt-api-credentials


key: DT_ENDPOINT


- name: DT_API_TOKEN


valueFrom:


secretKeyRef:


name: dynatrace-otelcol-dt-api-credentials


key: DT_API_TOKEN


image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0


resources:


limits:


memory: 512Mi


ports:


- containerPort: 8888 # Default endpoint for querying metrics of prometheus exporter.


volumeMounts:


- name: dynatrace-otel-collector-config


mountPath: /conf


volumes:


- configMap:


name: dynatrace-otel-collector-config


items:


- key: otel-collector-config


path: otel-collector-config.yaml


name: dynatrace-otel-collector-config
```

Service account

В Kubernetes часто используется обогащение сигналов OpenTelemetry с помощью [процессора Kubernetes Attributes](use-cases/kubernetes/k8s-enrich.md "Настройка OpenTelemetry Collector для обогащения OTLP-запросов данными Kubernetes."). Для этого требуется service account Kubernetes, который автоматически настраивается при использовании Operator или Helm.

Для необработанных манифестов это нужно настроить вручную, добавив запись `spec.serviceAccountName: collector` в манифест развёртывания.

### Docker

Выполните следующую команду для загрузки образа Dynatrace Collector:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0
```

Затем убедитесь, что [файл конфигурации Collector](configuration.md "Настройка OpenTelemetry Collector.") существует в текущем рабочем каталоге, и запустите образ Collector следующей командой:

```
docker run -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0 --config=/etc/otelcol/otel-collector-config.yaml
```

Параметр `-v` связывает локальный файл конфигурации с указанным путём в контейнере, который затем передаётся параметру `--config`.

Убедитесь, что вы пробросили все необходимые сетевые порты с помощью [параметра `-p`](https://docs.docker.com/reference/cli/docker/container/run/#publish). Например, если вы принимаете OTLP gRPC-запросы на порту по умолчанию, необходимо указать порт 4317. Для OTLP через HTTP укажите порт 4318.

#### Docker Compose

Используйте следующую конфигурацию в файле Compose для развёртывания и запуска образа Collector:

```
version: "3"


services:


collector:


image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0


command: ["--config=/etc/otelcol/otel-collector-config.yaml"]


volumes:


- ./otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml


ports:


- "4317:4317"   # OTLP gRPC


- "4318:4318"   # OTLP HTTP
```

В примере выше `ports` настроен для gRPC и HTTP. Настройте список портов в соответствии с вашим конкретным вариантом использования.

### Windows, macOS и Linux

Для установки бинарного файла Collector вручную:

1. Загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.44.0) для вашей операционной системы с GitHub.
2. Распакуйте архив.
3. Настройте нужную конфигурацию и сохраните её в `otel-collector-config.yaml`.
4. Запустите бинарный файл `dynatrace-otel-collector` и передайте путь к файлу конфигурации с помощью параметра `--config`.

   ```
   ./dynatrace-otel-collector --config=$(pwd)/otel-collector-config.yaml
   ```

### Установочные пакеты Linux

Dynatrace также предоставляет установочные пакеты DEB и RPM для систем Linux на архитектурах x86-64 и ARM64.

Требуемая система инициализации

Установочные пакеты требуют, чтобы Systemd была активной системой инициализации.

Для развёртывания Collector с помощью установочного пакета загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.44.0) для вашей операционной системы с GitHub и установите его с правами root с помощью следующих команд.

Замените следующие два заполнителя в командах их фактическим содержимым:

* `<VERSION>` -- тег версии загрузки
* `<ARCH>` -- тег архитектуры системы (то есть `x86_64` или `arm64`) загрузки

Debian (.deb)

Red Hat (.rpm)

```
apt-get update


dpkg -i dynatrace-otel-collector_<VERSION>_Linux_<ARCH>.deb
```

```
yum update


rpm -ivh dynatrace-otel-collector_<VERSION>_Linux_<ARCH>.rpm
```

#### Конфигурация сервиса

При первом запуске сервис может не запуститься, если [файл конфигурации](configuration.md "Настройка OpenTelemetry Collector.") ещё не создан. По умолчанию Collector ищет файл по пути `/etc/dynatrace-otel-collector/config.yaml`.

Пользовательское расположение конфигурации

Если вы хотите использовать другой путь, вы можете переопределить путь по умолчанию с помощью параметра `--config` в переменной `OTELCOL_OPTIONS` в файле среды Systemd по пути `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:

```
OTELCOL_OPTIONS="--config=<HERE-PATH-TO-CONFIG-FILE>"
```

Последующие обновления пакета заменят этот файл, поэтому обязательно сохраните и восстановите его содержимое при обновлении пакета Collector. Как альтернативу, вы можете переопределить конфигурацию с помощью [команды `systemctl edit`](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).

Чтобы увидеть все доступные параметры конфигурации, запустите бинарный файл Collector с параметром `--help`.

После изменения конфигурации обязательно перезапустите сервис с помощью следующей команды и прав root:

```
systemctl restart dynatrace-otel-collector
```

#### Статус сервиса

Для просмотра текущего статуса сервиса Collector выполните следующую команду с правами root:

```
systemctl status dynatrace-otel-collector
```

Для проверки вывода сервиса Collector выполните следующую команду с правами root:

```
journalctl -u dynatrace-otel-collector
```

## Реестры образов контейнеров

Образы контейнеров для дистрибутива Dynatrace OpenTelemetry Collector доступны в следующих реестрах:

* [GitHub Container Registry (GHCR)](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)

  + `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0`
* [Amazon Elastic Container Registry (Amazon ECR)](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)

  + `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.44.0`
* [Docker Hub Container Registry](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)

  + `dynatrace/dynatrace-otel-collector:0.44.0`
