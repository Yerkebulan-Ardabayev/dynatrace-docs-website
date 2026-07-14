---
title: Deploy the Dynatrace OTel Collector
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/collector/deployment
---

# Deploy the Dynatrace OTel Collector

# Deploy the Dynatrace OTel Collector

* How-to guide
* 9-min read
* Updated on Apr 10, 2026

This page describes how to deploy the Dynatrace distribution of the OTel Collector ("Dynatrace OTel Collector").

## Deployment modes

The Dynatrace OTel Collector can be [deployed﻿](https://opentelemetry.io/docs/collector/quick-start/) as a standalone agent or gateway.

For illustrative purposes, the graphics below show the modes in a Kubernetes setup, but the same modes can also be used outside of Kubernetes.

Agent

Gateway

As an agent, the Dynatrace OTel Collector is deployed either with the application or on the same host as the application. This Dynatrace OTel Collector can receive telemetry data and enhance it with, for example, tags or infrastructure information.

![OTel Collector as agent](https://cdn.bfldr.com/B686QPH3/as/2h9fmzj68vw6vgts9t38hp/Collector_deployment_Agent_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector as agent

As a gateway, one or more Dynatrace OTel Collector instances can be deployed as standalone services. This Dynatrace OTel Collector can be deployed additionally, for example, per cluster, region, or data center. A load balancer can help scale the independently operating Dynatrace OTel Collector instances.

![OTel Collector as gateway](https://cdn.bfldr.com/B686QPH3/as/ghvnk47j6phmrjjnv859chxr/Collector_deployment_Gateway_-_Light_Mode?auto=webp&format=png&position=1)

OTel Collector as gateway

It's also possible to combine these deployment modes and chain Dynatrace OTel Collector instances. Consider this if you're deploying the Dynatrace OTel Collector in large environments.

## Deployment options

The Dynatrace OTel Collector can be deployed for the following platforms:

* [Kubernetes](#kubernetes)
* [Docker](#docker)
* [Windows, macOS, and Linux](#binary)
* [Linux installer packages](#linux-installer-packages)

### Kubernetes

For Kubernetes, the Dynatrace OTel Collector can be deployed in the following ways:

* OpenTelemetry Kubernetes Operator
* Helm
* Raw manifest

#### Dynatrace access details

Before you deploy the Dynatrace OTel Collector, you need to set up the necessary Kubernetes secrets for the Dynatrace access details.

Use kubectl to create Kubernetes secrets for the Dynatrace export details. Replace the placeholders (indicated by curly brackets) with the actual values for [the export URL and the API token](/managed/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

```
kubectl create secret generic dynatrace-otelcol-dt-api-credentials --from-literal=DT_ENDPOINT={ENDPOINT_URL_HERE} --from-literal=DT_API_TOKEN={API_TOKEN_HERE}
```

#### Kubernetes deployment variants

The following sample configurations apply a resource limit of 512 megabytes. You may need to adjust this under `resources.limits.memory` for your particular use case.

OpenTelemetry Operator

Helm

Raw manifest

#### Prerequisites

If you haven't installed OpenTelemetry Operator yet, first make sure [cert-manager﻿](https://cert-manager.io/docs/installation/) is installed. Afterwards, you can deploy Operator with the following `kubectl` command:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/download/v0.154.0/opentelemetry-operator.yaml
```

After the installation, deploy the Dynatrace OTel Collector either in [gateway or agent deployment mode](#deployment-modes), with one of the following configuration samples. Save it as `crd-dynatrace-collector.yaml` and deploy it with `kubectl apply`.

Custom Resource Definition

The Kubernetes CRD of the Operator can be found on [GitHub﻿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.154.0/docs/api/opentelemetrycollectors.md).

Deploy as a gateway (Deployment)

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

Deploy as an agent (DaemonSet)

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

Choose one of the common [deployment modes](#deployment-modes) for the Dynatrace OTel Collector.

The Helm charts below use `alternateConfig` to provide the Dynatrace OTel Collector configuration. With this entry, the default Helm chart configuration, as well as a possibly present `config` object, will be ignored.

Deploy as a gateway (Deployment)

1. Save the following YAML configuration under `values-deployment.yaml`

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
2. Run the following commands to configure and install the Helm charts

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-deployment.yaml
   ```

Deploy as an agent (DaemonSet)

1. Save the following YAML configuration under `values-daemonset.yaml`.

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
2. Run the following commands to configure and install the Helm charts.

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-daemonset.yaml
   ```

Network ports

Make sure to configure and forward all relevant network ports, using the [`ports` configuration value﻿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).

Service

Use `kubectl apply` with the following configuration to set up the service definitions and configure the correct ports.

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

Create a `ConfigMap` by applying the following configuration with `kubectl apply` to set up the Dynatrace OTel Collector configuration.

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

Apply the following manifest configuration with `kubectl apply` to create the Dynatrace OTel Collector Deployment in [gateway mode](#deployment-modes).

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



image: ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0



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

In Kubernetes, it is common to enrich OpenTelemetry signals using the [Kubernetes Attributes processor](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."). This requires a Kubernetes service account, which is automatically configured when using Operator or Helm.

For raw manifests, this needs to be configured manually by adding a `spec.serviceAccountName: collector` entry to the deployment manifest.

### Docker

Run the following command to download the most recent Dynatrace OTel Collector image:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0
```

Next, ensure that the [Dynatrace OTel Collector configuration file](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") exists in the current working directory and run the Dynatrace OTel Collector image with the following command:

```
docker run -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0 --config=/etc/otelcol/otel-collector-config.yaml
```

The `-v` parameter maps the local configuration file to the given container path, which is subsequently passed to the `--config` parameter.

Make sure to map all required network ports with the [`-p` parameter﻿](https://docs.docker.com/reference/cli/docker/container/run/#publish). For example, if you accept OTLP gRPC requests on the default port, you need to specify port 4317. For OTLP over HTTP specify port 4318.

#### Docker compose

Use the following configuration in your compose file to deploy and run the Dynatrace OTel Collector image:

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

In the example above, `ports` is configured for gRPC and HTTP. Adjust the list of ports according to your specific use case.

### Windows, macOS, and Linux

To install the Dynatrace OTel Collector binary manually:

1. Download the [dynatrace-otel-collector﻿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.52.0) for your operating system from GitHub.
2. Decompress the archive file.
3. Set up the desired configuration and save it to `otel-collector-config.yaml`.
4. Run the `dynatrace-otel-collector` binary and pass the path to the configuration file using the `--config` parameter.

   ```
   ./dynatrace-otel-collector --config=$(pwd)/otel-collector-config.yaml
   ```

### Linux installer packages

Dynatrace also provides DEB and RPM installer packages for Linux systems on x86-64 and ARM64 architectures.

Required init system

The installer packages require Systemd to be the active init system.

To deploy the Dynatrace OTel Collector using an installer package, download the [dynatrace-otel-collector﻿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.52.0) for your operating system from GitHub, and install it using root privileges and the following commands.

Replace the following two placeholders in the commands with their actual content:

* `<VERSION>`: Replace with the version tag of the download.
* `<ARCH>`: Replace with the system architecture tag (that is, `x86_64` or `arm64`) of the download.

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

#### Service configuration

When first starting the service, it may fail to start if there is no [configuration file](/managed/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") in place yet. By default, the Dynatrace OTel Collector attempts to find the file at `/etc/dynatrace-otel-collector/config.yaml`.

Custom configuration location

If you wish to use a different path, you can override the default path with the `--config` parameter as part of the `OTELCOL_OPTIONS` variable in the Systemd environment file at `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:

```
OTELCOL_OPTIONS="--config=<HERE-PATH-TO-CONFIG-FILE>"
```

Subsequent package updates will replace this file, so be sure to back up and restore its content during an update of the Dynatrace OTel Collector package. Alternatively, you can override the configuration with the [`systemctl edit` command﻿](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).

To see all available configuration options, run the Dynatrace OTel Collector binary with the `--help` parameter.

After changing the configuration, make sure to restart the service using the following command and root privileges:

```
systemctl restart dynatrace-otel-collector
```

#### Service status

To view the current status of the Dynatrace OTel Collector service, run the following command with root privileges:

```
systemctl status dynatrace-otel-collector
```

To check the output of the Dynatrace OTel Collector service, run the following command with root privileges:

```
journalctl -u dynatrace-otel-collector
```

## Container image registries

Container images for the Dynatrace OTel Collector:

* [GitHub Container Registry (GHCR)﻿](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)

  + `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.52.0`
* [Amazon Elastic Container Registry (Amazon ECR)﻿](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)

  + `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.52.0`
* [Docker Hub Container Registry﻿](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)

  + `dynatrace/dynatrace-otel-collector:0.52.0`