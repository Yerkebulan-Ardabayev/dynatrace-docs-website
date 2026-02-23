---
title: Trace Azure Functions with OpenTelemetry .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure
scraped: 2026-02-23T21:25:40.885810
---

# Trace Azure Functions with OpenTelemetry .NET

# Trace Azure Functions with OpenTelemetry .NET

* Latest Dynatrace
* How-to guide
* 4-min read
* Published Mar 09, 2022

The OpenTelemetry Protocol (OTLP) exporters for .NET currently support [gRPC and HTTP 1.1 with binary Protocol Buffers (Protobuf) payloadï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#exporters) transports. Supported corresponding protocol values are `grpc` and `http/protobuf`. [Configuration optionsï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options) can be set either via environment variables or explicitly in code.

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

## Instrument Azure Functions

Dynatrace uses OpenTelemetry Trace Ingest to provide end-to-end visibility to your Azure Functions.

To instrument your Azure Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Set up export**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#export "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add dependencies**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#dependencies "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Instrument code**](/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure#instrument "Learn how to use OpenTelemetry .NET to trace Azure Functions.")

### Step 1 Set up export

gRPC export

HTTP export

To ingest **gRPC** via the Dynatrace Trace API, you need to use an [OpenTelemetry collectorï»¿](https://dt-url.net/vf23sfn) between Dynatrace and the exporter.

If you use environment variables for setup, you need to set the following value:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `grpc`

#### Configure the OpenTelemetry Collector

To ingest **gRPC** via the Dynatrace Trace API, you need to use an [OpenTelemetry collectorï»¿](https://dt-url.net/vf23sfn) between Dynatrace and the exporter.

The OpenTelemetry Collector is available as a [Docker imageï»¿](https://hub.docker.com/r/otel/opentelemetry-collector).
To use this collector to export trace data to Dynatrace, you need to customize the [configurationï»¿](https://opentelemetry.io/docs/collector/configuration/) using the OpenTelemetry OTLP exporter.

Here is a sample configuration file:

```
receivers:



otlp:



protocols:



grpc:



exporters:



otlp_http:



endpoint: "https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp"



headers: {"Authorization": "Api-Token <YOUR-DYNATRACE-API-TOKEN}"}



service:



pipelines:



traces:



receivers: [otlp]



exporters: [otlp_http]
```

For further details on configuration, see [OpenTelemetry and Dynatrace](/docs/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

To ingest **HTTP** via the Dynatrace Trace API, you need to [configure the exporterï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options). The exporter will then directly send traces to the configured endpoint.

If you use environment variables for setup, you need to set the following values:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `http/protobuf`
* For `OTEL_EXPORTER_OTLP_ENDPOINT`: the URL for export endpoint

  + If you set the endpoint URL via environment variables, the export endpoints for traces and metrics are automatically appended by `v1/traces` for traces and `v1/metrics` for metrics. For example, if the endpoint is set to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp`, traces will be exported to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp/v1/traces`.
  + If you set the endpoint explicitly in code, it will be used as is.

  For details, see [Endpoint URLs for OTLP/HTTPï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#endpoint-urls-for-otlphttp).
* For `OTEL_EXPORTER_OTLP_HEADERS`: the authorization API token value in the following format: `Authorization=Api-Token <TOKEN>`.

### Step 2 Add dependencies

Add the following dependencies via NuGet to your project:

```
OpenTelemetry.Exporter.OpenTelemetryProtocol
```

OpenTelemetry also provides other [auto-instrumentation libraries available as NuGet packagesï»¿](https://www.nuget.org/packages?q=opentelemetry.instrumentation).

### Step 3 Instrument code with OpenTelemetry

Intrument using gRPC export

Instrument using HTTP export

If you don't set the `Protocol` property of the `OtlpExporterOptions` class via environment variables or in code, it will be initialized as [`OtlpExportProtocol.Grpc` by defaultï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry.Exporter.OpenTelemetryProtocol/OtlpExporterOptions.cs#L99).

```
public class Startup : FunctionsStartup



{



public override void Configure(IFunctionsHostBuilder builder)



{



string activitySource = "[activitySource]";



string serviceName = "[serviceName]";



string collectorUrl = "[collectorUrl]"  // Points to the running collector, configured before.



builder.Services.AddSingleton((builder) =>



{



return Sdk.CreateTracerProviderBuilder()



.SetSampler(new AlwaysOnSampler())



.AddSource(activitySource)



.SetResourceBuilder(ResourceBuilder.CreateDefault().AddService(serviceName))



.AddHttpClientInstrumentation(op =>



{



// Exclude frequent calls generated by Azure Application Insights



op.FilterHttpRequestMessage = (req) => !req.RequestUri.AbsoluteUri.Contains("visualstudio");



})



.AddOtlpExporter(otlpOptions =>



{



otlpOptions.Endpoint = new Uri(collectorUrl);



})



.Build();



});



}



}
```

The code sample using **HTTP exporter** is similar to the **gRPC exporter** sample; the only difference is in the configuration of `OtlpExporterOptions`:

```
return Sdk.CreateTracerProviderBuilder()



// ...



// ... other initialization code (see the code snippet for the gRPC case)



// ...



.AddOtlpExporter(otlpOptions =>



{



otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;



otlpOptions.Headers = "Authorization=Api-Token <TOKEN>";



//Use an explicitly set endpoint for export



//or an endpoint configured via environment variable.



otlpOptions.Endpoint = new Uri("https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp");



})



.Build();
```

If the configuration is done via environment variables, the code for adding an OTLP/HTTP exporter is even simpler:

```
return Sdk.CreateTracerProviderBuilder()



// ...



// ... other initialization code (see the code snippet for the gRPC case)



// ...



.AddOtlpExporter()



.Build();
```