---
title: Instrument your JavaScript application on Node.js with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/nodejs
scraped: 2026-02-17T05:07:08.426197
---

# Instrument your JavaScript application on Node.js with OpenTelemetry

# Instrument your JavaScript application on Node.js with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 5-min read
* Updated on Nov 14, 2023

This walkthrough shows how to add observability to your JavaScript application using the OpenTelemetry JavaScript libraries and tools.

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

## Step 2 Initialize OpenTelemetry

1. Run the following `npm` command to install the necessary libraries and dependencies.

   ```
   npm install \



   @opentelemetry/api \



   @opentelemetry/exporter-metrics-otlp-proto \



   @opentelemetry/exporter-trace-otlp-proto \



   @opentelemetry/instrumentation \



   @opentelemetry/resources \



   @opentelemetry/sdk-metrics \



   @opentelemetry/sdk-trace-node \



   @opentelemetry/semantic-conventions
   ```

   Depending on the libraries your application is using, there may be also additional instrumentation support libraries that you want to add to the dependencies. A list of support libraries can be found [hereï»¿](https://www.npmjs.com/search?q=%40opentelemetry%2Finstrumentation). Common examples would be [@opentelemetry/instrumentation-httpï»¿](https://www.npmjs.com/package/@opentelemetry/instrumentation-http) and [@opentelemetry/instrumentation-netï»¿](https://www.npmjs.com/package/@opentelemetry/instrumentation-net) for the HTTP and network libraries.
2. Create a file named `otel.js` in your application directory and save the following content.

   ```
   const opentelemetry = require("@opentelemetry/api");



   const { resourceFromAttributes, emptyResource, defaultResource } = require("@opentelemetry/resources");



   const { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } = require("@opentelemetry/semantic-conventions");



   const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");



   const { registerInstrumentations } = require("@opentelemetry/instrumentation");



   const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



   const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



   const { OTLPMetricExporter } = require("@opentelemetry/exporter-metrics-otlp-proto");



   const { MeterProvider, PeriodicExportingMetricReader, AggregationTemporality } = require('@opentelemetry/sdk-metrics');



   const DT_API_URL = ''; // TODO: Provide your SaaS/Managed URL here



   const DT_API_TOKEN = ''; // TODO: Provide the OpenTelemetry-scoped access token here



   // ===== GENERAL SETUP =====



   registerInstrumentations({



   instrumentations: [ /* TODO Register your auto-instrumentation libraries here */ ],



   });



   const fs = require("fs");



   let dtmetadata = emptyResource();



   for (let name of ['dt_metadata_e617c525669e072eebe3d0f08212e8f2.json', '/var/lib/dynatrace/enrichment/dt_metadata.json', '/var/lib/dynatrace/enrichment/dt_host_metadata.json']) {



   try {



   dtmetadata = dtmetadata.merge(



   resourceFromAttributes(JSON.parse(fs.readFileSync(name.startsWith("/var") ?



   name : fs.readFileSync(name).toString('utf-8').trim()).toString('utf-8'))));



   break



   } catch { }



   }



   const resource =



   defaultResource().merge(



   resourceFromAttributes({



   [ATTR_SERVICE_NAME]: "js-agent",



   [ATTR_SERVICE_VERSION]: "0.1.0",



   })



   ).merge(dtmetadata);



   // ===== TRACING SETUP =====



   const exporter = new OTLPTraceExporter({



   url: DT_API_URL + '/v1/traces',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN }



   });



   const processor = new BatchSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: resource,



   spanProcessors: [ processor ]



   });



   provider.register();



   // ===== METRIC SETUP =====



   const metricExporter = new OTLPMetricExporter({



   url: DT_API_URL + '/v1/metrics',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN },



   temporalityPreference: AggregationTemporality.DELTA



   });



   const metricReader = new PeriodicExportingMetricReader({



   exporter: metricExporter,



   exportIntervalMillis: 3000



   });



   const meterProvider = new MeterProvider({



   resource: resource,



   readers: [ metricReader ]



   });



   // Set this MeterProvider to be global to the app being instrumented.



   opentelemetry.metrics.setGlobalMeterProvider(meterProvider);
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.
3. If you export using OTLP, configure the two variables `DT_API_URL` and `DT_API_TOKEN` in `otel.js` with their [respective values](#dynatrace-docs--otlp-export).

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Adjust the Node.js call for your application to include the [ârequireï»¿](https://nodejs.org/api/cli.html#-r---require-module) command line parameter and point it towards `otel.js`.

   ```
   node --require ./otel.js ./myapplication.js
   ```

## Step 3 Manually instrument your application

### Add tracing

1. Obtain a reference to the OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Now we can get a tracer object.

   ```
   const tracer = opentelemetry.trace.getTracer('my-tracer');
   ```
3. With `tracer`, we can use a span builder to create and start new spans.

   ```
   const span = tracer.startSpan('Call to /myendpoint');



   span.setAttribute('http.method', 'GET');



   span.setAttribute('net.protocol.version','1.1');



   // TODO your code goes here



   span.end();
   ```

   In the above code, we:

   * Create a new span and name it "Call to /myendpoint"
   * Add two attributes, following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version
   * Add a `TODO` in place of the eventual business logic
   * Call the span's `end()` method to complete the span

### Collect metrics

1. As with tracing, we first need to get a reference to the OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Next, we need to obtain a meter object.

   ```
   const meter = opentelemetry.metrics.getMeter('my-meter');
   ```
3. With `meter`, we can now create individual instruments, such as a counter.

   ```
   const requestCounter = meter.createCounter('request_counter', {



   description: 'The number of requests we received'



   });
   ```
4. We can now invoke the `add()` method of `requestCounter` to record new values with the counter and save additional attributes (for example, `action.type`).

   ```
   requestCounter.add(1, { 'action.type': 'create' });
   ```

You can also create an asynchronous gauge, which requires a callback function that will be invoked by OpenTelemetry upon data collection.

The following example records on each invocation the available memory:

```
const gauge = meter.createObservableGauge('free_memory');



gauge.addCallback(r => {



r.observe(require('os').freemem());



});
```

### Connect logs

No example yet, as OpenTelemetry for Node.js does not have stable support for logs yet.

Depending on the status of the OpenTelemetry SDK, the pre-release version may nonetheless already allow the ingestion of your logs.

### Ensure context propagation Optional

Context propagation is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

The following examples assume that we received a network call via [`ClientRequest`ï»¿](https://nodejs.org/api/http.html#class-httpclientrequest) and uses `extract()` to create the context object `remoteCtx`, based on the context information received from the HTTP headers. This allows us to continue the previous trace with our spans.

```
//Extract context from incoming headers



const { SpanKind, ROOT_CONTEXT } = require("@opentelemetry/api");



const remoteCtx = opentelemetry.propagation.extract(ROOT_CONTEXT, req.headers);



const serverSpan = opentelemetry.trace.getTracer('my-server-tracer')



.startSpan('my-server-span', {



kind: SpanKind.SERVER,



attributes: {



'my-server-key-1': 'my-server-value-1'



},



}, remoteCtx);
```

#### Injecting the context when sending requests

In the following example, we use the [axiosï»¿](https://www.npmjs.com/package/axios) HTTP client to send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we create a `ctx` object, pass it the current span, and mark it as active. Then we pass that context object and an empty `my_headers` object to `inject()` and, once the call is returned, we have the appropriate headers in `my_headers`, which we can eventually pass to our HTTP call.

```
const ctx = opentelemetry.trace.setSpan(



opentelemetry.context.active(),



serverSpan



);



const my_headers = {};



opentelemetry.propagation.inject(ctx, my_headers);



await axios.get(URL, {headers: my_headers});



serverSpan.end();
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