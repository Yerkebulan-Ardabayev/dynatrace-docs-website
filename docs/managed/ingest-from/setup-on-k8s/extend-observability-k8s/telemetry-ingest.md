---
title: Enable Dynatrace telemetry ingest endpoints
source: https://docs.dynatrace.com/managed/ingest-from/setup-on-k8s/extend-observability-k8s/telemetry-ingest
---

# Enable Dynatrace telemetry ingest endpoints

# Enable Dynatrace telemetry ingest endpoints

* Updated on Nov 04, 2025

Dynatrace Operator version 1.6+

Enable Dynatrace telemetry endpoints in Kubernetes for cluster-local data ingest.

* Ingest data via [OTLP﻿](https://opentelemetry.io/docs/specs/otel/protocol/), [Jaeger﻿](https://www.jaegertracing.io/), [StatsD﻿](https://github.com/statsd/statsd) or [Zipkin﻿](https://zipkin.io/) endpoints
* Analyze context-rich data with built-in apps, DQL, Notebooks and Dashboards

## Prerequisites

* The [data ingest token](/managed/ingest-from/setup-on-k8s/deployment/tokens-permissions#dataIngestToken "Configure tokens and permissions to monitor your Kubernetes cluster") requires the token scopes `openTelemetryTrace.ingest`, `logs.ingest`, and `metrics.ingest` and must be provided via the `dataIngestToken` field in the same [secret](/managed/ingest-from/setup-on-k8s/deployment/k8s-obs-managed#create-secret-helm "Deploy Dynatrace Operator for Kubernetes observability.") as your API token.

## Setup and Use

The following two steps explain how to setup and use telemetry ingest endpoints.

Kubernetes App onboarding

If you got your DynaKube from the [onboarding screen of the Dynatrace Kubernetes App](/managed/ingest-from/setup-on-k8s/quickstart "Deploy Dynatrace Operator on Kubernetes") the telemetry ingest service name will be set to `telemetry-ingest.dynatrace`. See [Customize the name of the telemetry ingest service](#customize-the-service-name) to change it.

1. Create DynaKube

To enable telemetry ingest endpoints, specify a list of desired protocols in the DynaKube field `.spec.telemetryIngest.protocols`. Please find more information about the exact values in our [DynaKube reference](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#telemetry-ingest-v1beta5 "List the available parameters for setting up Dynatrace Operator on Kubernetes.") documentation.

Data routing

With an ActiveGate running in the Kubernetes cluster, the [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") will be configured to route all ingested data through the in-cluster ActiveGate instead of connecting directly to a public ActiveGate. Additionally, the capabilities required for telemetry ingest will automatically be enabled.

If no in-cluster ActiveGate is deployed (i.e., `.spec.activeGate` is not specified), the OpenTelemetry Collector will be configured to communicate directly with your Dynatrace tenant.

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

OTel collector image

OTel collector image is sourced from our [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), make sure the used `tag` exists! Alternatively, you can use your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

2. Configure applications

Once the DynaKube is applied, the Dynatrace Operator will deploy the Dynatrace OpenTelemetry Collector with the default image ([configurable using `.spec.templates.otelCollector.imageRef`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters#extensions-collector-image-ref "List the available parameters for setting up Dynatrace Operator on Kubernetes.")) and a Kubernetes service named `<dynakube-name>-telemetry-ingest.dynatrace` ([configurable using `.spec.telemetryIngest.serviceName`](#customize-the-service-name)) for telemetry ingest. The used port number depends on the protocol your application supports. To find the respective port numbers, please see the [reference](#port-list) below.

The following snippet shows how you can configure an application using an environment variable that is instrumented with the OpenTelemetry SDK:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: http://<dynakube-name>-telemetry-ingest.dynatrace:4317
```

### Ports reference

The following ports are open for telemetry data ingestion:

| Name | Protocol | Port |
| --- | --- | --- |
| OTLP GRPC | TCP | 4317 |
| OTLP HTTP | TCP | 4318 |
| Zipkin | TCP | 9411 |
| Jaeger GRPC | TCP | 14250 |
| Jaeger Thrift Binary | UDP | 6832 |
| Jaeger Thrift Compact | UDP | 6831 |
| Jaeger Thrift HTTP | TCP | 14268 |
| StatsD | UDP | 8125 |

## Additional configurations

### Use HTTPS endpoints

By default, the ingest endpoints operate in HTTP mode. If you want to encrypt the telemetry traffic by using HTTPS, you can reference a [Kubernetes TLS secret﻿](https://dt-url.net/yw03zsm) via [`.spec.telemetryIngest.tlsRefName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."). The ingest endpoints will then be configured to use referenced certificates and listen for HTTPS.

Example for an OpenTelemetry instrumented application using HTTPS

The following snippet shows how you can configure an application that is instrumented with the OpenTelemetry SDK through the environment variable:

```
env:



- name: OTEL_EXPORTER_OTLP_ENDPOINT



value: https://<dynakube-name>-telemetry-ingest.dynatrace:4318
```

### Customize the name of the telemetry ingest service

By default, the service name for telemetry ingest is `<dynakube-name>-telemetry-ingest.dynatrace`, but it can be customized by setting [`.spec.telemetryIngest.serviceName`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."). The provided value will be used as a service name, but the services will still be in the namespace of the DynaKube, which is where also the Dynatrace OpenTelemetry Collector is deployed.

Be aware that having multiple DynaKubes with the same service name will cause service name collisions.

For example, if you set `.spec.telemetryIngest.serviceName` to `my-telemetry-ingest`, the endpoints are available at `http://my-telemetry-ingest.dynatrace:4318`.

Example

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

OTel collector image

OTel collector image is sourced from our [supported public registries](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-public-registry#supported-public-registries "Configure the Dynatrace Operator to use public registry images for itself and its managed components. This can be done manually or through automatic resolution from your Dynatrace environment."), make sure the used `tag` exists! Alternatively, you can use your [private registry](/managed/ingest-from/setup-on-k8s/guides/container-registries/use-private-registry "Use a private registry").

### Proxy settings

Any proxy specified in [`.spec.proxy`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") will be propagated to the OpenTelemetry Collector via environment variables `HTTP_PROXY` and `HTTPS_PROXY`. If an in-cluster ActiveGate is used, the URL of the in-cluster ActiveGate will automatically be added to the `NO_PROXY` environment variable to avoid unnecessary communication loops.

#### Trusted CAs

If you need to use certificates for proxy communication, they can be specified in [`.spec.trustedCAs`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes."). System CAs from the OpenTelemetry Collector container image are loaded together with CAs in `trustedCAs`. The system CAs contain the certificates required for communication with public ActiveGates.

### ActiveGate persistent storage

When telemetry ingest is used with an in-cluster ActiveGate, ingested data is buffered on a PersistentVolume on the ActiveGate until data has been transfered successfully. For this purpose, a [PersistentVolumeClaim is mounted to the ActiveGate](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/activegate-pvc "Set up a persistent storage for containerized ActiveGate to be used as temporary storage for ingested data."). The following example illustrates the default PVC configured to the ActiveGate by the operator if no custom PVC is specified:

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

Default storage class

Please ensure a [default storage class﻿](https://kubernetes.io/docs/concepts/storage/persistent-volumes/#class-1) is defined. Otherwise, the PersistentVolumeClaim of the ActiveGate cannot be provisioned.

A custom PersistentVolumeClaim can be configured in [`.spec.activegate.volumeClaimTemplate`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

#### Ephemeral volume

For test purposes, a PVC can be replaced by local ephemeral storage using [`.spec.activeGate.useEphemeralVolume`](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.").

Using `.spec.activeGate.useEphemeralVolume` is not recommended for production environments.

### ActiveGate time for shutdown

If an ActiveGate is shut down (for example, in scale-in scenarios), it needs some time to flush its buffers by sending all the buffered data to Dynatrace.
In large environments, this can take some time and Kubernetes could potentially terminate the ActiveGate too early. To expand the so-called termination grace period, you can increase the duration via ['.spec.activegate.terminationGracePeriodSeconds'](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.") to give the ActiveGate pod more time to gracefully shut down.

## Related topics

* [DynaKube parameters for Dynatrace Operator](/managed/ingest-from/setup-on-k8s/reference/dynakube-parameters "List the available parameters for setting up Dynatrace Operator on Kubernetes.")