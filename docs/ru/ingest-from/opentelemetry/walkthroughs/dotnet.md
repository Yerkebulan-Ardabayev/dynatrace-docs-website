---
title: Инструментирование приложения .NET с помощью OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/dotnet
scraped: 2026-03-06T21:26:10.680904
---

Это руководство показывает, как добавить наблюдаемость в ваше приложение .NET с использованием библиотек и инструментов OpenTelemetry .NET.

| Функция | Поддержка |
| --- | --- |
| Автоматическое инструментирование | Да |
| Трассировки | Да |
| Метрики | Да |
| Логи | Да |

## Предварительные требования

* Dynatrace версии 1.254+
* Для трассировки необходимо включить W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Шаг 1. Получите данные доступа Dynatrace

### Определите базовый URL API

Подробности о том, как сформировать базовый URL OTLP-эндпоинта, см. в разделе [Эндпоинты Dynatrace OTLP API](../otlp-api.md#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получите токен доступа API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Эндпоинты Dynatrace OTLP API](../otlp-api.md#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") содержат дополнительную информацию о формате и необходимых правах доступа.

## Шаг 2. Выберите способ инструментирования вашего приложения

Для .NET OpenTelemetry поддерживает автоматическое и ручное инструментирование (или их комбинацию).

Какое инструментирование выбрать?

Рекомендуется начать с автоматического инструментирования и добавить ручное инструментирование, если автоматический подход не работает или не предоставляет достаточно информации.

## Шаг 3 (необязательно). Автоматическое инструментирование приложения

Автоматическое инструментирование .NET может быть настроено как во время разработки, так и после развёртывания.

Обогащение с помощью OneAgent

В настоящее время невозможно обогатить автоматически инструментированные сервисы информацией, относящейся к хосту. Для этого необходимо переключиться на ручное инструментирование.

Во время разработки

После развёртывания

1. Установите [`OpenTelemetry.Extensions.Hosting`](https://www.nuget.org/packages/OpenTelemetry.Extensions.Hosting).

   ```
   dotnet add package OpenTelemetry.Extensions.Hosting
   ```
2. Установите соответствующую библиотеку инструментирования для вашего фреймворка .NET (полный список доступен [здесь](https://www.nuget.org/packages?q=OpenTelemetry.Instrumentation)).

   ```
   dotnet add package OpenTelemetry.Instrumentation.[FRAMEWORK_NAME]
   ```

1. Скачайте [последний автоматический установщик](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation/releases/latest) для целевой операционной системы.
2. [Запустите (на Unix)](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#shell-scripts) или [импортируйте (на Windows)](https://github.com/open-telemetry/opentelemetry-dotnet-instrumentation#powershell-module-windows) автоматический установщик для установки и настройки всех необходимых библиотек автоматического инструментирования.
3. Запустите ваше приложение.

В дополнение к настройке инструментирования выше, вам также необходимо настроить соответствующие параметры экспорта через переменные окружения. Это включает [URL эндпоинта](../otlp-api.md#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."), [токен аутентификации](../otlp-api.md#authentication-export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") и [предпочтение темпоральности для метрик](../otlp-api/ingest-otlp-metrics/about-metrics-ingest.md#aggregation-temporality "Узнайте, как Dynatrace принимает метрики OpenTelemetry и какие ограничения применяются.").

```
OTEL_EXPORTER_OTLP_ENDPOINT=[URL]


OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"


OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
```

## Шаг 4 (необязательно). Ручное инструментирование приложения

### Настройка

Шаги настройки немного различаются в зависимости от того, инструментируете ли вы обычное приложение .NET или приложение ASP.NET.

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
2. Добавьте следующие директивы `using` в класс запуска, который загружает ваше приложение.

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
3. Добавьте эти поля в ваш класс запуска, где первые два содержат [данные доступа](#dynatrace-docs--otlp-export), если вы используете экспорт OTLP.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here


   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here


   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here


   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);


   private static ILoggerFactory loggerFactoryOT;
   ```

   Внедрение значений

   Вместо жёсткого кодирования URL и токена вы также можете рассмотреть чтение их из хранилища, специфичного для вашего фреймворка приложения (например, переменные окружения или секреты фреймворка).
4. Добавьте метод `initOpenTelemetry` в ваш класс запуска и вызовите его как можно раньше при запуске вашего приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры трассировки и метрик по умолчанию.

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

   Операции чтения файлов, а именно парсинг файлов `dt_metadata` в примере кода, выполняют попытку чтения файлов данных OneAgent для обогащения OTLP-запроса и обеспечения доступности всей необходимой топологической информации в Dynatrace.

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
2. Добавьте следующие директивы `using` в класс запуска, который загружает ваше приложение.

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
3. Добавьте эти поля в ваш класс запуска, где первые два содержат [данные доступа](#dynatrace-docs--otlp-export), если вы используете экспорт OTLP.

   ```
   private static string DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here


   private static string DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here


   private const string activitySource = "Dynatrace.DotNetApp.Sample"; // TODO: Provide a descriptive name for your application here


   public static readonly ActivitySource MyActivitySource = new ActivitySource(activitySource);


   private static ILoggerFactory loggerFactoryOT;
   ```

   Внедрение значений

   Вместо жёсткого кодирования URL и токена вы также можете рассмотреть чтение их из хранилища, специфичного для вашего фреймворка приложения (например, переменные окружения или секреты фреймворка).
4. Добавьте метод `initOpenTelemetry` в ваш класс запуска и вызовите его как можно раньше при запуске вашего приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры трассировки и метрик по умолчанию.

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

   Операции чтения файлов, а именно парсинг файлов `dt_metadata` в примере кода, выполняют попытку чтения файлов данных OneAgent для обогащения OTLP-запроса и обеспечения доступности всей необходимой топологической информации в Dynatrace.

### Добавление трассировки

Используя `MyActivitySource` из [шага настройки](#setup), мы теперь можем запускать новые действия (трассировки):

```
using var activity = Startup.MyActivitySource.StartActivity("Call to /myendpoint", ActivityKind.Consumer, parentContext.ActivityContext);


activity?.SetTag("http.method", "GET");


activity?.SetTag("net.protocol.version", "1.1");
```

В приведённом коде мы:

* Создаём новое действие (спан) и называем его "Call to /myendpoint"
* Добавляем два тега (атрибута) в соответствии с [соглашением о семантическом именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информация о методе HTTP и версии

Действие будет автоматически установлено как текущий и активный спан до тех пор, пока поток выполнения не покинет текущую область метода. Последующие действия автоматически станут дочерними спанами.

### Сбор метрик

1. Для создания новых инструментов метрик нам сначала нужен объект измерителя (meter).

   ```
   private static readonly Meter meter = new Meter("my-meter", "1.0.0");  //TODO Replace with the name of your meter
   ```
2. С помощью `meter` мы теперь можем создавать отдельные инструменты, например счётчик.

   ```
   private static readonly Counter<long> counter = meter.CreateCounter<long>("request_counter");
   ```
3. Теперь мы можем вызывать метод `Add()` объекта `counter` для записи новых значений нашего счётчика и сохранения дополнительных атрибутов (например, `action.type`).

   ```
   counter.Add(1, new("ip", "an ip address here"), new("some other key", "some other value"));
   ```

### Подключение логов

С помощью переменной `loggerFactoryOT`, которую мы инициализировали в разделе [Настройка](#setup), мы теперь можем создавать отдельные экземпляры логгеров, которые будут передавать записанную информацию непосредственно в настроенный эндпоинт OpenTelemetry в Dynatrace.

```
var logger = loggerFactoryOT.CreateLogger<Startup>();


services.AddSingleton<ILoggerFactory>(loggerFactoryOT);


services.AddSingleton(logger);


logger.LogInformation(eventId: 123, "Log line");
```

### Обеспечение распространения контекста (необязательно)

[Распространение контекста](../../opentelemetry.md#context-propagation "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассировки, метрики и логи) в Dynatrace.") особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки покрываются автоматическим инструментированием, это будет автоматически обработано библиотеками инструментирования. В противном случае ваш код должен учитывать это.

#### Извлечение контекста при получении запроса

В следующем примере мы предполагаем, что получили сетевой вызов через `System.Web.HttpRequest`, и мы определяем экземпляр `CompositeTextMapPropagator` для извлечения информации о контексте из HTTP-заголовков. Затем мы передаём этот экземпляр в `Extract()`, который возвращает объект контекста, позволяющий нам продолжить предыдущую трассировку с нашими спанами.

```
private CompositeTextMapPropagator propagator = new CompositeTextMapPropagator(new TextMapPropagator[] {


new TraceContextPropagator(),


new BaggagePropagator(),


});


private static readonly Func<HttpRequest, string, IEnumerable<string>> valueGetter = (request, name) => request.Headers[name];


var parentContext = propagator.Extract(default, HttpContext.Request, valueGetter);


using var activity = MyActivitySource.StartActivity("my-span", ActivityKind.Consumer, parentContext.ActivityContext);
```

#### Внедрение контекста при отправке запросов

В следующем примере мы отправляем REST-запрос к другому сервису и предоставляем наш существующий контекст как часть HTTP-заголовков нашего запроса.

Для этого мы определяем экземпляр `TextMapPropagator`, который добавляет соответствующую информацию. После создания нашего REST-объекта мы передаём его вместе с контекстом и экземпляром setter в `Inject()`, который добавит необходимые заголовки в запрос.

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

## Шаг 5 (необязательно). Настройте захват данных для соответствия требованиям конфиденциальности

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, только значения атрибутов, указанные в списке разрешённых, сохраняются и отображаются в веб-интерфейсе Dynatrace. Это предотвращает случайное сохранение персональных данных, позволяя вам соответствовать требованиям конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра ваших пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. раздел [Редактирование атрибутов](../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 6. Проверьте приём данных в Dynatrace

После завершения инструментирования вашего приложения выполните несколько тестовых действий для создания и отправки демонстрационных трассировок, метрик и логов и убедитесь, что они были корректно приняты в Dynatrace.

Для этого для трассировок перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо этого **PurePaths**.

Для метрик и логов перейдите в **Metrics** или ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Связанные темы

* Обогащение принимаемых данных полями, специфичными для Dynatrace
