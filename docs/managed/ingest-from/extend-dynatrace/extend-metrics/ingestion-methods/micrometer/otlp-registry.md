---
title: Send Micrometer metrics with the OTLP registry
source: https://docs.dynatrace.com/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer/otlp-registry
---

# Send Micrometer metrics with the OTLP registry

# Send Micrometer metrics with the OTLP registry

* 5-min read
* Published Jul 23, 2026

The [Micrometer OTLP registry﻿](https://docs.micrometer.io/micrometer/reference/implementations/otlp.html) exports [Micrometer﻿](https://dt-url.net/7u039ck) metrics over the OpenTelemetry Protocol (OTLP). It's an alternative to the [Dynatrace registry](/managed/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/micrometer/dynatrace-registry "Learn how to send Micrometer metrics to Dynatrace using the Dynatrace Micrometer registry.") for teams that want to standardize on OpenTelemetry across their applications.

Using the OTLP registry, your Micrometer metrics are exported the same way as any other OpenTelemetry signal, so you can rely on standard OpenTelemetry resource attributes and configuration conventions.

## Prerequisites

* Micrometer version 1.13.15+
* Optional Spring Boot version 4.1.x+
* The registry dependency must be added to your project:

  Micrometer standalone

  Spring Boot

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-otlp:latest.release'
  ```

  Maven

  Replace `{micrometer.version}` with the latest version of Micrometer or a specific version that you want to use.
  A list of released versions is available on [Maven Central﻿](https://central.sonatype.com/artifact/io.micrometer/micrometer-registry-otlp/versions).
  We recommend that you use the latest version.

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-otlp</artifactId>



  <version>{micrometer.version}</version>



  </dependency>
  ```

  The Spring Boot BOM specifies a Micrometer version that has been tested with the respective version of Spring Boot.
  It's therefore enough to specify the name of the dependency without specifying the version.
  This will result in the correct, matching version being pulled by Gradle or Maven.

  Gradle

  ```
  implementation 'io.micrometer:micrometer-registry-otlp'
  ```

  Maven

  ```
  <dependency>



  <groupId>io.micrometer</groupId>



  <artifactId>micrometer-registry-otlp</artifactId>



  </dependency>
  ```

## Ingest metrics from Spring Boot apps

With Dynatrace Operator for Kubernetes

Export to the OpenTelemetry Collector

Standalone

The Dynatrace Operator automatically configures the OTLP exporter by injecting the standard OpenTelemetry environment variables (such as `OTEL_EXPORTER_OTLP_ENDPOINT` and `OTEL_EXPORTER_OTLP_HEADERS`) and Kubernetes resource attributes into your pod. No explicit Spring Boot configuration is required: having the `io.micrometer:micrometer-registry-otlp` dependency on the classpath is enough.

For the full list of supported environment variables, see the [Spring Boot OpenTelemetry environment variables reference﻿](https://docs.spring.io/spring-boot/reference/actuator/observability.html#actuator.observability.opentelemetry.environment-variables).

For configuration examples, see [Dynakube examples﻿](https://github.com/Dynatrace/dynatrace-operator/tree/main/assets/samples/dynakube).
For more information about metadata enrichment, see [the documentation on enrichment files](/managed/ingest-from/extend-dynatrace/extend-data#operator-enrichment-directory "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.").

Dynatrace Operator's environment variable injection is all-or-nothing per pod. If **any** `OTEL_EXPORTER_OTLP_*` variable is already present in your container spec (regardless of which signal it targets: `_METRICS_*`, `_LOGS_*`, `_TRACES_*`), the Operator skips injecting all signal-specific OTLP variables. Only `OTEL_RESOURCE_ATTRIBUTES` continues to be injected in that case.

To ensure Dynatrace Operator manages the full OTLP configuration, do not set any `OTEL_EXPORTER_OTLP_*` variables manually in your pod or container spec.

### 1. Configure the OTLP exporter settings

Routing metrics through an [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") lets you centralize cross-cutting configuration, such as the endpoint URL, authentication, batching, and [enrichment](#enrich), in the Collector rather than in each application. For an example Collector configuration that receives OTLP data and forwards it to Dynatrace, see [Configuration example](/managed/ingest-from/opentelemetry/collector/configuration#configuration-example "How to configure the OpenTelemetry Collector.").

Spring Boot's OTLP export already targets a local Collector on `http://localhost:4318/v1/metrics` by default, so you don't need to set a URL or token for a local Collector. Set `management.otlp.metrics.export.url` only when your Collector runs elsewhere.

You must still set the aggregation temporality to `delta`, because the default is `cumulative` and Dynatrace requires `delta`.

**YAML**

```
management:



otlp:



metrics:



export:



# url: set only for a remote Collector; defaults to http://localhost:4318/v1/metrics



aggregationTemporality: delta
```

**.properties**

```
# management.otlp.metrics.export.url= set only for a remote Collector; defaults to http://localhost:4318/v1/metrics



management.otlp.metrics.export.aggregationTemporality=delta
```

### 1. Configure the OTLP exporter settings

To send metrics directly to Dynatrace, for example from serverless deployments (such as AWS ECS) or other non-Kubernetes environments, use the [OTLP metrics ingest API](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics "Learn how Dynatrace ingests OpenTelemetry metrics."). For the endpoint URL and token format, see [URL examples](/managed/ingest-from/opentelemetry/otlp-api#url-examples "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

Ensure that the URL is explicitly configured, as leaving it unset will default to the OpenTelemetry collector on `localhost:4318`.

You can use the Spring placeholder notation (for example, `Authorization: Api-Token ${YOUR_METRICS_INGEST_API_TOKEN}`), which will automatically read the environment variable and supply it to the Micrometer configuration.

HTTP clients connecting to the non-public ActiveGate REST endpoint must trust provided certificates. For details, see [Add a custom certificate for ActiveGate](/managed/ingest-from/setup-on-k8s/guides/networking-security-compliance/network-configurations "Configure Dynatrace in network-restricted environments, network-related settings and proxy configurations.").

**YAML**

```
management:



otlp:



metrics:



export:



url: "https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics"



aggregationTemporality: delta



headers:



Authorization: "Api-Token ${YOUR_METRICS_INGEST_API_TOKEN}"
```

**.properties**

```
management.otlp.metrics.export.url=https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics



management.otlp.metrics.export.aggregationTemporality=delta



management.otlp.metrics.export.headers.Authorization=Api-Token ${YOUR_METRICS_INGEST_API_TOKEN}
```

To enrich these metrics with Dynatrace metadata, see [Enrich your metrics](#enrich).

## Ingest metrics directly from Micrometer

With Dynatrace Operator for Kubernetes

Export to the OpenTelemetry Collector

Standalone

Dynatrace Operator automatically injects the standard `OTEL_EXPORTER_OTLP_*` environment variables into your pod, so no explicit endpoint or token configuration is required.

However, the ActiveGate running in the Kubernetes cluster uses a self-signed certificate that is not trusted by the JVM by default. Unlike Spring Boot, Micrometer does not support the `OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE` environment variable natively (tracked in a [Micrometer issue﻿](https://github.com/micrometer-metrics/micrometer/issues/6921)), so you need to provide a custom HTTP sender that reads this variable and builds a scoped `SSLContext`.

### 1. Create a custom HTTP sender that trusts the ActiveGate certificate

Create the following `JdkClientHttpSender` class:

```
import io.micrometer.core.ipc.http.HttpSender;



import javax.net.ssl.SSLContext;



import javax.net.ssl.TrustManagerFactory;



import java.io.FileInputStream;



import java.io.IOException;



import java.io.InputStream;



import java.net.URI;



import java.net.http.HttpClient;



import java.net.http.HttpRequest;



import java.net.http.HttpResponse;



import java.security.KeyStore;



import java.security.cert.Certificate;



import java.security.cert.CertificateFactory;



import java.time.Duration;



class JdkClientHttpSender implements HttpSender {



private final HttpClient httpClient;



JdkClientHttpSender() throws Exception {



HttpClient.Builder builder = HttpClient.newBuilder()



.connectTimeout(Duration.ofSeconds(10));



SSLContext sslContext = buildSslContextIfCertPresent();



if (sslContext != null) {



builder.sslContext(sslContext);



}



this.httpClient = builder.build();



}



@Override



public Response send(Request request) throws IOException {



HttpRequest.Builder httpRequest = HttpRequest.newBuilder()



.uri(URI.create(request.getUrl().toString()))



.timeout(Duration.ofSeconds(30));



request.getRequestHeaders().forEach(httpRequest::header);



httpRequest.method(request.getMethod().name(),



HttpRequest.BodyPublishers.ofByteArray(request.getEntity()));



try {



HttpResponse<String> response = this.httpClient.send(



httpRequest.build(), HttpResponse.BodyHandlers.ofString());



return new Response(response.statusCode(), response.body());



} catch (InterruptedException ex) {



Thread.currentThread().interrupt();



throw new IOException("HTTP request interrupted", ex);



}



}



private static SSLContext buildSslContextIfCertPresent() throws Exception {



String certPath = System.getenv("OTEL_EXPORTER_OTLP_METRICS_CERTIFICATE");



if (certPath == null || certPath.isBlank()) return null;



KeyStore trustStore = KeyStore.getInstance(KeyStore.getDefaultType());



trustStore.load(null, null);



CertificateFactory cf = CertificateFactory.getInstance("X.509");



try (InputStream is = new FileInputStream(certPath)) {



Certificate cert = cf.generateCertificate(is);



trustStore.setCertificateEntry("custom-ca", cert);



}



TrustManagerFactory tmf = TrustManagerFactory.getInstance(TrustManagerFactory.getDefaultAlgorithm());



tmf.init(trustStore);



SSLContext sslContext = SSLContext.getInstance("TLS");



sslContext.init(null, tmf.getTrustManagers(), null);



return sslContext;



}



}
```

### 2. Create the registry using the custom sender

`OtlpConfig.DEFAULT` still picks up all other `OTEL_*` environment variables:

```
OtlpMeterRegistry registry = OtlpMeterRegistry.builder(OtlpConfig.DEFAULT)



.metricsSender(new OtlpHttpMetricsSender(new JdkClientHttpSender()))



.build();
```

Dynatrace Operator's environment variable injection is all-or-nothing per pod. If **any** `OTEL_EXPORTER_OTLP_*` variable is already present in your container spec (regardless of which signal it targets: `_METRICS_*`, `_LOGS_*`, `_TRACES_*`), the Operator skips injecting all signal-specific OTLP variables. Only `OTEL_RESOURCE_ATTRIBUTES` continues to be injected in that case.

To ensure the Operator manages the full OTLP configuration, do not set any `OTEL_EXPORTER_OTLP_*` variables manually in your pod or container spec.

### 1. Set the required OTLP environment variables

Routing metrics through an [OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector "Learn how to use the OpenTelemetry Collector, including the Dynatrace OTel Collector, to ingest telemetry from OpenTelemetry.") lets you centralize cross-cutting configuration, such as the endpoint URL, authentication, batching, and [enrichment](#enrich), in the Collector rather than in each application. For an example Collector configuration that receives OTLP data and forwards it to Dynatrace, see [Configuration example](/managed/ingest-from/opentelemetry/collector/configuration#configuration-example "How to configure the OpenTelemetry Collector.").

The OTLP registry endpoint already defaults to `http://localhost:4318/v1/metrics`, so a local Collector needs no endpoint configuration. Set `OTEL_EXPORTER_OTLP_METRICS_ENDPOINT` only when your Collector runs elsewhere. You must still request `delta` temporality, because the default is `cumulative` and Dynatrace requires delta:

```
# OTEL_EXPORTER_OTLP_METRICS_ENDPOINT= set only for a remote Collector; defaults to http://localhost:4318/v1/metrics



OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

### 2. Create the registry

Create the registry using the default config, which picks up all `OTEL_*` variables automatically:

```
OtlpMeterRegistry registry = new OtlpMeterRegistry();
```

### 1. Set the required OTLP environment variables

The OTLP registry supports configuration via OpenTelemetry environment variables. Set the following environment variables before starting your application:

```
OTEL_EXPORTER_OTLP_METRICS_ENDPOINT=https://{your-environment-id}.live.dynatrace.com/api/v2/otlp/v1/metrics



OTEL_EXPORTER_OTLP_HEADERS=Authorization=Api-Token ${YOUR_METRICS_INGEST_API_TOKEN}



OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

For the endpoint URL and token format, see [URL examples](/managed/ingest-from/opentelemetry/otlp-api#url-examples "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

### 2. Set optional variables to identify your service

Optional

You can also set the following optional variables to identify your service:

```
OTEL_SERVICE_NAME=my-service



OTEL_RESOURCE_ATTRIBUTES=deployment.environment=production,team=backend
```

### 3. Create the registry

Create the registry using the default config, which picks up all `OTEL_*` variables automatically:

```
OtlpMeterRegistry registry = new OtlpMeterRegistry();
```

For all supported configuration options, see the [Micrometer OTLP registry documentation﻿](https://docs.micrometer.io/micrometer/reference/implementations/otlp.html#_configuring).

To enrich these metrics with Dynatrace metadata, see [Enrich your metrics](#enrich).

## Enrich your metrics

Enrichment adds Dynatrace metadata (host, process group, and Kubernetes attributes) to your metrics so they are associated with the right entities in the topology model.

Enrichment applies to the **Standalone** and **Export to the OpenTelemetry Collector** setups. The **Dynatrace Operator** setup enriches your metrics automatically, so you can skip this section when you use the Operator.

### Enrich with the OpenTelemetry Collector

If you export your metrics to an OpenTelemetry Collector, enrich them at the Collector level:

* **Non-containerized environments**: Use the Resource Detection processor with the `dynatrace` detector. For the configuration, see [Enrich OTLP with OneAgent data](/managed/ingest-from/opentelemetry/collector/use-cases/enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with OneAgent host data.").
* **Kubernetes**: Use the Kubernetes attributes processor to attach pod, namespace, and node metadata. For the configuration, see [Enrich Kubernetes data with the OpenTelemetry Collector](/managed/ingest-from/opentelemetry/collector/use-cases/kubernetes/k8s-enrich "Configure the OpenTelemetry Collector to enrich OTLP requests with Kubernetes data.").

### Enrich manually with OneAgent metadata

When OneAgent runs on the host but you export metrics directly to Dynatrace (the **Standalone** setup), the OTLP registry does not read OneAgent enrichment data automatically. Add custom code that reads the [OneAgent metadata enrichment file](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") and adds the attributes to your meter registry.

Spring Boot

Micrometer standalone

### 1. Add the Dynatrace metric utils dependency

Add the `dynatrace-metric-utils-java` dependency, which reads the OneAgent metadata enrichment file:

**Gradle**

```
implementation 'com.dynatrace.metric.util:dynatrace-metric-utils-java:2.5.0'
```

**Maven**

```
<dependency>



<groupId>com.dynatrace.metric.util</groupId>



<artifactId>dynatrace-metric-utils-java</artifactId>



<version>2.5.0</version>



</dependency>
```

### 2. Create a helper class to read the enrichment metadata

Create a helper class that reads the OneAgent enrichment metadata and converts it to Micrometer tags:

```
import com.dynatrace.metric.util.MetricException;



import com.dynatrace.metric.util.MetricLinePreConfiguration;



import io.micrometer.core.instrument.Tag;



import java.util.List;



public final class DtMetadata {



private DtMetadata() {}



public static List<Tag> readEnrichmentTags() {



try {



MetricLinePreConfiguration preConfig = MetricLinePreConfiguration.builder()



.dynatraceMetadataDimensions()



.build();



return preConfig.getDynatraceMetadataDimensions().entrySet().stream()



.map(e -> Tag.of(e.getKey(), e.getValue()))



.toList();



} catch (MetricException e) {



return List.of();



}



}



}
```

### 3. Register the enrichment tags as a MeterFilter bean

Register the tags as a `MeterFilter` bean in a `@Configuration` class. Spring Boot's `MetricsAutoConfiguration` picks up all `MeterFilter` beans and applies them to every `MeterRegistry` before any meter is registered:

```
import io.micrometer.core.instrument.Tag;



import io.micrometer.core.instrument.config.MeterFilter;



import org.springframework.context.annotation.Bean;



import org.springframework.context.annotation.Configuration;



import java.util.List;



@Configuration



public class MetricsConfig {



@Bean



MeterFilter dtEnrichmentFilter() {



List<Tag> dtTags = DtMetadata.readEnrichmentTags();



return MeterFilter.commonTags(dtTags);



}



}
```

The enrichment attributes are added as datapoint attributes, not as OTLP resource attributes. Support for injecting them as resource attributes is being tracked in a [Spring Boot issue﻿](https://github.com/spring-projects/spring-boot/issues/50861).

### 1. Add the Dynatrace metric utils dependency

Add the `dynatrace-metric-utils-java` dependency, which reads the OneAgent metadata enrichment file:

**Gradle**

```
implementation 'com.dynatrace.metric.util:dynatrace-metric-utils-java:2.5.0'
```

**Maven**

```
<dependency>



<groupId>com.dynatrace.metric.util</groupId>



<artifactId>dynatrace-metric-utils-java</artifactId>



<version>2.5.0</version>



</dependency>
```

### 2. Create a helper class to read the enrichment metadata

Create a helper class that reads the OneAgent enrichment metadata and converts it to Micrometer tags:

```
import com.dynatrace.metric.util.MetricException;



import com.dynatrace.metric.util.MetricLinePreConfiguration;



import io.micrometer.core.instrument.Tag;



import java.util.List;



public final class DtMetadata {



private DtMetadata() {}



public static List<Tag> readEnrichmentTags() {



try {



MetricLinePreConfiguration preConfig = MetricLinePreConfiguration.builder()



.dynatraceMetadataDimensions()



.build();



return preConfig.getDynatraceMetadataDimensions().entrySet().stream()



.map(e -> Tag.of(e.getKey(), e.getValue()))



.toList();



} catch (MetricException e) {



return List.of();



}



}



}
```

### 3. Apply the enrichment tags to the registry

Create the registry and apply the enrichment tags as common tags:

```
OtlpMeterRegistry registry = new OtlpMeterRegistry();



registry.config().commonTags(DtMetadata.readEnrichmentTags());
```

The enrichment attributes are added as datapoint attributes, not as OTLP resource attributes. Support for injecting them as resource attributes is being tracked in a [Spring Boot issue﻿](https://github.com/spring-projects/spring-boot/issues/50861).

## TLS configuration

If you export metrics to an environment ActiveGate that uses a self-signed certificate, make sure the certificate is properly installed on the ActiveGate. For details, see [Configure a custom SSL certificate on ActiveGate](/managed/ingest-from/dynatrace-activegate/configuration/configure-custom-ssl-certificate-on-activegate "Learn how to configure the SSL certificate on your ActiveGate.").

## Verify the metrics

After you have sent your metrics, verify the data in [**Data Explorer**](/managed/analyze-explore-automate/explorer "Query for metrics and transform results to gain desired insights.").

## Additional information

### Metric types

Micrometer instruments are mapped to OTLP metric types and then to Dynatrace metric types as follows:

| Micrometer instrument | OTLP metric | Dynatrace metric |
| --- | --- | --- |
| Counter, FunctionCounter | Sum (delta) | Counter |
| Gauge, TimeGauge, MultiGauge | Gauge | Gauge |
| Timer, DistributionSummary, LongTaskTimer | Histogram (delta) | Explicit bucket histogram |
| FunctionTimer | Sum (delta) | Counter |

Timer, DistributionSummary, and LongTaskTimer export as Histogram by default. If you configure client-side percentiles, they export as the OTLP Summary type instead, which is not supported by Dynatrace. Avoid enabling client-side percentiles when exporting to Dynatrace.

For the full OTLP to Dynatrace metric type mapping, see [About OTLP metrics ingest](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#dynatrace-specific-mapping "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.").

### Reference documentation

For upstream reference documentation, see:

* [Micrometer OTLP registry documentation﻿](https://docs.micrometer.io/micrometer/reference/implementations/otlp.html)
* [OpenTelemetry resource semantic conventions﻿](https://opentelemetry.io/docs/specs/semconv/resource/)

## Related topics

* [Ingest OTLP metrics](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics "Learn how Dynatrace ingests OpenTelemetry metrics.")