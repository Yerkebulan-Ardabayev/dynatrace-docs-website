---
title: Связывание данных журналов с трейсами
source: https://www.dynatrace.com/docs/analyze-explore-automate/logs/lma-log-enrichment
scraped: 2026-03-06T21:12:18.348722
---

Dynatrace может дополнять принятые данные журналов дополнительной информацией, которая помогает Dynatrace распознавать, коррелировать и оценивать данные. Обогащение журналов позволяет проводить более тонкий анализ ваших журналов.

Обогащение журналов позволяет:

* Плавно переключать контекст и анализировать отдельные спаны, транзакции или целые рабочие нагрузки
* Расширить возможности команд разработчиков, упрощая и ускоряя обнаружение и локализацию проблем

## Автоматическое обогащение журналов

Вы можете включить обогащение журналов для конкретной технологии, используемой для создания данных журналов, и позволить Dynatrace автоматически добавлять дополнительные атрибуты в каждую получаемую запись журнала. Этот метод рекомендуется для структурированных данных журналов известных технологий.

Ограничение обогащения журналов

Используйте **Process group override**, чтобы ограничить обогащение журналов конкретной группой процессов или процессом внутри группы процессов.

### Включение/отключение обогащения журналов для конкретной технологии

Чтобы включить обогащение журналов для конкретной технологии:

Глобально

Переопределение группы процессов в OneAgent

Пространство имён Kubernetes

1. Перейдите в **Settings** и выберите **Preferences** > **OneAgent features**.
2. Отфильтруйте по **enrichment**.
3. Включите/отключите обогащение журналов для каждой технологии, которую вы используете для генерации принятых данных журналов.
4. Выберите **Save changes**, чтобы сохранить конфигурацию.

1. Откройте группу процессов, которую вы ищете.
2. Выберите **More** (**…**) > **OneAgent features**.
3. Отфильтруйте по **enrichment**.
4. Включите/отключите обогащение журналов для каждой технологии, которую вы используете для генерации принятых данных журналов.
5. Выберите **Save changes**, чтобы сохранить конфигурацию.

