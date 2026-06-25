---
title: Журналы AWS Lambda в контексте трасс
source: https://docs.dynatrace.com/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment
scraped: 2026-05-12T12:00:24.886809
---

# Журналы AWS Lambda в контексте трасс

# Журналы AWS Lambda в контексте трасс

* Практическое руководство
* Чтение: 2 мин
* Опубликовано 08 февраля 2022 г.

На этой странице описано, как включить информацию `TraceId` и `SpanId` в сгенерированные пользователем сообщения журнала. Это позволяет связать сообщения журнала с окружающей трассой.

## Предварительные условия

* Настройте [сбор журналов AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector "Сбор журналов с AWS Lambda-функций") или [Потоковую передачу журналов через Amazon Data Firehose (Logs Classic)](/managed/ingest-from/amazon-web-services/integrate-with-aws/aws-logs-ingest/lm-stream-logs-with-firehose "Интеграция с Amazon Data Firehose позволяет принимать облачные журналы напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.").
* [Включите OpenTelemetry interoperability](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability#enable-otel-interoperability "Включение и использование OpenTelemetry interoperability в AWS Lambda.") для Lambda-функции.
* Вывод журналов, генерируемый AWS Lambda-функцией, должен быть отформатирован так, чтобы информация `TraceId` и `SpanId` могла быть считана. Ожидаемый формат обогащённых полей в неструктурированном журнале:

  + Заключены в квадратные скобки `[]` с префиксом `!dt`
  + `dt.trace_id` и `dt.span_id` должны быть строками в hex-кодировке
    **Пример:** `[!dt dt.trace_id=0af7651916cd43dd8448eb211c80319c,dt.span_id=00f067aa0ba902b7]`

Подробнее об ограничениях см. [Сбор журналов AWS Lambda](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/collector#limitations "Сбор журналов с AWS Lambda-функций"), поскольку обогащение журналов Lambda **не** выполняется автоматически.

## OpenTelemetry Python

В примере ниже создана функция `dt_log`, которая обогащает заданное сообщение журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в настроенный приёмник журналов связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

```
import logging



from opentelemetry import trace



def dt_log(self, record):



if (not self.disabled) and self.filter(record):



ctx = trace.get_current_span().get_span_context()



if ctx.is_valid:



trace_id = "{0:032X}".format(ctx.trace_id)



span_id = "{0:016X}".format(ctx.span_id)



record.msg = f"[!dt dt.trace_id={trace_id},dt.span_id={span_id}] - {record.msg}"



self.callHandlers(record)



logging.Logger.handle = dt_log



def lambda_handler(event, context):



logger = logging.getLogger()



logger.warning("Hello world")



return {



"statusCode": 200,



"body": "Hello from lambda"



}
```

## OpenTelemetry JavaScript (Node.js)

В примере ниже создана функция `dt_log`, которая обогащает заданное сообщение журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в `stdout` связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

```
const opentelemetry = require('@opentelemetry/api');



function dtLog(msg) {



const spanContext = opentelemetry.trace.getSpanContext(opentelemetry.context.active()) ?? opentelemetry.INVALID_SPAN_CONTEXT;



console.log(`[!dt dt.trace_id=${spanContext.traceId},dt.span_id=${spanContext.spanId}] - ${msg}`);



}



exports.handler = function(event, context) {



const msg = "Hello World"



dtLog(msg);



context.succeed({



statusCode: 200,



body: msg



});



};
```

Журналы, создаваемые некоторыми часто используемыми Node.js-фреймворками логирования, автоматически связываются с трассами благодаря соответствующим инструментациям OpenTelemetry.

| Фреймворк логирования Node.js | Инструментация OpenTelemetry |
| --- | --- |
| [winston](https://www.npmjs.com/package/winston) | [@opentelemetry/instrumentation-winston](https://www.npmjs.com/package/@opentelemetry/instrumentation-winston) |
| [pino](https://www.npmjs.com/package/pino) | [@opentelemetry/instrumentation-pino](https://www.npmjs.com/package/@opentelemetry/instrumentation-pino) |
| [bunyan](https://www.npmjs.com/package/bunyan) | [@opentelemetry/instrumentation-bunyan](https://www.npmjs.com/package/@opentelemetry/instrumentation-bunyan) |

В примере ниже используется инструментация winston для обогащения info-журнала winston значениями TraceId и SpanId. Созданный журнал связывается с активным в данный момент span в Dynatrace.

```
const otelApi = require('@opentelemetry/api');



const { registerInstrumentations } = require('@opentelemetry/instrumentation');



const { WinstonInstrumentation } = require('@opentelemetry/instrumentation-winston');



registerInstrumentations({



instrumentations: [new WinstonInstrumentation()],



});



const winston = require('winston');



exports.handler = function (event, context, callback) {



const logger = winston.createLogger({



transports: [new winston.transports.Console()],



});



logger.info('winston info log');



context.succeed({



statusCode: 200,



body: 'Hello from AWS Lambda Node.js',



});



}
```

## OpenTelemetry Java

В примере ниже создан метод `dtLog`, который обогащает заданное сообщение журнала информацией `TraceId` и `SpanId`. Вывод этого обогащённого сообщения через `System.out` связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

```
package com.amazonaws.lambda.demo;



import com.amazonaws.services.lambda.runtime.Context;



import com.amazonaws.services.lambda.runtime.RequestHandler;



import io.opentelemetry.api.trace.Span;



import io.opentelemetry.api.trace.SpanContext;



public class HelloJava implements RequestHandler<Object, String> {



private static void dtLog(final String msg) {



SpanContext spanContext = Span.current().getSpanContext();



System.out.printf(



"[!dt dt.trace_id=%s,dt.span_id=%s] - %s%n",



spanContext.getTraceId(),



spanContext.getSpanId(),



msg



);



}



@Override



public String handleRequest(Object input, Context context) {



String msg = "Hello World";



dtLog(msg);



return msg;



}



}
```