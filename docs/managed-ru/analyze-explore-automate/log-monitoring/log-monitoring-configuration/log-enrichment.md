---
title: Связывание данных журналов с трассами (Logs Classic)
source: https://docs.dynatrace.com/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment
scraped: 2026-05-12T11:13:25.602284
---

# Связывание данных журналов с трассами (Logs Classic)

# Связывание данных журналов с трассами (Logs Classic)

* Чтение: 9 мин
* Обновлено 25 ноября 2025 г.

Log Monitoring Classic

Dynatrace может обогащать принятые данные журналов дополнительной информацией, которая помогает Dynatrace распознавать, коррелировать и оценивать данные. Обогащение журналов обеспечивает более детальный анализ журналов.

Обогащение журналов позволяет:

* Беспрепятственно переключать контекст и анализировать отдельные span'ы, транзакции или целые рабочие нагрузки
* Расширять возможности команд разработчиков, упрощая и ускоряя обнаружение и локализацию проблем

## Автоматическое обогащение журналов

Можно включить обогащение журналов для конкретной технологии, используемой для создания данных журналов, и позволить Dynatrace автоматически добавлять дополнительные атрибуты в каждую принятую запись журнала. Этот метод рекомендуется для структурированных данных журналов известных технологий.

Ограничение обогащения журналов

Используйте **Process group override** для ограничения обогащения журналов до конкретной группы процессов или процесса в группе.

### Включение/отключение обогащения журналов для конкретной технологии

Чтобы включить обогащение журналов для конкретной технологии:

Глобально

Переопределение группы процессов в OneAgent

Пространство имён Kubernetes

1. Перейдите в **Settings** > **Preferences** > **OneAgent features**.
2. Отфильтруйте по **enrichment**.
3. Включите/отключите обогащение журналов для каждой технологии, используемой для генерации принятых данных журналов.
4. Нажмите **Save changes** для сохранения конфигурации.

1. Откройте нужную группу процессов.
2. Выберите **More** (**...**) > **OneAgent features**.
3. Отфильтруйте по **enrichment**.
4. Включите/отключите обогащение журналов для каждой технологии, используемой для генерации принятых данных журналов.
5. Нажмите **Save changes** для сохранения конфигурации.

1. Перейдите в **Infrastructure Observability** > **Kubernetes**.
2. Выберите значение **Namespaces** для вашего кластера Kubernetes.
3. Выберите запись пространства имён Kubernetes, которая вас интересует.
4. В левом верхнем углу страницы перейдите в **More** (**...**) > **Settings** > **OneAgent features**.
5. Нажмите **Add override**.
6. Выберите технологию обогащения журналов из списка **Feature** и убедитесь, что переключатель переопределения функции включён.
7. Нажмите **Save and close**.

### Что делает автоматическое обогащение журналов?

Обогащение журналов изменяет принятые данные журналов и добавляет следующую информацию в каждую обнаруженную запись журнала:

* `dt.trace_id`
* `dt.span_id`
* `dt.entity.process_group_instance`

## Поддерживаемые фреймворки

Список поддерживаемых фреймворков для обогащения контекста журналов трассами/span'ами см. в разделе [Technology support](/managed/ingest-from/technology-support#web-servers "Найдите технические детали поддержки Dynatrace для конкретных платформ и фреймворков разработки.").

## Структурированные данные журналов

Для структурированных данных журналов (JSON, XML и хорошо определённые текстовые форматы) Dynatrace добавляет поле атрибута в запись журнала.

### Пример обогащённых данных журнала в формате JSON

Данные журнала в формате JSON обогащаются дополнительными свойствами `<dt.trace_id>`, `<dt.span_id>` и `dt.entity.process_group_instance`.

```
{



"severity": "error",



"time": 1638957438023,



"pid": 1,



"hostname": "paymentservice-788946fdcd-42lgq",



"name": "paymentservice-charge",



"dt.trace_id": "d04b42bc9f4b6ecdbf6bc9f4b6ecdbc",



"dt.span_id": "9adc716eb808d428",



"dt.entity.process_group_instance": "PROCESS_GROUP_INSTANCE-27204EFED3D8466E",



"message": "Unsupported card type for cardNumber=************0454"



}
```

### Пример обогащённых данных журнала в формате XML

Данные журнала в формате XML обогащаются дополнительными узлами `<dt.trace_id>`, `<dt.span_id>` и `<dt.entity.process_group_instance>`.

