---
title: Ручное инструментирование Python-приложения с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/python/python-manual
scraped: 2026-05-12T12:04:15.770289
---

# Ручное инструментирование Python-приложения с OpenTelemetry

# Ручное инструментирование Python-приложения с OpenTelemetry

* Практическое руководство
* Чтение: 4 мин
* Обновлено: 14 ноября 2023

В этом руководстве показано, как добавить наблюдаемость в ваше Python-приложение с помощью библиотек и инструментов OpenTelemetry Python.

## Шаг 1 Получение данных доступа Dynatrace

### Определение базового URL API

Подробнее о том, как собрать базовый URL эндпоинта OTLP, см. [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#export-to-activegate "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа к API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

В разделе [Эндпоинты OTLP API Dynatrace](/managed/ingest-from/opentelemetry/otlp-api#authentication "Узнайте об эндпоинтах OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") больше подробностей о формате и необходимых областях доступа.

## Шаг 2 Инструментирование приложения

1. С помощью [pip](https://pypi.org/project/pip/) установите пакеты OpenTelemetry SDK и API.

   ```
   pip install opentelemetry-api



   pip install opentelemetry-sdk



   pip install opentelemetry-exporter-otlp-proto-http
   ```
2. Добавьте следующие импорты в свой код.

   ```
   import json



   import logging



   from opentelemetry.sdk.resources import Resource



   # Import exporters



   from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter



   from opentelemetry.exporter.otlp.proto.http.metric_exporter import OTLPMetricExporter



   from opentelemetry.exporter.otlp.proto.http._log_exporter import OTLPLogExporter



   # Trace imports



   from opentelemetry.trace import set_tracer_provider, get_tracer_provider



   from opentelemetry.sdk.trace import TracerProvider, sampling



   from opentelemetry.sdk.trace.export import BatchSpanProcessor



   # Metric imports



   from opentelemetry import metrics as metrics



   from opentelemetry.sdk.metrics.export import (



   AggregationTemporality,



   PeriodicExportingMetricReader,



   )



   from opentelemetry.sdk.metrics import MeterProvider, Counter, UpDownCounter, Histogram, ObservableCounter, ObservableUpDownCounter



   from opentelemetry.metrics import set_meter_provider, get_meter_provider



   # Logs import



   from opentelemetry.sdk._logs import LoggerProvider, LoggingHandler



   from opentelemetry.sdk._logs.export import BatchLogRecordProcessor



   from opentelemetry._logs import set_logger_provider
   ```
3. Добавьте следующий код в последовательность запуска, чтобы инициализировать OpenTelemetry сразу после старта приложения. Передайте в переменные `DT_API_URL` и `DT_API_TOKEN` значения [URL Dynatrace](#base-url) и [токена доступа](#access-token).

   ```
   # ===== GENERAL SETUP =====



   DT_API_URL = ""



   DT_API_TOKEN = ""



   merged = dict()



   for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json", "/var/lib/dynatrace/enrichment/dt_host_metadata.json"]:



   try:



   data = ''



   with open(name) as f:



   data = json.load(f if name.startswith("/var") else open(f.read()))



   merged.update(data)



   except:



   pass



   merged.update({



   "service.name": "python-quickstart", #TODO Replace with the name of your application



   "service.version": "1.0.1", #TODO Replace with the version of your application



   })



   resource = Resource.create(merged)



   # ===== TRACING SETUP =====



   tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



   set_tracer_provider(tracer_provider)



   tracer_provider.add_span_processor(



   BatchSpanProcessor(



   OTLPSpanExporter(



   endpoint = DT_API_URL + "/v1/traces",



   headers = {



   "Authorization": "Api-Token " + DT_API_TOKEN



   }



   )



   )



   )



   # ===== METRIC SETUP =====



   exporter = OTLPMetricExporter(



   endpoint = DT_API_URL + "/v1/metrics",



   headers = {"Authorization": "Api-Token " + DT_API_TOKEN},



   preferred_temporality = {



   Counter: AggregationTemporality.DELTA,



   UpDownCounter: AggregationTemporality.CUMULATIVE,



   Histogram: AggregationTemporality.DELTA,



   ObservableCounter: AggregationTemporality.DELTA,



   ObservableUpDownCounter: AggregationTemporality.CUMULATIVE,



   }



   )



   reader = PeriodicExportingMetricReader(exporter)



   provider = MeterProvider(metric_readers=[reader], resource=resource)



   set_meter_provider(provider)



   # ===== LOG SETUP =====



   logger_provider = LoggerProvider(resource=resource)



   set_logger_provider(logger_provider)



   logger_provider.add_log_record_processor(



   BatchLogRecordProcessor(OTLPLogExporter(



   endpoint = DT_API_URL + "/v1/logs",



   headers = {"Authorization": "Api-Token " + DT_API_TOKEN}



   ))



   )



   handler = LoggingHandler(level=logging.NOTSET, logger_provider=logger_provider)



   # Attach OTLP handler to root logger



   logging.getLogger().addHandler(handler)
   ```

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей релевантной информации о топологии внутри Dynatrace.

   Внедрение значений

   Вместо жёсткого кодирования этих значений можно также считывать их из хранилища, специфичного для фреймворка вашего приложения (например, из переменных окружения или секретов фреймворка).

## Шаг 3 (необязательно) Добавление сигналов телеметрии вручную (необязательно)

### Создание спанов

1. Чтобы создавать новые спаны, сначала нам нужен объект tracer.

   ```
   tracer = get_tracer_provider().get_tracer("my-tracer")
   ```
2. С помощью `tracer` теперь можно использовать `start_as_current_span()`, чтобы создавать и запускать новые спаны.

   ```
   with tracer.start_as_current_span("Call to /myendpoint") as span:



   span.set_attribute("http.method", "GET")



   span.set_attribute("net.protocol.version", "1.1")



   #TODO your code goes here
   ```

   В приведённом выше коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [семантическим соглашениям об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичным для действия этого спана: информацию о методе и версии HTTP

   Спан автоматически устанавливается как текущий и активный, пока поток выполнения не выйдет за пределы области текущего метода. Последующие спаны автоматически становятся дочерними спанами.

### Сбор метрик

1. Чтобы создавать новые инструменты метрик, сначала нам нужен объект meter.

   ```
   meter = get_meter_provider().get_meter("my-meter", "0.1.2") #TODO Replace with the name of your meter
   ```
2. С помощью `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   counter = meter.create_counter(



   name="request_counter",



   description="The number of requests we received"



   )
   ```
3. Теперь можно вызвать метод `add()` у `counter`, чтобы записать новые значения нашим счётчиком и сохранить дополнительные атрибуты (например, `action.type`).

   ```
   attributes = {"action.type": "create"}



   counter.add(1, attributes)
   ```

### Подключение логов

С помощью переменной `logging`, инициализированной в разделе [Setup](#setup), можно вести запись логов напрямую в настроенный эндпоинт OpenTelemetry в Dynatrace.

```
logging.error("Log line")
```

Логи Python всё ещё [считаются экспериментальными](https://opentelemetry.io/docs/languages/python/#status-and-releases), и в будущих версиях возможны несовместимые изменения.

## Шаг 4 Обеспечьте context propagation

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

### Извлечение контекста при получении запроса

В следующем примере мы получаем значение заголовка `traceparent` и используем метод `extract()` у `TraceContextTextMapPropagator`, чтобы извлечь предоставленную информацию о контексте, которую затем передаём в `start_as_current_span()`, чтобы продолжить нашу трассировку.

```
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator



traceparent = request.headers.get_all("traceparent")



carrier = {"traceparent": traceparent}



ctx = TraceContextTextMapPropagator().extract(carrier)



with tracer.start_as_current_span("my-span", context=ctx) as span:



span.set_attribute("my-key-1", "my-value-1")
```

### Внедрение контекста при отправке запросов

В следующем примере мы отправляем REST-запрос другому сервису и предоставляем наш существующий контекст в составе HTTP-заголовков нашего запроса.

Для этого мы передаём пустой объект в `TraceContextTextMapPropagator.inject()`, который затем получает необходимое значение заголовка `traceparent`. Затем мы включаем это значение в наш вызов [requests](https://pypi.org/project/requests/) к другому сервису.

```
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator



with tracer.start_as_current_span("my-span") as span:



span.set_attribute("my-key-1", "my-value-1")



try:



carrier = {}



TraceContextTextMapPropagator().inject(carrier)



header = {"traceparent": carrier["traceparent"]}



response = requests.get(url, headers=header)



except Exception as e:



pass
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