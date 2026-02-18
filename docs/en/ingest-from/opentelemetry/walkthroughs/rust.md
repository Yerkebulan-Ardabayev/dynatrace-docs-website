---
title: Instrument your Rust application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/rust
scraped: 2026-02-18T21:25:45.296937
---

# Instrument your Rust application with OpenTelemetry

# Instrument your Rust application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Jan 07, 2026

This walkthrough shows how to add observability to your Rust application using the OpenTelemetry Rust libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

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

## Step 2 Set up OpenTelemetry

1. Add the following crates to your `Cargo.toml` file.

   ```
   opentelemetry = { version = "~0", features = ["trace", "metrics"] }



   opentelemetry_sdk = { version = "~0", features = ["rt-tokio", "metrics", "logs", "spec_unstable_metrics_views"] }



   opentelemetry-otlp = { version = "~0", features = ["http-proto", "http-json", "logs", "reqwest-blocking-client", "reqwest-rustls"] }



   opentelemetry-http = { version = "~0" }



   opentelemetry-appender-log = { version = "~0" }



   opentelemetry-semantic-conventions = { version = "~0" }
   ```
2. Add the following `use` declarations to your code.

   ```
   use std::{env, convert::Infallible, net::SocketAddr, collections::HashMap, io::{BufRead, BufReader, Read}};



   use opentelemetry_sdk::trace::SdkTracerProvider;



   use opentelemetry_sdk::{logs::SdkLoggerProvider, metrics::{PeriodicReader, SdkMeterProvider}, propagation::TraceContextPropagator, Resource};



   use opentelemetry_otlp::{LogExporter, MetricExporter, Protocol, SpanExporter, WithExportConfig, WithHttpConfig};



   use opentelemetry_semantic_conventions::trace;



   use opentelemetry_http::{Bytes, HeaderExtractor, HeaderInjector};



   use opentelemetry_appender_log::OpenTelemetryLogBridge;



   use opentelemetry::{global, trace::{FutureExt, Span, SpanKind, TraceContextExt, Tracer}, Context, KeyValue};
   ```
3. Add the following function to your startup file.

   ```
   fn init_opentelemetry() {



   // Helper function to read potentially available OneAgent data



   fn read_dt_metadata() ->  Vec<KeyValue> {



   fn read_single(path: &str, metadata: &mut Vec<KeyValue>) -> std::io::Result<()> {



   let mut file = std::fs::File::open(path)?;



   if path.starts_with("dt_metadata") {



   let mut name = String::new();



   file.read_to_string(&mut name)?;



   file = std::fs::File::open(name)?;



   }



   for line in BufReader::new(file).lines() {



   if let Some((k, v)) = line?.split_once('=') {



   metadata.push(KeyValue::new(k.to_string(), v.to_string()))



   }



   }



   Ok(())



   }



   let mut metadata = Vec::new();



   for name in [



   "dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"



   ] {



   let _ = read_single(name, &mut metadata);



   }



   return metadata;



   }



   // ===== GENERAL SETUP =====



   let dt_api_token = env::var("DT_API_TOKEN").unwrap(); // TODO: change



   let dt_api_url = env::var("DT_API_URL").unwrap();



   let mut map = HashMap::new();



   map.insert("Authorization".to_string(), format!("Api-Token {}", dt_api_token));



   let resource = Resource::builder()



   .with_service_name("rust-manual-quickstart")



   .with_attributes(read_dt_metadata())



   .build();



   // ===== TRACING SETUP =====



   global::set_text_map_propagator(TraceContextPropagator::new());



   let tracer_exporter = SpanExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_protocol(Protocol::HttpBinary)



   .with_endpoint(dt_api_url.clone() + "/v1/traces")



   .build()



   .unwrap();



   let tracer_provider = SdkTracerProvider::builder()



   .with_resource(resource.clone())



   .with_batch_exporter(tracer_exporter)



   .build();



   global::set_tracer_provider(tracer_provider.clone());



   // ===== METRICS SETUP ======



   let metrics_exporter = MetricExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/metrics")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let meter_provider = SdkMeterProvider::builder()



   .with_reader(PeriodicReader::builder(metrics_exporter).build())



   .with_resource(resource.clone())



   .build();



   global::set_meter_provider(meter_provider);



   // ===== LOGS SETUP ======



   let logger_exporter = LogExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/logs")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let logger_provider = SdkLoggerProvider::builder()



   .with_batch_exporter(logger_exporter)



   .with_resource(resource.clone())



   .build();



   let otel_log_appender = OpenTelemetryLogBridge::new(&logger_provider);



   log::set_boxed_logger(Box::new(otel_log_appender)).unwrap();



   log::set_max_level(Level::Debug.to_level_filter());



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
4. Make sure the environment variables `DT_API_URL` and `DT_API_TOKEN` are properly configured for the [Dynatrace URL](#base-url) and [access token](#access-token).
5. Call `init_opentelemetry()` as early as possible in your startup code.

## Step 3 Instrument your application

### Add tracing

1. First, we need to get a tracer object.

   ```
   let tracer = global::tracer("my-tracer");
   ```
2. With `tracer`, we can now start new spans.

   ```
   let mut _span = tracer



   .span_builder("Call to /myendpoint")



   .with_kind(SpanKind::Internal)



   .start(&tracer);



   _span.set_attribute(KeyValue::new("http.method", "GET"));



   _span.set_attribute(KeyValue::new("net.protocol.version", "1.1"));



   // TODO: Your code goes here



   _span.end();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `end()` method to complete the span

