---
title: Trace .NET Lambda functions
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration
scraped: 2026-02-20T21:11:07.785292
---

# Trace .NET Lambda functions

# Trace .NET Lambda functions

* How-to guide
* 9-min read
* Updated on Aug 24, 2023

Dynatrace uses [OpenTelemetryï»¿](https://dt-url.net/y903u4j) to monitor AWS Lambda invocations.

## Prerequisites

Ensure that you use a [supported AWS Lambda runtime](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "AWS Lambda capabilities and integration options") and that you have followed the **initial configuration** steps described in [Monitor AWS Lambda with OpenTelemetry](/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup "Prerequisites for monitoring AWS Lambda with OpenTelemetry") before using the packages below.

The following NuGet packages can be used to cover different aspects of AWS Lambda tracing:

* Recommended OpenTelemetry.Instrumentation.AWSLambda version 1.2.0-beta.1+âcontains methods to trace incoming AWS Lambda invocations, such as calls triggered by AWS SQS/SNS messages.
* Recommended OpenTelemetry.Instrumentation.AWS version 1.1.0-beta.1+âtraces outgoing AWS SDK calls to other AWS Lambda invocations and calls to AWS services, such as DynamoDB, SQS, and SNS.
* Required `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`âenables linking through outgoing AWS Lambda Invoke SDK calls from one Lambda to another. This is the only way to link these kinds of requests; however, if you don't need such linking or don't use the AWS Lambda client SDK to invoke or receive other Lambda invocations, you can replace the package with `Dynatrace.OpenTelemetry`.

## Installation

Any of the above-listed packages can be installed via the CLI. For example, `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` can be installed using the following command:

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AwsLambda
```

Some packages may require you to specify a version explicitly or use the `--prerelease` command line flag, such as
`dotnet add package --prerelease OpenTelemetry.Instrumentation.AWSLambda`.

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

## Initialization

The initialization code for AWS Lambda tracing in your `Function.cs` file could look as follows (where `Function` is the configured Lambda handler class):

```
using System.Threading.Tasks;



using Amazon.Lambda.Core;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AwsLambda;



using OpenTelemetry;



using OpenTelemetry.Instrumentation.AWSLambda;



using OpenTelemetry.Trace;



[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]



namespace Examples.AwsFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



static Function()



{



DynatraceSetup.InitializeLogging();



TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddDynatrace()



// Configures AWS Lambda invocations tracing



.AddAWSLambdaConfigurations(c => c.DisableAwsXRayContextExtraction = true)



// Instrumentation for creation of span (Activity) representing AWS SDK call.



// Can be omitted if there are no outgoing AWS SDK calls to other AWS Lambdas and/or calls to AWS services like DynamoDB and SQS.



.AddAWSInstrumentation(c => c.SuppressDownstreamInstrumentation = true)



// Adds injection of Dynatrace-specific context information in certain SDK calls (e.g. Lambda Invoke).



// This is required if there are outgoing calls to other Lambdas or DynamoDB using AWS SDK clients.



.AddDynatraceAwsSdkInjection()



.Build();



}



}



}
```

* Setting the option `DisableAwsXRayContextExtraction` to `true` is required to skip Amazon X-Ray parent extraction, which may conflict with the Dynatrace propagation.
* If the option `SuppressDownstreamInstrumentation` is set to `true`, HTTP child nodes will not be shown under AWS SDK calls.

## Tracing incoming AWS Lambda calls

### Example 1: Trace an AWS Lambda invoked via AWS SDK

In addition to the initialization part provided [above](#initialization), the handler method of a Lambda invoked via AWS SDK could look as follows:

```
using System.Threading.Tasks;



using Amazon.Lambda.Core;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AwsLambda;



using OpenTelemetry;



using OpenTelemetry.Instrumentation.AWSLambda;



using OpenTelemetry.Trace;



[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]



namespace Examples.AwsFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



// Use initialization code from the "Initialization" section of the docs



