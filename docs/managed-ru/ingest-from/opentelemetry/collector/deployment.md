---
title: Развёртывание Dynatrace OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/deployment
---

# Развёртывание Dynatrace OTel Collector

# Развёртывание Dynatrace OTel Collector

* Практическое руководство
* 9 минут на чтение
* Обновлено 10 апр. 2026 г.

На этой странице описано, как развернуть дистрибутив Dynatrace для OTel Collector ("Dynatrace OTel Collector").

## Режимы развёртывания

Dynatrace OTel Collector можно [развернуть﻿](https://opentelemetry.io/docs/collector/quick-start/) как отдельный агент или как шлюз.

В иллюстративных целях на графиках ниже показаны режимы в настройке Kubernetes, но те же режимы можно использовать и вне Kubernetes.

Агент

Шлюз

В качестве агента Dynatrace OTel Collector развёртывается либо вместе с приложением, либо на том же хосте, что и приложение. Этот Dynatrace OTel Collector может принимать данные телеметрии и дополнять их, например, тегами или информацией об инфраструктуре.

![OTel Collector as agent](https://cdn.bfldr.com/B686QPH3/as/2h9fmzj68vw6vgts9t38hp/Collector_deployment_Agent_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector в роли агента

В качестве шлюза один или несколько экземпляров Dynatrace OTel Collector можно развернуть как отдельные сервисы. Этот Dynatrace OTel Collector можно развернуть дополнительно, например, на кластер, регион или дата-центр. Балансировщик нагрузки помогает масштабировать независимо работающие экземпляры Dynatrace OTel Collector.

![OTel Collector as gateway](https://cdn.bfldr.com/B686QPH3/as/ghvnk47j6phmrjjnv859chxr/Collector_deployment_Gateway_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector в роли шлюза

Также можно совмещать эти режимы развёртывания и выстраивать цепочку из экземпляров Dynatrace OTel Collector. Стоит рассмотреть этот вариант при развёртывании Dynatrace OTel Collector в крупных средах.

## Варианты развёртывания

Dynatrace OTel Collector можно развернуть для следующих платформ:

* [Kubernetes](#kubernetes)
* [Docker](#docker)
* [Windows, macOS и Linux](#binary)
* [Пакеты установщика для Linux](#linux-installer-packages)

### Kubernetes

Для Kubernetes Dynatrace OTel Collector можно развернуть следующими способами:

* OpenTelemetry Kubernetes Operator
* Helm
* Обычный манифест (raw manifest)

#### Данные доступа Dynatrace

Перед развёртыванием Dynatrace OTel Collector нужно настроить необходимые Kubernetes secrets с данными доступа Dynatrace.

Используй kubectl для создания Kubernetes secrets с данными экспорта Dynatrace. Замени плейсхолдеры (указанные в фигурных скобках) на реальные значения [URL экспорта и токена API](/managed/ingest-from/opentelemetry/otlp-api "Узнай о конечных точках OTLP API, которые твоё приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

```
kubectl create secret generic dynatrace-otelcol-dt-api-credentials --from-literal=DT_ENDPOINT={ENDPOINT_URL_HERE} --from-literal=DT_API_TOKEN={API_TOKEN_HERE}
```

#### Варианты развёртывания Kubernetes

В следующих примерах конфигураций применяется лимит ресурсов 512 мегабайт. Возможно, потребуется скорректировать значение `resources.limits.memory` под конкретный сценарий использования.

OpenTelemetry Operator

Helm

Обычный манифест

#### Предварительные требования

Если OpenTelemetry Operator ещё не установлен, сначала убедись, что установлен [cert-manager﻿](https://cert-manager.io/docs/installation/). После этого можно развернуть Operator следующей командой `kubectl`:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/download/v0.156.0/opentelemetry-operator.yaml
```

После установки разверни Dynatrace OTel Collector в [режиме gateway или agent](#deployment-modes), используя один из следующих примеров конфигурации. Сохрани его как `crd-dynatrace-collector.yaml` и разверни командой `kubectl apply`.

Custom Resource Definition

CRD Kubernetes для Operator можно найти на [GitHub﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.156.0/docs/api/opentelemetrycollectors.md).

Развернуть как gateway (Deployment)

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



image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0"



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

Развернуть как agent (DaemonSet)

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



image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0"



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

Выбери один из распространённых [режимов развёртывания](#deployment-modes) для Dynatrace OTel Collector.

Приведённые ниже чарты Helm используют `alternateConfig` для передачи конфигурации Dynatrace OTel Collector. При использовании этого параметра стандартная конфигурация чарта Helm, а также возможно присутствующий объект `config`, будут проигнорированы.

Развернуть как gateway (Deployment)

1. Сохрани следующую конфигурацию YAML в `values-deployment.yaml`

   ```
   mode: deployment



   image:



   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector



   tag: 0.52.0



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



   file_log: null



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
2. Выполни следующие команды, чтобы настроить и установить чарты Helm

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-deployment.yaml
   ```

Развернуть как agent (DaemonSet)

1. Сохрани следующую конфигурацию YAML в `values-daemonset.yaml`.

   ```
   mode: daemonset



   image:



   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector



   tag: 0.52.0



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
2. Выполни следующие команды, чтобы настроить и установить чарты Helm.

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-daemonset.yaml
   ```

Сетевые порты

Убедись, что настроены и проброшены все необходимые сетевые порты с помощью [значения конфигурации `ports`﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).

Service

Используй `kubectl apply` со следующей конфигурацией, чтобы настроить определения service и указать нужные порты.

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

Создай `ConfigMap`, применив следующую конфигурацию командой `kubectl apply`, чтобы настроить конфигурацию Dynatrace OTel Collector.

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

Manifest

Примени следующую конфигурацию манифеста командой `kubectl apply`, чтобы создать Deployment Dynatrace OTel Collector в [режиме gateway](#deployment-modes).

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



#Возможно, потребуется настроить RBAC, чтобы выдать нужные разрешения для обогащения данных



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



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0



resources:



limits:



memory: 512Mi



ports:



- containerPort: 8888 # Стандартный endpoint для запроса метрик prometheus exporter.



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


Учётная запись службы


В Kubernetes принято обогащать сигналы OpenTelemetry с помощью [Kubernetes Attributes processor](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настроить OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes."). Для этого нужна учётная запись службы Kubernetes, которая настраивается автоматически при использовании Operator или Helm.


Для необработанных манифестов это нужно настроить вручную, добавив запись `spec.serviceAccountName: collector` в манифест deployment.

### Docker

Выполните следующую команду, чтобы скачать самый свежий образ Dynatrace OTel Collector:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0
```

Далее убедитесь, что [файл конфигурации Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") находится в текущем рабочем каталоге, и запустите образ Dynatrace OTel Collector следующей командой:

```
docker run -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0 --config=/etc/otelcol/otel-collector-config.yaml
```

Параметр `-v` сопоставляет локальный файл конфигурации с указанным путём внутри контейнера, который затем передаётся в параметр `--config`.

Обязательно сопоставьте все необходимые сетевые порты с помощью [параметра `-p`﻿](https://docs.docker.com/reference/cli/docker/container/run/#publish). Например, если нужно принимать запросы OTLP gRPC на порту по умолчанию, укажите порт 4317. Для OTLP через HTTP укажите порт 4318.

#### Docker compose

Используйте следующую конфигурацию в compose-файле для развёртывания и запуска образа Dynatrace OTel Collector:

```
version: "3"



services:



collector:



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0



command: ["--config=/etc/otelcol/otel-collector-config.yaml"]



volumes:



- ./otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml



ports:



- "4317:4317"   # OTLP gRPC



- "4318:4318"   # OTLP HTTP
```

В примере выше `ports` настроен для gRPC и HTTP. Скорректируйте список портов в соответствии со своим сценарием использования.

### Windows, macOS и Linux

Чтобы установить бинарный файл Dynatrace OTel Collector вручную:

1. Скачайте [dynatrace-otel-collector﻿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.52.0) для своей операционной системы с GitHub.
2. Распакуйте архивный файл.
3. Настройте нужную конфигурацию и сохраните её в `otel-collector-config.yaml`.
4. Запустите бинарный файл `dynatrace-otel-collector`, передав путь к файлу конфигурации через параметр `--config`.

   ```
   ./dynatrace-otel-collector --config=$(pwd)/otel-collector-config.yaml
   ```

### Пакеты установщика для Linux

Dynatrace также предоставляет установочные пакеты DEB и RPM для систем Linux на архитектурах x86-64 и ARM64.

Требуется соответствующая init-система

Пакеты установщика требуют, чтобы активной init-системой был Systemd.

Чтобы развернуть Dynatrace OTel Collector с помощью пакета установщика, скачайте [dynatrace-otel-collector﻿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.52.0) для своей операционной системы с GitHub и установите его с правами root следующими командами.

Замените в командах следующие два плейсхолдера на их фактическое содержимое:

* `<VERSION>`: замените на тег версии скачанного файла.
* `<ARCH>`: замените на тег архитектуры системы (то есть `x86_64` или `arm64`) скачанного файла.

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

#### Конфигурация службы

При первом запуске службы она может не запуститься, если ещё нет [файла конфигурации](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector."). По умолчанию Dynatrace OTel Collector пытается найти файл по пути `/etc/dynatrace-otel-collector/config.yaml`.

Свой путь к конфигурации

Если нужно использовать другой путь, можно переопределить путь по умолчанию параметром `--config` в переменной `OTELCOL_OPTIONS` файла окружения Systemd по адресу `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:

```
OTELCOL_OPTIONS="--config=<HERE-PATH-TO-CONFIG-FILE>"
```

Последующие обновления пакета заменят этот файл, поэтому обязательно сделайте резервную копию его содержимого и восстановите его при обновлении пакета Dynatrace OTel Collector. Также можно переопределить конфигурацию с помощью [команды `systemctl edit`﻿](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).

Чтобы увидеть все доступные параметры конфигурации, запустите бинарный файл Dynatrace OTel Collector с параметром `--help`.

После изменения конфигурации обязательно перезапустите службу следующей командой с правами root:

```
systemctl restart dynatrace-otel-collector
```

#### Статус службы

Чтобы посмотреть текущий статус службы Dynatrace OTel Collector, выполните следующую команду с правами root:

```
systemctl status dynatrace-otel-collector
```

Чтобы проверить вывод службы Dynatrace OTel Collector, выполните следующую команду с правами root:

```
journalctl -u dynatrace-otel-collector
```

## Реестры образов контейнеров

Образы контейнеров для Dynatrace OTel Collector:

* [GitHub Container Registry (GHCR)﻿](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)

  + `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0`
* [Amazon Elastic Container Registry (Amazon ECR)﻿](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)

  + `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.52.0`
* [Docker Hub Container Registry﻿](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)

  + `dynatrace/dynatrace-otel-collector:0.52.0`