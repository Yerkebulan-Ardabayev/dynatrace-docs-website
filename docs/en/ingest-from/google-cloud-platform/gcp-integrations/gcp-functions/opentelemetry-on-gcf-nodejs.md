---
title: Integrate on Google Cloud Functions Node.js
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-nodejs
scraped: 2026-02-15T09:06:15.200367
---

# Integrate on Google Cloud Functions Node.js

# Integrate on Google Cloud Functions Node.js

* Latest Dynatrace
* How-to guide
* 4-min read
* Updated on Sep 26, 2025

The [`@dynatrace/opentelemetry-gcf`ï»¿](https://dt-url.net/zm03ye8) module provides APIs for tracing Node.js on Google Cloud Functions (GCF).

## Prerequisites

Make sure you have followed the instructions on how to [integrate OpenTelemetry on Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").

* So far, only [HTTP triggersï»¿](https://dt-url.net/os23yfz) are supported.
* Cloud Function product version: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry Node.js integration on Google Cloud Functions, run the command below in the root directory of your Google Cloud Function project.

```
npm install --save @dynatrace/opentelemetry-gcf
```

This will install the latest version of the [`@dynatrace/opentelemetry-gcf`ï»¿](https://dt-url.net/zm03ye8) module from NPM. Note that this library by itself is not enough to start tracing your Google Cloud Functions.
See the [Usage](#usage) section below for the remaining required steps.

## Usage

To export traces to Dynatrace

1. Select one of the two ways below to initialize tracing.

   * `NodeTracerProvider` used to initialize tracing is more lightweight than `NodeSDK`.
   * `NodeSDK` is typically used if you're interested in additional OpenTelemetry signals such as metrics.

   Using NodeTracerProvider (recommended)

   Using NodeSDK

   Install the required OpenTelemetry packages with the command below.

   ```
   npm install --save @opentelemetry/sdk-trace-node @opentelemetry/semantic-conventions
   ```

   After you install the packages, initialize tracing using the following snippet as an example.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



   const processor = new DtSpanProcessor(new DtSpanExporter());



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource",



   }),



   sampler: new DtSampler(),



   // for @opentelemetry/sdk-trace-node versions lower than 1.29.0 use `provider.addSpanProcessor(processor)` instead



   spanProcessors: [processor]



   // ...other configurations



   });



   provider.register({



   propagator: new DtTextMapPropagator(),



   // ...other configurations



   });
   ```

   Install the required OpenTelemetry packages with the command below.

   ```
   npm install --save @opentelemetry/sdk-node @opentelemetry/semantic-conventions
   ```

   After you install the packages, initialize tracing using the following snippet as an example.

   ```
   const { Resource } = require('@opentelemetry/resources');



   const { NodeSDK } = require('@opentelemetry/sdk-node');



   const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');



   const { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } = require('@dynatrace/opentelemetry-gcf');



   const sdk = new NodeSDK({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



   }),



   sampler: new DtSampler(),



   spanProcessor: new DtSpanProcessor(new DtSpanExporter()),



   textMapPropagator: new DtTextMapPropagator(),



   // ...other configurations



   });



   sdk.start().then(() => {



   // Resources have been detected and SDK is started



   });
   ```
2. Start the root Google Cloud Function server span, using one of the two general patterns in OpenTelemetry below.

   Start an active span (recommended)

   Start the span and activate it later

   Example that starts and immediately activates a span inside a Google Cloud Function:

   ```
   const { startActiveHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   await startActiveHttpSpan(req, async (span) => {



   let error;



   try {



   // do something



   } catch (e) {



   error = e;



   }



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   });



   }
   ```

   Example that starts a span inside a Google Cloud Function and later activates it within the same function.

   ```
   const { context, trace, ROOT_CONTEXT } = require('@opentelemetry/api');



   const { startHttpSpan, endHttpSpanAndFlush } = require('@dynatrace/opentelemetry-gcf');



   // ...tracing initialization code



   async function handler(req, res) {



   const span = await startHttpSpan(req);



   let error;



   await context.with(trace.setSpan(ROOT_CONTEXT, span), async () => {



   try {



   // do something



   } catch (e) {



   error = e;



   }



   });



   // status should be set before span ends



   res.status(error != null ? 500 : 200);



   /**



   * Span must be ended and flushed before handler sends response.



   * This limitiation comes from GCF, for details see:



   * https://cloud.google.com/functions/docs/concepts/nodejs-runtime#signal-termination



   */



   await endHttpSpanAndFlush(span, res, error);



   res.send("hello world");



   }
   ```

## Compatibility

| OneAgent version | OpenTelemetry API | OpenTelemetry SDK |
| --- | --- | --- |
| 1.243 - 1.255 | 1.x.y | 1.0.x |
| 1.257+ | 1.x.y | 1.0.x - 1.7.x |
| 1.259+ | 1.x.y | 1.0.x - 1.8.x |
| 1.261+ | 1.x.y | 1.0.x - 1.9.x |
| 1.265+ | 1.x.y | 1.0.x - 1.10.x |
| 1.273+ | 1.x.y | 1.0.x - 1.15.x |
| 1.279+ | 1.x.y | 1.0.x - 1.17.x |
| 1.283+ | 1.x.y | 1.0.x - 1.18.x |
| 1.285+ | 1.x.y | 1.0.x - 1.20.x |
| 1.289+ | 1.x.y | 1.0.x - 1.22.x |
| 1.293+ | 1.x.y | 1.0.x - 1.24.x |
| 1.297+ | 1.x.y | 1.0.x - 1.25.x |
| 1.303+ | 1.x.y | 1.0.x - 1.26.x |
| 1.307+ | 1.x.y | 1.0.x - 1.29.x |
| 1.313+ | 1.x.y | 1.0.x - 1.30.x |
| 1.327+ | 1.x.y | 1.0.x - 2.0.x |
| 1.331+ | 1.x.y | 1.0.x - 2.2.x |

Dynatrace version 1.327+ The `@dynatrace/opentelemetry-gcf` module supports OpenTelemetry SDK V2. To use V2 (instead of V1), override the version of `@dynatrace/opentelemetry-core` module (required by `@dynatrace/opentelemetry-gcf`) with a version that supports OpenTelemetry SDK V2.

1. From the table above, choose a version that supports OpenTelemetry SDK V2.
2. In your `package.json` file, adding the `overrides` section and specify one of the versions of the `@dynatrace/opentelemetry-core` module to enforce.
3. Run `npm install` to apply the changes.

Example:

```
{



"dependencies": {



"@dynatrace/opentelemetry-gcf": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Once `@dynatrace/opentelemetry-gcf` is changed to use OpenTelemetry SDK V2 by default, this override won't be needed anymore.

## Cold start

Starting a Google Cloud Function span during [cold startsï»¿](https://dt-url.net/j543yr9) produces additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://dt-url.net/jc83y1m) and set the attributes required for Dynatrace to process the spans.

## Span flush

To ensure that spans are exported properly, you need to flush the spans before a function's response is sent to the client. For details on this limitation, see [Signalling function terminationï»¿](https://dt-url.net/5ta3ywp).

You can use `endHttpSpan()` and `flushSpans()` separately instead of `endHttpSpanAndFlush()` when needed.

Flushing spans in the function's code results in longer execution times, as this operation becomes part of the function's execution logic. To avoid this, you can omit the flush operation. Spans will still be periodically exported in the background.

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Caveats

You need to pay special attention to cases like unhandled exceptions or function timeouts. If not handled properly, they could lead to a non-ended, and therefore non-exported, span.

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)