---
title: Instrument your .NET application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/dotnet
scraped: 2026-02-24T21:32:19.929892
---

# Instrument your .NET application with OpenTelemetry

# Instrument your .NET application with OpenTelemetry

* Latest Dynatrace
* How-to guide
* 7-min read
* Updated on Nov 14, 2023

This walkthrough shows how to add observability to your .NET application using the OpenTelemetry .NET libraries and tools.

| Feature | Supported |
| --- | --- |
| Automatic instrumentation | Yes |
| Traces | Yes |
| Metrics | Yes |
| Logs | Yes |

## Prerequisites

* Dynatrace version 1.254+
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

For .NET, OpenTelemetry supports automatic and manual instrumentation (or a combination of both).

Which instrumentation should I choose?

It's a good idea to start with automatic instrumentation and add manual instrumentation if the automatic approach doesn't work or doesn't provide enough information.

## Step 3 optional Automatically instrument your application Optional

.NET automatic instrumentation can be configured either during development or later after deployment.

Enrichment with OneAgent

It is currently not possible to [enrich](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") automatically instrumented services with host-relevant information. To achieve this, you'd need to switch to manual instrumentation.

During development

After deployment

1. Install [`OpenTelemetry.Extensions.Hosting`ï»¿](https://www.nuget.org/packages/OpenTelemetry.Extensions.Hosting).

   ```
   dotnet add package OpenTelemetry.Extensions.Hosting
   ```
2. Install the appropriate instrumentation library for your .NET framework (full list available [hereï»¿](https://www.nuget.org/packages?q=OpenTelemetry.Instrumentation)).

   ```
   dotnet add package OpenTelemetry.Instrumentation.[FRAMEWORK_NAME]
   ```

1. Download the [latest auto installerï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest) for the target operating system.
2. [Run (on Unix)ï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#shell-scripts) or [import (on Windows)ï»¿](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#powershell-module-windows) the auto installer, to install and set up all necessary auto instrumentation libraries.
3. Run your application.

In addition to the instrumentation setup above, you also need to configure the relevant export parameters with environment variables. This includes the [endpoint URL](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), the [authentication token](/docs/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."), and the [temporality preference for metrics](/docs/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Learn how Dynatrace ingests OpenTelemetry metrics and what limitations apply.").

```
OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

## Step 4 optional Manually instrument your application Optional

### Setup

The setup steps slightly differ depending on whether you instrument a plain .NET application or an ASP.NET application.

.NET

ASP.NET

1. Install the following packages.

   ```
   dotnet add package Microsoft.Extensions.Logging



   dotnet add package OpenTelemetry.Extensions.Hosting



   dotnet add package OpenTelemetry



   dotnet add package OpenTelemetry.Api



   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
   ```
2. Add the following `using` statements to the startup class, which bootstraps your application.

   ```
   using OpenTelemetry;



   using OpenTelemetry.Trace;



   using OpenTelemetry.Exporter;



   using OpenTelemetry.Metrics;



   using OpenTelemetry.Logs;



   using OpenTelemetry.Resources;



   using OpenTelemetry.Context.Propagation;



   using System.Diagnostics;



   using System.Diagnostics.Metrics;



   using Microsoft.Extensions.Logging;
   ```
3. Add these fields to your startup class, with the first two containing the [access details](#dynatrace-docs--otlp-export), if you are using the OTLP export.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Add the `initOpenTelemetry` method to your startup class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry(IServiceCollection services)



   {



   List<KeyValuePair<string, object>> dt_metadata = new List<KeyValuePair<string, object>>();



   foreach (string name in new string[] {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"}) {



   try {



   foreach (string line in System.IO.File.ReadAllLines(name.StartsWith("/var") ? name : System.IO.File.ReadAllText(name))) {



   var keyvalue = line.Split("=");



   dt_metadata.Add( new KeyValuePair<string, object>(keyvalue[0], keyvalue[1]));



   }



   }



   catch { }



   }



   Action<ResourceBuilder> configureResource = r => r



   .AddService(serviceName: "dotnet-quickstart") //TODO Replace with the name of your application



   .AddAttributes(dt_metadata);



   services.AddOpenTelemetry()



   .ConfigureResource(configureResource)



   .WithTracing(builder => {



   builder



   .SetSampler(new AlwaysOnSampler())



   .AddSource(MyActivitySource.Name)



   .AddOtlpExporter(options =>



   {



   options.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/traces");



   options.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   options.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   });



   })



   .WithMetrics(builder => {



   builder



   .AddMeter("my-meter")



   .AddOtlpExporter((OtlpExporterOptions exporterOptions, MetricReaderOptions readerOptions) =>



   {



   exporterOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/metrics");



   exporterOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   exporterOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   readerOptions.TemporalityPreference = MetricReaderTemporalityPreference.Delta;



   });



   });



   var resourceBuilder = ResourceBuilder.CreateDefault();



   configureResource!(resourceBuilder);



   loggerFactoryOT = LoggerFactory.Create(builder => {



   builder



   .AddOpenTelemetry(options => {



   options.SetResourceBuilder(resourceBuilder).AddOtlpExporter(options => {



   options.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/logs");



   options.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   options.ExportProcessorType = OpenTelemetry.ExportProcessorType.Batch;



   options.Protocol = OtlpExportProtocol.HttpProtobuf;



   });



   })



   .AddConsole();



   });



   Sdk.CreateTracerProviderBuilder()



   .SetSampler(new AlwaysOnSampler())



   .AddSource(MyActivitySource.Name)



   .ConfigureResource(configureResource);



   // add-logging



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

1. Install the following packages.

   ```
   dotnet add package Microsoft.Extensions.Logging



   dotnet add package OpenTelemetry.Extensions.Hosting



   dotnet add package OpenTelemetry



   dotnet add package OpenTelemetry.Api



   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol



   dotnet add package OpenTelemetry.Instrumentation.AspNetCore



   dotnet add package OpenTelemetry.Instrumentation.Http



   dotnet add package OpenTelemetry.Instrumentation.Runtime
   ```
2. Add the following `using` statements to the startup class, which bootstraps your application.

   ```
   using OpenTelemetry;



   using OpenTelemetry.Trace;



   using OpenTelemetry.Exporter;



   using OpenTelemetry.Metrics;



   using OpenTelemetry.Logs;



   using OpenTelemetry.Resources;



   using OpenTelemetry.Context.Propagation;



   using System.Diagnostics;



   using System.Diagnostics.Metrics;



   using Microsoft.Extensions.Logging;



   using OpenTelemetry.Instrumentation.AspNetCore;
   ```
3. Add these fields to your startup class, with the first two containing the [access details](#dynatrace-docs--otlp-export), if you are using the OTLP export.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Value injection

   Instead of hardcoding the URL and token, you might also consider reading them from storage specific to your application framework (for example, environment variables or framework secrets).
4. Add the `initOpenTelemetry` method to your startup class and invoke it as early as possible during your application startup. This initializes OpenTelemetry for the Dynatrace backend and creates default tracer and meter providers.

   ```
   private static void initOpenTelemetry(){



   var port = System.Environment.GetEnvironmentVariable("PORT") ?? "8080";



   var appBuilder = WebApplication.CreateBuilder();



   appBuilder.WebHost.ConfigureKestrel(options =>{



   options.ListenAnyIP(Convert.ToInt32(port)); // hardcoding the port



   });



   List<KeyValuePair<string, object>> dt_metadata = new List<KeyValuePair<string, object>>();



   foreach (string name in new string[] {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"}) {



   try {



   foreach (string line in System.IO.File.ReadAllLines(name.StartsWith("/var") ? name : System.IO.File.ReadAllText(name))) {



   var keyvalue = line.Split("=");



   dt_metadata.Add( new KeyValuePair<string, object>(keyvalue[0], keyvalue[1]));



   }



   }



   catch { }



   }



   Action<ResourceBuilder> configureResource = r => r



   .AddService(serviceName: "dotnetManual") //TODO Replace with the name of your application



   .AddAttributes(dt_metadata);



   appBuilder.Services.AddOpenTelemetry()



   .ConfigureResource(configureResource)



   .WithTracing(builder =>{



   appBuilder.Services.Configure<AspNetCoreTraceInstrumentationOptions>(appBuilder.Configuration.GetSection("AspNetCoreInstrumentation"));



   builder



   .AddSource(MyActivitySource.Name)



   .SetSampler(new AlwaysOnSampler())



   .AddHttpClientInstrumentation()



   .AddAspNetCoreInstrumentation()



   .AddOtlpExporter(otlpOptions =>{



   otlpOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/traces");



   otlpOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   otlpOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   });



   })



   .WithMetrics(builder =>{



   builder



   .AddMeter("my-meter")



   // .AddMeter(Instrumentation.MeterName)



   .AddRuntimeInstrumentation()



   .AddHttpClientInstrumentation()



   .AddAspNetCoreInstrumentation()



   .AddOtlpExporter((OtlpExporterOptions exporterOptions, MetricReaderOptions readerOptions) => {



   exporterOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/metrics");



   exporterOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   exporterOptions.Protocol = OpenTelemetry.Exporter.OtlpExportProtocol.HttpProtobuf;



   readerOptions.TemporalityPreference = MetricReaderTemporalityPreference.Delta;



   });



   appBuilder.Logging.ClearProviders();



   appBuilder.Logging.AddOpenTelemetry(options =>



   {



   var resourceBuilder = ResourceBuilder.CreateDefault();



   configureResource(resourceBuilder);



   options.SetResourceBuilder(resourceBuilder);



   options.AddOtlpExporter(otlpOptions => {



   otlpOptions.Endpoint = new Uri(Environment.GetEnvironmentVariable("DT_API_URL")+ "/v1/logs");



   otlpOptions.Headers = $"Authorization=Api-Token {Environment.GetEnvironmentVariable("DT_API_TOKEN")}";



   otlpOptions.ExportProcessorType = OpenTelemetry.ExportProcessorType.Batch;



   otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;



   });



   });



   appBuilder.Services.AddControllers();



   appBuilder.Services.AddEndpointsApiExplorer();



   var app = appBuilder.Build();



   app.MapControllers();



   app.Run();



   });



   }
   ```

   The file read operations, parsing the `dt_metadata` files in the example code, attempt to read the [OneAgent data files](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.") to enrich the OTLP request and ensure that all relevant topology information is available within Dynatrace.

### Add tracing

Using `MyActivitySource` from the [setup step](#setup), we can now start new activities (traces):

```
using var activity = Startup.MyActivitySource.StartActivity("Call to /myendpoint", ActivityKind.Consumer, parentContext.ActivityContext);



activity?.SetTag("http.method", "GET");



activity?.SetTag("net.protocol.version", "1.1");
```

In the above code, we:

* Create a new activity (span) and name it "Call to /myendpoint"
* Add two tags (attributes), following the [semantic naming conventionï»¿](https://opentelemetry.io/docs/specs/semconv/general/trace/), specific to the action of this span: information on the HTTP method and version

The activity will be automatically set as the current and active span until the execution flow leaves the current method scope. Subsequent activities will automatically become child spans.

### Collect metrics

1. To instantiate new metric instruments, we first need a meter object.

   ```
   private static readonly Meter meter = new Meter("my-meter", "1.0.0");  //TODO Replace with the name of your meter
   ```
2. With `meter`, we can now create individual instruments, such as a counter.

   ```
   private static readonly Counter<long> counter = meter.CreateCounter<long>("request_counter");
   ```
3. We can now invoke the `Add()` method of `counter` to record new values with our counter and save additional attributes (for example, `action.type`).

   ```
   counter.Add(1, new("ip", "an ip address here"), new("some other key", "some other value"));
   ```

### Connect logs

With the `loggerFactoryOT` variable, we initialized under [Setup](#setup), we can now create individual logger instances, which will pass logged information straight to the configured OpenTelemetry endpoint at Dynatrace.

```
var logger = loggerFactoryOT.CreateLogger<Startup>();



services.AddSingleton<ILoggerFactory>(loggerFactoryOT);



services.AddSingleton(logger);



logger.LogInformation(eventId: 123, "Log line");
```

### Ensure context propagation Optional

[Context propagation](/docs/ingest-from/opentelemetry#context-propagation "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.") is particularly important when network calls (for example, REST) are involved.

If you are using automatic instrumentation and your networking libraries are covered by automatic instrumentation, this will be automatically taken care of by the instrumentation libraries. Otherwise, your code needs to take this into account.

#### Extracting the context when receiving a request

In the following example, we assume that we have received a network call via `System.Web.HttpRequest` and we define a `CompositeTextMapPropagator` instance to fetch the context information from the HTTP headers. We then pass that instance to `Extract()`, returning the context object, which allows us to continue the previous trace with our spans.

```
private CompositeTextMapPropagator propagator = new CompositeTextMapPropagator(new TextMapPropagator[] {



new TraceContextPropagator(),



new BaggagePropagator(),



});



private static readonly Func<HttpRequest, string, IEnumerable<string>> valueGetter = (request, name) => request.Headers[name];



var parentContext = propagator.Extract(default, HttpContext.Request, valueGetter);



using var activity = MyActivitySource.StartActivity("my-span", ActivityKind.Consumer, parentContext.ActivityContext);
```

#### Injecting the context when sending requests

In the following example, we send a REST request to another service and provide our existing context as part of the HTTP headers of our request.

To do so, we define a `TextMapPropagator` instance, which adds the respective information. Once we have instantiated our REST object, we pass it, along with the context and the setter instance, to `Inject()`, which will add the necessary headers to the request.

```
private CompositeTextMapPropagator propagator = new CompositeTextMapPropagator(new TextMapPropagator[] {



new TraceContextPropagator(),



new BaggagePropagator()



});



private static Action<HttpRequestMessage, string, string> _headerValueSetter => (request, name, value) => {



request.Headers.Remove(name);



request.Headers.Add(name, value);



};



propagator.Inject(new PropagationContext(activity!.Context, Baggage.Current), request, _headerValueSetter);
```

## Step 5 optional Configure data capture to meet privacy requirements Optional

While Dynatrace automatically captures all OpenTelemetry attributes, only attribute values specified in the allowlist are stored and displayed in the Dynatrace web UI. This prevents accidental storage of personal data, so you can meet your privacy requirements and control the amount of monitoring data stored.

To view your custom attributes, you need to allow them in the Dynatrace web UI first. To learn how to configure attribute storage and masking, see [Attribute redaction](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Step 6 Verify data ingestion into Dynatrace

Once you have finished the instrumentation of your application, perform a couple of test actions to create and send demo traces, metrics, and logs and verify that they were correctly ingested into Dynatrace.

To do that for traces, go to ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** and select the **Ingested traces** tab. If you use OneAgent, select **PurePaths** instead.

For metrics and logs, go to **Metrics** or ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Related topics

* [Enrich ingested data with Dynatrace-specific dimensions](/docs/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific dimensions.")