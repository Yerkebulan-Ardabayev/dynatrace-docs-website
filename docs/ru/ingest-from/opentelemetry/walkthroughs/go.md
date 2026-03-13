---
title: Instrument your Go application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/go
scraped: 2026-03-06T21:30:47.260842
---

# Инструментирование приложения Go с помощью OpenTelemetry

# Инструментирование приложения Go с помощью OpenTelemetry

* Последняя версия Dynatrace
* Практическое руководство
* Чтение: 5 мин
* Опубликовано 20 апреля 2023

Это пошаговое руководство описывает, как добавить наблюдаемость в ваше приложение Go с использованием библиотек и инструментов OpenTelemetry Go.

| Функция | Поддержка |
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

## Шаг 1. Получите данные доступа Dynatrace

### Определите базовый URL API

Подробнее о том, как составить базовый URL конечной точки OTLP, см. в разделе [Конечные точки OTLP API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получите токен доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Конечные точки OTLP API Dynatrace](/docs/ingest-from/opentelemetry/otlp-api#authentication "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") содержат подробную информацию о формате и необходимых областях доступа.

## Шаг 2. Выберите способ инструментирования приложения

OpenTelemetry поддерживает в Go автоматическое и ручное инструментирование, а также их комбинацию.

Какое инструментирование выбрать?

Рекомендуется начать с автоматического инструментирования и добавить ручное, если автоматический подход не работает или не предоставляет достаточно информации.

## Шаг 3. Инициализируйте OpenTelemetry

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
2. Выполните команду Go [`mod tidy`](https://go.dev/ref/mod#go-mod-tidy) для установки зависимостей.

   ```
   go mod tidy
   ```
3. Добавьте следующий код в файл запуска приложения и укажите [соответствующие значения](#get-the-dynatrace-access-details) для `DT_API_HOST` и `DT_API_TOKEN`.

   * `DT_API_HOST` должен содержать только имя хоста вашего URL Dynatrace (например, `XXXXX.live.dynatrace.com`); это не URL и не должен содержать схемы или пути
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
4. Убедитесь, что `InitOpenTelemetry` вызывается как можно раньше в коде запуска для инициализации OpenTelemetry.

## Шаг 4 (необязательно). Автоматическое инструментирование приложения

1. Просмотрите [реестр OpenTelemetry](https://opentelemetry.io/ecosystem/registry/?language=go&component=instrumentation) и выберите библиотеки инструментирования, соответствующие библиотекам вашего приложения.
2. Добавьте соответствующие пакеты в операторы импорта.

   ```
   import (



   "go.opentelemetry.io/[PACKAGE]"



   )
   ```
3. Выполните команду Go [`mod tidy`](https://go.dev/ref/mod#go-mod-tidy) для установки зависимостей.

   ```
   go mod tidy
   ```
4. Оберните существующий код вызовами вспомогательных библиотек.

### Пример для `net/http`

1. Установите [библиотеку инструментирования для `net/http`](https://pkg.go.dev/go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp).
2. Добавьте пакет в операторы импорта.

   ```
   import (



   // other packages



   "go.opentelemetry.io/contrib/instrumentation/net/http/otelhttp"



   )
   ```
3. Оберните вашу функцию HTTP-обработчика.

   ```
   handler := http.HandlerFunc(httpHandler)



   wrappedHandler := otelhttp.NewHandler(handler, "my-span") //TODO Replace with the name of your span



   //Use the wrappedHandler with your handle



   http.Handle("/", wrappedHandler)
   ```

## Шаг 5. Ручное инструментирование приложения

### Добавление трассировки

1. Сначала необходимо получить объект tracer.

   ```
   tracer := otel.Tracer("my-tracer")
   ```
2. С помощью `tracer` вы можете создавать и запускать новые спаны.

   ```
   _, span := tracer.Start(r.Context(), "Call to /myendpoint")



   defer span.End()



   span.SetAttributes(attribute.String("http.method", "GET"), attribute.String("net.protocol.version", "1.1"))



   // TODO your code goes here
   ```

   В приведённом коде мы:

   * Создаём новый спан с именем "Call to /myendpoint"
   * Планируем отложенный вызов `End()`, чтобы спан корректно закрывался при возврате из функции
   * Добавляем два атрибута в соответствии с [соглашением об именовании семантики](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичные для действия этого спана: информацию о методе HTTP и версии
   * Добавляем `TODO` вместо будущей бизнес-логики

### Сбор метрик

1. Получите объект meter.

   ```
   meter := otel.Meter("my-meter")
   ```
2. С помощью `meter` можно создавать отдельные инструменты, например счётчик.

   ```
   requestCounter, _ := meter.Int64Counter("request_counter")
   ```
3. Теперь можно вызвать метод `Add()` объекта `requestCounter` для записи новых значений счётчика.

   ```
   requestCounter.Add(context.Background(), 1)
   ```

### Подключение логов

После инициализации логирования OpenTelemetry в `InitOpenTelemetry()` и установки его в качестве логгера по умолчанию для [slog](https://pkg.go.dev/log/slog) можно вызывать любые функции логирования slog (например, [`Info()`](https://pkg.go.dev/log/slog#Info)) для отправки информации из логов в Dynatrace.

```
slog.Info("an info message")



slog.Debug("a debug message")



slog.Error("an error")
```

### Обеспечение распространения контекста (необязательно)

Распространение контекста особенно важно при сетевых вызовах (например, REST).

#### Извлечение контекста при получении запроса

В следующем примере предполагается, что мы получили сетевой вызов через библиотеку [`net/http`](https://pkg.go.dev/net/http) и её тип [`Request`](https://pkg.go.dev/net/http#Request).

Чтобы получить ссылку на исходный контекст (предоставленный вызывающим сервисом), мы передаём объект HTTP-заголовка (`r.Header`) в функцию `Extract` глобального синглтона пропагатора, которая создаёт экземпляр контекста и возвращает его в `parentCtx`. Это позволяет продолжить предыдущую трассировку нашими собственными спанами.

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

В следующем примере мы создаём новый экземпляр [`Request`](https://pkg.go.dev/net/http#Request) и передаём объект в вызов `Inject` глобального синглтона пропагатора. Это добавляет необходимые HTTP-заголовки к объекту запроса, который мы затем передаём в `Do` для выполнения сетевого запроса.

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

## Шаг 6. Настройте захват данных в соответствии с требованиями конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в списке разрешённых. Это предотвращает случайное хранение персональных данных, позволяя соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. [Редактирование атрибутов](/docs/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 7. Проверьте приём данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий для создания и отправки демонстрационных трассировок, метрик и логов и убедитесь, что они были корректно приняты в Dynatrace.

Для проверки трассировок перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо этого **PurePaths**.

Для метрик и логов перейдите в **Metrics** или ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/docs/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")