### Collect metrics

1. First, we need to get a tracer object.

   ```
   let meter = global::meter("request_counter");
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   let updown_counter = meter.i64_up_down_counter("request_counter").build();
   ```
3. We can now invoke the `add()` method of `updown_counter` to record new values with the counter.

   ```
   updown_counter.add(1,&[],);
   ```

### Connect logs

In `init_opentelemetry()`, we earlier initialized the [logï»¿](https://docs.rs/log/latest/log/) crate with its OpenTelemetry log bridge and can now call any of its [logging macrosï»¿](https://docs.rs/log/latest/log/#macros) to log directly to Dynatrace.

```
error!("logging an error");



debug!("logging a debug message");
```

Maximum log level

Note the call to the [`log::set_max_level`ï»¿](https://docs.rs/log/latest/log/fn.set_max_level.html) method in the [initialization of OpenTelemetry](#set-up-opentelemetry) earlier. This sets the maximum log level of the log crate to `Level::Debug` and is required for the logged messages at that level to be emitted in the first place and picked up by the OpenTelemetry log bridge. Adjust this if you use a different maximum log level.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

#### Extracting the context when receiving a request

To continue an existing trace from an HTTP request, we first need to extract the context. For this, we declare the function `extract_context_from_request()`, which takes the incoming request object, extracts the passed context using the propagator's `extract()` method, and returns the matching context object.

```
// Utility function to extract the context from the incoming request headers



fn extract_context_from_request(req: &Request<Incoming>) -> Context {



global::get_text_map_propagator(|propagator| {



propagator.extract(&HeaderExtractor(req.headers()))



})



}
```

We can then use `extract_context_from_request()` in our request handler to obtain that context and pass it as parent to our own, new [server spanï»¿](https://opentelemetry.io/docs/concepts/signals/traces/#server) using `start_with_context()`.

```
async fn router(req: Request<Incoming>) -> Result<Response<BoxBody<Bytes, hyper::Error>>, Infallible> {



// Extract the context from the incoming request headers



let parent_cx = extract_context_from_request(&req);



let response = {



// Create a span parenting the remote client span.



let tracer = global::tracer("example/server");



let mut span = tracer



.span_builder("router")



.with_kind(SpanKind::Server)



.start_with_context(&tracer, &parent_cx);



// Adding custom attributes



span.set_attribute(KeyValue::new("my-server-key-1", "my-server-value-1"));



};



// TODO Handle the HTTP request



}
```

#### Injecting the context when sending requests

To propagate the current context to another HTTP service, we inject the context information into the HTTP request headers. The following example declares the function `send_request()`, which takes the URL of the request, the request content, and sends the request using [hyperï»¿](https://docs.rs/hyper/latest/hyper/index.html).

Once the hyper request object is initialized, we call `get_text_map_propagator()` to obtain the global `propagator` object and then use its `inject_context()` function to add the current context information to the request.

```
async fn send_request(url: &str, body_content: &str, span_name: &str) -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync + 'static>> {



let client = Client::builder(TokioExecutor::new()).build_http();



let tracer = global::tracer("example/client");



let span = tracer



.span_builder(String::from(span_name))



.with_kind(SpanKind::Client)



.start(&tracer);



let cx = Context::current_with_span(span);



let mut req = hyper::Request::builder().uri(url);



global::get_text_map_propagator(|propagator| {



propagator.inject_context(&cx, &mut HeaderInjector(req.headers_mut().unwrap()))



});



let res = client



.request(req.body(Full::new(Bytes::from(body_content.to_string())))?)



.await?;



cx.span().add_event(



"Got response!",



vec![KeyValue::new("status", res.status().to_string())],



);



Ok(())



}
```

## Step 4 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 5 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")