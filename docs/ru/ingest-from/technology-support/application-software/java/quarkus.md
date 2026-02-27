---
title: Red Hat Quarkus native applications monitoring
source: https://www.dynatrace.com/docs/ingest-from/technology-support/application-software/java/quarkus
scraped: 2026-02-27T21:25:25.165095
---

# Red Hat Quarkus native applications monitoring

# Red Hat Quarkus native applications monitoring

* Latest Dynatrace
* 3-min read
* Updated on Jan 28, 2026

[Red Hat Quarkusï»¿](https://www.redhat.com/en/topics/cloud-native-apps/what-is-quarkus) is an open source Java framework optimized for GraalVM Native Images to make Java a valuable citizen in the world of microservices. Quarkus belongs to the family of full-stack frameworks tailored for Kubernetes. It includes modern Java libraries and follows the latest Java standards.

Learn how Dynatrace can trace native Java applications and monitor metrics and logs of a Quarkus application compiled as a native image.

## Prerequisites

* Your GraalVM version is [supported by Dynatrace](/docs/ingest-from/technology-support#java-native-image "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* GraalVM is configured to build native images. For details, see the [Building a native executableï»¿](https://quarkus.io/guides/building-native-image) Quarkus guide.
* OneAgent or Dynatrace Operator is installed on the machine where the application is about to be executed.

  The required installation depends on your application:

  | If your application is running | See the instruction for |
  | --- | --- |
  | on a virtual machine or bare-metal | [OneAgent](/docs/ingest-from/dynatrace-oneagent/installation-and-operation "Install OneAgent on a server for the very first time.") |
  | as workload in Kubernetes or OpenShift | [Dynatrace Operator](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes") |

## Traces

Dynatrace can automatically trace just-in-time (JIT) compiled Quarkus applications executed on OpenJDK HotSpot JVM and GraalVM.

For ahead-of-time (AOT) compiled Quarkus applications executed on GraalVM, see [GraalVM Native Image](/docs/ingest-from/technology-support/application-software/java/graalvm-native-image "Install, configure, and manage Dynatrace GraalVM Native Image module.") to get started.

#### OpenTelemetry

You can export Quarkus tracing information using [OpenTelemetry](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Simplified setup options when monitored by OneAgent

If your environment is monitored by OneAgent, you have those simplified configuration options available:

* **[OneAgent OpenTelemetry Span Sensor](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#oneagent-otel-span-sensor "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")** Recommended: Automatically captures OpenTelemetry API calls and stitches them into OneAgent traces without requiring manual OTLP export configuration. To use this approach, [enable the OpenTelemetry Span Sensor](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.") and **don't** configure manual OTLP export.
* **[Local OTLP endpoint via EEC](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Learn how to send OpenTelemetry data to a Dynatrace OneAgent.")**: For non-containerized environments, you can send traces to the local OTLP endpoint at `http://localhost:14499/otlp/v1/traces` after [enabling the Extension Execution Controller](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel#send-opentelemetry-traces-to-the-otlp-endpoint-exposed-by-oneagent "Learn how to send OpenTelemetry data to a Dynatrace OneAgent."). This eliminates the need for API tokens and external endpoints.

If you prefer a OneAgent-based method, skip the manual configuration below.

If you prefer manual configuration or donât use OneAgent, follow the steps below.

To manually configure OpenTelemetry export, use the [Quarkus-specific configuration parametersï»¿](https://dt-url.net/3g039zt) to configure the exporter to send trace data to one of the two available endpoints, [ActiveGate or OneAgent](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The following example shows how to configure `application.properties` to export to a Dynatrace SaaS endpoint. It specifies the API URL and the necessary, percent-encoded [`Authorization` header](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") with the API token.

```
quarkus.application.name=myservice



quarkus.otel.exporter.otlp.traces.endpoint=https://{your-environment-id}.live.dynatrace.com/api/v2/otlp



quarkus.otel.exporter.otlp.traces.headers=authorization=Api-Token%20dt.....



quarkus.log.console.format=%d{HH:mm:ss} %-5p traceId=%X{traceId}, parentId=%X{parentId}, spanId=%X{spanId}, sampled=%X{sampled} [%c{2.}] (%t) %s%e%n
```

## Metrics

Red Hat recommends that you obtain metrics from Quarkus via the `quarkus-micrometer-registry-prometheus` library.

To learn how to utilize Micrometer metrics in your Quarkus application, see the [Micrometer metricsï»¿](https://quarkus.io/guides/micrometer) Quarkus guide.

Dynatrace offers two approaches for obtaining Micrometer metrics from Prometheus: via API or via an extension.

### Ingest Micrometer metrics via Dynatrace API

Use the Dynatrace API to ingest metrics obtained from the `quarkus-micrometer-registry-prometheus` library.

To learn more about the ingestion procedure, see [Send Micrometer metrics to Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Learn how to send Micrometer metrics to Dynatrace.").

For natively built applications, be sure to follow the [Directly in Micrometer](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer#properties-direct "Learn how to send Micrometer metrics to Dynatrace.") approach.

### Ingest Micrometer metrics via an extension

Use the Dynatrace [Extension 2.0 Framework](/docs/ingest-from/extensions "Learn how to create and manage Dynatrace Extensions.") to ingest Micrometer metrics obtained from the [Prometheus data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")âyou need to create a custom extension for that.

As a starting point, you can use the custom extension example below. It's tailored to the `quarkus-micrometer-registry-prometheus` library. Be sure to use the correct metrics endpoint in your configuration. The default endpoint is `localhost:8080/q/metrics`.

Extension example based on Prometheus

```
name: custom:com.dynatrace.extension.micrometer-quarkus



version: 1.0.0



minDynatraceVersion: "1.247"



author:



name: Dynatrace



#dashboards:



#  - path: "dashboards/dashboard_exporter.json"



#alerts:



#  - path: "alerts/alert_socket_usage.json"



prometheus:



- group: quarkus metrics



interval:



minutes: 1



featureSet: all



dimensions:



- key: quarkus



value: const:quarkus



subgroups:



# global counters



- subgroup: quarkus global counter



dimensions:



- key: global_counters



value: const:global_counters



metrics:



# HELP process_uptime_seconds The uptime of the Java virtual machine



# TYPE process_uptime_seconds gauge



- key: com.dynatrace.process.global.uptime.seconds



value: metric:process_uptime_seconds



type: gauge



featureSet: global



# HELP process_cpu_usage The "recent cpu usage" for the Java Virtual Machine process



# TYPE process_cpu_usage gauge



- key: com.dynatrace.process.global.cpu.usage



value: metric:process_cpu_usage



type: gauge



featureSet: global



# HELP system_cpu_usage The "recent cpu usage" of the system the application is running in



# TYPE system_cpu_usage gauge



- key: com.dynatrace.system.global.cpu.usage



value: metric:system_cpu_usage



type: gauge



featureSet: global



# HELP jvm_classes_unloaded_classes_total The total number of classes unloaded since the Java virtual machine has started execution



# TYPE jvm_classes_unloaded_classes_total counter



- key: com.dynatrace.jvm.classes.global.uploaded.total



value: metric:jvm_classes_unloaded_classes_total



type: count



featureSet: global



# HELP jvm_info_total JVM version info



# TYPE jvm_info_total counter



- key: com.dynatrace.jvm.global.info.total



value: metric:jvm_info_total



type: count



featureSet: global



# HELP http_server_connections_seconds_max



# TYPE http_server_connections_seconds_max gauge



- key: com.dynatrace.http.server.connections.seconds.global.max



value: metric:http_server_connections_seconds_max



type: gauge



featureSet: global



# HELP http_server_connections_seconds



# TYPE http_server_connections_seconds summary



- key: com.dynatrace.http.server.connections.seconds.active.global.count



value: metric:http_server_connections_seconds_active_count



type: count



featureSet: global



- key: com.dynatrace.http.server.connections.seconds.active.global.duration.summary



value: metric:http_server_connections_seconds_duration_sum



type: gauge



featureSet: global



# HELP process_files_max_files The maximum file descriptor count



# TYPE process_files_max_files gauge



- key: com.dynatrace.process.files.global.max



value: metric:process_files_max_files



type: gauge



featureSet: global



# HELP http_server_bytes_written_max



# TYPE http_server_bytes_written_max gauge





- key: com.dynatrace.http.server.bytes.wrriten.global.max



value: metric:http_server_bytes_written_max



type: gauge



featureSet: global



# HELP http_server_bytes_written



# TYPE http_server_bytes_written summary



- key: com.dynatrace.http.server.bytes.written.global.count



value: metric:http_server_bytes_written_count



type: count



featureSet: global



- key: com.dynatrace.http.server.bytes.written.global.summary



value: metric:http_server_bytes_written_sum



type: gauge



featureSet: global



# HELP system_load_average_1m The sum of the number of runnable entities queued to available processors and the number of runnable entities running on the available processors averaged over a period of time



# TYPE system_load_average_1m gauge



- key: com.dynatrace.system.load.average.global.lm



value: metric:system_load_average_1m



type: gauge



featureSet: global



# HELP jvm_gc_overhead_percent An approximation of the percent of CPU time used by GC activities over the last lookback period or since monitoring began, whichever is shorter, in the range [0..1]



# TYPE jvm_gc_overhead_percent gauge



- key: com.dynatrace.jvm.gc.overhead.global.percent



value: metric:jvm_gc_overhead_percent



type: gauge



featureSet: global



# HELP jvm_threads_daemon_threads The current number of live daemon threads



# TYPE jvm_threads_daemon_threads gauge



- key: com.dynatrace.jvm.threads.daemon.global.threads



value: metric:jvm_threads_daemon_threads



type: gauge



featureSet: global



# HELP jvm_threads_live_threads The current number of live threads including both daemon and non-daemon threads



# TYPE jvm_threads_live_threads gauge



- key: com.dynatrace.jvm.threads.live.global.threads



value: metric:jvm_threads_live_threads



type: gauge



featureSet: global



# HELP http_server_requests_seconds



# TYPE http_server_requests_seconds summary



- key: com.dynatrace.http.server.bytes.written.global.count



value: metric:http_server_requests_seconds_count



type: count



featureSet: global



- key: com.dynatrace.http.server.bytes.written.global.summary



value: metric:http_server_requests_seconds_sum



type: gauge



featureSet: global



# HELP http_server_requests_seconds_max



# TYPE http_server_requests_seconds_max gauge



- key: com.dynatrace.http.server.requests.seconds.max



value: metric:http_server_requests_seconds_max



type: gauge



featureSet: global



# HELP process_start_time_seconds Start time of the process since unix epoch.



# TYPE process_start_time_seconds gauge



- key: com.dynatrace.process.start.time.global.seconds



value: metric:process_start_time_seconds



type: gauge



featureSet: global



# HELP jvm_classes_loaded_classes The number of classes that are currently loaded in the Java virtual machine



# TYPE jvm_classes_loaded_classes gauge



- key: com.dynatrace.jvm.classes.loaded.global.max



value: metric:jvm_classes_loaded_classes



type: gauge



featureSet: global



# HELP jvm_threads_peak_threads The peak live thread count since the Java virtual machine started or peak was reset



# TYPE jvm_threads_peak_threads gauge



- key: com.dynatrace.jvm.threads.peak.global.threads



value: metric:jvm_threads_peak_threads



type: gauge



featureSet: global



# HELP system_cpu_count The number of processors available to the Java virtual machine



# TYPE system_cpu_count gauge



- key: com.dynatrace.system.cpu.global.counter



value: metric:system_cpu_count



type: gauge



featureSet: global



# HELP process_files_open_files The open file descriptor count



# TYPE process_files_open_files gauge



- key: com.dynatrace.process.files.open.global.files



value: metric:process_files_open_files



type: gauge



featureSet: global
```

## Logs

Dynatrace offers [various options](/docs/ingest-from/extend-dynatrace/extend-logs "Learn how to extend log observability in Dynatrace.") for collecting logs from your applications and environments.

To learn how to set up logging in your Quarkus application, see the [Configuring loggingï»¿](https://quarkus.io/guides/logging) Quarkus guide.

For the procedure below, we assume your application writes logs to the `/var/log/quarkus-app.log` file.

1. Start your Quarkus native application.
2. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic** and select your host.
3. Scroll down to the **Process analysis** section and, in the list of processes, select the process of your Quarkus native application.
4. On the right side of the **Process** panel, select ![More](https://dt-cdn.net/images/more-icon-01c8b008ca.svg "More") > **Settings**.
5. In the process group settings, select **Log monitoring** > **Add new log for monitoring**.
6. Enter the full path of your log file. Be sure to follow the [log path requirements](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-manually-v2#considerations-for-adding-text-log-files-manually "Learn how to manually add log files for analysis.").
7. Select **Save changes**.
8. [Include the added log files](/docs/analyze-explore-automate/log-monitoring/acquire-log-data/add-log-files-sources-v2 "Learn how to include and exclude log sources for analysis.") in your log storage.

## Related topics

* [Send Micrometer metrics to Dynatrace](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer "Learn how to send Micrometer metrics to Dynatrace.")
* [Manage Prometheus extensions](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/prometheus/prometheus-extensions "Learn how to extend observability in Dynatrace with declarative Prometheus metrics ingestion.")
* [Prometheus data source](/docs/ingest-from/extensions/develop-your-extensions/data-sources/prometheus-extensions "Learn how to create a Prometheus extension using the Extensions framework.")
* [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.")