---
title: Configure OpenTelemetry tracing with Istio
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/integrations/istio
---

# Configure OpenTelemetry tracing with Istio

# Configure OpenTelemetry tracing with Istio

* How-to guide
* 3-min read
* Updated on Jul 30, 2026

Support statement

This integration is based on open source code governed by the respective communities and is not covered under the Dynatrace support policy. While we strive to assist, issues and feature requests should be reported directly to the respective project. Dynatrace cannot ensure fixes/features due to the independent nature of OSS projects.

Always use the most recent release version to ensure you have the latest patches and fixes deployed.

This page describes how to use Istio version 1.22+ with the [Istio OpenTelemetry extension provider﻿](https://istio.io/latest/docs/reference/config/istio.mesh.v1alpha1/#MeshConfig-ExtensionProvider-OpenTelemetryTracingProvider), and how to configure it to export OpenTelemetry traces to Dynatrace. This lets you monitor traffic flowing through your Istio service mesh directly in Dynatrace.

## Prerequisites

* Istio version 1.22+ (that is, Istio releases that ship with Envoy 1.30+)
* `kubectl` access to your cluster
* Disable the OneAgent Envoy code module

  1. Go to the applicable configuration page:

     + For the entire environment:

       - In Latest Dynatrace, go to ![Settings](https://dt-cdn.net/images/settings-icon-256-38e1321b51.webp "Settings") **Settings** > **Collect and capture** > **General monitoring settings** > **Monitored technologies**.
       - In Dynatrace Classic, go to **Settings** > **Monitoring** > **Monitored technologies**.
     + For a particular host, go to **Your host** > **Host settings** > **General**.
  2. Find **Envoy** in the list of monitored technologies and select  **Edit**.
  3. Select the **Monitor Envoy** toggle, as appropriate, to turn off the OneAgent Envoy code module.

## Licensing impact

In certain deployment setups, tracing with Istio version 1.22+ results in consumption of the following [rate card﻿](https://www.dynatrace.com/pricing/) capabilities:

* When using the Dynatrace resource detector and sampler:

  + Classic Full-Stack or cloud-native Full-Stack deployments: Usage is included in [Full-Stack Monitoring (DPS)](/managed/license/capabilities/app-infra-observability/full-stack-monitoring "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") and [Host Units (Dynatrace Classic License)](/managed/license/classic-licensing/application-and-infrastructure-monitoring "Understand how Dynatrace application and infrastructure monitoring consumption is calculated based on host units.").
  + For Application-Observability-only deployments: Usage incurs consumption of [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.") or [DDUs for custom traces (Dynatrace Classic License)](/managed/license/classic-licensing/davis-data-units/custom-traces "Understand how DDU consumption is calculated for spans ingested via the Trace API.").
* Without the Dynatrace resource detector and sampler: Usage incurs consumption of [Custom Traces Classic (DPS)](/managed/license/capabilities/platform-extensions "Learn how consumption of Dynatrace platform extensions is calculated using the Dynatrace Platform Subscription model.") or [DDUs for custom traces (Dynatrace Classic License)](/managed/license/classic-licensing/davis-data-units/custom-traces "Understand how DDU consumption is calculated for spans ingested via the Trace API.").

## Deployment modes

You can configure Istio OpenTelemetry tracing in a standalone deployment or in combination with Dynatrace Operator.

### Istio and Dynatrace Operator

You can use the Istio OpenTelemetry integration in combination with a Dynatrace Operator deployment with [metadata enrichment](/managed/ingest-from/setup-on-k8s/guides/metadata-automation/metadata-enrichment "Configure metadata enrichment in Dynatrace Operator to attach Kubernetes metadata to telemetry signals using OneAgent, OTLP exporter, or standalone enrichment.") and [telemetry ingest endpoints](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") enabled. Other features like OneAgent or ActiveGate are not required.

This provides the following benefits compared to standalone usage:

* Resilient and more efficient delivery of traces by providing retry and batching capabilities.
* Spans are enriched with Kubernetes metadata allowing correlation with Kubernetes workloads or services in Dynatrace.

Prerequisites for this deployment mode:

* Dynatrace Operator is [deployed](/managed/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes").
* [Telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") endpoints are enabled.

### Istio standalone

In a standalone deployment, Istio exports traces directly to the Dynatrace OTLP API.
Use this deployment mode only if you cannot deploy Dynatrace Operator.

Caveats when using standalone deployment:

* No Kubernetes metadata will be available for traces. This means traces will not be automatically correlated with Kubernetes workloads or services in Dynatrace.
* Potentially unreliable delivery of traces. The current implementation of the OTLP HTTP exporter in Envoy doesn't provide any means of retry or error handling in case of connectivity or other issues when sending traces to Dynatrace, which can lead to loss of traces.

### Istio ambient mode

Istio in ambient mode doesn't rely on Envoy proxies to route traffic, so tracing Istio traffic using the OpenTelemetry integration is not possible. If you use waypoint proxies, they would still emit traces, but the metadata would be misleading or wrong. Currently, there is no solution for end-to-end tracing in Istio ambient mode.

## Configure Istio tracing

### 1. Create a Dynatrace access token

Dynatrace Operator

Standalone

1. In Dynatrace, select `Ctrl+K` and search for **Access tokens**.
2. Select **Generate new token**.
3. Give the token a name and add the following scopes:

   * **Read sampling configuration for Adaptive Traffic Management** (`adaptiveTrafficManagement.read`)
4. Select **Generate token** and copy the token value.

For more information, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

1. In Dynatrace, select `Ctrl+K` and search for **Access tokens**.
2. Select **Generate new token**.
3. Give the token a name and add the following scopes:

   * **Ingest OpenTelemetry traces** (`openTelemetryTrace.ingest`)
   * **Read sampling configuration for Adaptive Traffic Management** (`adaptiveTrafficManagement.read`)
4. Select **Generate token** and copy the token value.

For more information, see [Dynatrace API - Tokens and authentication](/managed/dynatrace-api/basics/dynatrace-api-authentication "Find out how to get authenticated to use the Dynatrace API.").

### 2. Apply the mesh configuration to your Istio installation

Use the following configuration as a starting point for your Istio installation, or append it to your existing Istio MeshConfig.

Existing Mesh configuration

If you already use your own custom Mesh configuration, you need to merge its content with the provided snippet. Otherwise, you can use the snippet as-is.

Dynatrace Operator

Standalone

```
apiVersion: install.istio.io/v1alpha1



kind: IstioOperator



spec:



components:



pilot:



k8s:



env:



- name: ENABLE_NATIVE_SIDECARS



value: "false"



meshConfig:



extensionProviders:



- name: dynatrace-otel



opentelemetry:



port: 4318



service: "<dynakube-name>-telemetry-ingest.<dynatrace-operator-namespace>"



http:



path: "/v1/traces"



timeout: 5s



resource_detectors:



dynatrace: {}



dynatrace_sampler:



tenant: "<your-tenant-id>"



cluster_id: <cluster-id>



http_service:



service: "istio-system/<your-tenant-id>.live.dynatrace.com"



port: 80



http:



path: "/api/v2/samplingConfiguration"



timeout: 10s



headers:



- name: "Authorization"



value: "Api-Token <API_TOKEN>"
```

The configuration snippet uses the following placeholders.
Replace the placeholder with the appropriate value.

* `<dynakube-name>-telemetry-ingest.<dynatrace-operator-namespace>`: The name of your [telemetry ingest](/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest "Enable Dynatrace telemetry ingest endpoints in Kubernetes for cluster-local data ingest.") service. For example, `telemetry-ingest.dynatrace.svc.cluster.local`
* `<your-tenant-id>`: Your Dynatrace environment ID. See [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") to find yours.
* `<cluster-id>`: The numeric ID of your Dynatrace cluster. Use the `GET /api/v1/config/clusterid` API to get your cluster ID.
* `<API_TOKEN>`: The access token you generated in the previous step.

Save the file as `meshconfig.yaml` and apply it:

```
istioctl install -f meshconfig.yaml
```

```
apiVersion: install.istio.io/v1alpha1



kind: IstioOperator



spec:



meshConfig:



extensionProviders:



- name: dynatrace-otel



opentelemetry:



port: 80



service: "istio-system/<your-environment-id>.live.dynatrace.com"



http:



path: "/api/v2/otlp/v1/traces"



timeout: 10s



headers:



- name: "Authorization"



value: "Api-Token <API_TOKEN>"



resource_detectors:



dynatrace: {}



dynatrace_sampler:



tenant: "<your-tenant-id>"



cluster_id: <cluster-id>
```

The configuration snippet uses the following placeholders.
Replace the placeholder with the appropriate value.

* `<your-environment-id>`: Your Dynatrace environment ID. See [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") to find yours.
* `<API_TOKEN>`: The access token you generated in the previous step.
* `<your-tenant-id>`: The same value as `<your-environment-id>`.
* `<cluster-id>`: The numeric ID of your Dynatrace cluster. Use the `GET /api/v1/config/clusterid` API to get your cluster ID.

Save the file as `meshconfig.yaml` and apply it:

```
istioctl install -f meshconfig.yaml
```

### 3. Deploy the ServiceEntry resource

A [`ServiceEntry`﻿](https://istio.io/latest/docs/reference/config/networking/service-entry/) is required to communicate with the Dynatrace API.
This is needed for exporting spans and/or for obtaining sampling configuration when using the Dynatrace Sampler.
Save the following configuration as `dt-serviceentry.yaml`.

```
apiVersion: networking.istio.io/v1alpha3



kind: ServiceEntry



metadata:



name: dynatrace-se-otel



spec:



hosts:



- <your-environment-id>.live.dynatrace.com



ports:



- number: 80



name: http-port



protocol: HTTP



targetPort: 443



- number: 443



name: https-port



protocol: HTTPS



resolution: DNS



location: MESH_EXTERNAL



---



apiVersion: networking.istio.io/v1alpha3



kind: DestinationRule



metadata:



name: dynatrace-dr-otel



spec:



host: <your-environment-id>.live.dynatrace.com



trafficPolicy:



portLevelSettings:



- port:



number: 80



tls:



mode: SIMPLE
```

The configuration snippet uses the following placeholders.
Replace the placeholder with the appropriate value.

* `<your-environment-id>`: Your Dynatrace environment ID. See [environment ID](/managed/discover-dynatrace/get-started/monitoring-environment "Learn what a Dynatrace monitoring environment is, how to find your environment ID, and how to set up and connect multiple environments.") to find yours.

Apply the configuration:

```
kubectl apply -f dt-serviceentry.yaml -n istio-system
```

### 4. Deploy the Telemetry resource

As the last configuration step, use the Istio telemetry API to activate the tracing provider. Save the following configuration as `dt-telemetry.yaml`.

```
apiVersion: telemetry.istio.io/v1alpha1



kind: Telemetry



metadata:



name: dynatrace-telemetry-otel



spec:



tracing:



- providers:



- name: dynatrace-otel
```

Apply the configuration to the desired namespace:

```
kubectl apply -n istio-system -f dt-telemetry.yaml
```

### 5. Verify the setup

Once the setup is complete and you have ingested your first data, you can verify if the traces show up on the **Distributed traces** page.

## Next steps

To also trace traffic passing through standalone Envoy proxies outside of Istio, see [Configure OpenTelemetry tracing with Envoy](/managed/ingest-from/opentelemetry/integrations/envoy "Configure Envoy to export OpenTelemetry traces to Dynatrace using the Envoy OpenTelemetry tracer, including resource detection and adaptive sampling.").