```
<?xml version="1.0" encoding="windows-1252" standalone="no"?>



<record>



<date>2021-08-24T14:41:36.565218700Z</date>



<millis>1629816096565</millis>



<nanos>218700</nanos>



<sequence>0</sequence>



<logger>com.apm.testapp.logging.jul.XMLLoggingSample</logger>



<level>INFO</level>



<class>com.apm.testapp.logging.jul.BaseLoggingSample</class>



<method>info</method>



<thread>1</thread>



<message>Update completed successfully.</message>



<dt.trace_id>513fcd4e9b08792fcd4e9b08792</dt.trace_id>



<dt.span_id>125840e3125840e3</dt.span_id>



<dt.entity.process_group_instance>PROCESS_GROUP_INSTANCE-27204EFED3D8466E</dt.entity.process_group_instance>



</record>
```

## Неструктурированные данные журналов

Прежде чем использовать автоматическое обогащение журналов для неструктурированных данных, проверьте, как обогащение журналов Dynatrace повлияет на существующий пайплайн обработки журналов.

Неструктурированные данные журналов, как правило, представляют собой необработанный текст в последовательном порядке, предназначенный для чтения людьми. Dynatrace не обогащает неструктурированные данные журналов автоматически. Dynatrace способен обогащать неструктурированные данные журналов, однако добавление дополнительной информации к данным журналов может повлиять на сторонние инструменты, которые потребляют эти данные.

### Пример обогащённых данных журнала в формате обычного текста

Данные журнала в формате обычного текста обогащаются дополнительной строкой `[!dt dt.trace_id=$trace_id, dt.span_id=$span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]` (атрибуты и их значения).

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e,dt.span_id=b93ede8b93ede8, dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-27204EFED3D8466E]
```

## Ручное обогащение журналов

OneAgent версии 1.239+

Можно вручную обогащать принятые данные журналов Dynatrace, определив шаблон журнала для включения полей `dt.span_id`, `dt.trace_id`, `dt.trace_sampled` и `dt.entity.process_group_instance`. Ручное обогащение журналов для конкретной технологии можно включить, следуя [инструкциям по обогащению журналов](/managed/analyze-explore-automate/log-monitoring/log-monitoring-configuration/log-enrichment#enableenr "Узнайте, как можно связать входящие данные журналов с трассами для более точного анализа в Dynatrace.").

При форматировании обогащённых полей в неструктурированном журнале необходимо соблюдать следующие правила:

* Поля должны быть заключены в квадратные скобки (`[]`) с префиксом `!dt`.  
  Например: `[!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]`
* Поля должны быть отформатированы без двойных кавычек.
* Любые недопустимые символы в именах или значениях полей должны быть экранированы.
* Управляющие символы, такие как `\n`, должны быть исключены из определения обогащения.

### Пример ручного обогащения данных журнала NGINX

Предположим, требуется вручную обогатить данные журнала NGINX значениями `dt.trace_id`, `dt.span_id` и `dt.trace_sampled`. Файл конфигурации NGINX содержит множество стандартных переменных NGINX, а определение формата журнала должно находиться в разделе `log_format`. Например:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled]';



access_log logs/access.log custom;
```

В результате будет создан файл `access.log` с обогащёнными записями журнала:

```
127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=b9e5c9ec08be5fab5071d76f427be7da,dt.span_id=43c5bb9432593963,dt.trace_sampled=true]



127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=01e52950b145d97bf22345e68c5e6c58,dt.span_id=de819d856eecb236,dt.trace_sampled=true]
```

Для OneAgent версии 1.237 и более ранних используются другие переменные NGINX. Например:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$trace_id,dt.span_id=$span_id]'; access_log logs/access.log custom
```

В результате будет создан файл `access.log` с обогащёнными записями журнала:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=e1c0afeb0b8a91d7748139aa764ee37e,dt.span_id=e5e6748fab93ede8]



127.0.0.1 - [21/Oct/2021:10:33:31 +0200] GET /index.html HTTP/1.1 200 1056 [!dt dt.trace_id=81fe7816ba6c38f7aa09aef3684cd941,dt.span_id=3bdacc466ae073cd]
```

Если используется фреймворк журналирования и форматтер логов с поддержкой пользовательских шаблонов, можно адаптировать шаблон в форматтере и напрямую обращаться к атрибутам обогащения Dynatrace.

### Пример ручного обогащения данных журнала Log4j

В PatternFormatter **Log4j** можно задать шаблон для включения информации об обогащении Dynatrace:

```
<PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} dt.trace_id=%X{dt.trace_id} dt.span_id=%X{dt.span_id} dt.entity.process_group_instance=%X{dt.entity.process_group_instance} - %msg%n"/>
```

### Пример ручного обогащения с помощью Logstash Logback encoder

Logback — это преемник проекта log4j. Logstash Logback — расширение, предоставляющее кодировщики, макеты и аппендеры logback для журналирования в JSON и других форматах, поддерживаемых Jackson.

Ниже приведён пример ручного обогащения с использованием кодировщика Logstash. Обратите внимание на дополнительное свойство `mdc` в файле конфигурации, в котором можно включить переменные MDC.

