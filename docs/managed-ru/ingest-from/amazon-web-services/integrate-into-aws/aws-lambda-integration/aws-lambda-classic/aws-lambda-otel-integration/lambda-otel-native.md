---
title: Трассировка Lambda-функций AWS .NET Core с OpenTelemetry .NET
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native
scraped: 2026-05-12T11:27:43.486292
---

# Трассировка Lambda-функций AWS .NET Core с OpenTelemetry .NET

# Трассировка Lambda-функций AWS .NET Core с OpenTelemetry .NET

* Практическое руководство
* Чтение: 6 мин
* Обновлено 23 сентября 2022 г.

Доступна новая версия

Хотя вы можете использовать стандартные возможности OpenTelemetry для инструментации ваших Lambda-функций AWS на .NET, как описано в этом руководстве, рекомендуем следовать нашей улучшенной версии,  
[трассировка Lambda-функций AWS на .NET](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration "Трассировка Lambda-функций AWS на среде выполнения .NET"), которая значительно снижает усилия по инструментации и даёт более глубокое и качественное понимание вызовов ваших функций.

В феврале 2021 года AWS объявила о [поддержке трассировки .NET в AWS Distro for OpenTelemetry](https://aws.amazon.com/de/blogs/opensource/aws-distro-for-opentelemetry-adds-net-tracing-support/). Общую информацию об AWS Distro for OpenTelemetry см. на странице [AWS Distro for OpenTelemetry](https://aws-otel.github.io/).

О трассировке AWS Lambda для других языков, таких как Java, Node.JS и Python, с использованием Dynatrace AWS Lambda Layer, см. [Развёртывание OneAgent как расширения Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-extension "Мониторинг Lambda-функций, написанных на Python, Node.js и Java.").

## Предварительные условия

Применяются следующие предварительные условия и ограничения:

* Dynatrace версии 1.222+
* Включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

Экспортёры OpenTelemetry Protocol (OTLP) для .NET в настоящее время поддерживают транспорты [gRPC и HTTP 1.1 с бинарной нагрузкой Protocol Buffers (Protobuf)](https://github.com/open-telemetry/opentelemetry-specification/blob/main/spec-compliance-matrix.md#exporters). Соответствующие поддерживаемые значения протокола: `grpc` и `http/protobuf`. [Параметры конфигурации](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options) можно задать как через переменные окружения, так и явно в коде.

## Инструментация Lambda-функций AWS .NET Core

Dynatrace использует приём трасс OpenTelemetry, чтобы обеспечить сквозную видимость ваших Lambda-функций AWS .NET Core.

Чтобы инструментировать ваши Lambda-функции AWS .NET Core,

[![Шаг 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Шаг 1")

**Настройка экспорта**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#export "Узнайте, как использовать OpenTelemetry для трассировки Lambda-функций AWS .NET Core.")[![Шаг 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Шаг 2")

**Добавление зависимостей**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#instrument-handler "Узнайте, как использовать OpenTelemetry для трассировки Lambda-функций AWS .NET Core.")[![Шаг 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Шаг 3")

**Добавление OpenTelemetry Tracer**](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/aws-lambda-otel-integration/lambda-otel-native#tracer "Узнайте, как использовать OpenTelemetry для трассировки Lambda-функций AWS .NET Core.")

## Шаг 1 Настройка экспорта

Экспорт gRPC

Экспорт HTTP

Чтобы принимать gRPC через Dynatrace Trace API, нужно использовать [коллектор OpenTelemetry](https://dt-url.net/vf23sfn) между Dynatrace и экспортёром. Можно либо развернуть собственный коллектор, либо использовать AWS Distro for OpenTelemetry Collector (ADOT Collector).

Если для настройки используются переменные окружения, нужно задать следующее значение:

* Для `OTEL_EXPORTER_OTLP_PROTOCOL`: `grpc`

### Добавление ARN ADOT Collector Lambda Layer

Регион AWS

Lambda layers являются региональным ресурсом, то есть их можно использовать только в том регионе AWS, в котором они опубликованы. Используйте слой в том же регионе, что и ваши Lambda-функции.

Слой коллектора: `aws-otel-collector-ver-0-27-0`.

Полный список Lambda-слоёв OpenTelemetry, управляемых AWS, см. в репозитории [AWS Distro for OpenTelemetry - AWS Lambda](https://github.com/aws-observability/aws-otel-lambda)

Формат ARN Lambda layer:

```
arn:aws:lambda:\<region>:901920570463:layer:<layer>:1
```

### Настройка ADOT Collector

Конфигурация ADOT Collector следует стандарту OpenTelemetry.

По умолчанию ADOT Lambda layer использует файл `config.yaml`, который экспортирует данные OpenTelemetry в AWS X-Ray. Чтобы экспортировать данные в Dynatrace, нужно настроить конфигурацию с использованием экспортёра OpenTelemetry OTLP.

Чтобы кастомизировать конфигурацию коллектора, добавьте YAML-файл конфигурации в код вашей функции. После того как файл был развёрнут с Lambda-функцией, создайте у вашей Lambda-функции переменную окружения `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` и установите её в `/var/task/<path>/<to>/<filename>`. Это укажет расширению, где найти конфигурацию коллектора.

Ниже приведён пример файла конфигурации `collector.yaml` в корневом каталоге:

1. Скопируйте `collector.yaml` в корневой каталог
2. Установите переменной окружения `OPENTELEMETRY_COLLECTOR_CONFIG_FILE` значение `/var/task/<path>/<to>/<file>`

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

Подробнее о конфигурации см. [OpenTelemetry и Dynatrace](/managed/ingest-from/opentelemetry "Узнайте, как интегрировать и принимать данные OpenTelemetry (трассы, метрики и логи) в Dynatrace.").

Это можно настроить через консоль Lambda или AWS CLI. С CLI используйте следующую команду:

```
aws lambda update-function-configuration --function-name Function --environment Variables={OPENTELEMETRY_COLLECTOR_CONFIG_FILE=/var/task/collector.yaml}
```

Переменные окружения также можно настроить через шаблон CloudFormation:

```
Function:



Type: AWS::Serverless::Function



Properties:



...



Environment:



Variables:



OPENTELEMETRY_COLLECTOR_CONFIG_FILE: /var/task/collector.yaml
```

Чтобы принимать HTTP через Dynatrace Trace API, нужно [настроить экспортёр](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#configuration-options). Экспортёр будет отправлять трассы непосредственно на настроенный эндпоинт.

Если для настройки используются переменные окружения, нужно задать следующие значения:

* Для `OTEL_EXPORTER_OTLP_PROTOCOL`: `http/protobuf`
* Для `OTEL_EXPORTER_OTLP_ENDPOINT`: URL эндпоинта для экспорта

  + Если задать URL эндпоинта через переменные окружения, эндпоинты экспорта для трасс и метрик автоматически дополняются `v1/traces` для трасс и `v1/metrics` для метрик. Например, если эндпоинт задан как `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp`, трассы будут экспортироваться в `https://<YOUR-TENANT-ID>.live.dynatrace.com/api/v2/otlp/v1/traces`.
  + Если эндпоинт явно задан в коде, он будет использоваться как есть.

  Подробнее см. [URL эндпоинтов для OTLP/HTTP](https://github.com/open-telemetry/opentelemetry-specification/blob/main/specification/protocol/exporter.md#endpoint-urls-for-otlphttp).
* Для `OTEL_EXPORTER_OTLP_HEADERS`: значение API-токена авторизации в следующем формате: `Authorization=Api-Token <TOKEN>`.

## Шаг 2 Добавление зависимостей

Добавьте в ваш проект следующие зависимости через NuGet:

```
OpenTelemetry.Exporter.OpenTelemetryProtocol
```

Если вы используете AWS SDK для взаимодействия с другими сервисами AWS, можете добавить автоматическую инструментацию с помощью ADOT SDK для .NET

```
OpenTelemetry.Contrib.Instrumentation.AWS
```

OpenTelemetry также предоставляет другие [библиотеки автоматической инструментации в виде пакетов NuGet](https://www.nuget.org/packages?q=opentelemetry.instrumentation)

## Шаг 3 Добавление OpenTelemetry Tracer

Экспорт gRPC

Экспорт HTTP

AWS Distro for OpenTelemetry не предоставляет wrapper-слой для .NET, как это сделано для других языков. Нужно добавить tracer в ваш код и создать корневой span трассировки.

В следующем примере используется [AWS Lambda Proxy Integration](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html) и транспорт gRPC.

Если не задать свойство `Protocol` класса `OtlpExporterOptions` через переменные окружения или в коде, оно будет инициализировано как [`OtlpExportProtocol.Grpc` по умолчанию](https://github.com/open-telemetry/opentelemetry-dotnet/blob/main/src/OpenTelemetry.Exporter.OpenTelemetryProtocol/OtlpExporterOptions.cs#L99).

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

Пример кода с **HTTP exporter** аналогичен примеру с **gRPC exporter**; единственное отличие в конфигурации `OtlpExporterOptions`:

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

Если конфигурация выполняется через переменные окружения, код добавления экспортёра OTLP/HTTP выглядит ещё проще:

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