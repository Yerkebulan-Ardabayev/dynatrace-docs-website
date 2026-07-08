---
title: Manually instrument your Python application with OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual
---

# Manually instrument your Python application with OpenTelemetry

# Manually instrument your Python application with OpenTelemetry

* How-to guide
* 4-min read
* Updated on Nov 14, 2023

This walkthrough shows how to add observability to your Python application using the OpenTelemetry Python libraries and tools.

## Step 1 Get the Dynatrace access details

### Determine the API base URL

For details on how to assemble the base OTLP endpoint URL, see [Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). The URL should end in `/api/v2/otlp`.

### Get API access token

To generate an access token, in Dynatrace, go to ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Dynatrace OTLP API endpoints](/managed/ingest-from/opentelemetry/otlp-api#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") has more details on the format and the necessary access scopes.

## Step 2 Instrument your application

1. Use [pip﻿](https://pypi.org/project/pip/) to install the OpenTelemetry SDK and API packages.

   ```
   pip install opentelemetry-api



   pip install opentelemetry-sdk



   pip install opentelemetry-exporter-otlp-proto-http
   ```
2. Add the following imports to your code.

   ```
   import json



   import logging



   from opentelemetry.sdk.resources import Resource



   # Import exporters



   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter



   from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter



   from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter



   # Trace imports



   from opentelemetry.trace import set_tracer_provider, get_tracer_provider



   from opentelemetry.sdk.trace import TracerProvider, sampling



   from opentelemetry.sdk.trace.export import BatchSpanProcessor



   # Metric imports



   from opentelemetry import metrics as metrics



   from opentelemetry.sdk.metrics.export import (



   AggregationTemporality,



   PeriodicExportingMetricReader,



   )



   from opentelemetry.sdk.metrics import MeterProvider, Counter, UpDownCounter, Histogram, ObservableCounter, ObservableUpDownCounter



   from opentelemetry.metrics import set_meter_provider, get_meter_provider



   # Logs import



   from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler



   from opentelemetry.sdk._logs.export import BatchLogRecordProcessor



   from opentelemetry._logs import set_logger_provider
   ```
3. Add the following code to your startup sequence, to initialize OpenTelemetry right after your application has started. Provide the variables `DT_API_URL` and `DT_API_TOKEN` with the [Dynatrace URL](#base-url) and the [access token](#access-token).

   ```
   # ===== GENERAL SETUP =====



   DT_API_URL = ""



   DT_API_TOKEN = ""



   merged = dict()



   for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json", "/var/lib/dynatrace/enrichment/dt_host_metadata.json"]:



   try:



   data = ''



   with open(name) as f:



   data = json.load(f if name.startswith("/var") else open(f.read()))



   merged.update(data)



   except:



   pass



   merged.update({



   "service.name": "python-quickstart", #TODO Replace with the name of your application



   "service.version": "1.0.1", #TODO Replace with the version of your application



   })



   resource = Resource.create(merged)



   # ===== TRACING SETUP =====



   tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



   set_tracer_provider(tracer_provider)



   tracer_provider.add_span_processor(



   BatchSpanProcessor(



   OTLPSpanExporter(



   endpoint = DT_API_URL + "/v1/traces",



   headers = {



   "Authorization": "Api-Token " + DT_API_TOKEN



   }



   )



   )



   )



   # ===== METRIC SETUP =====



   exporter = OTLPMetricExporter(



   endpoint = DT_API_URL + "/v1/metrics",



   headers = {"Authorization": "Api-Token " + DT_API_TOKEN},



   preferred_temporality = {



   Counter: AggregationTemporality.DELTA,



   UpDownCounter: AggregationTemporality.CUMULATIVE,



   Histogram: AggregationTemporality.DELTA,



   ObservableCounter: AggregationTemporality.DELTA,



   ObservableUpDownCounter: AggregationTemporality.CUMULATIVE,



   }



   )



   reader = PeriodicExportingMetricReader(exporter)



   provider = MeterProvider(metric_readers=[reader], resource=resource)



   set_meter_provider(provider)



   # ===== LOG SETUP =====



   logger_provider = LoggerProvider(resource=resource)



   set_logger_provider(logger_provider)



   logger_provider.add_log_record_processor(



   BatchLogRecordProcessor(OTLPLogExporter(



   endpoint = DT_API_URL + "/v1/logs",



   headers = {"Authorization": "Api-Token " + DT_API_TOKEN}



   ))



   )



   handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)



   # Attach OTLP handler to root logger



   logging.getLogger().addHandler(handler)
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

   Value injection

   Instead of hardcoding these values, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).

## Step 3 optional Add telemetry signals manually Optional

### Create spans

1. To create new spans, we first need a tracer object.

   ```
   tracer = get_tracer_provider().get_tracer("my-tracer")
   ```
2. With `tracer`, we can now use `start_as_current_span()` to create and start new spans.

   ```
   with tracer.start_as_current_span("Call to /myendpoint") as span:



   span.set_attribute("http.method", "GET")



   span.set_attribute("net.protocol.version", "1.1")



   #TODO your code goes here
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming convention﻿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version

   The span will be automatically set as a current and active span until the execution flow leaves the current method scope. Subsequent spans will automatically become child spans.

### Collect metrics

1. To instantiate new metric instruments, we first need a meter object.

   ```
   meter = get_meter_provider().get_meter("my-meter", "0.1.2") #TODO Replace with the name of your meter
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   counter = meter.create_counter(



   name="request_counter",



   description="The number of requests we received"



   )
   ```
3. We can now invoke the `add()` method of `counter` to record new values with our counter and save additional attributes (for example, `action.type`).

   ```
   attributes = {"action.type": "create"}



   counter.add(1, attributes)
   ```

### Connect logs

With the `logging` variable, initialized under [Setup](#setup), we can log straight to the configured OpenTelemetry endpoint at Dynatrace.

```
logging.error("Log line")
```

Python logs are still [considered experimental﻿](https://opentelemetry.io/docs/languages/python/#status-and-releases) and future version may introduce incompatible changes.

## Step 4 Ensure context propagation

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

### Extracting the context when receiving a request

In the following example, we fetch the value of the `traceparent` header and use the `extract()` method of `TraceContextTextMapPropagator` to retrieve the provided context information, which we subsequently pass to `start_as_current_span()` to continue our trace.

```
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator



traceparent = request.headers.get_all("traceparent")



carrier = {"traceparent": traceparent}



ctx = TraceContextTextMapPropagator().extract(carrier)



with tracer.start_as_current_span("my-span", context=ctx) as span:



span.set_attribute("my-key-1", "my-value-1")
```

### Injecting the context when sending requests

In the following example, we send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we pass an empty object to `TraceContextTextMapPropagator.inject()`, which then receives the necessary `traceparent` header value. We then include that value in our [requests﻿](https://pypi.org/project/requests/) call to the other service.

```
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator



with tracer.start_as_current_span("my-span") as span:



span.set_attribute("my-key-1", "my-value-1")



try:



carrier = {}



TraceContextTextMapPropagator().inject(carrier)



header = {"traceparent": carrier["traceparent"]}



response = requests.get(url, headers=header)



except Exception as e:



pass
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