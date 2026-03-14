---
title: Трассировка Azure Functions с OpenTelemetry .NET
source: https://www.dynatrace.com/docs/ingest-from/microsoft-azure-services/azure-integrations/azure-functions/func-dynamic-plans/otel-native-dotnet-azure
scraped: 2026-03-05T21:39:19.122956
---

# Трассировка Azure Functions с помощью OpenTelemetry .NET


* Latest Dynatrace
* How-to guide
* 4-min read
* Published Mar 09, 2022

Экспортёры OpenTelemetry Protocol (OTLP) для .NET в настоящее время поддерживают транспорты [gRPC и HTTP 1.1 с двоичными данными Protocol Buffers (Protobuf)](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#exporters). Поддерживаемые соответствующие значения протоколов: `grpc` и `http/protobuf`. [Параметры конфигурации](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options) можно задать как через переменные среды, так и непосредственно в коде.

## Предварительные требования

Действуют следующие предварительные требования и ограничения:

* Dynatrace версии 1.222+
* W3C Trace Context включён

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Инструментирование Azure Functions

Dynatrace использует приём трассировок OpenTelemetry для обеспечения сквозной видимости ваших Azure Functions.

Для инструментирования Azure Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Настройка экспорта**](otel-native-dotnet-azure.md#export "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Добавление зависимостей**](otel-native-dotnet-azure.md#dependencies "Learn how to use OpenTelemetry .NET to trace Azure Functions.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Инструментирование кода**](otel-native-dotnet-azure.md#instrument "Learn how to use OpenTelemetry .NET to trace Azure Functions.")

### Шаг 1. Настройка экспорта

Экспорт gRPC

Экспорт HTTP

Для приёма данных через **gRPC** посредством Dynatrace Trace API необходимо использовать [коллектор OpenTelemetry](https://dt-url.net/vf23sfn) между Dynatrace и экспортёром.

Если для настройки используются переменные среды, необходимо задать следующее значение:

* Для `OTEL_EXPORTER_OTLP_PROTOCOL`: `grpc`

#### Настройка коллектора OpenTelemetry

Для приёма данных через **gRPC** посредством Dynatrace Trace API необходимо использовать [коллектор OpenTelemetry](https://dt-url.net/vf23sfn) между Dynatrace и экспортёром.

Коллектор OpenTelemetry доступен в виде [Docker-образа](https://hub.docker.com/r/otel/opentelemetry-collector).
Чтобы использовать этот коллектор для экспорта данных трассировки в Dynatrace, необходимо настроить [конфигурацию](https://opentelemetry.io/docs/collector/configuration/) с использованием OTLP-экспортёра OpenTelemetry.

Пример файла конфигурации:

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

Дополнительные сведения о конфигурации см. в разделе [OpenTelemetry и Dynatrace](../../../../opentelemetry.md "Learn how to integrate and ingest OpenTelemetry data (traces, metrics, and logs) into Dynatrace.").

Для приёма данных через **HTTP** посредством Dynatrace Trace API необходимо [настроить экспортёр](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options). После этого экспортёр будет напрямую отправлять трассировки на настроенную конечную точку.

Если для настройки используются переменные среды, необходимо задать следующие значения:

* Для `OTEL_EXPORTER_OTLP_PROTOCOL`: `http/protobuf`
* Для `OTEL_EXPORTER_OTLP_ENDPOINT`: URL конечной точки экспорта

  + Если вы задаёте URL конечной точки через переменные среды, конечные точки экспорта для трассировок и метрик автоматически дополняются суффиксами `v1/traces` для трассировок и `v1/metrics` для метрик. Например, если конечная точка задана как `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp`, трассировки будут экспортироваться в `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp/v1/traces`.
  + Если вы задаёте конечную точку явно в коде, она используется как есть.

  Подробности см. в разделе [URL конечных точек для OTLP/HTTP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#endpoint-urls-for-otlphttp).
* Для `OTEL_EXPORTER_OTLP_HEADERS`: значение токена авторизации API в следующем формате: `Authorization=Api-Token <TOKEN>`.

### Шаг 2. Добавление зависимостей

Добавьте следующие зависимости через NuGet в ваш проект:

```
OpenTelemetry.Exporter.OpenTelemetryProtocol
```

OpenTelemetry также предоставляет другие [библиотеки автоматического инструментирования, доступные в виде NuGet-пакетов](https://www.nuget.org/packages?q=opentelemetry.instrumentation).

### Шаг 3. Инструментирование кода с помощью OpenTelemetry

Инструментирование с использованием экспорта gRPC

Инструментирование с использованием экспорта HTTP

Если вы не задаёте свойство `Protocol` класса `OtlpExporterOptions` через переменные среды или в коде, оно инициализируется значением [`OtlpExportProtocol.Grpc` по умолчанию](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry.Exporter.OpenTelemetryProtocol/OtlpExporterOptions.cs#L99).

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

Пример кода с использованием **HTTP-экспортёра** аналогичен примеру с **gRPC-экспортёром**; единственное отличие — в настройке `OtlpExporterOptions`:

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

Если конфигурация выполняется через переменные среды, код для добавления OTLP/HTTP-экспортёра ещё проще:

```
return Sdk.CreateTracerProviderBuilder()


// ...


// ... other initialization code (see the code snippet for the gRPC case)


// ...


.AddOtlpExporter()


.Build();
```