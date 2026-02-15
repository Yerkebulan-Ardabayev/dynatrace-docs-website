---
title: Trace Azure Functions written in .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet
scraped: 2026-02-15T09:06:08.717587
---

# Trace Azure Functions written in .NET

# Trace Azure Functions written in .NET

* Latest Dynatrace
* How-to guide
* 10-min read
* Updated on Jul 31, 2024

## Prerequisites

Ensure that you have followed the **initial configuration** steps described in [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.") before using the packages below.

.NET version 8 or earlier

## Installation

1. Add the following dependencies to your project.

   * Required `Dynatrace.OpenTelemetry`âprovides integration of Dynatrace-specific components (for activity export and propagation) into OpenTelemetry .NET.
   * Optional [`OpenTelemetry.Extensions.Hosting`ï»¿](https://dt-url.net/w603yxv)âuses a `TracerProvider` with a dependency injection. While the latest release is supported for worker functions, in-process functions require OpenTelemetry.Extensions.Hosting version 1.0.0-rc9.5 or earlier. For details, see [Compatibility with `dotnet` (in-process) runtime](#compatibility-with-dotnet-in-process-runtime) below.

   Example commands to add dependencies

   ```
   dotnet add package Dynatrace.OpenTelemetry



   dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Extensions.Hosting
   ```
2. Additionally, depending on the runtime you use, we recommend that you use the following Azure-functions helper packages:

   * Recommended For in-process (library) functions (`dotnet` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions`
     + `OpenTelemetry.Instrumentation.AspNetCore`

     To add the packages, run the command below.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions



     dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Instrumentation.AspNetCore
     ```
   * Recommended For isolated aka worker functions (`dotnet-isolated` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker`

     To add the package, run the command below.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker
     ```
   * Optional Alternatively, on both runtimes you can use a Dynatrace package called `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` with the following functions:

     + [`AzureFunctionsCoreInstrumentation.Trace`](#manual-trace-instrumentation)
     + [`AzureFunctionsCoreInstrumentation.TraceAsync`](#manual-trace-instrumentation)

## Compatibility with OpenTelemetry and `System.Diagnostics.DiagnosticSource` versions

Periodically, we need to upgrade the minimum version of the `OpenTelemetry` NuGet package
our components depend on, and consequently, the minimum version of the `System.Diagnostics.DiagnosticSource` library.
This table lists the compatibility between `Dynatrace.OpenTelemetry`, `OpenTelemetry`, and `System.Diagnostics.DiagnosticSource` versions.

| `Dynatrace.OpenTelemetry` version | Minimum `OpenTelemetry` version | Minimum `System.Diagnostics.DiagnosticSource` version |
| --- | --- | --- |
| 1.273 and earlier | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

You don't usually need to worry about these dependencies as they're defined for you in our NuGet package. This
means that when you upgrade `Dynatrace.OpenTelemetry`, NuGet might implicitly upgrade your `OpenTelemetry` or
`System.Diagnostics.DiagnosticSource` version if you are currently on an earlier one.

## Compatibility with `dotnet` (in-process) runtime

For the `dotnet` (in-process) runtime, only certain versions of OpenTelemetry are compatible with certain versions of the Azure runtime:

* Azure Functions `dotnet` runtime v3 is not compatible with OpenTelemetry.
* Azure Functions `dotnet` runtime v4 is compatible with OpenTelemetry 1.3.x (`System.Diagnostics.DiagnosticSource` 6).

When using the `dotnet` (in-process) runtime, functions are loaded into the same CLR as the runtime. For instrumentation to work properly, the same `System.Diagnostics.DiagnosticSource` assembly needs to be used in the runtime and by the OpenTelemetry dependencies of the function. Symptoms of incompatible combinations may include your function failing to build, failing to load at runtime, or producing incomplete traces.

## Example using the dotnet (in-process) runtime

Your `Startup.cs` could look as follows:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Microsoft.Azure.Functions.Extensions.DependencyInjection;



using Microsoft.Extensions.DependencyInjection;



using OpenTelemetry.Trace;



[assembly: FunctionsStartup(typeof(Examples.AzureFunctionApp.Startup))]



namespace Examples.AzureFunctionApp



{



internal class Startup : FunctionsStartup



{



public override void Configure(IFunctionsHostBuilder builder)



{



builder.Services.AddOpenTelemetryTracing(sdk => sdk



.AddAzureFunctionsInstrumentation()



.AddAspNetCoreInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace & call AddTelemetrySdk (see below)



);



}



}



}
```

An instrumented in-process function could look like this:

```
using System.Diagnostics;



using System.Threading.Tasks;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Microsoft.AspNetCore.Http;



using Microsoft.AspNetCore.Mvc;



using Microsoft.Azure.WebJobs;



using Microsoft.Azure.WebJobs.Extensions.Http;



using Microsoft.Extensions.Logging;



namespace Examples.AzureFunctionApp



{



public class Function



{



public Function(ILoggerFactory loggerFactory)



{



// This is needed in every function in your app.



DynatraceSetup.InitializeLogging(loggerFactory);



}



[FunctionName("MyFunction")]



public async Task<IActionResult> Run(



[HttpTrigger(AuthorizationLevel.Function, "get", Route = null)] HttpRequest request,



Microsoft.Azure.WebJobs.ExecutionContext ctx)



{



// This adds the required attributes to make the activity recognizable as an Azure function invocation.



// Put this line first - there should be minimal time elapsing between the Activity being created



// by the ASP.NET core instrumentation and the call to this method.



AzureFunctionsInstrumentation.AddIncomingHttpAzureFunctionCallInfo(Activity.Current, ctx);



// Your handler code...



}



}



}
```

Additionally, you need to modify `host.json` to allow logging for `Dynatrace.OpenTelemetry`.
Note that this does not enable logging unless [explicitly configured](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace."). See [InitializeLogging](#initializelogging).

```
{



"version": "2.0",



"logging": {



// ...



"logLevel": {



"Dynatrace.OpenTelemetry": "Debug"



}



}



}
```

## Example using the dotnet-isolated runtime

The following examples use the [built-in HTTP modelï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model) of Azure functions and do **not** apply to functions using the [ASP.NET core integrationï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) of isolated Azure functions. See the chapter about [`ASP.NET core integration`](#asp-net-core-integration) below.

Your `Program.cs` could look as follows:

OpenTelemetry versions earlier than 1.4

OpenTelemetry version 1.4+

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWorkerDefaults(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetryTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWorkerDefaults(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

No additional code is needed to instrument functions; everything is handled by the middleware.

## ASP.NET core integration (isolated runtime)

If you create a new project for Azure function .NET8 or laterâfor example, using Visual Studio templateâthen, it'll add [ASP.NET core integrationï»¿](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) in Azure Function by default.

To enable function tracing, you need to use only the `ConfigureFunctionsWebApplication` method instead of `ConfigureFunctionsWorkerDefaults` in your initialization code given in [`ASP.NET core integration`](#asp-net-core-integration). The initialization code may look as follows:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker;



using Microsoft.Extensions.DependencyInjection;



using Microsoft.Extensions.Hosting;



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



.ConfigureFunctionsWebApplication(fw => fw.UseTracingMiddleware())



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddAzureFunctionsInstrumentation()



// ... any custom OTel setup ...



.AddDynatrace()



// ... if you need custom resources, set them after AddDynatrace (see below)



))



.Build();



host.Run();
```

## Technical details

### `InitializeLogging`

* Calling `InitializeLogging` is required even if you don't plan to enable logging, and the actual log messages won't be logged even after calling this method, unless [configured](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.").
* If you use the [`dotnet-isolated` runtimeï»¿](https://dt-url.net/2i23yrm) (out-of-process, worker functions), you need to call `InitializeLogging` in your `Main` method before calling `AddDynatrace`. You can pass `null` as `loggerFactory`, so that, if enabled, logging can use `Console.Out`/`Console.Error`. This is automatically forwarded to AppInsights for the `dotnet-isolated` runtime.
* If you have specific requirements, you can also pass any custom `LoggingFactory`.
* For the [`dotnet` runtimeï»¿](https://dt-url.net/2r43yf7) (in-process, class-library), sending logs to AppInsights requires using an `ILogger` or `ILoggerFactory` injected into the function with a dependency injection. Thus, you shouldn't use `null` as an argument for the `loggerFactory` parameter, but call `InitializeLogging` the first time any function in your Function App is invoked. To get the `ILoggerFactory`, simply add a parameter of that type.
* If you use the `ILoggerFactory` provided by Azure Functions, you also need to modify `host.json` to enable logging there. We recommend that you always use the `debug` log-level in `host.json`, as the actual log messages handed to the ILogger are separately configured in the Dynatrace configuration.

  ```
  {



  "version": "2.0",



  "logging": {



  // ...



  "logLevel": {



  "Dynatrace.OpenTelemetry": "Debug"



  }



  }



  }
  ```

### `AddDynatrace`

* `AddDynatrace` is an extension method to OpenTelemetry's `TracerProvider`. It requires `using Dynatrace.OpenTelemetry`. Currently, there aren't any additional parameters for this function, as configuration is read from environment variables and a `dtconfig.json` file. For details, see [Set up OpenTelemetry monitoring for Azure Functions on Consumption Plan](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Monitor Azure Functions consumption plan with OpenTelemetry and Dynatrace.").
* `AddDynatrace` mainly adds an `ActivityProcessor` to the `TracerProvider` that will send all activities to Dynatrace. This extension:

  + Sets the resources required by Dynatrace. Due to [an issue with the OpenTelemetry .NET SDKï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/issues/2909), this will override any existing resources. If you need custom resources, you need to call `SetResourceBuilder` on the `TracerProvider` *after* `AddDynatrace`. Be aware that this will override the resources configured by `AddDynatrace` and you need to readd them as part of the same `SetResourceBuilder` call. You can do this by calling the OpenTelemetry SDK's `AddTelemetrySdk` extension method on the `ResourceBuilder`.
  + Exchanges the global `Propagators.DefaultTextMapPropagator` with a custom one that is based on the default W3C-format, but does additional processing of `tracestate` and additional Dynatrace-specific HTTP headers. The baggage propagator is also enabled, as is default for OpenTelemetry .NET. There's currently no way to disable it. Using another propagator isn't supported and will lead to missing links in the distributed traces.

The following minimal snippet might be used to initialize a `TracerProvider` with `AddDynatrace`:

```
using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions;



using OpenTelemetry.Trace;



// ...



// (call DynatraceSetup.InitializeLogging before or after AddDynatrace depending on runtime)



// ...



TracerProvider tracerProvider = Sdk.CreateTracerProviderBuilder().AddDynatrace().Build();
```

### `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync`

This is the low-level instrumentation function provided in the `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` package. You usually shouldn't use these, but instead use the runtime-specific helpers, as in the [examples above](#helper-usage-examples).

This function creates and starts a `System.Diagnostics.Activity`. It runs the handler function argument, then stops `Activity` and records any exception on it. An example usage could look like this:

```
public class HttpExample {



private readonly TracerProvider _tracerProvider;



public HttpExample(TracerProvider tracerProvider) {



_tracerProvider = tracerProvider;



}



[Function("HttpExample")]



public IActionResult Run([HttpTrigger(AuthorizationLevel.Function, "get")] HttpRequestData req, FunctionContext ctx)



{



var parent = ExtractParentContext(req, ctx); // See further below after this code snippet



return AzureFunctionsCoreInstrumentation.Trace(_tracerProvider, ctx.FunctionDefinition.Name, () => RunInternal(req), parent);



}



public IActionResult RunInternal(HttpRequestData req)



{



// ... your actual handler code ...



return new OkObjectResult("Your result");



}



}
```

The parent `ActivityContext` must be extracted from the HTTP headers using the `Propagators.DefaultTextMapPropagator`, which `AddDynatrace` initializes. If you don't pass any parent, a trace root span will be created (`Activity.Current` won't be used).

This is how a parent could be manually extracted with in-process functions for use with `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync` when not using the ASP.NET core instrumentation:

```
private static ActivityContext ExtractParentContext(HttpRequest request)



{



var context = Propagators.DefaultTextMapPropagator.Extract(default, request, HeaderValuesGetter);



return context.ActivityContext;



}



private static IEnumerable<string> HeaderValuesGetter(HttpRequest request, string name) =>



request.Headers.TryGetValue(name, out var values) ? values : (IEnumerable<string>)null;
```

For worker functions, the code can become more complex because in addition to HTTP headers, you may want to
(but don't have to) use the W3C TraceContext provided in the `FunctionContext`:

```
private static ActivityContext ExtractParentContext(HttpRequestData request, FunctionContext context) {



ActivityContext parent = default;



PropagationContext ctx = Propagators.DefaultTextMapPropagator.Extract(



default,



request.Headers,



(c, k) => c.TryGetValues(k, out var value) ? value : null);



parent = ctx.ActivityContext;



if (parent == default)



{



PropagationContext ctx2 = Propagators.DefaultTextMapPropagator.Extract(



default,



context.TraceContext,



(c, k) =>



{



string? result =



k.Equals("traceparent", StringComparison.OrdinalIgnoreCase) ? c.TraceParent :



k.Equals("tracestate", StringComparison.OrdinalIgnoreCase) ? c.TraceState :



null;



return result == null ? null : new[] { result };



});



parent = ctx2.ActivityContext;



}



return parent;



}
```

## Instrumenting `HttpClient` calls (outgoing HTTP requests)

A very common need is to trace outgoing HTTP requests. This can be achieved by using the [`OpenTelemetry.Instrumentation.Http` NuGet packageï»¿](https://www.nuget.org/packages/OpenTelemetry.Instrumentation.Http).

The instrumentation then has to be added to your `TracerProvider` setup by calling `AddHttpClientInstrumentation`, for example, in `Program.cs`:

OpenTelemetry versions earlier than 1.4

OpenTelemetry version 1.4+

```
// ...



using OpenTelemetry.Trace;



// ...



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



// ...



.ConfigureServices(services => services



.AddOpenTelemetryTracing(tracing => tracing



// ...



.AddHttpClientInstrumentation(op =>



{



// Exclude outgoing calls to external telemetry endpoints



op.Filter = AzureFunctionsCoreInstrumentation.FilterExternalTelemetry;



})))



.Build();



// ...
```

```
// ...



using OpenTelemetry.Trace;



// ...



DynatraceSetup.InitializeLogging();



var host = new HostBuilder()



// ...



.ConfigureServices(services => services



.AddOpenTelemetry()



.WithTracing(tracing => tracing



.AddHttpClientInstrumentation(op =>



{



// Exclude irrelevant outgoing calls (e.g. AppInsights QuickPulse pings)



op.FilterHttpRequestMessage = AzureFunctionsCoreInstrumentation.FilterExternalTelemetry;



})))



.Build();



host.Run();
```

Using a request filter as in the example above is highly recommended, as otherwise, depending on your Function Apps configuration, you might observe a large number of periodic requests to `https://rt.services.visualstudio.com/QuickPulseService.svc/ping` or similar URLs.

Alternatively, you can [disable telemetry dynamicallyï»¿](https://dt-url.net/95038ca).

We recommend to use the helper function `AzureFunctionsCoreInstrumentation.FilterExternalTelemetry` which is available in package `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` since version 1.267. In earlier versions, you can use the following filter instead:

```
op.FilterHttpRequestMessage = req => Activity.Current?.Parent != null;
```

Because of an [Azure Functions runtime issueï»¿](https://github.com/Azure/azure-functions-host/issues/7278), the HTTP instrumentation won't work on Azure Functions in-process version 3.x.

The underlying issue can also affect other instrumentations. Therefore, we do not recommend using in-process version 3 functions.

## Related topics

* [Set up Dynatrace on Microsoft Azure](/docs/ingest-from/microsoft-azure-services "Set up and configure monitoring for Microsoft Azure.")