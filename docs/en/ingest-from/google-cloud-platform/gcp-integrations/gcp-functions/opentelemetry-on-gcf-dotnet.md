---
title: Integrate on Google Cloud Functions .NET
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet
scraped: 2026-02-25T21:24:54.969764
---

# Integrate on Google Cloud Functions .NET

# Integrate on Google Cloud Functions .NET

* Latest Dynatrace
* How-to guide
* 3-min read
* Published Jul 25, 2023

The `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` NuGet package provides APIs for tracing server-side .NET Google Cloud Function (GCF) invocations.

## Prerequisites

* [Set up OpenTelemetry monitoring for Google Cloud Functions](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf "Monitor Google Cloud Functions with OpenTelemetry and Dynatrace.").
* Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions version 1.273+
* Cloud Functions product versions: 1st gen, 2nd gen

## Installation

To set up OpenTelemetry .NET integration on Google Cloud Functions, run the command below in the root directory of your Google Cloud Function project.

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions
```

This adds the latest version of the `Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions` NuGet package as a dependency on your project.

## Trace export

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Initialize tracing**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#initialize "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Instrument a handler function**](/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/opentelemetry-on-gcf-dotnet#instrument "Monitor Google Cloud Functions with OpenTelemetry for .NET and Dynatrace.")

## Step 1 Initialize tracing

The initialization code for GCF tracing in your `Function.cs` file could look as follows (where `Function` is the configured GCF handler class):

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions;



using Google.Cloud.Functions.Framework;



using Microsoft.AspNetCore.Http;



using OpenTelemetry;



using OpenTelemetry.Trace;



namespace Examples.GcfFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



static Function()



{



DynatraceSetup.InitializeLogging();



TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



.AddGoogleCloudFunctionsInstrumentation()



.Build();



}



}



}
```

## Step 2 Instrument a handler function

Dynatrace.OpenTelemetry.Instrumentation.GoogleCloudFunctions version 1.273 Only tracing of incoming calls for HTTP-triggered functions is supported.

To instrument an HTTP-triggered function to trace incoming calls, in addition to the [initialization code above](#initialization), wrap the GCF function handler method using either `GoogleCloudFunctionsWrapper.Trace` or `GoogleCloudFunctionsWrapper.TraceAsync` as shown in the following example.

```
public Task HandleAsync(HttpContext context)



{



return GoogleCloudFunctionsWrapper.TraceAsync(



TracerProvider,



() => HandleInternalAsync(context), context);



}



private Task HandleInternalAsync(HttpContext context)



{



// This is just an example of function handler and should be replaced by actual code.



return Task.CompletedTask;



}
```

## Cold start

When the function handler is invoked for the first time after a [cold startï»¿](https://cloud.google.com/functions/docs/concepts/exec#cold_starts), the instrumentation initialization method `AddGoogleCloudFunctionsInstrumentation`
makes additional HTTP requests to fetch metadata from your [Google Cloud environmentï»¿](https://cloud.google.com/compute/docs/metadata/overview). This metadata is used to set the required attributes for Dynatrace to process
the span ("Activity" in .NET terminology).

### Limitations

The additional HTTP requests from `AddGoogleCloudFunctionsInstrumentation` method might cause unhandled exceptions during the initialization phase (for example, `HttpRequestException` in the case of a broken network connection). If your code is set to avoid monitoring when startup fails, exceptions will still be caught.

## Span flush

By default, all wrapping `Trace/TraceAsync` methods automatically perform a flush operation before the end of function invocation to ensure that all spans are exported properly. Because span flushing becomes part of the function's execution logic, it might result in a longer execution time.

To disable flushing after every invocation, you can provide a configuration parameter with the flag `ForceFlushAfterEachInvocation` set to `false` in the `AddGoogleCloudFunctionsInstrumentation` method. Spans will still be periodically exported in the background.

```
TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



// Setting ForceFlushAfterEachInvocation to false disables the flushing after every function invocation.



.AddGoogleCloudFunctionsInstrumentation(c => c.ForceFlushAfterEachInvocation = false)



.Build();
```

Because code running outside the function execution can be terminated at any time, it's discouraged by Google Cloud Functions.

* Google Cloud Functions 1st gen

  Background task execution after function invocation is not guaranteed without flushing spans and might result in span loss. In practice, samples have shown that not explicitly flushing spans usually still results in correctly exported spans.
* Google Cloud Functions 2nd gen

  Google Cloud Functions 2nd gen can handle multiple concurrent requests in a single function instance. The flush operation of one invocation can prolong the execution time of another function invocation.
  Because function instances usually need to be kept idle for some time to handle multiple concurrent requests, you can disable the flushing of spans to improve performance. For details, see [Instance lifecycleï»¿](https://cloud.google.com/run/docs/container-contract#lifecycle-services).
  Note that idle function instances are not guaranteed to be allocated CPU unless their [CPU allocationï»¿](https://cloud.google.com/run/docs/configuring/cpu-allocation) mode is set to `CPU always allocated`.

  For details, see [Function execution timelineï»¿](https://cloud.google.com/functions/docs/concepts/execution-environment#execution-timeline).

## Dynatrace overhead

* Because span export and metadata fetch take some time during cold starts, they increase the duration of the function and subsequently increase costs.
* Pay attention to infrequently invoked functions (usually with cold starts), which might require more time for the TCP handshake during span export.
* Any network problem between the exporter and Dynatrace backend might also lead to unexpectedly high overhead.

## Related topics

* [Set up Dynatrace on Google Cloud](/docs/ingest-from/google-cloud-platform "Monitor Google Cloud with Dynatrace.")
* [Google Cloud monitoringï»¿](https://www.dynatrace.com/technologies/google-cloud-monitoring/)