---
title: Инструментирование Go-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/go
scraped: 2026-05-12T12:04:03.912527
---

# Инструментирование Go-приложения с OpenTelemetry

# Инструментирование Go-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 5 мин
* Опубликовано: 20 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Go-приложение с помощью библиотек и инструментов OpenTelemetry для Go.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Да |
| Трассировки | Да |
| Метрики | Да |
| Логи | Нет |

## Предварительные требования

* Dynatrace версии 1.222+
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

OpenTelemetry поддерживает в Go автоматическое и ручное инструментирование или их сочетание.

Какое инструментирование выбрать?

Имеет смысл начать с автоматического инструментирования и добавить ручное, если автоматический подход не работает или не даёт достаточно информации.

## Шаг 3 Инициализация OpenTelemetry

1. Добавьте следующие операторы импорта.

   ```
   import (



   "context"



   "github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



   "go.opentelemetry.io/otel"



   "go.opentelemetry.io/otel/attribute"



   "go.opentelemetry.io/otel/exporters/otlp/otlpmetric/otlpmetrichttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlptrace/otlptracehttp"



   "go.opentelemetry.io/otel/exporters/otlp/otlplog/otlploghttp"



   "go.opentelemetry.io/otel/propagation"



   "go.opentelemetry.io/otel/trace"



   sdkmetric "go.opentelemetry.io/otel/sdk/metric"



   "go.opentelemetry.io/otel/sdk/metric/metricdata"



   "go.opentelemetry.io/otel/sdk/resource"



   sdktrace "go.opentelemetry.io/otel/sdk/trace"



   semconv "go.opentelemetry.io/otel/semconv/v1.20.0"



   "log"



   "time"



   "log/slog"



   "go.opentelemetry.io/contrib/bridges/otelslog"



   "go.opentelemetry.io/otel/log/global"



   sdklog "go.opentelemetry.io/otel/sdk/log"



   )
   ```
