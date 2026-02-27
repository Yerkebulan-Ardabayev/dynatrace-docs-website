---
title: Instrument your Go application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/go
scraped: 2026-02-27T21:22:28.716673
---

# Instrument your Go application with OpenTelemetry

# Instrument your Go application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Published Apr 20, 2023

This walkthrough shows how to add observability to your Go application using the OpenTelemetry Go libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | No |

## Prerequisites

* Dynatrace version 1.222+
* For tracing, W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/docs/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Choose how you want to instrument your application

OpenTelemetry supports on Go automatic and manual instrumentation, or a combination of both.

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 Initialize OpenTelemetry

1. Add the following import statements.

   ```
   import (



   "context"



   "github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



   "go.opentelemetry.io/otel"



   "go.opentelemetry.io/otel/attribute"



   "go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp"



   "go.opentelemetry.io/otel/propagation"



   "go.opentelemetry.io/otel/trace"



   sdkmetric "go.opentelemetry.io/otel/sdk/metric"



   "go.opentelemetry.io/otel/sdk/metric/metricdata"



   "go.opentelemetry.io/otel/sdk/resource"



   sdktrace "go.opentelemetry.io/otel/sdk/trace"



   semconv "go.opentelemetry.io/otel/semconv/v1.20.0"



   "log"



   "time"



   "log/slog"



   "go.opentelemetry.io/contrib/bridges/otelslog"



   "go.opentelemetry.io/otel/log/global"



   sdklog "go.opentelemetry.io/otel/sdk/log"



   )
   ```
2. Run Go's [`mod tidy` commandï»¿](https://go.dev/ref/mod#go-mod-tidy) to install the dependencies.

   ```
   go mod tidy
   ```