public Task FunctionHandlerAsync(object input, ILambdaContext context)



{



var propagationContext = AwsLambdaHelpers.ExtractPropagationContext(context);



return AWSLambdaWrapper.TraceAsync(TracerProvider, FunctionHandlerInternalAsync, input, context, propagationContext.ActivityContext);



}



private Task FunctionHandlerInternalAsync(object input, ILambdaContext context)



{



// This is just an example of function handler and should be replaced by actual code.



return Task.CompletedTask;



}



}



}
```

* A parent context is extracted explicitly using the `AwsLambdaHelpers` class from the `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` package.
* An activity tracing the incoming request and the handler is created by the `TraceAsync` method.
* `TraceAsync` should be used when you trace an async function or a function returning a task. That way, the activity ends only when the task completes.

### Example 2: Trace an AWS Lambda invoked via Amazon API Gateway (incoming HTTP request)

In addition to the initialization part provided above, the Lambda handler invoked via Amazon API Gateway could look as follows:

```
using Amazon.Lambda.APIGatewayEvents;



using Amazon.Lambda.Core;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AwsLambda;



using OpenTelemetry;



using OpenTelemetry.Instrumentation.AWSLambda;



using OpenTelemetry.Trace;



[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]



namespace Examples.AwsFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



// Use initialization code from the "Initialization" section of the docs



public APIGatewayHttpApiV2ProxyResponse FunctionHandler(APIGatewayHttpApiV2ProxyRequest request, ILambdaContext context)



{



return AWSLambdaWrapper.Trace(TracerProvider, FunctionHandlerInternal, request, context);



}



private APIGatewayHttpApiV2ProxyResponse FunctionHandlerInternal(APIGatewayHttpApiV2ProxyRequest request, ILambdaContext context)



{



// This is just an example of function handler and should be replaced by actual code.



return new APIGatewayHttpApiV2ProxyResponse



{



StatusCode = 200,



Body = "Example function result",



};



}



}



}
```

* A parent context is extracted from the incoming request in the `Trace` (or `TraceAsync`) method.
* An activity tracing the incoming request and the handler is created by the `Trace` method.
* In general, the `Trace`/`TraceAsync` methods support any trigger, but extended support is available for the `APIGatewayProxyRequest` and `APIGatewayHttpApiV2ProxyRequest` trigger types. For more details about request/response types, consult the [GitHub documentationï»¿](https://dt-url.net/wm034ja).
* `Trace` should only be used when you have a function returning something other than a `Task`. For the asynchronous handler, `TraceAsync` should be used instead.

### Example 3: Tracing without the `AwsLambda` package

If you prefer not to use the `OpenTelemetry.Instrumentation.AWSLambda` package, you can manually create an activity for Lambda. Note that this involves quite a bit of work, as Dynatrace requires certain activity tags (span attributes) to detect the service (conforming to the OpenTelemetry FaaS [trace conventionsï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/trace/semantic_conventions/faas.md)
and [resource conventionsï»¿](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/resource/semantic_conventions/faas.md)). You also need to manually extract the parent context.

For this example, only the `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` package is required.

```
using System;



using System.Collections.Generic;



using System.Diagnostics;



using System.Reflection;



using Amazon.Lambda.APIGatewayEvents;



using Amazon.Lambda.Core;



using Dynatrace.OpenTelemetry;



using Dynatrace.OpenTelemetry.Instrumentation.AwsLambda;



using OpenTelemetry;



using OpenTelemetry.Context.Propagation;



using OpenTelemetry.Trace;



[assembly: LambdaSerializer(typeof(Amazon.Lambda.Serialization.SystemTextJson.DefaultLambdaJsonSerializer))]



namespace Examples.AwsFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



private static readonly ActivitySource ActivitySource;



static Function()