2. Выполните команду Go [`mod tidy`](https://go.dev/ref/mod#go-mod-tidy), чтобы установить зависимости.

   ```
   go mod tidy
   ```
3. Добавьте следующий код в файл запуска и укажите [соответствующие значения](#get-the-dynatrace-access-details) для `DT_API_HOST` и `DT_API_TOKEN`.

   * `DT_API_HOST` должен содержать только имя хоста вашего URL Dynatrace (например, `XXXXX.live.dynatrace.com`); это не URL и он не должен содержать схем или путей
   * `DT_API_TOKEN` должен содержать токен доступа

   ```
   func InitOpenTelemetry() {



   // ===== GENERAL SETUP =====



   DT_API_HOST := "" // Only the host part of your Dynatrace URL



   DT_API_BASE_PATH := "/api/v2/otlp"



   DT_API_TOKEN := ""



   authHeader := map[string]string{"Authorization": "Api-Token " + DT_API_TOKEN}



   ctx := context.Background()



   oneagentsdk := sdk.CreateInstance()



   dtMetadata := oneagentsdk.GetEnrichmentMetadata()



   var attributes []attribute.KeyValue



   for k, v := range dtMetadata {



   attributes = append(attributes, attribute.KeyValue{Key: attribute.Key(k), Value: attribute.StringValue(v)})



   }



   attributes = append(attributes,



   semconv.ServiceNameKey.String("go-quickstart"), //TODO Replace with the name of your application



   semconv.ServiceVersionKey.String("1.0.1"),      //TODO Replace with the version of your application



   )



   res, err := resource.New(ctx, resource.WithAttributes(attributes...))



   if err != nil {



   log.Fatalf("Failed to create resource: %v", err)



   }



   // ===== TRACING SETUP =====



   exporter, err := otlptracehttp.New(



   ctx,



   otlptracehttp.WithEndpoint(DT_API_HOST),



   otlptracehttp.WithURLPath(DT_API_BASE_PATH+"/v1/traces"),



   otlptracehttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   tp := sdktrace.NewTracerProvider(



   sdktrace.WithResource(res),



   sdktrace.WithSampler(sdktrace.AlwaysSample()),



   sdktrace.WithBatcher(exporter),



   )



   otel.SetTracerProvider(tp)



   otel.SetTextMapPropagator(propagation.NewCompositeTextMapPropagator(propagation.TraceContext{}, propagation.Baggage{}))



   // ===== METRIC SETUP =====



   var deltaTemporalitySelector = func(sdkmetric.InstrumentKind) metricdata.Temporality { return metricdata.DeltaTemporality }



   metricsExporter, err := otlpmetrichttp.New(



   ctx,



   otlpmetrichttp.WithEndpoint(DT_API_HOST),



   otlpmetrichttp.WithURLPath(DT_API_BASE_PATH+"/v1/metrics"),



   otlpmetrichttp.WithHeaders(authHeader),



   otlpmetrichttp.WithTemporalitySelector(deltaTemporalitySelector),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   mp := sdkmetric.NewMeterProvider(



   sdkmetric.WithResource(res),



   sdkmetric.WithReader(sdkmetric.NewPeriodicReader(metricsExporter, sdkmetric.WithInterval(2*time.Second))),



   )



   otel.SetMeterProvider(mp)



   // ===== LOG SETUP =====



   logExporter, err := otlploghttp.New(



   ctx,



   otlploghttp.WithEndpoint(DT_API_HOST),



   otlploghttp.WithURLPath(DT_API_BASE_PATH+"/v1/logs"),



   otlploghttp.WithHeaders(authHeader),



   )



   if err != nil {



   log.Fatalf("Failed to create OTLP exporter: %v", err)



   }



   lp := sdklog.NewLoggerProvider(



   sdklog.WithProcessor(sdklog.NewBatchProcessor(logExporter)),



   sdklog.WithResource(res),



   )



   global.SetLoggerProvider(lp)



   logger := otelslog.NewLogger("my-logger-scope", otelslog.WithLoggerProvider(lp))



   slog.SetDefault(logger) // here we are overwriting the sdtout to http logger exporter



   }
   ```
4. Обязательно вызовите `InitOpenTelemetry` как можно раньше в коде запуска, чтобы инициализировать OpenTelemetry.

## Шаг 4 (необязательно) Автоматическое инструментирование приложения (необязательно)

1. Просмотрите [реестр OpenTelemetry](https://opentelemetry.io/ecosystem/registry/?language=go&component=instrumentation) и выберите библиотеки инструментирования, соответствующие библиотекам вашего приложения.
2. Добавьте нужные пакеты в операторы импорта.

   ```
   import (



   "go.opentelemetry.io/[PACKAGE]"



   )
   ```
3. Выполните команду Go [`mod tiny`](https://go.dev/ref/mod#go-mod-tidy), чтобы установить зависимости.

   ```
   go mod tidy
   ```
4. Оберните существующий код вызовами библиотек поддержки.

### Пример для `net/http`

1. Установите [библиотеку инструментирования для `net/http`](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp).
2. Добавьте пакет в операторы импорта.

   ```
   import (



   // other packages



   "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



   )
   ```
3. Оберните функцию-обработчик HTTP.

   ```
   handler := http.HandlerFunc(httpHandler)



   wrappedHandler := otelhttp.NewHandler(handler, "my-span") //TODO Replace with the name of your span



   //Use the wrappedHandler with your handle



   http.Handle("/", wrappedHandler)
   ```

## Шаг 5 Ручное инструментирование приложения

### Добавление трассировки

1. Сначала нужно получить объект tracer.

   ```
   tracer := otel.Tracer("my-tracer")
   ```
2. С помощью `tracer` теперь можно использовать построитель спанов для создания и запуска новых спанов.

   ```
   _, span := tracer.Start(r.Context(), "Call to /myendpoint")



   defer span.End()



   span.SetAttributes(attribute.String("http.method", "GET"), attribute.String("net.protocol.version", "1.1"))



   // TODO your code goes here
   ```

   В коде выше мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Планируем отложенный вызов `End()`, чтобы спан корректно закрывался при возврате из функции
   * Добавляем два атрибута по [семантическому соглашению об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информацию о методе и версии HTTP
   * Добавляем `TODO` на место будущей бизнес-логики

### Сбор метрик

1. Получите объект meter.

   ```
   meter := otel.Meter("my-meter")
   ```
2. С помощью `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   requestCounter, _ := meter.Int64Counter("request_counter")
   ```
3. Теперь можно вызвать метод `Add()` объекта `requestCounter`, чтобы записывать новые значения счётчиком.

   ```
   requestCounter.Add(context.Background(), 1)
   ```

### Подключение логов

После того как логирование OpenTelemetry инициализировано в `InitOpenTelemetry()` и задано как логгер по умолчанию для [slog](https://pkg.go.dev/log/slog), мы можем вызвать любую из функций логирования slog (например, [`Info()`](https://pkg.go.dev/log/slog#Info)), чтобы отправить информацию из наших логов в Dynatrace.

```
slog.Info("an info message")



slog.Debug("a debug message")



slog.Error("an error")
```

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

#### Извлечение контекста при получении запроса

В следующем примере предполагается, что мы получили сетевой вызов через библиотеку [`net/http`](https://pkg.go.dev/net/http) и её тип [`Request`](https://pkg.go.dev/net/http#Request).

Чтобы получить дескриптор исходного контекста (предоставленного вызывающим сервисом), мы передаём объект HTTP-заголовка (`r.Header`) в функцию `Extract` глобального синглтона-пропагатора, который инстанцирует этот контекст и возвращает его в `parentCtx`. Это позволяет продолжить предыдущую трассировку нашими собственными спанами.

```
func httpHandler(w http.ResponseWriter, r *http.Request) {



parentCtx := otel.GetTextMapPropagator().Extract(r.Context(), propagation.HeaderCarrier(r.Header))



tracer := otel.Tracer("my-tracer")



ctx, span := tracer.Start(



parentCtx,



"manual-server", //TODO Replace with the name of your span



trace.WithAttributes(



attribute.String("my-key-1", "my-value-1"), //TODO Add attributes



),



)



defer span.End()



//TODO your code goes here



}
```

#### Внедрение контекста при отправке запросов

В следующем примере мы настраиваем новый экземпляр [`Request`](https://pkg.go.dev/net/http#Request) и передаём объект в вызов `Inject` глобального синглтона-пропагатора. Это добавляет необходимые HTTP-заголовки в объект запроса, который мы в итоге передаём в `Do` для выполнения сетевого запроса.

```
client := http.Client{}



req, err := http.NewRequest("<method>", "<url>", <body>)



if err != nil {



// TODO handle error



}



//Method to inject the current context in the request headers



otel.GetTextMapPropagator().Inject(ctx, propagation.HeaderCarrier(req.Header))



client.Do(req) // Your call goes here
```

## Шаг 6 Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 7 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")