1. Перейдите в ![Kubernetes (new)](https://dt-cdn.net/images/kubernetes-new-1024-45d3de15d1.webp "Kubernetes (new)") **Kubernetes** > **Namespaces**.
2. Выберите интересующую вас запись пространства имён.
3. В заголовке пространства имён выберите > **Anomaly detection settings**.
4. Закройте оверлей и выберите **Collect and capture** > **OneAgent features**.
5. Выберите **Add override**.
6. Выберите технологию обогащения журналов из раскрывающегося списка **Feature** и убедитесь, что переключатель переопределения функции включён.
7. Выберите **Save and close**.

### Что делает автоматическое обогащение журналов?

Обогащение журналов изменяет принятые данные журналов и добавляет следующую информацию к каждой обнаруженной записи журнала:

* `dt.trace_id`
* `dt.span_id`
* `dt.entity.process_group_instance`

## Поддерживаемые фреймворки

Полный список фреймворков логирования, поддерживающих автоматическое обогащение контекста трейсов/спанов в журналах, см. на странице [Поддержка технологий](../../ingest-from/technology-support.md#web-servers "Найдите технические подробности о поддержке Dynatrace для конкретных платформ и фреймворков разработки.").

## Структурированные данные журналов

Для структурированных данных журналов, таких как JSON, XML и хорошо определённые текстовые форматы журналов, Dynatrace добавляет поле атрибута в запись журнала.

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

Перед использованием автоматического обогащения журналов на неструктурированных данных проверьте, влияет ли обогащение журналов Dynatrace на существующий конвейер данных журналов.

Чтобы избежать обогащения журналов из тестовых или симуляционных запусков, рекомендуется исключить процессы, содержащие `--dry-run`. Например, сервер приложений Payara использует стартовые скрипты с такими dry run, и сервер может не запуститься корректно, если это исключение не установлено.

Неструктурированные данные журналов обычно представляют собой необработанный простой текст в последовательном порядке, предназначенный для чтения людьми. Dynatrace не обогащает неструктурированные данные журналов автоматически. Dynatrace способен обогащать неструктурированные данные журналов, но добавление дополнительной информации к данным журналов может повлиять на сторонние инструменты, которые потребляют те же данные журналов.

### Пример обогащённых данных журнала в формате необработанного текста

Данные журнала в необработанном тексте обогащаются дополнительной строкой `[!dt dt.trace_id=$trace_id, dt.span_id=$span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]` (атрибуты и их значения).

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=aa764ee37ebaa764ee37eaa764ee37e,dt.span_id=b93ede8b93ede8, dt.entity.process_group_instance=PROCESS_GROUP_INSTANCE-27204EFED3D8466E]
```

## Ручное обогащение журналов

OneAgent версии 1.239+

Вы можете вручную обогащать принятые данные журналов Dynatrace, определив шаблон журнала для включения полей `dt.span_id`, `dt.trace_id`, `dt.trace_sampled` и `dt.entity.process_group_instance`. Вы можете включить ручное обогащение журналов для конкретной технологии, следуя [инструкциям по обогащению журналов](lma-log-enrichment.md#enableenr "Подключите входящие данные журналов к трейсам для более точного анализа Dynatrace.").

Убедитесь, что соблюдаете следующие правила для формата обогащённых полей в неструктурированном журнале:

* Поля должны быть заключены в квадратные скобки (`[]`) с префиксом `!dt`.
  Например, `[!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id, dt.entity.process_group_instance=$dt.entity.process_group_instance]`
* Поля должны быть отформатированы без двойных кавычек.
* Все недопустимые символы в поле и значении поля должны быть экранированы.
* Управляющие символы, такие как `\n`, должны быть исключены из определения обогащения.

### Пример ручного обогащения данных журнала NGINX

Предположим, вы хотите вручную обогатить данные журнала NGINX значениями `dt.trace_id`, `dt.span_id` и `dt.trace_sampled`. Файл конфигурации NGINX содержит множество стандартных переменных NGINX; определение формата журнала должно находиться в разделе `log_format`. Например:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$dt_trace_id,dt.span_id=$dt_span_id,dt.trace_sampled=$dt_trace_sampled]';


access_log logs/access.log custom;
```

В результате файл `access.log` будет содержать обогащённые записи журнала:

```
127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=b9e5c9ec08be5fab5071d76f427be7da,dt.span_id=43c5bb9432593963,dt.trace_sampled=true]


127.0.0.1 - [22/Mar/2022:08:50:45 +0100] GET /index.htm HTTP/1.1 200 30 [!dt dt.trace_id=01e52950b145d97bf22345e68c5e6c58,dt.span_id=de819d856eecb236,dt.trace_sampled=true]
```

Для OneAgent версии 1.237 и более ранних используются другие переменные NGINX. Например:

```
log_format custom '$remote_addr - [$time_local] $request $status $body_bytes_sent [!dt dt.trace_id=$trace_id,dt.span_id=$span_id]'; access_log logs/access.log custom
```

В результате файл `access.log` будет содержать обогащённые записи журнала:

```
127.0.0.1 - [21/Oct/2021:10:33:28 +0200] GET /index.htm HTTP/1.1 404 597 [!dt dt.trace_id=e1c0afeb0b8a91d7748139aa764ee37e,dt.span_id=e5e6748fab93ede8]


127.0.0.1 - [21/Oct/2021:10:33:31 +0200] GET /index.html HTTP/1.1 200 1056 [!dt dt.trace_id=81fe7816ba6c38f7aa09aef3684cd941,dt.span_id=3bdacc466ae073cd]
```

Если вы используете фреймворк логирования и форматтер журналов, допускающий пользовательские шаблоны журналов, вы можете адаптировать шаблон в форматтере журналов и напрямую обращаться к атрибутам обогащения Dynatrace.

### Пример ручного обогащения данных журнала Log4j

В **Log4j** PatternFormatter вы можете указать следующий шаблон для включения информации обогащения Dynatrace:

```
<PatternLayout pattern="%d{HH:mm:ss.SSS} [%t] %-5level %logger{36} dt.trace_id=%X{dt.trace_id} dt.span_id=%X{dt.span_id} dt.entity.process_group_instance=%X{dt.entity.process_group_instance} - %msg%n"/>
```

### Пример ручного обогащения энкодера Logstash Logback

Logback — преемник проекта log4j. Logstash Logback — расширение, предоставляющее энкодеры, компоновщики и аппендеры для logback для записи в JSON и других форматах, поддерживаемых Jackson.

Ниже приведён пример ручного обогащения с использованием энкодера Logstash. Обратите внимание на дополнительное свойство `mdc` в файле конфигурации, где можно включить переменные MDC.

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

### Пример ручного обогащения данных журнала .NET Serilog

В .NET Serilog вы можете настроить выходные шаблоны для текстовых приёмников, например консоли или файловых приёмников, чтобы включить информацию обогащения Dynatrace.

```
{Timestamp:yyyy-MM-dd HH:mm:ss.fff zzz} [{Level:u3}] [!dt dt.trace_id={trace_id}, dt.span_id={span_id}, dt.trace_sampled={trace_sampled}] {Message:lj}{NewLine}{Exception}
```

## NGINX ingress с Kubernetes

Вы можете обогащать журналы с помощью NGINX ingress с Kubernetes в два шага:

1. Выполните инструкции по инструментированию [ingress-nginx на Kubernetes](../../ingest-from/setup-on-k8s/guides/deployment-and-configuration/monitoring-and-instrumentation/instrument-nginx.md "Инструментирование ingress-nginx на Kubernetes").
2. Добавьте приведённую ниже команду в файл `configmap.yaml` для NGINX ingress.

   Добавление строки `main-snippet` включает приём данных OneAgent и является необязательным, если вы уже следовали инструкциям по ручному инструментированию.

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

## Получение идентификаторов спана и трейса

Чтобы Dynatrace сопоставлял журналы с соответствующими трейсами, вы можете включать идентификаторы спана и трейса в сообщения журналов, используя нотацию `[!dt]`.

Следующие примеры показывают, как получить идентификаторы спана и трейса с помощью OpenTelemetry или OneAgent SDK:

Python с OpenTelemetry

JavaScript (Node.js) с OpenTelemetry

Java с OpenTelemetry

Go с OneAgent SDK

В примере ниже создана функция `dt_log` для обогащения заданного сообщения журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в настроенный приёмник журналов связывает сообщение журнала с текущим активным спаном в веб-интерфейсе Dynatrace.

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

В примере ниже создана функция `dt_log` для обогащения заданного сообщения журнала информацией `trace_id` и `span_id`. Вывод этого обогащённого сообщения в `stdout` связывает сообщение журнала с текущим активным спаном в веб-интерфейсе Dynatrace.

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

В примере ниже создан метод `dtLog` для обогащения заданного сообщения журнала информацией `TraceId` и `SpanId`. Вывод этого обогащённого сообщения через `System.out` связывает сообщение журнала с текущим активным спаном в веб-интерфейсе Dynatrace.

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

В примере ниже HTTP-обработчик использует `Printf()` для записи ответа в стандартный вывод и обогащает эту информацию идентификаторами трейса и спана, полученными из `oneagentsdk.GetTraceContextInfo()`. Вывод этого обогащённого сообщения связывает сообщение журнала с текущим активным спаном в веб-интерфейсе Dynatrace.

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

Подробнее о конфигурации см. в разделе [Журналы AWS Lambda в контексте трейсов](../../ingest-from/amazon-web-services/integrate-into-aws/aws-lambda-integration/aws-lambda-classic/opentelemetry-interoperability/log-enrichment.md "Настройка обогащения сообщений журналов с помощью OpenTelemetry на AWS Lambda.").

Инструкции по получению этих атрибутов через OneAgent SDK:

* **Go:** см. [документацию GO на GitHub](https://github.com/Dynatrace/OneAgent-SDK-for-Go)
* **.NET:** см. [документацию .NET на GitHub](https://github.com/Dynatrace/OneAgent-SDK-for-dotnet#trace-context)

## Получение идентификатора экземпляра группы процессов

Вы можете получить поле `dt.entity.process_group_instance` с помощью команды Python OpenTelemetry, содержащей `merged`. `process_group_instance` извлекается как один из атрибутов, доступных в `merged`, как показано в примере ниже:

С OneAgent вы можете просто указать локальную конечную точку без токена аутентификации для включения приёма трейсов.

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

При использовании OneAgent убедитесь, что публичный [Extension Execution Controller](../../ingest-from/extensions/concepts.md#eec "Узнайте больше о концепции расширений Dynatrace.") включён в настройках Dynatrace, иначе данные не будут отправлены.

Перейдите в **Settings** > **Preferences** > **Extension Execution Controller**. Переключатели **Enable Extension Execution Controller** и **Enable local PIPE/HTTP metric and Log Ingest API** должны быть активны.

Подробнее о конфигурации см. в разделе [Инструментирование приложения Python с помощью OpenTelemetry](../../ingest-from/opentelemetry/walkthroughs/python.md "Узнайте, как инструментировать приложение Python с помощью OpenTelemetry и Dynatrace.")

## Ограничения

Если вы используете пользовательский форматтер/транспорт winston (применимо только к Node.js), вам необходимо вручную добавить внедрённые `dt.traceId` и `dt.spanId`, как показано в примере ниже:

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

## Связанные темы

* [Использование обогащения журналов для трейсов при решении проблем](../../observe/application-observability/distributed-traces/use-cases/problems-logs-traces.md "Используйте обогащение журналов для просмотра связанных записей журналов в представлении распределённых трейсов и расширения аналитических возможностей.")
* [Автоматическое обогащение журналов](lma-log-ingestion/lma-log-ingestion-via-oa/lma-log-data-transformation-oa.md "Общий приём журналов автоматически преобразует данные журналов в выходные значения для атрибута loglevel.")
