---
title: OpenTracing
source: https://www.dynatrace.com/docs/ingest-from/extend-dynatrace/extend-tracing/opentracing
scraped: 2026-02-25T21:16:39.508133
---

# OpenTracing

# OpenTracing

* Latest Dynatrace
* 2-min read
* Updated on Sep 23, 2022

Early Adopter

OpenTracing is an open source project that provides APIs and instrumentation for distributed tracing. Although OpenTracing and OpenCensus merged in 2019 to form OpenTelemetry, OpenTracing instrumentations are still used by many popular frameworks, libraries, and projects.

Dynatrace OneAgent for Java automatically collects OpenTracing span data and integrates it into end-to-end PurePathÂ® distributed traces.
OpenTracing with OneAgent enables you to:

* Gain insights into Java third-party libraries or frameworks that arenât natively covered by OneAgent but come with OpenTracing pre-instrumentation.
* Enrich monitoring data with project-specific additions (for example, custom instrumentation that adds business data or the capture of developer-specific diagnostics points).
* Stitch together independent, unrelated transactions to extend end-to-end distributed traces (for instance, by adding vendor-neutral custom instrumentation to gain business-process-specific or domain-specific end-to-end transactional insights).

![OpenTracing support in OneAgent](https://dt-cdn.net/images/oneagent-opentracing-support-2596-85407ecec3.png)

The quality of the OpenTracing spans captured by OneAgent depends on the quality of instrumentation provided by the third-party library.

## Prerequisites

| Monitoring framework | Versions |
| --- | --- |
| [OpenTelemetryï»¿](https://github.com/open-telemetry/opentelemetry-java/) | 1.0 - 1.3[1](#fn-monitoring-framework-1-def), 1.4 - 1.54[1](#fn-monitoring-framework-1-def) |
| [OpenTracingï»¿](https://opentracing.io/guides/java/) | 0.33, 0.32, 0.31 |

1

Supported in [AWS Lambda](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration "AWS Lambda capabilities and integration options").

## Enable OpenTracing integration

To enable support for capturing span data

1. Go to **Settings** > **Preferences** > **OneAgent features**.
2. Filter for **OpenTracing**.
3. You can enable OneAgent to:

   * Automatically register Dynatrace as the `GlobalTracer` and thereby override other tracers that are registered in the application. Select this setting only if you're sure that you want to override the other tracers (for example, Jaeger) in your tracing system.
   * Automatically register Dynatrace as the `GlobalTracer` when no other tracer is registered in the application. Do this if you don't want to interfere with any other tracers in your tracing system.
4. In your application code, use the return value from `GlobalTracer.get()` to create spans.
   The following sample shows how to manually create spans with OpenTracing:

   ```
   // Make sure to use the correct Tracer.



   Tracer tracer = GlobalTracer.get();



   SpanBuilder spanBuilder = tracer.buildSpan("hello");



   spanBuilder.withTag("foo", "bar");



   Span span = spanBuilder.start();



   // Make sure to close every created Scope.



   // It is recommended to use a try-with-resource statement for that.



   try (Scope scope = tracer.activateSpan(span)) {



   // Do actual operation.



   } finally {



   // Make sure to finish every started Span.



   span.finish();



   }
   ```

   The following sample shows how to use an existing instrumentation scope/library to create spans with OpenTracing:

   ```
   HazelcastInstance untraced = HazelcastClient.newHazelcastClient();



   // This operation will not be visible in Dynatrace.



   untraced.getMap("map").put("key", "value");



   // TracingHazelcastInstance implements the same interface (HazelcastInstance)



   // but automatially creates span for every operation.



   // It internally calls GlobalTracer.get().



   // Available as a separate instrumentation scope/library:



   // https://github.com/opentracing-contrib/java-hazelcast



   HazelcastInstance traced = new TracingHazelcastInstance(



   HazelcastClient.newHazelcastClient(),



   false // traceWithActiveSpanOnly



   );



   // This operation will be visible in Dynatrace.



   traced.getMap("map").put("key", "value");
   ```

See [Span settings](/docs/ingest-from/extend-dynatrace/extend-tracing/span-settings "Learn how to configure span settings for OpenTelemetry and OpenTracing.") for all configuration options.

## Limitations

* [Span default service](/docs/observe/application-observability/services/service-detection/service-detection-v1#span-service "Find out how Dynatrace Service Detection v1 detects and names different types of services.")
* When both OneAgent and OpenTracing instrumentation are present for the same technology (for example, incoming web requests via the Servlet API), you may experience the following limitations:

  + Duplicate nodes in PurePathÂ® distributed traces
  + Additional overhead
  + For JDBC, such double instrumentation may break service detection
    Be extra cautious when enabling OneAgent OpenTracing Java support for OneAgent out-of-the-box [supported technologies](/docs/ingest-from/technology-support#java "Find technical details related to Dynatrace support for specific platforms and development frameworks.").
* Integrating traces from OpenTracing Spring framework instrumentation currently is not supported.
* The OpenTracing Java sensor doesn't capture `array`-type attributes.

## Supported technologies

Dynatrace integrates traces from any OpenTracing instrumentations. We have positively tested the instrumentation of the following libraries and frameworks:

* Hazelcast for OpenTracing Java
* Couchbase starting with [java-client version 3.1.3ï»¿](https://github.com/couchbase/couchbase-jvm-clients) for OpenTracing Java