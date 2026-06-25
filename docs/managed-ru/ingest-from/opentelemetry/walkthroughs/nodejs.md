---
title: Инструментирование JavaScript-приложения на Node.js с OpenTelemetry
source: https://docs.dynatrace.com/managed/ingest-from/opentelemetry/walkthroughs/nodejs
scraped: 2026-05-12T12:04:22.354571
---

# Инструментирование JavaScript-приложения на Node.js с OpenTelemetry

# Инструментирование JavaScript-приложения на Node.js с OpenTelemetry

* Практическое руководство
* Чтение: 5 мин
* Обновлено: 14 ноября 2023

В этом руководстве показано, как добавить наблюдаемость в ваше JavaScript-приложение с помощью библиотек и инструментов OpenTelemetry для JavaScript.

| Возможность | Поддерживается |
| --- | --- |
| Автоматическое инструментирование | Да |
| Traces | Да |
| Metrics | Да |
| Logs | Нет |

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

## Шаг 2 Инициализация OpenTelemetry

1. Выполните следующую команду `npm`, чтобы установить необходимые библиотеки и зависимости.

   ```
   npm install \



   @opentelemetry/api \



   @opentelemetry/exporter-metrics-otlp-proto \



   @opentelemetry/exporter-trace-otlp-proto \



   @opentelemetry/instrumentation \



   @opentelemetry/resources \



   @opentelemetry/sdk-metrics \



   @opentelemetry/sdk-trace-node \



   @opentelemetry/semantic-conventions
   ```

   В зависимости от того, какие библиотеки использует ваше приложение, могут понадобиться дополнительные библиотеки поддержки инструментирования, которые вы захотите добавить в зависимости. Список библиотек поддержки можно найти [здесь](https://www.npmjs.com/search?q=%40opentelemetry%2Finstrumentation). Типичные примеры: [@opentelemetry/instrumentation-http](https://www.npmjs.com/package/@opentelemetry/instrumentation-http) и [@opentelemetry/instrumentation-net](https://www.npmjs.com/package/@opentelemetry/instrumentation-net) для библиотек HTTP и сети.
2. Создайте файл с именем `otel.js` в каталоге приложения и сохраните следующее содержимое.

   ```
   const opentelemetry = require("@opentelemetry/api");



   const { resourceFromAttributes, emptyResource, defaultResource } = require("@opentelemetry/resources");



   const { ATTR_SERVICE_NAME, ATTR_SERVICE_VERSION } = require("@opentelemetry/semantic-conventions");



   const { NodeTracerProvider } = require("@opentelemetry/sdk-trace-node");



   const { registerInstrumentations } = require("@opentelemetry/instrumentation");



   const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");



   const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");



   const { OTLPMetricExporter } = require("@opentelemetry/exporter-metrics-otlp-proto");



   const { MeterProvider, PeriodicExportingMetricReader, AggregationTemporality } = require('@opentelemetry/sdk-metrics');



   const DT_API_URL = ''; // TODO: Provide your SaaS/Managed URL here



   const DT_API_TOKEN = ''; // TODO: Provide the OpenTelemetry-scoped access token here



   // ===== GENERAL SETUP =====



   registerInstrumentations({



   instrumentations: [ /* TODO Register your auto-instrumentation libraries here */ ],



   });



   const fs = require("fs");



   let dtmetadata = emptyResource();



   for (let name of ['dt_metadata_e617c525669e072eebe3d0f08212e8f2.json', '/var/lib/dynatrace/enrichment/dt_metadata.json', '/var/lib/dynatrace/enrichment/dt_host_metadata.json']) {



   try {



   dtmetadata = dtmetadata.merge(



   resourceFromAttributes(JSON.parse(fs.readFileSync(name.startsWith("/var") ?



   name : fs.readFileSync(name).toString('utf-8').trim()).toString('utf-8'))));



   break



   } catch { }



   }



   const resource =



   defaultResource().merge(



   resourceFromAttributes({



   [ATTR_SERVICE_NAME]: "js-agent",



   [ATTR_SERVICE_VERSION]: "0.1.0",



   })



   ).merge(dtmetadata);



   // ===== TRACING SETUP =====



   const exporter = new OTLPTraceExporter({



   url: DT_API_URL + '/v1/traces',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN }



   });



   const processor = new BatchSpanProcessor(exporter);



   const provider = new NodeTracerProvider({



   resource: resource,



   spanProcessors: [ processor ]



   });



   provider.register();



   // ===== METRIC SETUP =====



   const metricExporter = new OTLPMetricExporter({



   url: DT_API_URL + '/v1/metrics',



   headers: { Authorization: 'Api-Token ' + DT_API_TOKEN },



   temporalityPreference: AggregationTemporality.DELTA



   });



   const metricReader = new PeriodicExportingMetricReader({



   exporter: metricExporter,



   exportIntervalMillis: 3000



   });



   const meterProvider = new MeterProvider({



   resource: resource,



   readers: [ metricReader ]



   });



   // Set this MeterProvider to be global to the app being instrumented.



   opentelemetry.metrics.setGlobalMeterProvider(meterProvider);
   ```

   Операции чтения файлов, которые разбирают файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](/managed/ingest-from/extend-dynatrace/extend-data "Узнайте, как автоматически обогащать данные телеметрии полями, специфичными для Dynatrace."), чтобы обогатить запрос OTLP и обеспечить доступность всей соответствующей информации о топологии в Dynatrace.
