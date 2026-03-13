---
title: Трассировка Azure Functions, написанных на .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet
scraped: 2026-03-06T21:38:21.488936
---

# Трассировка Azure Functions, написанных на .NET

# Трассировка Azure Functions, написанных на .NET

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 10 мин
* Обновлено 31 июля 2024 г.

## Предварительные требования

Убедитесь, что вы выполнили **начальную настройку**, описанную в [Настройка мониторинга OpenTelemetry для Azure Functions на плане потребления](opentelemetry-on-azure-functions.md "Мониторинг Azure Functions на плане потребления с помощью OpenTelemetry и Dynatrace."), прежде чем использовать пакеты, описанные ниже.

.NET версии 8 или более ранней

## Установка

1. Добавьте следующие зависимости в свой проект.

   * Обязательный `Dynatrace.OpenTelemetry` — обеспечивает интеграцию компонентов, специфичных для Dynatrace (для экспорта активностей и распространения контекста), в OpenTelemetry .NET.
   * Необязательный [`OpenTelemetry.Extensions.Hosting`](https://dt-url.net/w603yxv) — использует `TracerProvider` с внедрением зависимостей. Хотя последний релиз поддерживается для worker-функций, in-process функции требуют OpenTelemetry.Extensions.Hosting версии 1.0.0-rc9.5 или более ранней. Подробнее см. [Совместимость со средой выполнения `dotnet` (in-process)](#compatibility-with-dotnet-in-process-runtime) ниже.

   Примеры команд для добавления зависимостей

   ```
   dotnet add package Dynatrace.OpenTelemetry



   dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Extensions.Hosting
   ```
2. Дополнительно, в зависимости от используемой среды выполнения, мы рекомендуем использовать следующие вспомогательные пакеты для Azure Functions:

   * Рекомендуемый Для in-process (библиотечных) функций (среда выполнения `dotnet`)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions`
     + `OpenTelemetry.Instrumentation.AspNetCore`

     Чтобы добавить пакеты, выполните команду ниже.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions



     dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Instrumentation.AspNetCore
     ```
   * Рекомендуемый Для изолированных (worker) функций (среда выполнения `dotnet-isolated`)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker`

     Чтобы добавить пакет, выполните команду ниже.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker
     ```
   * Необязательный В качестве альтернативы в обеих средах выполнения можно использовать пакет Dynatrace `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` со следующими функциями:

     + [`AzureFunctionsCoreInstrumentation.Trace`](#manual-trace-instrumentation)
     + [`AzureFunctionsCoreInstrumentation.TraceAsync`](#manual-trace-instrumentation)

## Совместимость с версиями OpenTelemetry и `System.Diagnostics.DiagnosticSource`

Периодически нам необходимо обновлять минимальную версию NuGet-пакета `OpenTelemetry`, от которого зависят наши компоненты, и, соответственно, минимальную версию библиотеки `System.Diagnostics.DiagnosticSource`.
В этой таблице перечислена совместимость между версиями `Dynatrace.OpenTelemetry`, `OpenTelemetry` и `System.Diagnostics.DiagnosticSource`.

| Версия `Dynatrace.OpenTelemetry` | Минимальная версия `OpenTelemetry` | Минимальная версия `System.Diagnostics.DiagnosticSource` |
| --- | --- | --- |
| 1.273 и более ранние | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

Обычно вам не нужно беспокоиться об этих зависимостях, так как они определены в нашем NuGet-пакете. Это значит, что при обновлении `Dynatrace.OpenTelemetry` NuGet может неявно обновить вашу версию `OpenTelemetry` или `System.Diagnostics.DiagnosticSource`, если вы используете более раннюю версию.

## Совместимость со средой выполнения `dotnet` (in-process)

Для среды выполнения `dotnet` (in-process) только определённые версии OpenTelemetry совместимы с определёнными версиями среды выполнения Azure:

* Среда выполнения Azure Functions `dotnet` v3 несовместима с OpenTelemetry.
* Среда выполнения Azure Functions `dotnet` v4 совместима с OpenTelemetry 1.3.x (`System.Diagnostics.DiagnosticSource` 6).

При использовании среды выполнения `dotnet` (in-process) функции загружаются в тот же CLR, что и среда выполнения. Для корректной работы инструментирования необходимо, чтобы одна и та же сборка `System.Diagnostics.DiagnosticSource` использовалась как в среде выполнения, так и в зависимостях OpenTelemetry функции. Симптомы несовместимых комбинаций могут включать ошибку сборки функции, ошибку загрузки во время выполнения или неполные трассировки.

## Пример с использованием среды выполнения dotnet (in-process)

Ваш файл `Startup.cs` может выглядеть следующим образом:

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

Инструментированная in-process функция может выглядеть следующим образом:

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

Дополнительно необходимо изменить `host.json`, чтобы разрешить логирование для `Dynatrace.OpenTelemetry`.
Обратите внимание, что это не включает логирование, если оно не [настроено явно](opentelemetry-on-azure-functions.md "Мониторинг Azure Functions на плане потребления с помощью OpenTelemetry и Dynatrace."). См. [InitializeLogging](#initializelogging).

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

## Пример с использованием среды выполнения dotnet-isolated

Следующие примеры используют [встроенную HTTP-модель](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model) Azure Functions и **не** применимы к функциям, использующим [интеграцию ASP.NET Core](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) изолированных Azure Functions. См. раздел об [`интеграции ASP.NET Core`](#asp-net-core-integration) ниже.

Ваш файл `Program.cs` может выглядеть следующим образом:

Версии OpenTelemetry до 1.4

OpenTelemetry версии 1.4+

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

Дополнительный код для инструментирования функций не требуется; всё обрабатывается промежуточным ПО (middleware).

## Интеграция ASP.NET Core (изолированная среда выполнения)

Если вы создаёте новый проект для Azure Function .NET8 или более поздней версии — например, используя шаблон Visual Studio — то по умолчанию будет добавлена [интеграция ASP.NET Core](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) в Azure Function.

Для включения трассировки функций необходимо использовать только метод `ConfigureFunctionsWebApplication` вместо `ConfigureFunctionsWorkerDefaults` в коде инициализации, описанном в разделе [`интеграция ASP.NET Core`](#asp-net-core-integration). Код инициализации может выглядеть следующим образом:

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

## Технические подробности

### `InitializeLogging`

* Вызов `InitializeLogging` обязателен, даже если вы не планируете включать логирование, и фактические сообщения логов не будут записываться даже после вызова этого метода, если не выполнена [настройка](opentelemetry-on-azure-functions.md "Мониторинг Azure Functions на плане потребления с помощью OpenTelemetry и Dynatrace.").
* Если вы используете [среду выполнения `dotnet-isolated`](https://dt-url.net/2i23yrm) (out-of-process, worker-функции), вам необходимо вызвать `InitializeLogging` в методе `Main` перед вызовом `AddDynatrace`. Вы можете передать `null` в качестве `loggerFactory`, чтобы при включении логирование могло использовать `Console.Out`/`Console.Error`. Это автоматически перенаправляется в AppInsights для среды выполнения `dotnet-isolated`.
* При наличии особых требований вы также можете передать любой пользовательский `LoggingFactory`.
* Для [среды выполнения `dotnet`](https://dt-url.net/2r43yf7) (in-process, class-library) отправка логов в AppInsights требует использования `ILogger` или `ILoggerFactory`, внедрённых в функцию через механизм внедрения зависимостей. Поэтому не следует использовать `null` в качестве аргумента для параметра `loggerFactory`, а нужно вызвать `InitializeLogging` при первом вызове любой функции в вашем Function App. Чтобы получить `ILoggerFactory`, просто добавьте параметр этого типа.
* Если вы используете `ILoggerFactory`, предоставленный Azure Functions, вам также необходимо изменить `host.json`, чтобы включить логирование там. Мы рекомендуем всегда использовать уровень логирования `debug` в `host.json`, поскольку фактические сообщения логов, передаваемые в ILogger, настраиваются отдельно в конфигурации Dynatrace.

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

* `AddDynatrace` — это метод расширения для `TracerProvider` из OpenTelemetry. Он требует `using Dynatrace.OpenTelemetry`. В настоящее время у этой функции нет дополнительных параметров, так как конфигурация считывается из переменных окружения и файла `dtconfig.json`. Подробнее см. [Настройка мониторинга OpenTelemetry для Azure Functions на плане потребления](opentelemetry-on-azure-functions.md "Мониторинг Azure Functions на плане потребления с помощью OpenTelemetry и Dynatrace.").
* `AddDynatrace` в основном добавляет `ActivityProcessor` к `TracerProvider`, который будет отправлять все активности в Dynatrace. Это расширение:

  + Устанавливает ресурсы, необходимые для Dynatrace. Из-за [проблемы в OpenTelemetry .NET SDK](https://github.com/open-telemetry/opentelemetry-dotnet/issues/2909) это переопределит любые существующие ресурсы. Если вам нужны пользовательские ресурсы, вы должны вызвать `SetResourceBuilder` для `TracerProvider` *после* `AddDynatrace`. Имейте в виду, что это переопределит ресурсы, настроенные `AddDynatrace`, и вам нужно будет добавить их заново в рамках того же вызова `SetResourceBuilder`. Это можно сделать, вызвав метод расширения `AddTelemetrySdk` из OpenTelemetry SDK для `ResourceBuilder`.
  + Заменяет глобальный `Propagators.DefaultTextMapPropagator` на пользовательский, основанный на стандартном формате W3C, но с дополнительной обработкой `tracestate` и дополнительных HTTP-заголовков, специфичных для Dynatrace. Пропагатор baggage также включён, как это принято по умолчанию в OpenTelemetry .NET. В настоящее время нет возможности отключить его. Использование другого пропагатора не поддерживается и приведёт к отсутствию связей в распределённых трассировках.

Следующий минимальный фрагмент кода может быть использован для инициализации `TracerProvider` с `AddDynatrace`:

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

Это низкоуровневая функция инструментирования, предоставляемая в пакете `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core`. Обычно вам не следует использовать их напрямую, а лучше воспользоваться вспомогательными средствами для конкретной среды выполнения, как в [примерах выше](#helper-usage-examples).

Эта функция создаёт и запускает `System.Diagnostics.Activity`. Она выполняет функцию-обработчик, переданную в качестве аргумента, затем останавливает `Activity` и записывает все исключения. Пример использования может выглядеть следующим образом:

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

Родительский `ActivityContext` должен быть извлечён из HTTP-заголовков с помощью `Propagators.DefaultTextMapPropagator`, который инициализирует `AddDynatrace`. Если вы не передаёте родительский контекст, будет создан корневой спан трассировки (`Activity.Current` не будет использоваться).

Ниже показано, как родительский контекст можно вручную извлечь для in-process функций при использовании `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync` без инструментирования ASP.NET Core:

```
private static ActivityContext ExtractParentContext(HttpRequest request)



{



var context = Propagators.DefaultTextMapPropagator.Extract(default, request, HeaderValuesGetter);



return context.ActivityContext;



}



private static IEnumerable<string> HeaderValuesGetter(HttpRequest request, string name) =>



request.Headers.TryGetValue(name, out var values) ? values : (IEnumerable<string>)null;
```

Для worker-функций код может быть более сложным, так как помимо HTTP-заголовков вы можете (но не обязаны) использовать W3C TraceContext, предоставленный в `FunctionContext`:

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

## Инструментирование вызовов `HttpClient` (исходящие HTTP-запросы)

Очень часто возникает необходимость трассировки исходящих HTTP-запросов. Это можно реализовать с помощью [NuGet-пакета `OpenTelemetry.Instrumentation.Http`](https://www.nuget.org/packages/OpenTelemetry.Instrumentation.Http).

Инструментирование необходимо добавить в настройку `TracerProvider`, вызвав `AddHttpClientInstrumentation`, например, в `Program.cs`:

Версии OpenTelemetry до 1.4

OpenTelemetry версии 1.4+

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

Настоятельно рекомендуется использовать фильтр запросов, как в примере выше, так как в противном случае, в зависимости от конфигурации вашего Function App, вы можете наблюдать большое количество периодических запросов к `https://rt.services.visualstudio.com/QuickPulseService.svc/ping` или аналогичным URL.

В качестве альтернативы вы можете [динамически отключить телеметрию](https://dt-url.net/95038ca).

Мы рекомендуем использовать вспомогательную функцию `AzureFunctionsCoreInstrumentation.FilterExternalTelemetry`, которая доступна в пакете `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` начиная с версии 1.267. В более ранних версиях можно использовать следующий фильтр:

```
op.FilterHttpRequestMessage = req => Activity.Current?.Parent != null;
```

Из-за [проблемы в среде выполнения Azure Functions](https://github.com/Azure/azure-functions-host/issues/7278) инструментирование HTTP не будет работать в Azure Functions in-process версии 3.x.

Основная проблема также может затрагивать другие инструментирования. Поэтому мы не рекомендуем использовать in-process функции версии 3.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](../../../../microsoft-azure-services.md "Настройка и конфигурация мониторинга для Microsoft Azure.")