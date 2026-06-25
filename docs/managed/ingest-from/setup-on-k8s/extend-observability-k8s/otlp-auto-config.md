---
title: Enable automatic OpenTelemetry OTLP exporter configuration
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/otlp-auto-config
scraped: 2026-05-12T12:03:40.512966
---

# Enable automatic OpenTelemetry OTLP exporter configuration

# Enable automatic OpenTelemetry OTLP exporter configuration

* Published Nov 24, 2025

Dynatrace Operator version 1.8.0+

Dynatrace Operator can automatically configure the OpenTelemetry OTLP exporter for applications instrumented with an [OpenTelemetry SDKï»¿](https://opentelemetry.io/docs/languages/). This is done by injecting environment variables into your application pods at startup, allowing telemetry data to be sent directly to Dynatrace.

## Enable OTLP auto-configuration

### Provide a data ingest token

You need to provide a [data ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Configure tokens and permissions to monitor your Kubernetes cluster") to the Dynatrace Operator. This token is passed to your application as part of the OTLP exporter configuration.

### Update your DynaKube resource

Add the `otlpExporterConfiguration` section to your DynaKube custom resource. This enables auto-configuration for all signals (metrics, traces, logs):

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

You can enable injection for each signal type (metrics, traces, logs) separately.

The following secrets are created in each [injected namespace](#namespace-selector):

* `dynatrace-otlp-exporter-certs` holds the certificates required for communication with the configured endpoint, which is one of the following:

  + The TLS certificate for the ActiveGate.
  + Certificates contained in `.spec.trustedCAs`, if provided and no ActiveGate with TLS certificates is available.
* `dynatrace-otlp-exporter-config` holds a copy of the [data ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Configure tokens and permissions to monitor your Kubernetes cluster").

Secrets are updated automatically when the token or certificate changes, but only new pods will receive updated values. Restart your application pods subsequent to a change to avoid authentication or communication issues.

**Notes**:

* OTLP exporter configuration [is skipped](#verify-config) in case prerequisites are not fulfilled.
* By default, if any `OTEL_EXPORTER_OTLP_*` environment variable is already present in the container spec, Dynatrace Operator will skip the injection of endpoint configuration (aka. `OTEL_EXPORTER_OTLP_*`) â even if the existing configuration doesn't overlap with what would be added automatically. To allow Dynatrace Operator to override the existing configuration, enable [override mode](#override). Resource attributes (`OTEL_RESOURCE_ATTRIBUTES`) are not affected by this logic and will still be set or extended.

### Verify the auto-configuration

If the OTLP auto-configuration has been injected successfully, your application pod receives the following annotation:

```
otlp-exporter-configuration.dynatrace.com/injected: "true"
```

If something goes wrong, the pod is annotated with a reason for the failure:

```
otlp-exporter-configuration.dynatrace.com/injected: "false"



otlp-exporter-configuration.dynatrace.com/reason: <reason>
```

## Injected OTLP configuration

### Environment variables

The following environment variables are injected into your application containers:

| Variable | Value |
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

### Resource attributes

Dynatrace Operator adds resource attributes in `OTEL_RESOURCE_ATTRIBUTES` to enrich OpenTelemetry data providing topology and additional context on data points for a rich Dynatrace experience:

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

The values for those attributes are derived from the cluster and pod metadata. Furthermore, all metadata provided in the `metadata.dynatrace.com/<key>: <value>` annotations on the namespace or on the injected pod are added as resource attributes.

Any attributes you have already set in `OTEL_RESOURCE_ATTRIBUTES` are preserved, and the above attributes are appended.

Resource attributes are always injected when autoâconfiguration is enabled, regardless of existing OTLP exporter settings or whether override mode is enabled.

## Limitations

### Application pods using `envFrom`

When you populate your environment variables using `envFrom`, Dynatrace Operator is not able to discover environment variables that are already set. In this case, the injected Dynatrace OTLP exporter config takes precedence over values coming from `envFrom`, even without using the [override mode](#override).

### Hardcoded SDK configuration

* In OTel SDKs, programmatic configuration takes precedence over environment variables. Ensure the standard exporter environment variables are supported by your application.
* Dynatrace always uses protocol `http/protobuf`. If your application is restricted to gRPC, the injected protocol variable will have no effect and communication will fail.

## Route OTLP traffic via ActiveGate

If an in-cluster ActiveGate is deployed with the same DynaKube that is used for OTLP auto-configuration, the traffic is routed through this ActiveGate. Without the in-cluster ActiveGate the traffic is sent directly to your Dynatrace tenant.

## Injection control

### Namespace selector

To limit auto-configuration to specific namespaces, you can use a namespace selector:

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



my.app.com/otel: "true"



signals:



metrics: {}



traces: {}



logs: {}
```

### Pod and container annotations

For fine-grained control beyond the [namespace selector](#namespace-selector), you can use annotations to control injection behaviour on the pods directly:

Per default automatic injection and therefore OTLP exporter auto-configuration is enabled for all namespaces (controlled via [feature-flag](/managed/ingest-from/setup-on-k8s/reference/dynakube-feature-flags "List the feature flags to configure Dynatrace Operator on Kubernetes.")).

You can control the OTLP exporter auto-configuration using either existing annotations that control all Dynatrace injections at once (see the [documentation](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/annotate#podexclusion "Configure monitoring for namespaces and pods") for more information) or by adding `otlp-exporter-configuration.dynatrace.com/inject: true/false` to a Pod.

Known inconsistency in Dynatrace Operator 1.8

There is a known inconsistency on how these flags work between OTLP exporter configuration injection and OneAgent injection. The value of `feature.dynatrace.com/inject` is used as default value for `dynatrace.com/inject`, the annotation `otlp-exporter-configuration.dynatrace.com/inject` defaults to `true`. This will be fixed in the next Dynatrace Operator release.

Injection flag combinations

| `dynatrace.com/inject` [1](#fn-1-1-def) | `otlp-exporter-configuration.dynatrace.com/inject` [2](#fn-1-2-def) | `feature.dynatrace.com/automatic-injection` [3](#fn-1-3-def) | Injected |
| --- | --- | --- | --- |
| `false` | <n/a> | <n/a> | Not applicablenot injected |
| `true` / unset [4](#fn-1-4-def) | `false` | <n/a> | Not applicablenot injected |
| `true` / unset [4](#fn-1-4-def) | `true` | <n/a> | Applicableinjected |
| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `true` / unset [4](#fn-1-4-def) | Applicableinjected |
| `true` / unset [4](#fn-1-4-def) | unset [5](#fn-1-5-def) | `false` | Not applicablenot injected |

[1](#fn-1-1-def) set on application Pod

[2](#fn-1-2-def) set on application Pod

[3](#fn-1-3-def) set on the DynaKube

[4](#fn-1-4-def) default `true`

[5](#fn-1-5-def) value of `feature.dynatrace.com/automatic-injection` used as default

## Enable environment variable overrides

By default, any existing configuration (for example, already set environment variables) is not altered, overwritten, or removed. This includes all environment variables matching the pattern `OTEL_EXPORTER_OTLP_*`. If any of those environment variables already exist in a container specification, no automatic configuration is made **at all**, even if the activated signal does not directly conflict with the existing configuration.

For example, if only `traces` is activated in `.spec.otlpExporterConfiguration.signals` and the container has `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` already set, `OTEL_EXPORTER_OTLP_TRACES_ENDPOINT` won't be configured on your pod.

To enable this override, you can turn on the override mode:

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

With `.spec.otlpExporterConfiguration.overrideEnvVars: true`, Dynatrace Operator will:

* Add configuration for signals not yet present (in this example, `metrics`)
* Overwrite configuration for signals already present
* Retain existing configurations if they don't conflict with the configured signals

The following examples have the above DynaKube configuration with `metrics` enabled and `overrideEnvVars` set to `true`.

### Simple override

**Before**

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

**After**

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

### Simple addition of the new signal

**Before**

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

**After**

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

### OTLP general configuration environment variables

A special case is the use of `OTEL_EXPORTER_OTLP_ENDPOINT` and its companion environment variables. These variables provide defaults for all signals at once. If such a variable is already set for the container, it is not removed. Instead, the signal-specific configuration is added and takes precedence.

In this example, metrics will now be sent to the Dynatrace endpoint, while traces and logs would still be reported to the previously configured endpoint.

**Before**

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

**After**

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

## `NO_PROXY` support

If you choose to have an ActiveGate and a proxy configured on your application pods, the ActiveGate service is automatically added to the `NO_PROXY` environment variable. If the environment variable does not yet exist, it will be created.

You can opt-out of of this by adding the following annotation to your DynaKube:

```
apiVersion: dynatrace.com/v1beta6



kind: DynaKube



metadata:



annotations:



feature.dynatrace.com/otlp-exporter-configuration-set-no-proxy: "false"
```

## Related topics

* [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.")