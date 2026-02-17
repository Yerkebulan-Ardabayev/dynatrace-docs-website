# Dynatrace Documentation: ingest-from/opentelemetry

Generated: 2026-02-17

Files combined: 40

---


## Source: configuration.md


---
title: Configure the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/configuration
scraped: 2026-02-17T21:34:20.565348
---

# Configure the OpenTelemetry Collector

# Configure the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Dec 05, 2025

To successfully configure your Collector instance, you need to configure each component (receiver, optional processor, and exporter) individually in the Collector YAML configuration file and enable them via additional pipeline objects.

Dynatrace Collector

As part of a Dynatrace Collector setup, note that you can only configure the components shipped with Dynatrace Collector.

Find a full list of all supported Collector components at [Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.").

## Configuration example

Here is an example YAML file for a very basic Collector configuration that can be used to export OpenTelemetry traces, metrics, and logs to Dynatrace.

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: "${env:DT_ENDPOINT}"



logs_endpoint: "${env:DT_ENDPOINT}/v1/logs?structure=flattened"



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



processors: [cumulativetodelta]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: []



exporters: [otlp_http]
```

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to a value higher than how often the collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

In this YAML file, we configure the following components:

* An OTLP receiver (`otlp`) that can receive data via gRPC and HTTP.
* A processor to convert any metrics with cumulative temporality to delta temporality (see [Delta metrics](#delta-metrics) for more details).
* An OTLP HTTP exporter (`otlp_http`) configured with:

  + The Dynatrace endpoint, see [Base URLs](/docs/ingest-from/opentelemetry/otlp-api#base-url "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").
  + The logs endpoint configured to flatten structured logs, see <#structured-logs>.
  + An API token, see [Authentication](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

In the example configuration above, the Dynatrace token needs to have the **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`), the **Ingest metrics** (`metrics.ingest`), and the **Ingest logs** (`logs.ingest`) permissions.

Within the service section, you define each component separately.

* Extensions can be enabled in their own section, while receivers, processors, and exporters are grouped under a pipeline section.
* Pipelines can be of type traces, metrics, or logs.
* Each receiver/processor/exporter can be used in more than one pipeline. For processors referenced in multiple pipelines, each pipeline gets a separate instance of the processors. This contrasts with receivers/exporters referenced in multiple pipelines, where only one instance of a receiver/exporter is used for all pipelines. Also, note that the order of processors dictates the order in which data is processed.
* You can also define the same components more than once. For example, you can have two different receivers or even two or more distinct parts of the pipeline.
* Even if a component is properly configured in its section, it will not be enabled unless it's also defined in the service section.

## Validate the configuration

It is important to ensure the used Collector configuration is syntactically and semantically correct. For example, YAML uses spaces (not tabs) for indentation, to define the document hierarchy, and it is necessary to use the right level of indentation for each section and component. Collector provides the built-in `validate` command to verify the configuration and its components and services are properly configured.

```
dynatrace-otel-collector validate --config=[PATH_TO_YOUR_CONFIGURATION_FILE]
```

If you run a container instance of the Collector, you can also use the following Docker command to run the validation directly from your container.

```
docker run -v $(pwd):$(pwd) -w $(pwd) ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0 validate --config=[YOUR_CONFIGURATION_FILE]
```

## Delta metrics

