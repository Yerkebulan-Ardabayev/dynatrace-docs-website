---
title: Monitor Prometheus metrics
source: https://www.dynatrace.com/docs/observe/infrastructure-observability/container-platform-monitoring/kubernetes-monitoring/monitor-prometheus-metrics
scraped: 2026-02-22T21:14:55.179621
---

# Monitor Prometheus metrics

# Monitor Prometheus metrics

* 14-min read
* Updated on Jan 29, 2026

Prometheus is an open-source monitoring and alerting toolkit which is popular in the Kubernetes community. Prometheus scrapes metrics from a number of HTTP(s) endpoints that expose metrics in the OpenMetrics format.
See the list of available [exportersï»¿](https://dt-url.net/vd03n1m) in the Prometheus documentation.

## Prometheus Metric Type Ingest

Dynatrace is able to ingest Prometheus metrics [Counter](#counter), [Gauge](#gauge), [Histogram](#histogram) and [Summary](#summary)
in Kubernetes using [Prometheus exportersï»¿](https://dt-url.net/lw02ror) and makes them available for charting, alerting and analysis.

### Counter

The Prometheus counter metric[1](#fn-1-1-def) is a monotonically increasing value typically used for measurements that can only increase or remain constant.
Dynatrace uses its [`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") metric type, which uses **delta encoding**[2](#fn-1-2-def) in order to reduce data redundancy, for data ingestion.
As such, the value displayed in Dynatrace does not reflect the actual counter value, but instead its change, or delta, over observations.

This method results in a counter metric appearing one minute delayed in contrast to a [Gauge](#gauge) metric if scraping for both metrics started simultaneously.
For details, see the [metric ingestion protocol reference](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

Ingesting Counter metrics

The **delta encoding** used by the Dynatrace [`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") ingestion type means that the ingested value *does not* reflect the actual value, but the difference between measurements.

1

[Prometheus official documentation: Counterï»¿](https://dt-url.net/cd02rce)

2

Delta encoding, also known as delta-compression, stores data by computing the difference between two observations or target values. Primarily used
for seldomly changing data, the method avoids data redundancy.

### Gauge

In contrast to [Counter](#counter), the gauge metric[1](#fn-2-1-def) stores a single numerical value which can increase and decrease and is typically used for measured values such as
current memory usage or number of users online. In Dynatrace, the [`GAUGE`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.") metric type will be used for data ingest.

1

[Prometheus official documentation: Gaugeï»¿](https://dt-url.net/lb22r1o)

### Histogram

Histograms[1](#fn-3-1-def) provide visual insights into the distribution and frequency of numerical data.
For a base metric name of `<basename>`, Dynatrace will ingest the data according to the
following table.

Prometheus Metric

Dynatrace Ingest Type

`<basename>_bucket{le="<upper inclusive bound>"}`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_bucket_sum`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_bucket_count`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

Additional flexibility and control is provided via the [`builtin:histogram-metrics`ï»¿](https://dt-url.net/ne02rlq) settings schema.
This schema allows to configure the ingestion of `<basename>_bucket{le="<upper inclusive bound>"}` metrics.

1

[Prometheus official documentation: Histogramï»¿](https://dt-url.net/vc02rmb)

### Summary

Like a [Histogram](#histogram), the summary metric[1](#fn-4-1-def) samples observations. In contrast to the histogram metric, a summary's buckets are
represented by Ï-quantiles where 0 â¤ Ï â¤ 1. For a base metric name of `<basename>`, Dynatrace will ingest the data according to the
following table.

Prometheus Metric

Dynatrace Ingest Type

`<basename>{quantile="<Ï>"}`

[`GAUGE`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#gauge-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_sum`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

`<basename>_count`

[`COUNT`](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#count-metric "Learn how the data ingestion protocol for Dynatrace Metrics API works.")

1

[Prometheus official documentation: Summaryï»¿](https://dt-url.net/7g234n1).

### Unsupported

The following types are currently not supported by Dynatrace:

* info, gaugehistogram or stateset metrics
* exemplars

## Prerequisites

We recommend using an ActiveGate that is running inside the Kubernetes cluster which you want to scrape Prometheus metrics from. If the ActiveGate is running outside the monitored cluster (for example, in a virtual machine or in a different Kubernetes cluster), it won't be able to scrape any Prometheus endpoints on pods which require authentication (such as [RBAC](#rbac) or [client authentication](#client)). ActiveGates running inside the clusters will also provide performance improvements.

* In Dynatrace, go to your Kubernetes cluster monitoring settings page and enable

  + **Monitor Kubernetes namespaces, services, workloads, and pods**
  + **Monitor annotated Prometheus exporters**
* Annotated pod definitions. For details, see below.
* Verify that your network policies allow the ActiveGate to connect to the exporters.

  For example, if you deployed the ActiveGate in your Kubernetes cluster using the Dynatrace Operator and you have annotated Prometheus exporters in the namespace `online-boutique`, and you also have a network policy defined for this namespace, you need to make sure that the ActiveGate pod, located in the `dynatrace` namespace, can connect to the annotated Prometheus exporters in the `online-boutique` namespace.

## Annotate Prometheus exporter pods

Dynatrace collects metrics from any pods that are annotated with a `metrics.dynatrace.com/scrape` property set to `true` in the pod definition. This functionality applies to all pods across the entire Kubernetes cluster, regardless of whether the pod is running in a namespace that matches the Dynakube's namespace selector.

Depending on the actual exporter in a pod, you might need to set additional annotations to the pod definition in order to allow Dynatrace to properly ingest those metrics.

### Enable metrics scraping Required

Set `metrics.dynatrace.com/scrape` to `true` to enable Dynatrace to collect Prometheus metrics exposed for this pod.

### Metrics port Required

By default, Prometheus metrics are available at the first exposed TCP port of the pod. Set `metrics.dynatrace.com/port` to the respective port.

To determine the port value, see [Default port allocationsï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) for a list of common ports for known exporters.

### Path to metrics endpoint Optional

Use `metrics.dynatrace.com/path` to override the default (`/metrics`) Prometheus endpoint.

### HTTP/HTTPS Optional

Set `metrics.dynatrace.com/secure` to `true` if you want to collect metrics that are exposed by an exporter via HTTPS. The default value is `false`, because most exporters expose their metrics via HTTP.

If you want to skip verification of the TLS certificate (for example, if you use self-signed certificates), you can set the annotation
`metrics.dynatrace.com/insecure_skip_verify` to `true`. This annotation, however, is only considered when using an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### Filter metrics Optional



Use `metrics.dynatrace.com/filter` to define a filter that allows you to include (`"mode": "include"`) or exclude (`"mode": "exclude"`) a list of metrics. If no filter annotation is defined, all metrics are collected.
The filter syntax also supports the asterisk (`*`). This symbol allows you to filter metrics keys that begin with, end with, or contain a particular sequence, such as:

* `redis_db*` filters all metrics starting with `redis_db`
* `*insights*` filters all metrics containing `insights`
* `*bytes` filters all metrics ending with `bytes`

Using the `*` symbol within a filter, such as `redis_*_bytes`, is not supported.

The filter is applied to the raw metric key, so it's important to know that Dynatrace automatically appends suffixes to some metric keys, depending on the original metric key and metric type.
For details, see [Payload](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol#payload "Learn how the data ingestion protocol for Dynatrace Metrics API works.").

For summary and histogram, the filter is applied to the whole metric family, as stated in the `#TYPE` line of OpenMetrics format.
For example, if the summary metric family `foo_seconds` is filtered, all the metric points, including `foo_seconds_count` and `foo_seconds_sum`, are filtered.
Conversely, if `foo_seconds_count` is stated as a filter, nothing is filtered because there's no such metric family.

This example shows how to use the filter syntax in a pod definition with annotations:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/filter: |



{



"mode": "include",



"names": [



"redis_db_keys",



"*insights*",



"*bytes"



]



}



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

The values of `metrics.dynatrace.com/path`, `metrics.dynatrace.com/port`, and `metrics.dynatrace.com/secure` depend on the exporter being used; adapt them to your requirements. To determine the port value, see [Default port allocationsï»¿](https://github.com/prometheus/prometheus/wiki/Default-port-allocations) for a list of common ports for known exporters.

### Client authentication Optional

**Requirements:** Add the permissions to access `secrets` and `configmaps` for the `dynatrace-kubernetes-monitoring` ClusterRole.

Some systems require extra authentication before Dynatrace can scrape them. For such cases, you can set the following additional annotations:

* `metrics.dynatrace.com/tls.ca.crt`
* `metrics.dynatrace.com/tls.crt`
* `metrics.dynatrace.com/tls.key`

The required certificates/keys are automatically loaded from `secret`/`configmaps` specified in the annotation value.  
The schema for the annotation values is `<configmap|secret>:<namespace>:<resource_name>:<field_name_in_data_section>`.

For example, the annotations could look as follows:

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/tls.ca.crt: 'configmap:kubernetes-config:etcd-metric-serving-ca:ca-bundle.crt'



metrics.dynatrace.com/tls.crt: 'secret:kubernetes-config:etcd-metric-client:tls.crt'



metrics.dynatrace.com/tls.key: 'secret:kubernetes-config:etcd-metric-client:tls.key'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring client authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### HTTP - Basic authentication Optional

**Requirements:** Add the permissions to access `secrets` for the `dynatrace-kubernetes-monitoring` ClusterRole.

For systems that require basic HTTP authentication before scraping, you can apply the following additional annotations.

* `metrics.dynatrace.com/http.auth.basic.username`
* `metrics.dynatrace.com/http.auth.basic.password`

The following example shows two secrets created in the `default` namespace â one for a username and one for a password.
The aforementioned annotations are then used on a pod, with the secrets referenced in the annotation values.

```
apiVersion: v1



kind: Secret



metadata:



name: user-secret



data:



username: bXktdXNlcm5hbWUtc2VjcmV0Cg==



---



apiVersion: v1



kind: Secret



metadata:



name: password-secret



data:



password: bXktcGFzc3dvcmQtc2VjcmV0Cg==
```

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth.basic.username: 'secret:default:user-secret:username'



metrics.dynatrace.com/http.auth.basic.password: 'secret:default:password-secret:password'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring basic HTTP authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### HTTP - Bearer token authentication Optional

**Requirements:**

* ActiveGate version 1.317+
* Add the permissions to access `secrets` for the `dynatrace-kubernetes-monitoring` ClusterRole.

For systems that require Bearer token authentication before scraping, you can apply the additional annotation `metrics.dynatrace.com/http.auth`.

The following example shows a secret called `token-secret` created in the `default` namespace. The required Bearer token is stored under the key `bearer`.

```
apiVersion: v1



kind: Secret



metadata:



name: token-secret



data:



bearer: bXktYmVhcmVyLXRva2VuCg==
```

The annotation is then used on a pod, with the secret referenced in the annotation values.

```
apiVersion: v1



kind: Pod



metadata:



name: mypod



annotations:



metrics.dynatrace.com/scrape: 'true'



metrics.dynatrace.com/path: '/path/to-metrics'



metrics.dynatrace.com/port: '9001'



metrics.dynatrace.com/secure: 'false'



metrics.dynatrace.com/http.auth: 'secret:default:token-secret:bearer'



spec:



containers:



- name: mycontainer



image: myregistry/myimage:mytag
```

Ingesting metrics from exporters requiring Bearer token authentication is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

### Role-based access control (RBAC) authorization for metric ingestion

Exporter pods such as `node-exporter`, `kube-state-metrics`, and `openshift-state-metrics` require [RBAC authorizationï»¿](https://dt-url.net/n721pt6). For these pods, add the annotation:

`metrics.dynatrace.com/http.auth: 'builtin:default'`

This annotation applies the token from the `dynatrace-activegate` service account as an authorization header for requests to the exporter.

Ingesting metrics from exporters requiring RBAC authorization is only possible with an ActiveGate deployed inside the monitored cluster and the Kubernetes connection settings configured to monitor the local Kubernetes API endpoint.

For more information on how to annotate pods, see [Annotation best practices](#best).

## Annotate Kubernetes services

**Requirements:** Add the permission to access **services** for the `dynatrace-kubernetes-monitoring` ClusterRole (not needed for Dynatrace Operator users, as this is enabled by default in [clusterrole-kubernetes-monitoring.yamlï»¿](https://dt-url.net/gl027s4)).

You can also annotate services instead of pods. Pods corresponding to the Kubernetes services are automatically discovered via the service label selector, causing scraping of all pods belonging to the service.

* The service and its corresponding pods must be located in the same namespace.
* The `metrics.dynatrace.com/port` annotation should specify the target port of the container pod within the service, not the service's own port, since the service is not used for proxying the scraping process.

For more information on how to annotate services, see [Annotation best practices](#best).

## Annotation best practices

There are multiple ways to place annotations on pods or services. See below to decide which approach fits your scenario best.

### Recommended if you have full control

If you have full control over the pod template or service definition, we recommend adding the annotations by editing these files. This is the most reliable way to ensure persistency of annotations. We recommend editing the pod template over editing the service definition, as this requires fewer permissions (for example, if you don't have access to services).  
**Pro:** Annotations are persistent, so they don't need to be recreated if a pod is removed.

### Options if you don't have full control



If you don't have full control over the pod template, you have the following options:

* Annotate an existing service (in YAML)  
  **Requirements:** Have control over an existing YAML and permission to edit the existing Kubernetes service object.  
  **Pro:** Annotations are persistent.  
  **Con:** None.  
  **Example:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 9100



  targetPort: 12071



  selector:



  app.kubernetes.io/name: node-exporter
  ```
* Create a new service (in YAML)  
  **Requirements**: The new service should be created with a name that preferably starts with the `dynatrace-monitoring-` prefix. This service must be in the same namespace as the pods, and have permission to create a Kubernetes service object. The service is preferably headless (`clusterIP` is set to `None`) since it emphasizes that the service is not used for proxying.

  **Pro:** You have control over the original workload/service.  
  **Con:** A label selector sync is required. We support only the label selector.  
  **Example:**

  ```
  kind: Service



  apiVersion: v1



  metadata:



  name: dynatrace-monitoring-node-exporter



  namespace: kubernetes-monitoring



  annotations:



  metrics.dynatrace.com/port: '12071'



  metrics.dynatrace.com/scrape: 'true'



  metrics.dynatrace.com/secure: 'true'



  metrics.dynatrace.com/path: '/metrics'



  spec:



  ports:



  - name: dynatrace-monitoring-node-exporter-port



  port: 12071



  selector:



  app.kubernetes.io/name: node-exporter



  clusterIP: None
  ```
* Annotate an existing service (in CLI)  
  **Requirements:** Have permission to edit the existing Kubernetes service object.  
  **Pro:** No label selector sync is required.  
  **Con:** Annotations aren't persistent, so changes will overwrite the annotations. We support only the label selector.
* Annotate existing pods (in CLI)  
  **Requirements:** None.  
  **Pro:** You can quickly test metric ingestion.  
  **Con:** Annotations aren't persistent, so changes will overwrite the annotations.

## View metrics on a dashboard

Metrics from Prometheus exporters are available in Data Explorer for custom charting. Select **Create custom chart** and select **Try it out** in the top banner. For more information, see [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

You can simply search for metric keys of all available metrics and define how youâd like to analyze and chart your metrics. After that you can pin your charts on a dashboard.

## Metric alerts

You can also create custom alerts based on the Prometheus scraped metrics. Go to **Settings** > **Anomaly detection** > **Metric events** and select **Add metric event**. In the **Add metric event** page, search for a Prometheus metric using its key and define your alert. For more information, see [Metric events for alerting](/docs/dynatrace-intelligence/anomaly-detection/metric-events "Learn about metric events in Dynatrace").

## Limitations

The current limitations of the Prometheus metrics integration are as follows:

### Multiple exporters in a pod

Only one port and path can be specified in the annotations. However, it is possible to scrape multiple exporters in a pod by [annotating
additional services](#annotate-kubernetes-services) that select the same pod.

For example, if you want to scrape two endpoints in a pod, you could annotate the pod and the service
that selects the pod. If no such service exists, you can create a new service just for this purpose.

Alternatively, you could also annotate two different services that select the same pod. For more information, see [Annotation best practices](#best).

### Number of pods, metrics, and metric data points

Per Kubernetes cluster, this integration supports a maximum of:

* 1,000 exporter pods
* 1,000 metrics per pod
* 500,000 metric data points per pod

  Even though larger datasets are allowed, these can lead to ingestion gaps, as Dynatrace collects all metrics every minute before sending them to the cluster.

### Monitoring methods

There are two distinct methods of monitoring technologies:

* The first method involves using the [Extensions 2.0ï»¿](https://dt-url.net/9t036yh) framework, which supports a handful of extensions for Prometheus exporters out of the box.

  This method provides comprehensive monitoring features, including technology-specific dashboards, alerting capabilities, topology visualization, and entity pages. However, this method operates outside of Kubernetes.
* The second method involves annotating Prometheus pods within Kubernetes to scrape Prometheus exporters.

  While this method provides a more Kubernetes-native approach, it currently offers minimal functional overlap with the features provided by the Extensions 2.0 framework.

These two methods serve different contexts, work independently from each other, and don't share the same metrics.

## Monitoring consumption

If you have DPS licensing, you can get more information about your environment's custom metric consumption from our [licensing documentation](/docs/license/capabilities/platform-extensions/custom-metrics-classic "Learn how your consumption of the Dynatrace Custom Metrics Classic DPS capability is billed and charged.").

* Full-Stack Monitoring [includes a fixed number of custom metric data points](/docs/license/capabilities/app-infra-observability/full-stack-monitoring#full-stack-metrics "Learn how your consumption of the Dynatrace Full-Stack Monitoring DPS capability is billed and charged.") for each GiB that contributes to your environment's GiB-hour consumption for containers with code-modules.

If you have Dynatrace classic licensing, Prometheus metrics in Kubernetes environments are subject to [DDU consumption](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

* Prometheus metrics from exporters running on hosts monitored by OneAgent are first deducted from your quota of [included metrics per host unit](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation#metrics-per-host-unit "Understand how to calculate Davis data unit consumption and costs related to monitored metrics."). After this quota is exceeded, any additional metrics consume [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").
* Prometheus metrics from exporters running on hosts not monitored by OneAgent always consume [DDUs](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

## Troubleshooting

To troubleshoot Prometheus integration issues, download the [Kubernetes Monitoring Statistics extensionï»¿](https://dt-url.net/n903xmb). For more information, see the community article on [How to troubleshoot missing Prometheus metricsï»¿](https://dt-url.net/3m02ozr).

## Related topics

* [Metrics Classic](/docs/analyze-explore-automate/metrics-classic "Learn about metrics classic that Dynatrace offers.")
* [Set up Dynatrace on Kubernetes](/docs/ingest-from/setup-on-k8s "Ways to deploy and configure Dynatrace on Kubernetes")