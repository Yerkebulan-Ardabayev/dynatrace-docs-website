---
title: Trace Azure Functions written in Node.js
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-nodejs
scraped: 2026-02-20T21:11:09.328920
---

# Trace Azure Functions written in Node.js

# Trace Azure Functions written in Node.js

* Latest Dynatrace
* How-to guide
* 6-min read
* Updated on Nov 04, 2025

The [`@dynatrace/opentelemetry-azure-functions` moduleï»¿](https://dt-url.net/9603x96) provides APIs for tracing Node.js on Azure Functions.

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

* @dynatrace/opentelemetry-azure-functions version 1.243+

## Installation

To set up OpenTelemetry Node.js integration on Azure Functions, run the following command.

```
npm install --save @dynatrace/opentelemetry-azure-functions
```

## Trace export

Azure Functions can be developed by using either of two different [programming modelsï»¿](https://dt-url.net/9p03lmb), v3 and v4. To accommodate differences between the two models, Dynatrace provides two different ways of trace export:

* For programming model v3, the Azure Functions handler is wrapped (with the `wrapHandler` API) to generate and export traces.
* For programming model v4, [Azure Functions Hooksï»¿](https://dt-url.net/v323l3e) are used to achieve the same. Note that hooks are available only for the programming model v4.

For details, see below.

### Programming model v3

To export traces to Dynatrace from Azure Functions developed with [programming model v3ï»¿](https://dt-url.net/n443lxw)

1. Select one of the two ways below to initialize tracing.

   * `NodeTracerProvider`âmore lightweight than `NodeSDK`
   * `NodeSDK`âtypically used if you're interested in additional OpenTelemetry signals such as metrics

   It is possible to bundle several Azure Functions into a single Azure Function app. It's therefore important to initialize tracing only once per Azure Function app instead of once per function. The simplest way to do this is to put a tracing setup code into a shared file as described in the [Azure Functions JavaScript developer guideï»¿](https://dt-url.net/t223xf2) and require it at the top of all functions.

   The tracing setup code should be implemented to set up tracing only once before any other third-party module is required.

   NodeTracerProvider example (recommended)

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



   // tracing setup



   const exporter = new DtSpanExporter();



   const processor = new DtSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: new Resource({



   "my.resource.attribute": "My Resource"



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

   NodeSDK example

   ```
   import { Resource } from "@opentelemetry/resources";



   import { NodeSDK } from "@opentelemetry/sdk-node";



   import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



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
2. Wrap your function handler as below and export the wrapped handler.

   ```
   import type { AzureFunction, Context, HttpRequest } from "@azure/functions"



   // Import the wrapHandler function.



   import { wrapHandler } from "@dynatrace/opentelemetry-azure-functions";



   const httpTrigger: AzureFunction = async function (context: Context, req: HttpRequest): Promise<void> {



   // The created span is set as active by the OpenTelemetry ContextManager here



   context.log("HTTP trigger function processed a request.");



   const name = (req.query.name || (req.body && req.body.name));



   const responseMessage = name



   ? "Hello, " + name + ". This HTTP triggered function executed successfully."



   : "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.";



   context.res = {



   status: 200,



   body: responseMessage



   };



   };



   // Export the wrapped handler function.



   export default wrapHandler(httpTrigger);
   ```

### Programming model v4

There are two ways to export traces to Dynatrace from Azure Functions developed with [programming model v4ï»¿](https://dt-url.net/7t03lem).

* Use the `initDynatrace` API.
* Initialize tracing by registering Azure Function hooks manually.

Regardless of the instrumentation approach you choose, always implement the tracing setup code to set up tracing only once before any other third-party module is required.

#### Use the `initDynatrace` API

The `initDynatrace` API registers Azure Function hooks required for tracing and optionally registers required tracing components.

You can do this either with or without the OpenTelemetry setup:

* initDynatrace with OpenTelemetry setup (recommended)

  Pass `true` as the first argument to the `initDynatrace` to set up tracing and return the registered NodeTracerProvider. Resource attributes for the provider can be passed as the second optional argument.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // initialize instrumentation with tracing setup



  const provider = initDynatrace(true, {



  "my.resource.attribute": "My Resource"



  });



  // azure functions registration goes here
  ```
* initDynatrace without OpenTelemetry setup

  Call `initDynatrace` without parameters to register required Azure Function hooks only and set up tracing manually. This is convenient if customizations are required in the tracing setup.

  ```
  import { initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  import { Resource } from "@opentelemetry/resources";



  import { NodeTracerProvider } from "@opentelemetry/sdk-trace-node";



  import { DtSpanExporter, DtSpanProcessor, DtTextMapPropagator, DtSampler } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const exporter = new DtSpanExporter();



  const processor = new DtSpanProcessor(exporter);



  const provider = new NodeTracerProvider({



  resource: new Resource({



  "my.resource.attribute": "My Resource"



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



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

  Note that the tracing setup code is the same as for programming model v3 and the example with NodeSDK (from the model v3 above) would work here as well. To make it more convenient, there is the `configureDynatrace` API, which does the same as the above.

  ```
  import { configureDynatrace, initDynatrace } from "@dynatrace/opentelemetry-azure-functions";



  // tracing setup



  const provider = configureDynatrace({



  "my.resource.attribute": "My Resource"



  });



  // initialize instrumentation



  initDynatrace();



  // azure functions registration goes here
  ```

#### Initializing tracing by registering Azure Function hooks manually.

In cases where you need to register additional Azure Functions hooks, the `initDynatrace` API might not be suitable.

Because Azure Function hooks are executed in the same order they are registered, it's important to:

* Register the Dynatrace Trace Start hook as the first pre-invocation hook
* Register the Dynatrace Trace End hook as the last post-invocation hook

Hook execution times are included in the total function execution time. If the order of the registered hooks is incorrect, the function execution time reported by our instrumentation won't be accurate either.

To find out more about Azure Function hooks, see the [Azure Functions Node.js developer guideï»¿](https://dt-url.net/uo23lv1).

To order hooks as needed, you can use the `registerTraceStartHook` and `registerTraceEndHook` APIs as shown below.

```
import { app, PreInvocationContext, PostInvocationContext } from "@azure/functions";



import { configureDynatrace, registerTraceStartHook, registerTraceEndHook } from "@dynatrace/opentelemetry-azure-functions";



// setup tracing with configureDynatrace or manually



const provider = configureDynatrace();



// register Dynatrace Trace Start hook



registerTraceStartHook();



// register other user's pre-invocation hooks



app.hook.preInvocation(async (context: PreInvocationContext) => {



// hook code



});



// register other user's post-invocation hooks



app.hook.postInvocation(async (context: PostInvocationContext) => {



// hook code



});



// register Dynatrace Trace End hook



registerTraceEndHook();



// azure functions registration goes here
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

Dynatrace version 1.327+ The `@dynatrace/opentelemetry-azure-functions` module supports OpenTelemetry SDK V2. To use V2 (instead of V1), override the version of `@dynatrace/opentelemetry-core` module (required by `@dynatrace/opentelemetry-azure-functions`) with a version that supports OpenTelemetry SDK V2.

1. From the table above, choose a version that supports OpenTelemetry SDK V2.
2. In your `package.json` file, add the `overrides` section and specify one of the versions of the `@dynatrace/opentelemetry-core` module to enforce.
3. Run `npm install` to apply the changes.

Example:

```
{



"dependencies": {



"@dynatrace/opentelemetry-azure-functions": "1.327.0"



},



"overrides": {



"@dynatrace/opentelemetry-core": "1.327.0"



}



}
```

Once `@dynatrace/opentelemetry-azure-functions` is changed to use OpenTelemetry SDK V2 by default, this override won't be needed anymore.

Supported [Azure Functions runtimeï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-versions?tabs=v4&pivots=programming-language-javascript):

* 4.x

Supported [Azure Functions programming modelï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-node?source=recommendations&tabs=javascript%2Cwindows%2Cazure-cli&pivots=nodejs-model-v4#supported-versions):

* 3.x
* 4.x @dynatrace/opentelemetry-azure-functions version 1.289+

## Limitations

* Only `async` function handlers are supported.

  + This follows the Azure recommendation to use [`async` and `await`ï»¿](https://dt-url.net/be03x31).
  + `wrapHandler` returns any non-`async` function unwrapped, so the function itself will work but no span will be created.
  + Note that async functions were introduced in ECMAScript 2017. No span will be created if an earlier version of ECMAScript is used. In case TypeScript is used, make sure [compilation targetï»¿](https://dt-url.net/df02zbc) is set to ECMAScript 2017 or higher.
* The package supports only the [Consumption planï»¿](https://dt-url.net/ck022yx). While it may work on other plans, we cannot guarantee compatibility or performance.
* Signaling function completion using the deprecated [`context.done()`ï»¿](https://dt-url.net/0l23xfy) or [`context.res.send()`ï»¿](https://dt-url.net/dj43xgq) calls is not supported. Either use a `$return` binding and return the result from the function handler, or use a named `out` binding and set `context.binding.<name>`. For HTTP triggers, setting `context.res` is also supported.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")