Dynatrace requires metrics data to be [sent with delta temporality](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.") and **not** cumulative temporality.

If your application doesn't allow you to configure delta temporality, you can use the [`cumulativetodelta` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to have your Collector instance adjust cumulative values to delta values. The [configuration example](#configuration-example) above shows how to configure and reference the processor in your Collector configuration.

## Chained and load-balanced Collectors

When you use more than one Collector instance, it's important to maintain stable value propagation across all instances.

This is particularly important when you send OTLP requests across different Collector instances (for example, load balancing), as each Collector instance keeps track of its own delta offset, which may break the data reported to the Dynatrace backend.

In such scenarios, we recommend routing your OTLP requests through a single, outbound Collector instance that forwards the data to the Dynatrace backend and takes care of the delta conversion. The other Collector instances should use a cumulative aggregation, to ensure stable and consistent value propagation.

## Configure structured logs processing

When you export structured logs to Dynatrace, Dynatrace processes the log data in one of two ways.
It either:

* Keeps the original nested structure from your logs source ("raw").
* Flattens it so all log attribute values are accessible via key paths ("flattened").

To configure this behavior, use the `logs_endpoint` setting as shown in the [configuration example](#configuration-example), line 16.
Make sure to include the complete API endpoint path including `/v1/logs` (environment variables are allowed), followed by the desired behavior.

* To keep the original nested structure, use `structure=raw`.
* To flatten the log data, use `structure=flattened`.

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+ and environments created after February 1, 2026: Raw.
* For environments created before February 1, 2026: Flattened.


---


## Source: deployment.md


---
title: Deploy Dynatrace OTel Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/deployment
scraped: 2026-02-17T21:33:07.713557
---

# Deploy Dynatrace OTel Collector

# Deploy Dynatrace OTel Collector

* Latest Dynatrace
* How-to guide
* 9-min read
* Updated on Feb 12, 2024

## Deployment modes

The Collector can be [deployedï»¿](https://opentelemetry.io/docs/collector/quick-start/) as a standalone agent or gateway.

For illustrative purposes, the graphics below show the modes in a Kubernetes setup, but the same modes can also be used outside of Kubernetes.

Agent

Gateway

As an agent, the Collector is deployed either with the application or on the same host as the application. This Collector can receive telemetry data and enhance it with, for example, tags or infrastructure information.

![OpenTelemetry collector as agent](https://dt-cdn.net/images/collector-agent-deployment-new-9322-7f44156cfc.jpg)

As a gateway, one or more Collector instances can be deployed as standalone services. This Collector can be deployed additionally, for example, per cluster, region, or data center. A load balancer can help scale the independently operating Collector instances.

![OpenTelemetry collector as gateway](https://dt-cdn.net/images/collector-gateway-deployment-new-2-9322-7087373547.jpg)

It's also possible to combine these deployment modes and chain Collector instances. Consider this if you're deploying the Collector in large environments.

## Deployment Options

The Dynatrace Collector can be deployed for the following platforms:

* [Kubernetes](#kubernetes)
* [Docker](#docker)
* [Windows, macOS, and Linux](#binary)
* [Linux installer packages](#linux-installer-packages)

### Kubernetes

For Kubernetes, the Dynatrace Collector can be deployed in the following ways:

* OpenTelemetry Kubernetes Operator
* Helm
* Raw manifest

#### Dynatrace access details

Before you deploy the Collector, you need to set up the necessary Kubernetes secrets for the Dynatrace access details.

Use kubectl to create Kuberenetes secrets for the Dynatrace export details. Replace the placeholders (indicated by curly brackets) with the actual values for [the export URL and the API token](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

```
kubectl create secret generic dynatrace-otelcol-dt-api-credentials --from-literal=DT_ENDPOINT={ENDPOINT_URL_HERE} --from-literal=DT_API_TOKEN={API_TOKEN_HERE}
```

#### Kubernetes deployment variants

The following sample configurations apply a resource limit of 512 megabytes. You may need to adjust this under `resources.limits.memory` for your particular use case.

OpenTelemetry Operator

Helm

Raw manifest

#### Prerequisites

If you haven't installed OpenTelemetry Operator yet, first make sure [cert-managerï»¿](https://cert-manager.io/docs/installation/) is installed. Afterwards, you can deploy Operator with the following `kubectl` command:

```
kubectl apply -f https://github.com/open-telemetry/opentelemetry-operator/releases/download/v0.144.0/opentelemetry-operator.yaml
```

After the installation, deploy the Dynatrace Collector either in [gateway or agent deployment mode](#deployment-modes), with one of the following configuration samples. Save it as `crd-dynatrace-collector.yaml` and deploy it with `kubectl apply`.

Custom Resource Definition

The Kubernetes CRD of the Operator can be found on [GitHubï»¿](https://github.com/open-telemetry/opentelemetry-operator/blob/v0.144.0/docs/api.md#opentelemetrycollector-1).

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

Choose one of the common [deployment modes](#deployment-modes) for the Dynatrace Collector.

The Helm charts below use `alternateConfig` to provide the Collector configuration. With this entry, the default Helm chart configuration, as well as a possibly present `config` object, will be ignored.

Deploy as a gateway (Deployment)

1. Save the following YAML configuration under `values-deployment.yaml`

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
2. Run the following commands to configure and install the Helm charts

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-deployment.yaml
   ```

Deploy as an agent (DaemonSet)

1. Save the following YAML configuration under `values-daemonset.yaml`

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
2. Run the following commands to configure and install the Helm charts

   ```
   helm repo add open-telemetry https://open-telemetry.github.io/opentelemetry-helm-charts



   helm repo update



   helm upgrade -i dynatrace-collector open-telemetry/opentelemetry-collector -f values-daemonset.yaml
   ```

Network ports

Make sure to configure and forward all relevant network ports, using the [`ports` configuration valueï»¿](https://github.com/open-telemetry/opentelemetry-helm-charts/blob/opentelemetry-collector-0.106.0/charts/opentelemetry-collector/values.yaml#L266-L313).

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

Create a ConfigMap by applying the following configuration with `kubectl apply` to set up the Collector configuration.

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

Apply the following manifest configuration with `kubectl apply` to create the Dynatrace Collector Deployment in [gateway mode](#deployment-modes).

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

In Kubernetes, it is common to enrich OpenTelemetry signals using the [Kubernetes Attributes processor](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."). This requires a Kubernetes service account, which is automatically configured when using Operator or Helm.

For raw manifests, this needs to be configured manually by adding a `spec.serviceAccountName: collector` entry to the deployment manifest.

### Docker

Run the following command to download the image of the Dynatrace Collector:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0
```

Next, ensure that the [Collector configuration file](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") exists in the current working directory and run the Collector image with the following command:

```
docker run -v $(pwd)/otel-collector-config.yaml:/etc/otelcol/otel-collector-config.yaml ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0 --config=/etc/otelcol/otel-collector-config.yaml
```

The `-v` parameter maps the local configuration file to the given container path, which is subsequently passed to the `--config` parameter.

Make sure to map all required network ports with the [`-p` parameterï»¿](https://docs.docker.com/reference/cli/docker/container/run/#publish). For example, if you accept OTLP gRPC requests on the default port, you need to specify port 4317. For OTLP over HTTP specify port 4318.

#### Docker Compose

Use the following configuration in your Compose file to deploy and run the Collector image:

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

In the example above, `ports` is configured for gRPC and HTTP. Adjust the list of ports according to your specific use case.

### Windows, macOS, and Linux

To install the Collector binary manually

1. Download the [dynatrace-otel-collectorï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.44.0) for your operating system from GitHub.
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

To deploy the Collector using an installer package, download the [dynatrace-otel-collectorï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.44.0) for your operating system from GitHub, and install it using root privileges and the following commands.

Replace the following two placeholders in the commands with their actual content:

* `<VERSION>` with the version tag of the download
* `<ARCH>` with the system architecture tag (that is, `x86_64` or `arm64`) of the download

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

When first starting the service, it may fail to start if there is no [configuration file](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") in place yet. By default, the Collector attempts to find the file at `/etc/dynatrace-otel-collector/config.yaml`.

Custom configuration location

If you wish to use a different path, you can override the default path with the `--config` parameter as part of the `OTELCOL_OPTIONS` variable in the Systemd environment file at `/etc/dynatrace-otel-collector/dynatrace-otel-collector.conf`:

```
OTELCOL_OPTIONS="--config=<HERE-PATH-TO-CONFIG-FILE>"
```

Subsequent package updates will replace this file, so be sure to back up and restore its content during an update of the Collector package. Alternatively, you can override the configuration with the [`systemctl edit` commandï»¿](https://docs.fedoraproject.org/en-US/quick-docs/systemd-understanding-and-administering/#_modifying_existing_systemd_services).

To see all available configuration options, run the Collector binary with the `--help` parameter.

After changing the configuration, make sure to restart the service using the following command and root privileges:

```
systemctl restart dynatrace-otel-collector
```

#### Service status

To view the current status of the Collector service, run the following command with root privileges:

```
systemctl status dynatrace-otel-collector
```

To check the output of the Collector service, run the following command with root privileges:

```
journalctl -u dynatrace-otel-collector
```

## Container image registries

Container images for the Dynatrace distribution of the OpenTelemetry Collector are available in

* [GitHub Container Registry (GHCR)ï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector)

  + `ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0`
* [Amazon Elastic Container Registry (Amazon ECR)ï»¿](https://gallery.ecr.aws/dynatrace/dynatrace-otel-collector)

  + `public.ecr.aws/dynatrace/dynatrace-otel-collector:0.44.0`
* [Docker Hub Container Registryï»¿](https://hub.docker.com/r/dynatrace/dynatrace-otel-collector)

  + `dynatrace/dynatrace-otel-collector:0.44.0`


---


## Source: scaling.md


---
title: How to scale the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/scaling
scraped: 2026-02-17T21:25:55.666213
---

# How to scale the OpenTelemetry Collector

# How to scale the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 10-min read
* Published Sep 30, 2025

When the Collector's CPU or memory usage exceeds a threshold that would put it
at risk of being overloaded if there were a burst of traffic, it is recommended
to find ways to either increase the resources allotted to the Collector, or to
scale processing to multiple Collector instances. We will primarily focus on
solutions available in Kubernetes here. Note that the guidance and examples in
this documentation are generalized and may not give optimal performance for your
specific case; you will need to analyze your systems to determine the best way
to scale them.

For more general information in the OpenTelemetry documentation, please see the
[Scaling the Collectorï»¿](https://opentelemetry.io/docs/collector/scaling/) page
on the OpenTelemetry website.

## Determining when to scale

You will want to consider scaling when you begin to approach the limits of the
resources that have been allotted to your Collector. Self-monitoring metrics
available through the Collector and metrics available from the host environment
(e.g. Kubernetes) will be helpful to track this. See our page on [Collector self-monitoring](/docs/ingest-from/opentelemetry/collector/self-monitoring "How to monitor OpenTelemetry Collectors with Dynatrace dashboards.")
for more information on collecting this data.
The following are a few metrics worth paying attention to:

* `otelcol_processor_refused_spans`: If you have the [Memory Limiter
  Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/memorylimiterprocessor)
  enabled, this metric (or the equivalent for other signals) will indicate that
  the Collector needs more memory to continue processing its current load.
* `otelcol_exporter_queue_capacity` and `otelcol_exporter_queue_size`: Once the
  exporter queue size starts to get close to or exceed the queue capacity, that
  indicates the Collector is having trouble sending data to the backend. This is
  either because workers are not becoming available to send the data, or the
  backend itself is overloaded. You may need to increase the processing power
  available to the Collector to continue processing this volume of data.
* `k8s.resource_quota.used`: If you are monitoring your Kubernetes cluster with
  the [Kubernetes Cluster
  Receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/k8sclusterreceiver),
  this can be used to determine the amount of
  CPU/memory quota your Collector has used.
* `container.cpu.usage` and `container.memory.usage`: If you are monitoring your
  cluster with the [Kubelet Stats
  Receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/kubeletstatsreceiver),
  these can tell you if a given Collector container is nearing or hitting its
  quota limits.

## Scaling the Collector

Kubernetes comes with multiple object types capable of scaling the Collector
based on the needs of specific scenarios. For simple scaling, Deployments or
ReplicaSets can be used to create a pool of Collectors that can be scheduled by
Kubernetes without too much forethought. For more general information on
Collector deployment architectures, see our guide on [Deploy Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.").

Most of the advice in this document applies to horizontally scaling the
Collector by creating more Collector instances or spreading instances across
machines. However, if your current deployment uses a single Collector instance
to do all your processing, you should first determine if vertically scaling the
Collector is sufficient for your anticipated load. Vertically scaling the
Collector has a lower cap on the amount of processing power and memory that can
be given to the Collector, but is also simpler. In Kubernetes, you can do this
by raising the CPU and memory limits on the Collector pod.

### Scaling stateless Collectors

It's comparatively easy to scale stateless Collectors: since it doesn't matter
which data goes to which Collector, the decision about which Collector to send a
payload to can be made regardless of the contents of the data. As a result,
any standard load balancer for a given transmission protocol should work.

The simplest way to balance load is through a Kubernetes Service object that
points to multiple replicas of a Collector pod deployed through any standard
type of Kubernetes workload such as a Deployment, ReplicaSet, StatefulSet, or
DaemonSet. For short-lived connections, this will distribute load among the
Collectors accessible through the service fairly evenly. Note that long-lived
connections, such as those over HTTP/2 or gRPC, will keep a connection open
to a single Collector and therefore may make the load between Collectors uneven.

For more complex cases, such as handling gRPC connections, a Service with type
`LoadBalancer` can offer more control over how load is balanced. LoadBalancer
Services are able to leverage a separate load balancer to determine which
Collector a connection is routed to. Service meshes such as Istio or Linkerd can
also help with load balancing, as they have detailed control over network
connections inside the cluster.

For cases where your deployment topology matters, for example with gateway
Collectors deployed through a DaemonSet, you can use a Service object with
specialized routing settings to only send data to Collectors running on the same
node as the source of the data. On Kubernetes version 1.26+, this is done by
configuring a service to [only accept traffic internal to a
nodeï»¿](https://kubernetes.io/docs/concepts/services-networking/service-traffic-policy/).

### Scaling stateful processing using non-pooled Collectors

When using the Collector to do stateful processing, it's important that the same
data is always sent to the same Collector. You can increase the throughput of
your pipeline while still following this rule by choosing certain Collectors to
handle certain data. This can be done by choosing a particular deployment
pattern for Collectors, or by assigning data sources to Collectors:

* **Sidecar Collectors**: If a Collector is deployed as a sidecar and is coupled
  to an application, then all the data from that application will go through the
  sidecar Collector and can be processed with stateful operations.
* **DaemonSet Collectors**: An agent Collector deployed to a Kubernetes node
  (such as through a DaemonSet) can be used for stateful processing if a given
  application on the node always sends its data to the Collector. Note that this
  assumes there is only a single Collector per node.
* **Single Collector**: If you only need to run a
  single Collector for a given set of data sources, this Collector can be used
  for stateful processing since all data will flow through the same Collector.
  You may choose this if you decide to send a particular signal or data from a
  chosen set of applications to a given Collector. Note that for
  high-availability, redundant Collector instances must be kept as backups and
  not receive data unless the first Collector goes down. Additionally,
  processing will be reset if a redundant Collector is activated.

### Scaling pooled stateful Collectors with the Load Balancing Exporter

Scaling a horizontally-scaled pool of stateful Collectors likely necessitates
using the [Load Balancing
Exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/exporter/loadbalancingexporter).
The Load Balancing Exporter turns the
Collector into an OTLP-aware load balancer that allows you to route data to a
specific downstream Collector based on information inside an OTLP payload such
as a metric name.

Note that for metrics, the Load Balancing Exporter component has a [Development
stability
levelï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/docs/component-stability.md).
It is not recommended for production use at this time.

#### Stateful processors

You will want to consider using the exporter if you are scaling and using any
of the following stateful components. We only cover components
included in the Dynatrace Collector here, you
will need to determine the best default for any other stateful components you
use. You can also configure which part of the data is used for routing. The best
key to use depends on your use-case, but we give recommendations below.

* The [Cumulative to Delta
  Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor):
  Data points for the same metric are required to be sent to the same Collector
  for the collection period of the metric. The `metric_name` key is therefore a
  good default for routing.
* The [Tail Sampling
  Processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor):
  In order to make a decision about whether to sample a trace, the processor
  must be able to see all spans within the trace. Therefore, all spans must be
  sent to the same Collector, and we recommend routing by the `traceID` key to
  accomplish this.
* The [Span Metrics
  Connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector):
  The connector needs to see all spans from a service in order to emit metrics
  about its performance. Therefore we highly recommend routing by the `service`
  key.

#### Configuring the Load Balancing Exporter

There are two important elements involved with configuring the [Load Balancing
Exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/exporter/loadbalancingexporter):
the key used to route the data, and the method the exporter uses to find
Collectors in the pool.

Configuring the routing key is done by setting the `routing_key` option. The defaults for each signal are:

* Traces: `traceID`
* Metrics: `service`
* Logs: `traceID` if present, otherwise a random trace ID. The `routing_key`
  option will not override this behavior and will have no effect on how logs are
  routed.

We recommend you leave these as the default or set them based on the
recommendations in the [Stateful processors](#stateful-processors) section
above.

The other important configuration option is the `resolver` key, which is used
by the exporter to determine which Collectors are available to forward data to.
In Kubernetes, we recommend using the `k8s` resolver since it is
Kubernetes-native. Specifically, it supports dynamically updating the pool based
on which Collector pods are running, and will add or remove Collectors if the
number of replicas changes. It will also remove Collectors that become
unhealthy, ensuring high-availability requirements are met if retries are also
configured through the `retry_on_failure` option.

Note that configuring the `static` resolver with a set pool of Collectors can
cause data loss if a Collector goes down and is not replaced before the retry
limit is met. The Collectors configured in the pool are set for the lifetime of
the load-balancing Collector.

#### Resiliency

The load balancing exporter comes with resiliency options to help mitigate the
risk of data loss. These options are both for dealing with a fluctuating number of downstream
Collectors as well as issues sending data to a particular Collector. The
[upstream
docsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/exporter/loadbalancingexporter#resilience-and-scaling-considerations)
cover these in detail and explain how and when to use them.

#### Scaling load balancer Collectors

Since the Load Balancing Exporter uses a deterministic hash to determine which
downstream Collector to send data to, load-balancing Collectors can be
considered stateless and can therefore be scaled using the approaches outlined
in the [Scaling stateless Collectors](#scaling-stateless-collectors) section.
Note that if the resolver for the load-balancing Collectors update their
downstream pools at different times, this may result in data meant for a single
Collector momentarily being sent to multiple Collectors.

## Demo configuration

```
extensions:



health_check:



endpoint: 0.0.0.0:13133



receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



exporters:



loadbalancing/traces:



protocol:



otlp:



resolver:



k8s:



service: traces-receiver.default



ports:



- 4317



loadbalancing/logs:



protocol:



otlp:



resolver:



k8s:



service: logs-receiver.default



ports:



- 4317



loadbalancing/metrics:



retry_on_failure:



enabled: true



initial_interval: 5s



max_interval: 30s



max_elapsed_time: 300s



sending_queue:



enabled: true



num_consumers: 10



queue_size: 1000



sizer: requests



protocol:



otlp:



resolver:



k8s:



service: metrics-receiver.default



ports:



- 4317



service:



extensions: [health_check]



pipelines:



metrics:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/metrics



traces:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/traces



logs:



receivers: [otlp]



processors: []



exporters:



- loadbalancing/logs
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we use the following components.

### Receivers

Under `receivers`, we configure the [`otlp` receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/receiver/otlpreceiver) to receive data over gRPC and HTTP.

### Exporters

In the `exporters` section, we configure three [`loadbalancing exporters`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/exporter/loadbalancingexporter),
one for each signal. The exporters are all configured to use the `k8s` resolver,
which uses a Kubernetes service to determine the pool of Collectors to send data
to. One reason to split further processing by signal is that each signal likely
receives different amounts of traffic: for example, you may receive a large
amount of logs, some traces, and relatively few metrics. Therefore, you would
want the Collector pool that processes logs to be bigger than the one that processes
metrics; extra Collectors allocated for processing fewer metrics may waste
resources.

### Service pipelines

In our pipelines, we receive data over OTLP and export it through the Load
Balancing Exporter for the particular signal, without doing any additional
processing. Since this Collector is exclusively for load balancing, we want to
do as little processing as possible so it can handle as much data as possible.

## Related topics

* [Batch OTLP requests with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")
* [Apply memory limits to the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")


---


## Source: system-requirements.md


---
title: Dynatrace OTel Collector system requirements.
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/system-requirements
scraped: 2026-02-16T21:32:49.819658
---

# Dynatrace OTel Collector system requirements.

# Dynatrace OTel Collector system requirements.

* Latest Dynatrace
* Reference
* 2-min read
* Updated on Sep 04, 2025

This page describes system requirements for the Dynatrace OpenTelemetry Collector distribution for different use cases.

### Hardware used

The numbers below were gathered using an Azure virtual machine of type Dadsv5-series (AMD EPYC 7763v Genoa CPU) with 4 vCPUs and 16GB RAM.

### CPU and memory requirements for traces, metrics and logs (combined)

The requirements for the Dynatrace Collector are based on a load scenario with the following numbers per second:

* 1000 traces (~1.2 KB each)
* 1000 metrics (~1.2 KB each)
* 1 MB logs

The recommended resources for this combined scenario are:

* 500 MiB RAM
* 500 mCPU

If you need additional data processing (for example, filter or transform processors), system requirements will increase.

For specific scaling and infrastructure architecture considerations, see [Deploy Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [How to scale the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/scaling "How to scale the OpenTelemetry Collector.").

### Specific load scenarios

The Dynatrace Collector was also tested under heavier scenarios than above but only with single signal types.
The following table shows performance data based on the following base data sizes:

* Traces: ~1 KiB per trace
* Metrics: ~3 KiB per metric
* Logs: ~3 KiB per line

This table shows throughput scenarios based on the above data sizes with different amounts of load and different used protocols.

| Scenario (traces, metrics, logs per second) | CPU cores | RAM (MiB) |
| --- | --- | --- |
| OTLP-HTTP 10k traces | 0.25 | 100 |
| OTLP-HTTP 100k traces | 1.5 | 120 |
| OTLP-HTTP 10k metrics | 0.25 | 110 |
| OTLP-HTTP 100k metrics | 1 | 100 |
| Syslog 10k logs 1 per batch | 0.2 | 100 |
| Syslog 10k logs 100 per batch | 0.2 | 100 |
| Syslog 70k logs 1 per batch | 1 | 100 |
| Syslog 70k logs 100 per batch | 0.5 | 110 |

### Prometheus scrape performance

Additional metrics based load scenarios were done based on Prometheus scraping with the following base settings:

* 1s scrape interval
* Metrics data size: ~3 KiB per metric

This table shows the load results with different scenarios.

| Scenario | CPU cores | RAM (MiB) |
| --- | --- | --- |
| 1 endpoint (10k data points each) | 0.5 | 300 |
| 1 endpoint (1k data points each) | 0.1 | 140 |
| 5 endpoints (1k data points each) | 1.5 | 250 |
| 10 endpoints (1k data points each) | 2 | 500 |


---


## Source: batch.md


---
title: Batch OTLP requests with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/batch
scraped: 2026-02-17T05:07:06.562681
---

# Batch OTLP requests with the OpenTelemetry Collector

# Batch OTLP requests with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Oct 11, 2023

The following configuration example shows how you configure a Collector instance and its native batch processor to queue and batch OTLP requests and improve throughput performance.

Recommended configuration

For optimal performance of your Collector instance, we recommend that you apply this configuration with all setups.

If you use other processors, make sure the batch processor is configured last in your pipeline.

## Prerequisites

* One of the following Collector distributions with the [batch processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + The OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.") distribution
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



batch/traces:



send_batch_size: 5000



send_batch_max_size: 5000



timeout: 60s



batch/metrics:



send_batch_size: 3000



send_batch_max_size: 3000



timeout: 60s



batch/logs:



send_batch_size: 1800



send_batch_max_size: 2000



timeout: 60s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [batch/traces]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [batch/metrics]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [batch/logs]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify a different [`batch` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/batchprocessor)
for each telemetry signal, with the following parameters:

* `send_batch_size`: sets the minimum number of entries the processor will queue before sending the whole batch.
* `send_batch_max_size`: sets the maximum number of entries a batch may contain. More entries will split the batch into smaller ones.
* `timeout`: defines the duration after which the batch will be sent. A batch is sent after the `timeout` only when the `send_batch_size` condition is not reached.

With this configuration, the Collector queues telemetry entries in batches, ensuring a good balance between the size and number of export requests
to the Dynatrace API.

Batch size values

Not only the number of individual telemetry entries will contribute to the eventual size
of a batch, but also the number of associated attributes and their size.

For example, attributes on spans/metrics/logs can make a batch size with the same amount of entries larger,
depending on how many/how large the attributes are.

Use the configuration values above as a starting point, but be sure to adapt them to fit your data volume
and comply with the Dynatrace API limits for each signal type ([traces](/docs/ingest-from/opentelemetry/otlp-api/ingest-traces#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply."),
[metrics](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#limits "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply."), [logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs#ingestion-limits "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")) to avoid request rejections.

You can use the [ActiveGate self-monitoring metrics](/docs/ingest-from/dynatrace-activegate/activegate-sfm-metrics#rest "Explore ActiveGate self-monitoring  metrics.")
to troubleshoot rejected requests. For example, you can use: `dsfm:active_gate.rest.request_count` filtering for the `operation`
dimension (`POST /otlp/v1/<...>` for OTLP ingest) and split by `response_code`. Large requests are rejected with HTTP status code `413`.

Another alternative is checking the Collector logs for error messages such as: `HTTP Status Code 413, Message=Max Payload size of`.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our batch processor by referencing it under `processors` for each respective pipeline.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: enrich.md


---
title: Enrich OTLP with OneAgent data (non-containerized)
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/enrich
scraped: 2026-02-17T05:06:37.065527
---

# Enrich OTLP with OneAgent data (non-containerized)

# Enrich OTLP with OneAgent data (non-containerized)

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 17, 2025

The following configuration example shows how you configure a Collector instance to enrich OpenTelemetry data with OneAgent host entities.

Enrichment is used for linking OpenTelemetry data to its OneAgent host and properly associating it within the topology model. For example, when ingesting logs from different hosts, tying the host entity to the respective log data allows you to run host-based log analytics tasks.

Container environments

Enrichment is specific to non-container OneAgent environments. Configuring a containerized Collector enrichment setup may lead to incorrect host and topology associations.

## Prerequisites

* One of the following Collector distributions with the [Resource Detection processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* A OneAgent running on the same host as the Collector, where the OneAgent monitors in either Full-Stack, Infrastructure, or Foundation & Discovery mode.
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported, configured as system environment variable
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate), configured as system environment variable

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



resourcedetection/dynatrace:



detectors: [dynatrace]



override: false



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [resourcedetection/dynatrace]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify the [`resourcedetection` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor) and configure it with the [Dynatrace-specific detector `dynatrace`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/resourcedetectionprocessor/README.md#dynatrace).

With this configuration, the resource detector processor will attempt to load the following three attributes from the [OneAgent enrichment file](/docs/ingest-from/extend-dynatrace/extend-data#dynatrace-oneagent "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions."):

* `dt.entity.host`
* `host.name`
* `dt.smartscape.host`

If the resource detector could load these values successfully, it will add them as resource attributes to the OTLP request. No additional processor configuration is necessary.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `headers`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into service pipelines, which will perform these steps:

* accept OTLP requests on the configured ports
* enrich them with the Dynatrace-relevant host data, using the resource detector processor
* and export the enriched data to Dynatrace


---


## Source: grpc.md


---
title: Transform OTLP gRPC to HTTP with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/grpc
scraped: 2026-02-17T05:08:18.584161
---

# Transform OTLP gRPC to HTTP with the OpenTelemetry Collector

# Transform OTLP gRPC to HTTP with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 11, 2023

The following configuration example shows how you would configure a Collector instance to transform a gRPC OTLP request to its HTTP counterpart.

## Prerequisites

* One of the following Collector distributions:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



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

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the gRPC [`otlp` receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/receiver/otlpreceiver) as active receiver component for our Collector instance.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into pipelines, which explictly accept gRPC requests and forward them on HTTP to Dynatrace.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: histograms.md


---
title: Compute histogram summaries with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/histograms
scraped: 2026-02-16T09:33:35.925773
---

# Compute histogram summaries with the OpenTelemetry Collector

# Compute histogram summaries with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Apr 08, 2024

Ingest histograms directly

Starting with Dynatrace version 1.300, histogram ingestion is supported directly via OTLP ingest API. Consequently, it's not required to use Collector as a workaround. Dynatrace recommends ingesting histograms directly without additional data manipulation.

The following configuration example shows how to use the Collector to compute and ingest summaries of histogram buckets, such as the overall sum of all values in the bucket and their total count.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and [filterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) processors:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



transform:



metric_statements:



- context: metric



statements:



# Get count from the histogram. The new metric name will be <histogram_name>_count



- extract_count_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# Get sum from the histogram. The new metric name will be <histogram_name>_sum



- extract_sum_metric(true) where type == METRIC_DATA_TYPE_HISTOGRAM



# convert the <histogram_name>_sum metrics to gauges.



- convert_sum_to_gauge() where IsMatch(name, ".*_sum")



filter:



metrics:



metric:



# Drop metrics of type histogram. The _count and _sum metrics will still be exported.



- type == METRIC_DATA_TYPE_HISTOGRAM



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [otlp]



processors: [transform,filter]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance and configure it to accept OTLP requests on gRPC and HTTP.

### Processors

Under `processors`, we configure the following two processor instances:

* [`transform`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), to compute the desired sum and count values of the histograms:

  + We first use the function [`extract_count_metric`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_count_metric) to compute the number of values in each histogram bucket.
  + Then, we use the function [`extract_sum_metric`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#extract_sum_metric) to compute the total sum of all of its values and convert it to a gauge using [`convert_sum_to_gauge`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md#convert_sum_to_gauge).
* [`filter`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), to drop the existing histogram buckets (based on `type`) and avoid histogram-related error messages.

With this configuration, the Collector drops histogram metrics and creates in their place two new metrics for the sum and item count of each respective histogram.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`:

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into a metric pipeline and enable the two processors by referencing them under `processors`.

## Limits and limitations

Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: jaeger.md


---
title: Ingest Jaeger data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/jaeger
scraped: 2026-02-17T05:07:56.609579
---

# Ingest Jaeger data with the OpenTelemetry Collector

# Ingest Jaeger data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Oct 11, 2023

The following configuration example shows how you configure a Collector instance to accept Jaeger data, transform it to OTLP, and send it to the Dynatrace backend.

## Prerequisites

* One of the following Collector distributions with the [Jaeger receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/jaegerreceiver):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



jaeger:



protocols:



grpc:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [jaeger]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `jaeger` receiver as active receiver component for our Collector instance.

The Jaeger receiver can be customized with [a few more attributesï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/jaegerreceiver), which we leave with their default values in our example.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will handle our Jaeger transformation to OTLP.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: memory.md


---
title: Apply memory limits to the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/memory
scraped: 2026-02-17T21:25:06.587423
---

# Apply memory limits to the OpenTelemetry Collector

# Apply memory limits to the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Jan 08, 2026

The following configuration example shows how you configure a Collector instance and its native memory limiter processor to guarantee memory allocation keeps within the specified parameters.

Recommended configuration

For optimal memory usage with your Collector instance, we recommend that you
apply this configuration with most containerized setups. See the section on
[deployment considerations](#deployment-considerations) for more information.

## Prerequisites

* One of the following Collector distributions with the [memory limiter processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Core](/docs/ingest-from/opentelemetry/collector#collector-core "Learn about the Dynatrace OTel Collector.") or [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



memory_limiter:



check_interval: 1s



limit_percentage: 90



spike_limit_percentage: 20



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [memory_limiter]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is mainly for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processors

Under `processors`, we specify the [`memory_limiter` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor/memorylimiterprocessor) with the following parameters:

* `check_interval` configured to check the memory status every second
* `limit_percentage` configured to allow a maximum memory allocation of 90 percent
* `spike_limit_percentage` configured to allow a maximum spike memory usage of 20 percent

With this configuration, the Collector checks the memory allocation every second
and starts to apply pressure using separate mechanisms after the following
limits are reached:

* Soft limit (`limit_percentage - spike_limit_percentage`): After this limit is
  reached, the processor rejects payloads until memory usage is under the limit.
  It is up to the receiver upstream of the processor to send the proper
  rejection messages.
* Hard limit: (`limit_percentage`): After this limit is reached, the processor
  will force garbage Collection until memory usage is under the limit. Data will
  continue to be rejected until usage is under the soft limit.

In addition to the memory limiter processor, we highly recommend you set the
`GOMEMLIMIT` environment variable to a value 80% of the hard limit. Note that
`GOMEMLIMIT` requires an absolute value in bytes to be set. For example, you
could set `GOMEMLIMIT=1024MiB` to start increasing the frequency of garbage
collection cycles once the Collector reaches 1024 MiB of memory used on the Go
VM heap. For more information, see the [Go package
documentationï»¿](https://pkg.go.dev/runtime#hdr-Environment_Variables) describing
how the environment variable works.

#### Deployment considerations

In containerized environments, or other places where the host environment sets
the Collector's maximum allowed memory, we recommend you use the
`limit_percentage` and `spike_limit_percentage` options.

For deployments on virtual machines or bare metal where the Collector is not
given an explicit memory quota, we instead recommend you use the `limit_mib` and
`spike_limit_mib` options.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into pipelines for traces, metrics, and logs and enable our memory limiter processor by referencing it under `processors` for each respective pipeline.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: netflow.md


---
title: Ingest NetFlow with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/netflow
scraped: 2026-02-17T21:31:31.211646
---

# Ingest NetFlow with the OpenTelemetry Collector

# Ingest NetFlow with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Jan 27, 2026

The following configuration example shows how to configure a Collector instance to accept NetFlow packets and ingest them as OTLP requests into Dynatrace.

## Prerequisites

* One of the following Collector distributions with the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver):

  + [The Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + [A custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported.
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the Ingest logs (`logs.ingest`) scope.
* A NetFlow- or sFlow-capable device that can send NetFlow packets to the Collector instance.

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Collector configuration

```
receivers:



netflow:



hostname: "0.0.0.0"



scheme: netflow



port: 2055



sockets: 2



workers: 4



processors:



batch:



send_batch_size: 30



timeout: 30s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



logs:



receivers: [netflow]



processors: [batch]



exporters: [otlp_http]
```

Check the [NetFlow receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#netflow-receiver) documentation for the available configuration options.

We recommend setting the `sockets` parameter to match the number of CPU cores available on the Collector instance, and the `workers` parameter to twice the number of sockets. This configuration allows the Collector to process multiple incoming NetFlow packets concurrently, which improves performance.

For extremely large volumes of data, you should parallelize the configuration among multiple Collector instances.

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `netflow` receiver as the active receiver component for our Collector instance and configure it to listen on specified ports.

### Processors

Under `processors`, we specify the `batch` processor, which batches the incoming NetFlow packets before sending them to Dynatrace. This is useful for optimizing performance and reducing the number of requests sent.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble our receiver and exporter objects into a logs pipeline, which will listen on the configured address for incoming NetFlow packets and forward them to Dynatrace using the exporter.

## Data visualization

The logs records will be available in Dynatrace with fields documented in the [receiver documentationï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/netflowreceiver#data-format).

### Example DQL queries

* Fetch all NetFlow logs and summarize the bytes and packets by source and destination addresses:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes)), packets=sum(toDouble(flow.io.packets))}, by: {source = source.address, destination = destination.address}



  | fieldsAdd bytes_relative=bytes



  | fieldsAdd packets_relative=packets



  | sort bytes desc
  ```

  ![Sample NetFlow charts showing top sources, destination and conversations](https://dt-cdn.net/images/screenshot-2025-06-16-at-12-55-07-pm-1956-d01b596006.png)
* Fetch the most used ports:

  ```
  fetch logs



  | filter otel.scope.name == "otelcol/netflowreceiver"



  | summarize {bytes=sum(toDouble(flow.io.bytes))}, by: {port = destination.port}



  | sort bytes desc



  | limit 10
  ```

  ![A NetFlow chart showing the top used ports by bytes](https://dt-cdn.net/images/screenshot-2025-06-16-at-1-04-11-pm-734-9a3a884a16.png)

## Limits and limitations

Logs are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Ingest logs from files with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")


---


## Source: prometheus.md


---
title: Scrape Promethus metrics with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/prometheus
scraped: 2026-02-17T21:26:39.844213
---

# Scrape Promethus metrics with the OpenTelemetry Collector

# Scrape Promethus metrics with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 09, 2025

The following configuration example shows how you configure a Collector instance to scrape data from an existing Prometheus setup and import it as OTLP request into Dynatrace.

## Prerequisites

* A Prometheus instance running on port 8888
* One of the following Collector distributions with the [Prometheus receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/prometheusreceiver), the [metric start time processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor), and the [cumulative-to-delta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

Dynatrace Collector v0.41.0+

The example pipeline below uses the [`metricstarttime` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor), which is required to convert the metrics to delta temporality.

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: 'node-exporter'



scrape_interval: 60s



static_configs:



- targets: ['prometheus-prometheus-node-exporter:9100']



- job_name: opentelemetry-collector



scrape_interval: 60s



static_configs:



- targets:



- 127.0.0.1:8888



processors:



metricstarttime:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [prometheus]



processors: [metricstarttime, cumulativetodelta]



exporters: [otlp_http]
```

Dynatrace Collector v0.40.0 or earlier

In **v0.40.0** of the Dynatrace Collector, you must run the Collector
with the following flag in order to keep adjusting start times in the
Prometheus receiver:

```
--feature-gates=-receiver.prometheusreceiver.RemoveStartTimeAdjustment
```

```
receivers:



prometheus:



config:



scrape_configs:



- job_name: 'node-exporter'



scrape_interval: 60s



static_configs:



- targets: ['prometheus-prometheus-node-exporter:9100']



- job_name: opentelemetry-collector



scrape_interval: 60s



static_configs:



- targets:



- 127.0.0.1:8888



processors:



cumulativetodelta:



max_staleness: 25h



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



metrics:



receivers: [prometheus]



processors: [cumulativetodelta]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

Cumulativetodelta processor recommendation

It is recommended to set the `max_staleness` parameter of the [cumulativetodelta processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to a value higher than how often the collector receives metrics (e.g., how often metrics via OTLP are received, or how long the Prometheus scrape interval is). This ensures that no references to abandoned metric streams accumulate in memory over time.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `prometheus` receiver as active receiver component for our Collector instance. We configure the receiver with the two jobs `node-exporter` and `opentelemetry-collector` under `scrape_configs`, to fetch data from the specified hosts once a minute (`scrape_interval: 60s`).

For a full list of configuration parameters, see the [Prometheus documentationï»¿](https://github.com/prometheus/prometheus/blob/v2.28.1/docs/configuration/configuration.md).

### Processors

Under `processors`, we specify the [`cumulativetodelta` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/cumulativetodeltaprocessor) to convert the metrics emitted by the Prometheus receiver to their [delta aggregation format](/docs/ingest-from/opentelemetry/collector/configuration#delta-metrics "How to configure the OpenTelemetry Collector.").

In Dynatrace Collector v0.41.0+, we specify the
[`metricstarttime`
processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/metricstarttimeprocessor)
to add start timestamps to the metrics. This is required to properly convert the metrics to delta temporality.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into a metrics pipeline, which will execute the Prometheus jobs, convert their metrics to delta values, and ingest the data into Dynatrace.

## Limits and limitations

Metrics are ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP API](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and are subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")

To avoid data duplication, make sure that only one OpenTelemetry Collector scrapes a given target (for example, Kafka broker or Prometheus endpoint).

If you run multiple collector replicas, configure each one with a different target. This prevents duplicate metrics and unnecessary ingest costs.

The [Target Allocatorï»¿](https://opentelemetry.io/docs/platforms/kubernetes/operator/target-allocator/) automatically distributes the Prometheus targets among a pool of Collectors.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: redact.md


---
title: Mask sensitive data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/redact
scraped: 2026-02-16T09:33:56.399168
---

# Mask sensitive data with the OpenTelemetry Collector

# Mask sensitive data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 12, 2026

Telemetry data can often include sensitive data (such as [PIIï»¿](https://en.wikipedia.org/wiki/Personal_data)), which may need to be redacted due to security and regulatory reasons. While this can be implemented on the application side, it typically is best to handle this centrally using gateways such as the Collector. This enables the single-point management of redaction rules across all your applications and services, without the need to update your code each time a new redaction rule is required.

This page shows sample Collector configurations for the redaction of specific sensitive data (for example, credit card numbers or email addresses) which may appear in telemetry data and which should be masked/redacted before leaving your network.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and/or [redactionï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/redactionprocessor) processors:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + [OpenTelemetry Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Redaction processor versus transform processor

The following examples make use of these two Collector [processorsï»¿](https://opentelemetry.io/docs/collector/architecture/#processors):

* the [transform processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md)
* the [redaction processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/redactionprocessor/README.md)

While the following examples use both processors to mask data, each processor has its own distinct purpose. The redaction processor is straightforward and takes a list of values, based on which matching data will be completely redacted. On the other hand, the purpose of the transform processor is more versatile and goes beyond mere data redaction.

For data redaction, typically either processor can be used and you may want to choose the one best for your use case. For example, for full data redaction, the redaction processor may be easier to use. On the other hand, partial data redaction can only be achieved with the transform processor. In addition, the transform processor can also filter by data in the body of logs, whereas the redaction processor only has access to attributes.

## Limitations and considerations

The examples provided on this page are samples demonstrating common redaction scenarios. Note the following:

* The examples may not be exhaustive for all use cases. You may need to adapt them to your specific requirements.
* The regex patterns and attribute matching only work when the entire attribute value matches the pattern to be redacted. Partial matches within larger strings may require more complex patterns or additional processing.
* The span name is stored as a separate field in the OTLP message structure, not as an attribute. Therefore, redaction processors targeting attributes will not affect span names by default. See the [Span names](#span-names) example for how to handle this.
* Processor order in pipelines matters. Apply transform/redaction before routing or exporting, and keep related processors adjacent so downstream steps see the sanitized data.

## Demo configuration

This YAML document is a basic Collector configuration skeleton, containing basic, general components (that is, receivers, exporters, and the pipeline definition).

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



"Authorization": "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [PLACEHOLDER-FOR-PROCESSOR-REFERENCES]



exporters: [otlp_http]
```

Make sure to replace the placeholder values in the document with the respective configurations:

* `PLACEHOLDER-FOR-PROCESSOR-CONFIGURATIONS`: the relevant processor configuration
* `PLACEHOLDER-FOR-PROCESSOR-REFERENCES`: referencing the applicable processor objects for the individual signal types

### IP addresses

Using the transform processor, we mask the attribute `client.address` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



# this will not only mask end user client IP addresses,



# but also the address of a server acting as a client when establishing a connection to another server



- set(attributes["client.address"], "<masked-clientip-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Email addresses

Using the transform processor, we mask the attribute `user.email` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.email"], "<masked-email-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Dynatrace API tokens

Using the redaction processor, we use the regular expression `dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})` to mask all occurrences of [Dynatrace API tokens](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.") in our telemetry data.

```
redaction:



allow_all_keys: true



blocked_values:



- dt0[a-z]0[1-9]\.[A-Za-z0-9]{24}\.([A-Za-z0-9]{64})



summary: info
```

### Usernames

Using the transform processor, we mask the attributes `user.id`, `user.name`, and `user.full_name` with the [`set` statementï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set).

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- set(attributes["user.id"], "<masked-userid-ot>")



- set(attributes["user.name"], "<masked-username-ot>")



- set(attributes["user.full_name"], "<masked-userfullname-ot>")



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

### Credit card numbers

Using the transform processor, we configure three [`replace_all_patterns` statementsï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#replace_all_patterns) to mask any occurrences of credit card numbers and mask everything but the last four digits.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements: &filter-statements



- replace_all_patterns(attributes, "value", "^3\\s*[47](\\s*[0-9]){9}((\\s*[0-9]){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^(5[1-5]([0-9]){2}|222[1-9]|22[3-9]\\d|2[3-6]\\d{2}|27[0-1]\\d|2720)(\\s*[0-9]){8}\\s*([0-9]{4})$", "<masked-pcard$$4-ot>") where IsValidLuhn(attributes["value"])



- replace_all_patterns(attributes, "value", "^4(\\s*[0-9]){8,14}\\s*(([0-9]\\s*){4})$", "<masked-pcard$$2-ot>") where IsValidLuhn(attributes["value"])



metric_statements:



- context: datapoint



statements: *filter-statements



log_statements:



- context: log



statements: *filter-statements
```

For credit card numbers, it is also possible to use the built-in, [standard OTTL function `IsValidLuhn()`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/pkg/ottl/ottlfuncs#isvalidluhn) instead of regular expressions, if you prefer to block values altogether instead of just masking them.

### IBAN numbers

Using the redaction processor, we use the regular expression `^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$` to mask all IBAN occurrences in our telemetry data.

```
redaction:



allow_all_keys: true



blocked_values:



- "^[A-Z]{2}[0-9]{2}(\\s*[A-Z0-9]){8,30}$"



summary: info
```

### Span names

Span names are not stored as attributes in the OTLP message structure, so attribute-based redaction does not apply to them.
There are multiple ways of redacting and simplifying span names:

#### Generate a new span name

Recommended

`set_semconv_span_name` is available from Collector Contrib version 0.142.0 and .

Use the transform processor's [`set_semconv_span_name`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor#set_semconv_span_name) to derive a low-cardinality name that is compliant with OpenTelemetry semantic conventions. This will use the (low-cardinality) `http.request.method` and `http.route` to generate a new span name. It keeps the name consistent with HTTP/RPC/messaging/database conventions and avoids leaking identifiers.

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- set_semconv_span_name("1.37.0")
```

#### Redact the span name explicitly

```
transform:



error_mode: ignore



trace_statements:



- context: span



statements:



- replace_pattern(name, "(GET /api/v1/users/)\\d+", "$$1{id}")
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we use the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

### Processors

Under `processors`, we place the configuration for the relevant processor instances.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble all the configured objects into pipelines for the individual telemetry signals (traces, etc.) and have the Collector instance run the configured tasks.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: sampling.md


---
title: Sampling with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/sampling
scraped: 2026-02-17T05:04:00.823679
---

# Sampling with the OpenTelemetry Collector

# Sampling with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 5-min read
* Published May 28, 2024

A distributed application under heavy load may generate a massive amount of observability data. This data incurs generation, processing, transmission, and storage costs. However, it's often possible to use samplingâwhere you use only a relatively small portion of the observability data and drop the restâto reduce costs and still effectively monitor your application.

In OpenTelemetry, there are two main sampling methods:

* **Head sampling** is done within your application by the OpenTelemetry SDK, and typically involves saving a random sample of transactions.

  Head sampling is simple and effective, but it has important limitations. For example, because the sampling decision needs to be made at the start of the transaction, it can't be affected by anything that happens after that point.
* **Tail sampling** is used to make sampling decisions based on information unknown at the start of the transaction.

  In OpenTelemetry, tail sampling is typically done with the Collector by temporarily storing the full set of monitoring data until a transaction is completed. The Collector then decides to either save or drop the transaction data based on a set of sampling policies.

  Because tail sampling typically is not random, it's important to ensure that any calculated metrics are unbiased. This can be done by calculating metrics from the full set of transactions, as shown below, or from a separate, randomly sampled stream.

The following configuration example shows how to configure a Collector instance to sample trace data and import it as an OTLP request into Dynatrace. It uses the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) to compute service metrics from traces before sampling in order to ensure their accuracy.

## Prerequisites

* One of the following Collector distributions with the [`transform`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor), [`filter`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), and [`tail_sampling`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor) processors, and the [`spanmetrics`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) connector:

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + The OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.") distribution
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



tail_sampling:



# This configuration keeps errors, traces longer than 500ms, and 20% of all remaining traces.



# Adjust with policies of your choice.



policies:



- name: policy1-keep-errors



type: status_code



status_code: {status_codes: [ERROR, UNSET]}



- name: policy2-keep-slow-traces



type: latency



latency: {threshold_ms: 500}



- name: policy3-keep-random-sample



type: probabilistic



probabilistic: {sampling_percentage: 20}



decision_wait: 30s



connectors:



spanmetrics:



aggregation_temporality: "AGGREGATION_TEMPORALITY_DELTA"



namespace: "requests"



metrics_flush_interval: 15s



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: Api-Token ${env:DT_API_TOKEN}



service:



pipelines:



traces:



receivers: [otlp]



processors: [tail_sampling]



exporters: [otlp_http]



traces/spanmetrics:



receivers: [otlp]



processors: []



exporters: [spanmetrics]



metrics:



receivers: [spanmetrics]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance and configure it to accept OTLP requests on gRPC and HTTP.

### Processors

* [`tail_sampling`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/tailsamplingprocessor) to sample distributed traces based on properties of the trace.

### Connectors

Under `connectors`, we specify the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) to compute service metrics from spans.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we assemble three pipelines:

* `traces` assembles the OTLP receiver, tail sampling processor, and `otlp_http` exporter to send sampled spans to Dynatrace.
* `traces/spanmetrics` uses the same OTLP receiver and the `spanmetrics` connector to compute service metrics from received spans, without sampling, and forwards the computed metrics to `metrics`.
* `metrics` uses the `transform`, `filter`, and `transform/spanmetrics` processors to format metrics for Dynatrace metric ingest before sending metrics to Dynatrace using the `otlp_http` exporter.

## OpenTelemetry sampling considerations

### Mixed-mode sampling

OpenTelemetry and OneAgent use incompatible approaches to sampling that should not be mixed. If a distributed trace, which may include multiple applications and services, only partially utilizes either method, it's likely to result in inconsistent results and incomplete distributed traces. Each distributed trace should be sampled by only one of the methods to ensure it's captured in its entirety.

### Trace-derived service metrics

Dynatrace trace-derived metrics are calculated from trace data after it's ingested into Dynatrace.

If OpenTelemetry traces are sampled, the trace-derived metrics are calculated only from the sampled subset of trace data. This means that some trace-derived metrics might be biased or incorrect.

For example, a probabilistic sampler that saves 5% of traffic will result in a throughput metric that shows 5% of the actual throughput. If you use OpenTelemetry tail-based sampling to also capture 100% of slow or error traces, your service metrics will not only show incorrect throughput, but will also incorrectly bias error rates and response times.

To mitigate this, if you want to sample OpenTelemetry traces, you should calculate service metrics before sampling and use those metrics rather than the trace-derived metrics calculated by Dynatrace. If you're using the Collector for sampling, trace-derived metrics should be calculated by the Collector before applying sampling, or by the SDK. This can be done with the [`spanmetrics` connectorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/connector/spanmetricsconnector) as shown in the example above.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Batch OTLP requests with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")
* [Compute histogram summaries with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")
* [Apply memory limits to the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")
* [Send OpenTelemetry data to multiple backends](/docs/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")


---


## Source: transform.md


---
title: Transform and filter data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/transform
scraped: 2026-02-17T21:32:29.153387
---

# Transform and filter data with the OpenTelemetry Collector

# Transform and filter data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Aug 19, 2024

The following configuration example shows how to configure a Collector instance to transform and manipulate OTLP requests, before forwarding them to Dynatrace.

Using the processors shown in this example (`filter` and `transform`), it is possible to streamline requests before sending them to Dynatrace and omit data possibly irrelevant to your use case, and to reduce billing costs.

## Prerequisites

* One of the following Collector distributions with the [transformï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) and [filterï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor) processors

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [API URL](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") of your Dynatrace environment
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



otlp:



protocols:



grpc:



endpoint: 0.0.0.0:4317



http:



endpoint: 0.0.0.0:4318



processors:



transform:



trace_statements:



- context: resource



statements:



# Only keep a certain set of resource attributes



- keep_matching_keys(attributes, "^(aaa|bbb|ccc).*")



- context: span



statements:



# Only keep a certain set of span attributes



- keep_matching_keys(attributes, "(^xyz.pqr$)|(^(aaa|bbb|ccc).*)")



# Set a static key



- set(attributes["svc.marker"], "purchasing")



# Delete a specific key



- delete_key(attributes, "message")



# Rewrite a key



- set(attributes["purchase.id"], ConvertCase(attributes["purchase.id"], "upper"))



# Apply regex replacement



- replace_pattern(name, "^.*(DataSubmission-\d+).*$", "$$1")



metric_statements:



- context: metric



statements:



# Rename all metrics containing '_bad' suffix in their name with `_invalid`



- replace_pattern(name, "(.*)_bad$", "$${1}_invalid")



filter:



error_mode: ignore



traces:



span:



# Filter spans with resource attributes matching the provided regular expression



- IsMatch(resource.attributes["k8s.pod.name"], "^my-pod-name.*")



metrics:



metric:



# Filter metrics which contain at least one data point with a "bad.metric" attribute



- 'HasAttrKeyOnDatapoint("bad.metric")'



logs:



log_record:



# Filter logs with resource attributes matching the configured names



- resource.attributes["service.name"] == "service1"



- resource.attributes["service.name"] == "service2"



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [otlp]



processors: [filter,transform]



exporters: [otlp_http]



metrics:



receivers: [otlp]



processors: [filter]



exporters: [otlp_http]



logs:



receivers: [otlp]



processors: [filter]



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receiver

Under `receivers`, we specify the standard `otlp` receiver as active receiver component for our Collector instance.

This is for demonstration purposes. You can specify any other valid receiver here (for example, `zipkin`).

### Processor

#### Transform

Under `processors`, we specify the [`transform` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/transformprocessor) with a set of different attribute modification statements. `context` indicates the scope to which the statements should apply (here, `resource` for resource attributes, `span` for span attributes, and `metric` for metrics).

See the [OpenTelemetry documentation of the transform processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/transformprocessor/README.md) for more details on the individual configuration options.

The sample configuration above uses the following statements:

Statement

Description

[`keep_matching_keys`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#keep_matching_keys)

Evaluates the attribute key names and only keeps those, whose names match the given regular expressions of `^(aaa|bbb|ccc).*` for resource attributes and `(^xyz.pqr$)|(^(aaa|bbb|ccc).*)` for span attributes.

[`set`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#set)

Adds/changes the following two span attributes:

* `svc.marker`, with the static value `purchasing`
* `purchase.id`, coverting its value to uppercase, using [`ConvertCase`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#convertcase)

[`delete_key`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#delete_key)

Deletes attributes named `message`.

[`replace_pattern`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#replace_pattern)

Matches a string against a given regular expression and perform a string substitution on all matching entries.

In our example, we first use it for traces to match the name against the regular expression `^.*(DataSubmission-\d+).*$` and replace its content with the first capture group (`$$1`) of our expression. This essentially means, we search strings for `DataSubmission` suffixed by a number and â if found â only keep the value of the found match.

We also use the function for metrics with the regular expression `(.*)_bad$`, to change the `_bad` suffix to `_invalid`.

#### Filter

In addition, we also configure an instance of the [`filter` processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/processor/filterprocessor), to filter signal based on the following criteria:

Signal

Description

Traces

Uses [`IsMatch`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/pkg/ottl/ottlfuncs/README.md#ismatch) to match the name of resource attributes against the regular expression `^my-pod-name.*`, dropping spans with attributes whose names start with `my-pod-name`.

Metrics

Uses [`HasAttrKeyOnDatapoint`ï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/filterprocessor/README.md#HasAttrKeyOnDatapoint) to evalute if datapoints have attributes with the name `bad.metric`.

Logs

Uses a strict string match of the resource attribute `service.name` against the strings `service1` and `service2`.

See the [OpenTelemetry documentation of the filter processorï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/blob/v0.145.0/processor/filterprocessor/README.md) for more details on the individual configuration options.

### Exporter

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipeline

Under `service`, we assemble our receiver, processor, and exporter objects into a traces pipeline, which accepts OTLP traces on the configured endpoints and transforms trace attributes according to the configured rules, before forwarding everything to Dynatrace using the exporter.

## Limits and limitations

Data is ingested using the OpenTelemetry protocol (OTLP) via the [Dynatrace OTLP APIs](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") and is subject to the API's limits and restrictions.
For more information see:

* [OpenTelemetry metrics limitations](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Dynatrace metrics mapping](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OpenTelemetry logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: zipkin.md


---
title: Ingest Zipkin data with the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases/zipkin
scraped: 2026-02-17T21:31:16.420627
---

# Ingest Zipkin data with the OpenTelemetry Collector

# Ingest Zipkin data with the OpenTelemetry Collector

* Latest Dynatrace
* How-to guide
* 2-min read
* Published Oct 11, 2023

The following configuration example shows how you configure a Collector instance to accept Zipkin data, transform it to OTLP, and send it to the Dynatrace backend.

## Limitations

### B3 requirements

Pay attention to the B3 requirements, to avoid having spans being dropped because of shared and duplicated span identifiers. See the [propagator specificationï»¿](https://opentelemetry.io/docs/specs/otel/context/api-propagators/#b3-requirements) for more details.

For example, if you are using [Spring Code Sleuthï»¿](https://cloud.spring.io/spring-cloud-sleuth/2.1.x/multi/multi__propagation.html#_extracting_a_propagated_context), you can use the following configuration setting to disable span sharing:

```
spring:



sleuth:



supports-join: false
```

### Single Collector routing

Make sure to route all related Zipkin/B3 spans via the same Collector instance, to guarantee full ingestion. If you ingest some spans using OneAgent alone, they may not be properly linked and not show up as connected to your Zipkin spans.

## Prerequisites

* One of the following Collector distributions with the [Zipkin receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver):

  + The [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector#dt-collector-dist "Learn about the Dynatrace OTel Collector.")
  + OpenTelemetry [Contrib](/docs/ingest-from/opentelemetry/collector#collector-contrib "Learn about the Dynatrace OTel Collector.")
  + A [custom Builder version](/docs/ingest-from/opentelemetry/collector#collector-builder "Learn about the Dynatrace OTel Collector.")
* The [Dynatrace API endpoint URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") to which the data should be exported
* An [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the relevant access scope (only required for SaaS and ActiveGate)

See [Collector Deployment](/docs/ingest-from/opentelemetry/collector/deployment "How to deploy Dynatrace OTel Collector.") and [Collector Configuration](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.") on how to set up your Collector with the configuration below.

## Demo configuration

```
receivers:



zipkin:



exporters:



otlp_http:



endpoint: ${env:DT_ENDPOINT}



headers:



Authorization: "Api-Token ${env:DT_API_TOKEN}"



service:



pipelines:



traces:



receivers: [zipkin]



processors: []



exporters: [otlp_http]
```

Configuration validation

[Validate your settings](/docs/ingest-from/opentelemetry/collector/configuration#validate "How to configure the OpenTelemetry Collector.") to avoid any configuration issues.

## Components

For our configuration, we configure the following components.

### Receivers

Under `receivers`, we specify the `zipkin` receiver as active receiver component for our Collector instance.

The Zipkin receiver can be customized with [a few more attributesï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib/tree/v0.145.0/receiver/zipkinreceiver), which we leave with their default values in our example.

### Exporters

Under `exporters`, we specify the default [`otlp_http` exporterï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/exporter/otlphttpexporter) and configure it with our Dynatrace API URL and the required authentication token.

For this purpose, we set the following two environment variables and reference them in the configuration values for `endpoint` and `Authorization`.

* `DT_ENDPOINT` contains the [base URL of the Dynatrace API endpoint](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") (for example, `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`)
* `DT_API_TOKEN` contains the [API token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Service pipelines

Under `service`, we eventually assemble our receiver and exporter objects into a traces pipeline, which will handle our Zipkin transformation to OTLP.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Enrich OTLP requests with Kubernetes data](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")


---


## Source: use-cases.md


---
title: OpenTelemetry Collector use cases
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/use-cases
scraped: 2026-02-17T21:33:50.530532
---

# OpenTelemetry Collector use cases

# OpenTelemetry Collector use cases

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Dec 09, 2025

## Recommended configurations

When using the Collector, we recommend using the following features in the basic configuration, in addition to components specific to your use case.

* [Batching](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")âto improve network performance and throughput
* [Memory Limitation](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")âto avoid memory allocation related issues
* [Kubernetes Enrichment](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.")âto include Kubernetes-specific information in your requests and support data correlation in the Dynatrace backend

## Use cases

[### Batching

Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.](/docs/ingest-from/opentelemetry/collector/use-cases/batch "Configure the OpenTelemetry Collector to send data in batches to the Dynatrace backend.")[### Enrich with OneAgent

Configure the OpenTelemetry Collector to enrich data with OneAgent.](/docs/ingest-from/opentelemetry/collector/use-cases/enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with OneAgent host data.")[![FluentD](https://dt-cdn.net/images/untitled-300-c72685245e.png "FluentD")

### FluentD

Configure the OpenTelemetry Collector to ingest data from FluentD.](/docs/ingest-from/opentelemetry/collector/use-cases/fluentd "Configure the OpenTelemetry Collector to ingest FluentD data.")[### gRPC to HTTP

Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.")[### Histogram summaries

Configure the OpenTelemetry Collector to compute bucket summaries for histogram metrics.](/docs/ingest-from/opentelemetry/collector/use-cases/histograms "Configure the OpenTelemetry Collector to compute histogram summaries.")[![Jaeger](https://dt-cdn.net/images/jaeger-300-3d21c8cbd4-300-2d7104a994.png "Jaeger")

### Jaeger

Configure the OpenTelemetry Collector to ingest and transform Jaeger data into Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/jaeger "Configure the OpenTelemetry Collector to ingest and convert Jaeger data into Dynatrace.")[### Kafka

Configure the OpenTelemetry Collector to integrate with Apache Kafka.](/docs/ingest-from/opentelemetry/collector/use-cases/kafka "How to configure the OpenTelemetry Collector to buffer data via Kafka.")[### Kubernetes Enrichment

Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes "Configure the OpenTelemetry Collector to ingest Kubernetes data into Dynatrace.")[### Log files

Configure the OpenTelemetry Collector to ingest log files.](/docs/ingest-from/opentelemetry/collector/use-cases/filelog "Configure the OpenTelemetry Collector to ingest log data into Dynatrace.")[### Mask sensitive data

Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")[### Memory Limitation

Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.](/docs/ingest-from/opentelemetry/collector/use-cases/memory "Configure the OpenTelemetry Collector to respect memory limits and not use excessive system resources.")[### Multiple backends

Configure the OpenTelemetry Collector to export to multiple backends.](/docs/ingest-from/opentelemetry/collector/use-cases/multi-export "Configure the OpenTelemetry Collector to send data to more than one backend.")[### NetFlow

Configure the OpenTelemetry Collector to ingest NetFlow packets.](/docs/ingest-from/opentelemetry/collector/use-cases/netflow "Configure the OpenTelemetry Collector to ingest NetFlow data.")[![Prometheus](https://dt-cdn.net/images/prometheus-logo-grey-e85840f462-8e7b2967a6.svg "Prometheus")

### Prometheus

Configure the OpenTelemetry Collector to scrape your Prometheus data.](/docs/ingest-from/opentelemetry/collector/use-cases/prometheus "Configure the OpenTelemetry Collector to scrape your Prometheus data.")[### Sampling

Configure the OpenTelemetry Collector to sample distributed traces.](/docs/ingest-from/opentelemetry/collector/use-cases/sampling "Configure the OpenTelemetry Collector to sample data using the `tail_sampling` processor.")[### StatsD

Configure the OpenTelemetry Collector to ingest StatsD data.](/docs/ingest-from/opentelemetry/collector/use-cases/statsd "Configure the OpenTelemetry Collector to ingest StatsD data.")[### Syslog

Configure the OpenTelemetry Collector to ingest syslog data.](/docs/ingest-from/opentelemetry/collector/use-cases/syslog "Configure the OpenTelemetry Collector to ingest syslog data into Dynatrace.")[### Transforming and filtering

Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.](/docs/ingest-from/opentelemetry/collector/use-cases/transform "Configure the OpenTelemetry Collector to add, transform, and drop OpenTelemetry data.")[![Zipkin](https://dt-cdn.net/images/zipkin-gray-300-7e572e6589.png "Zipkin")

### Zipkin

Configure the OpenTelemetry Collector to ingest and transform Zipkin data into Dynatrace.](/docs/ingest-from/opentelemetry/collector/use-cases/zipkin "Configure the OpenTelemetry Collector to ingest and convert Zipkin data into Dynatrace.")


---


## Source: collector.md


---
title: Dynatrace OTel Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector
scraped: 2026-02-17T21:24:32.016989
---

# Dynatrace OTel Collector

# Dynatrace OTel Collector

* Latest Dynatrace
* Overview
* 5-min read
* Updated on Nov 17, 2025

The Collector is a network service application that you can use to batch and transform telemetry data. It acts as a proxy and can receive OTLP requests as well as data from other sources, transform these requests according to defined rules, and forward them to the backend.

![OpenTelemetry Collector Overview](https://dt-cdn.net/images/collector-1062-e6ec25a6ee.png)

## Advantages of using the Collector

In general, using the Collector alongside your service can be an advantage, since it allows your service to offload data quickly and takes care of additional handling such as retries, batching, encryption, or sensitive data filtering. It centralizes common processing tasks instead of duplicating them in each application.

You should use the Collector if:

* You need to collect data from different data sources in different formats and you need an easy way to make them all deliver their data to a backend that would otherwise be incompatible.
* You need to have common processing of attributes on your telemetry data.

The Collector is a relatively lightweight component, so teams can deploy their own to avoid sharing the same configuration.

The Collector is configured in a single YAML file. This eliminates the need to browse through multiple files and reduces maintenance. You can find more information on the configuration at [Configure the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/configuration "How to configure the OpenTelemetry Collector.").

## Distributions

The Collector comes in different distribution flavors and with different setup and deployment options.

### Dynatrace Collector

The Dynatrace distribution of the OpenTelemetry Collector is a customized Collector build provided by Dynatrace and tailored for typical use cases in a Dynatrace context. It ships with an optimized and verified set of Collector components.

Advantages of Dynatrace Collector

The Dynatrace Collector offers the following advantages compared to the OpenTelemetry Collector distributions:

* Covered by Dynatrace support (x86-64 and ARM64)
* Collector components verified by Dynatrace
* Security patches independent of OpenTelemetry Collector releases

You can download the Dynatrace Collector release from [our repositoryï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/releases/v0.44.0).

It is also available as a container image at [Github Packagesï»¿](https://github.com/Dynatrace/dynatrace-otel-collector/pkgs/container/dynatrace-otel-collector%2Fdynatrace-otel-collector) and can be pulled using the following Docker command:

```
docker pull ghcr.io/dynatrace/dynatrace-otel-collector/dynatrace-otel-collector:0.44.0
```

More information about further available container repositories can be found under [Deploy Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector/deployment#container-image-registries "How to deploy Dynatrace OTel Collector.").

Dynatrace Collector ships with specific components as described in the Dynatrace Collector's GitHub repo.
For the full list, see [Componentsï»¿](https://github.com/Dynatrace/dynatrace-otel-collector#components).

Take a look at [OpenTelemetry Collector use cases](/docs/ingest-from/opentelemetry/collector/use-cases "Configure your Collector instance for different use cases.") for concrete use-case and configuration examples for the individual components.

### OpenTelemetry Distributions

There are two principal OpenTelemetry distributions of the Collector:

* **Collector Core**
* **Collector Contrib**

Additionally, OpenTelemetry also provides the **Collector Builder**, which allows you to build your own, customized Collector binary.

Dynatrace support

Dynatrace only provides limited support for Core, Contrib, and Builder setups, covering only the components and their versions included in the Dynatrace Collector.

For a fully supported Collector distribution, see [Dynatrace Collector](#dt-collector-dist).

#### Collector Core

The [Core distributionï»¿](https://github.com/open-telemetry/opentelemetry-collector) contains the basic proxy service and a few fundamental service components:

* A receiver for OTLP over HTTP and gRPC
* Processors for batching requests and ensuring memory usage constraints
* Exporters for console logging and OTLP over HTTP and gRPC

#### Collector Contrib

The [Contrib distributionï»¿](https://github.com/open-telemetry/opentelemetry-collector-contrib) builds on top of Core and enhances its functionality by shipping with a large number of additional receivers, processors, and exporters, contributed by third parties.

Given that the Contrib distribution is an all-in-one package and comes with all service components pre-compiled, it may use more system resources (storage and memory) than an optimized Collector build. Generally, we recommend using the Contrib distribution for testing purposes and a custom build of the Collector (see [Builder](#collector-builder)) in production.

#### Collector Builder (ocb)

In addition to the two distributions, OpenTelemetry also offers the [Collector Builderï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/cmd/builder), a command line tool that allows you to build your own customized version of the Collector.

### Which distribution should I use?

| Type | When should I use it? |
| --- | --- |
| Dynatrace Collector Recommended | The preferred choice for most use cases. It ships with a set of verified and stable Collector components, typically used with Dynatrace setups. |
| Custom Builder version | When you need to fully customize the Collector instance and only run the components required for your use case. |
| Core | When you primarily want to convert between OTLP protocols (HTTP â gRPC), ensure memory usage constraints, or apply request batching. |
| Contrib | Ideal for test setups, as it contains all third-party components and doesn't require a custom build. It's generally not recommended for use in production systems, as it typically uses more resources and may be less stable than an optimized Builder instance. |

## Components

### Receiver

A receiver is a component that enables data to come into the Collector. It can receive data from multiple sources. Many receivers come with default settings and do not need much configuration.

For a list of available receivers and their basic configuration, see the official [OpenTelemetry documentation on receiversï»¿](https://opentelemetry.io/docs/collector/configuration/#receivers).

### Processor Optional

A processor is an optional component that decides what to do with the data.

For a list of available processors and their basic configuration, see the official [OpenTelemetry documentation on processorsï»¿](https://opentelemetry.io/docs/collector/configuration/#processors). OpenTelemetry has a list of [recommended processorsï»¿](https://github.com/open-telemetry/opentelemetry-collector/tree/v0.145.0/processor#recommended-processors), but these are optional.

### Exporter

An exporter is a component that sends processed data to one or more backends. Exporters can support more than one data source.

Because many exporters require additional configuration (for example, an endpoint), be sure to check the official [OpenTelemetry documentation on exportersï»¿](https://opentelemetry.io/docs/collector/configuration/#exporters) for a list of available exporters and their configurations.

### Services

Services are used to define pipelines that channel data through the Collector. They define which components work together to process OpenTelemetry data.


---


## Source: getting-started.md


---
title: Get started with OpenTelemetry and Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/getting-started
scraped: 2026-02-17T21:15:34.514463
---

# Get started with OpenTelemetry and Dynatrace

# Get started with OpenTelemetry and Dynatrace

* Latest Dynatrace
* Overview
* 3-min read
* Updated on Oct 15, 2025

Find the information that you need to get started with ingesting OpenTelemetry logs, metrics, and traces into Dynatrace.

[### OTLP APIs

The Dynatrace OTLP API endpoints and token scopes needed to configure telemetry exports to Dynatrace.](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")[### Instrument your apps

Instrument your apps to send OpenTelemetry data to Dynatrace API endpoints.](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")[### Dynatrace Collector

The customized Collector build, provided by Dynatrace and tailored for typical use cases in a Dynatrace context.](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.")[### Istio and Envoy

Configure Istio and Envoy for OpenTelemetry exports to Dynatrace.](/docs/ingest-from/opentelemetry/integrations "Learn how to integrate OpenTelemetry and Dynatrace with Istio and Envoy.")[### Ensuring success

Make sure you get the OpenTelemetry data that you need in Dynatrace.](/docs/ingest-from/opentelemetry/troubleshooting "Troubleshoot common issues in the context of OpenTelemetry and data ingestion.")[### Licensing

How to calculate DPS consumption related to OpenTelemetry.](/docs/ingest-from/opentelemetry/opentelemetry-licensing "Learn how Dynatrace calculates licensing for data ingested via OpenTelemetry, using the Dynatrace Platform Subscription (DPS) model.")


---


## Source: envoy.md


---
title: Configure OpenTelemetry tracing with Envoy
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations/envoy
scraped: 2026-02-17T21:19:46.243131
---

# Configure OpenTelemetry tracing with Envoy

# Configure OpenTelemetry tracing with Envoy

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Oct 15, 2025

Support statement

This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.

Always use the most recent release version to ensure you have the latest patches and fixes deployed.

This page describes how to configure your Envoy version 1.29+ instance to export traces to Dynatrace.

If you're using Envoy versions 1.28 and earlier, you can still export traces to Dynatrace via the OneAgent Envoy code module.

### Prerequisites

* The [OTLP traces URL](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") for the export.
* The OneAgent Envoy code module is disabled.
  To do this:

  1. Go to the applicable configuration page:

     + For the entire environment, go to **Settings** > **Monitoring** > **Monitored technologies**.
     + For a particular host, go to **Your host** > **Host settings** > **General**.
  2. Find **Envoy** in the list of monitored technologies and select  **Edit**.
  3. Select the **Monitor Envoy** toggle, as appropriate, to disable the OneAgent Envoy code module.

### Steps

1. Get configuration entries

1. In Dynatrace Hub, search for `Envoy`.
2. Select the Hub entry for Envoy.
3. Select **Set up**.
4. Configure the API token.
5. Proceed with the following steps and use (and adjust) the two provided configuration snippets where applicable.

2. Add Dynatrace cluster entry for OpenTelemetry export

For Envoy to send traces to Dynatrace, you first need to configure a [clusterï»¿](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/intro/terminology) entry for Dynatrace in the Envoy configuration file. For that, add the [cluster configuration entry as obtained in step 2](#snippets) under the top-level `clusters` key.

3. Dynatrace-specific configuration for the OpenTelemetry tracer

Next, you need to add the tracing provider to the [HTTP connection manager filterï»¿](https://www.envoyproxy.io/docs/envoy/latest/intro/arch_overview/http/http_connection_management#http-connection-management) in the [Envoy configuration fileï»¿](https://www.envoyproxy.io/docs/envoy/latest/start/quick-start/configuration-static#listeners).

Envoy 1.30+

Envoy 1.29

Use the [tracer configuration entry you obtained in step 2](#snippets), configure the [API token](#prerequisites) under `tracing` - `provider` - `typed_config` - `http_service` - `request_headers_to_add` - `header` - `value` (the correct syntax is `value: "Api-Token YOUR_API_TOKEN_HERE"`), and add the tracer configuration under aforementioned `filters` entry.

Configure the following snippet under `filters`.

```
tracing:



provider:



name: envoy.tracers.opentelemetry



typed_config:



"@type": type.googleapis.com/envoy.config.trace.v3.OpenTelemetryConfig



service_name: your-service-name



http_service:



http_uri:



uri: "{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces"



cluster: dynatrace



timeout: 10s



request_headers_to_add:



- header:



key: "Authorization"



value: "Api-Token {API_TOKEN_HERE}"



resource_detectors:



- name: envoy.tracers.opentelemetry.resource_detectors.dynatrace



typed_config:



"@type": type.googleapis.com/envoy.extensions.tracers.opentelemetry.resource_detectors.v3.DynatraceResourceDetectorConfig
```

These values need to be adjusted to reflect your Dynatrace environment and the export configuration:

* `uri`âSpecifies the desired [export URL with the trace path](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The value must not include the protocol scheme but start with hostname instead.
* `cluster`âSpecifies the cluster name and has to match the value of `cluster_name` of the previous cluster definition.
* `request_headers_to_add`âContains the HTTP headers to be included in the request. Necessary when exporting to ActiveGate (configured for the [API token](#prerequisites)).

4. Verify the setup

Once the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.

![trace](https://dt-cdn.net/images/screenshot-1863-979a8a5284.png)

## Related topics

* [Prometheus](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus "Learn how to extend observability in Dynatrace with Prometheus metrics.")
* [Istio/Envoy proxy metrics](/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-istio-metrics "Istio metric ingestion and topology detection")


---


## Source: istio.md


---
title: Configure OpenTelemetry tracing with Istio
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations/istio
scraped: 2026-02-17T05:05:47.206005
---

# Configure OpenTelemetry tracing with Istio

# Configure OpenTelemetry tracing with Istio

* Latest Dynatrace
* How-to guide
* 3-min read
* Updated on Oct 22, 2025

Support statement

This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.

Always use the most recent release version to ensure you have the latest patches and fixes deployed.

This page describes how to use Istio version 1.22+ with the [Istio OpenTelemetry extension providerï»¿](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider), and how to configure it to export OpenTelemetry traces to Dynatrace.

### System requirements

The following prerequisites are necessary to configure Istio OpenTelemetry trace configuration, including Dynatrace resource detection and sampling:

* Istio version 1.22+ (i.e., Istio releases that ship with Envoy 1.30+)

Istio version 1.21 and earlier

Istio versions 1.21 and earlier ship with Envoy versions 1.29 and earlier, which is based on OpenTracing.
To use these Isito releases, enable the Dynatrace Envoy code module as described in [Configure OpenTelemetry tracing with Envoy](/docs/ingest-from/opentelemetry/integrations/envoy#envoy-code-module "Learn how to configure Envoy to send OpenTelemetry traces to Dynatrace.").

## Licensing impact

In certain deployment setups, tracing with Istio version 1.22+ results in consumption of the following [rate cardï»¿](https://www.dynatrace.com/pricing/) capabilities:

* When using the Dynatrace resource detector and sampler:

  + Classic Full-Stack or cloud-native Full-Stack deployments: Usage is included in [Full-Stack Monitoring (DPS)](/docs/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") and [Host Units (Dynatrace Classic License)](/docs/license/monitoring-consumption-classic/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").
  + For Application-Observability-only deployments: Usage incurs consumption of [Custom Traces Classic (DPS)](/docs/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.") or [DDUs for custom traces (Dynatrace Classic License)](/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces "Understand how DDU consumption is calculated for spans ingested via the Trace API.").
* Without the Dynatrace resource detector and sampler: Usage incurs consumption of [Custom Traces Classic (DPS)](/docs/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.") or [DDUs for custom traces (Dynatrace Classic License)](/docs/license/monitoring-consumption-classic/davis-data-units/custom-traces "Understand how DDU consumption is calculated for spans ingested via the Trace API.").

## Deployment considerations

It's possible to configure Istio OpenTelemetry tracing in a standalone deployment or in combination with Dynatrace Operator.

### Deployment in combination with Dynatrace Operator Recommended

We recommend using the Istio OpenTelemetry integration in combination with a Dynatrace Operator deployment with [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") and [telemetry ingest endpoints](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") enabled. Other features like OneAgent or ActiveGate are not required.

This provides the following benefits compared to standalone usage:

* Resilient and more efficient delivery of traces by providing retry and batching capabilities.
* Optional routing through ActiveGate.
* No additional access token required.
* No additional `ServiceEntries` required.
* Compatibility with Dynatrace Operator `enableIstio`.

### Standalone deployment

It's possible to ingest Istio traces without a Dynatrace Operator instance deployed, but this comes with major downsides and should only be used if it's not possible to deploy Dynatrace Operator.

Caveats when using standalone deployment:

* No Kubernetes metadata will be available for traces. This means traces will not be automatically correlated with Kubernetes workloads or services in Dynatrace.
* Potentially unreliable delivery of traces. The current implementation of the OTLP HTTP exporter in Envoy doesn't provide any means of retry or error handling in case of connectivity or other issues when sending traces to Dynatrace, which can lead to loss of traces.
* The required `ServiceEntry` is not compatible with the `enableIstio` option of Dynatrace Operator.

### Other deployment considerations

Istio ambient mode

#### Istio ambient mode support

Istio in ambient mode doesn't rely on Envoy proxies to route traffic, so tracing Istio traffic using the OpenTelemetry integration is not possible. If waypoint proxies are used, those would still emit traces, but the metadata would be misleading or wrong. Currently, there is no solution for end-to-end tracing in Istio ambient mode.

## Steps

### 1. Requirements

Check the following requirements before starting to deploy tracing for Istio.

Dynatrace Operator

Standalone

1. Dynatrace Operator is [deployed](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").

   * For optimal configuration, follow the guide for [deployment alongside Istio](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/istio-deployment "Deployment of Dynatrace Operator alongside Istio in various scenarios").
2. [Telemetry ingest](/docs/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") endpoints are enabled.

Either Dynatrace Operator is not deployed, or `enableIstio` is set to `false` in the DynaKube.

### 2. Get configuration entries

Dynatrace Operator

Standalone

1. In Dynatrace Hub, search for `Istio`.
2. Filter by the category **Technology**.
3. Select the Hub entry **Istio Service Mesh**.
4. Select **Set up**.
5. Use the provided and pre-configured snippets to deploy the following items in the next steps:

   * Mesh configuration
   * Telemetry API

1. In Dynatrace Hub, search for `Istio`.
2. Filter by the category **Technology**.
3. Select the Hub entry **Istio Service Mesh**.
4. Select **Set up**.
5. Configure the API token.
6. Use the provided and pre-configured snippets to deploy the following items in the next steps:

   * Mesh configuration
   * Service entry
   * Telemetry API

### 3. Apply the mesh configuration to your Istio installation

Dynatrace Operator

Standalone

To use the telemetry ingest endpoints provided by the Dynatrace OpenTelemetry collector, we need to change the snippet obtained in step 2 by removing the API token header and changing the target service.

The resulting configuration should look like this, assuming the default ingest service name:

```
apiVersion: install.istio.io/v1alpha1



kind: IstioOperator



spec:



meshConfig:



extensionProviders:



- name: dynatrace-otel



opentelemetry:



port: 4318



service: "<dynakube-name>-telemetry-ingest.<dynatrace-operator-namespace>.svc.cluster.local" # <-- Please fill in your ingest endpoint service



http:



path: "/v1/traces"



timeout: 10s



resource_detectors:



dynatrace: {}



dynatrace_sampler:



tenant: "<your-tenant-id>"  # <-- This must not be changed from step 2



cluster_id: <cluster-id>    # <-- This must not be changed from step 2
```

Save the file as `meshconfig.yaml` and apply the configuration using the following command.

```
istioctl install -f meshconfig.yaml
```

Save the mesh configuration snippet you obtained in step 2 under `meshconfig.yaml` and configure Istio with the following command:

```
istioctl install -f meshconfig.yaml
```

Existing Mesh configuration

If you already use your own, custom Mesh configuration, you need to merge its content with the provided snippet. Otherwise, you can use the snippet as-is.

### 4. Deploy the service entry

Dynatrace Operator

Standalone

This step is only required for standalone deployment.
No action required when using Dynatrace Operator.

Next, you need to deploy the [Istio service entryï»¿](https://istio.io/latest/docs/reference/config/networking/service-entry/) manifest you obtained in step 1 using `kubectl`. Save it to `dt-serviceentry.yaml` and run the following command:

```
kubectl apply -n istio-system -f dt-serviceentry.yaml
```

### 5. Enable tracing provider

As last configuration step, use the Istio telemetry API to enable the tracing provider.

Save the telemetry API manifest you obtained in step 2 to `dt-telemetry.yaml` and use `kubectl` to apply the configuration to the desired namespace.

```
kubectl apply -n istio-system -f dt-telemetry.yaml
```

Multiple telemetry resources

Do not deploy more than one telemetry resource within a given namespace, as doing so may lead to configuration conflicts and incomplete tracing information.

If you require different telemetry resources, deploy them to different namespaces or using different selectors.

Pod restart

Make sure to restart all applicable Kubernetes pods, to let the changes to the mesh configuration take effect.

### 6. Verify the setup

Once the setup is complete and you have ingested your first data, you can verify if the traces show up in Dynatrace.

![trace](https://dt-cdn.net/images/istio-otel-tracing-2513-5da62a325b.png)


---


## Source: integrations.md


---
title: Integrate with Istio and Envoy
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations
scraped: 2026-02-17T21:24:34.331119
---

# Integrate with Istio and Envoy

# Integrate with Istio and Envoy

* Latest Dynatrace
* Overview
* 1-min read
* Updated on Oct 15, 2025

This page provides information on how to configure Istio and Envoy to export OpenTelemetry data to Dynatrace.

[### Istio](/docs/ingest-from/opentelemetry/integrations/istio "Learn how to configure Istio on Kubernetes to deploy pre-configured proxy services for OpenTelemetry tracing.")[### Envoy](/docs/ingest-from/opentelemetry/integrations/envoy "Learn how to configure Envoy to send OpenTelemetry traces to Dynatrace.")


---


## Source: opentelemetry-licensing.md


---
title: OpenTelemetry licensing
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/opentelemetry-licensing
scraped: 2026-02-17T21:24:29.628967
---

# OpenTelemetry licensing

# OpenTelemetry licensing

* Latest Dynatrace
* Overview
* 2-min read
* Published Aug 25, 2025

Latest Dynatrace

Learn how OpenTelemetry data ingest is calculated with the Dynatrace Platform Subscription (DPS) license model.

## Overview

Dynatrace provides seamless support for OpenTelemetry data ingestion and processing.
This lets you leverage the power of observability across your distributed systems.

Licensing for OpenTelemetry data is fully integrated into the Dynatrace Platform Subscription model, ensuring that all telemetry types (traces and spans, metrics, and logs) are billed transparently and consistently.

With Dynatrace, OpenTelemetry data is treated like any other ingested data.
Flexible pricing is based on the volume of data ingested, stored, and queried.
Pricing calculations use the same [rate card itemsï»¿](https://www.dynatrace.com/pricing/) as for all telemetry data that is ingested into the platform.

## Traces powered by Grail (DPS)

Dynatrace allows you to ingest and analyze OpenTelemetry trace data seamlessly.

For complete information, see [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### Ingestion

OpenTelemetry trace data is billed by the ingested volume.
It is charged as [Traces â Ingest & Process](/docs/license/capabilities/traces/dps-traces-ingest "Learn how your consumption of the Traces - Ingest & Process DPS capability is billed and charged.").

Full-Stack Monitoring includes a [defined amount of trace data volume](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-traces "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") for traces that are sent via the OneAgent Trace API or from a Full-Stack monitored host.
You are only charged for trace data (from these sources) that exceeds the included volume.

### Retention

Retention of OpenTelemetry trace data is billed based on the volume of trace data stored.
It is measured in gibibytes per day (GiB-day) and charged as [Traces â Retain](/docs/license/capabilities/traces/dps-traces-retain "Learn how your consumption of the Traces - Retain DPS capability is billed and charged.").

The default [trace data retention period of 10 days](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods#purepath "Check retention times for various data types.") is included.
Any trace data retained longer than 10 days is charged on a per-gibibyte basis as [Traces - Retain](/docs/license/capabilities/traces#trace-retain-usage "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.").

### Query

Querying of OpenTelmetry traces is billed based on gibibytes scanned (GiB-scanned) and charged as [Traces â Query](/docs/license/capabilities/traces/dps-traces-query "Learn how your consumption of the Traces - Query DPS capability is billed and charged.").

The use of [![Distributed Tracing](https://dt-cdn.net/images/distributed-tracing-4ed13d1274.svg "Distributed Tracing") **Distributed Tracing**](/docs/observe/application-observability/distributed-tracing "Trace and analyze in real time highly distributed systems with Grail.") and [![Services](https://dt-cdn.net/hub/logos/services.png "Services") **Services**](/docs/observe/application-observability/services/services-app "Maintain centralized control over service health, performance, and resources with the Services app.") is included with Dynatrace.
No query consumption is generated by these apps.

## Metrics powered by Grail (DPS)

Dynatrace supports OpenTelemetry metrics, allowing you to seamlessly ingest and analyze OpenTelemetry data alongside metrics from Dynatrace-monitored environments.
OpenTelemetry metrics are billed as Metrics powered by Grail, just like other ingested metrics.

For complete information, see [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.").

### Ingestion

OpenTelemetry metrics are billed by the number of metric data points ingested, measured as groups of 100,000 data points.
This ingest is charged as [Metrics â Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.").

Metrics originating from Full-Stack-monitored hosts or containers [include a defined amount of metric data points](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#dps-included-metrics "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.").
Each contributing GiB of host or application memory adds 900 data points in each 15-minute interval.

In an environment with Full-Stack Monitoring, you are only charged for metric data points that exceed this limit.

### Retention

Retention of OpenTelemetry metrics is billed based on the volume of metric data stored.
It is measured in gibibytes per day (GiB-day) and charged as [Metrics â Retain](/docs/license/capabilities/metrics/dps-metrics-retain "Learn how your consumption of the Metrics - Retain DPS capability is billed and charged.").

Metrics powered by Grail includes [15 months (462 days) of one-minute granularity](/docs/manage/data-privacy-and-security/data-privacy/data-retention-periods "Check retention times for various data types.").
Metrics that you choose to retain beyond that period are charged.

### Query

Querying metric data is included in [Metrics â Ingest & Process](/docs/license/capabilities/metrics/dps-metrics-ingest "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.").

## Logs powered by Grail (DPS)

Dynatrace provides full support for OpenTelemetry logs.
This enables you to centralize log data from OpenTelemetry sources alongside logs from Dynatrace-monitored environments. OpenTelemetry logs are billed as Logs powered by Grail.

For complete information, see [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.").

### Ingestion

OpenTelemetry log data is billed by the volume ingested.
It is measured in gibibytes (GiB) and charged as [Log Management & Analytics â Ingest & Process](/docs/license/capabilities/log-analytics/dps-log-ingest "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.").

### Retention

Retention of log data is billed based on the volume of log data stored.
It is measured in gibibytes per day (GiB-day) and charged as [Log Management & Analytics â Retain](/docs/license/capabilities/log-analytics/dps-log-retain "Learn how your consumption of the Log Management & Analytics - Retain DPS capability is billed and charged.").

### Query

Querying log data is billed based on the volume of log data queried.
It is measured in gibibytes scanned (GiB-scanned) and charged as [Log Management & Analytics - Query](/docs/license/capabilities/log-analytics/dps-log-query "Learn how your consumption of the Log Management & Analytics - Query DPS capability is billed and charged.").

## Track your consumption

Dynatrace provides different ways to track your OpenTelmetry ingest.
These are described on the respective DPS capability page:

* [Pre-made notebooks to track your trace ingest](/docs/license/capabilities/traces/dps-traces-ingest#consumption-trace-ingest "Learn how your consumption of the Traces - Ingest & Process DPS capability is billed and charged.")
* [Built-in metrics to track your log ingest](/docs/license/capabilities/log-analytics/dps-log-ingest#track-your-consumption "Learn how your consumption of the Log Management & Analytics - Ingest & Process DPS capability is billed and charged.")
* [Calculations to track your metrics ingest](/docs/license/capabilities/metrics/dps-metrics-ingest#calculate-your-consumption "Learn how your consumption of the Metrics - Ingest & Process DPS capability is billed and charged.")

## Related topics

* [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.")
* [Log Analytics (DPS)](/docs/license/capabilities/log-analytics "Learn how Dynatrace Log Analytics consumption is calculated using the Dynatrace Platform Subscription model.")
* [Traces powered by Grail overview (DPS)](/docs/license/capabilities/traces "Learn how Dynatrace Traces powered by Grail consumption is calculated using the Dynatrace Platform Subscription (DPS) model.")
* [Metrics powered by Grail overview (DPS)](/docs/license/capabilities/metrics "Learn how Dynatrace Metrics powered by Grail consumption is calculated using the Dynatrace Platform Subscription model.")


---


## Source: opentelemetry-security-context.md


---
title: Set up Grail permissions for OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/opentelemetry-security-context
scraped: 2026-02-17T21:24:50.107399
---

# Set up Grail permissions for OpenTelemetry

# Set up Grail permissions for OpenTelemetry

* Latest Dynatrace
* How-to guide
* 2-min read
* Updated on Nov 20, 2025

Dynatrace has a [permission model for Grail](/docs/platform/grail/organize-data/assign-permissions-in-grail "Find out how to assign permissions to buckets and tables in Grail."). This applies to all telemetry data, such as metrics, events, spans, and logs.

We recommend setting up permissions along organizational lines and deployment scopes. Suitable concepts include host groups, Kubernetes clusters, and Kubernetes namespaces. These attributes are typically available for all telemetry data ingested via Dynatrace collection methods like OneAgent, OpenTelemetry, or Kubernetes operator. Hence, you can use these attributes to enable [record-level permissions](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.").

For Kubernetes-based deployments, make sure Dynatrace Operator has [metadata enrichment](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Metadata enrichment in the Dynatrace Operator adds context to Kubernetes pods by attaching relevant metadata to entities like pods, hosts, and processes for better observability.") enabled.

If you only require a basic permission concept, setting up bucket-level permissions is the best option. You can then route your data to the correct bucket in OpenPipeline by matching one of the mentioned deployment-relevant primary Grail fields.

For more control in Dynatrace, you can set up policy boundaries with more granular restrictions on a data level. By default, you can use the following attributes:

* `dt.host_group.id`
* `k8s.cluster.name`
* `k8s.namespace.name`
* Any other attribute listed in the [permission model](/docs/platform/grail/organize-data/assign-permissions-in-grail#grail-permissions-table-record "Find out how to assign permissions to buckets and tables in Grail.")

Dynatrace provides a comprehensive permission model for Grail that applies to all telemetry data-including metrics, logs, spans, and events.

## Set up security context

If the permissions on deployment-level attributes or the bucket level are insufficient, Dynatrace allows you to set up fine-grained permissions by adding a `dt.security_context` attribute to your data. This context can represent your security architecture and could even be hierarchical by encoding this into a string such as `department-A/department-AB/team-C`.

To use `dt.security_context` and other attributes for permissions, make sure these attributes are present in your telemetry data.

To add the security context to your OpenTelemetry data, enrich your signals with the `dt.security_context` attribute. Dynatrace automatically propagates the `dt.security_context` value from spans to the service entity for span data.

You can use your existing labels and tags to facilitate permissions in Dynatrace.

### Security context via Kubernetes labels or annotations

You can use [Kubernetes labels or annotations](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment "Guides for telemetry enrichment on Kubernetes") as a source for your `dt.security_context`. This is one of the most convenient ways of doing this.

Alternatively, you can [configure the OpenTelemetry Collector to enrich data in transit](/docs/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data."). If you do this, you might have to map your Kubernetes metadata to `dt.security_context` in OpenPipeline.

### Security context via OpenTelemetry resource attributes

To use the [`OTEL_RESOURCE_ATTRIBUTES`](/docs/deliver/release-monitoring/version-detection-strategies#otel_resource_attributes "Metadata for version detection in different technologies") environment variable, just directly set the `dt.security_context` as a resource attribute. You can also use any resource attribute in OpenPipeline as a source for your `dt.security_context`.

### Security context via OneAgent metadata file

Dynatrace OneAgent provides enrichment files or environment variables to [add attributes directly in your application code](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

To read more about enrichment options and setup, see how to [enrich via environment variable](/docs/ingest-from/setup-on-k8s/guides/metadata-automation/k8s-metadata-telemetry-enrichment#expand--enrich-via-environment-variable--4 "Guides for telemetry enrichment on Kubernetes").


---


## Source: ingest-logs.md


---
title: Ingest OTLP logs
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-logs
scraped: 2026-02-17T21:30:18.207631
---

# Ingest OTLP logs

# Ingest OTLP logs

* Latest Dynatrace
* Reference
* 3-min read
* Updated on Feb 10, 2026

OpenTelemetry supports attributes at different levels in an OpenTelemetry log request, such as the resource level, scope level, and record level.

The Log ingestion API collects and attempts to automatically transform log data.

## Data transformation

Each log record from the ingested batch is mapped to a single Dynatrace log record, which contains three special attributes: `timestamp`, `loglevel`, `content`, and a set of other key-value attributes. These properties are set based on keys present in the input object as follows.

### Timestamp

* Set based on the **Timestamp** field of the input log record. See the differences between data models in the [Log ingestion API processing](#otlp-structured-logs) section below for more details.
* Log events older than the **Log Age** limit are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time. See the [Ingestion limits](#ingestion-limits) section for details.
* The default value is the current timestamp.

### Log level

* Set based on the **SeverityText** field (first priority) or **SeverityNumber** field (secondnd priority) of the input log record. See the differences between data models in the section [Log ingestion API processing](#otlp-structured-logs) below for more details.
* The default value is `NONE`.

### Content

* The content is set based on the **Body** field of the input log record.
* If the **Body** field is not a string type, the value is stringified. In case of complex types, it is stringified as a JSON string. For kvlist\_value type, see the differences between data models in the [Log ingestion API processing](#otlp-structured-logs) section below for more details.

### Attributes

* Contains all other attributes from the input record's attributes contained in the sections: **Resource**, **InstrumentationScope**, and **Attributes**.
* The `TraceID` and `SpanID` attributes are mapped to the `trace_id` and `span_id` fields, and their values are converted to hexadecimal representation (e.g., `0xCAFEBABE`).
* Automatic attribute. The `dt.auth.origin` attribute is automatically added to every log record ingested via API. This attribute is the public part of the API key that the log source authorizes to connect to the generic log ingest API.

All attributes should preferably map to **semantic attributes** for Dynatrace to interpret them correctly.

* Logs on Grail: All attributes can be used in queries, though Semantic Dictionary helps Davis AI in the interpretation of the logs. Refer to the [Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.") for more details.
* Log Monitoring Classic: Refer to the [Semantic attributes (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/logs-classic-ingestion-api/log-classic-semantic-attributes "Supported semantic attributes that are indexed in Log Monitoring Classic.") for more details.

## Data types

Dynatrace supports OpenTelemetry data types as described in the sections below.

### Scalar value

Scalar values are transformed as follows:

* Logs on Grail with OpenPipeline custom processing (Dynatrace SaaS version 1.295+, Environment ActiveGate version 1.295+): All JSON data types (string, number, boolean, null) are supported. All attributes can be used in queries. Keys are case-sensitive.
* Logs on Grail with OpenPipeline routed to Classic Pipeline: All attribute keys are lowercased and all attribute values are stringified. All attributes can be used in queries.
* Log Monitoring Classic: All attribute keys are lowercased and all attribute values are stringified. Custom attributes and semantic attributes can generally be used in queries.

### Byte array

Byte arrays are converted to base64-encoded strings. For example, the following array

```
[0x68, 0x65, 0x6c, 0x6c, 0x6f, 0x20, 0x77, 0x6f, 0x72, 0x6c, 0x64]
```

is transformed and ingested as `aGVsbG8gd29yZA==`.

### Array

Array attribute values are converted to arrays of a uniform type. The target type is chosen according to the following rules:

* Complex values, such as arrays, or objects are mapped to JSON string values.
* If any value in the array is a string, or if any value must be converted to a string (e.g., an object or array), the target type of the entire array is string.
* If all values in the source array are numeric, the target array type is numeric.
* Null values are considered compatible with any type.

### Map

Map processing depends on the data model used. See [Log ingestion API processing](#otlp-structured-logs) below for more details.

For example, this attribute map `planet`:

```
{



"name": "earth"



"system" : {



"name": "solar",



"galaxy": {



"name": "milky way",



"group": {



"name": "local"



}



}



}



}
```

would be flattened into four attributes:

```
"planet.name": "earth"



"planet.system.name": "solar"



"planet.system.galaxy.name": "milky way"



"planet.system.galaxy.group.name": "local"
```

* Scalar values are ingested in their string representation (see [scalar value](#scalar-value)).
* Byte arrays are ingested as Base64 strings (see [byte array](#byte-array)).
* `Any` arrays are ingested as lists, with values being transformed as [arrays](#array).
* Maps are flattened as outlined above ([up to five levels](#ingestion-limits)).

## Attribute ingestion

OpenTelemetry supports attributes at different levels in an OpenTelemetry log request, such as the resource level, scope level, and record level.

When Dynatrace ingests OpenTelemetry logs, it resolves duplicate attributes and automatically recognizes certain attributes names.

### Duplicate attributes

Dynatrace resolves duplicate attribute names automatically.
The exact method depends on the data model.

#### Flattened data model

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate.

For example, if you have three attributes all named `my.attribute` on the resource, scope, and log levels:

* The resource attribute is ingested as `my.attribute`.
* The scope attribute is ingested as `overwritten1.my.attribute`.
* The log attribute is ingested as `overwritten2.my.attribute`.

#### Raw data model

In the raw data model, OTLP resource attributes and OTLP attributes are parsed into Dynatrace top-level attributes, and the OTLP body is parsed into the content.

OTLP resource attributes and OTLP attributes are parsed into Dynatrace top-level attributes, and the OTLP body is parsed into the content.

Dynatrace prefixes duplicate attributes with an incrementing counter, for example `overwritten1.myattribute`. The counter value indicates how many times the attribute has been encountered as a duplicate. This avoids name collisions when attributes at different OTLP levels share the same name.

### Data transformation and automatic parsing

A number of attribute names are automatically recognized by Dynatrace and mapped to the respective Dynatrace log field.
These fields are defined in the Semantic Dictionary, see [Log Management and Analytics](/docs/semantic-dictionary/model/log "Get to know the Semantic Dictionary models related to Log Analytics.").

The timestamp, severity, and log message are set based on keys present in the input JSON object, as described in the following sections.

For a full list of attributes and their names, see [Log Monitoring API v2 - POST ingest logs](/docs/dynatrace-api/environment-api/log-monitoring-v2/post-ingest-logs#request-body-objects "Push custom logs to Dynatrace via the Log Monitoring API v2.").

#### Timestamp

The timestamp (`timestamp`) is determined based on one of the following, evaluated in order.

1. The `OTLP message timestamp` field.
2. The content of the body (if the body is a map).
3. The content of the OTLP log record.

If the timestamp is taken from the body or OTLP log record, the value is the first found attribute in the following list, evaluated in order:

1. `timestamp`
2. `@timestamp`
3. `_timestamp`
4. `eventtime`
5. `date`
6. `published_date`
7. `syslog.timestamp`
8. `syslog.timestamp`
9. `epochSecond`
10. `startTime`
11. `datetime`
12. `ts`
13. `timeMillis`
14. `@t`

Supported timestamp formats are: `UTC milliseconds`, `RFC3339`, and `RFC3164`.
For unsupported timestamp formats, the current timestamp is used, and the value of the unsupported format is stored in the `unparsed_timestamp` attribute.

Log records older than the [log age limit](/docs/analyze-explore-automate/logs/lma-limits#log-ingestion-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") are discarded. Timestamps more than 10 minutes ahead of the current time are replaced with the current time.

If there is no supported timestamp key in the log record, the default value is the current timestamp.

If there is no timezone in the timestamp, the default timezone is UTC.

#### Severity

The severity (`loglevel`), is determined based on one of the following, evaluated in order.

1. The `OTLP message severity` field.
2. The `severityText` field.
3. The content of the body (if the body is a map).
4. The content of the OTLP log record.

If the severity is taken from the body or OTLP log record, the value is the first found attribute in the following list, evaluated in order:

1. `loglevel`
2. `status`
3. `severity`
4. `level`
5. `syslog.severity`

The default value is `NONE`.

#### Log message

The log message (`content`), is determined based on the `OTLP log record body` field.

* If body is a scalar value, log content is set to the string representation of that value.

* If not, further processing depends on the data model:

  + Flattened model:

    - When the body is a map, content is set based on one of the following body attributes: content, message, payload, body, log (or left empty when no such key is present).
    - When the body is an array, the content is set to the string representation of the array.
  + Raw model: The content is set to the string representation of the array or map in the body.

## Ingestion limits

See [Log Management and Analytics default limits](/docs/analyze-explore-automate/logs/lma-limits "Default limits for the latest version of Dynatrace Log Management and Analytics.") and [Log Monitoring default limits (Logs Classic)](/docs/analyze-explore-automate/log-monitoring/log-monitoring-limits "Default limits for the latest version of Dynatrace Log Monitoring.") for the limits applied to ingested log requests, their attributes, and their attribute values.

## Log ingestion API processing

There are two data models that identify how structured logs are processed by log ingestion endpoints: **raw** and **flattened**. The difference between the two is in how attributes with object/dictionary values are transformed.

If this configuration option is not specified, the default behavior depends on when your environment was created.

* For Dynatrace version 1.331+: Raw.
* For Dynatrace versions 1.330 and earlier: Flattened.

Escaping in output examples is for visualization purposes only. `\"` is billed as one character.

### Raw data model

The raw data model transforms the content of structured logs as described in the sections below. All the following examples apply to Log ingestion API endpoints available on Environment ActiveGateand SaaS.

When using log shippers such as [Fluentbit](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-fluent-bit "Integrate Fluent Bit to stream logs to Dynatrace."), [Fluentd](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-fluentd-k8s "Integrate Fluentd with Dynatrace to stream logs from nodes and pods to Dynatrace.") or [Logstash](/docs/analyze-explore-automate/logs/lma-log-ingestion/lma-stream-logs-with-logstash "Integrate Logstash to stream logs from nodes and pods to Dynatrace."), avoid using JSON parsers on the shipper side and let Dynatrace handle the JSON parsing instead. This approach reduces processing overhead on your log shipper and ensures consistent parsing behavior.

#### Maps and arrays in attributes

For the raw data model, the map attribute values are turned into a JSON string, and the array attribute values are turned into an array of the uniform type.

Input

Log ingestion API endpoint output

```
body: "Hello world!"



Resource:



- "any-attr-type-3": {"3" = "c"}



Scope:



- "any-attr-type-2": {"2" = "b"}



Attributes:



- "any-attr-type-1": {"1" = "a"}



- "any-attr-type-4":



[ "val1", 10, -123.456, false, 0x01020304 ]
```

```
âcontentâ: "Hello world!"



"any-attr-type-1": "{\"1\": \"a\"}"



"any-attr-type-2": "{\"2\": \"b\"}"



"any-attr-type-3": "{\"3\": \"c\"}"



"any-attr-type-4":



["val1", "10", "-123.456", "false", "AQIDBA=="]
```

```
KeyValue {



key: "test"



value: {



kvlist_value: {



values: [



{



key: "attribute"



value: {



kvlist_value: {



values: [



{ key: "one", value: { string_value: "value 1" } },



{ key: "two", value: { string_value: "value 2" } }



]



}



}



}



]



}



}



}
```

```
"test": "{ \"attribute\": {\"one\": \"value 1\", \"two\": \"value 2\" } }"
```

#### Map in body

In this case, the **Body** field of the input log record is converted to a JSON string.

Input

Log ingestion API endpoint output

```
Body:



{



"content" = "Hello World!",



"my-body-attr-1": "abc",



"my-body-nested-1": {



"subkey": "val"



},



"@timestamp": "2025-06-01 13:01:02.123",



"loglevel": "INFO"



}
```

```
"content": "{ \"content\" = \"Hello World!\",



\"my-body-attr-1\": \"abc\",



\"my-body-nested-1\": {



\"subkey\": \"val\"



},



\"@timestamp\": \"2025-06-01 13:01:02.123\",



\"loglevel\": \"INFO\"



}"
```

#### Body as array

In this case, the array in the body is stringified.

Input

Log ingestion API endpoint output

```
Body:



[ "string-val", true, 12, 12.34, 0x6279746573 ]
```

```
"content": "[\"string-val\",true,12,12.34,\"Ynl0ZXM=\"]"



...
```

#### Name conflicts

In the raw data model, OTLP resource attributes and OTLP attributes are copied into Dynatrace top-level attributes, and the OTLP body is copied into the content.

Dynatrace prefixes duplicate attributes with an incrementing counter, for example `overwritten1.myattribute`. The counter value indicates how many times the attribute has been encountered as a duplicate. This avoids name collisions when attributes at different OTLP levels share the same name.

### Flattened data model

With the flattened data model, the content of structured logs is transformed as described in the sections below. All the following examples apply to Log ingestion API endpoints available on Environment ActiveGateand SaaS.

#### Maps and arrays in attributes

In this case, the map attribute values are flattened, i.e. replaced with keys concatenated using a dot (.) until a simple value is reached in the hierarchy, and the array attribute values are turned into a custom string.

Input

Log ingestion API endpoint output

```
body: "Hello world!"



Resource:



- "any-attr-type-3": {"3" = "c"}



Scope:



- "any-attr-type-2" : {"2" = "b"}



Attributes:



- "any-attr-type-1" : {"1" = "a"}



- "any-attr-type-4" :



[ "val1", 10, -123.456, false, 0x01020304 ]
```

```
âcontentâ: "Hello world!"



"any-attr-type-1.1": "a"



"any-attr-type-2.2": "b"



"any-attr-type-3.3": "c"



"any-attr-type-4":



["val1", 10, -123.456, false, "AQIDBA=="]
```

Flattening proceeds up to the maximum nesting level specified by the **Nested objects** limit. Structures nested deeper than this are replaced with the string value `<truncated due to nesting limit>`. See the [Ingestion limits](#ingestion-limits) section for details.

#### Map in body

In this case, the map attributes are merged with the log record.

Input

Log ingestion API endpoint output

```
Body:



{



"content" = "Hello World!",



"my-body-attr-1": "abc",



"my-body-nested-1": {



"subkey": "val"



},



"@timestamp": "2025-06-01 13:01:02.123",



"loglevel": "INFO"



}



Attributes:



- "any-attr-type-1" : "my-attr"
```

```
"content": "Hello world!"



"timestamp": "2025-06-01 13:01:02.123"



"loglevel": "INFO"



"any-attr-type-1": "my-attr"



"my-body-attr-1": "abc"



"my-body-nested-1.subkey": "val"
```

#### Body as array

In this case, the array in the body is stringified.

Input

Log ingestion API endpoint output

```
Body:



[ "string-val", true, 12, 12.34, 0x6279746573 ]
```

```
"content": "[\"string-val\",true,12,12.34,\"Ynl0ZXM=\"]"



...
```

#### Content-related behavior:

If the Body field is of **kvlist\_value** type (a list of key-value pairs), the structure is processed in the same way as log record attributes, including flattening and conflict resolution.

Attributes found in **Body** may also be used for setting the `timestamp`, `loglevel`, and `content` attributes of the log record, as described below.

##### Timestamp

* If the `timestamp` cannot be set based on the **Timestamp** field, the first of the following keys found in **Body** is used: `timestamp`, `@timestamp`, `_timestamp`, `eventtime`, `date`, `published_date`, `syslog.timestamp`, `time`, `epochSecond`, `startTime`, `datetime`, `ts`, `timeMillis`, `@t`.
* Supported timestamp formats: `UTC milliseconds`, `RFC3339`, and `RFC3164`.
* The default value is the current timestamp and the default timezone is UTC if it's missing in timestamp.

##### Log level

* If the `loglevel` cannot be set based on the **Severity** field, the first of the following keys found in **Body** is used: `loglevel`, `status`, `severity`, `level`, `syslog.severity`.
* The default value is `NONE`.

##### Content

* `content` is set based on the first of the following keys found in **Body**: `content`, `message`, `payload`, `body`, `log`, `_raw` (`_raw` is supported only in the raw data model).
* If no content attribute is found among supported content keys, the `content` is set to an empty string.

#### Name conflicts

When attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name. Dynatrace resolves this by prefixing duplicate attributes with `overwritten[COUNTER].`. The counter value indicates how many times the attribute name has been already encountered as a duplicate.

For example, if you have three attributes all named `my.attribute` on the resource, scope, and log levels:

* the resource attribute is ingested as `my.attribute`
* the scope attribute is ingested as `overwritten1.my.attribute`
* the log attribute is ingested as `overwritten2.my.attribute`

## Additional attributers handling

The Log ingestion API additionally accepts log attributes through:

* Query parameters
* Special header: `X-Dynatrace-Attr`

These attributes are merged with those provided in the OpenTelemetry log request according to the rules described below.

### Query parameter attributes

* All query parameters passed to the Log ingestion API endpoint are added to the log record attributes.
* If a parameter key appears multiple times, all values are captured as an array attribute.
* Keys and values follow the same attribute parsing rules as log request attributes.
* Certain parameters are processed by the API for internal purposes and never appear as log record attributes, even if explicitly provided (such as those used in the **XâDynatraceâOptions** header). For the complete list of reserved parameter names and their processing behavior, see the [API documentation](/docs/dynatrace-api/environment-api/opentelemetry/post-logs#parameters "Send OpenTelemetry logs to Dynatrace via API.").

#### Example

Request URL

Resulting output

```
otlphttp:



logs_endpoint: /api/v2/otlp/v1/logs?env=prod&env=blue&team=payments
```

```
Body: "Hello World!"
```

```
{



"content": "Hello World!",



"env": ["prod", "blue"],



"team": "payments"



}
```

### Header-based attributes (X-Dynatrace-Attr)

The API supports a special header for passing additional attributes:

```
otlphttp:



endpoint: /api/v2/otlp



headers:



X-Dynatrace-Attr: region=eu-central-1&team=core
```

Rules:

* Keys and values follow the same attribute parsing rules as query parameters.
* Multi-value behavior is also supported inside the header attributes.
* Same reserved parameter names restrictions apply.

### Attributes precedence rules

When attributes appear in multiple places, the Log ingestion API applies attribute precedence while still preserving body values for auditability. The attributes are applied in the following order:

* Query Parameters (highest precedence)
* X-Dynatrace-Attr header
* OpenTelemetry log request (lowest precedence; existing ingestion path)

#### Override behavior

When attributes from query parameters or the header override log request attributes:

* The final attribute value is set according to the attribute source precedence rules.
* The values already present in the log request are preserved and mirrored under `overwrittenN.<attribute_key>`.
  Where N is an incrementing integer (1, 2, â¦) depending on how many log request-originating values had to be preserved. This ensures uniqueness, even when multiple conflicts occur.
* Only values originating from the log request are preserved under the `overwrittenN.*` keys. Attributes overridden by higher-precedence sources do not generate overwritten copies.

#### Example

Request

Resulting output

```
otlphttp:



logs_endpoint: /api/v2/otlp/v1/logs?team=frontend
```

Log Request:

```
Body: "Hello World!"



Attributes:



- "team": "backend"
```

```
{



"content": "Hello World!",



"team": "frontend",



"overwritten1.team": "backend"



}
```

### Billing behavior

Attributes provided through query parameters or headers are included in billing calculations.

For multi-value attributes, the attribute key contributes to billing only once, regardless of how many values are present.

## Related topics

* [OpenTelemetry logs ingest API](/docs/dynatrace-api/environment-api/opentelemetry/post-logs "Send OpenTelemetry logs to Dynatrace via API.")


---


## Source: about-metrics-ingest.md


---
title: About OTLP metrics ingest
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest
scraped: 2026-02-17T21:31:40.465791
---

# About OTLP metrics ingest

# About OTLP metrics ingest

* Latest Dynatrace
* Explanation
* 2-min read
* Updated on Nov 04, 2025

Dynatrace version 1.254+

This page provides information about how Dynatrace ingests and enriches OpenTelemetry metrics.

Migrate from the Dynatrace OpenTelemetry metrics exporter

If you're still using the Dynatrace OpenTelemetry metrics exporter, we recommend that you migrate to the OTLP metrics exporter.
For more information, see [Migrating from the Dynatrace OTel metrics exporter to standard OTLP metrics exporterï»¿](https://community.dynatrace.com/t5/Open-Q-A/Migrating-from-the-Dynatrace-OTel-metrics-exporter-to-standard/m-p/286986/thread-id/37689#M37690).

## Dynatrace-specific mapping

Dynatrace maps the individual OpenTelemetry instruments to the following Dynatrace metric types:

| Instrument | with temporality | maps to Dynatrace |
| --- | --- | --- |
| Counter | Delta | Counter |
| Counter | Cumulative | N/A |
| Gauge | N/A | Gauge |
| Explicit bucket histogram [1](#fn-1-1-def) | Delta | Histogram |
| Exponential histogram [2](#fn-1-2-def) | Delta | Exponential histogram |
| UpDownCounter | Delta | Counter |
| UpDownCounter | Cumulative | Gauge |
| Summary | N/A | N/A |

1

Explicit bucket histograms are supported starting with Dynatrace version 1.300.

2

For exponential histograms, Dynatrace ingests the histogram's `min|max|sum|count` but doesn't ingest the buckets.

## API limits and validations

When ingesting OpenTelemetry metrics, the following limits and validations apply.

| Entity | Limit | Description |
| --- | --- | --- |
| Metric key length, characters | Min: 2, Max: 255 | The length of a metric key. |
| Dimension key length, characters | Min: 1, Max: 100 | The length of a dimension key. If the maximum length is exceeded, the key is truncated to 100 characters. |
| Dimension value length, characters | Min: 1, Max: 255 | The length of a dimension value. If the maximum length is exceeded, the dimension value is truncated to 255 characters. |
| Number of dimensions per metric data point | 50 | The maximum total number of dimensions in a single metric data point. If the number of dimensions is exceeded, the whole data point is dropped. |
| Total number of possible metric keys per environment | 100,000 | The maximum number of metric keys that can be active at the same time. |
| Number of tuples per month per metric | 1,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for each metric key for the last 30 days. |
| Number of tuples per month for all custom metrics | 50,000,000 | The maximum number of tuples (unique metric-dimension key-value type combinations) for all custom metrics for the last 30 days. |
| Instrument unit, characters | 63 | The maximum total length of the instrument unit. If the maximum length is exceeded, the unit is dropped. |
| Instrument description, characters | 1,023 | The maximum total length of the instrument description. If the maximum length is exceeded, the instrument description is truncated to 1,023 characters. |
| Request size | 4 MB | The maximum uncompressed size of an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |
| Metric data points | 15,000 | The maximum number of metric data points in an OTLP request with a metrics payload. If the limit is exceeded, the entire request is dropped. |

### Attribute ingestion

OpenTelemetry supports attributes on different levels in an OpenTelemetry metric request (that is, data points, scopes, and resources).
Because attributes are saved in a flattened fashion on the Dynatrace side, there may be name collisions if attributes on different levels share the same name.

To handle such name conflicts, Dynatrace applies the following order of priority to choose which attribute will be ingested:

1. Data point attributes
2. Scope attributes
3. Resource attributes

For example, if there is a data point and a scope attribute have the same name, the value of the data point will take precedence.
Similarly, if a scope and resource attribute share the same name, Dynatrace will ingest the value of the scope attribute.

### Aggregation temporality

The Dynatrace backend exclusively works with delta values and requires the respective aggregation temporality.
Please ensure your metrics exporter is accordingly configured or set the [`OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE`ï»¿](https://opentelemetry.io/docs/specs/otel/metrics/sdk_exporters/otlp/) environment variable to `DELTA`.

For examples on how to set the temporality under each individual language, see the [integration walkthroughs](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

### Metric keys

* A metric key consists of sections separated by dots (for example, `dt.metrics`).
* A metric key can contain lowercase and uppercase letters, numbers, hyphens (`-`), and underscores (`_`).
* A metric key must start with a letter character.
* A metric key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).
* A metric key may be suffixed automatically depending on the payload (for example, `.count` for counters and `.gauge` for gauges).

If you use characters that are invalid according to the rules above, they will be replaced with underscores.
If your metric key does not have at least one valid character, the data point will be dropped.

### Dimension keys

* Dimensions are comparable to span or resources attributes.
* A dimension key can contain only lowercase letters (not uppercase letters), numbers, hyphens (`-`), periods (`.`), and underscores (`_`).
* A dimension key must start with a letter character.
* A dimension key must not contain non-Latin characters (such as `Ã¤`, `Ã¶`, and `Ã¼`).
* A dimension key can be in the `key.key-section` format.
* You can specify up to 50 dimensions.
* If the same dimension key is specified multiple times in a single payload, only the value that occurs first is accepted.

If you use characters that are invalid according to the rules above, they will be replaced with underscores.
If your dimension key does not have at least one valid character, the key will be dropped.

Dimension values must be passed as a string, Boolean, or integer.

Dynatrace does not support non-string dimensions and will convert Booleans and integers to strings upon ingest.

If any other type is used, the entire dimension will be dropped.

### Histograms

For exponential histograms, Dynatrace ingests the histogram's `min|max|sum|count` but doesn't ingest the buckets.

If any of below happens, the OpenTelemetry ingest API returns the `400` or `200 with partial success` responses.

* Cumulative histograms aren't ingested (similarly to cumulative counters).
* Histogram data points without sum aren't ingested. This happens when negative values are recorded.
* Histogram buckets are not sorted.
* Histogram bucket boundary values of `NaN` or `Infinite` are invalid.

The Dynatrace OpenTelemetry ingest API only returns an HTTP `400` when all metrics in the OTLP request are invalid.

### Summaries

Dynatrace does not support summary metrics.

Summary metrics only exist in the OpenTelemetry protocol (OTLP) for compatibility with other formats.
Applications using official OpenTelemetry SDKs cannot produce summary metrics.


---


## Source: ingest-traces.md


---
title: Ingest OTLP traces
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/ingest-traces
scraped: 2026-02-17T21:24:56.384399
---

# Ingest OTLP traces

# Ingest OTLP traces

* Latest Dynatrace
* Reference
* 1-min read
* Updated on Jul 15, 2024

The following limitations apply to OpenTelemetry trace ingest requests and ingested spans.

| Type | Limit | Description |
| --- | --- | --- |
| Span end time | 60 minutes in the past | The minimum value of the span end timestamp at time of ingestion |
| Span end time | 10 minutes in the future | The maximum value of the span end timestamp at time of ingestion |
| Number of span attributes | 128[1](#fn-1-1-def) | The maximum number of span attributes per span |
| Number of span events | 128[1](#fn-1-1-def) | The maximum number of events per span |
| Number of event attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span event |
| Number of span links | 128[1](#fn-1-1-def) | The maximum number of links per span |
| Number of link attributes | 128[1](#fn-1-1-def) | The maximum number of attributes per span link |
| Request size | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (uncompressed data) |
| Request size (gzip) | 8 MB | The maximum size of an OTLP request for trace ingest to an ActiveGate (compressed data) |

1

Typical limit of the OpenTelemetry SDK. Not limited by Dynatrace.


---


## Source: otel-semantic-mapping.md


---
title: OpenTelemetry to Dynatrace semantic mapping
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api/otel-semantic-mapping
scraped: 2026-02-17T21:28:00.518594
---

# OpenTelemetry to Dynatrace semantic mapping

# OpenTelemetry to Dynatrace semantic mapping

* Latest Dynatrace
* Reference
* 2-min read
* Published Jan 08, 2026

Dynatrace automatically maps OpenTelemetry semantic conventions to the [Dynatrace Semantic Dictionary](/docs/semantic-dictionary "The Semantic Dictionary defines standardized field names used across monitoring data types like logs, events, spans, metrics, and entities.").

This mapping ensures consistent data interpretation across your observability stack and enables Dynatrace apps, analytics, and visualization features to work with OpenTelemetry instrumentation.

## Messaging operations

Dynatrace maps OpenTelemetry messaging attributes to the Dynatrace semantic model.

| OpenTelemetry attribute | Dynatrace attribute |
| --- | --- |
| `messaging.operation` | `messaging.operation.type` |

For [`messaging.operation.type`](/docs/semantic-dictionary/fields#messaging "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types."), the value `send` is normalized to `publish`.

## URL parsing

Dynatrace automatically parses [`url.full`](/docs/semantic-dictionary/fields#url "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") into its constituent components:

| Derived attribute | Description |
| --- | --- |
| `url.path` | The path component of the URL |
| `url.scheme` | The protocol scheme (for example, `https`) |
| `url.fragment` | The fragment identifier |
| `url.query` | The query string |
| `server.address` | The host address |
| `server.port` | The port number |

### Deprecated attributes

Dynatrace maps deprecated OpenTelemetry HTTP attributes to their current equivalents:

| Deprecated attribute | Current attribute |
| --- | --- |
| `http.url` | `url.full` |
| `http.method` | `http.request.method` |
| `http.status_code` | `http.response.status_code` |

## Cloud provider attributes

Dynatrace creates provider-specific attributes from standard OpenTelemetry cloud attributes.

### Account and project identifiers

Dynatrace creates provider-specific account attributes from the standard [`cloud.account.id`](/docs/semantic-dictionary/fields#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") attribute:

| Cloud provider | OpenTelemetry attribute | Created attribute |
| --- | --- | --- |
| AWS | `cloud.account.id` | `aws.account.id` |
| Azure | `cloud.account.id` | `azure.subscription` |
| Google Cloud | `cloud.account.id` | `gcp.project.id` |

### Regional attributes

Dynatrace creates provider-specific region attributes from standard [`cloud.region`](/docs/semantic-dictionary/fields#cloud "Get to know the list of global fields that have a well defined semantic meaning in Dynatrace and can be used across different monitoring types.") and related attributes:

| Cloud provider | OpenTelemetry attributes | Created attribute |
| --- | --- | --- |
| AWS | `cloud.region` | `aws.region` |
| Azure | `cloud.region` | `azure.location` |
| Google Cloud | `gcp.location` `gcp.zone` `cloud.region` `cloud.availability_zone` | `gcp.region` |

For Google Cloud, if multiple source attributes are present, they are evaluated in the order listed above.

## Use standard OpenTelemetry conventions

Standard [OpenTelemetry semantic conventionsï»¿](https://opentelemetry.io/docs/specs/semconv/) are supported in your instrumentation. Dynatrace handles the translation automatically. This allows standard OpenTelemetry semantic conventions to work with Dynatrace semantic analysis.


---


## Source: otlp-api.md


---
title: Dynatrace OTLP API endpoints
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/otlp-api
scraped: 2026-02-17T21:24:33.130347
---

# Dynatrace OTLP API endpoints

# Dynatrace OTLP API endpoints

* Latest Dynatrace
* Explanation
* 8-min read
* Updated on Jan 09, 2026

The [OpenTelemetry Protocol (OTLP)ï»¿](https://opentelemetry.io/docs/specs/otlp/) is the principal network protocol for the exchange of telemetry data between OpenTelemetry-backed services and applications.

Dynatrace provides native OTLP endpoints with the following services:

* The Dynatrace SaaS platform
* ActiveGate instances

Alternatively, you can deploy the [Dynatrace Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") as an intermediary service application to batch requests and improve network performance, or to transform requests before forwarding them to Dynatrace (for example, [mask sensitive data](/docs/ingest-from/opentelemetry/collector/use-cases/redact "Configure the OpenTelemetry Collector to mask sensitive data before forwarding to Dynatrace.")).

## Default ingest paths

The ingest paths used by Dynatrace for the individual signal types follow the [standard OpenTelemetry pathsï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/#endpoint-urls-for-otlphttp).

| Signal Type | Path |
| --- | --- |
| Traces | `/v1/traces` |
| Metrics | `/v1/metrics` |
| Logs | `/v1/logs` |

Depending on the configuration, you may need to append these paths individually to the base URLs of the following service endpoints when specifying the export URLs. This can happen either in-code, when using [manual instrumentation](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace."), or using the standard [environment variablesï»¿](https://opentelemetry.io/docs/languages/sdk-configuration/otlp-exporter/#endpoint-configuration).

## Export to Dynatrace

### Base URLs

The following addresses provide the base URLs for your OTLP ingest configuration. Use the URL applicable to your type of environment and replace the relevant part with your [environment ID](/docs/discover-dynatrace/get-started/monitoring-environment "Understand and learn how to work with monitoring environments.").
You will also use the base URL if you define the `OTEL_EXPORTER_OTLP_ENDPOINT` environment variable, see [Environment variables](#environment-variables).

| API Type | Base URL |
| --- | --- |
| Dynatrace SaaS | `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp` |
| Environment ActiveGate[1](#fn-1-1-def) | `https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp` |
| Containerized Environment ActiveGate[2](#fn-1-2-def) | `https://{your-activegate-domain}/e/{your-environment-id}/api/v2/otlp` |

1

Environment ActiveGates listen by default on port `9999`. If you changed that port, adjust the port in the URL accordingly.

2

A [PVC](/docs/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data.") is required for this setup.

If you copy your environment ID from the browser's address bar, make sure to remove `.apps`.

* Incorrect base URL: `https://{your-environment-id}.live.apps.dynatrace.com/api/v2/otlp`
* Correct base URL: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`

Otherwise, the API calls will return an error that looks like this:

```
not retryable error: Permanent error: rpc error: code = Unimplemented desc = error exporting items, request to https://<environment>.live.apps.dynatracelabs.com/api/v2/otlp/v1/logs responded with HTTP Status Code 404
```

### URL examples

The following example URLs illustrate combinations of base URLs and paths for signal types.

#### Dynatrace SaaS

Signal type

URL

Traces

`https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/traces`

Metrics

`https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics`

Logs

`https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/logs`

#### Environment ActiveGate

Signal type

URL

Traces

`https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/traces`

Metrics

`https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/metrics`

Logs

`https://{your-activegate-domain}:9999/e/{your-environment-id}/api/v2/otlp/v1/logs`

Information enrichment

Vanilla OTLP exports to ActiveGate require manual enrichment of Dynatrace host information to have the proper topology information.

To do so, make sure your traces have the correct mapping resource attributes set. The list of applicable attributes can be found in (or imported from) the [enrichment files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

### API limitations

Calls to Dynatrace API endpoints have the following limitations.

* gRPC is not supported.
  API calls need to use HTTP.
* JSON is not supported for Protocol Buffers.
  Binary format must be used.

### Environment variables

When you configure your application to export to Dynatrace, one way is to configure certain environment variables as described below.

```
OTEL_EXPORTER_OTLP_ENDPOINT=[YOUR_BASE_URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [YOUR_TOKEN]"



OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf
```

For more information about language-specific configuration, see [Instrument your application](/docs/ingest-from/opentelemetry/walkthroughs "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

### Authentication and access tokens

For exports to SaaS and ActiveGate, authentication is handled using an API access token and the `Authorization` HTTP header.
For more information on access tokens, see [Dynatrace API - Tokens and authentication](/docs/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

To create an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.
Use the appropriate access scopes for the signals that you want to export.
You can combine scopes in a single token, and also add scopes to an existing token.

* Traces: `openTelemetryTrace.ingest`
* Metrics: `metrics.ingest`
* Logs: `logs.ingest`

### Network requirements

Verify that the following are true:

* TCP port is not blocked

  Because OTLP communication with ActiveGate takes place over the ports 443 (for SaaS and Managed) or 9999 (for Environment ActiveGates), make sure that the TCP port in question is not blocked by a firewall or any other network management solution you might be using.
* Your system's certificate trust store is up to date

  To avoid possible SSL certificate issues with expired or missing default root certificates, make sure that your system's certificate trust store is up to date.

## Export to the Collector

Using the Collector as an intermediate gateway allows you to streamline and optimize your telemetry data and requests centrally. See [OpenTelemetry Collector use cases](/docs/ingest-from/opentelemetry/collector/use-cases "Configure your Collector instance for different use cases.") for more information and sample configurations for popular Collector use cases.

See [Dynatrace OTel Collector](/docs/ingest-from/opentelemetry/collector "Learn about the Dynatrace OTel Collector.") for more details on how to configure a Collector instance.

gRPC conversion

As Dynatrace currently requires OTLP exports with HTTP, you can use the Collector to convert gRPC exports to HTTP.

See [Transform OTLP gRPC to HTTP with the OpenTelemetry Collector](/docs/ingest-from/opentelemetry/collector/use-cases/grpc "Configure the OpenTelemetry Collector to transform a gRPC OTLP request to HTTP.") for more details.

### Authentication and TLS

Whether you need to use TLS and authenticate your requests against the Collector depends on your particular Collector setup/configuration. By default, the [OTLP receiverï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/receiver/otlpreceiver/README.md) is configured for plain-text HTTP and does not require authentication.

The eventual outbound connection from the Collector to Dynatrace always requires authentication and TLS.

### Network requirements

Verify that the following are true:

* Network ports not blocked

  Make sure the network ports required by the configured receiver instances are not blocked by a firewall or any other network management solution used as part of your infrastructure.

## Related topics

* [OpenTelemetry Protocol (OTLP) ingest API](/docs/dynatrace-api/environment-api/opentelemetry "Use Dynatrace API as a target for OpenTelemetry exporters to ingest OpenTelemetry metrics, logs, and traces.")


---


## Source: troubleshooting.md


---
title: Ensure success with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/troubleshooting
scraped: 2026-02-17T21:24:28.367468
---

# Ensure success with OpenTelemetry

# Ensure success with OpenTelemetry

* Latest Dynatrace
* Troubleshooting
* 1-min read
* Updated on Dec 03, 2025

Successfully implementing OpenTelemetry requires both reliable data export and proper visualization in Dynatrace.
This page offers guidance for properly configuring and troubleshooting your OpenTelemetry implementation with Dynatrace.

## Metrics for ingest monitoring

Dynatrace provides the following built-in metrics for the ingestion of OpenTelemetry signals.
In case of missing data, these can be useful in further analyzing possible ingestion issues.

In Dynatrace Classic, ingest monitoring metrics are prefixed with `dsfm:` instead of `dt.sfm.`

### Metrics for logs ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.active_gate.event_ingest.event_incoming_count` | Number of ingested log records |
| `dt.sfm.active_gate.event_ingest.drop_count` | Number of dropped log records |
| `dt.sfm.active_gate.event_ingest.event_otlp_size` | Payload size of received log requests |

### Metrics for metrics ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.accepted` | Number of accepted data points |
| `dt.sfm.active_gate.metrics.ingest.otlp.datapoints.rejected` | Number of rejected data points |

Rejected metrics come with a `reason` dimension, which provides additional details on why a data point was rejected.
In Dynatrace, you can filter, sort, and split by that dimension.

A typical reason is when metrics are sent with cumulative aggregation temporality (Dynatrace [requires delta temporality](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")), in which case `reason` indicates `UNSUPPORTED_METRIC_TYPE_MONOTONIC_CUMULATIVE_SUM`.

### Metrics for traces ingest

Latest Dynatrace

| Name | Description |
| --- | --- |
| `dt.sfm.server.spans.received` | Number of OpenTelemetry spans ingested via the OLTP trace endpoint (ActiveGate or OneAgent) that were successfully received by Dynatrace |
| `dt.sfm.server.spans.persisted` | Number of OpenTelemetry spans preserved by Dynatrace; only preserved spans are available for distributed traces analysis |
| `dt.sfm.server.spans.dropped` | Number of OpenTelemetry spans that were not preserved by Dynatrace because of the indicated reason (for example, span end time out of range) |

## Common issues and solutions

### Setup issues

* [I'm having setup issues with OpenTelemetry. What should I check?ï»¿](https://dt-url.net/dm038xt)
* [Fixing SSL Errors in OpenTelemetry SDKs when exporting to Dynatrace ActiveGateï»¿](https://community.dynatrace.com/t5/Troubleshooting/Fixing-SSL-Errors-in-OpenTelemetry-SDKs-when-exporting-to/ta-p/269404)

### Connection issues

* [Why do I get a connection error when exporting with OTLP to ActiveGate?ï»¿](https://dt-url.net/x0238hc)
* [Why do I get a connection error when exporting OpenTelemetry traces to OneAgent?ï»¿](https://dt-url.net/tk4384x)

### Authentication issues

* Problem: HTTP 401/403 errors in ingestion metrics.
* Solution: Verify API permissions and endpoint configurations.

See also:

* [Why does ActiveGate return a 401 Unauthorized error?ï»¿](https://dt-url.net/lg638i3)
* [Why does ActiveGate return a 403 Forbidden error?ï»¿](https://dt-url.net/2n838im)

### Data format issues

* Problem: High drop rates with format errors.
* Solution: Validate OpenTelemetry data format compliance and attribute limits.

### Configuration issues

* Problem: No data appears despite successful exports.
* Solution: Verify endpoint URLs, headers, and protocol configuration.

### Ingestion issues

* [Why does my OTLP export not work?ï»¿](https://dt-url.net/sb238k5)
* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")

### Vertical topology

* [Why is my vertical topology missing?ï»¿](https://dt-url.net/48038un)

## Signal-specific questions

Specific information about ingesting each signal type is available at

* [Ingest OTLP logs](/docs/ingest-from/opentelemetry/otlp-api/ingest-logs "Learn how Dynatrace ingests OpenTelemetry log records and what limitations apply.")
* [About OTLP metrics ingest](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.")
* [Ingest OTLP traces](/docs/ingest-from/opentelemetry/otlp-api/ingest-traces "Learn how Dynatrace ingests OpenTelemetry traces and what limitations apply.")

### Traces

* [Why are my spans not linked? Why are my spans orphaned?ï»¿](https://dt-url.net/ae038vj)
* [Why are my OpenTelemetry span attributes missing?ï»¿](https://dt-url.net/z402yxq)

### Metrics

* [Why are my metrics not ingested?ï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)
* [Why are my cumulative metrics not ingested?ï»¿](https://dt-url.net/s60382e)
* [Why do I receive a "Partial Success" response?ï»¿](https://dt-url.net/0u238ec)
* [Why are my metric attributes missing?ï»¿](https://dt-url.net/jj03800)
* [How to set up OpenTelemetry metrics with delta temporalityï»¿](https://community.dynatrace.com/t5/Troubleshooting/How-to-set-up-OpenTelemetry-metrics-with-delta-temporality/ta-p/269292)
* [Delay in displaying OpenTelemetry metric dimensions in Dynatraceï»¿](https://community.dynatrace.com/t5/Troubleshooting/Delay-in-displaying-OpenTelemetry-metric-dimensions-in-Dynatrace/ta-p/269732)
* [Why are my OpenTelemetry metrics not ingestedï»¿](https://community.dynatrace.com/t5/Troubleshooting/Why-are-my-OpenTelemetry-metrics-not-ingested/ta-p/269428)

## Best practices

### Use metric dimensions

Dimensions are used in Dynatrace to help distinguish what is being measured in a specific data point.

In OpenTelemetry, dimensions are called attributes.

For example, if you're measuring the number of requests an endpoint has received, you can use dimensions to split that metric into requests that went through (status code 200) and requests that failed (status code 500).

Your dimensions should be well-annotated (recognizable, readable, understandable), have descriptive names, and provide good information.

### Compression

Dynatrace recommends that you enable `gzip` compression on your OTLP exporters.

The default compression on the OTLP exporter [is not setï»¿](https://opentelemetry.io/docs/specs/otel/protocol/exporter/), but it can be configured through the following environment variables:

* `OTEL_EXPORTER_OTLP_COMPRESSION`
* `OTEL_EXPORTER_OTLP_TRACES_COMPRESSION`
* `OTEL_EXPORTER_OTLP_METRICS_COMPRESSION`
* `OTEL_EXPORTER_OTLP_LOGS_COMPRESSION`

Acceptable values are `none` or `gzip`.

### Batching

If you use the OpenTelemetry Collector, we highly recommend that you use a [batch processorï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md).

Batching helps better compress the data and reduce the number of outgoing connections required to transmit data to Dynatrace.

See this [GitHub readmeï»¿](https://github.com/open-telemetry/opentelemetry-collector/blob/v0.145.0/processor/batchprocessor/README.md) for more information.


---


## Source: cpp.md


---
title: Instrument your C++ application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/cpp
scraped: 2026-02-17T21:32:56.959708
---

# Instrument your C++ application with OpenTelemetry

# Instrument your C++ application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 12, 2025

This walkthrough shows how to add observability to your C++ application using the OpenTelemetry C++ libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Prerequisites

* Dynatrace version 1.222+
* A [supportedï»¿](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/README.md#supported-development-platforms) C++ compiler (C++ 11 and later)
* The [Protocol Buffers libraryï»¿](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md)
* The [OpenTelemetry libraryï»¿](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/INSTALL.md)
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Set up OpenTelemetry

1. Add the following directives to your CMake build configuration in `CMakeLists.txt`:

   ```
   find_package(CURL REQUIRED)



   find_package(Protobuf REQUIRED)



   find_package(opentelemetry-cpp CONFIG REQUIRED)



   include_directories("${OPENTELEMETRY_CPP_INCLUDE_DIRS}")



   target_link_libraries(



   <YOUR_EXE_NAME> ${OPENTELEMETRY_CPP_LIBRARIES}



   opentelemetry_trace



   opentelemetry_common



   opentelemetry_http_client_curl



   opentelemetry_exporter_otlp_http



   opentelemetry_exporter_otlp_http_client



   opentelemetry_otlp_recordable



   opentelemetry_resources



   opentelemetry_metrics



   opentelemetry_exporter_otlp_http_metric



   )
   ```
2. Create a file named `otel.h` in your application directory and save the following content:

   ```
   #include "opentelemetry/trace/provider.h"



   #include "opentelemetry/trace/propagation/http_trace_context.h"



   #include "opentelemetry/context/propagation/global_propagator.h"



   #include "opentelemetry/sdk/trace/simple_processor_factory.h"



   #include "opentelemetry/sdk/trace/tracer_context.h"



   #include "opentelemetry/sdk/trace/tracer_context_factory.h"



   #include "opentelemetry/sdk/trace/tracer_provider_factory.h"



   #include "opentelemetry/exporters/ostream/span_exporter_factory.h"



   #include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"



   #include "opentelemetry/metrics/provider.h"



   #include "opentelemetry/sdk/metrics/export/periodic_exporting_metric_reader.h"



   #include "opentelemetry/sdk/metrics/view/view_registry_factory.h"



   #include "opentelemetry/sdk/metrics/meter_context_factory.h"



   #include "opentelemetry/sdk/metrics/meter_provider_factory.h"



   #include "opentelemetry/exporters/ostream/metric_exporter_factory.h"



   #include "opentelemetry/exporters/otlp/otlp_http_metric_exporter_factory.h"



   #include "opentelemetry/logs/provider.h"



   #include "opentelemetry/sdk/logs/logger.h"



   #include "opentelemetry/sdk/logs/logger_provider_factory.h"



   #include "opentelemetry/sdk/logs/simple_log_record_processor_factory.h"



   #include "opentelemetry/sdk/logs/logger_context_factory.h"



   #include "opentelemetry/exporters/ostream/log_record_exporter.h"



   #include "opentelemetry/exporters/otlp/otlp_http_log_record_exporter_factory.h"



   #include <cstring>



   #include <iostream>



   #include <vector>



   #include <fstream>



   #include <list>



   #include <memory>



   #include <thread>



   #include <iostream>



   #include <string>



   using namespace std;



   namespace nostd    = opentelemetry::nostd;



   namespace otlp     = opentelemetry::exporter::otlp;



   namespace resource = opentelemetry::sdk::resource;



   namespace trace_api      = opentelemetry::trace;



   namespace trace_sdk      = opentelemetry::sdk::trace;



   namespace metrics_api   = opentelemetry::metrics;



   namespace metrics_sdk    = opentelemetry::sdk::metrics;



   namespace logs_api      = opentelemetry::logs;



   namespace logs_sdk      = opentelemetry::sdk::logs;



   namespace



   {



   // Class definition for context propagation



   otlp::OtlpHttpMetricExporterOptions options;



   std::string version{ "1.0.1" };



   std::string name{ "app_cpp" };



   std::string schema{ "https://opentelemetry.io/schemas/1.2.0" };



   template <typename T>



   class HttpTextMapCarrier : public opentelemetry::context::propagation::TextMapCarrier



   {



   public:



   HttpTextMapCarrier<T>(T &headers) : headers_(headers) {}



   HttpTextMapCarrier() = default;



   virtual nostd::string_view Get(nostd::string_view key) const noexcept override



   {



   std::string key_to_compare = key.data();



   // Header's first letter seems to be  automatically capitaliazed by our test http-server, so



   // compare accordingly.



   if (key == opentelemetry::trace::propagation::kTraceParent)



   {



   key_to_compare = "Traceparent";



   }



   else if (key == opentelemetry::trace::propagation::kTraceState)



   {



   key_to_compare = "Tracestate";



   }



   auto it = headers_.find(key_to_compare);



   if (it != headers_.end())



   {



   return it->second;



   }



   return "";



   }



   virtual void Set(nostd::string_view key, nostd::string_view value) noexcept override



   {



   headers_.insert(std::pair<std::string, std::string>(std::string(key), std::string(value)));



   }



   T headers_;



   };



   // ===== GENERAL SETUP =====



   void initTracer()



   {



   otlp::OtlpHttpExporterOptions traceOptions;



   traceOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/traces";



   traceOptions.content_type  = otlp::HttpRequestContentType::kBinary;



   traceOptions.http_headers.insert(



   std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   resource::ResourceAttributes dt_resource_attributes;



   try



   {



   for (string name : {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"})



   {



   string file_path;



   ifstream dt_file;



   dt_file.open(name);



   if (dt_file.is_open())



   {



   string dt_metadata;



   ifstream dt_properties;



   while (getline(dt_file, file_path))



   {



   dt_properties.open(file_path);



   if (dt_properties.is_open())



   {



   while (getline(dt_properties, dt_metadata))



   {



   dt_resource_attributes.SetAttribute(



   dt_metadata.substr(0, dt_metadata.find("=")),



   dt_metadata.substr(dt_metadata.find("=") + 1)



   );



   }



   dt_properties.close();



   }



   }



   dt_file.close();



   }



   }



   }



   catch (...) {}



   auto dt_resource = resource::Resource::Create(dt_resource_attributes);



   auto resource = resource::Resource::Create(resource_attributes);



   auto merged_resource = dt_resource.Merge(resource);



   auto exporter = otlp::OtlpHttpExporterFactory::Create(traceOptions);



   auto processor = trace_sdk::SimpleSpanProcessorFactory::Create(std::move(exporter));



   std::vector<std::unique_ptr<trace_sdk::SpanProcessor>> processors;



   processors.push_back(std::move(processor));



   auto context = trace_sdk::TracerContextFactory::Create(std::move(processors), merged_resource);



   std::shared_ptr<opentelemetry::trace::TracerProvider> provider = opentelemetry::sdk::trace::TracerProviderFactory::Create(std::move(context));



   // Set the global trace provider



   opentelemetry::trace::Provider::SetTracerProvider(provider);



   // set global propagator



   opentelemetry::context::propagation::GlobalTextMapPropagator::SetGlobalPropagator(



   opentelemetry::nostd::shared_ptr<opentelemetry::context::propagation::TextMapPropagator>(



   new opentelemetry::trace::propagation::HttpTraceContext()));



   }



   // ===== METRIC SETUP =====



   void initMeter() {



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   otlp::OtlpHttpMetricExporterOptions otlpOptions;



   auto resource = resource::Resource::Create(resource_attributes);



   otlpOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/metrics";



   otlpOptions.aggregation_temporality = otlp::PreferredAggregationTemporality::kDelta;



   otlpOptions.content_type = otlp::HttpRequestContentType::kBinary;



   otlpOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   //This creates the exporter with the options we have defined above.



   auto exporter = otlp::OtlpHttpMetricExporterFactory::Create(otlpOptions);



   metrics_sdk::PeriodicExportingMetricReaderOptions options;



   options.export_interval_millis = std::chrono::milliseconds(1000);



   options.export_timeout_millis  = std::chrono::milliseconds(500);



   std::unique_ptr<metrics_sdk::MetricReader> reader{new metrics_sdk::PeriodicExportingMetricReader(std::move(exporter), options) };



   auto context = metrics_sdk::MeterContextFactory::Create(opentelemetry::sdk::metrics::ViewRegistryFactory::Create(), resource);



   context->AddMetricReader(std::move(reader));



   auto u_provider = metrics_sdk::MeterProviderFactory::Create(std::move(context));



   std::shared_ptr<opentelemetry::metrics::MeterProvider> provider(std::move(u_provider));



   metrics_api::Provider::SetMeterProvider(provider);



   }



   // ===== LOG SETUP =====



   void initLogger() {



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   auto resource = resource::Resource::Create(resource_attributes);



   otlp::OtlpHttpLogRecordExporterOptions loggerOptions;



   loggerOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/logs";



   loggerOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   loggerOptions.content_type = opentelemetry::exporter::otlp::HttpRequestContentType::kBinary;



   auto exporter  = otlp::OtlpHttpLogRecordExporterFactory::Create(loggerOptions);



   auto processor = logs_sdk::SimpleLogRecordProcessorFactory::Create(std::move(exporter));



   std::vector<std::unique_ptr<logs_sdk::LogRecordProcessor>> processors;



   processors.push_back(std::move(processor));



   auto context = logs_sdk::LoggerContextFactory::Create(std::move(processors), resource);



   std::shared_ptr<logs_api::LoggerProvider> provider = logs_sdk::LoggerProviderFactory::Create(std::move(context));



   opentelemetry::logs::Provider::SetLoggerProvider(provider);



   }



   nostd::shared_ptr<opentelemetry::logs::Logger> get_logger(std::string scope){



   // TODO: add your log provider here



   return logger;



   }



   opentelemetry::nostd::shared_ptr<opentelemetry::trace::Tracer> get_tracer(std::string tracer_name)



   {



   // TODO: add your trace provider here



   return tracer;



   }



   nostd::unique_ptr<opentelemetry::metrics::Counter<uint64_t>> initIntCounter()



   {



   // TODO: add your custom metrics here



   return request_counter;



   }



   void initOpenTelemetry() {



   // You can import only the required method



   initLogger();



   initTracer();



   initMeter();



   }



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
3. Configure `DT_API_URL` and `DT_API_TOKEN` for the [Dynatrace URL](#base-url) and [access token](#access-token) in `otel.h`.

## Step 3 Instrument your application

To use OpenTelemetry, you first need to complete these two steps:

1. Add the necessary header files to your code.

   To add the header files, include `otel.h` wherever you want to make use of OpenTelemetry.

   ```
   #include "otel.h"
   ```
2. Initialize OpenTelemetry.

   For the initialization, use the `initOpenTelemetry` function in `otel.h` and call it early on in the startup code of your application.

### Add tracing

1. Get a reference to the tracer provider.

   ```
   auto provider = opentelemetry::trace::Provider::GetTracerProvider();
   ```
2. Obtain a tracer object.

   ```
   // In our case the GetTraces method takes the tracer name and returns the tracer provider



   auto tracer = provider->GetTracer(tracer_name);
   ```
3. With `tracer`, we can now start new spans and set them for the current execution scope.

   ```
   StartSpanOptions options;



   options.kind = SpanKind::kServer;



   auto span = tracer->StartSpan("Call to /myendpoint", {



   { "http.method", "GET" },



   { "net.protocol.version", "1.1" }



   }, options);



   auto scope = tracer->WithActiveSpan(span);



   // TODO: Your code goes here



   span->End();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `End()` method to complete the span

### Collect metrics

1. Get a reference to the meter provider.

   ```
   auto provider = metrics_api::Provider::GetMeterProvider();
   ```
2. Obtain a meter object.

   ```
   nostd::shared_ptr<metrics_api::Meter> meter = provider->GetMeter("my-meter", "1.0.1");
   ```
3. With `meter`, we can now create individual instruments, such as a counter.

   ```
   auto request_counter = meter->CreateUInt64Counter("request_counter");
   ```
4. We can now invoke the `Add()` method of `request_counter` to record new values with the counter and save additional attributes (for example, `action.type`).

   ```
   std::map<std::string, std::string> labels = { {"action.type", "create"} };



   auto labelkv = opentelemetry::common::KeyValueIterableView<decltype(labels)>{ labels };



   request_counter->Add(1, labelkv);
   ```

### Connect logs

1. Get a reference to the logger provider.

   ```
   auto provider = logs_api::Provider::GetLoggerProvider();
   ```
2. Call the provider's `GetLogger()` method to obtain a logger instance.

   ```
   auto logger = provider->GetLogger("scope_name", "", OPENTELEMETRY_SDK_VERSION);
   ```
3. Call any of the available logging methods to record a log statement. The following example logs a debug statement.

   ```
   logger->Debug("My debug statement here");
   ```

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

In the following examples, we assume that we are handling context propagation using the standard [W3C trace contextï»¿](https://www.w3.org/TR/trace-context/) headers, and we receive and set HTTP headers with the OpenTelemetry `http_client::Headers` object.

For that purpose, we use an instance of the class `HttpTextMapCarrier`, which we defined during the setup, and which is based on the OpenTelemetry class [`TextMapCarrier`ï»¿](https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/classopentelemetry_1_1context_1_1propagation_1_1TextMapCarrier.html#exhale-class-classopentelemetry-1-1context-1-1propagation-1-1textmapcarrier).

#### Extracting the context when receiving a request

To extract information on an existing context, we call the `Extract` method of the global propagator singleton and pass it the `HttpTextMapCarrier` instance, as well as the current context. This returns a new context object (`new_context`), which we allows us to continue the previous trace with our spans.

```
StartSpanOptions options;



options.kind          = SpanKind::kServer;



std::string span_name = request.uri;



// extract context from http header



std::map<std::string, std::string> &request_headers =



const_cast<std::map<std::string, std::string> &>(request.headers);



const HttpTextMapCarrier<std::map<std::string, std::string>> carrier(request_headers);



auto prop        = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();



auto current_ctx = context::RuntimeContext::GetCurrent();



auto new_context = prop->Extract(carrier, current_ctx);



options.parent   = GetSpan(new_context)->GetContext();



auto span = get_tracer("manual-server")



->StartSpan("my-server-span", { //TODO Replace with the name of your span



{"my-server-key-1", "my-server-value-1"} //TODO Add attributes



}, options);



auto scope = get_tracer("http_server")->WithActiveSpan(span);



for (auto &kv : request.headers)



{



span->SetAttribute("http.header." + std::string(kv.first.data()), kv.second);



}



span->AddEvent("Processing request");



response.headers[HTTP_SERVER_NS::CONTENT_TYPE] = HTTP_SERVER_NS::CONTENT_TYPE_TEXT;



response.body = doCall();



span->End();
```

#### Injecting the context when sending requests

For injecting current context information into an outbound request, we call the `Inject` method of the global propagator singleton and pass it the `HttpTextMapCarrier` instance, as well as the current context. This adds the applicable headers to the `carrier` instance, which we then use in the text step with our HTTP request.

```
auto http_client = http_client::HttpClientFactory::CreateSync();



std::string url  = std::getenv("URL"); // TODO set URL you want to call



CustomCounter(); // remove



// start active span



StartSpanOptions options;



options.kind = SpanKind::kClient;



opentelemetry::ext::http::common::UrlParser url_parser(url);



std::string span_name = url_parser.path_;



auto span = get_tracer("http-client")->StartSpan(span_name,



{{opentelemetry::semconv::url::kUrlFull, url_parser.url_},



{opentelemetry::semconv::url::kUrlScheme, url_parser.scheme_},



{opentelemetry::semconv::http::kHttpRequestMethod, "GET"}},



options);



auto scope = get_tracer("http-client")->WithActiveSpan(span);



// inject current context into http header



auto current_ctx = context::RuntimeContext::GetCurrent();



HttpTextMapCarrier<http_client::Headers> carrier;



auto prop = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();



prop->Inject(carrier, current_ctx);



// send http request



http_client::Result result = http_client->GetNoSsl(url, carrier.headers_);



//your code goes here



//then end span
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: dotnet.md


---
title: Instrument your .NET application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/dotnet
scraped: 2026-02-17T05:01:47.451090
---

# Instrument your .NET application with OpenTelemetry

# Instrument your .NET application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 14, 2023

This walkthrough shows how to add observability to your .NET application using the OpenTelemetry .NET libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Prerequisites

* Dynatrace version 1.254+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Choose how you want to instrument your application

For .NET, OpenTelemetry supports automatic and manual instrumentation (or a combination of both).

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 optional Automatically instrument your application Optional

.NET automatic instrumentation can be configured either during development or later after deployment.

Enrichment with OneAgent

It is currently not possible to [enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

During development

After deployment

1. Install [`OpenTelemetry.Extensions.Hosting`ï»¿](https://www.nuget.org/packages/OpenTelemetry.Extensions.Hosting).

   ```
   dotnet add package OpenTelemetry.Extensions.Hosting
   ```
2. Install the appropriate instrumentation library for your .NET framework (full list available [hereï»¿](https://www.nuget.org/packages?q=OpenTelemetry.Instrumentation)).

   ```
   dotnet add package OpenTelemetry.Instrumentation.[FRAMEWORK_NAME]
   ```

1. Download the [latest auto installerï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest) for the target operating system.
2. [Run (on Unix)ï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#shell-scripts) or [import (on Windows)ï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#powershell-module-windows) the auto installer, to install and set up all necessary auto instrumentation libraries.
3. Run your application.

In addition to the instrumentation setup above, you also need to configure the relevant export parameters with environment variables. This includes the [endpoint URL](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), the [authentication token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), and the [temporality preference for metrics](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.").

```
OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

## Step 4 optional Manually instrument your application Optional

### Setup

The setup steps slightly differ depending on whether you instrument a plain .NET application or an ASP.NET application.

.NET

ASP.NET

1. Install the following packages.

   ```
   dotnet add package Microsoft.Extensions.Logging



   dotnet add package OpenTelemetry.Extensions.Hosting



   dotnet add package OpenTelemetry



   dotnet add package OpenTelemetry.Api



   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
   ```
2. Add the following `using` statements to the startup class, which bootstraps your application.

   ```
   using OpenTelemetry;



   using OpenTelemetry.Trace;



   using OpenTelemetry.Exporter;



   using OpenTelemetry.Metrics;



   using OpenTelemetry.Logs;



   using OpenTelemetry.Resources;



   using OpenTelemetry.Context.Propagation;



   using System.Diagnostics;



   using System.Diagnostics.Metrics;



   using Microsoft.Extensions.Logging;
   ```
3. Add these fields to your startup class, with the first two containing the [access details](#dynatrace-docs--otlp-export), if you are using the OTLP export.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Add the `initOpenTelemetry` method to your startup class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry(IServiceCollection services)



   {



   List<KeyValuePair<string, object>> dt_metadata = new List<KeyValuePair<string, object>>();



   foreach (string name in new string[] {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"}) {



   try {



   foreach (string line in System.IO.File.ReadAllLines(name.StartsWith("/var") ? name : System.IO.File.ReadAllText(name))) {



   var keyvalue = line.Split("=");



   dt_metadata.Add( new KeyValuePair<string, object>(keyvalue[0], keyvalue[1]));



   }



   }



   catch { }



   }



   Action<ResourceBuilder> configureResource = r => r



   .AddService(serviceName: "dotnet-quickstart") //TODO Replace with the name of your application



   .AddAttributes(dt_metadata);



   services.AddOpenTelemetry()



   .ConfigureResource(configureResource)



   .WithTracing(builder => {



   builder



   .SetSampler(new AlwaysOnSampler())



   .AddSource(MyActivitySource.Name)



   .AddOtlpExporter(options =>



   {



   options.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/traces");



   options.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   options.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   });



   })



   .WithMetrics(builder => {



   builder



   .AddMeter("my-meter")



   .AddOtlpExporter((OtlpExporterOptions exporterOptions, MetricReaderOptions readerOptions) =>



   {



   exporterOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/metrics");



   exporterOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   exporterOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   readerOptions.TemporalityPreference = MetricReaderTemporalityPreference.Delta;



   });



   });



   var resourceBuilder = ResourceBuilder.CreateDefault();



   configureResource!(resourceBuilder);



   loggerFactoryOT = LoggerFactory.Create(builder => {



   builder



   .AddOpenTelemetry(options => {



   options.SetResourceBuilder(resourceBuilder).AddOtlpExporter(options => {



   options.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/logs");



   options.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   options.ExportProcessorType = OpenTelemetry.ExportProcessorType.Batch;



   options.Protocol = OtlpExportProtocol.HttpProtobuf;



   });



   })



   .AddConsole();



   });



   Sdk.CreateTracerProviderBuilder()



   .SetSampler(new AlwaysOnSampler())



   .AddSource(MyActivitySource.Name)



   .ConfigureResource(configureResource);



   // add-logging



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

1. Install the following packages.

   ```
   dotnet add package Microsoft.Extensions.Logging



   dotnet add package OpenTelemetry.Extensions.Hosting



   dotnet add package OpenTelemetry



   dotnet add package OpenTelemetry.Api



   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol



   dotnet add package OpenTelemetry.Instrumentation.AspNetCore



   dotnet add package OpenTelemetry.Instrumentation.Http



   dotnet add package OpenTelemetry.Instrumentation.Runtime
   ```
2. Add the following `using` statements to the startup class, which bootstraps your application.

   ```
   using OpenTelemetry;



   using OpenTelemetry.Trace;



   using OpenTelemetry.Exporter;



   using OpenTelemetry.Metrics;



   using OpenTelemetry.Logs;



   using OpenTelemetry.Resources;



   using OpenTelemetry.Context.Propagation;



   using System.Diagnostics;



   using System.Diagnostics.Metrics;



   using Microsoft.Extensions.Logging;



   using OpenTelemetry.Instrumentation.AspNetCore;
   ```
3. Add these fields to your startup class, with the first two containing the [access details](#dynatrace-docs--otlp-export), if you are using the OTLP export.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Add the `initOpenTelemetry` method to your startup class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry(){



   var port = System.Environment.GetEnvironmentVariable("PORT") ?? "8080";



   var appBuilder = WebApplication.CreateBuilder();



   appBuilder.WebHost.ConfigureKestrel(options =>{



   options.ListenAnyIP(Convert.ToInt32(port)); // hardcoding the port



   });



   List<KeyValuePair<string, object>> dt_metadata = new List<KeyValuePair<string, object>>();



   foreach (string name in new string[] {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"}) {



   try {



   foreach (string line in System.IO.File.ReadAllLines(name.StartsWith("/var") ? name : System.IO.File.ReadAllText(name))) {



   var keyvalue = line.Split("=");



   dt_metadata.Add( new KeyValuePair<string, object>(keyvalue[0], keyvalue[1]));



   }



   }



   catch { }



   }



   Action<ResourceBuilder> configureResource = r => r



   .AddService(serviceName: "dotnetManual") //TODO Replace with the name of your application



   .AddAttributes(dt_metadata);



   appBuilder.Services.AddOpenTelemetry()



   .ConfigureResource(configureResource)



   .WithTracing(builder =>{



   appBuilder.Services.Configure<AspNetCoreTraceInstrumentationOptions>(appBuilder.Configuration.GetSection("AspNetCoreInstrumentation"));



   builder



   .AddSource(MyActivitySource.Name)



   .SetSampler(new AlwaysOnSampler())



   .AddHttpClientInstrumentation()



   .AddAspNetCoreInstrumentation()



   .AddOtlpExporter(otlpOptions =>{



   otlpOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/traces");



   otlpOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   otlpOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   });



   })



   .WithMetrics(builder =>{



   builder



   .AddMeter("my-meter")



   // .AddMeter(Instrumentation.MeterName)



   .AddRuntimeInstrumentation()



   .AddHttpClientInstrumentation()



   .AddAspNetCoreInstrumentation()



   .AddOtlpExporter((OtlpExporterOptions exporterOptions, MetricReaderOptions readerOptions) => {



   exporterOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/metrics");



   exporterOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   exporterOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   readerOptions.TemporalityPreference = MetricReaderTemporalityPreference.Delta;



   });



   appBuilder.Logging.ClearProviders();



   appBuilder.Logging.AddOpenTelemetry(options =>



   {



   var resourceBuilder = ResourceBuilder.CreateDefault();



   configureResource(resourceBuilder);



   options.SetResourceBuilder(resourceBuilder);



   options.AddOtlpExporter(otlpOptions => {



   otlpOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/logs");



   otlpOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   otlpOptions.ExportProcessorType = OpenTelemetry.ExportProcessorType.Batch;



   otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;



   });



   });



   appBuilder.Services.AddControllers();



   appBuilder.Services.AddEndpointsApiExplorer();



   var app = appBuilder.Build();



   app.MapControllers();



   app.Run();



   });



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

### Add tracing

Using `MyActivitySource` from the [setup step](#setup), we can now start new activities (traces):

```
using var activity = Startup.MyActivitySource.StartActivity("Call to /myendpoint", ActivityKind.Consumer, parentContext.ActivityContext);



activity?.SetTag("http.method", "GET");



activity?.SetTag("net.protocol.version", "1.1");
```

In the above code, we:

* Create a new activity (span) and name it "Call to /myendpoint"
* Add two tags (attributes), following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version

The activity will be automatically set as the current and active span until the execution flow leaves the current method scope. Subsequent activities will automatically become child spans.

### Collect metrics

1. To instantiate new metric instruments, we first need a meter object.

   ```
   private static readonly Meter meter = new Meter("my-meter", "1.0.0");  //TODO Replace with the name of your meter
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   private static readonly Counter<long> counter = meter.CreateCounter<long>("request_counter");
   ```
3. We can now invoke the `Add()` method of `counter` to record new values with our counter and save additional attributes (for example, `action.type`).

   ```
   counter.Add(1, new("ip", "an ip address here"), new("some other key", "some other value"));
   ```

### Connect logs

With the `loggerFactoryOT` variable, we initialized under [Setup](#setup), we can now create individual logger instances, which will pass logged information straight to the configured OpenTelemetry endpoint at Dynatrace.

```
var logger = loggerFactoryOT.CreateLogger<Startup>();



services.AddSingleton<ILoggerFactory>(loggerFactoryOT);



services.AddSingleton(logger);



logger.LogInformation(eventId: 123, "Log line");
```

### Ensure context propagation Optional

[Context propagation](/docs/ingest-from/opentelemetry#context-propagation "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

In the following example, we assume that we have received a network call via `System.Web.HttpRequest` and we define a `CompositeTextMapPropagator` instance to fetch the context information from the HTTP headers. We then pass that instance to `Extract()`, returning the context object, which allows us to continue the previous trace with our spans.

```
private CompositeTextMapPropagator propagator = new CompositeTextMapPropagator(new TextMapPropagator[] {



new TraceContextPropagator(),



new BaggagePropagator(),



});



private static readonly Func<HttpRequest, string, IEnumerable<string>> valueGetter = (request, name) => request.Headers[name];



var parentContext = propagator.Extract(default, HttpContext.Request, valueGetter);



using var activity = MyActivitySource.StartActivity("my-span", ActivityKind.Consumer, parentContext.ActivityContext);
```

#### Injecting the context when sending requests

In the following example, we send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we define a `TextMapPropagator` instance, which adds the respective information. Once we have instantiated our REST object, we pass it, along with the context and the setter instance, to `Inject()`, which will add the necessary headers to the request.

```
private CompositeTextMapPropagator propagator = new CompositeTextMapPropagator(new TextMapPropagator[] {



new TraceContextPropagator(),



new BaggagePropagator()



});



private static Action<HttpRequestMessage, string, string> _headerValueSetter => (request, name, value) => {



request.Headers.Remove(name);



request.Headers.Add(name, value);



};



propagator.Inject(new PropagationContext(activity!.Context, Baggage.Current), request, _headerValueSetter);
```

## Step 5 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: erlang.md


---
title: Instrument your Erlang application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/erlang
scraped: 2026-02-17T21:33:55.810642
---

# Instrument your Erlang application with OpenTelemetry

# Instrument your Erlang application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Erlang application using the OpenTelemetry Erlang libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | No |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Set up OpenTelemetry

1. Add the current versions of the [following dependenciesï»¿](https://hex.pm/packages?search=opentelemetry&sort=recent_downloads) to `rebar.config`.

   ```
   {deps, [



   %TODO add any additional dependancies here



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter



   ]}.
   ```
2. Add the following dependencies to your `.app.src` file in the `src` directory.

   ```
   {applications, [kernel,



   stdlib,



   opentelemetry_api,



   opentelemetry,



   opentelemetry_exporter]}
   ```
3. Add the following configuration to `config/sys.config` and replace `[URL]` and `[TOKEN]` with the respective values for the [Dynatrace URL](#base-url) and [access token](#access-token).

   ```
   [



   {otel_getting_started, []},



   {opentelemetry,



   [{span_processor, batch},



   {traces_exporter, otlp},



   {resource,



   [{service,



   #{name => "erlang-quickstart", version => "1.0.1"} %%TODO Replace with the name and version of your application



   }]



   },



   {resource_detectors, [



   otel_resource_env_var,



   otel_resource_app_env,



   extra_metadata



   ]}



   ]



   },



   {opentelemetry_exporter,



   [{otlp_protocol, http_protobuf},



   {otlp_traces_endpoint, "[URL]"}, %%TODO Replace [URL] to your SaaS/Managed URL as mentioned in the next step



   {otlp_headers, [{"Authorization", "Api-Token [TOKEN]"}]} %%TODO Replace [TOKEN] with your API Token as mentioned in the next step



   ]}



   ].
   ```
4. Save the following code to `src/extra_metadata.erl`.

   ```
   -module(extra_metadata).



   -behaviour(otel_resource_detector).



   -export([get_resource/1]).



   get_resource(_) ->



   Metadata = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_metadata.properties")), []),



   {ok, MetadataFilePath} = file:read_file("dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties"),



   Metadata2 = otel_resource:create(otel_resource_app_env:parse(get_metadata(MetadataFilePath)), []),



   Metadata3 = otel_resource:create(otel_resource_app_env:parse(get_metadata("/var/lib/dynatrace/enrichment/dt_host_metadata.properties")), []),



   otel_resource:merge(otel_resource:merge(Metadata, Metadata2), Metadata3),



   otel_resource:merge(Metadata, Metadata2).



   get_metadata(FileName) ->



   try



   {ok, MetadataFile} = file:read_file(FileName),



   Lines = binary:split(MetadataFile, <<"\n">>, [trim, global]),



   make_tuples(Lines, [])



   catch _:_ -> "Metadata not found, safe to continue"



   end.



   make_tuples([Line|Lines], Acc) ->



   [Key, Value] = binary:split(Line, <<"=">>),



   make_tuples(Lines, [{Key, Value}|Acc]);



   make_tuples([], Acc) -> Acc.
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

## Step 3 Instrument your application

### Add tracing

Spans are started with the macro [`with_span`ï»¿](https://hexdocs.pm/opentelemetry_api/OpenTelemetry.Tracer.html#with_span/3) and accept an optional list of span attributes, as well as the code block for this span. The span will automatically finish when the code block returns.

```
-export([init/2]).



-include_lib("opentelemetry_api/include/otel_tracer.hrl").



-include_lib("opentelemetry/include/otel_resource.hrl").



init( Req, State ) ->



?with_span(<<"parent_span">>, #{attributes => [ %%TODO Add span name



{<<"my-key-1">>, <<"my-value-1">>}] %%TODO Add attributes at span creation



}, fun child_function/1),



%% Your code goes here



child_function(_SpanCtx) ->



?with_span(<<"child_span">>, #{},



fun(_ChildSpanCtx) ->



?set_attributes([{<<"child-key-1">>, <<"child-value-1">>}]) %%TODO Add attributes after span creation



end).
```

### Collect metrics

No example yet, as OpenTelemetry for Erlang does not have stable support for metrics yet.

### Connect logs

No example yet, as OpenTelemetry for Erlang does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

For extracting information on an existing context, we pass the headers to the `otel_propagator_text_map.extract` function, which parses the context information provided by the headers and sets the current context based on that.

```
%% Get Headers from incoming request



Headers = maps:get(headers, Req),



otel_propagator_text_map:extract(maps:to_list(Headers)),



SpanCtx = ?start_span(<<"span-name">>),



%% As we used `otel_propagator_text_map` the current context is from the parent span



Ctx = otel_ctx:get_current(),



proc_lib:spawn_link(fun() ->



%% Start span and set as current



otel_ctx:attach(Ctx),



?set_current_span(SpanCtx),



%% Create response



Resp = cowboy_req:reply(



200,



#{<<"content-type">> => <<"application/json">>},



<<"{\"message\": \"hello world\"}">>,



Req



),



{ok, Resp, State},



?end_span(SpanCtx)
```

#### Injecting the context when sending requests

The following example uses `otel_propagator_text_map:inject` to provide the HTTP headers (necessary for context propagation) in `NewHeaders`, which we eventually merge with the existing header object `Headers` and pass to the `httpc:request` call, which allows the receiving endpoint to continue the trace with the provided information.

```
?with_span(<<"span-name">>, #{},



fun(_ChildSpanCtx) ->



%% A custom header example



Headers = [{"content-type", "application/json"}, {"X-Custom-Header", "some-value"}],



%% We convert the traceparent information and merge the 2 headers as



%% Httpc:request requires tuples of strings



Tmp = [],



NewHeaders = headers_list(otel_propagator_text_map:inject(opentelemetry:get_text_map_injector(), Tmp)),



MergedHeaders = lists:append(Headers, NewHeaders),



{ok, Res} = httpc:request(get, {URL, MergedHeaders}, [], []),



io:format("Response: ~p~n", [Res])



end).



headers_list(Headers) ->



[{binary_to_list(Name), binary_to_list(Value)} || {Name, Value} <- Headers].
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: go.md


---
title: Instrument your Go application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/go
scraped: 2026-02-16T21:24:14.547867
---

# Instrument your Go application with OpenTelemetry

# Instrument your Go application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Go application using the OpenTelemetry Go libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Choose how you want to instrument your application

OpenTelemetry supports on Go automatic and manual instrumentation, or a combination of both.

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 Initialize OpenTelemetry

1. Add the following import statements.

   ```
   import (



   "context"



   "github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



   "go.opentelemetry.io/otel"



   "go.opentelemetry.io/otel/attribute"



   "go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp"



   "go.opentelemetry.io/otel/propagation"



   "go.opentelemetry.io/otel/trace"



   sdkmetric "go.opentelemetry.io/otel/sdk/metric"



   "go.opentelemetry.io/otel/sdk/metric/metricdata"



   "go.opentelemetry.io/otel/sdk/resource"



   sdktrace "go.opentelemetry.io/otel/sdk/trace"



   semconv "go.opentelemetry.io/otel/semconv/v1.20.0"



   "log"



   "time"



   "log/slog"



   "go.opentelemetry.io/contrib/bridges/otelslog"



   "go.opentelemetry.io/otel/log/global"



   sdklog "go.opentelemetry.io/otel/sdk/log"



   )
   ```
2. Run Go's [`mod tidy` commandï»¿](https://go.dev/ref/mod#go-mod-tidy) to install the dependencies.

   ```
   go mod tidy
   ```
3. Add the following code to your startup file and provide the [respective values](#get-the-dynatrace-access-details) for `DT_API_HOST` and `DT_API_TOKEN`.

   * `DT_API_HOST` should contain only the hostname of your Dynatrace URL (for example, `XXXXX.live.dynatrace.com`); it is not a URL and must not contain any schemas or paths
   * `DT_API_TOKEN` should contain the access token

   ```
   func InitOpenTelemetry() {



   // ===== GENERAL SETUP =====



   DT_API_HOST := "" // Only the host part of your Dynatrace URL



   DT_API_BASE_PATH := "/api/v2/otlp"



   DT_API_TOKEN := ""



   authHeader := map[string]string{"Authorization": "Api-Token " + DT_API_TOKEN}



   ctx := context.Background()



   oneagentsdk := sdk.CreateInstance()



   dtMetadata := oneagentsdk.GetEnrichmentMetadata()



   var attributes []attribute.KeyValue



   for k, v := range dtMetadata {



   attributes = append(attributes, attribute.KeyValue{Key: attribute.Key(k), Value: attribute.StringValue(v)})



   }



   attributes = append(attributes,



   semconv.ServiceNameKey.String("go-quickstart"), //TODO Replace with the name of your application



   semconv.ServiceVersionKey.String("1.0.1"),      //TODO Replace with the version of your application



   )



   res, err := resource.New(ctx, resource.WithAttributes(attributes...))



   if err != nil {



   log.Fatalf("Failed to create resource: %v", err)



   }



   // ===== TRACING SETUP =====



   exporter, err := otlptracehttp.New(



   ctx,



   otlptracehttp.WithEndpoint(DT_API_HOST),



   otlptracehttp.WithURLPath(DT_API_BASE_PATH+"/v1/traces"),



   otlptracehttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   tp := sdktrace.NewTracerProvider(



   sdktrace.WithResource(res),



   sdktrace.WithSampler(sdktrace.AlwaysSample()),



   sdktrace.WithBatcher(exporter),



   )



   otel.SetTracerProvider(tp)



   otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))



   // ===== METRIC SETUP =====



   var deltaTemporalitySelector = func(sdkmetric.InstrumentKind) metricdata.Temporality { return metricdata.DeltaTemporality }



   metricsExporter, err := otlpmetrichttp.New(



   ctx,



   otlpmetrichttp.WithEndpoint(DT_API_HOST),



   otlpmetrichttp.WithURLPath(DT_API_BASE_PATH+"/v1/metrics"),



   otlpmetrichttp.WithHeaders(authHeader),



   otlpmetrichttp.WithTemporalitySelector(deltaTemporalitySelector),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   mp := sdkmetric.NewMeterProvider(



   sdkmetric.WithResource(res),



   sdkmetric.WithReader(sdkmetric.NewPeriodicReader(metricsExporter, sdkmetric.WithInterval(2*time.Second))),



   )



   otel.SetMeterProvider(mp)



   // ===== LOG SETUP =====



   logExporter, err := otlploghttp.New(



   ctx,



   otlploghttp.WithEndpoint(DT_API_HOST),



   otlploghttp.WithURLPath(DT_API_BASE_PATH+"/v1/logs"),



   otlploghttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   lp := sdklog.NewLoggerProvider(



   sdklog.WithProcessor(sdklog.NewBatchProcessor(logExporter)),



   sdklog.WithResource(res),



   )



   global.SetLoggerProvider(lp)



   logger := otelslog.NewLogger("my-logger-scope", otelslog.WithLoggerProvider(lp))



   slog.SetDefault(logger) // here we are overwriting the sdtout to http logger exporter



   }
   ```
4. Make sure to call `InitOpenTelemetry` as early as possible in your startup code to initialize OpenTelemetry.

## Step 4 optional Automatically instrument your application Optional

1. Browse the [OpenTelemetry registryï»¿](https://opentelemetry.io/ecosystem/registry/?language=go&component=instrumentation) and pick the instrumentation libraries matching your application libraries.
2. Add the relevant packages to your import statements.

   ```
   import (



   "go.opentelemetry.io/[PACKAGE]"



   )
   ```
3. Run Go's [`mod tiny` commandï»¿](https://go.dev/ref/mod#go-mod-tidy) to install the dependencies.

   ```
   go mod tidy
   ```
4. Wrap your existing code with calls to the support libraries.

### Example for `net/http`

1. Install the [instrumentation library for `net/http`ï»¿](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp).
2. Add the package to your import statements.

   ```
   import (



   // other packages



   "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



   )
   ```
3. Wrap your HTTP handler function.

   ```
   handler := http.HandlerFunc(httpHandler)



   wrappedHandler := otelhttp.NewHandler(handler, "my-span") //TODO Replace with the name of your span



   //Use the wrappedHandler with your handle



   http.Handle("/", wrappedHandler)
   ```

## Step 5 Manually instrument your application

### Add tracing

1. You first need to get a tracer object.

   ```
   tracer := otel.Tracer("my-tracer")
   ```
2. With `tracer`, you can now use a span builder to create and start new spans.

   ```
   _, span := tracer.Start(r.Context(), "Call to /myendpoint")



   defer span.End()



   span.SetAttributes(attribute.String("http.method", "GET"), attribute.String("net.protocol.version", "1.1"))



   // TODO your code goes here
   ```

   In the code above, we:

   * Create a new span and name it "Call to /myendpoint"
   * Schedule a deferred call to `End()`, to ensure the span is properly closed when the function returns
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic

### Collect metrics

1. Obtain a meter object.

   ```
   meter := otel.Meter("my-meter")
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   requestCounter, _ := meter.Int64Counter("request_counter")
   ```
3. Now we can invoke the `Add()` method of `requestCounter` to record new values with the counter.

   ```
   requestCounter.Add(context.Background(), 1)
   ```

### Connect logs

With OpenTelemetry logging initialized in `InitOpenTelemetry()` and set as default logger for [slogï»¿](https://pkg.go.dev/log/slog), we can now call any of slog's log functions (for example, [`Info()`ï»¿](https://pkg.go.dev/log/slog#Info)) to send our log information to Dynatrace.

```
slog.Info("an info message")



slog.Debug("a debug message")



slog.Error("an error")
```

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

In the following example, we assume that we have received a network call via the [`net/http`ï»¿](https://pkg.go.dev/net/http) library and its [`Request`ï»¿](https://pkg.go.dev/net/http#Request) type.

To obtain a handle to the original context (which was provided by the calling service), we pass the HTTP header object (`r.Header`) to the `Extract` function of the global propagator singleton, which instantiates that context and returns in `parentCtx`. This allows us to continue the previous trace with our own spans.

```
func httpHandler(w http.ResponseWriter, r *http.Request) {



parentCtx := otel.GetTextMapPropagator().Extract(r.Context(), propagation.HeaderCarrier(r.Header))



tracer := otel.Tracer("my-tracer")



ctx, span := tracer.Start(



parentCtx,



"manual-server", //TODO Replace with the name of your span



trace.WithAttributes(



attribute.String("my-key-1", "my-value-1"), //TODO Add attributes



),



)



defer span.End()



//TODO your code goes here



}
```

#### Injecting the context when sending requests

In the following example, we set up a new instance of [`Request`ï»¿](https://pkg.go.dev/net/http#Request) and pass the object to the `Inject` call of the global propagator singleton. This adds the necessary HTTP headers to the request object, which we eventually pass to `Do` to execute the network request.

```
client := http.Client{}



req, err := http.NewRequest("<method>", "<url>", <body>)



if err != nil {



// TODO handle error



}



//Method to inject the current context in the request headers



otel.GetTextMapPropagator().Inject(ctx, propagation.HeaderCarrier(req.Header))



client.Do(req) // Your call goes here
```

## Step 6 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 7 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: java.md


---
title: Instrument your Java application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/java
scraped: 2026-02-17T21:31:06.694426
---

# Instrument your Java application with OpenTelemetry

# Instrument your Java application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 1-min read
* Published Apr 18, 2023

These walkthroughs show how to add observability to your Java application using the OpenTelemetry Java libraries and tools.

* [Automatically instrument your Java application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/java/java-auto "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")
* [Manually instrument your Java application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/java/java-manual "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")

The following features are currently supported by OpenTelemetry Java.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: nodejs.md


---
title: Instrument your JavaScript application on Node.js with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/nodejs
scraped: 2026-02-17T05:07:08.426197
---

# Instrument your JavaScript application on Node.js with OpenTelemetry

# Instrument your JavaScript application on Node.js with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 14, 2023

This walkthrough shows how to add observability to your JavaScript application using the OpenTelemetry JavaScript libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Initialize OpenTelemetry

1. Run the following `npm` command to install the necessary libraries and dependencies.

   ```
   npm install \



   @opentelemetry/api \



   @opentelemetry/exporter-metrics-otlp-proto \



   @opentelemetry/exporter-trace-otlp-proto \



   @opentelemetry/instrumentation \



   @opentelemetry/resources \



   @opentelemetry/sdk-metrics \



   @opentelemetry/sdk-trace-node \



   @opentelemetry/semantic-conventions
   ```

   Depending on the libraries your application is using, there may be also additional instrumentation support libraries that you want to add to the dependencies. A list of support libraries can be found [hereï»¿](https://www.npmjs.com/search?q=%40opentelemetry%2Finstrumentation). Common examples would be [@opentelemetry/instrumentation-httpï»¿](https://www.npmjs.com/package/@opentelemetry/instrumentation-http) and [@opentelemetry/instrumentation-netï»¿](https://www.npmjs.com/package/@opentelemetry/instrumentation-net) for the HTTP and network libraries.
2. Create a file named `otel.js` in your application directory and save the following content.

   ```
   const opentelemetry = require("@opentelemetry/api");



   const { resourceFromAttributes, emptyResource, defaultResource } = require("@opentelemetry/resources");



   const { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } = require("@opentelemetry/semantic-conventions");



   const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");



   const { registerInstrumentations } = require("@opentelemetry/instrumentation");



   const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



   const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



   const { OTLPMetricExporter } = require("@opentelemetry/exporter-metrics-otlp-proto");



   const { MeterProvider, PeriodicExportingMetricReader, AggregationTemporality } = require('@opentelemetry/sdk-metrics');



   const DT_API_URL = ''; // TODO: Provide your SaaS/Managed URL here



   const DT_API_TOKEN = ''; // TODO: Provide the OpenTelemetry-scoped access token here



   // ===== GENERAL SETUP =====



   registerInstrumentations({



   instrumentations: [ /* TODO Register your auto-instrumentation libraries here */ ],



   });



   const fs = require("fs");



   let dtmetadata = emptyResource();



   for (let name of ['dt_metadata_e617c525669e072eebe3d0f08212e8f2.json', '/var/lib/dynatrace/enrichment/dt_metadata.json', '/var/lib/dynatrace/enrichment/dt_host_metadata.json']) {



   try {



   dtmetadata = dtmetadata.merge(



   resourceFromAttributes(JSON.parse(fs.readFileSync(name.startsWith("/var") ?



   name : fs.readFileSync(name).toString('utf-8').trim()).toString('utf-8'))));



   break



   } catch { }



   }



   const resource =



   defaultResource().merge(



   resourceFromAttributes({



   [ATTR_SERVICE_NAME]: "js-agent",



   [ATTR_SERVICE_VERSION]: "0.1.0",



   })



   ).merge(dtmetadata);



   // ===== TRACING SETUP =====



   const exporter = new OTLPTraceExporter({



   url: DT_API_URL + '/v1/traces',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN }



   });



   const processor = new BatchSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: resource,



   spanProcessors: [ processor ]



   });



   provider.register();



   // ===== METRIC SETUP =====



   const metricExporter = new OTLPMetricExporter({



   url: DT_API_URL + '/v1/metrics',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN },



   temporalityPreference: AggregationTemporality.DELTA



   });



   const metricReader = new PeriodicExportingMetricReader({



   exporter: metricExporter,



   exportIntervalMillis: 3000



   });



   const meterProvider = new MeterProvider({



   resource: resource,



   readers: [ metricReader ]



   });



   // Set this MeterProvider to be global to the app being instrumented.



   opentelemetry.metrics.setGlobalMeterProvider(meterProvider);
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
3. If you export using OTLP, configure the two variables `DT_API_URL` and `DT_API_TOKEN` in `otel.js` with their [respective values](#dynatrace-docs--otlp-export).

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Adjust the Node.js call for your application to include the [ârequireï»¿](https://nodejs.org/api/cli.html#-r---require-module) command line parameter and point it towards `otel.js`.

   ```
   node --require ./otel.js ./myapplication.js
   ```

## Step 3 Manually instrument your application

### Add tracing

1. Obtain a reference to the OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Now we can get a tracer object.

   ```
   const tracer = opentelemetry.trace.getTracer('my-tracer');
   ```
3. With `tracer`, we can use a span builder to create and start new spans.

   ```
   const span = tracer.startSpan('Call to /myendpoint');



   span.setAttribute('http.method', 'GET');



   span.setAttribute('net.protocol.version','1.1');



   // TODO your code goes here



   span.end();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `end()` method to complete the span

### Collect metrics

1. As with tracing, we first need to get a reference to the OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Next, we need to obtain a meter object.

   ```
   const meter = opentelemetry.metrics.getMeter('my-meter');
   ```
3. With `meter`, we can now create individual instruments, such as a counter.

   ```
   const requestCounter = meter.createCounter('request_counter', {



   description: 'The number of requests we received'



   });
   ```
4. We can now invoke the `add()` method of `requestCounter` to record new values with the counter and save additional attributes (for example, `action.type`).

   ```
   requestCounter.add(1, { 'action.type': 'create' });
   ```

You can also create an asynchronous gauge, which requires a callback function that will be invoked by OpenTelemetry upon data collection.

The following example records on each invocation the available memory:

```
const gauge = meter.createObservableGauge('free_memory');



gauge.addCallback(r => {



r.observe(require('os').freemem());



});
```

### Connect logs

No example yet, as OpenTelemetry for Node.js does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

The following examples assume that we received a network call via [`ClientRequest`ï»¿](https://nodejs.org/api/http.html#class-httpclientrequest) and uses `extract()` to create the context object `remoteCtx`, based on the context information received from the HTTP headers. This allows us to continue the previous trace with our spans.

```
//Extract context from incoming headers



const { SpanKind, ROOT_CONTEXT } = require("@opentelemetry/api");



const remoteCtx = opentelemetry.propagation.extract(ROOT_CONTEXT, req.headers);



const serverSpan = opentelemetry.trace.getTracer('my-server-tracer')



.startSpan('my-server-span', {



kind: SpanKind.SERVER,



attributes: {



'my-server-key-1': 'my-server-value-1'



},



}, remoteCtx);
```

#### Injecting the context when sending requests

In the following example, we use the [axiosï»¿](https://www.npmjs.com/package/axios) HTTP client to send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we create a `ctx` object, pass it the current span, and mark it as active. Then we pass that context object and an empty `my_headers` object to `inject()` and, once the call is returned, we have the appropriate headers in `my_headers`, which we can eventually pass to our HTTP call.

```
const ctx = opentelemetry.trace.setSpan(



opentelemetry.context.active(),



serverSpan



);



const my_headers = {};



opentelemetry.propagation.inject(ctx, my_headers);



await axios.get(URL, {headers: my_headers});



serverSpan.end();
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: python.md


---
title: Instrument your Python application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/python
scraped: 2026-02-17T21:24:05.212095
---

# Instrument your Python application with OpenTelemetry

# Instrument your Python application with OpenTelemetry

* Latest Dynatrace
* Overview
* 1-min read
* Published Apr 18, 2023

These walkthroughs show how to add observability to your Python application using the OpenTelemetry Python libraries and tools.

* [Automatically instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python/python-auto "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")
* [Manually instrument your Python application with OpenTelemetry](/docs/ingest-from/opentelemetry/walkthroughs/python/python-manual "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")

The following features are currently supported by OpenTelemetry Python.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")
* [Get started](/docs/observe/dynatrace-for-ai-observability/get-started "Learn how to set up OpenLLMetry to observe an AI/ML model.")


---


## Source: ruby.md


---
title: Instrument your Ruby application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/ruby
scraped: 2026-02-17T04:51:46.831609
---

# Instrument your Ruby application with OpenTelemetry

# Instrument your Ruby application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Oct 23, 2025

This walkthrough shows how to add observability to your Ruby application using the OpenTelemetry Ruby libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | No |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Choose how you want to instrument your application

OpenTelemetry supports on Ruby automatic and manual instrumentation, or a combination of both.

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 Initialize OpenTelementry

1. Add the following dependencies to your Gemfile.

   ```
   gem 'opentelemetry-sdk'



   gem 'opentelemetry-exporter-otlp'
   ```
2. Add the following `require` declaration.

   ```
   require 'opentelemetry/sdk'



   require 'opentelemetry/exporter/otlp'
   ```
3. Add the `init_opentelemetry` function to startup code and provide the variables `DT_API_URL` and `DT_API_TOKEN` with the values for the [Dynatrace URL](#base-url) and [access token](#access-token).

   ```
   DT_API_URL = ENV['DT_API_URL']



   DT_API_TOKEN = ENV['DT_API_TOKEN']



   def init_opentelemetry



   OpenTelemetry::SDK.configure do |c|



   c.service_name = 'ruby-quickstart' #TODO Replace with the name of your application



   c.service_version = '1.0.1' #TODO Replace with the version of your application



   # TODO: add automatic instrumentation here (step 3 - optional)



   for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties", "/var/lib/dynatrace/enrichment/dt_metadata.properties", "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"] do



   begin



   c.resource = OpenTelemetry::SDK::Resources::Resource.create(Hash[*File.read(name.start_with?("/var") ? name : File.read(name)).split(/[=\n]+/)])



   rescue



   end



   end



   c.add_span_processor(



   OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(



   OpenTelemetry::Exporter::OTLP::Exporter.new(



   endpoint: DT_API_URL + "/v1/traces",



   headers: {



   "Authorization": "Api-Token " + DT_API_TOKEN



   }



   )



   )



   )



   end



   end
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

   Exporting to OneAgent

   The Ruby SDK uses content compression by default, which is not supported by OneAgent yet.

   When exporting to OneAgent, add `compression: "none"` to the `Exporter.new()` call to disable that feature. Otherwise, [export to ActiveGate](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") instead.
4. Call `init_opentelemetry` as early as possible during the startup of your application to ensure OpenTelemetry is initialized right from the start.

## Step 3 optional Automatically instrument your application Optional

1. Add the following dependency to your Gemfile.

   ```
   gem 'opentelemetry-instrumentation-all'
   ```
2. Add the following `require` declaration.

   ```
   require 'opentelemetry/instrumentation/all'
   ```
3. Add the following line after `c.service_version` in the `init_opentelemetry` function.

   ```
   c.use_all
   ```

## Step 4 optional Manually instrument your application Optional

### Add tracing

1. To create new spans, we first need a tracer object.

   ```
   tracer = OpenTelemetry.tracer_provider.tracer('my-tracer')
   ```
2. With `tracer`, we can now use `start_span()` to create and start new spans.

   ```
   span = tracer.start_span("Call to /myendpoint", kind: :internal)



   OpenTelemetry::Trace.with_span(span) do |span, context|



   span.set_attribute("http.method", "GET")



   span.set_attribute("net.protocol.version", "1.1")



   # TODO your code goes here



   end



   rescue Exception => e



   span&.record_exception(e)



   span&.status = OpenTelemetry::Trace::Status.error("Unhandled exception of type: #{e.class}")



   raise e



   ensure



   span&.finish
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `finish()` method to complete the span (in an `ensure` block to ensure the method is called)

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Collect metrics

No example yet, as OpenTelemetry for Ruby does not have stable support for metrics yet.

### Connect logs

No example yet, as OpenTelemetry for Ruby does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

The following example uses the default propagator's `extract()` method to extract and recreate the context from the request, in `parent_context`. We can then pass that context to a `start_span` call to continue the previous trace with our spans.

```
parent_context = OpenTelemetry.propagation.extract(



env,



getter: OpenTelemetry::Common::Propagation.rack_env_getter



)



span = tracer.start_span("hello world", with_parent: parent_context)



OpenTelemetry::Trace.with_span(span) do |span, context|



span.set_attribute("my-key-1", "my-value-1")



# ... expansive query



end



ensure



span&.finish



end
```

#### Injecting the context when sending requests

The following example uses Ruby's standard [Net:HTTPï»¿](https://ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html) library to call an instrumented third-party service. To add the necessary trace headers, we use the default propagator's `inject()` method.

```
request = Net::HTTP::Get.new(uri.request_uri)



OpenTelemetry.propagation.inject(request)



response = http.request(request)
```

## Step 5 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: rust.md


---
title: Instrument your Rust application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/rust
scraped: 2026-02-17T04:51:44.061499
---

# Instrument your Rust application with OpenTelemetry

# Instrument your Rust application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 07, 2026

This walkthrough shows how to add observability to your Rust application using the OpenTelemetry Rust libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Set up OpenTelemetry

1. Add the following crates to your `Cargo.toml` file.

   ```
   opentelemetry = { version = "~0", features = ["trace", "metrics"] }



   opentelemetry_sdk = { version = "~0", features = ["rt-tokio", "metrics", "logs", "spec_unstable_metrics_views"] }



   opentelemetry-otlp = { version = "~0", features = ["http-proto", "http-json", "logs", "reqwest-blocking-client", "reqwest-rustls"] }



   opentelemetry-http = { version = "~0" }



   opentelemetry-appender-log = { version = "~0" }



   opentelemetry-semantic-conventions = { version = "~0" }
   ```
2. Add the following `use` declarations to your code.

   ```
   use std::{env, convert::Infallible, net::SocketAddr, collections::HashMap, io::{BufRead, BufReader, Read}};



   use opentelemetry_sdk::trace::SdkTracerProvider;



   use opentelemetry_sdk::{logs::SdkLoggerProvider, metrics::{PeriodicReader, SdkMeterProvider}, propagation::TraceContextPropagator, Resource};



   use opentelemetry_otlp::{LogExporter, MetricExporter, Protocol, SpanExporter, WithExportConfig, WithHttpConfig};



   use opentelemetry_semantic_conventions::trace;



   use opentelemetry_http::{Bytes, HeaderExtractor, HeaderInjector};



   use opentelemetry_appender_log::OpenTelemetryLogBridge;



   use opentelemetry::{global, trace::{FutureExt, Span, SpanKind, TraceContextExt, Tracer}, Context, KeyValue};
   ```
3. Add the following function to your startup file.

   ```
   fn init_opentelemetry() {



   // Helper function to read potentially available OneAgent data



   fn read_dt_metadata() ->  Vec<KeyValue> {



   fn read_single(path: &str, metadata: &mut Vec<KeyValue>) -> std::io::Result<()> {



   let mut file = std::fs::File::open(path)?;



   if path.starts_with("dt_metadata") {



   let mut name = String::new();



   file.read_to_string(&mut name)?;



   file = std::fs::File::open(name)?;



   }



   for line in BufReader::new(file).lines() {



   if let Some((k, v)) = line?.split_once('=') {



   metadata.push(KeyValue::new(k.to_string(), v.to_string()))



   }



   }



   Ok(())



   }



   let mut metadata = Vec::new();



   for name in [



   "dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"



   ] {



   let _ = read_single(name, &mut metadata);



   }



   return metadata;



   }



   // ===== GENERAL SETUP =====



   let dt_api_token = env::var("DT_API_TOKEN").unwrap(); // TODO: change



   let dt_api_url = env::var("DT_API_URL").unwrap();



   let mut map = HashMap::new();



   map.insert("Authorization".to_string(), format!("Api-Token {}", dt_api_token));



   let resource = Resource::builder()



   .with_service_name("rust-manual-quickstart")



   .with_attributes(read_dt_metadata())



   .build();



   // ===== TRACING SETUP =====



   global::set_text_map_propagator(TraceContextPropagator::new());



   let tracer_exporter = SpanExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_protocol(Protocol::HttpBinary)



   .with_endpoint(dt_api_url.clone() + "/v1/traces")



   .build()



   .unwrap();



   let tracer_provider = SdkTracerProvider::builder()



   .with_resource(resource.clone())



   .with_batch_exporter(tracer_exporter)



   .build();



   global::set_tracer_provider(tracer_provider.clone());



   // ===== METRICS SETUP ======



   let metrics_exporter = MetricExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/metrics")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let meter_provider = SdkMeterProvider::builder()



   .with_reader(PeriodicReader::builder(metrics_exporter).build())



   .with_resource(resource.clone())



   .build();



   global::set_meter_provider(meter_provider);



   // ===== LOGS SETUP ======



   let logger_exporter = LogExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/logs")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let logger_provider = SdkLoggerProvider::builder()



   .with_batch_exporter(logger_exporter)



   .with_resource(resource.clone())



   .build();



   let otel_log_appender = OpenTelemetryLogBridge::new(&logger_provider);



   log::set_boxed_logger(Box::new(otel_log_appender)).unwrap();



   log::set_max_level(Level::Debug.to_level_filter());



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
4. Make sure the environment variables `DT_API_URL` and `DT_API_TOKEN` are properly configured for the [Dynatrace URL](#base-url) and [access token](#access-token).
5. Call `init_opentelemetry()` as early as possible in your startup code.

## Step 3 Instrument your application

### Add tracing

1. First, we need to get a tracer object.

   ```
   let tracer = global::tracer("my-tracer");
   ```
2. With `tracer`, we can now start new spans.

   ```
   let mut _span = tracer



   .span_builder("Call to /myendpoint")



   .with_kind(SpanKind::Internal)



   .start(&tracer);



   _span.set_attribute(KeyValue::new("http.method", "GET"));



   _span.set_attribute(KeyValue::new("net.protocol.version", "1.1"));



   // TODO: Your code goes here



   _span.end();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `end()` method to complete the span

### Collect metrics

1. First, we need to get a tracer object.

   ```
   let meter = global::meter("request_counter");
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   let updown_counter = meter.i64_up_down_counter("request_counter").build();
   ```
3. We can now invoke the `add()` method of `updown_counter` to record new values with the counter.

   ```
   updown_counter.add(1,&[],);
   ```

### Connect logs

In `init_opentelemetry()`, we earlier initialized the [logï»¿](https://docs.rs/log/latest/log/) crate with its OpenTelemetry log bridge and can now call any of its [logging macrosï»¿](https://docs.rs/log/latest/log/#macros) to log directly to Dynatrace.

```
error!("logging an error");



debug!("logging a debug message");
```

Maximum log level

Note the call to the [`log::set_max_level`ï»¿](https://docs.rs/log/latest/log/fn.set_max_level.html) method in the [initialization of OpenTelemetry](#set-up-opentelemetry) earlier. This sets the maximum log level of the log crate to `Level::Debug` and is required for the logged messages at that level to be emitted in the first place and picked up by the OpenTelemetry log bridge. Adjust this if you use a different maximum log level.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

To continue an existing trace from an HTTP request, we first need to extract the context. For this, we declare the function `extract_context_from_request()`, which takes the incoming request object, extracts the passed context using the propagator's `extract()` method, and returns the matching context object.

```
// Utility function to extract the context from the incoming request headers



fn extract_context_from_request(req: &Request<Incoming>) -> Context {



global::get_text_map_propagator(|propagator| {



propagator.extract(&HeaderExtractor(req.headers()))



})



}
```

We can then use `extract_context_from_request()` in our request handler to obtain that context and pass it as parent to our own, new [server spanï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#server) using `start_with_context()`.

```
async fn router(req: Request<Incoming>) -> Result<Response<BoxBody<Bytes, hyper::Error>>, Infallible> {



// Extract the context from the incoming request headers



let parent_cx = extract_context_from_request(&req);



let response = {



// Create a span parenting the remote client span.



let tracer = global::tracer("example/server");



let mut span = tracer



.span_builder("router")



.with_kind(SpanKind::Server)



.start_with_context(&tracer, &parent_cx);



// Adding custom attributes



span.set_attribute(KeyValue::new("my-server-key-1", "my-server-value-1"));



};



// TODO Handle the HTTP request



}
```

#### Injecting the context when sending requests

To propagate the current context to another HTTP service, we inject the context information into the HTTP request headers. The following example declares the function `send_request()`, which takes the URL of the request, the request content, and sends the request using [hyperï»¿](https://docs.rs/hyper/latest/hyper/index.html).

Once the hyper request object is initialized, we call `get_text_map_propagator()` to obtain the global `propagator` object and then use its `inject_context()` function to add the current context information to the request.

```
async fn send_request(url: &str, body_content: &str, span_name: &str) -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync + 'static>> {



let client = Client::builder(TokioExecutor::new()).build_http();



let tracer = global::tracer("example/client");



let span = tracer



.span_builder(String::from(span_name))



.with_kind(SpanKind::Client)



.start(&tracer);



let cx = Context::current_with_span(span);



let mut req = hyper::Request::builder().uri(url);



global::get_text_map_propagator(|propagator| {



propagator.inject_context(&cx, &mut HeaderInjector(req.headers_mut().unwrap()))



});



let res = client



.request(req.body(Full::new(Bytes::from(body_content.to_string())))?)



.await?;



cx.span().add_event(



"Got response!",



vec![KeyValue::new("status", res.status().to_string())],



);



Ok(())



}
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")


---


## Source: walkthroughs.md


---
title: Instrument your application
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs
scraped: 2026-02-17T21:24:30.909831
---

# Instrument your application

# Instrument your application

* Latest Dynatrace
* How-to guide
* 1-min read
* Updated on Nov 15, 2023

The following walk-throughs are guided, step-by-step tutorials for the different programming languages supported by OpenTelemetry. They provide code samples on how to integrate the OpenTelemetry libraries into your application, initialize OpenTelemetry, create the different signals (that is, traces, metrics, and logs), and export the data to the Dynatrace backend.

[### C++](/docs/ingest-from/opentelemetry/walkthroughs/cpp "Learn how to instrument your C++ application using OpenTelemetry and Dynatrace.")[![Elixir](https://dt-cdn.net/images/elixir-logo-180-b773ecbdae.png "Elixir")

### Elixir](/docs/ingest-from/opentelemetry/walkthroughs/elixir "Learn how to instrument your Elixir application using OpenTelemetry and Dynatrace.")[### Erlang](/docs/ingest-from/opentelemetry/walkthroughs/erlang "Learn how to instrument your Erlang application using OpenTelemetry and Dynatrace.")[### Go](/docs/ingest-from/opentelemetry/walkthroughs/go "Learn how to instrument your Go application using OpenTelemetry and Dynatrace.")[### Java](/docs/ingest-from/opentelemetry/walkthroughs/java "Learn how to instrument your Java application using OpenTelemetry and Dynatrace.")[### JavaScript](/docs/ingest-from/opentelemetry/walkthroughs/nodejs "Learn how to instrument your JavaScript application on Node.js using OpenTelemetry and Dynatrace.")[### .NET](/docs/ingest-from/opentelemetry/walkthroughs/dotnet "Learn how to instrument your .NET application using OpenTelemetry and Dynatrace.")[### PHP](/docs/ingest-from/opentelemetry/walkthroughs/php "Learn how to instrument your PHP application using OpenTelemetry and Dynatrace.")[### Python](/docs/ingest-from/opentelemetry/walkthroughs/python "Learn how to instrument your Python application using OpenTelemetry and Dynatrace.")[### Ruby](/docs/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.")[![Rust](https://dt-cdn.net/images/rust-logo-gray-8d1a6c296b.svg "Rust")

### Rust](/docs/ingest-from/opentelemetry/walkthroughs/rust "Learn how to instrument your Rust application using OpenTelemetry and Dynatrace.")

## Related topics

* [OpenTelemetry interoperability](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability "Enable and use OpenTelemetry interoperability in AWS Lambda.")
* [Google Cloud Functions monitoring](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions "Set up monitoring for Google Cloud Functions.")
* [Monitor Azure Functions on Consumption Plans](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans "Learn how to install, configure, update, and uninstall OneAgent for monitoring Azure Functions on serverless hosting plans")


---
