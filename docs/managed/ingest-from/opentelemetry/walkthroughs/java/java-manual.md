---
title: Manually instrument your Java application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/java/java-manual
---

# Manually instrument your Java application with OpenTelemetry

# Manually instrument your Java application with OpenTelemetry

* How-to guide
* 7-min read
* Published Apr 18, 2023

This walkthrough shows how to add observability to your Java application using the manual instrumention libraries and tools provided by OpenTelemetry Java.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").

The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

With SDK auto-configuration

Without SDK auto-configuration

1. Add the current versions of the following packages to your package configuration (e.g, Maven, Gradle).

   * [opentelemetry-sdk-extension-autoconfigure﻿](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-sdk-extension-autoconfigure)
   * [opentelemetry-exporter-otlp﻿](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-exporter-otlp)
   * [opentelemetry-semconv﻿](https://central.sonatype.com/artifact/io.opentelemetry.semconv/opentelemetry-semconv)
2. Configure the following environment variables to set the temporality preference to `delta` and define the export parameters, substituting `[URL]` and `[TOKEN]` with the values for the [base URL](#base-url) and [access token](#access-token).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_RESOURCE_ATTRIBUTES="service.name=java-quickstart,service.version=1.0.1"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```
3. Add the following import statements to the startup class, which bootstraps your application.

   ```
   import io.opentelemetry.api.common.Attributes;



   import io.opentelemetry.sdk.OpenTelemetrySdk;



   import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;



   import io.opentelemetry.sdk.resources.Resource;



   import io.opentelemetry.instrumentation.log4j.appender.v2_17.OpenTelemetryAppender;
   ```
4. Add the `initOpenTelemetry` method to your startup class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry() {



   OpenTelemetrySdk sdk = AutoConfiguredOpenTelemetrySdk.builder().addResourceCustomizer((resource, properties) -> {



   Resource dtMetadata = Resource.empty();



   for (String name : new String[]{"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties", "/var/lib/dynatrace/enrichment/dt_metadata.properties"}) {



   try {



   Properties props = new Properties();



   props.load(name.startsWith("/var") ? new FileInputStream(name) : new FileInputStream(Files.readAllLines(Paths.get(name)).get(0)));



   dtMetadata = dtMetadata.merge(Resource.create(props.entrySet().stream()



   .collect(Attributes::builder, (b, e) -> b.put(e.getKey().toString(), e.getValue().toString()), (b1, b2) -> b1.putAll(b2.build()))



   .build())



   );



   } catch (IOException e) {



   }



   }



   return resource.merge(dtMetadata);



   }).build().getOpenTelemetrySdk();



   OpenTelemetryAppender.install(sdk);



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

1. Add the current versions of the following packages to your package configuration (e.g, Maven, Gradle).

   * [opentelemetry-api﻿](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-api/)
   * [opentelemetry-sdk﻿](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-sdk/)
   * [opentelemetry-exporter-otlp﻿](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-exporter-otlp)
   * [opentelemetry-semconv﻿](https://central.sonatype.com/artifact/io.opentelemetry.semconv/opentelemetry-semconv)
2. Add the current version of [opentelemetry-log4j-appender-2.17﻿](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-appender-2.17) as a runtime library to your package configuration(a `runtime` scope for Maven, `runtimeOnly` for Gradle).
3. Add the following import statements to the startup class, which bootstraps your application.

   ```
   import io.opentelemetry.api.common.AttributeKey;



   import io.opentelemetry.api.common.Attributes;



   import io.opentelemetry.api.trace.propagation.W3CTraceContextPropagator;



   import io.opentelemetry.context.propagation.ContextPropagators;



   import io.opentelemetry.exporter.otlp.http.trace.OtlpHttpSpanExporter;



   import io.opentelemetry.exporter.otlp.http.logs.OtlpHttpLogRecordExporter;



   import io.opentelemetry.exporter.otlp.http.metrics.OtlpHttpMetricExporter;



   import io.opentelemetry.sdk.OpenTelemetrySdk;



   import io.opentelemetry.sdk.resources.Resource;



   import io.opentelemetry.sdk.trace.SdkTracerProvider;



   import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;



   import io.opentelemetry.sdk.trace.export.SpanExporter;



   import io.opentelemetry.sdk.trace.samplers.Sampler;



   import io.opentelemetry.sdk.metrics.SdkMeterProvider;



   import io.opentelemetry.sdk.metrics.export.PeriodicMetricReader;



   import io.opentelemetry.sdk.metrics.export.AggregationTemporalitySelector;



   import io.opentelemetry.sdk.logs.SdkLoggerProvider;



   import io.opentelemetry.sdk.logs.export.BatchLogRecordProcessor;



   import io.opentelemetry.instrumentation.log4j.appender.v2_17.OpenTelemetryAppender;
   ```
4. When ingesting using OTLP, add two fields to your startup class for your [Dynatrace URL and access token](#dynatrace-docs--otlp-export).

   ```
   private static final String DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static final String DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here
   ```

   Value injection

   Instead of hardcoding these values, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
5. Configure the service name using the environment variable `OTEL_SERVICE_NAME`.

   ```
   OTEL_SERVICE_NAME=java-quickstart
   ```
6. Add the `initOpenTelemetry` method to your initializer class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry()



   {



   // ===== GENERAL SETUP =====



   // Read service name from the environment variable OTEL_SERVICE_NAME, if present



   Resource serviceName = Optional.ofNullable(System.getenv("OTEL_SERVICE_NAME"))



   .map(n -> Attributes.of(AttributeKey.stringKey("service.name"), n))



   .map(Resource::create)



   .orElseGet(Resource::empty);



   // Parse the environment variable OTEL_RESOURCE_ATTRIBUTES into key-value pairs



   Resource envResourceAttributes = Resource.create(Stream.of(Optional.ofNullable(System.getenv("OTEL_RESOURCE_ATTRIBUTES")).orElse("").split(","))



   .filter(pair -> pair != null && pair.length() > 0 && pair.contains("="))



   .map(pair -> pair.split("="))



   .filter(pair -> pair.length == 2)



   .collect(Attributes::builder, (b, p) -> b.put(p[0], p[1]), (b1, b2) -> b1.putAll(b2.build()))



   .build()



   );



   // Define enrichment files



   String[] files = new String[] {



   "dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"



   };



   // Read host information from OneAgent files to enrich telemetry



   Resource dtMetadata = Resource.empty();



   for (String name : files) {



   try {



   Properties props = new Properties();



   props.load(name.startsWith("/var") ? new FileInputStream(name) : new FileInputStream(Files.readAllLines(Paths.get(name)).get(0)));



   dtMetadata = dtMetadata.merge(Resource.create(



   props.entrySet().stream()



   .collect(Attributes::builder, (b, e) -> b.put(e.getKey().toString(), e.getValue().toString()), (b1, b2) -> b1.putAll(b2.build()))



   .build()



   ));



   } catch (IOException e) {}



   }



   // ===== TRACING SETUP =====



   // Configure span exporter with the Dynatrace URL and the API token



   SpanExporter exporter = OtlpHttpSpanExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/traces")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .build();



   // Set up tracer provider with a batch processor and the span exporter



   SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .setSampler(Sampler.alwaysOn())



   .addSpanProcessor(BatchSpanProcessor.builder(exporter).build())



   .build();



   // ===== METRIC SETUP =====



   // Configure metric exporter with the Dynatrace URL and the API token



   OtlpHttpMetricExporter metricExporter = OtlpHttpMetricExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/metrics")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .setAggregationTemporalitySelector(AggregationTemporalitySelector.deltaPreferred())



   .build();



   // Set up meter provider with a periodic reader and the metric exporter



   SdkMeterProvider meterProvider = SdkMeterProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .registerMetricReader(PeriodicMetricReader.builder(metricExporter).build())



   .build();



   // ===== LOG SETUP =====



   // Configure log exporter with the Dynatrace URL and the API token



   OtlpHttpLogRecordExporter logExporter = OtlpHttpLogRecordExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/logs")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .build();



   // Set up log provider with the log exporter



   SdkLoggerProvider sdkLoggerProvider = SdkLoggerProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .addLogRecordProcessor(BatchLogRecordProcessor.builder(logExporter).build())



   .build();



   // ===== INITIALIZATION =====



   // Initialize OpenTelemetry with the tracer and meter providers



   OpenTelemetrySdk sdk = OpenTelemetrySdk.builder()



   .setTracerProvider(sdkTracerProvider)



   .setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))



   .setMeterProvider(meterProvider)



   .setLoggerProvider(sdkLoggerProvider)



   .buildAndRegisterGlobal();



   //



   Runtime.getRuntime().addShutdownHook(new Thread(sdkTracerProvider::close));



   OpenTelemetryAppender.install(sdk);



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

## Step 3 optional Add telemetry signals manually Optional

### Create spans

1. To create new spans, we first need a tracer object.

   ```
   Tracer tracer = GlobalOpenTelemetry



   .getTracerProvider()



   .tracerBuilder("my-tracer") //TODO Replace with the name of your tracer



   .build();
   ```
2. With `tracer`, we can now use a span builder to create and start new spans.

   ```
   // Obtain and name new span from tracer



   Span span = tracer.spanBuilder("Call to /myendpoint")



   .setSpanKind(SpanKind.CLIENT)



   .startSpan();



   // Set demo span attributes using semantic naming



   span.setAttribute("http.method", "GET");



   span.setAttribute("net.protocol.version", "1.1");



   // Set the span as current span and parent for future child spans



   try (Scope scope = span.makeCurrent())



   {



   // TODO your code goes here



   }



   finally



   {



   // Completing the span



   span.end();



   }
   ```

   In the code above, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming convention﻿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Use the span's `makeCurrent()` method to mark it as active span and parent of future spans (until the span finished)
   * Call the span's `end()` method to complete the span (in a `finally` block to ensure the method is called)

### Collect metrics

1. To instantiate new metrics instruments, we first need a meter object.

   ```
   Meter meter = GlobalOpenTelemetry



   .getMeterProvider()



   .meterBuilder("my-meter") //TODO Replace with the name of your meter



   .build();
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   LongCounter counter = meter.counterBuilder("request_counter")



   .setDescription("The number of requests we received")



   .setUnit()



   .build();
   ```
3. We can now invoke the `add()` method of `counter` to record new values with our counter and save additional attributes (for example, `action.type`).

   ```
   Attributes attrs = Attributes.of(stringKey("action.type"), "create");



   counter.add(1, attrs);
   ```

You can also create an asynchronous gauge, which requires a callback function that will be invoked by OpenTelemetry upon data collection.

The following example records on each invocation the available memory, along with an attribute on the number of active users obtained from a fictitious `getUserCount()` method.

```
meter.gaugeBuilder("free_memory")



.setDescription("Available memory in bytes")



.setUnit("bytes")



.buildWithCallback(measurement -> {



measurement.record(



Runtime.getRuntime().freeMemory(),



Attributes.of(stringKey("user_count"), getUserCount())



);



});
```

### Connect logs

You first need to adjust your Log4j 2 configuration file `log4j.xml`, to include the OpenTelemetry appender.

```
<?xml version="1.0" encoding="UTF-8"?>



<Configuration status="WARN" packages="io.opentelemetry.instrumentation.log4j.appender.v2_17">



<Appenders>



<Console name="Console" target="SYSTEM_OUT">



<PatternLayout



pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} trace_id: %X{trace_id} span_id: %X{span_id} trace_flags: %X{trace_flags} - %msg%n"/>



</Console>



<OpenTelemetry name="OpenTelemetryAppender"/>



</Appenders>



<Loggers>



<Root>



<AppenderRef ref="OpenTelemetryAppender" level="All"/>



<AppenderRef ref="Console" level="All"/>



</Root>



</Loggers>



</Configuration>
```

In this configuration, we added a new `<OpenTelemetry>` entry under `<Appenders>`, as well as an `<AppenderRef>` entry under `<Loggers>`.

With the call to `GlobalLoggerProvider`, which we previously performed under [Setup](#setup), this appender is configured for the Dynatrace backend.

## Step 4 Ensure context propagation

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

### Extracting the context when receiving a request

In the following example, we assume that we have received a network call via `com.sun.net.httpserver.HttpExchange` and we define a `TextMapGetter` instance to fetch the context information from the HTTP headers. We then pass that instance to `extract()`, returning the context object, which allows us to continue the previous trace with our spans.

```
//The getter will be used for incoming requests



TextMapGetter<HttpExchange> getter =



new TextMapGetter<>() {



@Override



public String get(HttpExchange carrier, String key) {



if (carrier.getRequestHeaders().containsKey(key)) {



return carrier.getRequestHeaders().get(key).get(0);



}



return null;



}



@Override



public Iterable<String> keys(HttpExchange carrier) {



return carrier.getRequestHeaders().keySet();



}



};



@Override



public void handle(HttpExchange httpExchange) {



//Extract the SpanContext and other elements from the request



Context extractedContext = GlobalOpenTelemetry.getPropagators().getTextMapPropagator()



.extract(Context.current(), httpExchange, getter);



try (Scope scope = extractedContext.makeCurrent()) {



//This will automatically propagate context by creating child spans within the extracted context



Span serverSpan = tracer.spanBuilder("my-server-span") //TODO Replace with the name of your span



.setSpanKind(SpanKind.SERVER) //TODO Set the kind of your span



.startSpan();



serverSpan.setAttribute(SemanticAttributes.HTTP_METHOD, "GET"); //TODO Add attributes



serverSpan.end();



}



}
```

### Injecting the context when sending requests

In the following example, we send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we define a `TextMapSetter` instance, which adds the respective information with `setRequestProperty()`. Once we have instantiated our REST object, we pass it, along with the context and the setter instance, to `inject()`, which will add the necessary headers to the request.

```
//The setter will be used for outgoing requests



TextMapSetter<HttpURLConnection> setter =



(carrier, key, value) -> {



assert carrier != null;



// Insert the context as Header



carrier.setRequestProperty(key, value);



};



URL url = new URL("<URL>"); //TODO Replace with the URL of the service to be called



Span outGoing = tracer.spanBuilder("my-client-span") //TODO Replace with the name of your span



.setSpanKind(SpanKind.CLIENT) //TODO Set the kind of your span



.startSpan();



try (Scope scope = outGoing.makeCurrent()) {



outGoing.setAttribute(SemanticAttributes.HTTP_METHOD, "GET"); //TODO Add attributes



HttpURLConnection transportLayer = (HttpURLConnection) url.openConnection();



// Inject the request with the *current*  Context, which contains our current span



GlobalOpenTelemetry.getPropagators().getTextMapPropagator().inject(Context.current(), transportLayer, setter);



// Make outgoing call



} finally {



outGoing.end();



}
```

## Step 5 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to **Distributed Traces** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or **Logs**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")