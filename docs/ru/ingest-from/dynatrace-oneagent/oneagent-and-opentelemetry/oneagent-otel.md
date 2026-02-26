---
title: Use OneAgent with OpenTelemetry data
source: https://www.dynatrace.com/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/oneagent-otel
scraped: 2026-02-26T21:17:28.495188
---

# Use OneAgent with OpenTelemetry data

# Use OneAgent with OpenTelemetry data

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Sep 30, 2025

There are two ways to use OneAgent with OpenTelemetry:

* Send OpenTelemetry traces to the [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").
* Detect OpenTelemetry spans from trace data, using the OneAgent code module's OpenTelemetry Span Sensor.

![OneAgent send data to Dynatrace](https://dt-cdn.net/images/screenshot-2025-09-30-at-12-44-35-2430-bc1bd03d62.png)

For most use cases, Dynatrace recommends exporting OTLP directly to Dynatrace without deploying a OneAgent.

## Send OpenTelemetry traces to the OTLP endpoint exposed by OneAgent

Dynatrace OneAgent offers a local-only OTLP endpoint for traces.
This is shown in the figure above, where the application uses the local-only OTLP endpoint.

* Local-only means OneAgent provides the endpoint exclusively at `127.0.0.1` (localhost).
* Traces-only means OneAgent only accepts tracing information, not metrics or logs.

Content encoding support

OneAgent does not support content compression using the HTTP header [`Content-Encoding`ï»¿](https://developer.mozilla.org/docs/Web/HTTP/Headers/Content-Encoding) yet. Pay particular attention to that when [instrumenting a Ruby application](/docs/ingest-from/opentelemetry/walkthroughs/ruby "Learn how to instrument your Ruby application using OpenTelemetry and Dynatrace.") as the OpenTelemetry SDK for Ruby uses by default `Content-Encoding: gzip`.

If you need to use content compression, please export to SaaS, the Collector, or ActiveGate.

To send traces to OneAgent, you first need to enable the **Extension Execution Controller**. You can do this globally for the whole environment, for host groups, or only for specific hosts.

Enable at the environment level

1. Go to **Settings** and select **Preferences** > **Extension Execution Controller**.
2. Turn on **Enable Extension Execution Controller**.
3. Turn on **Enable local HTTP Metric, Log and Event Ingest API**.

Enable for a host group

1. Go to ![Deployment Status](https://dt-cdn.net/images/deploy-status-512-c91e319ae5.png "Deployment Status") **Deployment Status** > **OneAgents**.
2. On the **OneAgent deployment** page, turn off **Show new OneAgent deployments**.
3. In the **Filter by** field, enter **Host group**, and then select the host group you want to configure from the dropdown list.

   The host list is now filtered by the selected host group. Each listed host has a **Host group:** `<group name>` link, where `<group name>` is the name of the host group that you want to configure.

   The **Host group** property is not displayed when the selected host doesn't belong to any host group.
4. Select the host group name in any row.

   As you have filtered by host group, all displayed hosts go to the same host group.

5. In the host group settings, select **Extension Execution Controller**.
6. Turn on **Enable Extension Execution Controller**.

Enable for a single host

1. Go to ![Hosts](https://dt-cdn.net/images/hosts-512-59f5d2dd7f.png "Hosts") **Hosts Classic**.
2. Find and select your host to display the host overview page.
3. In the upper-right corner of the host overview page, select **More** (**â¦**) > **Settings**.

4. In the host settings, select **Extension Execution Controller**.
5. Turn on **Enable Extension Execution Controller**.

With the EEC enabled, the OneAgent installations on the respective hosts will start accepting OTLP traces on URL `http://localhost:14499/otlp/v1/traces`.

OneAgent uses the TCP port 14499 as default port for this endpoint. You can change the port with [`oneagentctl`](/docs/ingest-from/extend-dynatrace/extend-metrics/ingestion-methods/oneagent-metric-api#communication-port "Use the Dynatrace API to retrieve the metrics of monitored entities.").

EEC unavailable on container setups

The EEC ingestion endpoint is only available with [Full-Stack and Infrastructure Monitoring](/docs/platform/oneagent/monitoring-modes/monitoring-modes "Find out more about the available monitoring modes when using OneAgent.") deployments. It is **not** available with [containerized setups](/docs/ingest-from/setup-on-k8s/deployment "Deploy Dynatrace Operator on Kubernetes"). Please use [ActiveGate](#export-to-saas-and-activegate) as export endpoint for container applications.

### Export details

Calls to these API endpoints need to adhere to the following protocol details:

* Use of HTTPâgRPC is not yet supported
* Use of the binary format of Protocol BuffersâJSON is not yet supported
* Does not support content compression using the `Content-Encoding` header

### Authentication

Because it's a local-only endpoint, OneAgent does not require authentication.

### Network requirements

* Make sure there are no local restrictions for the used TCP port (default: 14499)

  Because the OTLP communication is exclusively local, there should not be much network configuration to consider unless you have restricted local network communication, in which case you need to make sure there are no local restrictions on the used TCP port (default: 14499).

## Detect OpenTelemetry spans using the OneAgent code module's OpenTelemetry Span Sensor

The OneAgent code module includes an OpenTelemetry Span Sensor which can create new spans based on OpenTelemetry API calls.
This is shown in the figure above, where the code module (with the OpenTelemetry Span Sensor) sends data via the OpenTelemetry protocol.

Use this approach

* For services that are already instrumented by OneAgent automatically.
* To extend visibility into frameworks and libraries instrumented with OpenTelemetry.
* To customize the distributed traces.

This feature is for advanced users only, who want to create custom spans using OpenTelemetry API calls.

The feature described on this page provides the same functionality as the OneAgent SDK for span detection, but uses OpenTelemetry instead.

If you enable this feature while also exporting OTLP data, you will create duplicate spans.

OpenTelemetry span data can be captured for Java, Go, Node.js, PHP, and .NET, on all platforms supported by OneAgent.
For setup and configuration of the OneAgent Span Sensor, see [Enable the OpenTelemetry Span Sensor for OneAgent](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

When the OneAgent OpenTelemetry Span Sensor is enabled, API calls like this example are automatically detected and included in the trace waterfall view.
Since OneAgent captures these spans automatically, exporting them to an OTLP endpoint will create duplicate traces.

The following example shows what OneAgent would detect and stitch into the OneAgent trace without the complexity of manual propagation.

```
GET /calculate-price/ABC123  # OneAgent



âââ SELECT FROM products     # OneAgent



âââ calculate-discount       # OpenTelemetry



â   âââ seasonal-rules       # OpenTelemetry



â   âââ loyalty-calculation  # OpenTelemetry



âââ INSERT INTO prices       # OneAgent
```

These auto-instrumented spans are woven together with your manual OpenTelemetry spans into a single trace.

```
@RestController



public class PricingController {



private static final Tracer tracer = GlobalOpenTelemetry.getTracer("pricing-service");



@GetMapping("/calculate-price/{productId}")



public PriceResponse calculatePrice(@PathVariable String productId) {



Product product = productRepository.findById(productId);



Span calcSpan = tracer.spanBuilder("calculate-discount")



.setAttribute("product.category", product.getCategory())



.startSpan();



double discount;



try (Scope scope = calcSpan.makeCurrent()) {



discount = applySeasonalRules(product);



discount += applyCustomerLoyalty(product);



} finally {



calcSpan.end();



}



return priceRepository.save(new PriceResponse(product, discount));



}



private double applySeasonalRules(Product product) {



Span span = tracer.spanBuilder("seasonal-rules")



.setAttribute("season", "winter-sale")



.startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateSeasonalDiscount();



} finally {



span.end();



}



}



private double applyCustomerLoyalty(Product product) {



Span span = tracer.spanBuilder("loyalty-calculation").startSpan();



try (Scope scope = span.makeCurrent()) {



return calculateLoyaltyDiscount();



} finally {



span.end();



}



}



}
```