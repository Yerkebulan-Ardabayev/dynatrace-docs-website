---
title: Инструментирование Rust-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/rust
scraped: 2026-05-12T11:22:38.119969
---

# Инструментирование Rust-приложения с OpenTelemetry

# Инструментирование Rust-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 5 мин
* Обновлено: 7 января 2026

В этом руководстве показано, как добавить наблюдаемость в ваше Rust-приложение с помощью библиотек и инструментов OpenTelemetry для Rust.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Нет |
| Трассировки | Да |
| Метрики | Да |
| Логи | Да |

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

## Шаг 2 Настройка OpenTelemetry

1. Добавьте следующие крейты в файл `Cargo.toml`.

   ```
   opentelemetry = { version = "~0", features = ["trace", "metrics"] }



   opentelemetry_sdk = { version = "~0", features = ["rt-tokio", "metrics", "logs", "spec_unstable_metrics_views"] }



   opentelemetry-otlp = { version = "~0", features = ["http-proto", "http-json", "logs", "reqwest-blocking-client", "reqwest-rustls"] }



   opentelemetry-http = { version = "~0" }



   opentelemetry-appender-log = { version = "~0" }



   opentelemetry-semantic-conventions = { version = "~0" }
   ```
2. Добавьте следующие объявления `use` в код.

   ```
   use std::{env, convert::Infallible, net::SocketAddr, collections::HashMap, io::{BufRead, BufReader, Read}};



   use opentelemetry_sdk::trace::SdkTracerProvider;



   use opentelemetry_sdk::{logs::SdkLoggerProvider, metrics::{PeriodicReader, SdkMeterProvider}, propagation::TraceContextPropagator, Resource};



   use opentelemetry_otlp::{LogExporter, MetricExporter, Protocol, SpanExporter, WithExportConfig, WithHttpConfig};



   use opentelemetry_semantic_conventions::trace;



   use opentelemetry_http::{Bytes, HeaderExtractor, HeaderInjector};



   use opentelemetry_appender_log::OpenTelemetryLogBridge;



   use opentelemetry::{global, trace::{FutureExt, Span, SpanKind, TraceContextExt, Tracer}, Context, KeyValue};
   ```
3. Добавьте следующую функцию в файл запуска.

   ```
   fn init_opentelemetry() {



   // Helper function to read potentially available OneAgent data



   fn read_dt_metadata() ->  Vec<KeyValue> {



   fn read_single(path: &str, metadata: &mut Vec<KeyValue>) -> std::io::Result<()> {



   let mut file = std::fs::File::open(path)?;



   if path.starts_with("dt_metadata") {



   let mut name = String::new();



   file.read_to_string(&mut name)?;



   file = std::fs::File::open(name)?;



   }



   for line in BufReader::new(file).lines() {



   if let Some((k, v)) = line?.split_once('=') {



   metadata.push(KeyValue::new(k.to_string(), v.to_string()))



   }



   }



   Ok(())



   }



   let mut metadata = Vec::new();



   for name in [



   "dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",



   "/var/lib/dynatrace/enrichment/dt_metadata.properties",



   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"



   ] {



   let _ = read_single(name, &mut metadata);



   }



   return metadata;



   }



   // ===== GENERAL SETUP =====



   let dt_api_token = env::var("DT_API_TOKEN").unwrap(); // TODO: change



   let dt_api_url = env::var("DT_API_URL").unwrap();



   let mut map = HashMap::new();



   map.insert("Authorization".to_string(), format!("Api-Token {}", dt_api_token));



   let resource = Resource::builder()



   .with_service_name("rust-manual-quickstart")



   .with_attributes(read_dt_metadata())



   .build();



   // ===== TRACING SETUP =====



   global::set_text_map_propagator(TraceContextPropagator::new());



   let tracer_exporter = SpanExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_protocol(Protocol::HttpBinary)



   .with_endpoint(dt_api_url.clone() + "/v1/traces")



   .build()



   .unwrap();



   let tracer_provider = SdkTracerProvider::builder()



   .with_resource(resource.clone())



   .with_batch_exporter(tracer_exporter)



   .build();



   global::set_tracer_provider(tracer_provider.clone());



   // ===== METRICS SETUP ======



   let metrics_exporter = MetricExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/metrics")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let meter_provider = SdkMeterProvider::builder()



   .with_reader(PeriodicReader::builder(metrics_exporter).build())



   .with_resource(resource.clone())



   .build();



   global::set_meter_provider(meter_provider);



   // ===== LOGS SETUP ======



   let logger_exporter = LogExporter::builder()



   .with_http()



   .with_headers(map.clone())



   .with_endpoint(dt_api_url.clone() + "/v1/logs")



   .with_protocol(opentelemetry_otlp::Protocol::HttpBinary)



   .build()



   .unwrap();



   let logger_provider = SdkLoggerProvider::builder()



   .with_batch_exporter(logger_exporter)



   .with_resource(resource.clone())



   .build();



   let otel_log_appender = OpenTelemetryLogBridge::new(&logger_provider);



   log::set_boxed_logger(Box::new(otel_log_appender)).unwrap();



   log::set_max_level(Level::Debug.to_level_filter());



   }
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields."), чтобы обогатить запрос OTLP и обеспечить доступность всей значимой информации о топологии внутри Dynatrace.
4. Убедитесь, что переменные окружения `DT_API_URL` и `DT_API_TOKEN` правильно настроены для [URL Dynatrace](#base-url) и [токена доступа](#access-token).
5. Вызовите `init_opentelemetry()` как можно раньше в коде запуска.

## Шаг 3 Инструментирование приложения

### Добавление трассировки

1. Сначала нужно получить объект tracer.

   ```
   let tracer = global::tracer("my-tracer");
   ```
2. С помощью `tracer` теперь можно запускать новые спаны.

   ```
   let mut _span = tracer



   .span_builder("Call to /myendpoint")



   .with_kind(SpanKind::Internal)



   .start(&tracer);



   _span.set_attribute(KeyValue::new("http.method", "GET"));



   _span.set_attribute(KeyValue::new("net.protocol.version", "1.1"));



   // TODO: Your code goes here



   _span.end();
   ```

   В приведённом выше коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [семантическому соглашению об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичные для действия этого спана: информацию о методе и версии HTTP
   * Добавляем `TODO` на место будущей бизнес-логики
   * Вызываем метод `end()` спана, чтобы завершить спан

### Сбор метрик

1. Сначала нужно получить объект tracer.

   ```
   let meter = global::meter("request_counter");
   ```
2. С помощью `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   let updown_counter = meter.i64_up_down_counter("request_counter").build();
   ```
3. Теперь можно вызвать метод `add()` у `updown_counter`, чтобы записывать новые значения через счётчик.

   ```
   updown_counter.add(1,&[],);
   ```

### Подключение логов

В `init_opentelemetry()` мы ранее инициализировали крейт [log](https://docs.rs/log/latest/log/) с его мостом логов OpenTelemetry и теперь можем вызвать любой из его [макросов логирования](https://docs.rs/log/latest/log/#macros), чтобы логировать напрямую в Dynatrace.

```
error!("logging an error");



