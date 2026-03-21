---
title: Трассировка Google Cloud Functions с помощью OpenTelemetry JavaScript
source: https://www.dynatrace.com/docs/ingest-from/google-cloud-platform/gcp-integrations/gcp-functions/otel-gcf-nodejs
scraped: 2026-03-04T21:27:45.484805
---

* Latest Dynatrace
* 8 мин. чтения

Это руководство показывает, как инструментировать Google Cloud Functions с помощью [OpenTelemetry JS](https://github.com/open-telemetry/opentelemetry-js) и экспортировать трейсы в Dynatrace. Чтобы узнать больше о том, как Dynatrace работает с OpenTelemetry, см. [OpenTelemetry и Dynatrace](../../../opentelemetry.md "Узнайте, как интегрировать и принимать данные OpenTelemetry (трейсы, метрики и логи) в Dynatrace.").

## Предварительные требования

Применяются следующие предварительные требования и ограничения:

* Dynatrace версии 1.222+
* Включён W3C Trace Context

  1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
  2. Включите **Send W3C Trace Context HTTP headers**.

## Инструментирование Google Cloud Functions

Dynatrace использует OpenTelemetry Trace Ingest для обеспечения сквозной видимости ваших Google Cloud Functions.

Для инструментирования ваших Google Cloud Functions

[![Step 1](https://dt-cdn.net/images/step-1-086e22066c.svg "Step 1")

**Добавление зависимостей OpenTelemetry**](otel-gcf-nodejs.md#otel-dependencies "Узнайте, как инструментировать Google Cloud Functions с помощью OpenTelemetry JS и экспортировать трейсы в Dynatrace.")[![Step 2](https://dt-cdn.net/images/step-2-1a1384627e.svg "Step 2")

**Настройка OpenTelemetry**](otel-gcf-nodejs.md#otel-setup "Узнайте, как инструментировать Google Cloud Functions с помощью OpenTelemetry JS и экспортировать трейсы в Dynatrace.")[![Step 3](https://dt-cdn.net/images/step-3-350cf6c19a.svg "Step 3")

**Инструментирование точки входа функции**](otel-gcf-nodejs.md#instrument-handler "Узнайте, как инструментировать Google Cloud Functions с помощью OpenTelemetry JS и экспортировать трейсы в Dynatrace.")[![Step 4](https://dt-cdn.net/images/step-4-3f89d67d41.svg "Step 4")

**Инструментирование исходящих запросов**](otel-gcf-nodejs.md#outgoing-instrument "Узнайте, как инструментировать Google Cloud Functions с помощью OpenTelemetry JS и экспортировать трейсы в Dynatrace.")

### Шаг 1. Добавление зависимостей OpenTelemetry

Добавьте следующие необходимые зависимости OpenTelemetry в файл `package.json` (номера версий могут отличаться):

```
"dependencies": {


"@opentelemetry/api": "^1.0.4",


"@opentelemetry/core": "^1.0.1",


"@opentelemetry/exporter-trace-otlp-proto": "^0.27.0",


"@opentelemetry/instrumentation": "^0.27.0",


"@opentelemetry/instrumentation-http": "^0.27.0",


"@opentelemetry/sdk-trace-node": "^1.0.1",


"@opentelemetry/semantic-conventions": "^1.0.1"


}
```

### Шаг 2. Настройка OpenTelemetry

Чтобы обеспечить сбор, связывание и экспорт трейсов в Dynatrace, необходимо соответствующим образом настроить OpenTelemetry. Для этого требуются конечная точка Dynatrace и токен аутентификации.

Для определения конечной точки

1. Откройте Dynatrace.
2. Проверьте адресную строку вашего браузера. URL будет соответствовать одному из следующих шаблонов:

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/...`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/...`
3. Замените часть `...` на `api/v2/otlp`, чтобы получить URL, который вам нужно будет настроить в экспортёре OpenTelemetry.

   * **Dynatrace SaaS**: `https://{your-environment-id}.live.dynatrace.com/api/v2/otlp`
   * **Dynatrace Managed**: `https://{your-domain}/e/{your-environment-id}/api/v2/otlp`

Для создания токена аутентификации

1. Перейдите в **Access Tokens** и выберите **Generate new token**.
2. Укажите **Token name**.
3. В поле **Search scopes** найдите `Ingest OpenTelemetry traces` и установите флажок.
4. Выберите **Generate token**.
5. Выберите **Copy**, чтобы скопировать токен в буфер обмена.
6. Сохраните токен в безопасном месте; вы не сможете отобразить его снова, и он понадобится для настройки экспортёра OpenTelemetry.

Вот как настроить конвейер трассировки OpenTelemetry:

```
const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');


const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');


const { registerInstrumentations } = require('@opentelemetry/instrumentation');


const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');


const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');


const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");


const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");


const { Resource } = require("@opentelemetry/resources");


const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");


diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);


function setupOtel(functionName) {


// create tracer provider


const provider = new NodeTracerProvider({


resource: new Resource({


[SemanticResourceAttributes.SERVICE_NAME]: functionName,


}),


sampler: new AlwaysOnSampler()


});


// add proto exporter


const exporter = new OTLPTraceExporter();


provider.addSpanProcessor(new BatchSpanProcessor(exporter));


// register globally


provider.register({


propagator: new W3CTraceContextPropagator()


});


// add http automatic instrumentation


registerInstrumentations({


instrumentations: [


new HttpInstrumentation()


],


});


return provider;


}
```

Для настройки экспортёра на ваш тенант добавьте следующие переменные среды при развёртывании вашей Google Cloud Function:

* `OTEL_EXPORTER_OTLP_ENDPOINT`: установите ранее определённую конечную точку
* `OTEL_EXPORTER_OTLP_HEADERS`: установите значение `Authorization=Api-Token <TOKEN>`, где `<TOKEN>` — ранее созданный токен аутентификации.

### Шаг 3. Инструментирование точки входа функции

Для инструментирования вызовов Google Cloud Function с помощью OpenTelemetry необходимо сделать две вещи:

1. Создать спан вокруг точки входа функции для трассировки вызовов.
2. Извлечь и связать родительский спан из распространяемого контекста (подробнее о [W3C Trace Context](https://engineering.dynatrace.com/open-source/standards/w3c-trace-context/)).

Для некоторых библиотек OpenTelemetry JS уже предоставляет [инструментации](https://github.com/open-telemetry/opentelemetry-js-contrib), которые вы можете использовать для автоматизации этих задач.

В следующем разделе показано, как инструментировать HTTP (`Trigger: HTTP`) Google Cloud Function.

#### Инструментирование HTTP Google Cloud Function

Точка входа вновь созданной HTTP Google Cloud Function выглядит следующим образом:

```
/**


* Responds to any HTTP request.


*


* @param {!express:Request} req HTTP request context.


* @param {!express:Response} res HTTP response context.


*/


exports.helloWorld = (req, res) => {


let message = req.query.message || req.body.message || 'Hello World!';


res.status(200).send(message);


};
```

OpenTelemetry JS уже предоставляет [инструментацию](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) для этого. Чтобы убедиться, что входящий HTTP-запрос инструментирован и спаны захвачены, необходимо добавить несколько фрагментов кода в код функции.

Добавьте это как первый оператор `require`:

```
const { trace, context } = require("@opentelemetry/api");
```

Затем добавьте эту вспомогательную функцию, которая вызывает функцию `setupOtel`, определённую выше, и применяет пользовательское имя (`funcName`) к автоматически созданному спану.

```
function instrumentHandler(handler, funcName) {


setupOtel(funcName);


return (req, res) => {


const span = trace.getSpan(context.active());


if (span != null) {


span.updateName(funcName);


}


handler(req, res);


};


}
```

Далее мы переносим фактическую бизнес-логику функции в функцию `myHandler`.

```
async function myHandler(req, res) {


let message = req.query.message || req.body.message || 'Hello World!';


res.status(200).send(message);


};
```

Наконец, мы устанавливаем теперь инструментированную функцию `myHandler` в качестве точки входа и подключаем модули `http(s)`.

Без подключения модулей `http(s)` спаны не будут созданы, и трейс функции не появится в Dynatrace.

```
exports.helloWorld = instrumentHandler(myHandler, "helloWorld");


// make sure the http(s) library is patched before the first call


require("http");


require("https");
```

### Шаг 4. Инструментирование исходящих запросов

Для обеспечения сквозной трассировки важно, чтобы исходящие запросы также были инструментированы.

В следующем разделе показано, как инструментировать исходящие HTTP(S)-запросы.

#### Инструментирование исходящих HTTP-запросов

OpenTelemetry JS предоставляет [инструментацию](https://github.com/open-telemetry/opentelemetry-js/tree/main/experimental/packages/opentelemetry-instrumentation-http) для трассировки исходящих HTTP-вызовов (которую мы уже использовали в фрагментах кода выше для трассировки входящего HTTP-вызова).

Следующая вспомогательная функция `httpGet` оборачивает исходящие HTTP(S)-вызовы в объект `Promise`, чтобы результат вызова можно было получить через `await` в основной функции.

```
async function httpGet(url) {


return new Promise((resolve, reject) => {


const isHttps = url.startsWith("https://");


const httpLib = isHttps ? https : http;


const request = httpLib.get(url, (res) => {


console.log(`${url} status code - ${res.statusCode}`);


const responseData = [];


res.on("error", (error) => {


console.error(`${url} reponse error - ${error}`);


reject(error);


});


res.on("data", (chunk) => {


responseData.push(chunk);


});


res.on("end", () => {


resolve({ statusCode: res.statusCode, data: responseData });


});


});


request.on("error", error => {


console.error(`${url} request error - ${error}`);


reject(error);


});


request.end();


});


}
```

Основная функция затем может выполнять исходящие HTTP(S)-вызовы, используя вспомогательную функцию `httpGet`, которая автоматически инструментируется OpenTelemetry.

```
async function myHandler(req, res) {


await httpGet('https://example.com');


await httpGet('http://example.net');


let message = req.query.message || req.body.message || 'Hello World!';


res.status(200).send(message);


};
```

Собирая всё вместе, вот полный пример кода для трассировки Node.js Google Cloud Function, которая вызывается через HTTP и выполняет исходящие HTTP(S)-вызовы.

```
const { trace, context } = require("@opentelemetry/api");


const { NodeTracerProvider } = require('@opentelemetry/sdk-trace-node');


const { W3CTraceContextPropagator, AlwaysOnSampler } = require('@opentelemetry/core');


const { registerInstrumentations } = require('@opentelemetry/instrumentation');


const { HttpInstrumentation } = require('@opentelemetry/instrumentation-http');


const { SemanticResourceAttributes } = require('@opentelemetry/semantic-conventions');


const { OTLPTraceExporter } = require("@opentelemetry/exporter-trace-otlp-proto");


const { BatchSpanProcessor } = require("@opentelemetry/sdk-trace-base");


const { Resource } = require("@opentelemetry/resources");


const { diag, DiagConsoleLogger, DiagLogLevel } = require("@opentelemetry/api");


const http = require("http");


const https = require("https");


diag.setLogger(new DiagConsoleLogger(), DiagLogLevel.ALL);


function setupOtel(functionName) {


// create tracer provider


const provider = new NodeTracerProvider({


resource: new Resource({


[SemanticResourceAttributes.SERVICE_NAME]: functionName,


}),


sampler: new AlwaysOnSampler()


});


// add proto exporter


const exporter = new OTLPTraceExporter();


provider.addSpanProcessor(new BatchSpanProcessor(exporter));


// register globally


provider.register({


propagator: new W3CTraceContextPropagator()


});


// add http automatic instrumentation


registerInstrumentations({


instrumentations: [


new HttpInstrumentation()


],


});


return provider;


}


async function httpGet(url) {


return new Promise((resolve, reject) => {


const isHttps = url.startsWith("https://");


const httpLib = isHttps ? https : http;


const request = httpLib.get(url, (res) => {


console.log(`${url} status code - ${res.statusCode}`);


const responseData = [];


res.on("error", (error) => {


console.error(`${url} reponse error - ${error}`);


reject(error);


});


res.on("data", (chunk) => {


responseData.push(chunk);


});


res.on("end", () => {


resolve({ statusCode: res.statusCode, data: responseData });


});


});


request.on("error", error => {


console.error(`${url} request error - ${error}`);


reject(error);


});


request.end();


});


}


// The function's custom logic goes in here.


async function myHandler(req, res) {


// Perform 2 outgoing HTTP calls.


await httpGet('https://example.com');


await httpGet('http://example.net');


let message = req.query.message || req.body.message || 'Hello World!';


res.status(200).send(message);


};


function instrumentHandler(handler, funcName) {


setupOtel(funcName);


return (req, res) => {


const span = trace.getSpan(context.active());


if (span != null) {


span.updateName(funcName);


}


handler(req, res);


};


}


// This is the function'S entrypoint.


exports.helloWorld = instrumentHandler(myHandler, "helloWorld");


// make sure the http(s) library is patched before the first call


require("http");


require("https");
```

Вот результирующие *распределённые трейсы*, как они отображаются в Dynatrace.

![Трейсы OpenTelemetry JS GCF в Dynatrace](https://dt-cdn.net/images/otel-gcf-nodejs-1578-425c527e3f.png)

## Проверка приёма трейсов в Dynatrace

Через несколько минут после вызова ваших Google Cloud Functions найдите свои спаны:

* Перейдите в ![Distributed Traces Classic](https://dt-cdn.net/images/distributed-traces-classic-7197cdacfb.svg "Distributed Traces Classic") **Distributed Traces Classic** и выберите вкладку **Ingested traces**.
* Ваши спаны будут частью существующего распределённого трейса PurePath, если корень вашего вызова уже мониторится OneAgent.
  Если ваша Google Cloud Function не получает трафик, трейсов не будет.

## (Необязательно) Настройка захвата данных в соответствии с требованиями конфиденциальности

Хотя Dynatrace автоматически захватывает все атрибуты OpenTelemetry, только значения атрибутов, указанные в списке разрешённых, сохраняются и отображаются в веб-интерфейсе Dynatrace. Это предотвращает случайное хранение персональных данных, позволяя вам соответствовать требованиям конфиденциальности и контролировать объём хранимых данных мониторинга.

Для просмотра ваших пользовательских атрибутов необходимо сначала разрешить их в веб-интерфейсе Dynatrace. Чтобы узнать, как настроить хранение и маскировку атрибутов, см. [Редактирование атрибутов](../../../dynatrace-oneagent/oneagent-and-opentelemetry/configuration.md#attribute-redaction "Узнайте, как включить и настроить OneAgent Span Sensor для данных OpenTelemetry.").
