---
title: Трассировка Azure Functions на .NET
source: https://docs.dynatrace.com/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions-dotnet
scraped: 2026-05-12T12:07:48.195414
---

# Трассировка Azure Functions на .NET

# Трассировка Azure Functions на .NET

* Практическое руководство
* Чтение: 10 мин
* Обновлено 31 июля 2024 г.

## Предварительные требования

Перед использованием приведённых ниже пакетов убедитесь, что выполнили шаги **начальной настройки**, описанные в разделе [Настройка мониторинга OpenTelemetry для Azure Functions в плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.").

.NET версии 8 или более ранней

## Установка

1. Добавьте в проект следующие зависимости.

   * Обязательный `Dynatrace.OpenTelemetry`, обеспечивающий интеграцию компонентов Dynatrace (для экспорта activity и propagation) в OpenTelemetry .NET.
   * Необязательный [`OpenTelemetry.Extensions.Hosting`](https://dt-url.net/w603yxv): использует `TracerProvider` с внедрением зависимостей. Последний релиз поддерживается для worker functions, однако in-process functions требуют OpenTelemetry.Extensions.Hosting версии 1.0.0-rc9.5 или более ранней. Подробнее см. раздел [Совместимость с `dotnet` (in-process) runtime](#compatibility-with-dotnet-in-process-runtime) ниже.

   Примеры команд для добавления зависимостей

   ```
   dotnet add package Dynatrace.OpenTelemetry



   dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Extensions.Hosting
   ```
2. Кроме того, в зависимости от используемого runtime рекомендуется использовать следующие вспомогательные пакеты Azure Functions:

   * Рекомендуется для in-process (library) functions (`dotnet` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions`
     + `OpenTelemetry.Instrumentation.AspNetCore`

     Чтобы добавить пакеты, выполните команду ниже.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions



     dotnet add package --version 1.0.0-rc9.5 OpenTelemetry.Instrumentation.AspNetCore
     ```
   * Рекомендуется для isolated, то есть worker functions (`dotnet-isolated` runtime)

     + `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker`

     Чтобы добавить пакет, выполните команду ниже.

     ```
     dotnet add package Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Worker
     ```
   * Необязательно. В качестве альтернативы на обоих runtime можно использовать пакет Dynatrace `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` со следующими функциями:

     + [`AzureFunctionsCoreInstrumentation.Trace`](#manual-trace-instrumentation)
     + [`AzureFunctionsCoreInstrumentation.TraceAsync`](#manual-trace-instrumentation)

## Совместимость с версиями OpenTelemetry и `System.Diagnostics.DiagnosticSource`

Периодически требуется обновлять минимальную версию NuGet-пакета `OpenTelemetry`,
от которого зависят компоненты, и соответственно минимальную версию библиотеки `System.Diagnostics.DiagnosticSource`.
В таблице приведена совместимость версий `Dynatrace.OpenTelemetry`, `OpenTelemetry` и `System.Diagnostics.DiagnosticSource`.

| Версия `Dynatrace.OpenTelemetry` | Минимальная версия `OpenTelemetry` | Минимальная версия `System.Diagnostics.DiagnosticSource` |
| --- | --- | --- |
| 1.273 и ранее | 1.1.0 | 5.0.1 |
| 1.275+ | 1.3.1 | 6.0.0 |

Как правило, об этих зависимостях не нужно беспокоиться, так как они определены в NuGet-пакете. Это
означает, что при обновлении `Dynatrace.OpenTelemetry` NuGet может неявно обновить `OpenTelemetry` или
`System.Diagnostics.DiagnosticSource` до более новой версии, если текущая устарела.

## Совместимость с `dotnet` (in-process) runtime

Для `dotnet` (in-process) runtime только определённые версии OpenTelemetry совместимы с определёнными версиями Azure runtime:

* Azure Functions `dotnet` runtime v3 не совместим с OpenTelemetry.
* Azure Functions `dotnet` runtime v4 совместим с OpenTelemetry 1.3.x (`System.Diagnostics.DiagnosticSource` 6).

При использовании `dotnet` (in-process) runtime функции загружаются в тот же CLR, что и сам runtime. Для корректной работы инструментирования необходимо, чтобы в runtime и в зависимостях OpenTelemetry функции использовалась одна и та же сборка `System.Diagnostics.DiagnosticSource`. Признаки несовместимых комбинаций: сбой сборки функции, сбой загрузки во время выполнения или неполные трассировки.

## Пример с использованием dotnet (in-process) runtime

Файл `Startup.cs` может выглядеть следующим образом:

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

Пример инструментированной in-process function:

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

Кроме того, необходимо изменить `host.json`, чтобы разрешить ведение журнала для `Dynatrace.OpenTelemetry`.
Обратите внимание, что это не активирует ведение журнала, если оно не [настроено явно](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace."). См. [InitializeLogging](#initializelogging).

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

## Пример с использованием dotnet-isolated runtime

Приведённые примеры используют [встроенную HTTP-модель](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#built-in-http-model) Azure Functions и **не** применяются к функциям, использующим [ASP.NET core integration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) изолированных Azure Functions. См. раздел [`ASP.NET core integration`](#asp-net-core-integration) ниже.

Файл `Program.cs` может выглядеть следующим образом:

Версии OpenTelemetry ранее 1.4

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

Дополнительный код для инструментирования функций не требуется: всё обрабатывается middleware.

## ASP.NET core integration (isolated runtime)

При создании нового проекта для Azure Function .NET8 или более поздней версии, например с помощью шаблона Visual Studio, по умолчанию добавляется [ASP.NET core integration](https://learn.microsoft.com/en-us/azure/azure-functions/dotnet-isolated-process-guide#aspnet-core-integration) в Azure Function.

Чтобы включить трассировку функций, нужно использовать метод `ConfigureFunctionsWebApplication` вместо `ConfigureFunctionsWorkerDefaults` в коде инициализации, приведённом в [`ASP.NET core integration`](#asp-net-core-integration). Код инициализации может выглядеть следующим образом:

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

## Технические сведения

### `InitializeLogging`

* Вызов `InitializeLogging` обязателен, даже если вести журнал не планируется. Реальные сообщения журнала не будут логироваться после вызова этого метода, если только не [настроено](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.").
* При использовании [`dotnet-isolated` runtime](https://dt-url.net/2i23yrm) (out-of-process, worker functions) нужно вызвать `InitializeLogging` в методе `Main` перед вызовом `AddDynatrace`. Можно передать `null` в качестве `loggerFactory`, чтобы при включённом ведении журнала использовались `Console.Out`/`Console.Error`. Для `dotnet-isolated` runtime это автоматически перенаправляется в AppInsights.
* При наличии особых требований можно также передать произвольный `LoggingFactory`.
* Для [`dotnet` runtime](https://dt-url.net/2r43yf7) (in-process, class-library) отправка журналов в AppInsights требует использования `ILogger` или `ILoggerFactory`, внедрённых в функцию через dependency injection. Поэтому не следует передавать `null` в качестве аргумента параметра `loggerFactory`: нужно вызывать `InitializeLogging` при первом вызове любой функции в Function App. Чтобы получить `ILoggerFactory`, достаточно добавить параметр соответствующего типа.
* При использовании `ILoggerFactory`, предоставляемого Azure Functions, также необходимо изменить `host.json`, чтобы включить там ведение журнала. Рекомендуется всегда использовать уровень журнала `debug` в `host.json`, поскольку реальные сообщения, передаваемые ILogger, настраиваются отдельно в конфигурации Dynatrace.

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

* `AddDynatrace` является методом расширения `TracerProvider` OpenTelemetry. Для его использования необходим `using Dynatrace.OpenTelemetry`. На данный момент дополнительных параметров у этой функции нет: конфигурация считывается из переменных окружения и файла `dtconfig.json`. Подробнее см. [Настройка мониторинга OpenTelemetry для Azure Functions в плане Consumption](/managed/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/opentelemetry-on-azure-functions "Мониторинг плана Consumption для Azure Functions с помощью OpenTelemetry и Dynatrace.").
* `AddDynatrace` преимущественно добавляет `ActivityProcessor` в `TracerProvider`, который отправляет все activity в Dynatrace. Это расширение:

  + Устанавливает ресурсы, необходимые Dynatrace. Из-за [проблемы с OpenTelemetry .NET SDK](https://github.com/open-telemetry/opentelemetry-dotnet/issues/2909) это переопределяет существующие ресурсы. Если нужны пользовательские ресурсы, необходимо вызвать `SetResourceBuilder` на `TracerProvider` *после* `AddDynatrace`. Обратите внимание, что это переопределит ресурсы, настроенные `AddDynatrace`, и их нужно добавить заново в том же вызове `SetResourceBuilder`. Для этого вызовите метод расширения `AddTelemetrySdk` из OpenTelemetry SDK на `ResourceBuilder`.
  + Заменяет глобальный `Propagators.DefaultTextMapPropagator` на пользовательский, основанный на стандартном формате W3C, но выполняющий дополнительную обработку `tracestate` и специфичных для Dynatrace HTTP-заголовков. Также включается baggage propagator, что является стандартным для OpenTelemetry .NET. Отключить его в настоящее время невозможно. Использование другого propagator не поддерживается и приведёт к потере связей в распределённых трассировках.

Следующий минимальный фрагмент можно использовать для инициализации `TracerProvider` с помощью `AddDynatrace`:

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

Это низкоуровневая функция инструментирования из пакета `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core`. Как правило, использовать её не рекомендуется: вместо неё используйте вспомогательные средства, специфичные для runtime, как в [приведённых выше примерах](#helper-usage-examples).

Функция создаёт и запускает `System.Diagnostics.Activity`, выполняет переданный обработчик, затем останавливает `Activity` и фиксирует на ней любое исключение. Пример использования:

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

Родительский `ActivityContext` необходимо извлечь из HTTP-заголовков с помощью `Propagators.DefaultTextMapPropagator`, инициализируемого `AddDynatrace`. Если родительский контекст не передан, будет создан корневой спан трассировки (`Activity.Current` использоваться не будет).

Пример ручного извлечения родительского контекста для in-process functions при использовании `AzureFunctionsCoreInstrumentation.Trace`/`TraceAsync` без ASP.NET core instrumentation:

```
private static ActivityContext ExtractParentContext(HttpRequest request)



{



var context = Propagators.DefaultTextMapPropagator.Extract(default, request, HeaderValuesGetter);



return context.ActivityContext;



}



private static IEnumerable<string> HeaderValuesGetter(HttpRequest request, string name) =>



request.Headers.TryGetValue(name, out var values) ? values : (IEnumerable<string>)null;
```

Для worker functions код может усложниться, так как помимо HTTP-заголовков можно (но не обязательно) использовать
W3C TraceContext из `FunctionContext`:

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

Трассировка исходящих HTTP-запросов является частой задачей. Её можно решить с помощью [NuGet-пакета `OpenTelemetry.Instrumentation.Http`](https://www.nuget.org/packages/OpenTelemetry.Instrumentation.Http).

Инструментирование нужно добавить в настройку `TracerProvider`, вызвав `AddHttpClientInstrumentation`, например в `Program.cs`:

Версии OpenTelemetry ранее 1.4

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

Настоятельно рекомендуется использовать фильтр запросов, как в примере выше: в противном случае, в зависимости от конфигурации Function Apps, может наблюдаться большое количество периодических запросов на `https://rt.services.visualstudio.com/QuickPulseService.svc/ping` или аналогичные URL.

Кроме того, можно [динамически отключить телеметрию](https://dt-url.net/95038ca).

Рекомендуется использовать вспомогательную функцию `AzureFunctionsCoreInstrumentation.FilterExternalTelemetry`, доступную в пакете `Dynatrace.OpenTelemetry.Instrumentation.AzureFunctions.Core` начиная с версии 1.267. В более ранних версиях вместо неё можно использовать следующий фильтр:

```
op.FilterHttpRequestMessage = req => Activity.Current?.Parent != null;
```

Из-за [проблемы Azure Functions runtime](https://github.com/Azure/azure-functions-host/issues/7278) HTTP-инструментирование не работает в Azure Functions in-process версии 3.x.

Эта же проблема может затронуть другие инструментирования. Поэтому не рекомендуется использовать in-process functions версии 3.

## Связанные темы

* [Настройка Dynatrace в Microsoft Azure](/managed/ingest-from/microsoft-azure-services "Настройка и конфигурирование мониторинга для Microsoft Azure.")