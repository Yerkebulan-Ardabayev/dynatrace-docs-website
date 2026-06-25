---
title: Трассировка Lambda-функций .NET
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration
scraped: 2026-05-12T12:01:28.910041
---

# Трассировка Lambda-функций .NET

# Трассировка Lambda-функций .NET

* Практическое руководство
* Чтение: 9 мин
* Обновлено 24 августа 2023 г.

Dynatrace использует [OpenTelemetry](https://dt-url.net/y903u4j) для мониторинга вызовов AWS Lambda.

## Предварительные условия

Убедитесь, что вы используете [поддерживаемую среду выполнения AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration#support-lifecycle "Возможности и варианты интеграции AWS Lambda") и что выполнены шаги **первоначальной настройки**, описанные в [Мониторинг AWS Lambda с OpenTelemetry](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/aws-lambda-otel-setup "Предварительные условия для мониторинга AWS Lambda с OpenTelemetry"), прежде чем использовать перечисленные ниже пакеты.

Следующие пакеты NuGet можно использовать для покрытия различных аспектов трассировки AWS Lambda:

* Рекомендуется OpenTelemetry.Instrumentation.AWSLambda версии 1.2.0-beta.1+âсодержит методы для трассировки входящих вызовов AWS Lambda, например вызовов, инициированных сообщениями AWS SQS/SNS.
* Рекомендуется OpenTelemetry.Instrumentation.AWS версии 1.1.0-beta.1+âтрассирует исходящие вызовы AWS SDK к другим Lambda-вызовам и обращения к сервисам AWS, таким как DynamoDB, SQS и SNS.
* Обязательно `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`âобеспечивает связывание через исходящие вызовы AWS Lambda Invoke SDK от одной Lambda к другой. Это единственный способ связать такие запросы. Однако если такое связывание вам не нужно или вы не используете клиент AWS Lambda SDK для вызова или приёма других Lambda-вызовов, можно заменить этот пакет на `Dynatrace.OpenTelemetry`.

## Установка

Любой из перечисленных выше пакетов можно установить через CLI. Например, `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` устанавливается следующей командой:

```
dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AwsLambda
```

Некоторые пакеты могут требовать явного указания версии или использования флага командной строки `--prerelease`, например
`dotnet add package --prerelease OpenTelemetry.Instrumentation.AWSLambda`.

## Совместимость с версиями `OpenTelemetry` и `System.Diagnostics.DiagnosticSource`

Периодически нам нужно повышать минимальную версию пакета NuGet `OpenTelemetry`,
от которой зависят наши компоненты, и, как следствие, минимальную версию библиотеки `System.Diagnostics.DiagnosticSource`.
В этой таблице приведена совместимость между версиями `Dynatrace.OpenTelemetry`, `OpenTelemetry` и `System.Diagnostics.DiagnosticSource`.

| Версия `Dynatrace.OpenTelemetry` | Минимальная версия `OpenTelemetry` | Минимальная версия `System.Diagnostics.DiagnosticSource` |
| --- | --- | --- |
| 1.273 и ранее | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

Обычно беспокоиться об этих зависимостях не нужно, так как они уже определены за вас в нашем пакете NuGet. Это
означает, что при обновлении `Dynatrace.OpenTelemetry` NuGet может неявно поднять вашу версию `OpenTelemetry` или
`System.Diagnostics.DiagnosticSource`, если в данный момент у вас стоит более ранняя.

## Инициализация

Код инициализации для трассировки AWS Lambda в файле `Function.cs` может выглядеть так (где `Function` обозначает настроенный класс-обработчик Lambda):

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

* Установка опции `DisableAwsXRayContextExtraction` в `true` необходима, чтобы пропустить извлечение родительского контекста Amazon X-Ray, который может конфликтовать с propagation Dynatrace.
* Если опция `SuppressDownstreamInstrumentation` установлена в `true`, дочерние HTTP-узлы не будут отображаться под вызовами AWS SDK.

## Трассировка входящих вызовов AWS Lambda

### Пример 1: Трассировка AWS Lambda, вызываемой через AWS SDK

В дополнение к части инициализации, приведённой [выше](#initialization), метод-обработчик Lambda, вызываемой через AWS SDK, может выглядеть так:

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

* Родительский контекст явно извлекается с использованием класса `AwsLambdaHelpers` из пакета `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`.
* Activity, трассирующая входящий запрос и обработчик, создаётся методом `TraceAsync`.
* `TraceAsync` следует использовать, когда вы трассируете асинхронную функцию или функцию, возвращающую Task. Так Activity завершится только по завершении Task.

### Пример 2: Трассировка AWS Lambda, вызываемой через Amazon API Gateway (входящий HTTP-запрос)

В дополнение к части инициализации, приведённой выше, обработчик Lambda, вызываемой через Amazon API Gateway, может выглядеть так:

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
* Activity, трассирующая входящий запрос и обработчик, создаётся методом `Trace`.
* В общем случае методы `Trace`/`TraceAsync` поддерживают любые триггеры, но расширенная поддержка доступна для типов триггеров `APIGatewayProxyRequest` и `APIGatewayHttpApiV2ProxyRequest`. Подробнее о типах запросов и ответов см. [документацию на GitHub](https://dt-url.net/wm034ja).
* `Trace` следует использовать только когда функция возвращает значение, отличное от `Task`. Для асинхронного обработчика используйте `TraceAsync`.

### Пример 3: Трассировка без пакета `AwsLambda`

Если вы предпочитаете не использовать пакет `OpenTelemetry.Instrumentation.AWSLambda`, можно создать Activity для Lambda вручную. Учтите, что это требует значительной работы, так как Dynatrace требует определённых тегов Activity (атрибутов span) для распознавания сервиса (согласно OpenTelemetry FaaS [trace conventions](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/trace/semantic_conventions/faas.md)
и [resource conventions](https://github.com/open-telemetry/opentelemetry-specification/blob/v1.12.0/specification/resource/semantic_conventions/faas.md)). Также придётся вручную извлекать родительский контекст.

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

Можно использовать open-source пакеты NuGet с инструментацией, чтобы трассировать вызовы Amazon DynamoDB с использованием клиента вроде `AmazonDynamoDBClient` или вызовы SQS и SNS с использованием клиентов вроде `AmazonSQSClient` или `AmazonSimpleNotificationServiceClient`.

Чтобы настроить трассировку вызовов AWS SDK,

1. Убедитесь, что в ваш проект добавлены следующие пакеты:

   * `OpenTelemetry.Instrumentation.AWSLambda`
   * `OpenTelemetry.Instrumentation.AWS`

   Подробнее о пакетах см. [Предварительные условия](#prerequisites).
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

     Управляет тем, должен ли быть установлен родительский Activity при получении потенциально пакетного события, где доступно несколько родителей (например, SQS). При установке в `true` родитель устанавливается с использованием одного из полученных сообщений. Иначе родитель не устанавливается. В обоих случаях создаются ссылки (links).
   * `DisableAwsXRayContextExtraction`  
     Мы рекомендуем установить его в `true`, чтобы пропустить извлечение родительского контекста Amazon X-Ray и избежать конфликтов с propagation Dynatrace.

### Трассировка операций Amazon DynamoDB

Чтобы трассировать вызовы Amazon DynamoDB, [настройте инструментацию AWS SDK](#setup-aws-services-calls), убедитесь, что у вас как минимум версия 1.327.0 пакета `Dynatrace.OpenTelemetry.Instrumentation.AwsLambda`, и добавьте вызов `.AddDynatraceAwsSdkInjection()` в ваш [код инициализации](#initialization).
`Dynatrace.OpenTelemetry.Instrumentation.AwsLambda` и добавьте вызов `.AddDynatraceAwsSdkInjection()` в код инициализации.

В следующем примере операции DynamoDB `DescribeTable`, `UpdateItem` и `GetItem` представлены как отдельные дочерние span с общим родителем `outbound-aws-dotnet in eu-central-1` (Lambda-функция, выполняющая операции DynamoDB):

![span-узлы AWS Lambda .NET DynamoDB](https://dt-cdn.net/images/dynamodb-dotnet-1913-478c4bb6cb.png)

span-узлы AWS Lambda .NET DynamoDB

### Трассировка исходящих сообщений SQS/SNS

Чтобы трассировать исходящие сообщения SQS/SNS, [настройте инструментацию AWS SDK](#setup-aws-services-calls). Дополнительный код не требуется.

### Трассировка входящих сообщений SQS/SNS

Чтобы трассировать входящие сообщения SQS/SNS,

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

## Особые соображения по инструментации HttpClient

Поскольку с AWS Lambda среда исполнения функции может быть приостановлена в любой момент после выполнения обработчика, экспорт span может быть прерван или задержан (например, в некоторых случаях span может не быть экспортирован вообще), и исходящие HTTP-запросы обычно появляются только на следующем вызове функции.

Однако исходящие HTTP-запросы Activity, связанные с [AWS Runtime API](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-api.html#runtimes-api-next), могут быть захвачены [инструментацией OpenTelemetry HttpClient](https://github.com/open-telemetry/opentelemetry-dotnet/tree/main/src/OpenTelemetry.Instrumentation.Http) в текущем вызове функции, даже если это не ожидается. Чтобы избежать неожиданных исходящих HTTP-запросов в текущем вызове функции, рекомендуем настроить следующий фильтр при инициализации инструментации HttpClient.

```
var tracerProvider = Sdk.CreateTracerProviderBuilder()



// Initialization code similar to previous examples...



.AddHttpClientInstrumentation(op =>



{



op.FilterHttpRequestMessage = req => Activity.Current?.Parent?.IsAllDataRequested ?? false;



})



.Build();
```

## Поддержка Lambda-функций .NET с образами контейнеров

Начиная с .NET 6, Lambda-функции можно [собирать и развёртывать как образы контейнеров](https://dt-url.net/yz038r7). Инициализация и трассировка для [управляемой среды выполнения .NET](/managed/ingest-from/technology-support/application-software/dotnet "Узнайте обо всех аспектах поддержки Dynatrace для мониторинга приложений на .NET.") применяется к функциям из образов контейнеров без изменений.