---
title: Trace AWS Lambda .NET Core functions with OpenTelemetry .NET
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native
scraped: 2026-05-12T11:27:43.486292
---

# Trace AWS Lambda .NET Core functions with OpenTelemetry .NET

# Trace AWS Lambda .NET Core functions with OpenTelemetry .NET

* How-to guide
* 6-min read
* Updated on Sep 23, 2022

New version available

While you can use the vanilla OpenTelemetry capabilties to instrument your AWS Lambda functions for .NET as described within this tutorial, we recommend to follow our up-leveled version to  
[trace AWS Lambda .NET functions](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Trace AWS Lambda functions using a .NET runtime"), which heavily reduces instrumentation effort and gives deeper and better insights into your function invocations.

In Feb 2021, AWS announced [Support for AWS Distro for OpenTelemetry .NET Tracingï»¿](https://aws.amazon.com/de/blogs/opensource/aws-distro-for-opentelemetry-adds-net-tracing-support/). For general information about AWS Distro for OpenTelemetry, see the [AWS Distro for OpenTelemetryï»¿](https://aws-otel.github.io/) page.

For tracing AWS Lambda for other languages such as Java, Node.JS, and Python using the Dynatrace AWS Lambda Layer, see [Deploy OneAgent as Lambda extension](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Monitor Lambda functions written in Python, Node.js, and Java.").

## Prerequisites

The following prerequisites and limitations apply:

* Dynatrace version 1.222+
* W3C Trace Context is enabled

  1. Go to **Settings** > **Preferences** > **OneAgent features**.
  2. Turn on **Send W3C Trace Context HTTP headers**.

The OpenTelemetry Protocol (OTLP) exporters for .NET currently support [gRPC and HTTP 1.1 with binary Protocol Buffers (Protobuf) payloadï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#exporters) transports. Supported corresponding protocol values are `grpc` and `http/protobuf`. [Configuration optionsï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options) can be set either via environment variables or explicitly in code.

## Instrument AWS Lambda .NET Core functions

Dynatrace uses OpenTelemetry trace ingest to provide end-to-end visibility to your AWS Lambda .NET Core functions.

To instrument your AWS Lambda .NET Core functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Set up export**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#export "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Add dependencies**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#instrument-handler "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Add OpenTelemetry Tracer**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#tracer "Learn how to use OpenTelemetry to trace AWS Lambda .NET Core functions.")

## Step 1 Set up export

gRPC export

HTTP export

To ingest gRPC via the Dynatrace Trace API, you need to use an [OpenTelemetry collectorï»¿](https://dt-url.net/vf23sfn) between Dynatrace and the exporter. You can choose to either self-host a collector or use the AWS Distro for OpenTelemetry Collector (ADOT Collector).

If you use environment variables for setup, you need to set the following value:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `grpc`

### Add the ARN of the Lambda Layer ADOT Collector

AWS region

Lambda layers are a rationalized resource, meaning that they can only be used in the AWS region in which they are published. Make sure to use the layer in the same region as your Lambda functions.

Collector layer: `aws-otel-collector-ver-0-27-0`.

For a complete list of the AWS-managed OpenTelemetry Lambda layers, see [AWS Distro for OpenTelemetry - AWS Lambda repositoryï»¿](https://github.com/aws-observability/aws-otel-lambda)

Lambda layer ARN format is:

```
arn:aws:lambda:\<region>:901920570463:layer:<layer>:1
```

### Configure ADOT Collector

The configuration of the ADOT Collector follows the OpenTelemetry standard.

By default, the ADOT Lambda layer uses the `config.yaml` file, which exports OpenTelemetry data to AWS X-Ray. To export the data to Dynatrace, you need to customize the configuration using the OpenTelemetry OTLP exporter.

To customize the collector configuration, add a configuration YAML file to your function code. After the file has been deployed with a Lambda function, create environment variable `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` on your Lambda function and set it to `/var/task/<path>/<to>/<filename>`. This tells the extension where to find the collector configuration.

Here is a sample configuration file, `collector.yaml`, in the root directory:

1. Copy `collector.yaml` in the root directory
2. Set an environment variable `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` to `/var/task/<path>/<to>/<file>`

```
receivers:



otlp:



protocols:



grpc:



exporters:



otlp_http:



endpoint: "https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp"



headers: {"Authorization": "Api-Token <YOUR-DYNATRACE-API-TOKEN>"}



service:



pipelines:



traces:



receivers: [otlp]



exporters: [otlp_http]
```

For further details on configuration, see [OpenTelemetry and Dynatrace](/managed/ingest-from/opentelemetry "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

You can set this via the Lambda console or the AWS CLI. With the CLI, use the following command:

```
aws lambda update-function-configuration --function-name Function --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_FILE=/var/task/collector.yaml}
```

You can also configure environment variables via CloudFormation template:

```
Function:



Type: AWS::Serverless::Function



Properties:



...



Environment:



Variables:



OPENTELEMETRY_COLLECTOR_CONFIG_FILE: /var/task/collector.yaml
```

To ingest HTTP via the Dynatrace Trace API, you need to [configure the exporterï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options). The exporter will then directly send traces to the configured endpoint.

If you use environment variables for setup, you need to set the following values:

* For `OTEL_EXPORTER_OTLP_PROTOCOL`: `http/protobuf`
* For `OTEL_EXPORTER_OTLP_ENDPOINT`: the URL for export endpoint

  + If you set the endpoint URL via environment variables, the export endpoints for traces and metrics are automatically appended by `v1/traces` for traces and `v1/metrics` for metrics. For example, if the endpoint is set to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp`, traces will be exported to `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp/v1/traces`.
  + If you set the endpoint explicitly in code, it will be used as is.

  For details, see [Endpoint URLs for OTLP/HTTPï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#endpoint-urls-for-otlphttp).
* For `OTEL_EXPORTER_OTLP_HEADERS`: the authorization API token value in the following format: `Authorization=Api-Token <TOKEN>`.

## Step 2 Add dependencies

Add the following dependencies via NuGet to your project:

```
OpenTelemetry.Exporter.OpenTelemetryProtocol
```

If you are using the AWS SDK to interact with other AWS services, you can add auto-instrumentation using the ADOT SDK for .NET

```
OpenTelemetry.Contrib.Instrumentation.AWS
```

OpenTelemetry also provides other [auto-instrumentation libraries available as NuGet packagesï»¿](https://www.nuget.org/packages?q=opentelemetry.instrumentation)

## Step 3 Add OpenTelemetry Tracer

gRPC export

HTTP export

The AWS Distro for OpenTelemetry doesn't provide a wrapper layer for .NET as it does for other languages. You need to add a tracer to your code and create a trace root span.

The following sample uses an [AWS Lambda Proxy Integrationï»¿](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) and gRPC transport.

If you don't set the `Protocol` property of the `OtlpExporterOptions` class via environment variables or in code, it will be initialized as [`OtlpExportProtocol.Grpc` by defaultï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry.Exporter.OpenTelemetryProtocol/OtlpExporterOptions.cs#L99).

```
public class Functions



{



public Functions() {}



//Defines the OpenTelemetry resource attribute "service.name" which is mandatory



private const string servicename = "AWS Lambda";



//Defines the OpenTelemetry Instrumentation Scope.



private const string activitySource = "MyCompany.MyProduct.MyLibrary";



//Provides the API for starting/stopping activities.



private static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



public async Task<APIGatewayProxyResponse> Get(APIGatewayProxyRequest request, ILambdaContext context)



{



AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport",true);



//Initialize OpenTelemetry Tracer



using (Sdk.CreateTracerProviderBuilder()



.SetSampler(new AlwaysOnSampler())



.AddSource(activitySource)



.SetResourceBuilder(ResourceBuilder.CreateDefault().AddService(servicename))



.AddAWSInstrumentation() //Add auto-instrumentation for AWS SDK



.AddHttpClientInstrumentation() //Add auto-instrumentation for AWS SDK



.AddOtlpExporter(otlpOptions =>



{



//Use a local endpoint for AWS Lambda ADOT Collector Layer



//or an endpoint configured via environment variable.



var collectorUrl = Environment.GetEnvironmentVariable("COLLECTOR_URL") ?? "http://localhost:55680";



otlpOptions.Endpoint = new Uri(collectorUrl);



})



.Build())



{



//create root-span, connecting with trace-parent read from the http-header



using (var activity = MyActivitySource.StartActivity("Invoke", ActivityKind.Server, request.Headers["traceparent"]))



{



//.....



//... YOUR CODE GOES HERE



//....



}



}



}



}
```

The code sample using **HTTP exporter** is similar to the **gRPC exporter** sample; the only difference is in the configuration of `OtlpExporterOptions`:

```
//Initialize OpenTelemetry Tracer



using (Sdk.CreateTracerProviderBuilder()



// ... other initialization code (see code snippet for the gRPC case)



.AddOtlpExporter(otlpOptions =>



{



otlpOptions.Protocol = OtlpExportProtocol.HttpProtobuf;



otlpOptions.Headers = "Authorization=Api-Token <TOKEN>";



//Use an explicitly set endpoint for export



//or an endpoint configured via environment variable.



otlpOptions.Endpoint = new Uri("https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp");



})



.Build())



{



// ... span creation code and your code goes here (see code snippet for the gRPC case)



}
```

If configuration is done via environment variables, the code for adding an OTLP/HTTP exporter looks even simpler:

```
//Initialize OpenTelemetry Tracer



using (Sdk.CreateTracerProviderBuilder()



// ... other initialization code (see code snippet for the gRPC case)



.AddOtlpExporter()



.Build())



{



// ... span creation code and your code goes here (see code snippet for the gRPC case)



}
```