{



DynatraceSetup.InitializeLogging();



var activitySourceName = Assembly.GetExecutingAssembly().GetName().Name;



ActivitySource = new ActivitySource(activitySourceName);



TracerProvider = Sdk.CreateTracerProviderBuilder()



.AddSource(activitySourceName)



.AddDynatrace()



.Build();



}



public static IEnumerable<KeyValuePair<string, object>> GetFunctionTags(ILambdaContext context, string trigger)



{



return new KeyValuePair<string, object>[]



{



new("faas.name", context.FunctionName),



new("faas.id", context.InvokedFunctionArn),



new("faas.trigger", trigger),



new("cloud.platform", "aws_lambda"),



new("cloud.provider", "aws"),



new("cloud.region", Environment.GetEnvironmentVariable("AWS_REGION")),



};



}



public APIGatewayProxyResponse FunctionHandler(APIGatewayHttpApiV2ProxyRequest apiGatewayProxyEvent, ILambdaContext context)



{



try



{



var parentContext = ExtractParentContext(apiGatewayProxyEvent, context);



using var activity = ActivitySource.StartActivity(ActivityKind.Server, parentContext, GetFunctionTags(context, "http"));



return new APIGatewayProxyResponse



{



StatusCode = 200,



Body = "Example function result",



};



}



catch (Exception ex)



{



context.Logger.LogLine($"Exception occurred while handling request: {ex.Message}");



throw;



}



finally



{



TracerProvider?.ForceFlush();



}



}



private static ActivityContext ExtractParentContext(APIGatewayHttpApiV2ProxyRequest apiGatewayProxyEvent, ILambdaContext context)



{



var propagationContext = AwsLambdaHelpers.ExtractPropagationContext(context);



if (propagationContext == default)



{



propagationContext = Propagators.DefaultTextMapPropagator.Extract(default, apiGatewayProxyEvent, HeaderValuesGetter);



}



return propagationContext.ActivityContext;



}



private static IEnumerable<string> HeaderValuesGetter(APIGatewayHttpApiV2ProxyRequest apiGatewayProxyEvent, string name) =>



(apiGatewayProxyEvent.Headers != null && apiGatewayProxyEvent.Headers.TryGetValue(name.ToLowerInvariant(), out var value)) ? new[] { value } : null;



}



}
```

## Tracing AWS SDK calls

You can use open-source instrumentation NuGet packages to trace Amazon DynamoDB calls using client like `AmazonDynamoDBClient` or SQS and SNS calls using clients like `AmazonSQSClient`or `AmazonSimpleNotificationServiceClient`.

To set up tracing of AWS SDK calls,

1. Make sure that the following packages are added to your project:

   * `OpenTelemetry.Instrumentation.AWSLambda`
   * `OpenTelemetry.Instrumentation.AWS`

   To learn more about the packages, see [Prerequisites](#prerequisites).
2. After you add packages to your project, add the following initialization code:

   ```
   using Dynatrace.OpenTelemetry;



   using OpenTelemetry;



   using OpenTelemetry.Trace;



   namespace Examples.AwsFunctionApp



   {



   public class Function



   {



   private static readonly TracerProvider TracerProvider;



   static Function()



   {



   DynatraceSetup.InitializeLogging();



   TracerProvider = Sdk.CreateTracerProviderBuilder()



   .AddDynatrace()



   .AddAWSLambdaConfigurations(c =>



   {



   c.DisableAwsXRayContextExtraction = true;



   c.SetParentFromBatch = true;



   })



   // Instrumentation used for tracing outgoing calls to AWS services via AWS SDK (including Amazon DynamoDB, SQS/SNS).



   // Can be omitted if no outgoing AWS SDK calls expected.



   .AddAWSInstrumentation(c => c.SuppressDownstreamInstrumentation = true)



   .Build();



   }



   }



   }
   ```

   Values description

   * `SuppressDownstreamInstrumentation`  
     When set to `true`, HTTP child nodes will not be shown under AWS SDK calls.
   * SQS `SetParentFromBatch`

     It controls whether the parent Activity should be set when a potentially batched event is received where multiple parents would be available (e.g. SQS). When set to `true` the parent is set using one of the received messages. Else, the parent is not set. In both cases, links will be created.
   * `DisableAwsXRayContextExtraction`  
     We reccomend to set it to `true` to skip Amazon X-Ray parent extraction and avoid conflicts with the Dynatrace propagation.

### Tracing of Amazon DynamoDB operations

To trace Amazon DynamoDB calls, [set up AWS SDK instrumentation](#setup-aws-services-calls), ensure you have at least version 1.327.0 of `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` and add call `.AddDynatraceAwsSdkInjection()` to your [initialization code](#initialization).
`Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` and add call `.AddDynatraceAwsSdkInjection()` to your initialization code.

In the following example, the DynamoDB operations `DescribeTable`, `UpdateItem`, and `GetItem` are represented as separate span child nodes with a common parent `outbound-aws-dotnet in eu-central-1` (Lambda function performing DynamoDB operations):

![AWS Lambda .NET DynamoDB spans](https://dt-cdn.net/images/dynamodb-dotnet-1913-478c4bb6cb.png)

### Tracing of outgoing SQS/SNS messages

To trace outgoing SQS/SNS messages, [set up AWS SDK instrumentation](#setup-aws-services-calls). No additional code is required.

### Tracing of incoming SQS/SNS messages

To trace incoming SQS/SNS messages,

1. [Set up AWS SDK instrumentation](#setup-aws-services-calls).
2. Wrap the function handler into one of the tracing methods of the `AWSLambdaWrapper` class:

```
using Amazon.Lambda.Core;



