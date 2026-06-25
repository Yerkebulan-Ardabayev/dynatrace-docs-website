---
title: Инструментирование .NET-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/dotnet
scraped: 2026-05-12T12:04:17.920363
---

# Инструментирование .NET-приложения с OpenTelemetry

# Инструментирование .NET-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 7 мин
* Обновлено: 14 ноября 2023

В этом руководстве показано, как добавить наблюдаемость в ваше .NET-приложение с помощью библиотек и инструментов OpenTelemetry .NET.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Да |
| Трассировки | Да |
| Метрики | Да |
| Логи | Да |

## Предварительные требования

* Dynatrace версии 1.254+
* Для трассировки включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Выбор способа инструментирования приложения

Для .NET OpenTelemetry поддерживает автоматическое и ручное инструментирование (или их сочетание).

Какое инструментирование выбрать?

Хорошая идея, начать с автоматического инструментирования и добавить ручное, если автоматический подход не работает или не даёт достаточно информации.

## Шаг 3 (необязательно) Автоматическое инструментирование приложения (необязательно)

Автоматическое инструментирование .NET можно настроить либо во время разработки, либо позже, после развёртывания.

Обогащение через OneAgent

В настоящее время невозможно [обогатить](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.") автоматически инструментированные сервисы информацией, относящейся к хосту. Для этого потребуется перейти на ручное инструментирование.

Во время разработки

После развёртывания

1. Установите [`OpenTelemetry.Extensions.Hosting`](https://www.nuget.org/packages/OpenTelemetry.Extensions.Hosting).

   ```
   dotnet add package OpenTelemetry.Extensions.Hosting
   ```
2. Установите подходящую библиотеку инструментирования для вашего .NET framework (полный список доступен [здесь](https://www.nuget.org/packages?q=OpenTelemetry.Instrumentation)).

   ```
   dotnet add package OpenTelemetry.Instrumentation.[FRAMEWORK_NAME]
   ```

1. Скачайте [последний авто-установщик](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest) для целевой операционной системы.
2. [Запустите (в Unix)](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#shell-scripts) или [импортируйте (в Windows)](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#powershell-module-windows) авто-установщик, чтобы установить и настроить все необходимые библиотеки автоматического инструментирования.
3. Запустите приложение.

Помимо настройки инструментирования выше, также нужно настроить соответствующие параметры экспорта через переменные окружения. Это включает [URL эндпоинта](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), [токен аутентификации](/managed/ingest-from/opentelemetry/otlp-api#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и [предпочтение темпоральности для метрик](/managed/ingest-from/opentelemetry/otlp-api/ingest-otlp-metrics/about-metrics-ingest#aggregation-temporality "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.").

```
OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

## Шаг 4 (необязательно) Ручное инструментирование приложения (необязательно)

### Setup

Шаги настройки немного различаются в зависимости от того, инструментируете ли вы обычное .NET-приложение или ASP.NET-приложение.

.NET

ASP.NET

1. Установите следующие пакеты.

   ```
   dotnet add package Microsoft.Extensions.Logging



   dotnet add package OpenTelemetry.Extensions.Hosting



   dotnet add package OpenTelemetry



   dotnet add package OpenTelemetry.Api



   dotnet add package OpenTelemetry.Exporter.OpenTelemetryProtocol
   ```
2. Добавьте следующие выражения `using` в стартовый класс, который инициализирует ваше приложение.

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
3. Добавьте эти поля в стартовый класс, причём первые два содержат [данные доступа](#dynatrace-docs--otlp-export), если вы используете экспорт OTLP.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Внедрение значений

   Вместо жёсткого прописывания URL и токена в коде можно также рассмотреть их чтение из хранилища, специфичного для фреймворка вашего приложения (например, переменные окружения или секреты фреймворка).
4. Добавьте метод `initOpenTelemetry` в стартовый класс и вызовите его как можно раньше при запуске приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры tracer и meter по умолчанию.

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

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии внутри Dynatrace.

1. Установите следующие пакеты.

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
2. Добавьте следующие выражения `using` в стартовый класс, который инициализирует ваше приложение.

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
3. Добавьте эти поля в стартовый класс, причём первые два содержат [данные доступа](#dynatrace-docs--otlp-export), если вы используете экспорт OTLP.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here



   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here



   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);



   private static ILoggerFactory loggerFactoryOT;
   ```

   Внедрение значений

   Вместо жёсткого прописывания URL и токена в коде можно также рассмотреть их чтение из хранилища, специфичного для фреймворка вашего приложения (например, переменные окружения или секреты фреймворка).
4. Добавьте метод `initOpenTelemetry` в стартовый класс и вызовите его как можно раньше при запуске приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры tracer и meter по умолчанию.

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

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии внутри Dynatrace.

### Add tracing

Используя `MyActivitySource` из [шага настройки](#setup), теперь можно запускать новые activity (трассировки):

```
using var activity = Startup.MyActivitySource.StartActivity("Call to /myendpoint", ActivityKind.Consumer, parentContext.ActivityContext);



activity?.SetTag("http.method", "GET");



activity?.SetTag("net.protocol.version", "1.1");
```

В приведённом выше коде мы:

* Создаём новую activity (спан) и называем её "Call to /myendpoint"
* Добавляем два тега (атрибута), следуя [соглашению о семантическом именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информацию о методе и версии HTTP

Activity автоматически устанавливается как текущий и активный спан, пока поток выполнения не покинет область текущего метода. Последующие activity автоматически становятся дочерними спанами.

### Collect metrics

1. Чтобы создать экземпляры новых инструментов метрик, сначала нужен объект meter.

   ```
   private static readonly Meter meter = new Meter("my-meter", "1.0.0");  //TODO Replace with the name of your meter
   ```
2. С `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   private static readonly Counter<long> counter = meter.CreateCounter<long>("request_counter");
   ```
3. Теперь можно вызвать метод `Add()` объекта `counter`, чтобы записать новые значения нашим счётчиком и сохранить дополнительные атрибуты (например, `action.type`).

   ```
   counter.Add(1, new("ip", "an ip address here"), new("some other key", "some other value"));
   ```

### Connect logs

С помощью переменной `loggerFactoryOT`, которую мы инициализировали в разделе [Setup](#setup), теперь можно создавать отдельные экземпляры logger, которые будут передавать логируемую информацию напрямую на настроенный эндпоинт OpenTelemetry в Dynatrace.

```
var logger = loggerFactoryOT.CreateLogger<Startup>();



services.AddSingleton<ILoggerFactory>(loggerFactoryOT);



services.AddSingleton(logger);



logger.LogInformation(eventId: 123, "Log line");
```

### Ensure context propagation Optional

[Context propagation](/managed/ingest-from/opentelemetry#context-propagation "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

#### Extracting the context when receiving a request

В следующем примере мы предполагаем, что получили сетевой вызов через `System.Web.HttpRequest`, и определяем экземпляр `CompositeTextMapPropagator`, чтобы извлечь информацию о контексте из HTTP-заголовков. Затем мы передаём этот экземпляр в `Extract()`, возвращающий объект контекста, который позволяет нам продолжить предыдущую трассировку нашими спанами.

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

В следующем примере мы отправляем REST-запрос другому сервису и предоставляем наш существующий контекст как часть HTTP-заголовков нашего запроса.

Для этого мы определяем экземпляр `TextMapPropagator`, который добавляет соответствующую информацию. После того как мы создали экземпляр нашего REST-объекта, мы передаём его, вместе с контекстом и экземпляром setter, в `Inject()`, который добавит необходимые заголовки в запрос.

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

## Шаг 5 (необязательно) Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 6 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")