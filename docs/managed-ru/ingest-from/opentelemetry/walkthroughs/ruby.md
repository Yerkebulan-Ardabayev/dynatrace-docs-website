---
title: Инструментирование Ruby-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/ruby
scraped: 2026-05-12T11:22:10.019819
---

# Инструментирование Ruby-приложения с OpenTelemetry

# Инструментирование Ruby-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 4 мин
* Обновлено: 23 октября 2025

В этом руководстве показано, как добавить наблюдаемость в ваше Ruby-приложение с помощью библиотек и инструментов OpenTelemetry Ruby.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Да |
| Трассировки | Да |
| Метрики | Нет |
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

OpenTelemetry поддерживает в Ruby автоматическое и ручное инструментирование, а также их сочетание.

Какое инструментирование выбрать?

Хорошая идея, начать с автоматического инструментирования и добавить ручное, если автоматический подход не работает или не даёт достаточно информации.

## Шаг 3 Инициализация OpenTelementry

1. Добавьте следующие зависимости в ваш Gemfile.

   ```
   gem 'opentelemetry-sdk'



   gem 'opentelemetry-exporter-otlp'
   ```
2. Добавьте следующую декларацию `require`.

   ```
   require 'opentelemetry/sdk'



   require 'opentelemetry/exporter/otlp'
   ```
3. Добавьте функцию `init_opentelemetry` в код запуска и передайте переменным `DT_API_URL` и `DT_API_TOKEN` значения для [URL Dynatrace](#base-url) и [токена доступа](#access-token).

   ```
   DT_API_URL = ENV['DT_API_URL']



   DT_API_TOKEN = ENV['DT_API_TOKEN']



   def init_opentelemetry



   OpenTelemetry::SDK.configure do |c|



   c.service_name = 'ruby-quickstart' #TODO Replace with the name of your application



   c.service_version = '1.0.1' #TODO Replace with the version of your application



   # TODO: add automatic instrumentation here (step 3 - optional)



   for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.properties", "/var/lib/dynatrace/enrichment/dt_metadata.properties", "/var/lib/dynatrace/enrichment/dt_host_metadata.properties"] do



   begin



   c.resource = OpenTelemetry::SDK::Resources::Resource.create(Hash[*File.read(name.start_with?("/var") ? name : File.read(name)).split(/[=\n]+/)])



   rescue



   end



   end



   c.add_span_processor(



   OpenTelemetry::SDK::Trace::Export::BatchSpanProcessor.new(



   OpenTelemetry::Exporter::OTLP::Exporter.new(



   endpoint: DT_API_URL + "/v1/traces",



   headers: {



   "Authorization": "Api-Token " + DT_API_TOKEN



   }



   )



   )



   )



   end



   end
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии внутри Dynatrace.

   Экспорт в OneAgent

   Ruby SDK по умолчанию использует сжатие содержимого, которое OneAgent пока не поддерживает.

   При экспорте в OneAgent добавьте `compression: "none"` к вызову `Exporter.new()`, чтобы отключить эту функцию. В противном случае используйте [экспорт в ActiveGate](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.").
4. Вызовите `init_opentelemetry` как можно раньше при запуске приложения, чтобы OpenTelemetry инициализировался с самого начала.

## Шаг 3 (необязательно) Автоматическое инструментирование приложения (необязательно)

1. Добавьте следующую зависимость в ваш Gemfile.

   ```
   gem 'opentelemetry-instrumentation-all'
   ```
2. Добавьте следующую декларацию `require`.

   ```
   require 'opentelemetry/instrumentation/all'
   ```
3. Добавьте следующую строку после `c.service_version` в функции `init_opentelemetry`.

   ```
   c.use_all
   ```

## Шаг 4 (необязательно) Ручное инструментирование приложения (необязательно)

### Добавление трассировки

1. Чтобы создавать новые спаны, сначала нужен объект tracer.

   ```
   tracer = OpenTelemetry.tracer_provider.tracer('my-tracer')
   ```
2. С помощью `tracer` теперь можно использовать `start_span()` для создания и запуска новых спанов.

   ```
   span = tracer.start_span("Call to /myendpoint", kind: :internal)



   OpenTelemetry::Trace.with_span(span) do |span, context|



   span.set_attribute("http.method", "GET")



   span.set_attribute("net.protocol.version", "1.1")



   # TODO your code goes here



   end



   rescue Exception => e



   span&.record_exception(e)



   span&.status = OpenTelemetry::Trace::Status.error("Unhandled exception of type: #{e.class}")



   raise e



   ensure



   span&.finish
   ```

   В приведённом выше коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [соглашению о семантическом именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информацию о методе и версии HTTP
   * Добавляем `TODO` на месте будущей бизнес-логики
   * Вызываем метод `finish()` спана, чтобы завершить спан (в блоке `ensure`, чтобы гарантировать вызов метода)

### Сбор метрик

Примера пока нет, так как OpenTelemetry для Ruby пока не имеет стабильной поддержки метрик.

### Подключение логов

Примера пока нет, так как OpenTelemetry для Ruby пока не имеет стабильной поддержки логов.

В зависимости от статуса OpenTelemetry SDK, предварительная версия тем не менее уже может позволять приём ваших логов.

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

#### Извлечение контекста при получении запроса

В следующем примере используется метод `extract()` пропагатора по умолчанию для извлечения и воссоздания контекста из запроса, в `parent_context`. Затем мы можем передать этот контекст вызову `start_span`, чтобы продолжить предыдущую трассировку нашими спанами.

```
parent_context = OpenTelemetry.propagation.extract(



env,



getter: OpenTelemetry::Common::Propagation.rack_env_getter



)



span = tracer.start_span("hello world", with_parent: parent_context)



OpenTelemetry::Trace.with_span(span) do |span, context|



span.set_attribute("my-key-1", "my-value-1")



# ... expansive query



end



ensure



span&.finish



end
```

#### Внедрение контекста при отправке запросов

В следующем примере используется стандартная библиотека Ruby [Net:HTTP](https://ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html), чтобы вызвать инструментированный сторонний сервис. Чтобы добавить необходимые заголовки трассировки, мы используем метод `inject()` пропагатора по умолчанию.

```
request = Net::HTTP::Get.new(uri.request_uri)



OpenTelemetry.propagation.inject(request)



response = http.request(request)
```

## Шаг 5 Настройка захвата данных под требования конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в allowlist. Это предотвращает случайное хранение персональных данных, поэтому вы можете соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать ваши пользовательские атрибуты, сначала нужно разрешить их в веб-интерфейсе Dynatrace. О том, как настроить хранение и маскирование атрибутов, см. [Маскирование атрибутов](/managed/ingest-from/dynatrace-oneagent/oneagent-and-opentelemetry/configuration#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").

## Шаг 6 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий, чтобы создать и отправить демонстрационные трассировки, метрики и логи, и убедитесь, что они корректно приняты в Dynatrace.

Чтобы сделать это для трассировок, перейдите в **Distributed Traces** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо неё **PurePaths**.

Для метрик и логов перейдите в **Metrics** или **Logs**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace.")