---
title: Send Micrometer metrics to Dynatrace
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer
scraped: 2026-02-17T21:20:50.636302
---

# Send Micrometer metrics to Dynatrace

# Send Micrometer metrics to Dynatrace

* Latest Dynatrace
* 7-min read
* Updated on Feb 09, 2026

[Micrometerï»¿](https://dt-url.net/7u039ck) is an open source instrumentation framework for JVM-based application metrics. It's used by [Spring Bootï»¿](https://dt-url.net/ba239ye) to record a wide range of metrics. You can ingest Micrometer and Spring Boot metrics and analyze them with Dynatrace Intelligence end-to-end in the context of your trace, log, and diagnostics data. With Dynatrace, you get intelligent AI-based observability and automatic root cause analysis for Spring Boot, 15+ pre-instrumented JVM-based frameworks and servers, and custom metrics.

You can use Micrometer in Dynatrace to:

* Ingest pre-instrumented metrics from Spring Boot applications
* Ingest pre-instrumented metrics from JVM-based frameworks, servers, and cache systems
* Define and ingest custom metrics

Metrics ingested from Micrometer consume [DDUs for custom metrics](/docs/license/monitoring-consumption-classic/davis-data-units/metric-cost-calculation "Understand how to calculate Davis data unit consumption and costs related to monitored metrics.").

There are two ways of using Micrometer:

* [As part of Spring Boot](#micrometer-with-spring-boot)
* [As a metrics facade used directly in your code](#directly)

## Prerequisites

* Micrometer version 1.8.0+
* Optional Spring Boot version 2.6.0+
* The registry dependency must be added to your project:

  Micrometer standalone

  Spring Boot

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace:latest.release'
  ```

  Maven

  Replace `{micrometer.version}` with the latest version of Micrometer or a specific version that you want to use.
  A list of released versions is available on [Maven Centralï»¿](https://dt-url.net/ay439b4).
  We recommend that you use the latest version.

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-dynatrace</artifactId>



  <version>{micrometer.version}</version>



  </dependency>
  ```

  The Spring Boot BOM specifies a Micrometer version that has been tested with the respective version of Spring Boot.
  It's therefore enough to specify the name of the dependency without specifying the version.
  This will result in the correct, matching version being pulled by Gradle or Maven.

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-dynatrace'
  ```

  Maven

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-dynatrace</artifactId>



  </dependency>
  ```

## Ingestion channels

You can use one of the following ingestion channels to send your Micrometer metrics:

* [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.")âneeds OneAgent installed on the monitored host.
* [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

## Dynatrace Micrometer registry

Micrometer uses the concept of a registry to export metrics to monitoring systems.

* For Micrometer version 1.8.0 or later, [Dynatrace Registry v2ï»¿](https://micrometer.io/docs/registry/dynatrace) is available. It exports metrics via the [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API."). All new integrations of Micrometer and Dynatrace must use this version.
* Older Micrometer versions are no longer supported (see [Dynatrace Micrometer registry v1 (legacy)](#registry-v1) below).

## Ingest metrics from Spring Boot apps

Micrometer can be configured via a `.properties` or `.yaml` file used for Spring Boot configuration.
Spring Boot automatically binds properties with the `management.dynatrace.metrics.export` prefix to the [Dynatrace configuration object](#dt-configuration-properties).

All configuration should be made through the property files. Manually creating a Micrometer `MeterRegistry` breaks the auto-configuration.

Property names for binding attributes from Spring Boot have changed in Spring Boot version 3.0.0. If you use a Spring Boot version before 3.0.0, use `management.metrics.export.dynatrace` instead of `management.dynatrace.metrics.export`.

With OneAgent (recommended)

With Dynatrace Operator for Kubernetes

Without OneAgent

OneAgent on Kubernetes nodes does not support the ingestion of Micrometer metrics directly. See [Sending Metrics from Kubernetes](#k8s-metrics) for more details. If you're using Dynatrace on Kubernetes, we recommend using Dynatrace Operator, which provides autoconfiguration.

For hosts that are monitored by OneAgent, automatic configuration is available. You don't need to specify the API endpoint to ingest the metricâif the **uri** parameter is not set in the configuration, the metric will be ingested via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

YAML

```
management.dynatrace.metrics.export:



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

Dynatrace Operator configures Dynatrace Micrometer registry by providing ingest URL, credentials and Kubernetes metadata. For configuration examples, see our [Dynakube examplesï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
For more information about metadata enrichment, see [the documentation on enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

* This feature is available when using Dynatrace Micrometer registry versions 1.9.0 and above.
* An app using the Dynatrace Micrometer registry and running in Kubernetes with a Dynatrace Operator does not require any explicit configuration. Dynatrace Operator and the registry will work together and automatically export Micrometer metrics to Dynatrace.
* Explicitly specifying the `management.dynatrace.metrics.export.uri` will overwrite automatic configuration and should be avoided when used with Dynatrace Operator.

YAML

```
management.dynatrace.metrics.export:



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

To ingest metrics from hosts where OneAgent is not installed, such as serverless deployments (for example, AWS ECS) or other non-Kubernetes environments, you need to use the [ingest endpoint of the Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API."). To learn how to use the endpoint, see the [POST ingest data points example](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API."). The Micrometer Dynatrace registry exports to this API when the URI and token are set.

Ensure that the URI is explicitly configured, as leaving it unset will default to `localhost`, and the OneAgent local ingest is not available in these environments.

HTTP clients connecting to the non-public ActiveGate REST endpoint must trust provided certificates. For details, see [Add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.").

You can use the Spring placeholder notation (for example, `api-token: ${YOUR_METRICS_INGEST_API_TOKEN}`), which will automatically read the environment variable and supply it to the Micrometer configuration.

YAML

```
management.dynatrace.metrics.export:



uri: "https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest"



# Read the environment variable YOUR_METRICS_INGEST_API_TOKEN and supply the value of the env var instead.



api-token: ${YOUR_METRICS_INGEST_API_TOKEN}



v2:



metric-key-prefix: "service.component"



enrich-with-dynatrace-metadata: true



default-dimensions:



stack: "prod"



region: "us-east-1"
```

.properties

```
management.dynatrace.metrics.export.uri=https://mySampleEnv.live.dynatrace.com/api/v2/metrics/ingest



management.dynatrace.metrics.export.api-token=${YOUR_METRICS_INGEST_API_TOKEN}



management.dynatrace.metrics.export.v2.metric-key-prefix=service.component



management.dynatrace.metrics.export.v2.enrich-with-dynatrace-metadata=true



management.dynatrace.metrics.export.v2.default-dimensions.stack=prod



management.dynatrace.metrics.export.v2.default-dimensions.region=us-east-1
```

## Ingest metrics directly from Micrometer

With OneAgent (recommended)

With Dynatrace Operator for Kubernetes

Without OneAgent

For hosts that are monitored by OneAgent, automatic configuration is available. You don't need to specify the API endpoint to ingest the metricâif the **uri** parameter is not set in the configuration, the metric will be ingested via the [OneAgent metric API](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api "Use the Dynatrace API to retrieve the metrics of monitored entities.").

View auto-configuration code

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

Dynatrace Operator configures Dynatrace Micrometer registry by providing ingest URL, credentials and Kubernetes metadata. For configuration examples, see our [Dynakube examplesï»¿](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
For more information about metadata enrichment, see [the documentation on enrichment files](/docs/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.").

* This feature is available when using Dynatrace Micrometer registry versions 1.9.0 and above.
* An app using the Dynatrace Micrometer registry and running in Kubernetes with a Dynatrace Operator does not require any explicit configuration. Dynatrace Operator and the registry will work together and automatically export Micrometer metrics to Dynatrace.
* Explicitly specifying the `management.dynatrace.metrics.export.uri` will overwrite automatic configuration and should be avoided when used with Dynatrace Operator.

View auto-configuration code

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(config).build();
```

To ingest metrics from hosts where OneAgent is not installed, such as serverless deployments (for example, AWS ECS) or other non-Kubernetes environments, you need to use the [ingest endpoint of the Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API."). To learn how to use the endpoint, see the [POST ingest data points example](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics#example "Ingest custom metrics to Dynatrace via Metrics v2 API."). The Micrometer Dynatrace registry exports to this API when the URI and token are set.

Ensure that the URI is explicitly configured, as leaving it unset will default to `localhost`, and the OneAgent local ingest is not available in these environments.

HTTP clients connecting to the non-public ActiveGate REST endpoint must trust provided certificates. For details, see [Add a custom certificate for ActiveGate](/docs/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.").

View manual configuration code

In this example, the metrics ingest URL and access token are read from environment variables `YOUR_METRICS_INGEST_URL` and `YOUR_METRICS_INGEST_TOKEN`. You should never store secrets in the code directly, but read them from a secure source.

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



public DynatraceApiVersion apiVersion() {



// Not strictly required, but makes the code more clear/explicit



return DynatraceApiVersion.V2;



}



@Override



public String uri() {



// The endpoint of the Dynatrace Metrics API v2 including path:



// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest"



String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");



return endpoint != null ? endpoint : DynatraceConfig.super.uri();



}



@Override



public String apiToken() {



// Should be read from a secure source



String token = System.getenv("YOUR_METRICS_INGEST_TOKEN");



return token != null ? token : "";



}



@Override



@Nullable



public String get(String k) {



// This method can be used for retrieving arbitrary config items;



// null means accepting the defaults defined in DynatraceConfig



return null;



}



};



DynatraceMeterRegistry registry = DynatraceMeterRegistry.builder(dynatraceConfig).build();
```

## Verify the metrics

After you have sent your metrics, verify the data in the [Data Explorer](/docs/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.") or [query them in Grail](/docs/platform/grail/dynatrace-query-language/commands/metric-commands#timeseries "DQL metric commands").

## Configuration properties

To set up the Dynatrace Micrometer registry, you can use the Dynatrace configuration object (`DynatraceConfig`). The object contains the parameters of metric ingestion and is used to construct the Dynatrace registry (`DynatraceMeterRegistry`), which is registered with Micrometer to ingest metrics to Dynatrace. You can set the following parameters:

Spring Boot

Directly in Micrometer

When using Spring Boot, entries in your `application.properties` or `application.yaml` files will be mapped to the `DynatraceConfig` object automatically.

Property

Description

Required

api-version

The version of the Dynatrace API to ingest data to Dynatrace:

* `V2` (default): [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").
* `V1`: [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.")

Optional

uri

The ingestion endpoint of the API.

Optional

metric-key-prefix

The prefix to be added to all ingested metric keys (for example, a namespace).

Optional

enrich-with-dynatrace-metadata

[Enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") (`true`) or do not enrich (`false`) ingested metrics with additional metadata.

If not set, `true` is used.

Optional

default-dimensions

A list of dimensions to be added to the ingested metrics.

Dimensions are defined as key-value pairs.

Optional

use-dynatrace-summary-instruments

Micrometer versions 1.9.x+ Ignore the Dynatrace-specific implementation for summary instruments (`Timer` and `DistributionSummary`).

The default (`true`) uses the new Instruments. Use `false` to fall back to 1.8.x behavior.

Optional

export-meter-metadata

Micrometer versions 1.12.x+ Turn meter metadata export (unit & description) on or off.

The default (`true`) configures the registry to export meter metadata. Use `false` to turn off metadata exporting.

Optional

Property

Description

Required

apiVersion

The version of the Dynatrace API to ingest data to Dynatrace:

* `V2` (default): [Metrics API v2](/docs/dynatrace-api/environment-api/metric-v2/post-ingest-metrics "Ingest custom metrics to Dynatrace via Metrics v2 API.").
* `V1`: [Timeseries API v1](/docs/dynatrace-api/environment-api/metric-v1/custom-metrics "Manage custom metrics via the Timeseries v1 API.")

Optional

uri

The ingestion endpoint of the API.

Optional

metricKeyPrefix

The prefix to be added to all ingested metric keys (for example, a namespace).

Optional

enrichWithDynatraceMetadata

[Enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") (`true`) or do not enrich (`false`) ingested metrics with additional metadata.

If not set, `true` is used.

Optional

defaultDimensions

A list of dimensions to be added to the ingested metrics.

Dimensions are defined as key-value pairs.

Optional

useDynatraceSummaryInstruments

Micrometer versions 1.9.x+ Ignore the Dynatrace-specific implementation for summary instruments (`Timer` and `DistributionSummary`).

The default (`true`) uses the new Instruments. Use `false` to fall back to 1.8.x behavior.

Optional

exportMeterMetadata

Micrometer versions 1.12.x+ Turn meter metadata export (unit & description) on or off.

The default (`true`) configures the registry to export meter metadata. Use `false` to turn off metadata exporting.

Optional

Code snippet to set properties

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



@Override



public DynatraceApiVersion apiVersion() {



// Defaults to V2 if not set explicitly.



return DynatraceApiVersion.V2;



}



@Override



public String uri() {



// The endpoint of the Dynatrace Metrics API v2 including path. For example:



// "https://{your-environment-id}.live.dynatrace.com/api/v2/metrics/ingest".



String endpoint = System.getenv("YOUR_METRICS_INGEST_URL");



return endpoint != null ? endpoint : DynatraceConfig.super.uri();



}



@Override



public String apiToken() {



// Should be read from a secure source



String token = System.getenv("YOUR_METRICS_INGEST_API_TOKEN");



return token != null ? token : "";



}



@Override



public String metricKeyPrefix() {



// Will be prepended to all metric keys



return "service.component";



}



@Override



public boolean enrichWithDynatraceMetadata() {



// On by default, but can be turned off explicitly.



return true;



}



@Override



public Map<String, String> defaultDimensions() {



// Create and return a map containing the desired key-value pairs.



Map<String, String> dims = new HashMap<>();



dims.put("dimensionKey", "dimensionValue");



return dims;



}



// Only available in Micrometer 1.9.0 and above.



@Override



public boolean useDynatraceSummaryInstruments() {



return false;



}



// Only available in Micrometer 1.12.0 and above.



@Override



public boolean exportMeterMetadata() {



return false;



}



@Override



@Nullable



public String get(String k) {



return null; // Accept the rest of the defaults



}



};
```

## Additional information

### Metric types

All metrics are transformed to follow the [Metric ingestion protocol types](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/metric-ingestion-protocol "Learn how the data ingestion protocol for Dynatrace Metrics API works.") used by Dynatrace.

Micrometer instrument

Dynatrace metric type

Gauge

`gauge,X`

Counter

`count,delta=X`

Timer

`gauge,min=X,max=Y,sum=Z,count=N`

DistributionSummary

`gauge,min=X,max=Y,sum=Z,count=N`

LongTaskTimer

`gauge,min=X,max=Y,sum=Z,count=N`

TimeGauge

`gauge,X`

FunctionCounter

`count,delta=X`

FunctionTimer

`gauge,min=X,max=Y,sum=Z,count=N`

Note that the `count` for LongTaskTimers can be misleading as it is likely to double-count depending on the export frequency. In case you require the current number of active tasks, exporting a separate Gauge is more reliable.

### Meter metadata

Starting with version 1.12.0 of the Dynatrace Micrometer registry, meter metadata (unit and description) is automatically exported to Dynatrace.
No code changes are required to start exporting metadata.
To turn off metadata export, use the following configuration:

Spring Boot

Directly in Micrometer

YAML

```
management:



metrics:



export:



dynatrace:



v2:



export-meter-metadata: false  # default: true
```

.properties

```
management.dynatrace.metrics.export.v2.export-meter-metadata=false
```

Meter metadata was introduced with Micrometer 1.12.0, which was first included in Spring Boot 3.2.0.
The toggles described above are therefore available from Spring Boot 3.2.0.

Code snippet to set properties

```
DynatraceConfig dynatraceConfig = new DynatraceConfig() {



// Only available in Micrometer 1.12.0 and above.



@Override



public boolean exportMeterMetadata() {



return false;



}



@Override



@Nullable



public String get(String k) {



return null; // Accept the rest of the defaults



}



};
```

For previous versions of Micrometer, metadata needs to be specified manually using either the Dynatrace API or web UI.
For more information, see [Custom metric metadata](/docs/ingest-from/extend-dynatrace/extend-metrics/reference/custom-metric-metadata "Provide metadata for your custom metric.").

### Sending metrics from Kubernetes

OneAgent cannot be used for Micrometer metric ingestion on Kubernetes nodes. You can configure your Micrometer setup to push metrics directly to Dynatrace using the [Metrics API](/docs/dynatrace-api/environment-api/metric-v2 "Retrieve metric information via Metrics v2 API.").

### Capture JVM metrics in Micrometer

By default, JVM metrics are turned off when running Micrometer without Spring Boot. To learn how to enable them, see the [Micrometer documentationï»¿](https://docs.micrometer.io/micrometer/reference/reference/jvm.html). After they are enabled and registered with the Dynatrace registry (`DynatraceMeterRegistry`), JVM metrics are recorded and sent to Dynatrace automatically.

On hosts that are monitored by OneAgent, these metrics might already be captured by OneAgent.

### Restrict ingestion of specific metrics

Spring Boot

Directly in Micrometer

When running Micrometer in Spring Boot, [many metricsï»¿](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.metrics.supported) are automatically created and sent to Dynatrace, including JVM, process, and disk metrics.

To see all metrics created by your Spring Boot application, navigate to the [actuator endpoint on your Spring Boot appï»¿](https://docs.spring.io/spring-boot/docs/current/reference/html/actuator.html#actuator.enabling) (`/actuator/metrics`). Some of these metrics might already be captured by OneAgent.

### Disable metrics with Spring properties

Metrics can be disabled based on their prefix in the Spring Boot configuration. To find out which metrics can be excluded, check your Spring Boot applications actuator endpoint. Be sure to **exclude** your custom metric key prefix (if any, see [`metric-key-prefix`](#dt-configuration-properties)) when using this feature.

YAML

```
management.metrics.enable:



# disable jvm.memory metrics



jvm.memory: false



# disable all jvm metrics:



jvm: false
```

.properties

```
# disable jvm.memory metrics



management.metrics.enable.jvm.memory=false



# disable all jvm metrics



management.metrics.enable.jvm=false
```

It is also possible to disable all metrics first and then only re-enable the desired ones:

YAML

```
management.metrics.enable:



# disable all metrics



all: false



# re-enable only jvm.* metrics



jvm: true
```

.properties

```
# disable all metrics



management.metrics.enable.all=false



# re-enable jvm.* metrics



management.metrics.enable.jvm=true
```

### Disable metrics in code

Micrometer provides [meter filtersï»¿](https://docs.micrometer.io/micrometer/reference/concepts/meter-filters.html) to disable metrics based on a variety of conditions. Meter filters can also be configured via Spring Boot with the `@Configuration` annotation.

Show code snippet

```
@Configuration(proxyBeanMethods = false)



public class MyMeterRegistryConfiguration {



@Bean



public MeterRegistryCustomizer<MeterRegistry> metricsCommonTags() {



return registry -> registry.config()



.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));



}



}
```

The metric prefix configured for the Dynatrace registry will be applied after filtering, so properties to enable or disable metrics have to be specified using the original metric key without this prefix.

Register MeterFilters before creating or [turning on additional metrics](#add-automatically-created-metrics), as the `MeterFilter` will only be evaluated when the metric is added to the `MeterRegistry`.

You can configure the registry to filter out specific metrics by name and/or tags (for example, metrics that are already captured by OneAgent). To achieve that, use Micrometer's [meter filtersï»¿](https://micrometer.io/docs/concepts#_meter_filters). You need to add meter filters before you enable [capture of JVM metrics](#add-automatically-created-metrics), otherwise filters will be overridden.

The metric prefix configured for the Dynatrace registry will be applied after filtering, so `meterFilters` have to be specified using the original metric key without this prefix.

Disable metrics in code

```
// Disable all metrics with metric names starting with jvm.gc



registry.config()



.meterFilter(MeterFilter.denyNameStartsWith("jvm.gc"));
```

### Troubleshooting with logs

Spring Boot

Directly in Micrometer

Spring handles the logging when using Micrometer in the Spring Boot context. The log level for the Micrometer Dynatrace registry can be set via configuration properties.

YAML

```
logging.level.io.micrometer.dynatrace: DEBUG
```

.properties

```
logging.level.io.micrometer.dynatrace=DEBUG
```

Micrometer and the Dynatrace Micrometer registry use [slf4jï»¿](https://www.slf4j.org/) internally to log events, such as the lines that are sent to Dynatrace.
If you want to get this information, set up your project with the logging framework of your choice (for example, [logbackï»¿](https://logback.qos.ch/manual/configuration.html#automaticConf)) and set the log level to `debug`.

Debug logging with logback

When using the default logback implementation, debug logging to the console is enabled by default. In order to add logback to your project and log debug information, add the following dependency:

```
implementation 'ch.qos.logback:logback-classic:latest.release'
```

### Dynatrace summary instruments

Starting with Micrometer version 1.9.x, specialized instruments are used in the Dynatrace meter registry for certain summary instruments (`DynatraceTimer` and `DynatraceDistributionSummary`). Their purpose is to get around a peculiarity in how Micrometer records metrics, which, in some cases, led to metrics being rejected by Dynatrace for having an invalid format. The specialized instruments, tailored to Dynatrace metrics ingestion, prevent the creation of invalid metrics.

* They are available from version 1.9.0 and are used as a drop-in replacement by default. No action is needed from users upgrading to 1.9.0.
* If there's a discrepancy in the observed metrics, it's possible to return to the previous behavior by setting the `useDynatraceSummaryInstruments` toggle to `false`.

## Dynatrace Micrometer registry v1 Deprecated

Timeseries v1 API deprecation

The [Timeseries v1 API](/docs/dynatrace-api/environment-api/metric-v1 "Retrieve metric information via Timeseries v1 API.") is deprecated and no longer accepts data. Please migrate to the supported exporter as described on this page.