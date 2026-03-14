---
title: Журналы AWS Lambda в контексте трассировок
source: https://www.dynatrace.com/docs/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment
scraped: 2026-03-06T21:22:43.535336
---

# Логи AWS Lambda в контексте трассировок


* Classic
* Практическое руководство
* Время чтения: 2 мин
* Опубликовано 08 фев. 2022

На этой странице описано, как включить информацию о `TraceId` и `SpanId` в пользовательские лог-сообщения. Таким образом, вы можете связать лог-сообщения с окружающей трассировкой.

## Предварительные требования

* Настройте [сбор логов AWS Lambda](../../collector.md "Сбор логов из функций AWS Lambda") или [потоковую передачу логов через Amazon Data Firehose](../../../../integrate-with-aws/aws-logs-ingest/lma-stream-logs-with-firehose.md "Интеграция Amazon Data Firehose позволяет получать облачные логи напрямую, без дополнительной инфраструктуры и с более высокой пропускной способностью.").
* [Включите совместимость с OpenTelemetry](../opentelemetry-interoperability.md#enable-otel-interoperability "Включение и использование совместимости с OpenTelemetry в AWS Lambda.") для функции Lambda.
* Вывод логов, генерируемый функцией AWS Lambda, должен быть отформатирован таким образом, чтобы информация о `TraceId` и `SpanId` могла быть извлечена. Ожидаемый формат обогащённых полей в неструктурированном логе:

  + Заключены в квадратные скобки `[]` с префиксом `!dt`
  + `dt.trace_id` и `dt.span_id` должны быть строками в шестнадцатеричной кодировке
    **Пример:** `[!dt dt.trace_id=0af7651916cd43dd8448eb211c80319c,dt.span_id=00f067aa0ba902b7]`

Ознакомьтесь с разделом [Сбор логов AWS Lambda](../../collector.md#limitations "Сбор логов из функций AWS Lambda"), чтобы узнать больше об ограничениях, поскольку обогащение логов Lambda **не** выполняется автоматически.

## OpenTelemetry Python

В примере ниже создана функция `dt_log` для обогащения заданного лог-сообщения информацией о `trace_id` и `span_id`. Вывод этого обогащённого сообщения в настроенный приёмник логов связывает лог-сообщение с текущим активным span в веб-интерфейсе Dynatrace.

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

В примере ниже создана функция `dt_log` для обогащения заданного лог-сообщения информацией о `trace_id` и `span_id`. Вывод этого обогащённого сообщения в `stdout` связывает лог-сообщение с текущим активным span в веб-интерфейсе Dynatrace.

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

Логи, создаваемые некоторыми популярными фреймворками логирования Node.js, автоматически связываются с трассировками при использовании соответствующих инструментаций OpenTelemetry.

В примере ниже инструментация winston используется для обогащения информационного лога winston значениями TraceId и SpanId. Созданный лог связывается с текущим активным span в Dynatrace.

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

В примере ниже создан метод `dtLog` для обогащения заданного лог-сообщения информацией о `TraceId` и `SpanId`. Вывод этого обогащённого сообщения через `System.out` связывает лог-сообщение с текущим активным span в веб-интерфейсе Dynatrace.

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
