---
title: Trace Google Cloud Functions with OpenTelemetry JavaScript
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs
scraped: 2026-02-23T21:28:58.767724
---

# Trace Google Cloud Functions with OpenTelemetry JavaScript

# Trace Google Cloud Functions with OpenTelemetry JavaScript

* Latest Dynatrace
* How-to guide
* 8-min read
* Updated on Nov 13, 2023

This guide shows how to instrument Google Cloud Functions with [OpenTelemetry JSï»¿](https://github.com/open-telemetry/opentelemetry-js) and export the traces to Dynatrace. To learn more about how Dynatrace works with OpenTelemetry, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Instrument Google Cloud Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Google Cloud Functions.

To instrument your Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Add OpenTelemetry dependencies**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#otel-dependencies "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Set up OpenTelemetry**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#otel-setup "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument the function entry point**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#instrument-handler "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Instrument outgoing requests**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs#outgoing-instrument "Learn how to instrument Google Cloud Functions with OpenTelemetry JS and export the traces to Dynatrace.")

### Step 1 Add OpenTelemetry dependencies

Add the following required OpenTelemetry dependencies to `package.json` file (your version numbers may vary):

```
"dependencies": {



"@opentelemetry/api": "^1.0.4",



"@opentelemetry/core": "^1.0.1",



"@opentelemetry/exporter-trace-otlp-proto": "^0.27.0",



"@opentelemetry/instrumentation": "^0.27.0",



"@opentelemetry/instrumentation-http": "^0.27.0",



"@opentelemetry/sdk-trace-node": "^1.0.1",



"@opentelemetry/semantic-conventions": "^1.0.1"



}
```

### Step 2 Set up OpenTelemetry

To make sure traces are collected, linked, and exported to Dynatrace, you need to set up and configure OpenTelemetry accordingly. For this, the Dynatrace endpoint and an authentication token are required.

To determine the endpoint

1. Open Dynatrace.
2. Check the address line of your browser. The URL will match one of the following patterns:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Replace the `...` part with `api/v2/otlp` to get the URL you will need to configure the OpenTelemetry exporter.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

To create an authentication token

1. Go to **Access Tokens** and select **Generate new token**.
2. Provide a **Token name**.
3. In the **Search scopes** box, search for `Ingest OpenTelemetry traces` and select the checkbox.
4. Select **Generate token**.
5. Select **Copy** to copy the token to your clipboard.
6. Save the token in a safe place; you can't display it again, and you will need it to configure the OpenTelemetry exporter.

Here is how to setup the OpenTelemetry tracing pipeline:

```
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');



const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



const { Resource } = require("@opentelemetry/resources");



const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");



diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);



function setupOtel(functionName) {



// create tracer provider



const provider = new NodeTracerProvider({



resource: new Resource({



[SemanticResourceAttributes.SERVICE_NAME]: functionName,



}),



sampler: new AlwaysOnSampler()



});



// add proto exporter



const exporter = new OTLPTraceExporter();



provider.addSpanProcessor(new BatchSpanProcessor(exporter));



// register globally



provider.register({



propagator: new W3CTraceContextPropagator()



});



// add http automatic instrumentation



registerInstrumentations({



instrumentations: [



new HttpInstrumentation()



],



});



return provider;



}
```

To configure the exporter to your tenant add, the following environment variables when deploying your Google Cloud function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: set it to the previously determined endpoint
* `OTEL_EXPORTER_OTLP_HEADERS`: set it to `Authorization=Api-Token <TOKEN>`, where `<TOKEN>` is the previously created authentication token.

### Step 3 Instrument the function entry point

To instrument invocations to a Google Cloud Function with OpenTelemetry, there are basically two things to do:

1. Create a span around the entry point of the function to trace invocations.
2. Extract and link the parent span from the propagated context (learn more about [W3C Trace Contextï»¿](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/)).

For certain libraries OpenTelemetry JS already provides [instrumentationsï»¿](https://github.com/open-telemetry/opentelemetry-js-contrib) that you can use to take care of these things.

The following section shows how to instrument an HTTP (`Trigger: HTTP`) Google Cloud Function.

#### Instrument an HTTP Google Cloud Function

The entry point of a newly created HTTP Google Cloud Function looks like this:

```
/**



* Responds to any HTTP request.



*



* @param {!express:Request} req HTTP request context.



* @param {!express:Response} res HTTP response context.



*/



exports.helloWorld = (req, res) => {



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

OpenTelemetry JS already provides an [instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) for this. In order to make sure that an incoming HTTP request is instrumented
and spans are captured, a few code code snippets must be added to the function's code.

Add this as your first `require` statement:

```
const { trace, context } = require("@opentelemetry/api");
```

Then add this helper function, which calls the `setupOtel` function we defined above and applies a user-defined name (`funcName`) to the automatically created span.

```
function instrumentHandler(handler, funcName) {



setupOtel(funcName);



return (req, res) => {



const span = trace.getSpan(context.active());



if (span != null) {



span.updateName(funcName);



}



handler(req, res);



};



}
```

Next, we move the function's actual "business" logic into the `myHandler` function.

```
async function myHandler(req, res) {



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

Finally, we make sure to set the now instrumented `myHandler` function as the entry point and `require` the `http(s)` modules.

Without requiring the `http(s)` modules, no spans will be created and the function's trace will not show up in Dynatrace.

```
exports.helloWorld = instrumentHandler(myHandler, "helloWorld");



// make sure the http(s) library is patched before the first call



require("http");



require("https");
```

### Step 4 Instrument outgoing requests



To achieve end-to-end tracing, it is important that outgoing requests are also instrumented.

The following section shows how to instrument outgoing HTTP(S) requests.

#### Instrument outgoing HTTP requests

OpenTelemetry JS provides an [instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) for tracing outgoing HTTP calls (which we already used in the code snippets above for tracing the incoming HTTP call).

The following helper function `httpGet` wraps outgoing HTTP(S) calls in a `Promise` object so that the result of the call can be `await`ed in the main function.

```
async function httpGet(url) {



return new Promise((resolve, reject) => {



const isHttps = url.startsWith("https://");



const httpLib = isHttps ? https : http;



const request = httpLib.get(url, (res) => {



console.log(`${url} status code - ${res.statusCode}`);



const responseData = [];



res.on("error", (error) => {



console.error(`${url} reponse error - ${error}`);



reject(error);



});



res.on("data", (chunk) => {



responseData.push(chunk);



});



res.on("end", () => {



resolve({ statusCode: res.statusCode, data: responseData });



});



});



request.on("error", error => {



console.error(`${url} request error - ${error}`);



reject(error);



});



request.end();



});



}
```

The main function can then perform outgoing HTTP(S) calls, making use of this helper function `httpGet`, which is automatically instrumented by OpenTelemetry.

```
async function myHandler(req, res) {



await httpGet('https://example.com');



await httpGet('http://example.net');



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};
```

Putting everything together, here is the full sample code for tracing a Node.js Google Cloud Function that is invoked via HTTP and that performs outgoing HTTP(S) calls.

```
const { trace, context } = require("@opentelemetry/api");



const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');



const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



const { Resource } = require("@opentelemetry/resources");



const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");



const http = require("http");



const https = require("https");



diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);



function setupOtel(functionName) {



// create tracer provider



const provider = new NodeTracerProvider({



resource: new Resource({



[SemanticResourceAttributes.SERVICE_NAME]: functionName,



}),



sampler: new AlwaysOnSampler()



});



// add proto exporter



const exporter = new OTLPTraceExporter();



provider.addSpanProcessor(new BatchSpanProcessor(exporter));



// register globally



provider.register({



propagator: new W3CTraceContextPropagator()



});



// add http automatic instrumentation



registerInstrumentations({



instrumentations: [



new HttpInstrumentation()



],



});



return provider;



}



async function httpGet(url) {



return new Promise((resolve, reject) => {



const isHttps = url.startsWith("https://");



const httpLib = isHttps ? https : http;



const request = httpLib.get(url, (res) => {



console.log(`${url} status code - ${res.statusCode}`);



const responseData = [];



res.on("error", (error) => {



console.error(`${url} reponse error - ${error}`);



reject(error);



});



res.on("data", (chunk) => {



responseData.push(chunk);



});



res.on("end", () => {



resolve({ statusCode: res.statusCode, data: responseData });



});



});



request.on("error", error => {



console.error(`${url} request error - ${error}`);



reject(error);



});



request.end();



});



}



// The function's custom logic goes in here.



async function myHandler(req, res) {



// Perform 2 outgoing HTTP calls.



await httpGet('https://example.com');



await httpGet('http://example.net');



let message = req.query.message || req.body.message || 'Hello World!';



res.status(200).send(message);



};



function instrumentHandler(handler, funcName) {



setupOtel(funcName);



return (req, res) => {



const span = trace.getSpan(context.active());



if (span != null) {



span.updateName(funcName);



}



handler(req, res);



};



}



// This is the function'S entrypoint.



exports.helloWorld = instrumentHandler(myHandler, "helloWorld");



// make sure the http(s) library is patched before the first call



require("http");



require("https");
```

These are the resulting *Distributed traces* as they show up in Dynatrace.

![The OpenTelemetry JS GCF traces in Dynatrace](https://dt-cdn.net/images/otel-gcf-nodejs-1578-425c527e3f.png)

## Verify that the traces are ingested into Dynatrace

A few minutes after invoking your Google Cloud Functions, look for your spans:

* Go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab.
* Your spans will be part of an existing PurePath distributed trace if the root of your call is already being monitored by the OneAgent.
  If your Google Cloud Function is not getting any traffic, there will be no traces.

## (Optional) Configure data capture to meet privacy requirements

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").