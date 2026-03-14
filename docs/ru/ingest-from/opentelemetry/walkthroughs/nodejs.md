---
title: Инструментирование приложения JavaScript на Node.js с помощью OpenTelemetry
source: https://www.dynatrace.com/docs/ingest-from/opentelemetry/walkthroughs/nodejs
scraped: 2026-03-06T21:30:37.921494
---

# Инструментирование JavaScript-приложения на Node.js с помощью OpenTelemetry


* Latest Dynatrace
* Практическое руководство
* Чтение: 5 мин
* Обновлено 14 ноября 2023 г.

Это руководство показывает, как добавить наблюдаемость в ваше JavaScript-приложение с помощью библиотек и инструментов OpenTelemetry JavaScript.

| Функция | Поддерживается |
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

## Шаг 1. Получение данных доступа Dynatrace

### Определение базового URL API

Подробности о формировании базового URL конечной точки OTLP см. в разделе [Конечные точки Dynatrace OTLP API](../otlp-api.md#export-to-activegate "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace."). URL должен заканчиваться на `/api/v2/otlp`.

### Получение токена доступа API

Чтобы сгенерировать токен доступа, в Dynatrace перейдите в ![Access tokens](https://dt-cdn.net/images/access-tokens-512-a766b810b8.png "Access tokens") **Access Tokens**.

[Конечные точки Dynatrace OTLP API](../otlp-api.md#authentication "Узнайте о конечных точках OTLP API, которые ваше приложение использует для экспорта данных OpenTelemetry в Dynatrace.") содержат подробную информацию о формате и необходимых областях доступа.

## Шаг 2. Инициализация OpenTelemetry

1. Выполните следующую команду `npm` для установки необходимых библиотек и зависимостей.

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

   В зависимости от используемых вашим приложением библиотек могут существовать дополнительные библиотеки поддержки инструментирования, которые стоит добавить в зависимости. Список библиотек поддержки можно найти [здесь](https://www.npmjs.com/search?q=%40opentelemetry%2Finstrumentation). Распространённые примеры: [@opentelemetry/instrumentation-http](https://www.npmjs.com/package/@opentelemetry/instrumentation-http) и [@opentelemetry/instrumentation-net](https://www.npmjs.com/package/@opentelemetry/instrumentation-net) для HTTP и сетевых библиотек.
2. Создайте файл с именем `otel.js` в каталоге вашего приложения и сохраните следующее содержимое.

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


   const DT_API_URL = ''; // TODO: Укажите ваш URL SaaS/Managed здесь


   const DT_API_TOKEN = ''; // TODO: Укажите токен доступа OpenTelemetry здесь


   // ===== GENERAL SETUP =====


   registerInstrumentations({


   instrumentations: [ /* TODO Зарегистрируйте здесь ваши библиотеки автоинструментирования */ ],


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

   Операции чтения файлов, разбирающие файлы `dt_metadata` в примере кода, пытаются прочитать [файлы данных OneAgent](../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.") для обогащения OTLP-запроса и обеспечения доступности всей необходимой топологической информации в Dynatrace.
3. Если вы экспортируете через OTLP, настройте две переменные `DT_API_URL` и `DT_API_TOKEN` в `otel.js` с их [соответствующими значениями](#dynatrace-docs--otlp-export).

   Внедрение значений

   Вместо жёсткого задания URL и токена вы также можете рассмотреть возможность их чтения из хранилища, специфичного для вашего фреймворка (например, переменные окружения или секреты фреймворка).
4. Настройте вызов Node.js для вашего приложения, добавив параметр командной строки [--require](https://nodejs.org/api/cli.html#-r---require-module) с указанием на `otel.js`.

   ```
   node --require ./otel.js ./myapplication.js
   ```

## Шаг 3. Ручное инструментирование приложения

### Добавление трассировки

1. Получите ссылку на OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Теперь мы можем получить объект tracer.

   ```
   const tracer = opentelemetry.trace.getTracer('my-tracer');
   ```
3. С помощью `tracer` мы можем использовать span builder для создания и запуска новых span-ов.

   ```
   const span = tracer.startSpan('Call to /myendpoint');


   span.setAttribute('http.method', 'GET');


   span.setAttribute('net.protocol.version','1.1');


   // TODO ваш код здесь


   span.end();
   ```

   В приведённом выше коде мы:

   * Создаём новый span и называем его "Call to /myendpoint"
   * Добавляем два атрибута, следуя [семантическим соглашениям об именовании](https://opentelemetry.io/docs/specs/semconv/general/trace/), специфичным для действия этого span-а: информацию о HTTP-методе и версии
   * Добавляем `TODO` вместо конечной бизнес-логики
   * Вызываем метод `end()` span-а для его завершения

### Сбор метрик

1. Как и при трассировке, сначала нужно получить ссылку на OpenTelemetry API.

   ```
   const opentelemetry = require("@opentelemetry/api");
   ```
2. Далее нам нужно получить объект meter.

   ```
   const meter = opentelemetry.metrics.getMeter('my-meter');
   ```
3. С помощью `meter` мы можем создавать отдельные инструменты, например счётчик.

   ```
   const requestCounter = meter.createCounter('request_counter', {


   description: 'The number of requests we received'


   });
   ```
4. Теперь мы можем вызывать метод `add()` объекта `requestCounter` для записи новых значений в счётчик и сохранения дополнительных атрибутов (например, `action.type`).

   ```
   requestCounter.add(1, { 'action.type': 'create' });
   ```

Вы также можете создать асинхронный gauge, для которого требуется функция обратного вызова, вызываемая OpenTelemetry при сборе данных.

Следующий пример записывает при каждом вызове доступную память:

```
const gauge = meter.createObservableGauge('free_memory');


gauge.addCallback(r => {


r.observe(require('os').freemem());


});
```

### Подключение логов

Пример пока отсутствует, так как OpenTelemetry для Node.js ещё не имеет стабильной поддержки логов.

В зависимости от статуса OpenTelemetry SDK, предварительная версия тем не менее уже может позволять приём ваших логов.

### Обеспечение распространения контекста (необязательно)

Распространение контекста особенно важно при сетевых вызовах (например, REST).

Если вы используете автоматическое инструментирование и ваши сетевые библиотеки покрываются автоматическим инструментированием, это будет автоматически обработано библиотеками инструментирования. В противном случае ваш код должен это учитывать.

#### Извлечение контекста при получении запроса

Следующие примеры предполагают, что мы получили сетевой вызов через [`ClientRequest`](https://nodejs.org/api/http.html#class-httpclientrequest) и используем `extract()` для создания объекта контекста `remoteCtx` на основе информации о контексте, полученной из HTTP-заголовков. Это позволяет продолжить предыдущую трассировку с нашими span-ами.

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

В следующем примере мы используем HTTP-клиент [axios](https://www.npmjs.com/package/axios) для отправки REST-запроса другому сервису и предоставляем наш существующий контекст как часть HTTP-заголовков запроса.

Для этого мы создаём объект `ctx`, передаём ему текущий span и помечаем его как активный. Затем мы передаём этот объект контекста и пустой объект `my_headers` в `inject()` и, после возврата вызова, получаем соответствующие заголовки в `my_headers`, которые мы можем передать в наш HTTP-вызов.

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

## Шаг 4. Настройка сбора данных для соблюдения требований конфиденциальности (необязательно)

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, в веб-интерфейсе Dynatrace сохраняются и отображаются только значения атрибутов, указанные в списке разрешённых. Это предотвращает случайное хранение персональных данных, позволяя вам соблюдать требования конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра пользовательских атрибутов их необходимо сначала разрешить в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскирование атрибутов, см. [Редактирование атрибутов](../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Узнайте, как включить и настроить сенсор Span OneAgent для данных OpenTelemetry.").

## Шаг 5. Проверка приёма данных в Dynatrace

После завершения инструментирования приложения выполните несколько тестовых действий для создания и отправки демонстрационных трассировок, метрик и логов и убедитесь, что они были корректно приняты в Dynatrace.

Для трассировок перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**. Если вы используете OneAgent, выберите вместо этого **PurePaths**.

Для метрик и логов перейдите в **Metrics** или ![Logs and Events](https://dt-cdn.net/images/logs-and-events-512-4b43bbadbe.png "Logs and Events") **Logs & Events Classic**.

## Связанные темы

* [Обогащение принятых данных полями, специфичными для Dynatrace](../../extend-dynatrace/extend-data.md "Узнайте, как автоматически обогащать телеметрические данные полями, специфичными для Dynatrace.")
