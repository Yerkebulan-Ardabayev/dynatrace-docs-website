---
title: Трассировка функций .NET Lambda
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration
scraped: 2026-03-05T21:29:40.064891
---

# Трассировка .NET Lambda-функций


Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов AWS Lambda.

## Предварительные требования

Убедитесь, что вы используете [поддерживаемую среду выполнения AWS Lambda](../../aws-lambda-integration.md#support-lifecycle "Возможности и варианты интеграции AWS Lambda") и что вы выполнили шаги **начальной настройки**, описанные в Мониторинг AWS Lambda с помощью OpenTelemetry, прежде чем использовать пакеты ниже.

Следующие пакеты NuGet можно использовать для различных аспектов трассировки AWS Lambda:

* Рекомендуется OpenTelemetry.Instrumentation.AWSLambda версии 1.2.0-beta.1+ — содержит методы для трассировки входящих вызовов AWS Lambda, таких как вызовы, инициированные сообщениями AWS SQS/SNS.
* Рекомендуется OpenTelemetry.Instrumentation.AWS версии 1.1.0-beta.1+ — выполняет трассировку исходящих вызовов AWS SDK к другим вызовам AWS Lambda и вызовов к сервисам AWS, таким как DynamoDB, SQS и SNS.
* Обязательно `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` — обеспечивает связывание через исходящие вызовы AWS Lambda Invoke SDK из одной Lambda в другую. Это единственный способ связать такие запросы; однако если вам не нужно такое связывание или вы не используете AWS Lambda client SDK для вызова или получения вызовов других Lambda, можно заменить пакет на `Dynatrace.OpenTelemetry`.

## Установка

Любой из перечисленных выше пакетов можно установить через CLI. Например, `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` устанавливается следующей командой:

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AwsLambda
```

Для некоторых пакетов может потребоваться явное указание версии или использование флага командной строки `--prerelease`, например
`dotnet add package --prerelease OpenTelemetry.Instrumentation.AWSLambda`.

## Совместимость с версиями OpenTelemetry и `System.Diagnostics.DiagnosticSource`

Периодически нам необходимо обновлять минимальную версию пакета NuGet `OpenTelemetry`,
от которого зависят наши компоненты, и, соответственно, минимальную версию библиотеки `System.Diagnostics.DiagnosticSource`.
В этой таблице указана совместимость между версиями `Dynatrace.OpenTelemetry`, `OpenTelemetry` и `System.Diagnostics.DiagnosticSource`.

| Версия `Dynatrace.OpenTelemetry` | Минимальная версия `OpenTelemetry` | Минимальная версия `System.Diagnostics.DiagnosticSource` |
| --- | --- | --- |
| 1.273 и ранее | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

Обычно вам не нужно беспокоиться об этих зависимостях, так как они определены для вас в нашем пакете NuGet. Это
означает, что при обновлении `Dynatrace.OpenTelemetry` NuGet может неявно обновить версию `OpenTelemetry` или
`System.Diagnostics.DiagnosticSource`, если вы используете более раннюю версию.

## Инициализация

Код инициализации для трассировки AWS Lambda в вашем файле `Function.cs` может выглядеть следующим образом (где `Function` — настроенный класс обработчика Lambda):

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

* Установка параметра `DisableAwsXRayContextExtraction` в `true` необходима для пропуска извлечения родительского контекста Amazon X-Ray, который может конфликтовать с распространением Dynatrace.
* Если параметр `SuppressDownstreamInstrumentation` установлен в `true`, дочерние HTTP-узлы не будут отображаться под вызовами AWS SDK.

## Трассировка входящих вызовов AWS Lambda

### Пример 1: Трассировка AWS Lambda, вызванной через AWS SDK

В дополнение к части инициализации, приведённой [выше](#initialization), метод обработчика Lambda, вызываемой через AWS SDK, может выглядеть следующим образом:

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

* Родительский контекст извлекается явно с помощью класса `AwsLambdaHelpers` из пакета `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`.
* Activity, отслеживающая входящий запрос и обработчик, создаётся методом `TraceAsync`.
* `TraceAsync` следует использовать при трассировке асинхронной функции или функции, возвращающей Task. Таким образом, activity завершается только после завершения задачи.

### Пример 2: Трассировка AWS Lambda, вызванной через Amazon API Gateway (входящий HTTP-запрос)

В дополнение к части инициализации, приведённой выше, обработчик Lambda, вызываемый через Amazon API Gateway, может выглядеть следующим образом:

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

* Родительский контекст извлекается из входящего запроса в методе `Trace` (или `TraceAsync`).
* Activity, отслеживающая входящий запрос и обработчик, создаётся методом `Trace`.
* В целом методы `Trace`/`TraceAsync` поддерживают любой триггер, но расширенная поддержка доступна для типов триггеров `APIGatewayProxyRequest` и `APIGatewayHttpApiV2ProxyRequest`. Для получения дополнительной информации о типах запросов/ответов см. [документацию на GitHub](https://dt-url.net/wm034ja).
* `Trace` следует использовать только когда функция возвращает что-то отличное от `Task`. Для асинхронного обработчика следует использовать `TraceAsync`.

### Пример 3: Трассировка без пакета `AwsLambda`

Если вы предпочитаете не использовать пакет `OpenTelemetry.Instrumentation.AWSLambda`, можно вручную создать activity для Lambda. Обратите внимание, что это требует значительной работы, так как Dynatrace требует определённых тегов activity (атрибутов спана) для обнаружения сервиса (в соответствии с [соглашениями трассировки](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/trace/semantic_conventions/faas.md) OpenTelemetry FaaS
и [соглашениями ресурсов](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/resource/semantic_conventions/faas.md)). Также необходимо вручную извлечь родительский контекст.

Для этого примера требуется только пакет `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`.

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

## Трассировка вызовов AWS SDK

Вы можете использовать пакеты NuGet с открытым исходным кодом для трассировки вызовов Amazon DynamoDB с помощью клиента `AmazonDynamoDBClient`, а также вызовов SQS и SNS с помощью клиентов `AmazonSQSClient` или `AmazonSimpleNotificationServiceClient`.

Для настройки трассировки вызовов AWS SDK:

1. Убедитесь, что в ваш проект добавлены следующие пакеты:

   * `OpenTelemetry.Instrumentation.AWSLambda`
   * `OpenTelemetry.Instrumentation.AWS`

   Подробнее о пакетах см. [Предварительные требования](#prerequisites).
2. После добавления пакетов в проект добавьте следующий код инициализации:

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

   Описание значений

   * `SuppressDownstreamInstrumentation`
     При установке в `true` дочерние HTTP-узлы не будут отображаться под вызовами AWS SDK.
   * SQS `SetParentFromBatch`

     Управляет тем, должен ли устанавливаться родительский Activity при получении потенциально пакетного события, где доступно несколько родителей (например, SQS). При установке в `true` родитель устанавливается с использованием одного из полученных сообщений. В противном случае родитель не устанавливается. В обоих случаях создаются связи.
   * `DisableAwsXRayContextExtraction`
     Рекомендуется установить в `true` для пропуска извлечения родительского контекста Amazon X-Ray и предотвращения конфликтов с распространением Dynatrace.

### Трассировка операций Amazon DynamoDB

Для трассировки вызовов Amazon DynamoDB [настройте инструментацию AWS SDK](#setup-aws-services-calls), убедитесь, что у вас версия не ниже 1.327.0 пакета `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`, и добавьте вызов `.AddDynatraceAwsSdkInjection()` в [код инициализации](#initialization).
`Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` и добавьте вызов `.AddDynatraceAwsSdkInjection()` в код инициализации.

В следующем примере операции DynamoDB `DescribeTable`, `UpdateItem` и `GetItem` представлены как отдельные дочерние узлы спанов с общим родителем `outbound-aws-dotnet in eu-central-1` (Lambda-функция, выполняющая операции DynamoDB):

![Спаны DynamoDB для AWS Lambda .NET](https://dt-cdn.net/images/dynamodb-dotnet-1913-478c4bb6cb.png)

### Трассировка исходящих сообщений SQS/SNS

Для трассировки исходящих сообщений SQS/SNS [настройте инструментацию AWS SDK](#setup-aws-services-calls). Дополнительный код не требуется.

### Трассировка входящих сообщений SQS/SNS

Для трассировки входящих сообщений SQS/SNS:

1. [Настройте инструментацию AWS SDK](#setup-aws-services-calls).
2. Оберните обработчик функции в один из методов трассировки класса `AWSLambdaWrapper`:

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

## Особенности инструментации HttpClient

Поскольку в AWS Lambda среда выполнения функции может быть приостановлена в любой момент после выполнения обработчика функции, экспорт спанов может быть прерван или задержан (например, в некоторых случаях спан может вообще не быть экспортирован), и исходящие HTTP-запросы обычно появляются только при следующем вызове функции.

Однако activity исходящих HTTP-запросов, связанные с [AWS Runtime API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html#runtimes-api-next), могут быть захвачены [инструментацией HttpClient OpenTelemetry](https://github.com/open-telemetry/opentelemetry-dotnet/tree/main/src/OpenTelemetry.Instrumentation.Http) в текущем вызове функции, даже если это неожиданно. Чтобы избежать неожиданных исходящих HTTP-запросов в текущем вызове функции, мы рекомендуем настроить следующий фильтр при инициализации инструментации HttpClient.

```
var tracerProvider = Sdk.CreateTracerProviderBuilder()


// Initialization code similar to previous examples...


.AddHttpClientInstrumentation(op =>


{


op.FilterHttpRequestMessage = req => Activity.Current?.Parent?.IsAllDataRequested ?? false;


})


.Build();
```

## Поддержка .NET Lambda-функций с образами контейнеров

Начиная с .NET 6, Lambda-функции могут [собираться и развёртываться как образы контейнеров](https://dt-url.net/yz038r7). Инициализация и трассировка для управляемой среды выполнения .NET применяются к функциям с образами контейнеров без каких-либо изменений.
