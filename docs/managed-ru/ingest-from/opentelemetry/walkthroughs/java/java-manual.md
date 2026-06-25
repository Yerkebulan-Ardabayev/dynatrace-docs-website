---
title: Ручное инструментирование Java-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/java/java-manual
scraped: 2026-05-12T12:12:10.192247
---

# Ручное инструментирование Java-приложения с OpenTelemetry

# Ручное инструментирование Java-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 7 мин
* Опубликовано: 18 апреля 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Java-приложение с помощью библиотек и инструментов ручного инструментирования, предоставляемых OpenTelemetry Java.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").

URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

С авто-конфигурацией SDK

Без авто-конфигурации SDK

1. Добавьте текущие версии следующих пакетов в конфигурацию пакетов (например, Maven, Gradle).

   * [opentelemetry-sdk-extension-autoconfigure](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-sdk-extension-autoconfigure)
   * [opentelemetry-exporter-otlp](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-exporter-otlp)
   * [opentelemetry-semconv](https://central.sonatype.com/artifact/io.opentelemetry.semconv/opentelemetry-semconv)
2. Настройте следующие переменные окружения, чтобы задать предпочтение темпоральности `delta` и определить параметры экспорта, подставив вместо `[URL]` и `[TOKEN]` значения для [базового URL](#base-url) и [токена доступа](#access-token).

   ```
   OTEL_EXPORTER_OTLP_ENDPOINT=[URL]



   OTEL_EXPORTER_OTLP_HEADERS="Authorization=Api-Token [TOKEN]"



   OTEL_EXPORTER_OTLP_PROTOCOL=http/protobuf



   OTEL_RESOURCE_ATTRIBUTES="service.name=java-quickstart,service.version=1.0.1"



   OTEL_EXPORTER_OTLP_METRICS_TEMPORALITY_PREFERENCE=delta
   ```
3. Добавьте следующие операторы import в стартовый класс, который инициализирует ваше приложение.

   ```
   import io.opentelemetry.api.common.Attributes;



   import io.opentelemetry.sdk.OpenTelemetrySdk;



   import io.opentelemetry.sdk.autoconfigure.AutoConfiguredOpenTelemetrySdk;



   import io.opentelemetry.sdk.resources.Resource;



   import io.opentelemetry.instrumentation.log4j.appender.v2_17.OpenTelemetryAppender;
   ```
4. Добавьте метод `initOpenTelemetry` в стартовый класс и вызовите его как можно раньше при запуске приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры tracer и meter по умолчанию.

   ```
   private static void initOpenTelemetry() {



   OpenTelemetrySdk sdk = AutoConfiguredOpenTelemetrySdk.builder().addResourceCustomizer((resource, properties) -> {



   Resource dtMetadata = Resource.empty();



   for (String name : new String[]{"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties", "/var/lib/dynatrace/enrichment/dt_metadata.properties"}) {



   try {



   Properties props = new Properties();



   props.load(name.startsWith("/var") ? new FileInputStream(name) : new FileInputStream(Files.readAllLines(Paths.get(name)).get(0)));



   dtMetadata = dtMetadata.merge(Resource.create(props.entrySet().stream()



   .collect(Attributes::builder, (b, e) -> b.put(e.getKey().toString(), e.getValue().toString()), (b1, b2) -> b1.putAll(b2.build()))



   .build())



   );



   } catch (IOException e) {



   }



   }



   return resource.merge(dtMetadata);



   }).build().getOpenTelemetrySdk();



   OpenTelemetryAppender.install(sdk);



   }
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии в Dynatrace.

1. Добавьте текущие версии следующих пакетов в конфигурацию пакетов (например, Maven, Gradle).

   * [opentelemetry-api](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-api/)
   * [opentelemetry-sdk](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-sdk/)
   * [opentelemetry-exporter-otlp](https://central.sonatype.com/artifact/io.opentelemetry/opentelemetry-exporter-otlp)
   * [opentelemetry-semconv](https://central.sonatype.com/artifact/io.opentelemetry.semconv/opentelemetry-semconv)
2. Добавьте текущую версию [opentelemetry-log4j-appender-2.17](https://central.sonatype.com/artifact/io.opentelemetry.instrumentation/opentelemetry-log4j-appender-2.17) как runtime-библиотеку в конфигурацию пакетов (область `runtime` для Maven, `runtimeOnly` для Gradle).
3. Добавьте следующие операторы import в стартовый класс, который инициализирует ваше приложение.

   ```
   import io.opentelemetry.api.common.AttributeKey;



   import io.opentelemetry.api.common.Attributes;



   import io.opentelemetry.api.trace.propagation.W3CTraceContextPropagator;



   import io.opentelemetry.context.propagation.ContextPropagators;



   import io.opentelemetry.exporter.otlp.http.trace.OtlpHttpSpanExporter;



   import io.opentelemetry.exporter.otlp.http.logs.OtlpHttpLogRecordExporter;



   import io.opentelemetry.exporter.otlp.http.metrics.OtlpHttpMetricExporter;



   import io.opentelemetry.sdk.OpenTelemetrySdk;



   import io.opentelemetry.sdk.resources.Resource;



   import io.opentelemetry.sdk.trace.SdkTracerProvider;



   import io.opentelemetry.sdk.trace.export.BatchSpanProcessor;



   import io.opentelemetry.sdk.trace.export.SpanExporter;



   import io.opentelemetry.sdk.trace.samplers.Sampler;



   import io.opentelemetry.sdk.metrics.SdkMeterProvider;



   import io.opentelemetry.sdk.metrics.export.PeriodicMetricReader;



   import io.opentelemetry.sdk.metrics.export.AggregationTemporalitySelector;



   import io.opentelemetry.sdk.logs.SdkLoggerProvider;



   import io.opentelemetry.sdk.logs.export.BatchLogRecordProcessor;



   import io.opentelemetry.instrumentation.log4j.appender.v2_17.OpenTelemetryAppender;
   ```
4. При приёме данных через OTLP добавьте два поля в стартовый класс для [URL и токена доступа Dynatrace](#dynatrace-docs--otlp-export).

   ```
   private static final String DT_API_URL = ""; // TODO: Provide your SaaS/Managed URL here



   private static final String DT_API_TOKEN = ""; // TODO: Provide the OpenTelemetry-scoped access token here
   ```

   Внедрение значений

   Вместо жёсткого прописывания этих значений можно также рассмотреть их чтение из хранилища, специфичного для фреймворка вашего приложения (например, из переменных окружения или секретов фреймворка).
5. Настройте имя сервиса с помощью переменной окружения `OTEL_SERVICE_NAME`.

   ```
   OTEL_SERVICE_NAME=java-quickstart
   ```
6. Добавьте метод `initOpenTelemetry` в класс инициализатора и вызовите его как можно раньше при запуске приложения. Это инициализирует OpenTelemetry для бэкенда Dynatrace и создаёт провайдеры tracer и meter по умолчанию.

   ```
   private static void initOpenTelemetry()



   {



   // ===== GENERAL SETUP =====



   // Read service name from the environment variable OTEL_SERVICE_NAME, if present



   Resource serviceName = Optional.ofNullable(System.getenv("OTEL_SERVICE_NAME"))



   .map(n -> Attributes.of(AttributeKey.stringKey("service.name"), n))



   .map(Resource::create)



   .orElseGet(Resource::empty);



   // Parse the environment variable OTEL_RESOURCE_ATTRIBUTES into key-value pairs



   Resource envResourceAttributes = Resource.create(Stream.of(Optional.ofNullable(System.getenv("OTEL_RESOURCE_ATTRIBUTES")).orElse("").split(","))



   .filter(pair -> pair != null && pair.length() > 0 && pair.contains("="))



   .map(pair -> pair.split("="))



   .filter(pair -> pair.length == 2)



   .collect(Attributes::builder, (b, p) -> b.put(p[0], p[1]), (b1, b2) -> b1.putAll(b2.build()))



   .build()



   );



   // Define enrichment files



   String[] files = new String[] {



   "dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"



   };



   // Read host information from OneAgent files to enrich telemetry



   Resource dtMetadata = Resource.empty();



   for (String name : files) {



   try {



   Properties props = new Properties();



   props.load(name.startsWith("/var") ? new FileInputStream(name) : new FileInputStream(Files.readAllLines(Paths.get(name)).get(0)));



   dtMetadata = dtMetadata.merge(Resource.create(



   props.entrySet().stream()



   .collect(Attributes::builder, (b, e) -> b.put(e.getKey().toString(), e.getValue().toString()), (b1, b2) -> b1.putAll(b2.build()))



   .build()



   ));



   } catch (IOException e) {}



   }



   // ===== TRACING SETUP =====



   // Configure span exporter with the Dynatrace URL and the API token



   SpanExporter exporter = OtlpHttpSpanExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/traces")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .build();



   // Set up tracer provider with a batch processor and the span exporter



   SdkTracerProvider sdkTracerProvider = SdkTracerProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .setSampler(Sampler.alwaysOn())



   .addSpanProcessor(BatchSpanProcessor.builder(exporter).build())



   .build();



   // ===== METRIC SETUP =====



   // Configure metric exporter with the Dynatrace URL and the API token



   OtlpHttpMetricExporter metricExporter = OtlpHttpMetricExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/metrics")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .setAggregationTemporalitySelector(AggregationTemporalitySelector.deltaPreferred())



   .build();



   // Set up meter provider with a periodic reader and the metric exporter



   SdkMeterProvider meterProvider = SdkMeterProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .registerMetricReader(PeriodicMetricReader.builder(metricExporter).build())



   .build();



   // ===== LOG SETUP =====



   // Configure log exporter with the Dynatrace URL and the API token



   OtlpHttpLogRecordExporter logExporter = OtlpHttpLogRecordExporter.builder()



   .setEndpoint(DT_API_URL + "/v1/logs")



   .addHeader("Authorization", "Api-Token " + DT_API_TOKEN)



   .build();



   // Set up log provider with the log exporter



   SdkLoggerProvider sdkLoggerProvider = SdkLoggerProvider.builder()



   .setResource(Resource.getDefault().merge(envResourceAttributes).merge(serviceName).merge(dtMetadata))



   .addLogRecordProcessor(BatchLogRecordProcessor.builder(logExporter).build())



   .build();



   // ===== INITIALIZATION =====



   // Initialize OpenTelemetry with the tracer and meter providers



   OpenTelemetrySdk sdk = OpenTelemetrySdk.builder()



   .setTracerProvider(sdkTracerProvider)



   .setPropagators(ContextPropagators.create(W3CTraceContextPropagator.getInstance()))



   .setMeterProvider(meterProvider)



   .setLoggerProvider(sdkLoggerProvider)



   .buildAndRegisterGlobal();



   //



   Runtime.getRuntime().addShutdownHook(new Thread(sdkTracerProvider::close));



   OpenTelemetryAppender.install(sdk);



   }
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии в Dynatrace.

## Шаг 3 (необязательно) Добавление сигналов телеметрии вручную (необязательно)

### Создание спанов

1. Чтобы создавать новые спаны, сначала нужен объект tracer.

   ```
   Tracer tracer = GlobalOpenTelemetry



   .getTracerProvider()



   .tracerBuilder("my-tracer") //TODO Replace with the name of your tracer



   .build();
   ```
2. С `tracer` теперь можно использовать построитель спанов для создания и запуска новых спанов.

   ```
   // Obtain and name new span from tracer



   Span span = tracer.spanBuilder("Call to /myendpoint")



   .setSpanKind(SpanKind.CLIENT)



   .startSpan();



   // Set demo span attributes using semantic naming



   span.setAttribute("http.method", "GET");



   span.setAttribute("net.protocol.version", "1.1");



   // Set the span as current span and parent for future child spans



   try (Scope scope = span.makeCurrent())



   {



   // TODO your code goes here



   }



   finally



   {



   // Completing the span



   span.end();



   }
   ```

   В коде выше мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [соглашению о семантическом именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичному для действия этого спана: информацию о методе и версии HTTP
   * Используем метод спана `makeCurrent()`, чтобы пометить его как активный спан и родитель будущих спанов (пока спан не завершён)
   * Вызываем метод спана `end()`, чтобы завершить спан (в блоке `finally`, чтобы гарантировать вызов метода)

### Сбор метрик

1. Чтобы создать новые измерительные инструменты метрик, сначала нужен объект метра.

   ```
   Meter meter = GlobalOpenTelemetry



   .getMeterProvider()



   .meterBuilder("my-meter") //TODO Replace with the name of your meter



   .build();
   ```
2. С `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   LongCounter counter = meter.counterBuilder("request_counter")



   .setDescription("The number of requests we received")



   .setUnit()



   .build();
   ```
3. Теперь можно вызвать метод `add()` объекта `counter`, чтобы записать новые значения с помощью счётчика и сохранить дополнительные атрибуты (например, `action.type`).

   ```
   Attributes attrs = Attributes.of(stringKey("action.type"), "create");



   counter.add(1, attrs);
   ```

Можно также создать асинхронный gauge, для которого требуется функция обратного вызова, которая будет вызываться OpenTelemetry при сборе данных.

В следующем примере при каждом вызове записывается доступная память вместе с атрибутом о числе активных пользователей, полученном из вымышленного метода `getUserCount()`.

```
meter.gaugeBuilder("free_memory")



.setDescription("Available memory in bytes")



.setUnit("bytes")



.buildWithCallback(measurement -> {



measurement.record(



Runtime.getRuntime().freeMemory(),



Attributes.of(stringKey("user_count"), getUserCount())



);



});
```

### Подключение логов

Сначала нужно скорректировать файл конфигурации Log4j 2 `log4j.xml`, чтобы включить аппендер OpenTelemetry.

```
<?xml version="1.0" encoding="UTF-8"?>



<Configuration status="WARN" packages="io.opentelemetry.instrumentation.log4j.appender.v2_17">



<Appenders>



<Console name="Console" target="SYSTEM_OUT">



<PatternLayout



pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} trace_id: %X{trace_id} span_id: %X{span_id} trace_flags: %X{trace_flags} - %msg%n"/>



</Console>



<OpenTelemetry name="OpenTelemetryAppender"/>



</Appenders>



<Loggers>



<Root>



<AppenderRef ref="OpenTelemetryAppender" level="All"/>



<AppenderRef ref="Console" level="All"/>



</Root>



</Loggers>



</Configuration>
```

В этой конфигурации мы добавили новую запись `<OpenTelemetry>` под `<Appenders>`, а также запись `<AppenderRef>` под `<Loggers>`.

С вызовом `GlobalLoggerProvider`, который мы ранее выполнили в разделе [Setup](#setup), этот аппендер настроен для бэкенда Dynatrace.

## Шаг 4 Обеспечьте context propagation

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

### Извлечение контекста при получении запроса

В следующем примере мы предполагаем, что получили сетевой вызов через `com.sun.net.httpserver.HttpExchange`, и определяем экземпляр `TextMapGetter`, чтобы извлечь информацию о контексте из HTTP-заголовков. Затем мы передаём этот экземпляр в `extract()`, возвращающий объект контекста, который позволяет нам продолжить предыдущую трассировку нашими спанами.

```
//The getter will be used for incoming requests



TextMapGetter<HttpExchange> getter =



new TextMapGetter<>() {



@Override



public String get(HttpExchange carrier, String key) {



if (carrier.getRequestHeaders().containsKey(key)) {



return carrier.getRequestHeaders().get(key).get(0);



}



return null;



}



@Override



public Iterable<String> keys(HttpExchange carrier) {



return carrier.getRequestHeaders().keySet();



}



};



@Override



public void handle(HttpExchange httpExchange) {



//Extract the SpanContext and other elements from the request



Context extractedContext = GlobalOpenTelemetry.getPropagators().getTextMapPropagator()



.extract(Context.current(), httpExchange, getter);



try (Scope scope = extractedContext.makeCurrent()) {



//This will automatically propagate context by creating child spans within the extracted context



Span serverSpan = tracer.spanBuilder("my-server-span") //TODO Replace with the name of your span



.setSpanKind(SpanKind.SERVER) //TODO Set the kind of your span



.startSpan();



serverSpan.setAttribute(SemanticAttributes.HTTP_METHOD, "GET"); //TODO Add attributes



serverSpan.end();



}



}
```

### Внедрение контекста при отправке запросов

В следующем примере мы отправляем REST-запрос другому сервису и передаём наш существующий контекст как часть HTTP-заголовков нашего запроса.

Чтобы сделать это, мы определяем экземпляр `TextMapSetter`, который добавляет соответствующую информацию с помощью `setRequestProperty()`. После того как мы создали наш REST-объект, мы передаём его вместе с контекстом и экземпляром сеттера в `inject()`, который добавит необходимые заголовки в запрос.

```
//The setter will be used for outgoing requests



TextMapSetter<HttpURLConnection> setter =



(carrier, key, value) -> {



assert carrier != null;



// Insert the context as Header



carrier.setRequestProperty(key, value);



};



URL url = new URL("<URL>"); //TODO Replace with the URL of the service to be called



Span outGoing = tracer.spanBuilder("my-client-span") //TODO Replace with the name of your span



.setSpanKind(SpanKind.CLIENT) //TODO Set the kind of your span



.startSpan();



try (Scope scope = outGoing.makeCurrent()) {



outGoing.setAttribute(SemanticAttributes.HTTP_METHOD, "GET"); //TODO Add attributes



HttpURLConnection transportLayer = (HttpURLConnection) url.openConnection();



// Inject the request with the *current*  Context, which contains our current span



GlobalOpenTelemetry.getPropagators().getTextMapPropagator().inject(Context.current(), transportLayer, setter);



// Make outgoing call



} finally {



outGoing.end();



}
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