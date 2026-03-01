---
title: How to scale the OpenTelemetry Collector
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/collector/scaling
scraped: 2026-03-01T21:17:24.944717
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