```
<appender name="COMPOSITEJSONENCODER" class="ch.qos.logback.core.FileAppender">



<file>compositejsonencoder.log</file>



<encoder class="net.logstash.logback.encoder.LoggingEventCompositeJsonEncoder">



<providers>



<timestamp>



<fieldName>timestamp</fieldName>



<timeZone>UTC</timeZone>



</timestamp>



<loggerName>



<fieldName>logger</fieldName>



</loggerName>



<logLevel>



<fieldName>level</fieldName>



</logLevel>



<threadName>



<fieldName>thread</fieldName>



</threadName>



<mdc>



<includeMdcKeyName>dt.span_id</includeMdcKeyName>



<includeMdcKeyName>dt.trace_id</includeMdcKeyName>



<includeMdcKeyName>dt.entity.host</includeMdcKeyName>



</mdc>



<stackTrace>



<fieldName>stackTrace</fieldName>



<!-- maxLength - limit the length of the stack trace -->



<throwableConverter class="net.logstash.logback.stacktrace.ShortenedThrowableConverter">



<maxDepthPerThrowable>200</maxDepthPerThrowable>



<maxLength>14000</maxLength>



<rootCauseFirst>true</rootCauseFirst>



</throwableConverter>



</stackTrace>



<message />



<throwableClassName>



<fieldName>exceptionClass</fieldName>



</throwableClassName>



</providers>



</encoder>



</appender>
```

### Пример ручного обогащения данных журнала для winston (Node.js)

Чтобы включить обогащение журналов для winston, активируйте [функцию OneAgent](/managed/ingest-from/dynatrace-oneagent/oneagent-features "Управляйте функциями OneAgent глобально и на уровне группы процессов.") **Node.js - Trace/span context enrichment for unstructured logs**. Можно адаптировать транспорт winston для управления точным местом добавления обогащения, как показано в примере кода ниже.

```
const winston = require("winston");



const Transport = require("winston-transport");



class CustomTransport extends Transport {



log(info, next) {



let myLogLine = `MyLogLine: ${info.timestamp} level=${info.level}: ${info.message}`;



// this is important as above line only picks timestamp, level and message but nothing else from metadata



if (info["dt.trace_id"]) {



myLogLine = `[!dt dt.trace_id=${info["dt.trace_id"]},dt.span_id=${info["dt.span_id"]},dt.trace_sampled=${info["dt.trace_sampled"]}] ${myLogLine}`;



}



console.log(myLogLine);



next();



}



}



const logger = winston.createLogger({



level: "info",



format: winston.format.timestamp(),



transports: [



new CustomTransport(),



// this transport includes all metadata (including dynatrace added traceId,..)



new winston.transport.Console({



format: winston.format.simple()



})



]



})
```

## NGINX ingress с Kubernetes

Можно обогащать журналы с помощью NGINX ingress на Kubernetes в два шага:

1. Выполните инструкции по [инструментированию ingress-nginx на Kubernetes](/managed/ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx "Инструментируйте ingress-nginx на Kubernetes").
2. Добавьте приведённую ниже команду в файл `configmap.yaml` для NGINX ingress.

   Добавление строки `main-snippet` включает приём данных OneAgent и является опциональным, если инструкции ручного инструментирования уже выполнены.

```
main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'
```

Пример файла configmap.yaml

```
apiVersion: v1



kind: Namespace



metadata:



name: prod-ingress-nginx



labels:



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



---



# Source: ingress-nginx/templates/controller-serviceaccount.yaml



apiVersion: v1



kind: ServiceAccount



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx



namespace: prod-ingress-nginx



automountServiceAccountToken: true



---



# Source: ingress-nginx/templates/controller-configmap.yaml



apiVersion: v1



kind: ConfigMap



metadata:



labels:



helm.sh/chart: ingress-nginx-4.0.6



app.kubernetes.io/name: ingress-nginx



app.kubernetes.io/instance: ingress-nginx



app.kubernetes.io/version: 1.0.4



app.kubernetes.io/managed-by: Helm



app.kubernetes.io/component: controller



name: ingress-nginx-controller



namespace: prod-ingress-nginx



data:



allow-snippet-annotations: 'true'



main-snippet: load_module /opt/dynatrace/oneagent/agent/bin/current/linux-musl-x86-64/liboneagentnginx.so;



log-format-upstream: '$remote_addr - $remote_user [$time_local] "$request" [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled] $status $body_bytes_sent  "$http_referer" "$http_user_agent" $request_length'



...
```

## Получение идентификаторов span и trace

Чтобы Dynatrace сопоставлял журналы с соответствующими трассами, можно включать идентификаторы span и trace в сообщения журнала с помощью нотации `[!dt]`.

