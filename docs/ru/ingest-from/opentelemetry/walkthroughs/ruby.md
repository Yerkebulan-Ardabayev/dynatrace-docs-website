---
title: Instrument your Ruby application with OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/ruby
scraped: 2026-03-05T21:25:37.194989
---

# Инструментирование Ruby-приложения с помощью OpenTelemetry

# Инструментирование Ruby-приложения с помощью OpenTelemetry

* Актуальная версия Dynatrace
* Практическое руководство
* Чтение: 4 мин
* Обновлено 23 октября 2025

Это пошаговое руководство показывает, как добавить наблюдаемость в ваше Ruby-приложение с использованием библиотек и инструментов OpenTelemetry для Ruby.

| Функция | Поддержка |
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

Подробности о том, как собрать базовый URL конечной точки OTLP, см. в [Конечные точки OTLP API Dynatrace](../otlp-api.md#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Для генерации токена доступа в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Конечные точки OTLP API Dynatrace](../otlp-api.md#authentication "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.") содержат дополнительные сведения о формате и необходимых областях доступа.

## Шаг 2 Выбор способа инструментирования приложения

OpenTelemetry поддерживает для Ruby автоматическое и ручное инструментирование, а также их комбинацию.

Какое инструментирование выбрать?

Рекомендуется начать с автоматического инструментирования и добавить ручное, если автоматический подход не работает или не предоставляет достаточно информации.

## Шаг 3 Инициализация OpenTelemetry

1. Добавьте следующие зависимости в ваш Gemfile.

   ```
   gem 'opentelemetry-sdk'



   gem 'opentelemetry-exporter-otlp'
   ```
2. Добавьте следующее объявление `require`.

   ```
   require 'opentelemetry/sdk'



   require 'opentelemetry/exporter/otlp'
   ```
3. Добавьте функцию `init_opentelemetry` в код запуска и укажите переменные `DT_API_URL` и `DT_API_TOKEN` со значениями [URL Dynatrace](#base-url) и [токена доступа](#access-token).

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

   Операции чтения файлов, выполняющие разбор файлов `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](../../extend-dynatrace/extend-data.md "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.") для обогащения запроса OTLP и обеспечения доступности всей релевантной топологической информации в Dynatrace.

   Экспорт в OneAgent

   Ruby SDK по умолчанию использует сжатие содержимого, которое пока не поддерживается OneAgent.

   При экспорте в OneAgent добавьте `compression: "none"` в вызов `Exporter.new()`, чтобы отключить эту функцию. В противном случае [экспортируйте в ActiveGate](../otlp-api.md#export-to-activegate "Learn about the OTLP API endpoints that your application uses to export OpenTelemetry data to Dynatrace.").
4. Вызовите `init_opentelemetry` как можно раньше при запуске вашего приложения, чтобы обеспечить инициализацию OpenTelemetry с самого начала.

## Шаг 3 (необязательно) Автоматическое инструментирование приложения (необязательно)

1. Добавьте следующую зависимость в ваш Gemfile.

   ```
   gem 'opentelemetry-instrumentation-all'
   ```
2. Добавьте следующее объявление `require`.

   ```
   require 'opentelemetry/instrumentation/all'
   ```
3. Добавьте следующую строку после `c.service_version` в функции `init_opentelemetry`.

   ```
   c.use_all
   ```

## Шаг 4 (необязательно) Ручное инструментирование приложения (необязательно)

### Добавление трассировки

1. Для создания новых спанов сначала необходимо получить объект трассировщика.

   ```
   tracer = OpenTelemetry.tracer_provider.tracer('my-tracer')
   ```
2. С помощью `tracer` мы можем использовать `start_span()` для создания и запуска новых спанов.

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
   * Добавляем два атрибута, следуя [семантическим соглашениям об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичным для действия этого спана: информацию о HTTP-методе и версии
   * Добавляем `TODO` вместо бизнес-логики
   * Вызываем метод `finish()` спана для его завершения (в блоке `ensure`, чтобы гарантировать вызов метода)

## Обработка логов с помощью парсеров технологических пакетов

Через OpenPipeline вы можете использовать и настраивать технологические пакеты. Технологический пакет — это библиотека парсеров (правил обработки), которые обрабатывают логи от различных технологий, таких как Java, .NET и Microsoft IIS.

Парсеры помогают улучшить фильтрацию, поиск неисправностей, метрики, оповещения и дашборды за счёт эффективного извлечения уровней логирования и соответствующих атрибутов. Вы также можете использовать технологические пакеты для структурирования логов от технологий, которые не поддерживаются Dynatrace «из коробки».

![syslog-bundles](https://dt-cdn.net/images/env-syslogbundles-2589-90e4e38b45.png)

Для получения дополнительной информации см. [Обработка логов с помощью парсеров технологических пакетов](../../../platform/openpipeline/use-cases/tutorial-technology-processor.md "Set up a processing pipeline to structure technology-specific logs according to Dynatrace Semantic Dictionary.").

### Сбор метрик

Примера пока нет, так как OpenTelemetry для Ruby ещё не имеет стабильной поддержки метрик.

### Подключение логов

Примера пока нет, так как OpenTelemetry для Ruby ещё не имеет стабильной поддержки логов.

В зависимости от состояния OpenTelemetry SDK, предварительная версия тем не менее может уже позволять приём ваших логов.

### Обеспечение распространения контекста (необязательно)

Распространение контекста особенно важно при сетевых вызовах (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет автоматически обработано библиотеками инструментирования. В противном случае ваш код должен это учитывать.

#### Извлечение контекста при получении запроса

В следующем примере используется метод `extract()` пропагатора по умолчанию для извлечения и воссоздания контекста из запроса в `parent_context`. Затем мы можем передать этот контекст в вызов `start_span` для продолжения предыдущей трассировки нашими спанами.

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

В следующем примере используется стандартная библиотека Ruby [Net:HTTP](https://ruby-doc.org/stdlib-2.7.0/libdoc/net/http/rdoc/Net/HTTP.html) для вызова инструментированного стороннего сервиса. Для добавления необходимых заголовков трассировки мы используем метод `inject()` пропагатора по умолчанию.

```
request = Net::HTTP::Get.new(uri.request_uri)



OpenTelemetry.propagation.inject(request)



response = http.request(request)
```

## Шаг 5 Настройка захвата данных в соответствии с требованиями конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace хранятся и отображаются только значения атрибутов, указанные в списке разрешённых. Это предотвращает случайное сохранение персональных данных, что позволяет соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Чтобы просматривать пользовательские атрибуты, вам сначала нужно разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. [Редактирование атрибутов](../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Learn how to enable and configure the OneAgent Span Sensor for OpenTelemetry data.").

## Шаг 6 Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий для создания и отправки демонстрационных трассировок, метрик и логов и убедитесь, что они были корректно приняты в Dynatrace.

Для трассировок перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, вместо этого выберите **PurePaths**.

Для метрик и логов перейдите в **Metrics** или ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Связанные темы

* [Обогащение принятых данных специфичными для Dynatrace полями](../../extend-dynatrace/extend-data.md "Learn how to automatically enrich your telemetry data with Dynatrace-specific fields.")