using Amazon.Lambda.SQSEvents;



using Dynatrace.OpenTelemetry;



using OpenTelemetry;



using OpenTelemetry.Instrumentation.AWSLambda;



using OpenTelemetry.Trace;



using System.Threading.Tasks;



namespace Examples.AwsFunctionApp



{



public class Function



{



private static readonly TracerProvider TracerProvider;



static Function()



{



// See "Set up tracing for AWS SDK calls" section above.



}



public Task Handler(SQSEvent sqsEvent, ILambdaContext context) =>



AWSLambdaWrapper.TraceAsync(tracerProvider, HandlerInternal, sqsEvent, context);



private Task HandlerInternal(SQSEvent sqsEvent, ILambdaContext context)



{



// This is just an example of async function handler and it should be replaced by actual code.



return Task.CompletedTask;



}



}



}
```

## Special considerations for HttpClient instrumentation

Because with AWS Lambda the function execution environment might be suspended at any time after the function handler execution, the span export might be interrupted or delayed (for example, in some cases, the span might not be exported at all) and outgoing HTTP requests will typically appear only with the next function invocation.

However, outgoing HTTP request activities related to [AWS Runtime APIï»¿](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html#runtimes-api-next) might be captured by [OpenTelemetry HttpClient instrumentationï»¿](https://github.com/open-telemetry/opentelemetry-dotnet/tree/main/src/OpenTelemetry.Instrumentation.Http) in the current function invocation, even if unexpected. To avoid unexpected outgoing HTTP requests in the current function invocation, we recommend configuring the following filter when initializing the HttpClient instrumentation.

```
var tracerProvider = Sdk.CreateTracerProviderBuilder()



// Initialization code similar to previous examples...



.AddHttpClientInstrumentation(op =>



{



op.FilterHttpRequestMessage = req => Activity.Current?.Parent?.IsAllDataRequested ?? false;



})



.Build();
```

## Support of .NET Lambda functions with container images

Starting from .NET 6, Lambda functions can be [built and deployed as container imagesï»¿](https://dt-url.net/yz038r7). Initialization and tracing for [Managed .NET runtime](/docs/ingest-from/technology-support/application-software/dotnet "Learn about all aspects of Dynatrace support for .NET application monitoring.") apply to container image functions without any changes.