В следующих примерах показано, как получить идентификаторы span и trace с помощью OpenTelemetry или OneAgent SDK:

Python с OpenTelemetry

JavaScript (Node.js) с OpenTelemetry

Java с OpenTelemetry

Go с OneAgent SDK

В примере ниже создана функция `dt_log` для обогащения заданного сообщения журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в настроенный приёмник журналов связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

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

В примере ниже создана функция `dt_log` для обогащения заданного сообщения журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в `stdout` связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

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

В примере ниже создан метод `dtLog` для обогащения заданного сообщения журнала информацией `TraceId` и `SpanId`. Вывод этого обогащённого сообщения через `System.out` связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

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

В примере ниже HTTP-обработчик использует `Printf()` для записи ответа в стандартный вывод и обогащает эту информацию идентификаторами trace и span, полученными из `oneagentsdk.GetTraceContextInfo()`. Вывод этого обогащённого сообщения связывает сообщение с активным span'ом в веб-интерфейсе Dynatrace.

```
package main



import (



"fmt"



"log"



"net/http"



"github.com/Dynatrace/OneAgent-SDK-for-Go/sdk"



)



func main() {



// Create OneAgent SDK API instance



var oneagentsdk = sdk.CreateInstance()



http.HandleFunc("/", func(w http.ResponseWriter, _ *http.Request) {



// Get TraceContextInfo within the incoming HTTP request



// to obtain Trace ID and Span ID of the active distributed trace context



traceContext := oneagentsdk.GetTraceContextInfo()



msg := "Hello World"



// Log to console



fmt.Printf("[!dt dt.trace_id=%s,dt.span_id=%s] - %s\n", traceContext.GetTraceId(), traceContext.GetSpanId(), msg)



// Write HTTP body



fmt.Fprintf(w, msg)



})



fmt.Println("Starting HTTP server at port 8080...")



log.Fatal(http.ListenAndServe(":8080", nil))



}
```

Подробнее о конфигурации см. в разделе [Журналы AWS Lambda в контексте трасс](/managed/ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment "Настройте обогащение сообщений журнала с помощью OpenTelemetry на AWS Lambda.").

Инструкции по получению атрибутов через OneAgent SDK:

* **Go:** см. [документацию GO на GitHub](https://github.com/Dynatrace/OneAgent-SDK-for-Go)
* **.NET:** см. [документацию .NET на GitHub](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet#trace-context)

## Получение идентификатора экземпляра группы процессов

Поле `dt.entity.process_group_instance` можно получить с помощью команды OpenTelemetry Python, содержащей `merged`. `process_group_instance` извлекается как один из атрибутов, передаваемых в `merged`, как показано в примере ниже:

При использовании OneAgent достаточно указать локальный endpoint без токена аутентификации для включения приёма трасс.

```
import json



from opentelemetry import trace as OpenTelemetry



from opentelemetry.exporter.otlp.proto.http.trace_exporter import (



OTLPSpanExporter,



)



from opentelemetry.sdk.resources import Resource



from opentelemetry.sdk.trace import TracerProvider, sampling



from opentelemetry.sdk.trace.export import (



BatchSpanProcessor,



)



merged = dict()



for name in ["dt_metadata_e617c525669e072eebe3d0f08212e8f2.json", "/var/lib/dynatrace/enrichment/dt_metadata.json"]:



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



tracer_provider = TracerProvider(sampler=sampling.ALWAYS_ON, resource=resource)



OpenTelemetry.set_tracer_provider(tracer_provider)



tracer_provider.add_span_processor(



BatchSpanProcessor(OTLPSpanExporter(



endpoint="http://localhost:14499/otlp/v1/traces"



)))
```

При использовании OneAgent убедитесь, что в настройках Dynatrace включён общедоступный [Extension Execution Controller](/managed/ingest-from/extensions/concepts#eec "Узнайте подробнее о концепции расширений Dynatrace."), иначе данные не будут отправляться.

Перейдите в **Settings** > **Preferences** > **Extension Execution Controller**. Переключатели **Enable Extension Execution Controller** и **Enable local PIPE/HTTP metric and Log Ingest API** должны быть активированы.

Подробнее о конфигурации см. в разделе [Инструментирование Python-приложения с помощью OpenTelemetry](/managed/ingest-from/opentelemetry/walkthroughs/python "Узнайте, как инструментировать Python-приложение с помощью OpenTelemetry и Dynatrace.").

## Связанные темы

* [Использование обогащения журналов для трасс при решении проблем](/managed/observe/application-observability/distributed-traces/use-cases/problems-logs-traces "Используйте обогащение журналов для просмотра связанных записей журналов в представлении распределённых трасс и расширения возможностей анализа.")