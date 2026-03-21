---
title: Инструментирование приложения на C++ с помощью OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/cpp
scraped: 2026-03-05T21:25:30.036786
---

Это руководство показывает, как добавить наблюдаемость в ваше приложение на C++ с использованием библиотек и инструментов OpenTelemetry C++.

| Функция | Поддержка |
| --- | --- |
| Автоматическое инструментирование | Нет |
| Трассировки | Да |
| Метрики | Да |
| Логи | Да |

## Предварительные требования

* Dynatrace версии 1.222+
* [Поддерживаемый](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/README.md#supported-development-platforms) компилятор C++ (C++ 11 и выше)
* [Библиотека Protocol Buffers](https://github.com/protocolbuffers/protobuf/blob/master/src/README.md)
* [Библиотека OpenTelemetry](https://github.com/open-telemetry/opentelemetry-cpp/blob/main/INSTALL.md)
* Для трассировки необходимо включить W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Шаг 1. Получите данные доступа Dynatrace

### Определите базовый URL API

Подробности о том, как сформировать базовый URL OTLP-эндпоинта, см. в разделе [Эндпоинты Dynatrace OTLP API](../otlp-api.md#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получите токен доступа API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Эндпоинты Dynatrace OTLP API](../otlp-api.md#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") содержат дополнительную информацию о формате и необходимых правах доступа.

## Шаг 2. Настройте OpenTelemetry

1. Добавьте следующие директивы в конфигурацию сборки CMake в файле `CMakeLists.txt`:

   ```
   find_package(CURL REQUIRED)


   find_package(Protobuf REQUIRED)


   find_package(opentelemetry-cpp CONFIG REQUIRED)


   include_directories("${OPENTELEMETRY_CPP_INCLUDE_DIRS}")


   target_link_libraries(


   <YOUR_EXE_NAME> ${OPENTELEMETRY_CPP_LIBRARIES}


   opentelemetry_trace


   opentelemetry_common


   opentelemetry_http_client_curl


   opentelemetry_exporter_otlp_http


   opentelemetry_exporter_otlp_http_client


   opentelemetry_otlp_recordable


   opentelemetry_resources


   opentelemetry_metrics


   opentelemetry_exporter_otlp_http_metric


   )
   ```
2. Создайте файл с именем `otel.h` в каталоге вашего приложения и сохраните в него следующее содержимое:

   ```
   #include "opentelemetry/trace/provider.h"


   #include "opentelemetry/trace/propagation/http_trace_context.h"


   #include "opentelemetry/context/propagation/global_propagator.h"


   #include "opentelemetry/sdk/trace/simple_processor_factory.h"


   #include "opentelemetry/sdk/trace/tracer_context.h"


   #include "opentelemetry/sdk/trace/tracer_context_factory.h"


   #include "opentelemetry/sdk/trace/tracer_provider_factory.h"


   #include "opentelemetry/exporters/ostream/span_exporter_factory.h"


   #include "opentelemetry/exporters/otlp/otlp_http_exporter_factory.h"


   #include "opentelemetry/metrics/provider.h"


   #include "opentelemetry/sdk/metrics/export/periodic_exporting_metric_reader.h"


   #include "opentelemetry/sdk/metrics/view/view_registry_factory.h"


   #include "opentelemetry/sdk/metrics/meter_context_factory.h"


   #include "opentelemetry/sdk/metrics/meter_provider_factory.h"


   #include "opentelemetry/exporters/ostream/metric_exporter_factory.h"


   #include "opentelemetry/exporters/otlp/otlp_http_metric_exporter_factory.h"


   #include "opentelemetry/logs/provider.h"


   #include "opentelemetry/sdk/logs/logger.h"


   #include "opentelemetry/sdk/logs/logger_provider_factory.h"


   #include "opentelemetry/sdk/logs/simple_log_record_processor_factory.h"


   #include "opentelemetry/sdk/logs/logger_context_factory.h"


   #include "opentelemetry/exporters/ostream/log_record_exporter.h"


   #include "opentelemetry/exporters/otlp/otlp_http_log_record_exporter_factory.h"


   #include <cstring>


   #include <iostream>


   #include <vector>


   #include <fstream>


   #include <list>


   #include <memory>


   #include <thread>


   #include <iostream>


   #include <string>


   using namespace std;


   namespace nostd    = opentelemetry::nostd;


   namespace otlp     = opentelemetry::exporter::otlp;


   namespace resource = opentelemetry::sdk::resource;


   namespace trace_api      = opentelemetry::trace;


   namespace trace_sdk      = opentelemetry::sdk::trace;


   namespace metrics_api   = opentelemetry::metrics;


   namespace metrics_sdk    = opentelemetry::sdk::metrics;


   namespace logs_api      = opentelemetry::logs;


   namespace logs_sdk      = opentelemetry::sdk::logs;


   namespace


   {


   // Class definition for context propagation


   otlp::OtlpHttpMetricExporterOptions options;


   std::string version{ "1.0.1" };


   std::string name{ "app_cpp" };


   std::string schema{ "https://opentelemetry.io/schemas/1.2.0" };


   template <typename T>


   class HttpTextMapCarrier : public opentelemetry::context::propagation::TextMapCarrier


   {


   public:


   HttpTextMapCarrier<T>(T &headers) : headers_(headers) {}


   HttpTextMapCarrier() = default;


   virtual nostd::string_view Get(nostd::string_view key) const noexcept override


   {


   std::string key_to_compare = key.data();


   // Header's first letter seems to be  automatically capitaliazed by our test http-server, so


   // compare accordingly.


   if (key == opentelemetry::trace::propagation::kTraceParent)


   {


   key_to_compare = "Traceparent";


   }


   else if (key == opentelemetry::trace::propagation::kTraceState)


   {


   key_to_compare = "Tracestate";


   }


   auto it = headers_.find(key_to_compare);


   if (it != headers_.end())


   {


   return it->second;


   }


   return "";


   }


   virtual void Set(nostd::string_view key, nostd::string_view value) noexcept override


   {


   headers_.insert(std::pair<std::string, std::string>(std::string(key), std::string(value)));


   }


   T headers_;


   };


   // ===== GENERAL SETUP =====


   void initTracer()


   {


   otlp::OtlpHttpExporterOptions traceOptions;


   traceOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/traces";


   traceOptions.content_type  = otlp::HttpRequestContentType::kBinary;


   traceOptions.http_headers.insert(


   std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));


   resource::ResourceAttributes resource_attributes = {{"service.name", name},


   {"service.version", version}};


   resource::ResourceAttributes dt_resource_attributes;


   try


   {


   for (string name : {"dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties",


   "/var/lib/dynatrace/enrichment/dt_metadata.properties",


   "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"})


   {


   string file_path;


   ifstream dt_file;


   dt_file.open(name);


   if (dt_file.is_open())


   {


   string dt_metadata;


   ifstream dt_properties;


   while (getline(dt_file, file_path))


   {


   dt_properties.open(file_path);


   if (dt_properties.is_open())


   {


   while (getline(dt_properties, dt_metadata))


   {


   dt_resource_attributes.SetAttribute(


   dt_metadata.substr(0, dt_metadata.find("=")),


   dt_metadata.substr(dt_metadata.find("=") + 1)


   );


   }


   dt_properties.close();


   }


   }


   dt_file.close();


   }


   }


   }


   catch (...) {}


   auto dt_resource = resource::Resource::Create(dt_resource_attributes);


   auto resource = resource::Resource::Create(resource_attributes);


   auto merged_resource = dt_resource.Merge(resource);


   auto exporter = otlp::OtlpHttpExporterFactory::Create(traceOptions);


   auto processor = trace_sdk::SimpleSpanProcessorFactory::Create(std::move(exporter));


   std::vector<std::unique_ptr<trace_sdk::SpanProcessor>> processors;


   processors.push_back(std::move(processor));


   auto context = trace_sdk::TracerContextFactory::Create(std::move(processors), merged_resource);


   std::shared_ptr<opentelemetry::trace::TracerProvider> provider = opentelemetry::sdk::trace::TracerProviderFactory::Create(std::move(context));


   // Set the global trace provider


   opentelemetry::trace::Provider::SetTracerProvider(provider);


   // set global propagator


   opentelemetry::context::propagation::GlobalTextMapPropagator::SetGlobalPropagator(


   opentelemetry::nostd::shared_ptr<opentelemetry::context::propagation::TextMapPropagator>(


   new opentelemetry::trace::propagation::HttpTraceContext()));


   }


   // ===== METRIC SETUP =====


   void initMeter() {


   resource::ResourceAttributes resource_attributes = {{"service.name", name},


   {"service.version", version}};


   otlp::OtlpHttpMetricExporterOptions otlpOptions;


   auto resource = resource::Resource::Create(resource_attributes);


   otlpOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/metrics";


   otlpOptions.aggregation_temporality = otlp::PreferredAggregationTemporality::kDelta;


   otlpOptions.content_type = otlp::HttpRequestContentType::kBinary;


   otlpOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));


   //This creates the exporter with the options we have defined above.


   auto exporter = otlp::OtlpHttpMetricExporterFactory::Create(otlpOptions);


   metrics_sdk::PeriodicExportingMetricReaderOptions options;


   options.export_interval_millis = std::chrono::milliseconds(1000);


   options.export_timeout_millis  = std::chrono::milliseconds(500);


   std::unique_ptr<metrics_sdk::MetricReader> reader{new metrics_sdk::PeriodicExportingMetricReader(std::move(exporter), options) };


   auto context = metrics_sdk::MeterContextFactory::Create(opentelemetry::sdk::metrics::ViewRegistryFactory::Create(), resource);


   context->AddMetricReader(std::move(reader));


   auto u_provider = metrics_sdk::MeterProviderFactory::Create(std::move(context));


   std::shared_ptr<opentelemetry::metrics::MeterProvider> provider(std::move(u_provider));


   metrics_api::Provider::SetMeterProvider(provider);


   }


   // ===== LOG SETUP =====


   void initLogger() {


   resource::ResourceAttributes resource_attributes = {{"service.name", name},


   {"service.version", version}};


   auto resource = resource::Resource::Create(resource_attributes);


   otlp::OtlpHttpLogRecordExporterOptions loggerOptions;


   loggerOptions.url = std::string(std::getenv("DT_API_URL")) + "/v1/logs";


   loggerOptions.http_headers.insert(std::make_pair<const std::string, std::string>("Authorization", std::getenv("DT_API_TOKEN")));


   loggerOptions.content_type = opentelemetry::exporter::otlp::HttpRequestContentType::kBinary;


   auto exporter  = otlp::OtlpHttpLogRecordExporterFactory::Create(loggerOptions);


   auto processor = logs_sdk::SimpleLogRecordProcessorFactory::Create(std::move(exporter));


   std::vector<std::unique_ptr<logs_sdk::LogRecordProcessor>> processors;


   processors.push_back(std::move(processor));


   auto context = logs_sdk::LoggerContextFactory::Create(std::move(processors), resource);


   std::shared_ptr<logs_api::LoggerProvider> provider = logs_sdk::LoggerProviderFactory::Create(std::move(context));


   opentelemetry::logs::Provider::SetLoggerProvider(provider);


   }


   nostd::shared_ptr<opentelemetry::logs::Logger> get_logger(std::string scope){


   // TODO: add your log provider here


   return logger;


   }


   opentelemetry::nostd::shared_ptr<opentelemetry::trace::Tracer> get_tracer(std::string tracer_name)


   {


   // TODO: add your trace provider here


   return tracer;


   }


   nostd::unique_ptr<opentelemetry::metrics::Counter<uint64_t>> initIntCounter()


   {


   // TODO: add your custom metrics here


   return request_counter;


   }


   void initOpenTelemetry() {


   // You can import only the required method


   initLogger();


   initTracer();


   initMeter();


   }


   }
   ```

   Операции чтения файлов, а именно парсинг файлов `dt_metadata` в примере кода, выполняют попытку чтения [файлов данных OneAgent](../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать ваши телеметрические данные полями, специфичными для Dynatrace.") для обогащения OTLP-запроса и обеспечения доступности всей необходимой топологической информации в Dynatrace.
3. Настройте `DT_API_URL` и `DT_API_TOKEN` для [URL Dynatrace](#base-url) и [токена доступа](#access-token) в файле `otel.h`.

## Шаг 3. Инструментируйте ваше приложение

Чтобы использовать OpenTelemetry, сначала необходимо выполнить два шага:

1. Добавьте необходимые заголовочные файлы в ваш код.

   Для добавления заголовочных файлов подключите `otel.h` везде, где вы хотите использовать OpenTelemetry.

   ```
   #include "otel.h"
   ```
2. Инициализируйте OpenTelemetry.

   Для инициализации используйте функцию `initOpenTelemetry` из `otel.h` и вызовите её на раннем этапе запуска вашего приложения.

### Добавление трассировки

1. Получите ссылку на провайдер трассировки.

   ```
   auto provider = opentelemetry::trace::Provider::GetTracerProvider();
   ```
2. Получите объект трассировщика.

   ```
   // In our case the GetTraces method takes the tracer name and returns the tracer provider


   auto tracer = provider->GetTracer(tracer_name);
   ```
3. С помощью `tracer` мы теперь можем создавать новые спаны и устанавливать их для текущей области выполнения.

   ```
   StartSpanOptions options;


   options.kind = SpanKind::kServer;


   auto span = tracer->StartSpan("Call to /myendpoint", {


   { "http.method", "GET" },


   { "net.protocol.version", "1.1" }


   }, options);


   auto scope = tracer->WithActiveSpan(span);


   // TODO: Your code goes here


   span->End();
   ```

   В приведённом коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута в соответствии с [соглашением о семантическом именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информация о методе HTTP и версии
   * Добавляем `TODO` вместо реальной бизнес-логики
   * Вызываем метод `End()` спана для его завершения

### Сбор метрик

1. Получите ссылку на провайдер метрик.

   ```
   auto provider = metrics_api::Provider::GetMeterProvider();
   ```
2. Получите объект измерителя (meter).

   ```
   nostd::shared_ptr<metrics_api::Meter> meter = provider->GetMeter("my-meter", "1.0.1");
   ```
3. С помощью `meter` мы теперь можем создавать отдельные инструменты, например счётчик.

   ```
   auto request_counter = meter->CreateUInt64Counter("request_counter");
   ```
4. Теперь мы можем вызывать метод `Add()` объекта `request_counter` для записи новых значений счётчика и сохранения дополнительных атрибутов (например, `action.type`).

   ```
   std::map<std::string, std::string> labels = { {"action.type", "create"} };


   auto labelkv = opentelemetry::common::KeyValueIterableView<decltype(labels)>{ labels };


   request_counter->Add(1, labelkv);
   ```

### Подключение логов

1. Получите ссылку на провайдер логов.

   ```
   auto provider = logs_api::Provider::GetLoggerProvider();
   ```
2. Вызовите метод `GetLogger()` провайдера для получения экземпляра логгера.

   ```
   auto logger = provider->GetLogger("scope_name", "", OPENTELEMETRY_SDK_VERSION);
   ```
3. Вызовите любой из доступных методов логирования для записи лог-сообщения. Следующий пример записывает отладочное сообщение.

   ```
   logger->Debug("My debug statement here");
   ```

### Обеспечение распространения контекста (необязательно)

Распространение контекста особенно важно, когда задействованы сетевые вызовы (например, REST).

В следующих примерах мы предполагаем, что обрабатываем распространение контекста с использованием стандартных заголовков [W3C trace context](https://www.w3.org/TR/trace-context/), и мы получаем и устанавливаем HTTP-заголовки с помощью объекта OpenTelemetry `http_client::Headers`.

Для этой цели мы используем экземпляр класса `HttpTextMapCarrier`, который мы определили во время настройки и который основан на классе OpenTelemetry [`TextMapCarrier`](https://opentelemetry-cpp.readthedocs.io/en/latest/otel_docs/classopentelemetry_1_1context_1_1propagation_1_1TextMapCarrier.html#exhale-class-classopentelemetry-1-1context-1-1propagation-1-1textmapcarrier).

#### Извлечение контекста при получении запроса

Для извлечения информации о существующем контексте мы вызываем метод `Extract` глобального синглтона пропагатора и передаём ему экземпляр `HttpTextMapCarrier`, а также текущий контекст. Это возвращает новый объект контекста (`new_context`), который позволяет нам продолжить предыдущую трассировку с нашими спанами.

```
StartSpanOptions options;


options.kind          = SpanKind::kServer;


std::string span_name = request.uri;


// extract context from http header


std::map<std::string, std::string> &request_headers =


const_cast<std::map<std::string, std::string> &>(request.headers);


const HttpTextMapCarrier<std::map<std::string, std::string>> carrier(request_headers);


auto prop        = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();


auto current_ctx = context::RuntimeContext::GetCurrent();


auto new_context = prop->Extract(carrier, current_ctx);


options.parent   = GetSpan(new_context)->GetContext();


auto span = get_tracer("manual-server")


->StartSpan("my-server-span", { //TODO Replace with the name of your span


{"my-server-key-1", "my-server-value-1"} //TODO Add attributes


}, options);


auto scope = get_tracer("http_server")->WithActiveSpan(span);


for (auto &kv : request.headers)


{


span->SetAttribute("http.header." + std::string(kv.first.data()), kv.second);


}


span->AddEvent("Processing request");


response.headers[HTTP_SERVER_NS::CONTENT_TYPE] = HTTP_SERVER_NS::CONTENT_TYPE_TEXT;


response.body = doCall();


span->End();
```

#### Внедрение контекста при отправке запросов

Для внедрения информации о текущем контексте в исходящий запрос мы вызываем метод `Inject` глобального синглтона пропагатора и передаём ему экземпляр `HttpTextMapCarrier`, а также текущий контекст. Это добавляет соответствующие заголовки в экземпляр `carrier`, который мы затем используем на следующем шаге с нашим HTTP-запросом.

```
auto http_client = http_client::HttpClientFactory::CreateSync();


std::string url  = std::getenv("URL"); // TODO set URL you want to call


CustomCounter(); // remove


// start active span


StartSpanOptions options;


options.kind = SpanKind::kClient;


opentelemetry::ext::http::common::UrlParser url_parser(url);


std::string span_name = url_parser.path_;


auto span = get_tracer("http-client")->StartSpan(span_name,


{{opentelemetry::semconv::url::kUrlFull, url_parser.url_},


{opentelemetry::semconv::url::kUrlScheme, url_parser.scheme_},


{opentelemetry::semconv::http::kHttpRequestMethod, "GET"}},


options);


auto scope = get_tracer("http-client")->WithActiveSpan(span);


// inject current context into http header


auto current_ctx = context::RuntimeContext::GetCurrent();


HttpTextMapCarrier<http_client::Headers> carrier;


auto prop = context::propagation::GlobalTextMapPropagator::GetGlobalPropagator();


prop->Inject(carrier, current_ctx);


// send http request


http_client::Result result = http_client->GetNoSsl(url, carrier.headers_);


//your code goes here


//then end span
```

## Шаг 4. Настройте захват данных для соответствия требованиям конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, только значения атрибутов, указанные в списке разрешённых, сохраняются и отображаются в веб-интерфейсе Dynatrace. Это предотвращает случайное сохранение персональных данных, позволяя вам соответствовать требованиям конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра ваших пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. раздел [Редактирование атрибутов](../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 5. Проверьте приём данных в Dynatrace

После завершения инструментирования вашего приложения выполните несколько тестовых действий для создания и отправки демонстрационных трассировок, метрик и логов и убедитесь, что они были корректно приняты в Dynatrace.

Для этого для трассировок перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо этого **PurePaths**.

Для метрик и логов перейдите в **Metrics** или ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Связанные темы

* [Обогащение принимаемых данных полями, специфичными для Dynatrace](../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать ваши телеметрические данные полями, специфичными для Dynatrace.")