3. Add the following code to your startup file and provide the [respective values](#get-the-dynatrace-access-details) for `DT_API_HOST` and `DT_API_TOKEN`.

   * `DT_API_HOST` should contain only the hostname of your Dynatrace URL (for example, `XXXXX.live.dynatrace.com`); it is not a URL and must not contain any schemas or paths
   * `DT_API_TOKEN` should contain the access token

   ```
   func InitOpenTelemetry() {



   // ===== GENERAL SETUP =====



   DT_API_HOST := "" // Only the host part of your Dynatrace URL



   DT_API_BASE_PATH := "/api/v2/otlp"



   DT_API_TOKEN := ""



   authHeader := map[string]string{"Authorization": "Api-Token " + DT_API_TOKEN}



   ctx := context.Background()



   oneagentsdk := sdk.CreateInstance()



   dtMetadata := oneagentsdk.GetEnrichmentMetadata()



   var attributes []attribute.KeyValue



   for k, v := range dtMetadata {



   attributes = append(attributes, attribute.KeyValue{Key: attribute.Key(k), Value: attribute.StringValue(v)})



   }



   attributes = append(attributes,



   semconv.ServiceNameKey.String("go-quickstart"), //TODO Replace with the name of your application



   semconv.ServiceVersionKey.String("1.0.1"),      //TODO Replace with the version of your application



   )



   res, err := resource.New(ctx, resource.WithAttributes(attributes...))



   if err != nil {



   log.Fatalf("Failed to create resource: %v", err)



   }



   // ===== TRACING SETUP =====



   exporter, err := otlptracehttp.New(



   ctx,



   otlptracehttp.WithEndpoint(DT_API_HOST),



   otlptracehttp.WithURLPath(DT_API_BASE_PATH+"/v1/traces"),



   otlptracehttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   tp := sdktrace.NewTracerProvider(



   sdktrace.WithResource(res),



   sdktrace.WithSampler(sdktrace.AlwaysSample()),



   sdktrace.WithBatcher(exporter),



   )



   otel.SetTracerProvider(tp)



   otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))



   // ===== METRIC SETUP =====



   var deltaTemporalitySelector = func(sdkmetric.InstrumentKind) metricdata.Temporality { return metricdata.DeltaTemporality }



   metricsExporter, err := otlpmetrichttp.New(



   ctx,



   otlpmetrichttp.WithEndpoint(DT_API_HOST),



   otlpmetrichttp.WithURLPath(DT_API_BASE_PATH+"/v1/metrics"),



   otlpmetrichttp.WithHeaders(authHeader),



   otlpmetrichttp.WithTemporalitySelector(deltaTemporalitySelector),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   mp := sdkmetric.NewMeterProvider(



   sdkmetric.WithResource(res),



   sdkmetric.WithReader(sdkmetric.NewPeriodicReader(metricsExporter, sdkmetric.WithInterval(2*time.Second))),



   )



   otel.SetMeterProvider(mp)



   // ===== LOG SETUP =====



   logExporter, err := otlploghttp.New(



   ctx,



   otlploghttp.WithEndpoint(DT_API_HOST),



   otlploghttp.WithURLPath(DT_API_BASE_PATH+"/v1/logs"),



   otlploghttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   lp := sdklog.NewLoggerProvider(



   sdklog.WithProcessor(sdklog.NewBatchProcessor(logExporter)),



   sdklog.WithResource(res),



   )



   global.SetLoggerProvider(lp)



   logger := otelslog.NewLogger("my-logger-scope", otelslog.WithLoggerProvider(lp))



   slog.SetDefault(logger) // here we are overwriting the sdtout to http logger exporter



   }
   ```
4. Make sure to call `InitOpenTelemetry` as early as possible in your startup code to initialize OpenTelemetry.

## Step 4 optional Automatically instrument your application Optional

1. Browse the [OpenTelemetry registryï»¿](https://opentelemetry.io/ecosystem/registry/?language=go&component=instrumentation) and pick the instrumentation libraries matching your application libraries.
2. Add the relevant packages to your import statements.

   ```
   import (



   "go.opentelemetry.io/[PACKAGE]"



   )
   ```
3. Run Go's [`mod tiny` commandï»¿](https://go.dev/ref/mod#go-mod-tidy) to install the dependencies.

   ```
   go mod tidy
   ```
4. Wrap your existing code with calls to the support libraries.

### Example for `net/http`

1. Install the [instrumentation library for `net/http`ï»¿](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp).
2. Add the package to your import statements.

   ```
   import (



   // other packages



   "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



   )
   ```
3. Wrap your HTTP handler function.

   ```
   handler := http.HandlerFunc(httpHandler)



   wrappedHandler := otelhttp.NewHandler(handler, "my-span") //TODO Replace with the name of your span



   //Use the wrappedHandler with your handle



   http.Handle("/", wrappedHandler)
   ```

## Step 5 Manually instrument your application

### Add tracing

1. You first need to get a tracer object.

   ```
   tracer := otel.Tracer("my-tracer")
   ```
2. With `tracer`, you can now use a span builder to create and start new spans.

   ```
   _, span := tracer.Start(r.Context(), "Call to /myendpoint")



   defer span.End()



   span.SetAttributes(attribute.String("http.method", "GET"), attribute.String("net.protocol.version", "1.1"))



   // TODO your code goes here
   ```

   In the code above, we:

   * Create a new span and name it "Call to /myendpoint"
   * Schedule a deferred call to `End()`, to ensure the span is properly closed when the function returns
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic

### Collect metrics

1. Obtain a meter object.

   ```
   meter := otel.Meter("my-meter")
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   requestCounter, _ := meter.Int64Counter("request_counter")
   ```
3. Now we can invoke the `Add()` method of `requestCounter` to record new values with the counter.

   ```
   requestCounter.Add(context.Background(), 1)
   ```

### Connect logs

With OpenTelemetry logging initialized in `InitOpenTelemetry()` and set as default logger for [slogï»¿](https://pkg.go.dev/log/slog), we can now call any of slog's log functions (for example, [`Info()`ï»¿](https://pkg.go.dev/log/slog#Info)) to send our log information to Dynatrace.

```
slog.Info("an info message")



slog.Debug("a debug message")



slog.Error("an error")
```

### Ensure context propagation Optional



Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

In the following example, we assume that we have received a network call via the [`net/http`ï»¿](https://pkg.go.dev/net/http) library and its [`Request`ï»¿](https://pkg.go.dev/net/http#Request) type.

To obtain a handle to the original context (which was provided by the calling service), we pass the HTTP header object (`r.Header`) to the `Extract` function of the global propagator singleton, which instantiates that context and returns in `parentCtx`. This allows us to continue the previous trace with our own spans.

```
func httpHandler(w http.ResponseWriter, r *http.Request) {



parentCtx := otel.GetTextMapPropagator().Extract(r.Context(), propagation.HeaderCarrier(r.Header))



tracer := otel.Tracer("my-tracer")



ctx, span := tracer.Start(



parentCtx,



"manual-server", //TODO Replace with the name of your span



trace.WithAttributes(



attribute.String("my-key-1", "my-value-1"), //TODO Add attributes



),



)



defer span.End()



//TODO your code goes here



}
```

#### Injecting the context when sending requests

In the following example, we set up a new instance of [`Request`ï»¿](https://pkg.go.dev/net/http#Request) and pass the object to the `Inject` call of the global propagator singleton. This adds the necessary HTTP headers to the request object, which we eventually pass to `Do` to execute the network request.

```
client := http.Client{}



req, err := http.NewRequest("<method>", "<url>", <body>)



if err != nil {



// TODO handle error



}



//Method to inject the current context in the request headers



otel.GetTextMapPropagator().Inject(ctx, propagation.HeaderCarrier(req.Header))



client.Do(req) // Your call goes here
```

## Step 6 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 7 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")