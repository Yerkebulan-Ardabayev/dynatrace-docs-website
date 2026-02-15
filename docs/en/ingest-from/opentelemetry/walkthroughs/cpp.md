---
title: Instrument your C++ application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/cpp
scraped: 2026-02-15T21:20:52.889494
---

# Instrument your C++ application with OpenTelemetry

# Instrument your C++ application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 12, 2025

This walkthrough shows how to add observability to your C++ application using the OpenTelemetry C++ libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | No |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Prerequisites

* Dynatrace version 1.222+
* A [supportedï»¿](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/README.md#supported-development-platforms) C++ compiler (C++ 11 and later)
* The [Protocol Buffers libraryï»¿](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md)
* The [OpenTelemetry libraryï»¿](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/INSTALL.md)
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

1. Add the following directives to your CMake build configuration in `CMakeLists.txt`:

   ```
   find_package(CURL REQUIRED)



   find_package(Protobuf REQUIRED)



   find_package(opentelemetry-cpp CONFIG REQUIRED)



   include_directories("${OPENTELEMETRY_CPP_INCLUDE_DIRS}")



   target_link_libraries(



   <YOUR_EXE_NAME> ${OPENTELEMETRY_CPP_LIBRARIES}



   opentelemetry_trace



   opentelemetry_common



   opentelemetry_http_client_curl



   opentelemetry_exporter_otlp_http



   opentelemetry_exporter_otlp_http_client



   opentelemetry_otlp_recordable



   opentelemetry_resources



   opentelemetry_metrics



   opentelemetry_exporter_otlp_http_metric



   )
   ```
2. Create a file named `otel.h` in your application directory and save the following content:

   ```
   #include "opentelemetry/trace/provider.h"



   #include "opentelemetry/trace/propagation/http_trace_context.h"



   #include "opentelemetry/context/propagation/global_propagator.h"



   #include "opentelemetry/sdk/trace/simple_processor_factory.h"



   #include "opentelemetry/sdk/trace/tracer_context.h"



   #include "opentelemetry/sdk/trace/tracer_context_factory.h"



   #include "opentelemetry/sdk/trace/tracer_provider_factory.h"



   #include "opentelemetry/exporters/ostream/span_exporter_factory.h"



   #include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"



   #include "opentelemetry/metrics/provider.h"



   #include "opentelemetry/sdk/metrics/export/periodic_exporting_metric_reader.h"



   #include "opentelemetry/sdk/metrics/view/view_registry_factory.h"



   #include "opentelemetry/sdk/metrics/meter_context_factory.h"



   #include "opentelemetry/sdk/metrics/meter_provider_factory.h"



   #include "opentelemetry/exporters/ostream/metric_exporter_factory.h"



   #include "opentelemetry/exporters/otlp/otlp_http_metric_exporter_factory.h"



   #include "opentelemetry/logs/provider.h"



   #include "opentelemetry/sdk/logs/logger.h"



   #include "opentelemetry/sdk/logs/logger_provider_factory.h"



   #include "opentelemetry/sdk/logs/simple_log_record_processor_factory.h"



   #include "opentelemetry/sdk/logs/logger_context_factory.h"



   #include "opentelemetry/exporters/ostream/log_record_exporter.h"



   #include "opentelemetry/exporters/otlp/otlp_http_log_record_exporter_factory.h"



   #include <cstring>



   #include <iostream>



   #include <vector>



   #include <fstream>



   #include <list>



   #include <memory>



   #include <thread>



   #include <iostream>



   #include <string>



   using namespace std;



   namespace nostd    = opentelemetry::nostd;



   namespace otlp     = opentelemetry::exporter::otlp;



   namespace resource = opentelemetry::sdk::resource;



   namespace trace_api      = opentelemetry::trace;



   namespace trace_sdk      = opentelemetry::sdk::trace;



   namespace metrics_api   = opentelemetry::metrics;



   namespace metrics_sdk    = opentelemetry::sdk::metrics;



   namespace logs_api      = opentelemetry::logs;



   namespace logs_sdk      = opentelemetry::sdk::logs;



   namespace



   {



   // Class definition for context propagation



   otlp::OtlpHttpMetricExporterOptions options;



   std::string version{ "1.0.1" };



   std::string name{ "app_cpp" };



   std::string schema{ "https://opentelemetry.io/schemas/1.2.0" };



   template <typename T>



   class HttpTextMapCarrier : public opentelemetry::context::propagation::TextMapCarrier



   {



   public:



   HttpTextMapCarrier<T>(T &headers) : headers_(headers) {}



   HttpTextMapCarrier() = default;



   virtual nostd::string_view Get(nostd::string_view key) const noexcept override



   {



   std::string key_to_compare = key.data();



   // Header's first letter seems to be  automatically capitaliazed by our test http-server, so



   // compare accordingly.



   if (key == opentelemetry::trace::propagation::kTraceParent)



   {



   key_to_compare = "Traceparent";



   }



   else if (key == opentelemetry::trace::propagation::kTraceState)



   {



   key_to_compare = "Tracestate";



   }



   auto it = headers_.find(key_to_compare);



   if (it != headers_.end())



   {



   return it->second;



   }



   return "";



   }



   virtual void Set(nostd::string_view key, nostd::string_view value) noexcept override



   {



   headers_.insert(std::pair<std::string, std::string>(std::string(key), std::string(value)));



   }



   T headers_;



   };



   // ===== GENERAL SETUP =====



   void initTracer()



   {



   otlp::OtlpHttpExporterOptions traceOptions;



   traceOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/traces";



   traceOptions.content_type  = otlp::HttpRequestContentType::kBinary;



   traceOptions.http_headers.insert(



   std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   resource::ResourceAttributes dt_resource_attributes;



   try



   {



   for (string name : {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"})



   {



   string file_path;



   ifstream dt_file;



   dt_file.open(name);



   if (dt_file.is_open())



   {



   string dt_metadata;



   ifstream dt_properties;



   while (getline(dt_file, file_path))



   {



   dt_properties.open(file_path);



   if (dt_properties.is_open())



   {



   while (getline(dt_properties, dt_metadata))



   {



   dt_resource_attributes.SetAttribute(



   dt_metadata.substr(0, dt_metadata.find("=")),



   dt_metadata.substr(dt_metadata.find("=") + 1)



   );



   }



   dt_properties.close();



   }



   }



   dt_file.close();



   }



   }



   }



   catch (...) {}



   auto dt_resource = resource::Resource::Create(dt_resource_attributes);



   auto resource = resource::Resource::Create(resource_attributes);



   auto merged_resource = dt_resource.Merge(resource);



   auto exporter = otlp::OtlpHttpExporterFactory::Create(traceOptions);



   auto processor = trace_sdk::SimpleSpanProcessorFactory::Create(std::move(exporter));



   std::vector<std::unique_ptr<trace_sdk::SpanProcessor>> processors;



   processors.push_back(std::move(processor));



   auto context = trace_sdk::TracerContextFactory::Create(std::move(processors), merged_resource);



   std::shared_ptr<opentelemetry::trace::TracerProvider> provider = opentelemetry::sdk::trace::TracerProviderFactory::Create(std::move(context));



   // Set the global trace provider



   opentelemetry::trace::Provider::SetTracerProvider(provider);



   // set global propagator



   opentelemetry::context::propagation::GlobalTextMapPropagator::SetGlobalPropagator(



   opentelemetry::nostd::shared_ptr<opentelemetry::context::propagation::TextMapPropagator>(



   new opentelemetry::trace::propagation::HttpTraceContext()));



   }



   // ===== METRIC SETUP =====



   void initMeter() {



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   otlp::OtlpHttpMetricExporterOptions otlpOptions;



   auto resource = resource::Resource::Create(resource_attributes);



   otlpOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/metrics";



   otlpOptions.aggregation_temporality = otlp::PreferredAggregationTemporality::kDelta;



   otlpOptions.content_type = otlp::HttpRequestContentType::kBinary;



   otlpOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   //This creates the exporter with the options we have defined above.



   auto exporter = otlp::OtlpHttpMetricExporterFactory::Create(otlpOptions);



   metrics_sdk::PeriodicExportingMetricReaderOptions options;



   options.export_interval_millis = std::chrono::milliseconds(1000);



   options.export_timeout_millis  = std::chrono::milliseconds(500);



   std::unique_ptr<metrics_sdk::MetricReader> reader{new metrics_sdk::PeriodicExportingMetricReader(std::move(exporter), options) };



   auto context = metrics_sdk::MeterContextFactory::Create(opentelemetry::sdk::metrics::ViewRegistryFactory::Create(), resource);



   context->AddMetricReader(std::move(reader));



   auto u_provider = metrics_sdk::MeterProviderFactory::Create(std::move(context));



   std::shared_ptr<opentelemetry::metrics::MeterProvider> provider(std::move(u_provider));



   metrics_api::Provider::SetMeterProvider(provider);



   }



   // ===== LOG SETUP =====



   void initLogger() {



   resource::ResourceAttributes resource_attributes = {{"service.name", name},



   {"service.version", version}};



   auto resource = resource::Resource::Create(resource_attributes);



   otlp::OtlpHttpLogRecordExporterOptions loggerOptions;



   loggerOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/logs";



   loggerOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));



   loggerOptions.content_type = opentelemetry::exporter::otlp::HttpRequestContentType::kBinary;



   auto exporter  = otlp::OtlpHttpLogRecordExporterFactory::Create(loggerOptions);



   auto processor = logs_sdk::SimpleLogRecordProcessorFactory::Create(std::move(exporter));



   std::vector<std::unique_ptr<logs_sdk::LogRecordProcessor>> processors;



   processors.push_back(std::move(processor));



   auto context = logs_sdk::LoggerContextFactory::Create(std::move(processors), resource);



   std::shared_ptr<logs_api::LoggerProvider> provider = logs_sdk::LoggerProviderFactory::Create(std::move(context));



   opentelemetry::logs::Provider::SetLoggerProvider(provider);



   }



   nostd::shared_ptr<opentelemetry::logs::Logger> get_logger(std::string scope){



   // TODO: add your log provider here



   return logger;



   }



   opentelemetry::nostd::shared_ptr<opentelemetry::trace::Tracer> get_tracer(std::string tracer_name)



   {



   // TODO: add your trace provider here



   return tracer;



   }



   nostd::unique_ptr<opentelemetry::metrics::Counter<uint64_t>> initIntCounter()



   {



   // TODO: add your custom metrics here



   return request_counter;



   }



   void initOpenTelemetry() {



   // You can import only the required method



   initLogger();



   initTracer();



   initMeter();



   }



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
3. Configure `DT_API_URL` and `DT_API_TOKEN` for the [Dynatrace URL](#base-url) and [access token](#access-token) in `otel.h`.

## Step 3 Instrument your application

To use OpenTelemetry, you first need to complete these two steps:

1. Add the necessary header files to your code.

   To add the header files, include `otel.h` wherever you want to make use of OpenTelemetry.

   ```
   #include "otel.h"
   ```
2. Initialize OpenTelemetry.

   For the initialization, use the `initOpenTelemetry` function in `otel.h` and call it early on in the startup code of your application.

### Add tracing

1. Get a reference to the tracer provider.

   ```
   auto provider = opentelemetry::trace::Provider::GetTracerProvider();
   ```
2. Obtain a tracer object.

   ```
   // In our case the GetTraces method takes the tracer name and returns the tracer provider



   auto tracer = provider->GetTracer(tracer_name);
   ```
3. With `tracer`, we can now start new spans and set them for the current execution scope.

   ```
   StartSpanOptions options;



   options.kind = SpanKind::kServer;



   auto span = tracer->StartSpan("Call to /myendpoint", {



   { "http.method", "GET" },



   { "net.protocol.version", "1.1" }



   }, options);



   auto scope = tracer->WithActiveSpan(span);



   // TODO: Your code goes here



   span->End();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `End()` method to complete the span

### Collect metrics

1. Get a reference to the meter provider.

   ```
   auto provider = metrics_api::Provider::GetMeterProvider();
   ```
2. Obtain a meter object.

   ```
   nostd::shared_ptr<metrics_api::Meter> meter = provider->GetMeter("my-meter", "1.0.1");
   ```
3. With `meter`, we can now create individual instruments, such as a counter.

   ```
   auto request_counter = meter->CreateUInt64Counter("request_counter");
   ```
4. We can now invoke the `Add()` method of `request_counter` to record new values with the counter and save additional attributes (for example, `action.type`).

   ```
   std::map<std::string, std::string> labels = { {"action.type", "create"} };



   auto labelkv = opentelemetry::common::KeyValueIterableView<decltype(labels)>{ labels };



   request_counter->Add(1, labelkv);
   ```

### Connect logs

1. Get a reference to the logger provider.

   ```
   auto provider = logs_api::Provider::GetLoggerProvider();
   ```
2. Call the provider's `GetLogger()` method to obtain a logger instance.

   ```
   auto logger = provider->GetLogger("scope_name", "", OPENTELEMETRY_SDK_VERSION);
   ```
3. Call any of the available logging methods to record a log statement. The following example logs a debug statement.

   ```
   logger->Debug("My debug statement here");
   ```

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

In the following examples, we assume that we are handling context propagation using the standard [W3C trace contextï»¿](https://www.w3.org/TR/trace-context/) headers, and we receive and set HTTP headers with the OpenTelemetry `http_client::Headers` object.

For that purpose, we use an instance of the class `HttpTextMapCarrier`, which we defined during the setup, and which is based on the OpenTelemetry class [`TextMapCarrier`ï»¿](https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/classopentelemetry_1_1context_1_1propagation_1_1TextMapCarrier.html#exhale-class-classopentelemetry-1-1context-1-1propagation-1-1textmapcarrier).

#### Extracting the context when receiving a request

To extract information on an existing context, we call the `Extract` method of the global propagator singleton and pass it the `HttpTextMapCarrier` instance, as well as the current context. This returns a new context object (`new_context`), which we allows us to continue the previous trace with our spans.

```
StartSpanOptions options;



options.kind          = SpanKind::kServer;



std::string span_name = request.uri;



// extract context from http header



std::map<std::string, std::string> &request_headers =



const_cast<std::map<std::string, std::string> &>(request.headers);



const HttpTextMapCarrier<std::map<std::string, std::string>> carrier(request_headers);



auto prop        = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();



auto current_ctx = context::RuntimeContext::GetCurrent();



auto new_context = prop->Extract(carrier, current_ctx);



options.parent   = GetSpan(new_context)->GetContext();



auto span = get_tracer("manual-server")



->StartSpan("my-server-span", { //TODO Replace with the name of your span



{"my-server-key-1", "my-server-value-1"} //TODO Add attributes



}, options);



auto scope = get_tracer("http_server")->WithActiveSpan(span);



for (auto &kv : request.headers)



{



span->SetAttribute("http.header." + std::string(kv.first.data()), kv.second);



}



span->AddEvent("Processing request");



response.headers[HTTP_SERVER_NS::CONTENT_TYPE] = HTTP_SERVER_NS::CONTENT_TYPE_TEXT;



response.body = doCall();



span->End();
```

#### Injecting the context when sending requests

For injecting current context information into an outbound request, we call the `Inject` method of the global propagator singleton and pass it the `HttpTextMapCarrier` instance, as well as the current context. This adds the applicable headers to the `carrier` instance, which we then use in the text step with our HTTP request.

```
auto http_client = http_client::HttpClientFactory::CreateSync();



std::string url  = std::getenv("URL"); // TODO set URL you want to call



CustomCounter(); // remove



// start active span



StartSpanOptions options;



options.kind = SpanKind::kClient;



opentelemetry::ext::http::common::UrlParser url_parser(url);



std::string span_name = url_parser.path_;



auto span = get_tracer("http-client")->StartSpan(span_name,



{{opentelemetry::semconv::url::kUrlFull, url_parser.url_},



{opentelemetry::semconv::url::kUrlScheme, url_parser.scheme_},



{opentelemetry::semconv::http::kHttpRequestMethod, "GET"}},



options);



auto scope = get_tracer("http-client")->WithActiveSpan(span);



// inject current context into http header



auto current_ctx = context::RuntimeContext::GetCurrent();



HttpTextMapCarrier<http_client::Headers> carrier;



auto prop = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();



prop->Inject(carrier, current_ctx);



// send http request



http_client::Result result = http_client->GetNoSsl(url, carrier.headers_);



//your code goes here



//then end span
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