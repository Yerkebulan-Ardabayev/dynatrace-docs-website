---
title: Instrument your Ruby application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/ruby
scraped: 2026-02-25T21:20:49.300009
---

# Instrument your Ruby application with OpenTelemetry

# Instrument your Ruby application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Oct 23, 2025

This walkthrough shows how to add observability to your Ruby application using the OpenTelemetry Ruby libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | No |
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

OpenTelemetry supports on Ruby automatic and manual instrumentation, or a combination of both.

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 Initialize OpenTelementry

1. Add the following dependencies to your Gemfile.

   ```
   gem 'opentelemetry-sdk'



   gem 'opentelemetry-exporter-otlp'
   ```
2. Add the following `require` declaration.

   ```
   require 'opentelemetry/sdk'



   require 'opentelemetry/exporter/otlp'
   ```
3. Add the `init_opentelemetry` function to startup code and provide the variables `DT_API_URL` and `DT_API_TOKEN` with the values for the [Dynatrace URL](#base-url) and [access token](#access-token).

   ```
   DT_API_URL = ENV['DT_API_URL']



   DT_API_TOKEN = ENV['DT_API_TOKEN']



   def init_opentelemetry



   OpenTelemetry::SDK.configure do |c|



   c.service_name = 'ruby-quickstart' #TODO Replace with the name of your application



   c.service_version = '1.0.1' #TODO Replace with the version of your application



   # TODO: add automatic instrumentation here (step 3 - optional)



   for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties", "/var/lib/dynatrace/enrichment/dt_metadata.properties", "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"] do



   begin



   c.resource = OpenTelemetry::SDK::Resources::Resource.create(Hash[*File.read(name.start_with?("/var") ? name : File.read(name)).split(/[=\n]+/)])



   rescue



   end



   end



   c.add_span_processor(



   OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(



   OpenTelemetry::Exporter::OTLP::Exporter.new(



   endpoint: DT_API_URL + "/v1/traces",



   headers: {



   "Authorization": "Api-Token " + DT_API_TOKEN



   }



   )



   )



   )



   end



   end
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

   Exporting to OneAgent

   The Ruby SDK uses content compression by default, which is not supported by OneAgent yet.

   When exporting to OneAgent, add `compression: "none"` to the `Exporter.new()` call to disable that feature. Otherwise, [export to ActiveGate](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") instead.
4. Call `init_opentelemetry` as early as possible during the startup of your application to ensure OpenTelemetry is initialized right from the start.

## Step 3 optional Automatically instrument your application Optional

1. Add the following dependency to your Gemfile.

   ```
   gem 'opentelemetry-instrumentation-all'
   ```
2. Add the following `require` declaration.

   ```
   require 'opentelemetry/instrumentation/all'
   ```
3. Add the following line after `c.service_version` in the `init_opentelemetry` function.

   ```
   c.use_all
   ```

## Step 4 optional Manually instrument your application Optional

### Add tracing

1. To create new spans, we first need a tracer object.

   ```
   tracer = OpenTelemetry.tracer_provider.tracer('my-tracer')
   ```
2. With `tracer`, we can now use `start_span()` to create and start new spans.

   ```
   span = tracer.start_span("Call to /myendpoint", kind: :internal)



   OpenTelemetry::Trace.with_span(span) do |span, context|



   span.set_attribute("http.method", "GET")



   span.set_attribute("net.protocol.version", "1.1")



   # TODO your code goes here



   end



   rescue Exception => e



   span&.record_exception(e)



   span&.status = OpenTelemetry::Trace::Status.error("Unhandled exception of type: #{e.class}")



   raise e



   ensure



   span&.finish
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `finish()` method to complete the span (in an `ensure` block to ensure the method is called)

## Process logs with technology bundle parsers

Through OpenPipeline, you can use and configure technology bundles. A technology bundle is a library of parsers (processing rules) that process logs from various technologies, such as Java, .NET, and Microsoft IIS.

Parsers help you to improve filtering, troubleshooting, metrics, alerts, and dashboards by efficiently extracting log levels and relevant attributes. You can also use technology bundles to structure logs from technologies that are not supported by Dynatrace out of the box.

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

For more information, see [Process logs with technology bundle parsers](/docs/platform/openpipeline/use-cases/tutorial-technology-processor "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Collect metrics

No example yet, as OpenTelemetry for Ruby does not have stable support for metrics yet.

### Connect logs

No example yet, as OpenTelemetry for Ruby does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

The following example uses the default propagator's `extract()` method to extract and recreate the context from the request, in `parent_context`. We can then pass that context to a `start_span` call to continue the previous trace with our spans.

```
parent_context = OpenTelemetry.propagation.extract(



env,



getter: OpenTelemetry::Common::Propagation.rack_env_getter



)



span = tracer.start_span("hello world", with_parent: parent_context)



OpenTelemetry::Trace.with_span(span) do |span, context|



span.set_attribute("my-key-1", "my-value-1")



# ... expansive query



end



ensure



span&.finish



end
```

#### Injecting the context when sending requests

The following example uses Ruby's standard [Net:HTTPï»¿](https://ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html) library to call an instrumented third-party service. To add the necessary trace headers, we use the default propagator's `inject()` method.

```
request = Net::HTTP::Get.new(uri.request_uri)



OpenTelemetry.propagation.inject(request)



response = http.request(request)
```

## Step 5 Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace



Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific fields](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")