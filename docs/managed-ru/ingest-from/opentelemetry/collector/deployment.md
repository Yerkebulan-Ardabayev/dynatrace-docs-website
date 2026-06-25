---
title: Развёртывание Dynatrace OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/deployment
scraped: 2026-05-12T11:37:08.504826
---

# Развёртывание Dynatrace OTel Collector

# Развёртывание Dynatrace OTel Collector

* Практическое руководство
* Чтение: 9 мин
* Обновлено 10 апреля 2026 г.

На этой странице описано, как развернуть дистрибутив Dynatrace OTel Collector.

## Режимы развёртывания

Dynatrace OTel Collector можно [развернуть](https://opentelemetry.io/docs/collector/quick-start/) как автономный агент или шлюз.

Для наглядности на рисунках ниже режимы показаны в среде Kubernetes, но те же режимы можно использовать и за пределами Kubernetes.

Агент

Шлюз

В режиме агента Dynatrace OTel Collector развёртывается вместе с приложением или на том же хосте, что и приложение. В этом режиме Dynatrace OTel Collector принимает данные телеметрии и дополняет их, например, тегами или информацией об инфраструктуре.

![OTel Collector as agent](https://cdn.bfldr.com/B686QPH3/as/2h9fmzj68vw6vgts9t38hp/Collector_deployment_Agent_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector в режиме агента

В режиме шлюза один или несколько экземпляров Dynatrace OTel Collector развёртываются как автономные сервисы. Dynatrace OTel Collector в этом режиме можно развернуть дополнительно, например, на уровне кластера, региона или центра обработки данных. Балансировщик нагрузки помогает масштабировать независимо работающие экземпляры Dynatrace OTel Collector.

![OTel Collector as gateway](https://cdn.bfldr.com/B686QPH3/as/ghvnk47j6phmrjjnv859chxr/Collector_deployment_Gateway_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector в режиме шлюза

Также можно комбинировать эти режимы развёртывания и выстраивать экземпляры Dynatrace OTel Collector в цепочку. Это стоит рассмотреть при развёртывании Dynatrace OTel Collector в больших средах.

## Варианты развёртывания

Dynatrace OTel Collector можно развернуть на следующих платформах:

* [Kubernetes](#kubernetes)
* [Docker](#docker)
* [Windows, macOS и Linux](#binary)
* [Установочные пакеты Linux](#linux-installer-packages)

### Kubernetes

Для Kubernetes Dynatrace OTel Collector можно развернуть следующими способами:

* OpenTelemetry Kubernetes Operator
* Helm
* Raw manifest

#### Параметры доступа Dynatrace

Перед развёртыванием Dynatrace OTel Collector необходимо настроить секреты Kubernetes с параметрами доступа к Dynatrace.

С помощью kubectl создайте секреты Kubernetes с данными экспорта в Dynatrace. Замените заполнители (указанные в фигурных скобках) фактическими значениями [URL экспорта и API-токена](/managed/ingest-from/opentelemetry/otlp-api "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

```
kubectl create secret generic dynatrace-otelcol-dt-api-credentials --from-literal=DT_ENDPOINT={ENDPOINT_URL_HERE} --from-literal=DT_API_TOKEN={API_TOKEN_HERE}
```

#### Варианты развёртывания в Kubernetes

Приведённые ниже примеры конфигураций устанавливают ограничение ресурсов в 512 мегабайт. Для конкретного сценария использования это значение может потребоваться изменить в разделе `resources.limits.memory`.

OpenTelemetry Operator

Helm

Raw manifest

#### Предварительные требования

Если OpenTelemetry Operator ещё не установлен, сначала убедитесь, что установлен [cert-manager](https://cert-manager.io/docs/installation/). После этого можно развернуть Operator с помощью следующей команды `kubectl`:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/download/v0.150.0/opentelemetry-operator.yaml
```

После установки разверните Dynatrace OTel Collector в режиме [шлюза или агента](#deployment-modes), используя один из приведённых ниже примеров конфигурации. Сохраните файл как `crd-dynatrace-collector.yaml` и примените его командой `kubectl apply`.

Custom Resource Definition

Kubernetes CRD для Operator можно найти на [GitHub](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.150.0/docs/api/opentelemetrycollectors.md).

Развернуть как шлюз (Deployment)

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



image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0"



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

Развернуть как агент (DaemonSet)

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



image: "ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0"



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

Выберите один из стандартных [режимов развёртывания](#deployment-modes) для Dynatrace OTel Collector.

Представленные ниже Helm-чарты используют `alternateConfig` для передачи конфигурации Dynatrace OTel Collector. При использовании этого параметра стандартная конфигурация Helm-чарта, а также объект `config`, если он присутствует, будут проигнорированы.

Развернуть как шлюз (Deployment)

1. Сохраните следующую конфигурацию YAML в файл `values-deployment.yaml`

   ```
   mode: deployment



   image:



   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector



   tag: 0.48.0



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
2. Выполните следующие команды для настройки и установки Helm-чартов

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-deployment.yaml
   ```

Развернуть как агент (DaemonSet)

1. Сохраните следующую конфигурацию YAML в файл `values-daemonset.yaml`.

   ```
   mode: daemonset



   image:



   repository: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector



   tag: 0.48.0



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
2. Выполните следующие команды для настройки и установки Helm-чартов.

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-daemonset.yaml
   ```

Сетевые порты

Обязательно настройте и пробросьте все необходимые сетевые порты, используя [значение конфигурации `ports`](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).

Service

Примените следующую конфигурацию с помощью `kubectl apply`, чтобы создать определения сервиса и настроить нужные порты.

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

Создайте `ConfigMap`, применив следующую конфигурацию с помощью `kubectl apply`, чтобы задать конфигурацию Dynatrace OTel Collector.

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

Примените следующую конфигурацию манифеста с помощью `kubectl apply`, чтобы создать Deployment Dynatrace OTel Collector в [режиме шлюза](#deployment-modes).

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



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0



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

Сервисный аккаунт

В Kubernetes принято обогащать сигналы OpenTelemetry с помощью [processor Kubernetes Attributes](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Настройте OpenTelemetry Collector для обогащения запросов OTLP данными Kubernetes."). Для этого требуется сервисный аккаунт Kubernetes, который автоматически настраивается при использовании Operator или Helm.

При использовании raw-манифестов это необходимо настраивать вручную, добавив запись `spec.serviceAccountName: collector` в манифест развёртывания.

### Docker

Выполните следующую команду для загрузки актуального образа Dynatrace OTel Collector:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0
```

Убедитесь, что [файл конфигурации Dynatrace OTel Collector](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.") находится в текущей рабочей директории, и запустите образ Dynatrace OTel Collector следующей командой:

```
docker run -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0 --config=/etc/otelcol/otel-collector-config.yaml
```

Параметр `-v` сопоставляет локальный файл конфигурации с указанным путём в контейнере, который затем передаётся в параметр `--config`.

Обязательно пробросьте все необходимые сетевые порты с помощью [параметра `-p`](https://docs.docker.com/reference/cli/docker/container/run/#publish). Например, если принимаются запросы OTLP gRPC через порт по умолчанию, необходимо указать порт 4317. Для OTLP по HTTP укажите порт 4318.

#### Docker compose

Используйте следующую конфигурацию в файле compose для развёртывания и запуска образа Dynatrace OTel Collector:

```
version: "3"



services:



collector:



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0



command: ["--config=/etc/otelcol/otel-collector-config.yaml"]



volumes:



- ./otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml



ports:



- "4317:4317"   # OTLP gRPC



- "4318:4318"   # OTLP HTTP
```

В приведённом примере `ports` настроен для gRPC и HTTP. Скорректируйте список портов в соответствии с конкретным сценарием использования.

### Windows, macOS и Linux

Чтобы установить бинарный файл Dynatrace OTel Collector вручную:

1. Загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) для своей операционной системы с GitHub.
2. Распакуйте архивный файл.
3. Настройте нужную конфигурацию и сохраните её в файл `otel-collector-config.yaml`.
4. Запустите бинарный файл `dynatrace-otel-collector` и передайте путь к файлу конфигурации с помощью параметра `--config`.

   ```
   ./dynatrace-otel-collector --config=$(pwd)/otel-collector-config.yaml
   ```

### Установочные пакеты Linux

Dynatrace также предоставляет установочные пакеты DEB и RPM для Linux-систем на архитектурах x86-64 и ARM64.

Требуемая система инициализации

Установочные пакеты требуют, чтобы активной системой инициализации был Systemd.

Для развёртывания Dynatrace OTel Collector с помощью установочного пакета загрузите [dynatrace-otel-collector](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.48.0) для своей операционной системы с GitHub и установите с правами суперпользователя, используя следующие команды.

Замените в командах следующие два заполнителя их фактическими значениями:

* `<VERSION>`: замените тегом версии загружаемого файла.
* `<ARCH>`: замените тегом архитектуры системы (то есть `x86_64` или `arm64`) загружаемого файла.

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

При первом запуске сервис может не запуститься, если [файл конфигурации](/managed/ingest-from/opentelemetry/collector/configuration "Как настроить OpenTelemetry Collector.") ещё не создан. По умолчанию Dynatrace OTel Collector пытается найти файл по пути `/etc/dynatrace-otel-collector/config.yaml`.

Нестандартное расположение конфигурации

Если нужно использовать другой путь, можно переопределить путь по умолчанию с помощью параметра `--config` в составе переменной `OTELCOL_OPTIONS` в файле среды Systemd по пути `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:

```
OTELCOL_OPTIONS="--config=<HERE-PATH-TO-CONFIG-FILE>"
```

При последующих обновлениях пакета этот файл будет заменён, поэтому во время обновления пакета Dynatrace OTel Collector обязательно сделайте резервную копию и восстановите его содержимое. Также можно переопределить конфигурацию с помощью [команды `systemctl edit`](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).

Чтобы просмотреть все доступные параметры конфигурации, запустите бинарный файл Dynatrace OTel Collector с параметром `--help`.

После изменения конфигурации перезапустите сервис следующей командой с правами суперпользователя:

```
systemctl restart dynatrace-otel-collector
```

#### Статус сервиса

Чтобы просмотреть текущий статус сервиса Dynatrace OTel Collector, выполните следующую команду с правами суперпользователя:

```
systemctl status dynatrace-otel-collector
```

Чтобы проверить вывод сервиса Dynatrace OTel Collector, выполните следующую команду с правами суперпользователя:

```
journalctl -u dynatrace-otel-collector
```

## Реестры образов контейнеров

Образы контейнеров для Dynatrace OTel Collector:

* [GitHub Container Registry (GHCR)](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)

  + `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.48.0`
* [Amazon Elastic Container Registry (Amazon ECR)](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)

  + `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.48.0`
* [Docker Hub Container Registry](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)

  + `dynatrace/dynatrace-otel-collector:0.48.0`