3. Если вы экспортируете через OTLP, настройте две переменные `DT_API_URL` и `DT_API_TOKEN` в `otel.js`, задав им [соответствующие значения](#dynatrace-docs--otlp-export).

   Внедрение значений

   Вместо жёсткого задания URL и токена в коде вы также можете рассмотреть вариант чтения их из хранилища, специфичного для фреймворка вашего приложения (например, переменные окружения или секреты фреймворка).
4. Скорректируйте команду запуска Node.js для вашего приложения, добавив параметр командной строки [--require](https://nodejs.org/api/cli.html#-r---require-module) и указав в нём путь к `otel.js`.

   ```
   node --require ./otel.js ./myapplication.js
   ```

## Шаг 3 Ручное инструментирование приложения

### Добавление трассировки

1. Получите ссылку на API OpenTelemetry.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Теперь можно получить объект tracer.

   ```
   const tracer = opentelemetry.trace.getTracer('my-tracer');
   ```
3. С помощью `tracer` можно использовать построитель спанов для создания и запуска новых спанов.

   ```
   const span = tracer.startSpan('Call to /myendpoint');



   span.setAttribute('http.method', 'GET');



   span.setAttribute('net.protocol.version','1.1');



   // TODO your code goes here



   span.end();
   ```

   В приведённом выше коде мы:

   * Создаём новый спан и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [семантическому соглашению об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичных для действия этого спана: информацию о методе и версии HTTP
   * Добавляем `TODO` на месте будущей бизнес-логики
   * Вызываем метод `end()` спана, чтобы завершить спан

### Сбор метрик

1. Как и при трассировке, сначала нужно получить ссылку на API OpenTelemetry.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Затем нужно получить объект meter.

   ```
   const meter = opentelemetry.metrics.getMeter('my-meter');
   ```
3. С помощью `meter` теперь можно создавать отдельные инструменты, например счётчик.

   ```
   const requestCounter = meter.createCounter('request_counter', {



   description: 'The number of requests we received'



   });
   ```
4. Теперь можно вызвать метод `add()` объекта `requestCounter`, чтобы записать новые значения счётчиком и сохранить дополнительные атрибуты (например, `action.type`).

   ```
   requestCounter.add(1, { 'action.type': 'create' });
   ```

Также можно создать асинхронный gauge, для которого нужна функция обратного вызова, вызываемая OpenTelemetry при сборе данных.

В следующем примере при каждом вызове записывается доступная память:

```
const gauge = meter.createObservableGauge('free_memory');



gauge.addCallback(r => {



r.observe(require('os').freemem());



});
```

### Подключение логов

Примера пока нет, так как OpenTelemetry для Node.js пока не имеет стабильной поддержки логов.

В зависимости от состояния OpenTelemetry SDK предварительная версия тем не менее уже может позволять принимать ваши логи.

### Обеспечение context propagation (необязательно)

Context propagation особенно важно, когда задействованы сетевые вызовы (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки охвачены автоматическим инструментированием, это будет обработано библиотеками инструментирования автоматически. В противном случае это должен учитывать ваш код.

#### Извлечение контекста при получении запроса

В следующих примерах предполагается, что мы получили сетевой вызов через [`ClientRequest`](https://nodejs.org/api/http.html#class-httpclientrequest) и используется `extract()` для создания объекта контекста `remoteCtx` на основе информации о контексте, полученной из HTTP-заголовков. Это позволяет нам продолжить предыдущую трассировку нашими спанами.

```
//Extract context from incoming headers



const { SpanKind, ROOT_CONTEXT } = require("@opentelemetry/api");



const remoteCtx = opentelemetry.propagation.extract(ROOT_CONTEXT, req.headers);



const serverSpan = opentelemetry.trace.getTracer('my-server-tracer')



.startSpan('my-server-span', {



kind: SpanKind.SERVER,



attributes: {



'my-server-key-1': 'my-server-value-1'



},



}, remoteCtx);
```

#### Внедрение контекста при отправке запросов

В следующем примере мы используем HTTP-клиент [axios](https://www.npmjs.com/package/axios) для отправки REST-запроса другому сервису и передаём наш существующий контекст как часть HTTP-заголовков нашего запроса.

Для этого мы создаём объект `ctx`, передаём ему текущий спан и помечаем его как активный. Затем мы передаём этот объект контекста и пустой объект `my_headers` в `inject()`, и после возврата вызова у нас есть нужные заголовки в `my_headers`, которые мы в итоге можем передать в наш HTTP-вызов.

```
const ctx = opentelemetry.trace.setSpan(



opentelemetry.context.active(),



serverSpan



);



const my_headers = {};



opentelemetry.propagation.inject(ctx, my_headers);



await axios.get(URL, {headers: my_headers});



serverSpan.end();
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