debug!("logging a debug message");
```

Максимальный уровень логирования

Обратите внимание на вызов метода [`log::set_max_level`](https://docs.rs/log/latest/log/fn.set_max_level.html) при [инициализации OpenTelemetry](#set-up-opentelemetry) ранее. Он задаёт максимальный уровень логирования крейта log равным `Level::Debug` и требуется для того, чтобы залогированные на этом уровне сообщения вообще выдавались и подхватывались мостом логов OpenTelemetry. Скорректируйте это значение, если используете другой максимальный уровень логирования.

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

#### Извлечение контекста при получении запроса

Чтобы продолжить существующую трассировку из HTTP-запроса, сначала нужно извлечь контекст. Для этого мы объявляем функцию `extract_context_from_request()`, которая принимает объект входящего запроса, извлекает переданный контекст с помощью метода `extract()` пропагатора и возвращает соответствующий объект контекста.

```
// Utility function to extract the context from the incoming request headers



fn extract_context_from_request(req: &Request<Incoming>) -> Context {



global::get_text_map_propagator(|propagator| {



propagator.extract(&HeaderExtractor(req.headers()))



})



}
```

Затем можно использовать `extract_context_from_request()` в нашем обработчике запросов, чтобы получить этот контекст и передать его как родительский в наш собственный новый [серверный спан](https://opentelemetry.io/docs/concepts/signals/traces/#server) с помощью `start_with_context()`.

```
async fn router(req: Request<Incoming>) -> Result<Response<BoxBody<Bytes, hyper::Error>>, Infallible> {



// Extract the context from the incoming request headers



let parent_cx = extract_context_from_request(&req);



let response = {



// Create a span parenting the remote client span.



let tracer = global::tracer("example/server");



let mut span = tracer



.span_builder("router")



.with_kind(SpanKind::Server)



.start_with_context(&tracer, &parent_cx);



// Adding custom attributes



span.set_attribute(KeyValue::new("my-server-key-1", "my-server-value-1"));



};



// TODO Handle the HTTP request



}
```

#### Внедрение контекста при отправке запросов

Чтобы передать текущий контекст в другой HTTP-сервис, мы внедряем информацию о контексте в заголовки HTTP-запроса. В следующем примере объявляется функция `send_request()`, которая принимает URL запроса, содержимое запроса и отправляет запрос с помощью [hyper](https://docs.rs/hyper/latest/hyper/index.html).

После инициализации объекта запроса hyper мы вызываем `get_text_map_propagator()`, чтобы получить глобальный объект `propagator`, а затем используем его функцию `inject_context()`, чтобы добавить в запрос информацию о текущем контексте.

```
async fn send_request(url: &str, body_content: &str, span_name: &str) -> std::result::Result<(), Box<dyn std::error::Error + Send + Sync + 'static>> {



let client = Client::builder(TokioExecutor::new()).build_http();



let tracer = global::tracer("example/client");



let span = tracer



.span_builder(String::from(span_name))



.with_kind(SpanKind::Client)



.start(&tracer);



let cx = Context::current_with_span(span);



let mut req = hyper::Request::builder().uri(url);



global::get_text_map_propagator(|propagator| {



propagator.inject_context(&cx, &mut HeaderInjector(req.headers_mut().unwrap()))



});



let res = client



.request(req.body(Full::new(Bytes::from(body_content.to_string())))?)



.await?;



cx.span().add_event(



"Got response!",



vec![KeyValue::new("status", res.status().to_string())],



);



Ok(())



}
```

## Шаг 4 Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 5 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")