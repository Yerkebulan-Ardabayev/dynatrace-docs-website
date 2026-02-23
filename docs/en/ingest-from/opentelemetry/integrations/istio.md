---
title: Configure OpenTelemetry tracing with Istio
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/integrations/istio
scraped: 2026-02-23T21:39:52.247878
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